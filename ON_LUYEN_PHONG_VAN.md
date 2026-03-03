# 🚀 ÔN LUYỆN PHỎNG VẤN – Vue.js + Laravel Fullstack (Nâng Cao)

> **Vị trí:** Frontend (Vue.js / Nuxt.js) | Fullstack (Vue.js + Laravel) | Cập nhật: 2026-03-03

---

## 📋 MỤC LỤC

| # | Chủ đề | Độ ưu tiên |
|---|---|---|
| [1](#1-vuejs-core--nâng-cao) | Vue.js Core & Nâng Cao | ⭐⭐⭐⭐⭐ |
| [2](#2-pinia--vuex) | Pinia / Vuex | ⭐⭐⭐⭐⭐ |
| [3](#3-component-patterns--performance) | Component Patterns & Performance | ⭐⭐⭐⭐ |
| [4](#4-nuxtjs--ssr--seo) | Nuxt.js + SSR + SEO | ⭐⭐⭐⭐ |
| [5](#5-figma--code) | Figma → Code (CSS Tokens + Responsive) | ⭐⭐⭐ |
| [6](#6-laravel-framework--nâng-cao) | Laravel Framework & Nâng Cao | ⭐⭐⭐⭐⭐ |
| [7](#7-restful-api--bảo-mật) | RESTful API + JWT + Bảo Mật | ⭐⭐⭐⭐ |
| [8](#8-câu-hỏi-phỏng-vấn--đáp-án-chi-tiết) | Q&A Phỏng Vấn Chi Tiết | ⭐⭐⭐⭐⭐ |
| [9](#9-performance--security-checklist) | Performance & Security Checklist | ⭐⭐⭐⭐ |
| [10](#10-checklist--lộ-trình) | Checklist & Lộ Trình | — |

---

## 1. Vue.js Core & Nâng Cao

> 💡 **Vue 3 dùng Proxy** (khác Vue 2 dùng `Object.defineProperty`) → track dynamic properties, array mutations tự động reactive.

### 1.1 Reactivity System – Hiểu Sâu

```javascript
import { ref, reactive, computed, watch, watchEffect, toRefs, shallowRef, markRaw } from 'vue'

// ── ref: primitive + object, cần .value ──────────────
const count = ref(0)
const user  = ref({ name: 'Tín', age: 25 })
count.value++
user.value.name = 'Duy'  // ✅ reactive

// ── reactive: object/array, không cần .value ─────────
const state = reactive({ name: 'Tín', address: { city: 'HCM' } })
state.name = 'Bảo'           // ✅ reactive
state.address.city = 'HN'   // ✅ deep reactive

// ⚠️ QUAN TRỌNG: Mất reactivity khi destructure reactive
const { name } = state          // ❌ name là string thường
const { name } = toRefs(state)  // ✅ name.value vẫn reactive

// ── shallowRef: chỉ track cấp 1 (hiệu năng tốt cho big object) ──
const bigList = shallowRef([])   // Chỉ reactive khi replace: bigList.value = []
// bigList.value.push(x) → KHÔNG trigger update

// ── markRaw: không track (Chart.js, Map, 3rd-party objects) ──
const chart = shallowRef(markRaw(new SomeHeavyClass()))

// ── computed: cache, chỉ tính lại khi dependency thay đổi ──
const fullName = computed(() => `${state.name} Việt`)

// computed writable
const fullName2 = computed({
  get: () => `${state.first} ${state.last}`,
  set: (val) => {
    const [first, last] = val.split(' ')
    state.first = first
    state.last  = last
  }
})
```

---

### 1.2 watch vs watchEffect

```javascript
// watch – explicit source, LAZY (không chạy ngay)
watch(count, (newVal, oldVal) => {
  console.log(`${oldVal} → ${newVal}`)
}, {
  immediate: true,  // Chạy ngay lần đầu
  deep: true,       // Watch deep object changes
  flush: 'post',    // Chạy SAU khi DOM update
  once: true,       // Vue 3.4+: chỉ chạy 1 lần
})

// watch nhiều sources
watch([count, name], ([newCount, newName], [oldCount, oldName]) => {
  console.log(newCount, newName)
})

// watchEffect – auto track dependency, EAGER (chạy ngay lần đầu)
const stop = watchEffect(() => {
  console.log('count is:', count.value)  // Tự track count
  console.log('name is:', user.value.name)  // Tự track user.value.name
})
stop()  // Dừng watch thủ công

// watchEffect cleanup (abort fetch khi re-run)
watchEffect((onCleanup) => {
  const controller = new AbortController()
  fetch('/api/data', { signal: controller.signal })
  onCleanup(() => controller.abort())  // Cleanup trước khi re-run
})
```

> **🔑 Nhớ:** `watch` = cần biết oldVal/newVal, lazy. `watchEffect` = auto deps, eager (chạy ngay lần đầu).

---

### 1.3 Lifecycle Hooks – Đầy Đủ

```javascript
import {
  onBeforeMount, onMounted,
  onBeforeUpdate, onUpdated,
  onBeforeUnmount, onUnmounted,
  onErrorCaptured, onActivated, onDeactivated
} from 'vue'

onMounted(() => {
  // ✅ DOM đã có, gọi API, khởi tạo thư viện 3rd party (Chart.js, etc.)
})

onUnmounted(() => {
  // ✅ Dọn dẹp: clearInterval, removeEventListener, hủy subscription
  clearInterval(timer)
  window.removeEventListener('resize', handleResize)
})

onErrorCaptured((err, instance, info) => {
  // Bắt lỗi từ child component (Error Boundary pattern)
  console.error(err)
  return false // Ngăn lỗi lan lên trên
})

// onActivated / onDeactivated – dùng với <KeepAlive>
onActivated(() => { /* component được kích hoạt từ cache */ })
onDeactivated(() => { /* component bị đưa vào cache */ })
```

---

### 1.4 Component Communication – Đầy Đủ

```vue
<script setup>
// --- Props ---
const props = defineProps({
  title: { type: String, required: true },
  items: { type: Array, default: () => [] },
  config: { type: Object, default: () => ({}) },
})

// --- Emits với validation ---
const emit = defineEmits({
  update: (payload) => typeof payload.id === 'number', // Validate emit
  delete: null, // No validation
})

// --- defineExpose – expose để parent gọi qua ref ---
const inputRef = ref(null)
defineExpose({ focus: () => inputRef.value?.focus(), reset: () => { /* ... */ } })

// --- Provide / Inject ---
import { provide, inject, readonly } from 'vue'

// Parent: cung cấp readonly để tránh mutation từ child
const theme = ref('dark')
provide('theme', readonly(theme))
provide('updateTheme', (val) => { theme.value = val }) // Cung cấp setter riêng

// Child (bất kỳ cấp nào):
const theme = inject('theme')
const updateTheme = inject('updateTheme')
const themeWithDefault = inject('theme', 'light') // default value
</script>
```

---

### 1.5 Directives Tùy Chỉnh (Custom Directives)

```javascript
// main.js – đăng ký global directive
app.directive('focus', {
  mounted(el) { el.focus() }
})

// Component – đăng ký local
const vClickOutside = {
  mounted(el, binding) {
    el._clickHandler = (e) => {
      if (!el.contains(e.target)) binding.value(e)
    }
    document.addEventListener('click', el._clickHandler)
  },
  unmounted(el) {
    document.removeEventListener('click', el._clickHandler)
  }
}
```

```vue
<template>
  <!-- Sử dụng custom directive -->
  <input v-focus />
  <div v-click-outside="closeDropdown">...</div>
</template>
```

---

### 1.6 Teleport & Transition

```vue
<template>
  <!-- Teleport: render component vào nơi khác trong DOM (modal, tooltip) -->
  <Teleport to="body">
    <div class="modal" v-if="showModal">
      <p>Modal content</p>
    </div>
  </Teleport>

  <!-- Transition: animate khi component thêm/xoá -->
  <Transition name="fade" mode="out-in">
    <component :is="activeView" :key="activeView" />
  </Transition>

  <!-- TransitionGroup: animate list -->
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in list" :key="item.id">{{ item.name }}</li>
  </TransitionGroup>
</template>

<style>
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

.list-enter-active, .list-leave-active { transition: all 0.3s; }
.list-enter-from, .list-leave-to { opacity: 0; transform: translateX(-30px); }
</style>
```

---

### 1.7 Vue Router – Nâng Cao

```javascript
// router/index.js
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/dashboard',
      component: () => import('@/views/Dashboard.vue'), // Lazy load
      meta: { requiresAuth: true, title: 'Dashboard' },
      children: [
        { path: 'profile', component: () => import('@/views/Profile.vue') },
        { path: 'settings', component: () => import('@/views/Settings.vue') },
      ]
    },
    { path: '/:pathMatch(.*)*', name: '404', component: NotFound } // Catch-all
  ],
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 } // Scroll to top khi navigate
  }
})

// Navigation Guards
router.beforeEach(async (to, from) => {
  const userStore = useUserStore()

  if (to.meta.requiresAuth && !userStore.isLoggedIn) {
    return { name: 'login', query: { redirect: to.fullPath } }
  }

  // Dynamic title
  document.title = to.meta.title || 'App'
})

// Per-route guard
const route = {
  beforeEnter: (to, from) => {
    // Validate route params
    if (!isValidId(to.params.id)) return false
  }
}
```

---

## 2. Pinia / Vuex

### 2.1 Pinia – Composition Store Syntax (Mới hơn)

```javascript
// stores/useCartStore.js – Option Store (quen thuộc hơn)
export const useCartStore = defineStore('cart', {
  state: () => ({ items: [], discount: 0 }),
  getters: {
    totalItems: (state) => state.items.reduce((sum, i) => sum + i.qty, 0),
    totalPrice: (state) => {
      const sub = state.items.reduce((sum, i) => sum + i.price * i.qty, 0)
      return sub * (1 - state.discount / 100)
    },
  },
  actions: {
    addItem(product) {
      const existing = this.items.find(i => i.id === product.id)
      existing ? existing.qty++ : this.items.push({ ...product, qty: 1 })
    },
    async checkout() {
      const res = await api.post('/orders', { items: this.items })
      this.items = [] // $reset alternative
      return res.data
    }
  }
})

// Composition Store syntax (giống Composition API hơn)
export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const token = ref(localStorage.getItem('token'))
  const isLoggedIn = computed(() => !!token.value)

  async function login(credentials) {
    const res = await api.post('/auth/login', credentials)
    token.value = res.data.token
    user.value = res.data.user
    localStorage.setItem('token', token.value)
  }

  function logout() {
    token.value = null
    user.value = null
    localStorage.removeItem('token')
  }

  return { user, token, isLoggedIn, login, logout }
})
```

---

### 2.2 storeToRefs – Destructure Giữ Reactivity

```vue
<script setup>
import { storeToRefs } from 'pinia'
import { useCartStore } from '@/stores/useCartStore'

const cartStore = useCartStore()

// ❌ BAD: mất reactivity
const { items, totalPrice } = cartStore

// ✅ GOOD: storeToRefs cho state + getters (giống toRefs cho reactive)
const { items, totalPrice } = storeToRefs(cartStore)
// Actions lấy trực tiếp (không cần storeToRefs)
const { addItem, checkout } = cartStore
</script>
```

---

### 2.3 Pinia Plugin – Persist State

```javascript
// Store persistence (dùng pinia-plugin-persistedstate)
export const useSettingStore = defineStore('setting', {
  state: () => ({ theme: 'light', lang: 'vi' }),
  persist: {
    storage: localStorage,
    paths: ['theme', 'lang'], // Chỉ persist 1 số fields
  }
})

// Custom plugin
const piniaLogger = ({ store }) => {
  store.$onAction(({ name, args, after, onError }) => {
    console.log(`Action: ${name}`, args)
    after((result) => console.log(`Result:`, result))
    onError((error) => console.error(`Error:`, error))
  })
}
pinia.use(piniaLogger)
```

---

### 2.4 Vuex Modules (Legacy – Cần Biết)

```javascript
// store/modules/auth.js
const authModule = {
  namespaced: true,       // ✅ Luôn bật để tránh xung đột
  state: () => ({ user: null, token: null }),
  mutations: {
    SET_USER(state, user) { state.user = user }
  },
  actions: {
    async login({ commit }, credentials) {
      const res = await api.post('/login', credentials)
      commit('SET_USER', res.data.user)
    }
  },
  getters: {
    isAdmin: (state) => state.user?.role === 'admin'
  }
}

// Sử dụng với namespace
store.dispatch('auth/login', credentials)
store.getters['auth/isAdmin']

// Trong component với mapState/mapActions
import { mapState, mapActions } from 'vuex'
computed: { ...mapState('auth', ['user', 'token']) }
methods:  { ...mapActions('auth', ['login', 'logout']) }
```

---

## 3. Component Patterns & Performance

### 3.1 Composables – Các Pattern Thực Tế

```javascript
// composables/usePagination.js
export function usePagination(fetchFn, { pageSize = 10 } = {}) {
  const page = ref(1)
  const data = ref([])
  const total = ref(0)
  const loading = ref(false)

  const totalPages = computed(() => Math.ceil(total.value / pageSize))
  const hasNext = computed(() => page.value < totalPages.value)
  const hasPrev = computed(() => page.value > 1)

  async function load() {
    loading.value = true
    try {
      const res = await fetchFn({ page: page.value, limit: pageSize })
      data.value = res.data
      total.value = res.total
    } finally {
      loading.value = false
    }
  }

  function nextPage() { if (hasNext.value) { page.value++; load() } }
  function prevPage() { if (hasPrev.value) { page.value--; load() } }
  function goTo(p) { page.value = p; load() }

  onMounted(load)
  return { data, page, total, totalPages, loading, hasNext, hasPrev, nextPage, prevPage, goTo }
}
```

```javascript
// composables/useDebounce.js
export function useDebounce(fn, delay = 300) {
  let timer = null
  const debouncedFn = (...args) => {
    clearTimeout(timer)
    timer = setTimeout(() => fn(...args), delay)
  }
  onUnmounted(() => clearTimeout(timer))
  return debouncedFn
}

// Sử dụng trong component
const search = ref('')
const fetchResults = useDebounce(async () => {
  results.value = await api.get('/search', { params: { q: search.value } })
}, 400)
watch(search, fetchResults)
```

```javascript
// composables/useLocalStorage.js
export function useLocalStorage(key, defaultValue) {
  const stored = localStorage.getItem(key)
  const data = ref(stored ? JSON.parse(stored) : defaultValue)

  watch(data, (val) => {
    localStorage.setItem(key, JSON.stringify(val))
  }, { deep: true })

  return data
}
const theme = useLocalStorage('theme', 'light')
```

---

### 3.2 Performance Optimization – Chi Tiết

```vue
<script setup>
import { computed, shallowRef, defineAsyncComponent, markRaw } from 'vue'

// markRaw – không track reactivity (dùng cho 3rd party objects như Map instance, Chart.js)
const chartInstance = shallowRef(markRaw(new Chart(...)))

// defineAsyncComponent với loading/error/retry
const AsyncTable = defineAsyncComponent({
  loader: () => import('./DataTable.vue'),
  loadingComponent: LoadingSpinner,
  errorComponent: ErrorDisplay,
  delay: 200,       // Hiện loading sau 200ms (tránh flash)
  timeout: 3000,    // Timeout sau 3s
  onError(error, retry, fail, attempts) {
    if (attempts < 3) retry()
    else fail()
  }
})

// computed writable
const selectedIds = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val)
})
</script>

<template>
  <!-- v-once: render 1 lần, không bao giờ re-render -->
  <AppHeader v-once />

  <!-- v-memo: chỉ re-render khi deps trong array thay đổi -->
  <div v-for="item in bigList" :key="item.id" v-memo="[item.id, item.selected]">
    <ExpensiveItem :item="item" />
  </div>

  <!-- KeepAlive với include/exclude và max -->
  <KeepAlive :include="['UserProfile', 'CartPage']" :max="5">
    <component :is="currentPage" />
  </KeepAlive>
</template>
```

---

### 3.3 Advanced Slots

```vue
<!-- DataTable.vue – Slot cho từng cell để flexible -->
<template>
  <table>
    <thead>
      <tr>
        <th v-for="col in columns" :key="col.key">
          <slot :name="`header-${col.key}`" :col="col">
            {{ col.label }}   <!-- fallback content -->
          </slot>
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="row in data" :key="row.id">
        <td v-for="col in columns" :key="col.key">
          <!-- Scoped slot: truyền data ra ngoài để parent quyết định render -->
          <slot :name="`cell-${col.key}`" :row="row" :value="row[col.key]">
            {{ row[col.key] }}
          </slot>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<!-- Sử dụng -->
<DataTable :columns="cols" :data="products">
  <template #cell-status="{ value }">
    <Badge :color="value === 'active' ? 'green' : 'red'">{{ value }}</Badge>
  </template>
  <template #cell-price="{ value }">
    {{ value.toLocaleString('vi-VN') }}đ
  </template>
</DataTable>
```

---

## 4. Nuxt.js – SSR & SEO

### 4.1 Rendering Modes & routeRules

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  ssr: true,

  routeRules: {
    // Static Generation (build time)
    '/': { prerender: true },
    '/about': { prerender: true },
    '/blog/**': { prerender: true },

    // Cache với ISR
    '/products/**': { swr: 3600 },   // Revalidate sau 1h

    // CSR cho dashboard (không cần SEO)
    '/dashboard/**': { ssr: false },
    '/admin/**': { ssr: false },

    // Redirect
    '/old-page': { redirect: '/new-page' },
  },

  runtimeConfig: {
    // Private – chỉ server
    apiSecret: '',
    // Public – cả client và server
    public: {
      apiBase: '/api',
      siteUrl: 'https://myapp.com'
    }
  }
})
```

---

### 4.2 Layouts & Pages

```
layouts/
├── default.vue    → Layout mặc định
├── auth.vue       → Layout cho login/register (không có sidebar)
└── admin.vue      → Layout cho admin panel

pages/
├── index.vue      → /
├── login.vue      → /login (dùng layout: auth)
├── blog/
│   ├── index.vue           → /blog
│   └── [slug].vue          → /blog/:slug
├── products/
│   ├── index.vue           → /products
│   └── [id]/
│       ├── index.vue       → /products/:id
│       └── edit.vue        → /products/:id/edit
└── [...404].vue   → catch-all
```

```vue
<!-- pages/login.vue -->
<script setup>
definePageMeta({
  layout: 'auth',
  middleware: 'guest',          // Redirect nếu đã login
  title: 'Đăng Nhập',
})
</script>
```

---

### 4.3 Middleware Nuxt

```typescript
// middleware/auth.ts – Route middleware
export default defineNuxtRouteMiddleware((to, from) => {
  const { isLoggedIn } = useAuthStore()

  if (!isLoggedIn) {
    return navigateTo('/login?redirect=' + to.fullPath)
  }
})

// middleware/guest.ts – Chỉ cho user chưa login
export default defineNuxtRouteMiddleware(() => {
  const { isLoggedIn } = useAuthStore()
  if (isLoggedIn) return navigateTo('/dashboard')
})

// Global middleware (tự động apply tất cả routes)
// middleware/logger.global.ts
export default defineNuxtRouteMiddleware((to) => {
  console.log('Navigating to:', to.path)
})
```

---

### 4.4 Server Routes (Nuxt = Full-stack)

```typescript
// server/api/products/index.get.ts
export default defineEventHandler(async (event) => {
  const query = getQuery(event)
  const products = await $fetch(`${process.env.API_URL}/products`, {
    params: query,
    headers: { Authorization: `Bearer ${process.env.API_TOKEN}` }
  })
  return products
})

// server/api/products/[id].ts
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')
  const method = getMethod(event)

  if (method === 'GET') {
    return await db.product.findById(id)
  }
  if (method === 'DELETE') {
    await db.product.delete(id)
    return { success: true }
  }
})
```

---

### 4.5 Plugins Nuxt

```typescript
// plugins/axios.ts
export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig()
  const api = axios.create({ baseURL: config.public.apiBase })

  api.interceptors.request.use((config) => {
    const token = useCookie('token').value
    if (token) config.headers.Authorization = `Bearer ${token}`
    return config
  })

  return { provide: { api } }
})

// composables/useApi.ts – dùng plugin
const { $api } = useNuxtApp()
const data = await $api.get('/products')
```

---

### 4.6 Data Fetching – Chi Tiết

```vue
<script setup>
// useFetch – SSR + cache + reactive
const { data, pending, error, refresh } = await useFetch('/api/products', {
  query: { page: 1, limit: 10 },
  transform: (res) => res.data,    // Transform trước khi lưu vào data
  pick: ['id', 'name', 'price'],   // Chỉ pick fields cần thiết
  watch: [currentPage],            // Auto re-fetch khi currentPage thay đổi
  key: 'product-list',             // Custom cache key
  lazy: true,                      // Không block page render (pending = true trước)
})

// useAsyncData – when you need custom logic
const { data: stats } = await useAsyncData('dashboard-stats', async () => {
  const [sales, users, orders] = await Promise.all([
    $fetch('/api/stats/sales'),
    $fetch('/api/stats/users'),
    $fetch('/api/stats/orders'),
  ])
  return { sales, users, orders }
}, { server: true })

// Refresh sau action
async function deleteProduct(id) {
  await $fetch(`/api/products/${id}`, { method: 'DELETE' })
  await refresh()   // Refresh useFetch data
}
</script>
```

---

## 5. Figma → Code

### 5.1 Quy Trình Chuẩn & CSS Design Tokens

```css
/* 1. CSS Variables từ Figma Design Tokens */
:root {
  /* Colors */
  --color-primary-50:  #EFF6FF;
  --color-primary-500: #3B82F6;
  --color-primary-600: #2563EB;
  --color-gray-50:     #F9FAFB;
  --color-gray-900:    #111827;

  /* Typography */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --text-xs:   0.75rem;   /* 12px */
  --text-sm:   0.875rem;  /* 14px */
  --text-base: 1rem;      /* 16px */
  --text-lg:   1.125rem;  /* 18px */
  --text-xl:   1.25rem;   /* 20px */
  --text-2xl:  1.5rem;    /* 24px */

  /* Spacing (8px base grid) */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;

  /* Border radius */
  --radius-sm: 4px;
  --radius:    8px;
  --radius-lg: 12px;
  --radius-xl: 16px;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow:    0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05);
}
```

### 5.2 Flexbox & Grid Patterns Hay Dùng

```css
/* Flexbox patterns */
.flex-center   { display: flex; align-items: center; justify-content: center; }
.flex-between  { display: flex; align-items: center; justify-content: space-between; }
.flex-col      { display: flex; flex-direction: column; }

/* Card layout */
.card {
  background: white;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: var(--space-6);
}

/* Responsive Grid */
.grid-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: var(--space-6);
}

/* Container */
.container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 var(--space-4);
}
@media (min-width: 640px)  { .container { padding: 0 var(--space-6); } }
@media (min-width: 1024px) { .container { padding: 0 var(--space-8); } }
```

### 5.3 CSS Animation / Transition

```css
/* Hover animations */
.btn {
  background: var(--color-primary-500);
  color: white;
  padding: 10px 20px;
  border-radius: var(--radius);
  border: none;
  cursor: pointer;
  transition: background 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
}
.btn:hover {
  background: var(--color-primary-600);
  transform: translateY(-1px);
  box-shadow: var(--shadow-lg);
}
.btn:active { transform: translateY(0); }

/* Skeleton loading animation */
@keyframes shimmer {
  0%   { background-position: -200px 0; }
  100% { background-position: calc(200px + 100%) 0; }
}
.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200px 100%;
  animation: shimmer 1.5s infinite;
  border-radius: var(--radius-sm);
}
```

---

## 6. Laravel Framework & Nâng Cao

### 6.1 Kiến Trúc MVC & Request Lifecycle

```
Request
  → public/index.php (entry point)
  → bootstrap/app.php (application khởi tạo)
  → HTTP Kernel
  → Global Middleware (CORS, Session, ParseJSON...)
  → Route Matching
  → Route Middleware (auth, throttle...)
  → Controller@method
    → FormRequest (validation)
    → Service Layer (business logic)
      → Repository / Model (data access)
    → Resource (response transform)
  → Response → Client
