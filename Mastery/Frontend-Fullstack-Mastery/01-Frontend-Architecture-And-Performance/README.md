# 01. Kiến Trúc Frontend & Hiệu Năng (Góc nhìn Senior)

> Lý thuyết Vue 3 chi tiết đã có ở [`VueJS_Professional_Guide.md`](../../../08-Frontend-Mastery/VueJS_Professional_Guide.md) (Composition API, Proxy internals, Event Loop mục 6-7) và các bài Deep Dive trong [`CODE_EXERCISES.md`](../../../06-Exercises/CODE_EXERCISES.md) (Proxy vs `Object.defineProperty`, SSR Hydration). File này nối các mảnh đó thành **bức tranh vận hành thật của trình duyệt + framework**.

---

## 1. Vì sao Vue 3 dùng Proxy — không chỉ là "mới hơn nên tốt hơn"

`Object.defineProperty` (Vue 2) chỉ can thiệp được vào **property đã tồn tại sẵn** trên object — đây là lý do Vue 2 cần `Vue.set()`/`this.$set()` để thêm reactivity cho property mới, và **không** phát hiện được khi thêm/xóa phần tử mảng qua index (`arr[0] = x`) hay `arr.length = 0`.

`Proxy` (Vue 3) bọc toàn bộ object, chặn được **mọi** thao tác get/set/delete kể cả property động — giải quyết dứt điểm các hạn chế trên mà không cần API đặc biệt.

**Ứng dụng thực tế senior cần biết:** hiểu cơ chế Proxy giải thích được lý do 1 bug reactivity kinh điển:

```javascript
// ❌ Destructuring phá vỡ reactivity — mất kết nối Proxy
const { count } = reactive({ count: 0 })
count++ // KHÔNG trigger re-render — count giờ chỉ là số nguyên thường, không còn Proxy

// ✅ Đúng cách — dùng toRefs để giữ reactivity khi destructure
import { reactive, toRefs } from 'vue'
const state = reactive({ count: 0 })
const { count } = toRefs(state)
count.value++ // Đúng — vẫn giữ liên kết reactive
```

Đây là bug xảy ra RẤT thường xuyên khi dev quen React (không có khái niệm reactive object) chuyển sang Vue — không hiểu cơ chế Proxy thì chỉ "thử random" cho tới khi hết bug, không debug có hệ thống được.

---

## 2. Event Loop: Microtask vs Macrotask — quyết định thứ tự cập nhật UI

```javascript
console.log('1')
setTimeout(() => console.log('2'), 0)     // Macrotask
Promise.resolve().then(() => console.log('3'))  // Microtask
console.log('4')
// Thứ tự in ra: 1, 4, 3, 2 — vì TOÀN BỘ microtask queue được xử lý
// TRƯỚC khi engine lấy task tiếp theo từ macrotask queue
```

**Vì sao senior phải hiểu điều này:** Vue's `nextTick()` và React's batched updates đều dựa trên microtask queue để **gom nhiều thay đổi state thành 1 lần re-render** thay vì render lại DOM sau mỗi dòng code thay đổi state — đây chính là lý do framework UI hiện đại mượt hơn nhiều so với thao tác DOM trực tiếp (jQuery-style). Khi debug "vì sao DOM chưa cập nhật ngay sau khi đổi state", câu trả lời luôn nằm ở đây: `await nextTick()` để đợi đúng chu kỳ update.

---

## 3. Performance thực chiến — vấn đề thật khi UI có hàng nghìn item

Đã có kỹ thuật Virtual List trong [`CODE_EXERCISES.md` (VUE-09)](../../../06-Exercises/CODE_EXERCISES.md). Bổ sung góc nhìn **tại sao vấn đề này có thật**:

- **DOM node càng nhiều, reflow/repaint càng chậm** — render 10,000 item cùng lúc trong `<table>` có thể làm trình duyệt đơ vài giây, đặc biệt trên thiết bị di động yếu.
- **Virtual List (Windowing)** chỉ render các item **đang nằm trong viewport** (+ buffer nhỏ), tái sử dụng DOM node khi cuộn — đây là kỹ thuật bắt buộc cho bảng dữ liệu lớn (dashboard admin, bảng giao dịch tài chính, chat có hàng nghìn tin nhắn).
- **`v-memo` / `React.memo`:** tránh re-render component con khi props không đổi — bẫy thường gặp: truyền object/array literal trực tiếp làm prop (`:config="{a: 1}"`) tạo ra reference MỚI mỗi lần render cha, làm memo vô tác dụng vì so sánh reference luôn thấy khác nhau.

```javascript
// ❌ Object literal mới mỗi lần render → memo/computed cache bị vô hiệu hóa
<ChildComponent :config="{ theme: 'dark' }" />

// ✅ Định nghĩa 1 lần bên ngoài render, hoặc dùng computed
const config = { theme: 'dark' }  // ngoài render scope, reference ổn định
```

---

## 4. SSR Hydration — "tại sao console báo mismatch mà tôi không sửa gì"

Đã có cơ chế chi tiết ở [`CODE_EXERCISES.md` (SSR Hydration Deep Dive)](../../../06-Exercises/CODE_EXERCISES.md). Bổ sung sự cố thật hay gặp:

**Hydration mismatch** xảy ra khi HTML server render ra **khác** với HTML client render lần đầu — nguyên nhân phổ biến nhất trong thực tế: dùng `Date.now()`, `Math.random()`, hoặc `window`/`localStorage` (chỉ tồn tại ở client) ngay trong lúc render, khiến server và client tính ra giá trị khác nhau. Giải pháp senior: những giá trị phụ thuộc môi trường client phải được set **sau khi mount** (`onMounted`), không tính trực tiếp trong template/render function.

---

## 🎯 Câu hỏi senior hay hỏi khi review

1. "Component này re-render bao nhiêu lần khi user gõ 1 ký tự vào ô tìm kiếm — có cần debounce/memo không?"
2. "Bảng dữ liệu này có thể tới hàng chục nghìn dòng không? Nếu có, đã dùng virtual scroll chưa?"
3. "Nếu bật SSR, phần nào của component này phụ thuộc `window`/thời gian thực và có thể gây hydration mismatch?"

## 🔗 Liên kết module khác
- Quản lý state tập trung (Pinia) & data fetching → [`02-State-Management-And-Data-Fetching`](../02-State-Management-And-Data-Fetching/README.md)
- API mà frontend gọi tới được thiết kế ra sao ở backend → [`../Backend-Mastery/01`](../../Backend-Mastery/01-Request-Lifecycle-And-Architecture/README.md)
