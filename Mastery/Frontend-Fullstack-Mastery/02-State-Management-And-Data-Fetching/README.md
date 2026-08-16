# 02. Quản Lý State & Giao Tiếp API (Góc nhìn Senior)

> Lý thuyết Pinia, Axios Interceptor, JWT đã có ở [`CODE_EXERCISES.md`](../../06-Exercises/CODE_EXERCISES.md) (PINIA-01, PINIA-02, API-01) và [`VueJS_Professional_Guide.md`](../../08-Frontend-Mastery/VueJS_Professional_Guide.md) mục 8. File này bổ sung **tại sao thiết kế theo cách đó, và sự cố thật khi thiết kế sai**.

---

## 1. Khi nào cần global state (Pinia/Vuex), khi nào chỉ cần props/composable

**Sai lầm phổ biến của dev mới:** đưa MỌI state vào Pinia store "cho tiện" — dẫn tới store phình to, khó theo dõi state nào ảnh hưởng bởi component nào, và làm mất tính cục bộ (component không còn tái sử dụng độc lập được vì phụ thuộc cứng vào store toàn cục).

| Loại state | Nơi nên đặt | Vì sao |
|---|---|---|
| State chỉ 1 component dùng (VD: form đang mở/đóng) | `ref()`/`reactive()` local trong component | Không cần chia sẻ, đặt global chỉ làm rối |
| State chia sẻ giữa vài component gần nhau (cha-con) | Props xuống + Emit lên, hoặc `provide/inject` | Đủ dùng, không cần store |
| State toàn ứng dụng thật sự (user đăng nhập, giỏ hàng, theme) | Pinia store | Cần truy cập từ nhiều nơi không liên quan trực tiếp |
| Logic tái sử dụng nhưng KHÔNG cần chia sẻ state giữa các instance | Composable (`useFetch`, `useDebounce`) | Mỗi component gọi composable có state RIÊNG, khác với store (state DÙNG CHUNG) |

**Bẫy hay gặp:** nhầm composable với store — gọi `useCounter()` ở 2 component khác nhau, mỗi component có `count` **độc lập** (không đồng bộ), trong khi dev tưởng chúng chia sẻ chung 1 state như Pinia store.

---

## 2. Axios Interceptor + JWT Refresh — pattern production thật, không chỉ demo

Đã có code mẫu ở [`CODE_EXERCISES.md` (API-01)](../../06-Exercises/CODE_EXERCISES.md). Bổ sung các case biên senior phải xử lý:

```javascript
// Vấn đề thật: NHIỀU request cùng lúc gặp 401 (token hết hạn) →
// nếu không kiểm soát, sẽ gọi refresh-token NHIỀU LẦN đồng thời (race condition),
// có thể làm server revoke nhầm token hoặc tạo ra nhiều token refresh chồng chéo.
let isRefreshing = false
let failedQueue = []

function processQueue(error, token = null) {
  failedQueue.forEach(p => error ? p.reject(error) : p.resolve(token))
  failedQueue = []
}

axiosInstance.interceptors.response.use(
  response => response,
  async (error) => {
    const originalRequest = error.config
    if (error.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        // Các request khác đang chờ TỚI KHI refresh hoàn tất, không gọi refresh trùng lặp
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject })
        }).then(token => {
          originalRequest.headers.Authorization = `Bearer ${token}`
          return axiosInstance(originalRequest)
        })
      }
      originalRequest._retry = true
      isRefreshing = true
      try {
        const newToken = await refreshAccessToken()
        processQueue(null, newToken)
        originalRequest.headers.Authorization = `Bearer ${newToken}`
        return axiosInstance(originalRequest)
      } catch (refreshError) {
        processQueue(refreshError, null)
        redirectToLogin()  // refresh token cũng hết hạn — bắt buộc đăng nhập lại
        return Promise.reject(refreshError)
      } finally {
        isRefreshing = false
      }
    }
    return Promise.reject(error)
  }
)
```

**Đây chính là bug thật rất hay gặp khi test thủ công không phát hiện ra** (vì tay chỉ bấm 1 request tại 1 thời điểm) nhưng xảy ra ngay khi trang có nhiều API call song song lúc load (dashboard gọi 5 API cùng lúc, token hết hạn đúng lúc đó).

---

## 3. Nơi lưu token — tradeoff bảo mật thật, không có đáp án hoàn hảo

| Nơi lưu | Ưu điểm | Rủi ro |
|---|---|---|
| `localStorage` | Đơn giản, tồn tại qua lần reload | **Dễ bị đánh cắp qua XSS** — bất kỳ script độc hại nào chèn được vào trang đều đọc được toàn bộ localStorage |
| `httpOnly Cookie` | JavaScript KHÔNG đọc được → an toàn hơn trước XSS | Cần phòng **CSRF** riêng (SameSite cookie attribute, CSRF token) |
| Memory (biến JS, mất khi reload) | An toàn nhất trước cả XSS lẫn CSRF nếu kết hợp đúng | UX kém hơn (phải re-auth khi F5), cần thêm refresh token ở httpOnly cookie để khôi phục session |

**Khuyến nghị senior cho hệ thống thật sự quan tâm bảo mật:** access token ngắn hạn giữ trong memory, refresh token dài hạn đặt trong httpOnly cookie + `SameSite=Strict` — kết hợp ưu điểm của cả 2, đây là pattern các ngân hàng/fintech thường dùng.

---

## 🎯 Câu hỏi senior hay hỏi khi review

1. "State này có thật sự cần global không, hay chỉ đang 'tiện tay' đưa vào store?"
2. "Nếu 5 API call đồng thời đều gặp 401, interceptor của bạn có gọi refresh-token 5 lần không?"
3. "Token đang lưu ở đâu — bạn đã cân nhắc rủi ro XSS/CSRF tương ứng chưa?"

## 🔗 Liên kết module khác
- Reactivity nền tảng đứng sau Pinia → [`01-Frontend-Architecture-And-Performance`](../01-Frontend-Architecture-And-Performance/README.md)
- API backend phát hành/verify JWT thế nào → [`../Backend-Mastery/01`](../../Backend-Mastery/01-Request-Lifecycle-And-Architecture/README.md)