```

---

### 6.2 Eloquent ORM – Chi Tiết

```php
// Model đầy đủ tính năng
class Product extends Model
{
    use SoftDeletes, HasFactory;

    protected $fillable = ['name', 'slug', 'price', 'category_id', 'is_active'];
    protected $hidden   = ['deleted_at'];
    protected $casts    = [
        'price'     => 'decimal:2',
        'is_active' => 'boolean',
        'metadata'  => 'array',        // JSON auto cast
        'published_at' => 'datetime',
    ];

    // Relationships
    public function category(): BelongsTo    { return $this->belongsTo(Category::class); }
    public function tags(): BelongsToMany    { return $this->belongsToMany(Tag::class)->withTimestamps(); }
    public function images(): HasMany        { return $this->hasMany(ProductImage::class); }
    public function latestImage(): HasOne    { return $this->hasOne(ProductImage::class)->latestOfMany(); }

    // HasManyThrough
    public function reviews(): HasManyThrough
    {
        return $this->hasManyThrough(Review::class, OrderItem::class);
    }

    // Scopes
    public function scopeActive($q)                  { return $q->where('is_active', true); }
    public function scopePriceRange($q, $min, $max)  { return $q->whereBetween('price', [$min, $max]); }
    public function scopeSearch($q, $term)           { return $q->where('name', 'like', "%{$term}%"); }

