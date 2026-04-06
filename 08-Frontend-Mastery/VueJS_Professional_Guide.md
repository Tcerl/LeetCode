# 🖖 VUEJS 3: NÂNG TẦM FRONTEND ARCHITECT

Để xây dựng một giao diện người dùng (UI) mạnh mẽ như **NexusFlow**, bạn không thể chỉ dùng VueJS cơ bản. Bạn cần làm chủ **Composition API**, **Pinia** và cách xây dựng hệ thống **Reusable Components**.

---

## 📋 MỤC LỤC

1.  **[Script Setup: Cú pháp "tinh gọn" của Vue 3](#1-script-setup-cu-phap-tinh-gon-cua-vue-3)**
2.  **[Composables: Bí mật của việc tái cấu trúc logic](#2-composables-bi-mat-cua-viec-tai-cau-truc-logic)**
3.  **[Pinia: Quản lý "Trạng thái" tập trung như một Pro](#3-pinia-quan-ly-trang-thai-tap-trung-nhu-mot-pro)**
4.  **[Advanced UI Patterns: Scoped Slots & Teleport](#4-advanced-ui-patterns-scoped-slots--teleport)**
5.  **[Performance Optimization: Vite, Lazy Loading & v-memo](#5-performance-optimization-vite-lazy-loading--v-memo)**
6.  **[JavaScript Master: Event Loop & Microtasks](#6-javascript-master-event-loop--microtasks)**
7.  **[Vue 3 Internals: Sức mạnh của Proxy](#7-vue-3-internals-suc-manh-cua-proxy)**
8.  **[Enterprise Authentication: Bảo mật Fullstack JWT](#8-enterprise-authentication-bao-mat-fullstack-jwt)**
9.  **[Next Step: Nuxt 3 & SEO Mastery](#9-next-step-nuxt-3--seo-mastery)**
10. **[Clean UI Architecture: Atomic Design Pattern](#10-clean-ui-architecture-atomic-design-pattern)**
11. **[Mastering Components: Provide/Inject & Renderless](#11-mastering-components-provideinject--renderless)**

---

## ✨ 1. `<script setup>`: Cú pháp tinh gọn

Đừng dùng Options API lỗi thời. Hãy dùng `script setup` để code ngắn hơn phân nửa.

*   **Junior (Options API):**
    ```javascript
    export default {
        data() { return { count: 0 } },
        methods: { increment() { this.count++ } }
    }
    ```
*   **Senior (Script Setup):**
    ```vue
    <script setup>
    import { ref } from 'vue'
    const count = ref(0)
    const increment = () => count.value++
    </script>
    ```

---

## 🛠️ 2. Composables: "Vũ khí" tái sử dụng logic

Thay vì viết cùng một đoạn code xử lý API hay Tọa độ chuột ở 10 component khác nhau, hãy tách nó ra.

### Cách viết một Composable chuyên nghiệp (`useMouse.js`):
```javascript
import { ref, onMounted, onUnmounted } from 'vue'

export function useMouse() {
    const x = ref(0)
    const y = ref(0)
    const update = e => { x.value = e.pageX; y.value = e.pageY }
    onMounted(() => window.addEventListener('mousemove', update))
    onUnmounted(() => window.removeEventListener('mousemove', update))
    return { x, y }
}

// Tại Component bất kỳ:
// const { x, y } = useMouse()
```

---

## 🍍 3. Pinia: Quản lý trung tâm của hệ thống

Pinia thay thế Vuex, cung cấp cách quản lý dữ liệu (User, Token, Cấu hình) cực kỳ dễ hiểu.

### Logic của Chuyên gia:
Đừng sửa trực tiếp `state`, hãy dùng `actions` để mọi thứ minh bạch.

```javascript
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
    state: () => ({ name: 'Nexus User', isAdmin: false }),
    actions: {
        login(name) { this.name = name },
        logout() { this.name = '' }
    },
    getters: {
        welcomeMessage: (state) => `Chào mừng, ${state.name}!`
    }
})
```

---

## 🎭 4. Advanced UI Patterns

### A. Scoped Slots (Khe cắm phạm vi)
Cho phép Component CHA truyền giao diện nhưng Component CON quyết định dữ liệu.
```vue
<!-- Component Con: MyList.vue -->
<slot :item="data"></slot> 

<!-- Component Cha: App.vue -->
<MyList v-slot="{ item }">
    <div class="pro-card">{{ item.name }}</div>
</MyList>
```

### B. Teleport (Dịch chuyển tức thời)
Đưa các Modal, Popup ra ngoài cấu trúc HTML hiện tại (lên thẳng thẻ `<body>`) để tránh lỗi CSS `z-index`.
```vue
<Teleport to="body">
    <div class="modal">NexusFlow Alert</div>
</Teleport>
```

---

## 🚀 5. Performance Optimization: Bí mật của tốc độ

Khi hiển thị hàng triệu dòng dữ liệu thị trường trong NexusFlow:

1.  **`v-memo`:** Chỉ render lại khi dữ liệu thay đổi thực sự.
2.  **Lazy Loading Components:**
    ```javascript
    const AsyncComponent = defineAsyncComponent(() => import('./HeavyComponent.vue'))
    ```
3.  **Vite Build:** Tách file (Code splitting) để người dùng không phải tải một cục file JS khổng lồ.

---

## 🧠 6. JAVASCRIPT MASTER: EVENT LOOP & MICROTASKS

Tại sao `nextTick()` trong Vue lại quan trọng? Vì cách JS xử lý thứ tự thực thi:

1.  **Call Stack:** Nơi thực thi code đồng bộ.
2.  **Micotasks (Promise):** Ưu tiên chạy ngay sau khi stack trống.
3.  **Task Queue (SetTimeout):** Chạy cuối cùng sau khi Microtasks xong.

**Expert Insight:** Vue cập nhật giao diện (DOM) ở bước **Microtask**. Nếu bạn muốn truy cập phần tử DOM vừa thay đổi, bạn phải dùng `await nextTick()`.

---

## 🧙 7. VUE 3 INTERNALS: SỨC MẠNH CỦA PROXY

Vue 3 nhanh hơn Vue 2 vì nó dùng **ES6 Proxy** thay vì `Object.defineProperty`.

### Logic của Proxy:
Nó tạo ra một "phiên bản" ảo của object ban đầu. Khi bạn thay đổi giá trị, Proxy sẽ "Bắt lấy" (Trap) hành động đó và thông báo cho Vue để cập nhật giao diện mà không cần quét toàn bộ object.

```javascript
const user = { name: "Nexus" };
const proxyUser = new Proxy(user, {
    set(target, key, value) {
        console.log(`Đang thay đổi ${key} thành ${value}`);
        target[key] = value;
        // Kích hoạt re-render giao diện ở đây!
        return true;
    }
});
```

---

## 🔐 8. ENTERPRISE AUTHENTICATION: BẢO MẬT FULLSTACK JWT

Làm sao VueJS giao tiếp an toàn với Python Backend? Câu trả lời là **JWT (JSON Web Token)**.

### Quy trình tích hợp chuyên nghiệp:
1.  **Vue** gửi mật khẩu lên **Python**.
2.  **Python** trả về 2 loại token: `access_token` (ngắn hạn) và `refresh_token` (dài hạn).
3.  **Vue** lưu token vào **HttpOnly Cookies** (bảo mật nhất) hoặc Pinia.
4.  **Axios Interceptors:** Tự động đính kèm token vào mọi request gửi lên AWS.

```javascript
// Axios Interceptor ví dụ
axios.interceptors.request.use(config => {
    config.headers.Authorization = `Bearer ${token}`
    return config
})
```

---

## 🚀 9. NEXT STEP: NUXT 3 & SEO MASTERY

Khi ứng dụng NexusFlow của bạn quá lớn và cần được tìm kiếm trên Google (SEO), bạn phải dùng **Nuxt 3 (SSR)**.

*   **SSR (Server Side Rendering):** Server sẽ render HTML trước khi gửi xuống trình duyệt. Google Bot sẽ thấy web của bạn ngay lập tức.
*   **Auto-imports:** Nuxt tự động import mọi component và composable giúp bạn không cần viết hàng trăm dòng `import`.
*   **Performance:** Nuxt có cơ chế tối ưu hóa hình ảnh và code splitting mạnh mẽ hơn Vue thuần.

---

## 🏗️ 10. CLEAN UI ARCHITECTURE: ATOMIC DESIGN PATTERN

Đừng để thư mục `components/` của bạn như một nồi lẩu. Hãy chia theo triết lý hóa học:

1.  **Atoms (Nguyên tử):** Các thành phần cơ bản (Button, Input, Icon).
2.  **Molecules (Phân tử):** Kết hợp các nguyên tử (vd: Search Bar = Input + Button).
3.  **Organisms (Cơ quan):** Các khối giao diện lớn (Header, Footer, Product Card).
4.  **Templates (Mẫu):** Bố cục của trang (vd: Dashboard Layout).
5.  **Pages (Trang):** Liên kết các template với dữ liệu thực tế từ API.

**Lợi ích:** Hệ thống Design System cho NexusFlow sẽ cực kỳ nhất quán và dễ thay đổi giao diện toàn bộ website trong 5 phút.

---

## 🧙 11. MASTERING COMPONENTS: PROVIDE/INJECT & RENDERLESS

Nâng cao trình độ viết component để phục vụ các dự án khổng lồ.

### A. Provide/Inject (Thắp sáng cho con cháu)
Thay vì truyền Props qua 5 tầng component (Prop Drilling), hãy "Cung cấp" dữ liệu từ GỐC và con cháu tự "Lấy" về.
```javascript
// Cha: 
provide('theme', 'dark')

// Cháu 5 đời: 
const theme = inject('theme')
```

### B. Renderless Components (Component "Vô tướng")
Đây là kỹ thuật viết Component chỉ lo phần **XỬ LÝ DỮ LIỆU** và trả lại giao diện cho người dùng tự quyết định (sử dụng Scoped Slots).

```vue
<!-- Compoent "Logic": FetchData.vue -->
<template>
  <slot :data="result" :loading="isLoading"></slot>
</template>
```

---
🎯 **Thực hành ngay cho NexusFlow:**
*   Sử dụng **Pinia** để lưu trữ Token đăng nhập của khách hàng.
*   Viết **Composable `useFetch`** để tự động xử lý loading/error khi gọi API từ Python Backend.
*   Dùng **Vite** để build frontend chỉ trong 5 giây.