    // Accessors (Laravel 9+ attribute syntax)
    protected function price(): Attribute
    {
        return Attribute::make(
            get: fn($val) => $val / 100,       // Lưu cents, trả về đồng
            set: fn($val) => $val * 100,
        );
    }

    // Mutators (auto)
    protected function name(): Attribute
    {
        return Attribute::make(
            set: fn($val) => ucwords(strtolower($val))
        );
    }
}

// Complex Queries
$products = Product::query()
    ->with(['category:id,name', 'tags:id,name', 'images'])  // Select specific columns
    ->withCount('reviews')                                    // reviews_count
    ->withAvg('reviews', 'rating')                           // reviews_avg_rating
    ->active()
    ->search($request->search)
    ->priceRange($request->min_price, $request->max_price)
    ->when($request->category_id, fn($q) => $q->where('category_id', $request->category_id))
    ->orderBy($request->sort ?? 'created_at', $request->direction ?? 'desc')
    ->paginate(15)
    ->withQueryString();                                      // Giữ query params trong pagination
```

---

### 6.3 FormRequest – Validation Tách Biệt

```php
// php artisan make:request StoreProductRequest
class StoreProductRequest extends FormRequest
{
    public function authorize(): bool
    {
        // Kiểm tra quyền – false sẽ trả về 403
        return auth()->user()->can('create', Product::class);
    }

    public function rules(): array
    {
        return [
            'name'        => 'required|string|max:255',
            'slug'        => 'required|string|unique:products,slug',
            'price'       => 'required|numeric|min:0',
            'category_id' => 'required|exists:categories,id',
            'images'      => 'nullable|array|max:5',
            'images.*'    => 'image|mimes:jpeg,png,webp|max:2048',
            'metadata'    => 'nullable|array',
        ];
    }

    // Custom error messages
    public function messages(): array
    {
        return [
            'name.required'        => 'Tên sản phẩm là bắt buộc.',
            'category_id.exists'   => 'Danh mục không tồn tại.',
        ];
    }

    // Transform data trước khi validate xong
    protected function prepareForValidation(): void
    {
        $this->merge([
            'slug' => Str::slug($this->name),
        ]);
    }

    // Transform sau khi validated
    public function validated($key = null, $default = null): array
    {
        $data = parent::validated();
        $data['user_id'] = auth()->id();
        return $data;
    }
}
```

---

### 6.4 API Resource – Kiểm Soát Output

```php
// app/Http/Resources/ProductResource.php
class ProductResource extends JsonResource
{
    public function toArray(Request $request): array
    {
        return [
            'id'         => $this->id,
            'name'       => $this->name,
            'price'      => $this->price,
            'currency'   => 'VND',

            // Conditional – chỉ include khi được load
            'category'   => new CategoryResource($this->whenLoaded('category')),
            'tags'       => TagResource::collection($this->whenLoaded('tags')),

            // Conditional field – chỉ include nếu điều kiện đúng
            'admin_notes' => $this->when(
                $request->user()?->isAdmin(),
                $this->admin_notes
            ),

            // Aggregate
            'reviews_count' => $this->reviews_count ?? 0,
            'rating'        => round($this->reviews_avg_rating ?? 0, 1),

            'created_at' => $this->created_at->format('d/m/Y H:i'),
        ];
    }

    // Thêm meta data ngoài data
    public function with(Request $request): array
    {
        return ['version' => '1.0'];
    }
}

// Collection Resource với pagination
class ProductCollection extends ResourceCollection
{
    public function toArray(Request $request): array
    {
        return [
            'data' => $this->collection,
            'meta' => [
                'total'        => $this->total(),
                'per_page'     => $this->perPage(),
                'current_page' => $this->currentPage(),
            ],
        ];
    }
}
```

---

### 6.5 Repository Pattern

```php
// app/Contracts/ProductRepositoryInterface.php
interface ProductRepositoryInterface
{
    public function paginate(array $filters, int $perPage = 15): LengthAwarePaginator;
    public function findById(int $id): Product;
    public function create(array $data): Product;
    public function update(Product $product, array $data): Product;
    public function delete(Product $product): bool;
}

// app/Repositories/ProductRepository.php
class ProductRepository implements ProductRepositoryInterface
{
    public function paginate(array $filters, int $perPage = 15): LengthAwarePaginator
    {
        return Product::query()
            ->with(['category', 'tags'])
            ->when($filters['search'] ?? null, fn($q, $s) => $q->search($s))
            ->when($filters['category_id'] ?? null, fn($q, $id) => $q->where('category_id', $id))
            ->active()
            ->latest()
            ->paginate($perPage);
    }

    public function create(array $data): Product
    {
        return Product::create($data);
    }
}

// AppServiceProvider
$this->app->bind(ProductRepositoryInterface::class, ProductRepository::class);

// Controller
class ProductController extends Controller
{
    public function __construct(private ProductRepositoryInterface $repo) {}

    public function index(Request $request)
    {
        $products = $this->repo->paginate($request->only(['search', 'category_id']));
        return ProductResource::collection($products);
    }
}
```

---

### 6.6 Observer Pattern

```php
// php artisan make:observer ProductObserver --model=Product
class ProductObserver
{
    public function creating(Product $product): void
    {
        $product->user_id = auth()->id();
        $product->slug    = Str::slug($product->name);
    }

    public function created(Product $product): void
    {
        Cache::tags('products')->flush();   // Xoá cache
        event(new ProductCreated($product));
    }

    public function updated(Product $product): void
    {
        Cache::forget("product.{$product->id}");
    }

    public function deleting(Product $product): void
    {
        $product->images()->delete();   // Xoá related trước
    }
}

// Đăng ký trong AppServiceProvider
Product::observe(ProductObserver::class);
```

---

### 6.7 Caching

```php
// Cache thông dụng
Cache::put('key', $value, now()->addHours(1));
$value = Cache::get('key', 'default');
Cache::forget('key');
Cache::flush();

// remember – get hoặc store nếu chưa có
$products = Cache::remember('products.featured', 3600, function () {
    return Product::with('category')->active()->limit(10)->get();
});

// Cache tags – group để xoá theo nhóm
Cache::tags(['products', 'featured'])->put('list', $data, 3600);
Cache::tags('products')->flush();   // Xoá tất cả cache có tag 'products'

// Cache trong model
class Product extends Model
{
    public static function getFeatured(): Collection
    {
        return Cache::remember('products.featured', 3600, fn() =>
            static::active()->with('category')->limit(10)->get()
        );
    }
}
```

---

### 6.8 Policy – Authorization

```php
// php artisan make:policy ProductPolicy --model=Product
class ProductPolicy
{
    public function viewAny(User $user): bool            { return true; }
    public function view(?User $user, Product $product): bool { return $product->is_active || $user?->isAdmin(); }
    public function create(User $user): bool             { return $user->hasRole('seller') || $user->isAdmin(); }
    public function update(User $user, Product $product): bool { return $user->id === $product->user_id || $user->isAdmin(); }
    public function delete(User $user, Product $product): bool { return $user->id === $product->user_id || $user->isAdmin(); }
}

// Controller
$this->authorize('update', $product);   // Throw 403 nếu không có quyền

public function update(UpdateProductRequest $request, Product $product)
{
    $this->authorize('update', $product);
    $product->update($request->validated());
    return new ProductResource($product);
}
```

---

### 6.9 Testing (Cơ Bản)

```php
// tests/Feature/ProductApiTest.php
class ProductApiTest extends TestCase
{
    use RefreshDatabase;

    public function test_guest_cannot_create_product(): void
    {
        $response = $this->postJson('/api/products', ['name' => 'Test']);
        $response->assertUnauthorized();           // 401
    }

    public function test_seller_can_create_product(): void
    {
        $user    = User::factory()->create(['role' => 'seller']);
        $payload = Product::factory()->make()->toArray();

        $response = $this->actingAs($user)->postJson('/api/products', $payload);

        $response->assertCreated()                 // 201
                 ->assertJsonPath('data.name', $payload['name']);

        $this->assertDatabaseHas('products', ['name' => $payload['name']]);
    }

    public function test_product_list_is_cached(): void
    {
        Cache::shouldReceive('remember')->once()->andReturn(collect([]));
        $this->getJson('/api/products')->assertOk();
    }
}
```

---

## 7. RESTful API & Bảo Mật

### 7.1 API Response Structure Chuẩn

```json
// Success
{
  "success": true,
  "data": { "id": 1, "name": "Product A" },
  "message": "Tạo sản phẩm thành công"
}

// Collection
{
  "success": true,
  "data": [...],
  "meta": {
    "total": 100, "per_page": 15,
    "current_page": 1, "last_page": 7
  }
}

// Error
{
  "success": false,
  "message": "Validation failed",
  "errors": {
    "email": ["Email không hợp lệ"],
    "price": ["Giá phải là số dương"]
  }
}
```

```php
// app/Http/Controllers/Controller.php – Base response helpers
protected function success($data = null, string $message = 'OK', int $code = 200): JsonResponse
{
    return response()->json(['success' => true, 'data' => $data, 'message' => $message], $code);
}

protected function error(string $message, int $code = 400, $errors = null): JsonResponse
{
    return response()->json(['success' => false, 'message' => $message, 'errors' => $errors], $code);
}
```

---

### 7.2 JWT vs Sanctum vs Passport

| | JWT (tymon/jwt-auth) | Sanctum | Passport |
|---|---|---|---|
| Type | Stateless token | DB token (SPA/API) | Full OAuth2 server |
| Dùng khi | Mobile apps, microservices | SPA + API cùng domain | Cần OAuth2 server riêng |
| Phức tạp | Trung bình | Đơn giản | Cao |
| Revoke token | Cần blacklist | Xoá trong DB | Xoá trong DB |

```php
// Sanctum – Phổ biến nhất cho Laravel SPA/API
// 1. Cài đặt: composer require laravel/sanctum
// 2. Migrate: php artisan migrate
// 3. Thêm HasApiTokens vào User model

// Login
$token = $user->createToken('api-token', ['products:read', 'orders:write'])->plainTextToken;

// Kiểm tra ability
if ($request->user()->tokenCan('products:write')) { ... }

// Logout (revoke current token)
$request->user()->currentAccessToken()->delete();

// Revoke all tokens
$request->user()->tokens()->delete();
```

---

### 7.3 Bảo Mật API – OWASP Top 10 Liên Quan

```php
// 1. SQL Injection – Eloquent tự xử lý với parameterized queries
// ❌ Nguy hiểm:
DB::select("SELECT * FROM users WHERE name = '{$name}'");
// ✅ An toàn:
User::where('name', $name)->get();
DB::select('SELECT * FROM users WHERE name = ?', [$name]);

// 2. Mass Assignment – dùng $fillable
$product = Product::create($request->all());   // ❌ Nguy hiểm
$product = Product::create($request->validated()); // ✅

// 3. Broken Object Level Authorization – luôn kiểm tra ownership
public function update(Request $request, Product $product)
{
    abort_if($product->user_id !== auth()->id(), 403, 'Forbidden');
    // hoặc $this->authorize('update', $product);
}

// 4. Broken Function Level Authorization – dùng Policy/middleware
Route::middleware(['auth:sanctum', 'role:admin'])->group(...);

// 5. Sensitive Data Exposure – không trả về dữ liệu nhạy cảm
protected $hidden = ['password', 'remember_token', 'api_secret'];

// 6. Security Headers (middleware)
response()->header('X-Content-Type-Options', 'nosniff')
          ->header('X-Frame-Options', 'DENY')
          ->header('X-XSS-Protection', '1; mode=block');
```

---

### 7.4 Axios – Error Handling Chuẩn

```javascript
// lib/api.js – Cấu hình axios đầy đủ
import axios from 'axios'
import { useAuthStore } from '@/stores/useAuthStore'
import router from '@/router'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000,
  headers: { 'Accept': 'application/json' }
})

let isRefreshing = false
let failedQueue = []

const processQueue = (error, token = null) => {
  failedQueue.forEach(p => error ? p.reject(error) : p.resolve(token))
  failedQueue = []
}

api.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

api.interceptors.response.use(
  res => res,
  async err => {
    const originalRequest = err.config

    if (err.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        // Queue requests đang chờ refresh
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject })
        }).then(token => {
          originalRequest.headers.Authorization = `Bearer ${token}`
          return api(originalRequest)
        })
      }

      originalRequest._retry = true
      isRefreshing = true

      try {
        const { data } = await axios.post('/api/auth/refresh', {
          refresh_token: localStorage.getItem('refresh_token')
        })
        const newToken = data.access_token
        localStorage.setItem('access_token', newToken)
        processQueue(null, newToken)
        originalRequest.headers.Authorization = `Bearer ${newToken}`
        return api(originalRequest)
      } catch (refreshError) {
        processQueue(refreshError)
        useAuthStore().logout()
        router.push('/login')
        return Promise.reject(refreshError)
      } finally {
        isRefreshing = false
      }
    }

    return Promise.reject(err)
  }
)

export default api
```

---

## 8. Câu Hỏi Phỏng Vấn & Đáp Án Chi Tiết

### 🟦 Vue.js – 15 câu

**Q1: `v-if` vs `v-show` – khi nào dùng cái nào?**
> `v-if`: tạo/xoá DOM hoàn toàn, cost cao nhưng tiết kiệm memory khi hidden. `v-show`: chỉ toggle `display:none`, DOM luôn tồn tại. **Dùng `v-show`** khi toggle thường xuyên (dropdown, modal). **Dùng `v-if`** khi ít toggle hoặc cần giải phóng memory.

**Q2: `ref` vs `reactive` – ưu nhược điểm?**
> `ref`: dùng cho primitive, cần `.value`, hoạt động với destructure. `reactive`: dùng cho object phức tạp, không cần `.value`, nhưng **mất reactivity khi destructure** – phải dùng `toRefs()`. Nhiều người dùng `ref` cho tất cả để nhất quán.

**Q3: Giải thích Virtual DOM và cách Vue diff?**
> Vue duy trì một **Virtual DOM** (cây JS object). Khi state thay đổi, Vue tạo Virtual DOM mới → **so sánh (diff)** với cái cũ theo thuật toán O(n) → chỉ update đúng phần DOM thay đổi. Điều này hiệu quả hơn thao tác DOM trực tiếp vì DOM operation tốn kém.

**Q4: Tại sao `:key` trong `v-for` quan trọng?**
> Vue dùng key để **track identity** của node khi list thay đổi. Không có key → Vue dùng index, khi xoá/sắp xếp gây re-render sai (component state bị giữ nhầm phần tử). Key phải stable (id), không dùng index khi list có thể thay đổi thứ tự.

**Q5: `computed` vs `methods` vs `watch` – chọn cái nào?**
> `computed`: **cache**, chỉ tính lại khi dependency thay đổi → dùng để derive data (fullName, filteredList). `methods`: luôn chạy lại → dùng cho event handler. `watch`: side effect khi value thay đổi (gọi API, log, animation) → dùng khi cần oldVal/newVal.

**Q6: Composable khác Mixin như thế nào?**
> Mixin: **name collision** (hai mixin cùng method name → xung đột), không rõ property từ đâu, khó debug. Composable: dùng function → đặt tên rõ ràng, **không xung đột namespace**, TypeScript-friendly, dễ test độc lập.

**Q7: Làm sao giải quyết prop drilling?**
> Ba cách: (1) **`provide/inject`** – inject thẳng xuống component tree bất kể độ sâu. (2) **Pinia store** – global state. (3) Dùng **Event Bus** (ít dùng hơn trong Vue 3). Best practice: `provide/inject` cho scope nhỏ, Pinia cho global.

**Q8: `defineExpose` dùng để làm gì?**
> Khi dùng `<script setup>`, component mặc định **không expose** các method/ref ra ngoài. `defineExpose({ focus, reset })` cho phép parent component gọi method của child qua template ref: `childRef.value.focus()`.

**Q9: Giải thích `shallowRef` và khi nào dùng?**
> `shallowRef` chỉ track reactivity ở **cấp 1** (shallow). Khi assign lại toàn bộ value → reactive. Khi mutate nested property → không reactive. Dùng khi store large object/array mà chỉ cần trigger update khi replace toàn bộ (hiệu năng tốt hơn).

**Q10: `watchEffect` vs `watch` – khác gì?**
> `watchEffect`: **tự động track** dependencies (chạy function, bất cứ `ref` nào được read trong đó đều được track), **eager** (chạy ngay lần đầu), không có oldVal. `watch`: cần **khai báo source** tường minh, **lazy** (không chạy ngay, trừ `immediate: true`), có oldVal/newVal.

**Q11: Giải thích Teleport và use case?**
> `<Teleport to="body">` render nội dung ra ngoài component tree (trong DOM), nhưng vẫn thuộc component về logic. **Use case**: Modal, Toast notification, Tooltip – tránh bị `overflow: hidden` hay `z-index` của parent cắt mất.

**Q12: KeepAlive hoạt động thế nào?**
> `<KeepAlive>` cache component instance thay vì destroy. Component bị deactivate (không xoá) và re-activate khi dùng lại → giữ state. Dùng `onActivated`/`onDeactivated` thay vì `onMounted`/`onUnmounted`. Limit số lượng cache bằng `:max`.

**Q13: Khi nào dùng `markRaw`?**
> Dùng khi không muốn object bị Vue track reactivity (ví dụ: Chart.js instance, Map, large data object chỉ đọc). Dùng kết hợp với `shallowRef`: `const chart = shallowRef(markRaw(new Chart(...)))`. Tránh Vue tạo Proxy không cần thiết → hiệu năng tốt hơn.

**Q14: Vue 3 cải tiến gì so với Vue 2?**
> (1) Composition API – tái sử dụng logic tốt hơn. (2) Performance: Virtual DOM viết lại nhanh hơn, tree-shaking tốt hơn. (3) TypeScript support native. (4) `<script setup>` – DX tốt hơn. (5) Teleport, Suspense, `<Fragments>` (multiple root elements). (6) Reactivity dùng Proxy thay vì `Object.defineProperty` → track dynamic properties.

**Q15: Giải thích Suspense component?**
> `<Suspense>` hiển thị **fallback** trong khi đợi async component hoặc `async setup()` resolve. Kết hợp với `defineAsyncComponent` và `useAsyncData` trong Nuxt. Có 2 slots: `#default` (content khi ready) và `#fallback` (loading state).

---

### 🟧 Nuxt.js – 8 câu

**Q1: Nuxt giải quyết gì mà Vue thuần không làm được?**
> **SSR** (HTML sẵn sàng từ server → SEO + FCP tốt hơn), **file-based routing** (tự động từ `pages/`), **auto-import** (components, composables không cần import), **Server Routes** (`server/api/`), **Modules** ecosystem phong phú (auth, i18n, image...).

**Q2: SSR vs SSG – khi nào chọn cái nào?**
> **SSR**: data thay đổi theo từng request (user-specific content, real-time data, e-commerce). **SSG**: data ít thay đổi, build time OK (landing page, blog, docs). **ISR** (`swr`): content thay đổi nhưng không cần realtime (product catalog, news).

**Q3: `useFetch` vs `useAsyncData` vs `$fetch`?**
> `useFetch('/api/x')` = shorthand của `useAsyncData('key', () => $fetch('/api/x'))` với auto-key từ URL. `useAsyncData` khi cần custom key hoặc fetcher phức tạp (parallel requests). `$fetch` = raw client, không cache, không SSR-aware – dùng trong event handlers.

**Q4: Hydration mismatch là gì? Cách fix?**
> Xảy ra khi HTML server render khác với HTML client render (thường do date/time, random values, browser-only APIs). Fix: (1) dùng `<ClientOnly>` wrapper (2) dùng `useState` thay vì `ref` cho shared state (3) check `process.client` trước khi dùng browser API.

**Q5: Middleware trong Nuxt hoạt động thế nào?**
> Có 3 loại: (1) **Route middleware** (file trong `middleware/`) – run trước khi navigate. (2) **Global middleware** (filename có `.global`) – tự động apply tất cả routes. (3) **Server middleware** (`server/middleware/`) – run trên mọi server request. Khai báo trong `definePageMeta({ middleware: 'auth' })`.

**Q6: Nuxt Image tối ưu thế nào?**
> `<NuxtImg>` tự động: resize theo `sizes`, convert sang **WebP**, **lazy loading**, generate srcset cho responsive images. Dùng providers (Cloudinary, ImageKit) để process on-the-fly.

**Q7: `useRuntimeConfig` dùng để làm gì?**
> Access runtime config từ `nuxt.config.ts`. `runtimeConfig.apiSecret` chỉ có ở server. `runtimeConfig.public.*` có cả client và server. Giá trị có thể override bằng environment variables (`NUXT_API_SECRET=xxx`).

**Q8: Server-side Rendering ảnh hưởng đến Pinia thế nào?**
> Mỗi request tạo **Pinia instance mới** ở server (tránh state leak giữa các users). Dùng `useState` của Nuxt (không phải `ref`) để chia sẻ state giữa server và client qua **hydration**. Store phải được init sau `setActivePinia` ở server.

---

### 🟥 Laravel – 15 câu

**Q1: Service Container và Dependency Injection là gì?**
> IoC (Inversion of Control) Container tự động **resolve và inject** dependencies. Khi type-hint class/interface trong constructor, Laravel tự tạo instance (hoặc lấy singleton đã bind). Giúp code **loosely coupled**, dễ test (mock dependencies).

**Q2: N+1 query problem – giải thích và fix?**
> N+1: 1 query lấy list + N query cho mỗi item khi access relation trong loop. Fix: `eager loading` với `with(['posts', 'comments'])`. Dùng **Laravel Debugbar** hoặc `DB::listen()` để detect. `withCount()` thay vì `$user->posts->count()`.

**Q3: Middleware – pipeline hoạt động thế nào?**
> Request đi qua **middleware pipeline** (như onion): mỗi middleware có thể (1) modify request và pass tiếp (`$next($request)`), (2) trả về response sớm (abort, redirect). Response đi ngược lại qua pipeline để post-processing.

**Q4: `singleton` vs `bind` vs `scoped`?**
> `singleton`: 1 instance suốt vòng đời app. `bind`: instance mới mỗi resolve. `scoped`: 1 instance per HTTP request (dùng cho per-request state).

**Q5: Eloquent Accessor vs Mutator là gì?**
> **Accessor**: transform value khi đọc (`$product->price` → trả về formatted). **Mutator**: transform value khi ghi (`$product->name = 'abc'` → auto ucwords). Laravel 9+ dùng `Attribute::make(get:, set:)`.

**Q6: SoftDeletes hoạt động thế nào?**
> Thêm `deleted_at` column. Khi delete: set `deleted_at = now()` (không xoá physically). Query mặc định tự thêm `WHERE deleted_at IS NULL`. Dùng `withTrashed()`, `onlyTrashed()`, `restore()`, `forceDelete()`.

**Q7: Queue Driver và khi nào chọn gì?**
> `sync`: chạy đồng bộ (development). `database`: lưu trong DB (đơn giản, không cần Redis). `redis`: hiệu năng cao (production), monitoring với **Laravel Horizon**. `sqs`: AWS managed queue. Nên dùng `redis` + Horizon cho production.

**Q8: Event Sourcing vs Observer pattern?**
> **Observer** (Eloquent Observer): hook vào Eloquent lifecycle (creating, created, updating...). **Event/Listener**: loosely coupled, nhiều listener cho 1 event, có thể queue listener. Dùng Event/Listener cho business events, Observer cho data lifecycle.

**Q9: Làm sao tránh fat controller?**
> Tách ra: **FormRequest** (validation), **Service class** (business logic), **Repository** (data access), **Resource** (response transform), **Job** (async work), **Policy** (authorization). Controller chỉ **orchestrate**, không chứa logic.

**Q10: Migration best practices?**
> (1) Mỗi migration làm 1 việc. (2) Luôn viết `down()`. (3) Không sửa migration đã chạy production (tạo migration mới). (4) Thêm index đúng chỗ (`index`, `unique`). (5) Dùng `foreignId()->constrained()` thay vì viết tay.

**Q11: Laravel Sanctum vs Passport – khi nào dùng?**
> **Sanctum**: SPA authentication, mobile token, simple API tokens. Đơn giản, không cần OAuth2 server. **Passport**: cần full OAuth2 server (phát token cho third-party apps, complex authorization flows với scopes, grant types).

**Q12: `HasOne` vs `BelongsTo` – khác gì?**
> Cả hai đều lấy 1 record. Khác ở **foreign key**: `HasOne` – foreign key ở **bên kia** (User hasOne Profile → profiles.user_id). `BelongsTo` – foreign key ở **model hiện tại** (Profile belongsTo User → profiles.user_id).

**Q13: Cách xử lý race condition trong Queue?**
> Dùng `atomic lock`: `Cache::lock("process-order-{$orderId}")->block(5, function() { ... })`. Hoặc dùng `withoutOverlapping()` middleware cho job: `public function middleware() { return [new WithoutOverlapping($this->order->id)]; }`

**Q14: Laravel Horizon là gì?**
> Dashboard để monitor **Redis queues**: xem jobs đang chạy/thất bại, throughput, thời gian xử lý, tự động balance workers. Config trong `horizon.php`: số worker per queue, max processes.

**Q15: Policy vs Gate khác gì?**
> **Gate**: simple closure-based authorization cho không liên quan đến model. `Gate::define('view-dashboard', fn(User $u) => $u->isAdmin())`. **Policy**: class-based, liên kết với Model cụ thể, có nhiều method (view, create, update, delete...).

---

### 🔐 API & Security – 8 câu

**Q1: JWT structure là gì?**
> 3 phần base64url encoded: **Header** (alg, typ) + **Payload** (claims: sub, exp, iat, custom data) + **Signature** (HMAC SHA256 của header+payload+secret). Signature đảm bảo token không bị tamper. Server **verify signature** mà không cần DB lookup.

**Q2: Access token vs Refresh token strategy?**
> **Access token**: TTL ngắn (15-60 phút), stateless, gắn vào mỗi request. **Refresh token**: TTL dài (7-30 ngày), lưu httpOnly cookie (tránh XSS), dùng để lấy access token mới. Khi refresh token hết hạn → logout. Rotation: mỗi lần refresh, issue refresh token mới + blacklist cái cũ.

**Q3: Tại sao lưu token trong httpOnly cookie an toàn hơn localStorage?**
> **localStorage**: dễ bị **XSS** (JavaScript có thể đọc). **httpOnly cookie**: JavaScript không thể access, nhưng tự động gửi kèm request → phải chống **CSRF** (dùng SameSite=Strict hoặc CSRF token). Trade-off: localStorage = XSS risk, httpOnly cookie = CSRF risk nhưng dễ mitigate hơn.

**Q4: CSRF là gì? Laravel chống thế nào?**
> Cross-Site Request Forgery: attacker tạo trang web giả gửi request đến site của bạn với cookie của user. Laravel chống bằng **CSRF token** (synchronizer token pattern): mỗi form có `@csrf` token, Middleware VerifyCsrfToken kiểm tra. API stateless dùng JWT/Sanctum không cần CSRF.

**Q5: Rate Limiting – tại sao cần và cách implement?**
> Chống **brute force**, **DDoS**, abuse API. Laravel: `Route::middleware('throttle:60,1')` (60 req/phút). Custom: `RateLimiter::for('api', fn($req) => Limit::perMinute(60)->by($req->user()?->id ?: $req->ip()))`. Response headers: `X-RateLimit-Remaining`, `Retry-After`.

**Q6: API Versioning – các cách?**
> (1) **URL versioning**: `/api/v1/products` → rõ ràng nhất. (2) **Header versioning**: `Accept: application/vnd.api+json;version=1`. (3) **Query param**: `/api/products?version=1`. Khuyên dùng URL versioning vì dễ debug, cache, route nhóm.

**Q7: Idempotency trong API?**
> Request **idempotent** khi gọi nhiều lần không thay đổi kết quả: GET, PUT, DELETE đều idempotent. POST thường không (mỗi lần tạo record mới). Implement idempotency key cho POST: client gửi `Idempotency-Key: uuid` → server cache kết quả → duplicate request trả về kết quả cached.

**Q8: OAuth2 Authorization Code Flow?**
> (1) User click "Login with Google". (2) Redirect đến Google authorization server với `client_id`, `redirect_uri`, `scope`, `state`. (3) User đồng ý → Google redirect về với `code`. (4) Server exchange `code` + `client_secret` → `access_token`. (5) Dùng `access_token` gọi Google API. PKCE thay `client_secret` cho SPA/Mobile (không thể giữ secret).

---

## 9. Checklist & Lộ Trình

### ✅ Lộ Trình 5 Tuần

| Tuần | Mục tiêu | Output |
|---|---|---|
| 1 | Vue.js Core: Composition API, Lifecycle, Directives, Router | Tự code Todo App với Vue 3 |
| 2 | Pinia + Composables + Performance + Nuxt.js cơ bản | Thêm global state vào Todo App |
| 3 | Nuxt.js SSR, SEO, Middleware + Figma → Code | Clone 1 landing page từ Figma |
| 4 | Laravel: MVC, Eloquent, Middleware, Queue, JWT/Sanctum | Build REST API cho Todo App |
| 5 | Fullstack integration + Luyện Q&A | Deploy fullstack project lên GitHub |

---

### ✅ Checklist Kiến Thức Bắt Buộc

#### Vue.js
- [ ] Composition API: `ref`, `reactive`, `computed`, `watch`, `watchEffect`
- [ ] `toRefs`, `storeToRefs`, `markRaw`, `shallowRef`
- [ ] Lifecycle đầy đủ: `onMounted`, `onUnmounted`, `onErrorCaptured`
- [ ] Component: `defineProps`, `defineEmits`, `defineExpose`, slots
- [ ] `provide` / `inject` với readonly pattern
- [ ] Custom directive: `v-focus`, `v-click-outside`
- [ ] Teleport, Transition, TransitionGroup
- [ ] Composables: `useFetch`, `usePagination`, `useDebounce`, `useLocalStorage`
- [ ] Performance: `v-memo`, `v-once`, `defineAsyncComponent`, `KeepAlive`
- [ ] Vue Router: navigation guards, lazy routes, scroll behavior

#### Pinia
- [ ] Option Store: `state`, `getters`, `actions`
- [ ] Composition Store syntax
- [ ] `storeToRefs` để destructure
- [ ] Persistence plugin
- [ ] `$onAction` / `$subscribe`

#### Nuxt.js
- [ ] SSR vs SSG vs ISR – khi nào dùng
- [ ] `useFetch`, `useAsyncData`, `$fetch` – phân biệt
- [ ] `useSeoMeta`, `useHead` – dynamic meta
- [ ] File routing: dynamic `[slug]`, catch-all `[...]`, layouts
- [ ] Route middleware: guest, auth, global
- [ ] Server routes: `server/api/`
- [ ] `useRuntimeConfig` – env vars
- [ ] Nuxt Plugins – provide globally

#### Laravel
- [ ] Request lifecycle: Kernel → Middleware → Controller
- [ ] CRUD API: Controller + FormRequest + Resource
- [ ] Eloquent: relationships (6 types), eager loading, scopes, casts, accessors/mutators
- [ ] N+1 – detect và fix
- [ ] Middleware: tạo, pipeline, register
- [ ] Service Container: `bind`, `singleton`, interface binding
- [ ] FormRequest: `authorize`, `rules`, `messages`, `prepareForValidation`
- [ ] Repository Pattern: interface + implementation
- [ ] Migration: index, foreign key, SoftDeletes
- [ ] Queue + Job: dispatch, delay, retry, `$tries`, `failed()`
- [ ] Event + Listener: register, trigger, queue listener
- [ ] Observer: lifecycle hooks, cache invalidation
- [ ] Policy: view, create, update, delete
- [ ] Caching: `remember`, tags, flush
- [ ] Sanctum: token creation, `tokenCan`, revoke

#### API & Security
- [ ] HTTP Methods + Status Codes (thuộc lòng)
- [ ] JWT structure: header.payload.signature
- [ ] Access token + Refresh token strategy
- [ ] httpOnly cookie vs localStorage trade-offs
- [ ] CORS, CSRF, Rate Limiting
- [ ] SQL Injection, Mass Assignment protection
- [ ] Axios interceptors: auto token, auto refresh với queue
- [ ] API Response structure chuẩn
- [ ] OAuth2 Authorization Code + PKCE flow

---

### 📁 Bài Tập Thực Hành Khuyến Nghị

| Project | Stack | Features |
|---|---|---|
| **Todo App** | Vue 3 + Pinia + Laravel Sanctum | CRUD, auth, JWT flow |
| **Blog** | Nuxt 3 SSR + Laravel API | SEO, useFetch, pagination |
| **Clone Figma** | HTML/CSS/Vue | Responsive, pixel-perfect, animation |
| **E-shop mini** | Vue 3 + Pinia + Laravel (full) | Cart, orders, queue email |

---

### 🎯 Tips Trả Lời Phỏng Vấn

1. **STAR Method**: Situation → Task → Action → Result khi kể về kinh nghiệm
2. **Thừa nhận không biết**: "Tôi chưa dùng feature này trong thực tế, nhưng tôi hiểu concept là..."
3. **Liên hệ thực tế**: Luôn kết câu trả lời lý thuyết với dự án đã làm
4. **Hỏi lại khi cần**: "Bạn có thể cho biết use case cụ thể không?" – thể hiện bạn biết trade-offs
5. **Performance mindset**: Luôn đề cập đến cache, eager loading, lazy loading khi nói về optimization

---

### 📚 Tài Liệu Chính Thống

- [Vue 3 Docs](https://vuejs.org/guide/)
- [Pinia Docs](https://pinia.vuejs.org/)
- [Vue Router](https://router.vuejs.org/)
- [Nuxt 3 Docs](https://nuxt.com/docs)
- [Laravel Docs](https://laravel.com/docs)
- [Laravel Sanctum](https://laravel.com/docs/sanctum)
- [JWT.io](https://jwt.io/)
- [OWASP API Security](https://owasp.org/API-Security/)

---

## 9. Performance & Security Checklist

### 9.1 Frontend Performance

#### Core Web Vitals – Mục tiêu

| Metric | Tốt | Cần cải thiện | Kém |
|---|---|---|---|
| **LCP** (Largest Contentful Paint) | < 2.5s | 2.5 – 4s | > 4s |
| **FID** (First Input Delay) | < 100ms | 100 – 300ms | > 300ms |
| **CLS** (Cumulative Layout Shift) | < 0.1 | 0.1 – 0.25 | > 0.25 |
| **TTFB** (Time to First Byte) | < 800ms | 800ms – 1.8s | > 1.8s |

#### Checklist Frontend

```
Images:
✅ Dùng NuxtImage / <img loading="lazy"> cho ảnh dưới fold
✅ Format WebP (20-35% nhỏ hơn JPEG)
✅ Luôn khai báo width + height (tránh CLS)
✅ Preload LCP image: <link rel="preload" as="image">

JavaScript:
✅ Code splitting: defineAsyncComponent, dynamic import
✅ Tree shaking: import cụ thể (import { ref } không phải import Vue)
✅ Tránh tạo object/function inline trong template (re-render)
✅ Dùng v-memo cho list items nặng
✅ Dùng KeepAlive cho expensive components

CSS:
✅ Critical CSS inline trong <head>
✅ Font: preload + font-display: swap (tránh FOUT)
✅ Tránh @import trong CSS (blocking)

Caching:
✅ Cache-Control header đúng (assets: max-age=31536000, HTML: no-cache)
✅ Service Worker cho PWA (cache API responses)
✅ Nuxt: routeRules SWR/ISR cho pages ít thay đổi
```

#### Tránh Re-render Không Cần Thiết

```javascript
// ❌ Object literal tạo mới mỗi render → Child re-render
<Child :config="{ size: 'lg' }" />

// ✅ Dùng computed để memoize
const childConfig = computed(() => ({ size: 'lg' }))
<Child :config="childConfig" />

// ❌ Arrow function tạo mới mỗi render
<Child :onClick="(e) => handleClick(e)" />

// ✅ Named function (reference stable)
function handleClick(e) { /* ... */ }
<Child :onClick="handleClick" />

// v-memo: bỏ qua re-render nếu deps không đổi
<div v-for="item in items" :key="item.id" v-memo="[item.id, item.selected, item.name]">
  <ExpensiveRow :item="item" />
</div>
```

---

### 9.2 Backend Performance (Laravel)

```php
// ── Eloquent Query Optimization ────────────────────
// N+1 Problem
$posts = Post::with(['author', 'tags', 'comments' => function ($q) {
    $q->latest()->limit(3);
}])->get();

// withCount / withAvg / withSum
$categories = Category::withCount('products')
                       ->withAvg('products', 'price')
                       ->get();

// Chỉ SELECT columns cần (tránh SELECT *)
User::select(['id', 'name', 'email'])->get();

// Chunking: xử lý large dataset không bị OOM
Product::chunk(500, function ($products) {
    foreach ($products as $product) {
        // Process...
    }
});

// Cursor: stream từng row (memory ~O(1))
foreach (Product::cursor() as $product) {
    // Process 1 product tại một thời điểm
}

// ── Cache Layer ─────────────────────────────────────
// Simple cache
$products = Cache::remember('products.all', now()->addHour(), fn() =>
    Product::active()->with('category')->get()
);

// Cache tags (group & flush together)
Cache::tags(['products', 'category-1'])->remember('...', 3600, fn() => ...);
Cache::tags('products')->flush();  // Flush tất cả products cache

// ── Database Indexes ─────────────────────────────────
// EXPLAIN ANALYZE để tìm slow queries
// DB::statement("EXPLAIN ANALYZE SELECT * FROM products WHERE ...");

// Composite index đúng thứ tự (selectivity cao nhất trước)
Schema::table('orders', function (Blueprint $table) {
    $table->index(['user_id', 'status', 'created_at']);
    // Tốt cho: WHERE user_id = ? AND status = ? ORDER BY created_at
});
```

---

### 9.3 Security Checklist

#### Frontend

```
✅ Không lưu token trong localStorage (XSS attack vector)
   → Dùng httpOnly cookie hoặc in-memory (mất khi refresh)
✅ Sanitize user input trước v-html: dùng DOMPurify
✅ Content Security Policy (CSP) header
✅ HTTPS + HSTS header (Strict-Transport-Security)
✅ Không expose secrets trong frontend code
   → Dùng NUXT_PUBLIC_ prefix, đây là public!
   → API keys backend-only: để trong server routes
✅ Subresource Integrity (SRI) cho CDN scripts
```

#### Backend (Laravel)

```
Authentication & Authorization:
✅ Hash passwords: bcrypt (đã tự động với Hash::make)
✅ Rate limiting: ThrottleRequests middleware
✅ expire tokens: Sanctum tokenExpiration config
✅ Policy cho từng resource (không dùng if-else thô)

Input Validation:
✅ Always validate với FormRequest
✅ Mass assignment: $fillable (whitelist, safe mặc định)
✅ Parameterized queries: Eloquent/Query Builder (không raw string)
✅ Validate file uploads: MIME type, size, extension whitelist

Headers (thêm vào Middleware):
✅ X-Content-Type-Options: nosniff
✅ X-Frame-Options: DENY (chống clickjacking)
✅ X-XSS-Protection: 1; mode=block
✅ Referrer-Policy: strict-origin-when-cross-origin

Deployment:
✅ APP_DEBUG=false trong production
✅ composer audit (check vulnerabilities)
✅ Xóa /telescope, /horizon trên production (hoặc auth middleware)
✅ Database backup tự động + encryption at rest
✅ .env không được commit vào git (gitignore)
✅ Log rotation + không log sensitive data
```

#### OWASP API Security Top 10

| # | Tên | Laravel Fix |
|---|---|---|
| API1 | Broken Object Level Authorization (BOLA) | `Policy` – check `user_id === auth()->id()` |
| API2 | Broken Authentication | `Sanctum`, expire tokens, rate limit |
| API3 | Broken Object Property Level Auth | Chỉ return $fillable, dùng `Resource` |
| API4 | Unrestricted Resource Consumption | `throttle:60,1`, pagination |
| API5 | Broken Function Level Authorization | `Gate`/`Policy` cho mỗi action |
| API6 | Unrestricted Access to Sensitive Business Flows | Rate limit + CAPTCHA |
| API7 | Server Side Request Forgery (SSRF) | Validate URLs, whitelist domains |
| API8 | Security Misconfiguration | APP_DEBUG=false, remove dev routes |
| API9 | Improper Inventory Management | Document API, version (`/api/v1/`) |
| API10 | Unsafe Consumption of APIs | Validate 3rd-party API responses |

---

### 9.4 HTTP Status Codes – Bảng Tra Cứu

| Code | Tên | Khi nào dùng |
|---|---|---|
| **200** | OK | GET/PUT/PATCH thành công |
| **201** | Created | POST tạo resource thành công |
| **204** | No Content | DELETE thành công (không có body) |
| **301** | Moved Permanently | Redirect vĩnh viễn (SEO pass link juice) |
| **304** | Not Modified | Cache còn valid |
| **400** | Bad Request | Request malformed, sai format |
| **401** | Unauthorized | Chưa xác thực – "Who are you?" |
| **403** | Forbidden | Đã xác thực nhưng không có quyền – "I know you, but NO" |
| **404** | Not Found | Resource không tồn tại |
| **409** | Conflict | Duplicate (email đã tồn tại) |
| **422** | Unprocessable Entity | Validation errors (Laravel mặc định) |
| **429** | Too Many Requests | Rate limit exceeded |
| **500** | Internal Server Error | Server crash, lỗi không xử lý |
| **503** | Service Unavailable | Bảo trì, quá tải |

> **🔑 Nhớ nhanh:** 401 = chưa login · 403 = không đủ quyền · 422 = validation fail · 429 = rate limited

---

## 10. Quick Reference – Cheat Sheet

```
Vue.js Reactivity:
  ref          → primitive + .value, works everywhere
  reactive     → object, no .value, MẤT reactivity khi destructure
  computed     → cached derived, lazy eval
  watch        → side effects, lazy, có oldVal/newVal
  watchEffect  → auto-track deps, eager, dùng onCleanup

Lifecycle quan trọng:
  onMounted   → DOM ready, fetch data, init 3rd-party libs
  onUnmounted → cleanup timers, listeners, observers
  onActivated / onDeactivated → với KeepAlive

Props/Emits:
  defineProps({ title: { type: String, required: true } })
  defineEmits(['update:modelValue', 'close'])
  v-model custom = :modelValue + @update:modelValue

Provide/Inject – tránh prop drilling:
  parent: provide('key', readonly(ref))
  child:  inject('key', defaultValue)

Pinia:
  storeToRefs() để destructure state + getters (giữ reactive)
  Actions lấy trực tiếp (không cần storeToRefs)
  $patch() để update nhiều state cùng lúc

Nuxt fetch:
  useFetch      → SSR, cached, reactive, auto-key từ URL
  useAsyncData  → custom key + fetcher, SSR-aware
  $fetch        → raw HTTP, no cache, dùng trong event handlers

Laravel:
  N+1 fix       = with(), withCount(), withAvg()
  Mass assign   = $fillable (whitelist) > $guarded (blacklist)
  cascade       = xóa parent → xóa children (pivot tables)
  restrict      = xóa parent → lỗi nếu còn children (financial)
  Job           = async task, ShouldQueue, retry với backoff
  Event/Listener = 1 event → nhiều listeners (loose coupling)

Security:
  401 vs 403:   401 = chưa xác thực, 403 = không có quyền
  Token store:  httpOnly cookie > memory > localStorage
  Validation:   Luôn dùng FormRequest, không trust user input
  SQL:          Eloquent/parameterized, không raw string interpolation
```

---
---

## 11. TypeScript + Vue 3

> TypeScript là **bắt buộc** ở nhiều công ty hiện đại. Vue 3 được viết bằng TypeScript nên TS support rất tốt.

### 11.1 Props & Emits với TypeScript

```vue
<script setup lang="ts">
// ── Props với interface ──────────────────────────────
interface Product {
  id: number
  name: string
  price: number
  category: {
    id: number
    name: string
  }
  tags?: string[]   // optional
  status: 'active' | 'inactive' | 'draft'  // Union type
}

const props = defineProps<{
  product: Product
  isLoading?: boolean
  pageSize?: number
}>()

// Với default values (dùng withDefaults)
const props2 = withDefaults(defineProps<{
  product: Product
  isLoading?: boolean
  pageSize?: number
}>(), {
  isLoading: false,
  pageSize: 10,
})

// ── Emits với TypeScript ─────────────────────────────
const emit = defineEmits<{
  (e: 'update', id: number, data: Partial<Product>): void
  (e: 'delete', id: number): void
  (e: 'update:modelValue', value: string): void
}>()

// Vue 3.3+ shorthand:
const emit2 = defineEmits<{
  update: [id: number, data: Partial<Product>]
  delete: [id: number]
  'update:modelValue': [value: string]
}>()

// ── defineExpose ─────────────────────────────────────
const inputRef = ref<HTMLInputElement | null>(null)
defineExpose({
  focus: () => inputRef.value?.focus(),
})
</script>
```

---

### 11.2 Composables với TypeScript

```typescript
// composables/useFetch.ts
interface FetchState<T> {
  data: Ref<T | null>
  loading: Ref<boolean>
  error: Ref<Error | null>
  refresh: () => Promise<void>
}

export function useFetch<T>(url: string | Ref<string>): FetchState<T> {
  const data    = ref<T | null>(null) as Ref<T | null>
  const loading = ref(false)
  const error   = ref<Error | null>(null)

  async function fetch() {
    loading.value = true
    error.value   = null
    try {
      const response = await globalThis.fetch(unref(url))
      if (!response.ok) throw new Error(`HTTP ${response.status}`)
      data.value = await response.json() as T
    } catch (e) {
      error.value = e instanceof Error ? e : new Error(String(e))
    } finally {
      loading.value = false
    }
  }

  watchEffect(() => {
    unref(url)   // Track URL changes
    fetch()
  })

  return { data, loading, error, refresh: fetch }
}

// Sử dụng với type inference:
const { data: products, loading } = useFetch<Product[]>('/api/products')
// products: Ref<Product[] | null>  → TypeScript biết type đầy đủ!
```

---

### 11.3 Pinia với TypeScript

```typescript
// stores/useAuthStore.ts
interface User {
  id: number
  name: string
  email: string
  role: 'user' | 'seller' | 'admin'
}

interface AuthState {
  user: User | null
  token: string | null
  loading: boolean
}

export const useAuthStore = defineStore('auth', {
  state: (): AuthState => ({
    user:    null,
    token:   null,
    loading: false,
  }),

  getters: {
    isLoggedIn: (state): boolean => !!state.token,
    isAdmin:    (state): boolean => state.user?.role === 'admin',
    userName:   (state): string  => state.user?.name ?? 'Guest',
  },

  actions: {
    async login(credentials: { email: string; password: string }): Promise<void> {
      this.loading = true
      try {
        const res = await api.post<{ token: string; user: User }>('/auth/login', credentials)
        this.token = res.data.token
        this.user  = res.data.user
      } finally {
        this.loading = false
      }
    },

    logout(): void {
      this.$patch({ user: null, token: null })
    }
  }
})

// Type-safe usage:
const auth = useAuthStore()
auth.login({ email: 'a@b.com', password: '123' })  // TypeScript enforce params
if (auth.isAdmin) { /* admin logic */ }             // boolean, không cần cast
```

---

### 11.4 Vue Router với TypeScript

```typescript
// router/index.ts
import type { RouteRecordRaw } from 'vue-router'

// Extend route meta với custom types
declare module 'vue-router' {
  interface RouteMeta {
    requiresAuth?: boolean
    requiresAdmin?: boolean
    title?: string
    layout?: 'default' | 'auth' | 'admin'
  }
}

const routes: RouteRecordRaw[] = [
  {
    path: '/dashboard',
    component: () => import('@/pages/DashboardPage.vue'),
    meta: {
      requiresAuth: true,
      title: 'Dashboard',
      layout: 'default',
    },
  }
]

// Type-safe useRoute
const route = useRoute()
route.meta.requiresAuth  // boolean | undefined – TypeScript knows!
route.params.id          // string | string[] – cần cast nếu muốn number
const id = Number(route.params.id)
```

---

## 12. Testing – Vue & Laravel

### 12.1 Vue Component Testing (Vitest + Vue Test Utils)

```typescript
// tests/components/ProductCard.test.ts
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { mount, shallowMount } from '@vue/test-utils'
import { createPinia } from 'pinia'
import ProductCard from '@/components/ProductCard.vue'

const mockProduct = {
  id: 1,
  name: 'Giày Nike Air Max',
  price: 2500000,
  status: 'active' as const,
  category: { id: 1, name: 'Giày' },
}

describe('ProductCard', () => {
  // mount: render component + children (integration)
  // shallowMount: stub children (unit)

  it('renders product name correctly', () => {
    const wrapper = mount(ProductCard, {
      props: { product: mockProduct },
      global: {
        plugins: [createPinia()],  // Pinia store nếu cần
      }
    })

    expect(wrapper.find('[data-testid="product-name"]').text())
      .toBe('Giày Nike Air Max')
  })

  it('formats price in VND', () => {
    const wrapper = mount(ProductCard, { props: { product: mockProduct } })

    expect(wrapper.find('.price').text()).toContain('2.500.000')
  })

  it('emits add-to-cart event with product when button clicked', async () => {
    const wrapper = mount(ProductCard, { props: { product: mockProduct } })

    await wrapper.find('[data-testid="add-to-cart"]').trigger('click')

    expect(wrapper.emitted('add-to-cart')).toBeTruthy()
    expect(wrapper.emitted('add-to-cart')![0]).toEqual([mockProduct])
  })

  it('shows inactive badge when status is inactive', () => {
    const wrapper = mount(ProductCard, {
      props: { product: { ...mockProduct, status: 'inactive' } }
    })

    expect(wrapper.find('.badge-inactive').exists()).toBe(true)
  })

  it('disables add-to-cart button when loading prop is true', async () => {
    const wrapper = mount(ProductCard, {
      props: { product: mockProduct, isLoading: true }
    })

    expect(wrapper.find('[data-testid="add-to-cart"]').attributes('disabled'))
      .toBeDefined()
  })
})
```

```typescript
// Test composables
// tests/composables/useCounter.test.ts
import { describe, it, expect } from 'vitest'
import { useCounter } from '@/composables/useCounter'

describe('useCounter', () => {
  it('starts at initialValue', () => {
    const { count } = useCounter(5)
    expect(count.value).toBe(5)
  })

  it('increments correctly', () => {
    const { count, increment } = useCounter(0)
    increment()
    expect(count.value).toBe(1)
  })

  it('respects max value', () => {
    const { count, increment } = useCounter(9, { max: 10 })
    increment()
    increment()  // Would be 11, but max is 10
    expect(count.value).toBe(10)
  })

  it('resets to initial value', () => {
    const { count, increment, reset } = useCounter(3)
    increment()
    increment()
    reset()
    expect(count.value).toBe(3)
  })
})
```

---

### 12.2 Pinia Store Testing

```typescript
// tests/stores/useCartStore.test.ts
import { describe, it, expect, beforeEach, vi } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { useCartStore } from '@/stores/useCartStore'

const mockProduct = { id: 1, name: 'Nike', price: 500000 }

describe('useCartStore', () => {
  beforeEach(() => {
    // Tạo fresh Pinia cho mỗi test (tránh state leak)
    setActivePinia(createPinia())
  })

  it('adds item to empty cart', () => {
    const cart = useCartStore()
    cart.addItem(mockProduct)

    expect(cart.items).toHaveLength(1)
    expect(cart.items[0].qty).toBe(1)
  })

  it('increments qty for duplicate items', () => {
    const cart = useCartStore()
    cart.addItem(mockProduct)
    cart.addItem(mockProduct)

    expect(cart.items).toHaveLength(1)
    expect(cart.items[0].qty).toBe(2)
  })

  it('calculates totalPrice correctly', () => {
    const cart = useCartStore()
    cart.addItem({ id: 1, name: 'A', price: 100000 })
    cart.addItem({ id: 2, name: 'B', price: 200000 })
    cart.addItem({ id: 1, name: 'A', price: 100000 })  // qty → 2

    // A: 100000*2 = 200000, B: 200000*1 = 200000 → total = 400000
    expect(cart.totalPrice).toBe(400000)
  })

  it('clears cart after checkout', async () => {
    const cart = useCartStore()
    cart.addItem(mockProduct)

    // Mock API call
    vi.spyOn(global, 'fetch').mockResolvedValueOnce({
      ok: true,
      json: () => Promise.resolve({ orderId: 123 }),
    } as Response)

    await cart.checkout()

    expect(cart.items).toHaveLength(0)
  })
})
```

---

### 12.3 Laravel Testing Patterns

```php
// Tổ chức tests rõ ràng
tests/
├── Feature/          // Integration tests – HTTP requests
│   ├── Auth/
│   │   ├── LoginTest.php
│   │   └── RegisterTest.php
│   ├── Products/
│   │   ├── ProductIndexTest.php
│   │   ├── ProductStoreTest.php
│   │   └── ProductAuthorizationTest.php
│   └── Orders/
│       └── CheckoutTest.php
└── Unit/             // Unit tests – Models, Services
    ├── Models/
    │   └── ProductTest.php
    └── Services/
        └── PriceCalculatorTest.php
```

```php
// PHPUnit best practices
class OrderTest extends TestCase
{
    use RefreshDatabase;

    // ── Test naming convention: test_scenario_expectedResult ──
    public function test_checkout_sends_confirmation_email(): void
    {
        // ARRANGE
        Mail::fake();  // Bắt mail, không gửi thật
        $user    = User::factory()->create();
        $product = Product::factory()->create(['stock' => 5]);
        $cart    = [['product_id' => $product->id, 'qty' => 2]];

        // ACT
        $this->actingAs($user)
             ->postJson('/api/checkout', ['items' => $cart])
             ->assertCreated();

        // ASSERT
        Mail::assertSent(OrderConfirmationMail::class, function ($mail) use ($user) {
            return $mail->hasTo($user->email);
        });
    }

    public function test_checkout_decrements_stock(): void
    {
        $user    = User::factory()->create();
        $product = Product::factory()->create(['stock' => 10]);

        $this->actingAs($user)
             ->postJson('/api/checkout', [
                 'items' => [['product_id' => $product->id, 'qty' => 3]]
             ])
             ->assertCreated();

        $this->assertDatabaseHas('products', [
            'id'    => $product->id,
            'stock' => 7,  // 10 - 3
        ]);
    }

    public function test_checkout_fails_when_stock_insufficient(): void
    {
        $user    = User::factory()->create();
        $product = Product::factory()->create(['stock' => 2]);

        $this->actingAs($user)
             ->postJson('/api/checkout', [
                 'items' => [['product_id' => $product->id, 'qty' => 5]]
             ])
             ->assertUnprocessable()
             ->assertJsonValidationErrorFor('items.0.qty');
    }

    public function test_checkout_dispatches_processing_job(): void
    {
        Queue::fake();  // Bắt jobs, không chạy thật
        $user    = User::factory()->create();
        $product = Product::factory()->create(['stock' => 10]);

        $this->actingAs($user)
             ->postJson('/api/checkout', [
                 'items' => [['product_id' => $product->id, 'qty' => 1]]
             ])
             ->assertCreated();

        Queue::assertPushed(ProcessOrderJob::class);
        // Kiểm tra job với specific data:
        Queue::assertPushed(ProcessOrderJob::class, function ($job) use ($user) {
            return $job->order->user_id === $user->id;
        });
    }
}
```

---

## 13. Laravel Architecture Patterns

### 13.1 Repository Pattern

```php
// Tại sao dùng Repository?
// → Tách business logic khỏi data access
// → Swap data source dễ dàng (DB → API → Cache)
// → Dễ mock trong tests

// app/Repositories/Contracts/ProductRepositoryInterface.php
interface ProductRepositoryInterface
{
    public function all(array $filters = []): LengthAwarePaginator;
    public function findById(int $id): Product;
    public function create(array $data): Product;
    public function update(int $id, array $data): Product;
    public function delete(int $id): bool;
}

// app/Repositories/EloquentProductRepository.php
class EloquentProductRepository implements ProductRepositoryInterface
{
    public function all(array $filters = []): LengthAwarePaginator
    {
        return Product::query()
            ->when($filters['search'] ?? null, fn($q, $s) =>
                $q->where('name', 'like', "%{$s}%")
            )
            ->when($filters['category_id'] ?? null, fn($q, $id) =>
                $q->where('category_id', $id)
            )
            ->when($filters['min_price'] ?? null, fn($q, $price) =>
                $q->where('price', '>=', $price)
            )
            ->with('category')
            ->orderBy($filters['sort'] ?? 'created_at', $filters['dir'] ?? 'desc')
            ->paginate($filters['per_page'] ?? 15);
    }

    public function findById(int $id): Product
    {
        return Product::with(['category', 'tags', 'images'])
                      ->findOrFail($id);
    }

    public function create(array $data): Product
    {
        return Product::create($data);
    }

    public function update(int $id, array $data): Product
    {
        $product = Product::findOrFail($id);
        $product->update($data);
        return $product->fresh();
    }

    public function delete(int $id): bool
    {
        return Product::findOrFail($id)->delete();
    }
}

// app/Providers/RepositoryServiceProvider.php
class RepositoryServiceProvider extends ServiceProvider
{
    public function register(): void
    {
        $this->app->bind(
            ProductRepositoryInterface::class,
            EloquentProductRepository::class,
        );
    }
}

// app/Http/Controllers/ProductController.php
class ProductController extends Controller
{
    // DI qua constructor – Laravel Service Container tự resolve
    public function __construct(private ProductRepositoryInterface $products) {}

    public function index(Request $request): JsonResponse
    {
        return response()->json(
            ProductResource::collection(
                $this->products->all($request->validated())
            )
        );
    }
}
```

---

### 13.2 Service Layer Pattern

```php
// app/Services/OrderService.php
// → Chứa business logic phức tạp, orchestrate nhiều repositories

class OrderService
{
    public function __construct(
        private OrderRepository   $orders,
        private ProductRepository $products,
        private PaymentService    $payments,
    ) {}

    public function checkout(User $user, array $items): Order
    {
        // Validate stock
        foreach ($items as $item) {
            $product = $this->products->findById($item['product_id']);
            if ($product->stock < $item['qty']) {
                throw new InsufficientStockException($product, $item['qty']);
            }
        }

        // Wrap trong database transaction
        return DB::transaction(function () use ($user, $items) {
            // 1. Tạo order
            $order = $this->orders->create([
                'user_id' => $user->id,
                'total'   => $this->calculateTotal($items),
                'status'  => 'pending',
            ]);

            // 2. Tạo order items + trừ stock
            foreach ($items as $item) {
                $order->items()->create($item);
                $this->products->decrementStock($item['product_id'], $item['qty']);
            }

            // 3. Dispatch background job
            ProcessOrderJob::dispatch($order)->onQueue('orders');
            OrderPlaced::dispatch($order);  // Fire event

            return $order;
        });
    }

    private function calculateTotal(array $items): int
    {
        return collect($items)->sum(fn($item) =>
            $this->products->findById($item['product_id'])->price * $item['qty']
        );
    }
}

// Controller trở nên mỏng (thin controller):
class OrderController extends Controller
{
    public function __construct(private OrderService $orderService) {}

    public function store(CheckoutRequest $request): JsonResponse
    {
        try {
            $order = $this->orderService->checkout(auth()->user(), $request->items);
            return response()->json(new OrderResource($order), 201);
        } catch (InsufficientStockException $e) {
            return response()->json(['error' => $e->getMessage()], 422);
        }
    }
}
```

---

### 13.3 Observer Pattern

```php
// app/Observers/ProductObserver.php
// → Tự động trigger khi model thay đổi (tách side effects khỏi model)

class ProductObserver
{
    // Chạy SAU khi created
    public function created(Product $product): void
    {
        // Tự động tạo slug
        $product->updateQuietly(['slug' => Str::slug($product->name)]);

        // Notify admin
        Notification::route('mail', config('app.admin_email'))
                    ->notify(new NewProductNotification($product));
    }

    // Chạy SAU khi updated
    public function updated(Product $product): void
    {
        // Invalidate cache khi product thay đổi
        Cache::tags(['products', "product-{$product->id}"])->flush();

        // Reindex search nếu tên/giá thay đổi
        if ($product->wasChanged(['name', 'price', 'description'])) {
            SyncProductToSearchJob::dispatch($product);
        }
    }

    // Chạy TRƯỚC khi deleted
    public function deleting(Product $product): void
    {
        // Kiểm tra có order đang xử lý không
        if ($product->orders()->where('status', 'processing')->exists()) {
            throw new \Exception('Không thể xóa sản phẩm đang có đơn hàng đang xử lý');
        }
    }

    public function deleted(Product $product): void
    {
        Cache::tags("product-{$product->id}")->flush();
    }
}

// Đăng ký trong AppServiceProvider hoặc ProductServiceProvider:
Product::observe(ProductObserver::class);
```

---

### 13.4 Event & Listener

```php
// Khi nào dùng Event/Listener vs Observer?
// Observer: gắn với model lifecycle (created, updated, deleted)
// Event/Listener: business events ("OrderPlaced", "PaymentFailed", "UserRegistered")
//   → Loose coupling: nhiều listeners cho 1 event
//   → Listeners có thể queue (async)

// app/Events/OrderPlaced.php
class OrderPlaced
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    public function __construct(public readonly Order $order) {}
}

// app/Listeners/SendOrderConfirmation.php
class SendOrderConfirmation implements ShouldQueue
{
    use InteractsWithQueue;

    public int    $tries   = 3;
    public int    $backoff = 60;  // 60s giữa retry
    public string $queue   = 'notifications';

    public function handle(OrderPlaced $event): void
    {
        Mail::to($event->order->user)
            ->send(new OrderConfirmationMail($event->order));
    }

    // Chạy nếu job fail sau hết retries
    public function failed(OrderPlaced $event, Throwable $exception): void
    {
        Log::error("Failed to send order confirmation", [
            'order_id' => $event->order->id,
            'error'    => $exception->getMessage(),
        ]);
    }
}

// app/Listeners/UpdateInventory.php
class UpdateInventory
{
    public function handle(OrderPlaced $event): void
    {
        foreach ($event->order->items as $item) {
            $item->product->decrement('stock', $item->qty);
        }
    }
}

// EventServiceProvider.php
protected $listen = [
    OrderPlaced::class => [
        SendOrderConfirmation::class,  // Listener 1: email
        UpdateInventory::class,        // Listener 2: stock
        SyncToWarehouseSystem::class,  // Listener 3: ERP
    ],
    UserRegistered::class => [
        SendWelcomeEmail::class,
        AssignDefaultRole::class,
        TrackSignupAnalytics::class,
    ],
];
```

---

## 14. Nuxt.js – Advanced Patterns

### 14.1 useFetch vs useAsyncData vs $fetch – Khi nào dùng gì?

| | `useFetch` | `useAsyncData` | `$fetch` |
|---|---|---|---|
| **SSR** | ✅ | ✅ | ❌ (client-only) |
| **Cache** | ✅ auto (URL as key) | ✅ custom key | ❌ |
| **Reactive** | ✅ | ✅ | ❌ |
| **Khi dùng** | Simple API calls | Complex logic, multiple sources | Event handlers, manual fetch |

```vue
<script setup>
// ── useFetch: đơn giản, SSR + cache ──────────────────
const { data: products, pending, error } = await useFetch('/api/products', {
  query: { page: currentPage, per_page: 15 },
  key:   `products-page-${currentPage.value}`,    // Cache key tùy chỉnh
  watch: [currentPage],                            // Auto re-fetch khi page thay đổi
  transform: (res) => res.data,                    // Transform trước khi lưu vào data
  getCachedData: (key, nuxtApp) => {               // Custom cache handler
    return nuxtApp.payload.data[key]               // Dùng payload từ server
  }
})

// ── useAsyncData: nhiều fetches song song ─────────────
const { data: dashboardData } = await useAsyncData('dashboard', async () => {
  const [stats, recentOrders, topProducts] = await Promise.all([
    $fetch('/api/stats'),
    $fetch('/api/orders?limit=5'),
    $fetch('/api/products?sort=sales&limit=6'),
  ])
  return { stats, recentOrders, topProducts }
})

// ── $fetch: trong event handler ───────────────────────
async function createProduct(formData) {
  try {
    const result = await $fetch('/api/products', {
      method: 'POST',
      body: formData,
    })
    await refreshNuxtData('products-list')  // Invalidate related cache
    navigateTo(`/products/${result.id}`)
  } catch (error) {
    // xử lý lỗi
  }
}
</script>
```

---

### 14.2 State Management trong Nuxt

```javascript
// Nuxt cung cấp useState – shared state giữa server và client
// (Giải quyết hydration mismatch)

// composables/useAppState.ts
export const useTheme = () => useState<'light' | 'dark'>('theme', () => 'light')
export const useUser  = () => useState<User | null>('current-user', () => null)

// Sử dụng ở bất kỳ component/page nào:
const theme = useTheme()
const user  = useUser()

// useTheme() ở page A = useTheme() ở Layout = cùng 1 state

// ── Pinia + Nuxt SSR ──────────────────────────────────
// Pinia state được serialize từ server → gửi xuống client (payload)
// → Tránh duplication (fetch 1 lần trên server, hydrate client không fetch lại)

// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@pinia/nuxt'],
  pinia: {
    storesDirs: ['./stores/**'],  // Auto-import stores
  },
})
```

---

### 14.3 Nuxt Image Optimization

```vue
<template>
  <!-- NuxtImg: optimize + lazy load + WebP conversion -->
  <NuxtImg
    src="/products/nike-air.jpg"
    width="800"
    height="600"
    format="webp"
    quality="80"
    loading="lazy"
    sizes="(max-width: 768px) 100vw, (max-width: 1024px) 50vw, 33vw"
    :placeholder="[25, 25, 75, 5]"  // tiny placeholder trước khi load
    @load="onImageLoad"
  />

  <!-- NuxtPicture: multiple formats với fallback -->
  <NuxtPicture
    src="/hero/banner.jpg"
    :imgAttrs="{ class: 'hero-image' }"
    width="1200"
    height="500"
    preload  <!-- preload cho LCP image -->
    sizes="100vw"
  />
</template>
```

---

## 15. Các Pattern Vue Hay Gặp Trong Interview

### 15.1 v-model Custom Component

```vue
<!-- CustomInput.vue – pattern hay hỏi trong phỏng vấn -->
<script setup>
// v-model = :modelValue + @update:modelValue
const props = defineProps({
  modelValue: { type: String, default: '' },
  label:      { type: String, default: '' },
  error:      { type: String, default: '' },
})

const emit = defineEmits(['update:modelValue'])

// Computed writable để dùng v-model trong template
const value = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val),
})
</script>

<template>
  <div class="form-field">
    <label v-if="label">{{ label }}</label>
    <!-- v-model trên input bind với computed writable -->
    <input v-model="value" :class="{ error: error }" />
    <span v-if="error" class="error-msg">{{ error }}</span>
  </div>
</template>
```

```vue
<!-- Multiple v-models (Vue 3) -->
<MyModal v-model:visible="showModal" v-model:title="modalTitle" />

<!-- MyModal.vue -->
<script setup>
defineProps({
  visible: Boolean,
  title:   String,
})
defineEmits(['update:visible', 'update:title'])
</script>
```

---

### 15.2 Compound Component Pattern

```vue
<!-- Form.vue – Compound components: liên kết nhau qua provide/inject -->
<script setup lang="ts">
import { provide, reactive } from 'vue'

const props = defineProps<{
  initialValues?: Record<string, any>
  onSubmit: (values: Record<string, any>) => void | Promise<void>
}>()

const state = reactive({
  values: { ...props.initialValues },
  errors: {} as Record<string, string>,
  isSubmitting: false,
})

// Cung cấp context cho tất cả child components
provide('form', {
  values:   state.values,
  errors:   state.errors,
  setField: (key: string, val: any) => { state.values[key] = val },
  setError: (key: string, msg: string) => { state.errors[key] = msg },
})

async function submit() {
  state.isSubmitting = true
  await props.onSubmit(state.values)
  state.isSubmitting = false
}
</script>

<template>
  <form @submit.prevent="submit">
    <slot :isSubmitting="state.isSubmitting" />
  </form>
</template>
```

```vue
<!-- FormField.vue – inject từ Form parent -->
<script setup>
import { inject, computed } from 'vue'

const props = defineProps({ name: String })

const form = inject('form')  // Nhận context từ Form.vue

const value = computed({
  get: () => form.values[props.name],
  set: (val) => form.setField(props.name, val),
})

const error = computed(() => form.errors[props.name])
</script>

<template>
  <div>
    <slot :value="value" :error="error" :onChange="(v) => value = v" />
    <span v-if="error" class="error">{{ error }}</span>
  </div>
</template>
```

```vue
<!-- Sử dụng: API rất clean -->
<Form :initialValues="{ name: '', email: '' }" :onSubmit="handleSubmit">
  <template #default="{ isSubmitting }">
    <FormField name="name">
      <template #default="{ value, onChange }">
        <input :value="value" @input="onChange($event.target.value)" />
      </template>
    </FormField>

    <FormField name="email">
      <template #default="{ value, onChange }">
        <input type="email" :value="value" @input="onChange($event.target.value)" />
      </template>
    </FormField>

    <button type="submit" :disabled="isSubmitting">Submit</button>
  </template>
</Form>
```

---

### 15.3 Plugin Pattern

```javascript
// plugins/toast.js – Global plugin
const ToastPlugin = {
  install(app, options = {}) {
    // Đăng ký global component
    app.component('Toast', ToastComponent)

    // Global property (dùng được trong mọi component)
    const toast = {
      success: (msg) => showToast('success', msg),
      error:   (msg) => showToast('error', msg),
      warning: (msg) => showToast('warning', msg),
    }

    // Cung cấp qua provide
    app.provide('toast', toast)

    // Hoặc globalProperties (option API style)
    app.config.globalProperties.$toast = toast
  }
}

// main.js
app.use(ToastPlugin, { duration: 3000 })

// Trong component (Composition API):
const toast = inject('toast')
toast.success('Đã thêm vào giỏ hàng!')

// Trong component (Options API):
this.$toast.error('Có lỗi xảy ra!')
```

---

> **📝 Lưu ý cuối:** File `CODE_EXERCISES.md` chứa bài tập thực hành với code đầy đủ. Đọc lý thuyết ở file này → làm bài tập → tự kiểm tra!
