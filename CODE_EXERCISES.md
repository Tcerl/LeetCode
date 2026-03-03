# 💻 CODE EXERCISES – Vue.js + Laravel Fullstack

> Làm từng bài, tự viết code TRƯỚC, rồi mới xem đáp án.  
> Mỗi bài có: 🎯 Yêu cầu | 💡 Gợi ý | ✅ Giải thích sâu

---

## 📋 DANH SÁCH BÀI TẬP

| # | Chủ đề | Level |
|---|---|---|
| [VUE-01](#vue-01-reactivity--computed) | Reactivity & Computed | ⭐ Dễ |
| [VUE-02](#vue-02-composable-usecounter) | Composable `useCounter` | ⭐ Dễ |
| [VUE-03](#vue-03-composable-usefetch) | Composable `useFetch` | ⭐⭐ Trung bình |
| [VUE-04](#vue-04-component-communication) | Component Communication | ⭐⭐ Trung bình |
| [VUE-05](#vue-05-custom-directive-v-debounce) | Custom Directive `v-debounce` | ⭐⭐⭐ Khó |
| [VUE-06](#vue-06-composable-usedebouncedsearch) | Composable `useDebouncedSearch` | ⭐⭐ Trung bình |
| [PINIA-01](#pinia-01-cart-store) | Cart Store với Pinia | ⭐⭐ Trung bình |
| [PINIA-02](#pinia-02-auth-store-với-persist) | Auth Store + Persist | ⭐⭐⭐ Khó |
| [NUXT-01](#nuxt-01-seo-dynamic-meta) | SEO Dynamic Meta | ⭐ Dễ |
| [NUXT-02](#nuxt-02-data-fetching--error-handling) | Data Fetching + Error | ⭐⭐ Trung bình |
| [LARAVEL-01](#laravel-01-eloquent-relationships) | Eloquent Relationships | ⭐⭐ Trung bình |
| [LARAVEL-02](#laravel-02-crud-api-hoàn-chỉnh) | CRUD API hoàn chỉnh | ⭐⭐⭐ Khó |
| [LARAVEL-03](#laravel-03-queue--job) | Queue + Job | ⭐⭐⭐ Khó |
| [API-01](#api-01-axios-interceptor-với-jwt) | Axios Interceptor + JWT | ⭐⭐⭐ Khó |

---

## VUE-01: Reactivity & Computed

### 🎯 Yêu cầu
Tạo một component **GioHang** (shopping cart) chỉ dùng Composition API:
- Danh sách sản phẩm với `{ id, name, price, qty }`
- Computed: `totalItems`, `totalPrice`, `discountedPrice` (giảm 10% nếu > 500k)
- Hàm: `increaseQty`, `decreaseQty` (min = 1), `removeItem`
- Hiển thị danh sách + tổng tiền

### 💡 Gợi ý
Dùng `reactive` cho array, `computed` cho các giá trị phái sinh.

### ✅ Đáp Án

```vue
<!-- GioHang.vue -->
<script setup>
import { reactive, computed } from 'vue'

const items = reactive([
  { id: 1, name: 'Áo thun', price: 150000, qty: 2 },
  { id: 2, name: 'Quần jean', price: 350000, qty: 1 },
  { id: 3, name: 'Giày sneaker', price: 500000, qty: 1 },
])

// ──────────────────────────────
// Computed Properties
// ──────────────────────────────
const totalItems = computed(() =>
  items.reduce((sum, item) => sum + item.qty, 0)
)

const totalPrice = computed(() =>
  items.reduce((sum, item) => sum + item.price * item.qty, 0)
)

// Giảm 10% nếu tổng > 500k
const discountedPrice = computed(() => {
  const total = totalPrice.value
  return total > 500000 ? total * 0.9 : total
})

const hasDiscount = computed(() => totalPrice.value > 500000)

// ──────────────────────────────
// Actions
// ──────────────────────────────
function increaseQty(id) {
  const item = items.find(i => i.id === id)
  if (item) item.qty++
}

function decreaseQty(id) {
  const item = items.find(i => i.id === id)
  if (item && item.qty > 1) item.qty--
}

function removeItem(id) {
  const index = items.findIndex(i => i.id === id)
  if (index !== -1) items.splice(index, 1)
}

// Format tiền VNĐ
const formatMoney = (val) =>
  val.toLocaleString('vi-VN', { style: 'currency', currency: 'VND' })
</script>

<template>
  <div class="cart">
    <h2>🛒 Giỏ Hàng ({{ totalItems }} sản phẩm)</h2>

    <div v-if="items.length === 0" class="empty">
      Giỏ hàng trống
    </div>

    <ul v-else>
      <li v-for="item in items" :key="item.id" class="cart-item">
        <span class="name">{{ item.name }}</span>
        <span class="price">{{ formatMoney(item.price) }}</span>

        <div class="qty-controls">
          <button @click="decreaseQty(item.id)" :disabled="item.qty <= 1">−</button>
          <span>{{ item.qty }}</span>
          <button @click="increaseQty(item.id)">+</button>
        </div>

        <span class="subtotal">{{ formatMoney(item.price * item.qty) }}</span>
        <button class="remove" @click="removeItem(item.id)">🗑</button>
      </li>
    </ul>

    <div class="summary">
      <p>Tổng gốc: <b>{{ formatMoney(totalPrice) }}</b></p>
      <p v-if="hasDiscount" class="discount">
        Giảm 10%: <b>{{ formatMoney(discountedPrice) }}</b>
      </p>
      <p v-else class="hint">Mua thêm để được giảm 10% (chưa đủ 500k)</p>
    </div>
  </div>
</template>
```

### 🔍 Giải Thích Sâu

**Tại sao dùng `reactive` thay vì `ref` cho array?**
- `reactive([...])` cho phép mutate trực tiếp (`item.qty++`, `items.splice(...)`) mà vẫn reactive.
- Nếu dùng `ref([...])`, phải `.value.splice(...)` và tránh reassign (dùng `.value = newArray` thay vì splice sẽ trigger re-render cả array).

**Tại sao `computed` tốt hơn `methods` ở đây?**
- `totalPrice` phụ thuộc vào `items`. Mỗi khi `items` thay đổi, `computed` tự tính lại VÀ cache kết quả.
- Nếu dùng `methods`, mỗi lần template re-render đều gọi lại hàm dù `items` không đổi.

**Tại sao `items.find()` trả về reference?**
- `reactive()` trả về Proxy. `items.find(i => i.id === id)` trả về Proxy của item đó → modify `item.qty++` trực tiếp update reactive state ngay.

---

## VUE-02: Composable `useCounter`

### 🎯 Yêu cầu
Viết composable `useCounter` với:
- `count`, `isEven`, `isNegative` (computed)
- `increment(step = 1)`, `decrement(step = 1)`, `reset()`, `setCount(val)`
- Option: `{ min, max, initialValue }` để giới hạn range

### ✅ Đáp Án

```javascript
// composables/useCounter.js
import { ref, computed } from 'vue'

export function useCounter(options = {}) {
  const {
    initialValue = 0,
    min = -Infinity,
    max = Infinity,
  } = options

  const count = ref(initialValue)

  // Computed
  const isEven    = computed(() => count.value % 2 === 0)
  const isNegative = computed(() => count.value < 0)
  const progress  = computed(() => {
    if (max === Infinity) return null
    return ((count.value - min) / (max - min)) * 100
  })

  // Clamp helper
  function clamp(val) {
    return Math.min(Math.max(val, min), max)
  }

  // Actions
  function increment(step = 1) { count.value = clamp(count.value + step) }
  function decrement(step = 1) { count.value = clamp(count.value - step) }
  function reset()              { count.value = initialValue }
  function setCount(val)        { count.value = clamp(val) }

  return { count, isEven, isNegative, progress, increment, decrement, reset, setCount }
}
```

```vue
<!-- Sử dụng trong component -->
<script setup>
import { useCounter } from '@/composables/useCounter'

// Counter bình thường
const { count, isEven, increment, decrement, reset } = useCounter({ initialValue: 0 })

// Counter có giới hạn (ví dụ: chọn số lượng 1-10)
const qty = useCounter({ initialValue: 1, min: 1, max: 10 })
</script>

<template>
  <div>
    <button @click="decrement()">-</button>
    <span :class="{ even: isEven }">{{ count }}</span>
    <button @click="increment()">+</button>
    <button @click="reset()">Reset</button>
  </div>

  <!-- Qty selector có giới hạn -->
  <div>
    <button @click="qty.decrement()" :disabled="qty.count.value <= 1">-</button>
    <span>{{ qty.count }}</span>
    <button @click="qty.increment()" :disabled="qty.count.value >= 10">+</button>
  </div>
</template>
```

### 🔍 Giải Thích Sâu

**Tại sao cần destructure và composable pattern?**
```javascript
// ❌ Không dùng composable – logic rải rác trong component
const count = ref(0)
const isEven = computed(() => count.value % 2 === 0)
function increment() { count.value++ }
// → Khó tái sử dụng, khó test

// ✅ Dùng composable
const { count, isEven, increment } = useCounter()
// → Tái sử dụng, test độc lập, logic gom 1 chỗ
```

**Option object pattern:**
Truyền options dưới dạng object thay vì positional args giúp:
- Rõ nghĩa hơn: `useCounter({ min: 0, max: 10 })` vs `useCounter(0, 0, 10)`
- Dễ mở rộng sau này mà không break API hiện tại

---

## VUE-03: Composable `useFetch`

### 🎯 Yêu cầu
Viết composable `useFetch` đủ mạnh:
- States: `data`, `loading`, `error`
- Options: `{ immediate, transform, onSuccess, onError }`
- Auto-abort khi component unmount (tránh memory leak)
- Refresh function

### ✅ Đáp Án

```javascript
// composables/useFetch.js
import { ref, onUnmounted } from 'vue'

export function useFetch(url, options = {}) {
  const {
    immediate = true,        // Tự fetch khi mount
    transform = (data) => data, // Transform response
    onSuccess = null,
    onError = null,
  } = options

  const data    = ref(null)
  const loading = ref(false)
  const error   = ref(null)

  let controller = null   // AbortController để cancel request

  async function fetchData(params = {}) {
    // Hủy request trước nếu đang chạy
    if (controller) controller.abort()
    controller = new AbortController()

    loading.value = true
    error.value   = null

    try {
      const queryString = new URLSearchParams(params).toString()
      const fullUrl = queryString ? `${url}?${queryString}` : url

      const res = await fetch(fullUrl, {
        signal: controller.signal,         // Gắn abort signal
        headers: { 'Accept': 'application/json' }
      })

      if (!res.ok) throw new Error(`HTTP ${res.status}: ${res.statusText}`)

      const json = await res.json()
      data.value = transform(json)         // Apply transform

      onSuccess?.(data.value)             // Callback nếu có
    } catch (e) {
      if (e.name === 'AbortError') return  // Bỏ qua nếu bị abort
      error.value = e.message
      onError?.(e)
    } finally {
      loading.value = false
    }
  }

  // Cleanup: hủy request khi component unmount
  onUnmounted(() => controller?.abort())

  // Auto fetch nếu immediate = true
  if (immediate) fetchData()

  return { data, loading, error, refresh: fetchData }
}
```

```vue
<script setup>
import { ref } from 'vue'
import { useFetch } from '@/composables/useFetch'

// Fetch danh sách posts
const { data: posts, loading, error, refresh } = useFetch(
  'https://jsonplaceholder.typicode.com/posts',
  {
    transform: (data) => data.slice(0, 10),   // Chỉ lấy 10 bài đầu
    onSuccess: (data) => console.log('Loaded', data.length, 'posts'),
    onError: (e) => console.error('Failed:', e.message),
  }
)

// Fetch không tự động, cần gọi thủ công
const search = ref('')
const { data: results, loading: searching, refresh: doSearch } = useFetch(
  '/api/search',
  { immediate: false, transform: (res) => res.data }
)
</script>

<template>
  <div v-if="loading">Loading...</div>
  <div v-else-if="error" class="error">{{ error }}</div>
  <ul v-else>
    <li v-for="post in posts" :key="post.id">{{ post.title }}</li>
  </ul>
  <button @click="refresh()">Tải lại</button>
</template>
```

### 🔍 Giải Thích Sâu

**AbortController – tại sao quan trọng?**
```javascript
// ❌ Không có abort – memory leak và race condition
// User click nút tải → fetch A bắt đầu
// User click lại   → fetch B bắt đầu
// B resolve trước A → hiển thị B
// A resolve         → GHI ĐÈ lên B! ← Race condition

// ✅ Có abort
// Fetch B: controller.abort() hủy A trước khi fetch B
// Chỉ có 1 request active tại một thời điểm
```

**`onUnmounted` cleanup:**
```javascript
// Component unmount mà không abort → request vẫn chạy
// Khi resolve → cố gắng set data.value trên component đã bị destroy
// → Vue warning: "Set operation on key "value" failed: target is readonly"
```

---

## VUE-04: Component Communication

### 🎯 Yêu cầu
Xây dựng **ProductFilter** component:
- Parent truyền `filters` (object) xuống
- Child (FilterForm) emit `update:filters` khi user thay đổi
- Dùng `v-model:filters` từ parent
- Dùng `provide/inject` cho theme (dark/light)

### ✅ Đáp Án

```vue
<!-- FilterForm.vue (Child) -->
<script setup>
const props = defineProps({
  filters: {
    type: Object,
    required: true,
    // { search: '', category: 'all', minPrice: 0, maxPrice: 9999999 }
  }
})

const emit = defineEmits(['update:filters'])

// Helper để update 1 field mà không mutate props trực tiếp
function updateFilter(key, value) {
  emit('update:filters', { ...props.filters, [key]: value })
}

function resetFilters() {
  emit('update:filters', {
    search: '',
    category: 'all',
    minPrice: 0,
    maxPrice: 9999999
  })
}

// Inject theme từ ancestor
import { inject } from 'vue'
const theme = inject('theme', 'light')  // default: 'light'
</script>

<template>
  <div :class="['filter-form', `theme-${theme}`]">
    <input
      :value="filters.search"
      @input="updateFilter('search', $event.target.value)"
      placeholder="Tìm kiếm..."
    />

    <select :value="filters.category" @change="updateFilter('category', $event.target.value)">
      <option value="all">Tất cả</option>
      <option value="shoes">Giày</option>
      <option value="clothes">Quần áo</option>
    </select>

    <div class="price-range">
      <input type="number" :value="filters.minPrice"
             @input="updateFilter('minPrice', +$event.target.value)" />
      <span>-</span>
      <input type="number" :value="filters.maxPrice"
             @input="updateFilter('maxPrice', +$event.target.value)" />
    </div>

    <button @click="resetFilters">Reset</button>
  </div>
</template>
```

```vue
<!-- ProductPage.vue (Parent) -->
<script setup>
import { ref, computed, provide } from 'vue'
import FilterForm from './FilterForm.vue'

// Provide theme cho tất cả descendant
const theme = ref('dark')
provide('theme', theme)  // Reactive provide

const filters = ref({
  search: '',
  category: 'all',
  minPrice: 0,
  maxPrice: 9999999
})

const allProducts = ref([
  { id: 1, name: 'Giày Nike', category: 'shoes', price: 2500000 },
  { id: 2, name: 'Áo thun', category: 'clothes', price: 150000 },
])

const filteredProducts = computed(() => {
  return allProducts.value.filter(p => {
    const matchSearch   = p.name.toLowerCase().includes(filters.value.search.toLowerCase())
    const matchCategory = filters.value.category === 'all' || p.category === filters.value.category
    const matchPrice    = p.price >= filters.value.minPrice && p.price <= filters.value.maxPrice
    return matchSearch && matchCategory && matchPrice
  })
})
</script>

<template>
  <!-- v-model:filters = :filters + @update:filters -->
  <FilterForm v-model:filters="filters" />

  <div class="products">
    <p>{{ filteredProducts.length }} sản phẩm</p>
    <div v-for="p in filteredProducts" :key="p.id">{{ p.name }}</div>
  </div>
</template>
```

### 🔍 Giải Thích Sâu

**Tại sao không mutate props trực tiếp?**
```javascript
// ❌ Vi phạm one-way data flow
props.filters.search = 'abc'  // Vue warning + khó debug

// ✅ Emit để parent tự update
emit('update:filters', { ...props.filters, search: 'abc' })
// →  Parent nhận event → update ref → truyền xuống lại
// → Data flow rõ ràng, trace-able
```

**`v-model` với prop khác `modelValue`:**
```vue
<!-- Cú pháp đầy đủ -->
<FilterForm :filters="filters" @update:filters="filters = $event" />

<!-- Shorthand với v-model -->
<FilterForm v-model:filters="filters" />
```

---

## VUE-05: Custom Directive `v-debounce`

### 🎯 Yêu cầu
Tạo directive `v-debounce` để debounce input event:
```vue
<input v-debounce:500="onSearch" />
<!-- Gọi onSearch sau 500ms không có input mới -->
```

### ✅ Đáp Án

```javascript
// directives/vDebounce.js
export const vDebounce = {
  mounted(el, binding) {
    const delay = parseInt(binding.arg) || 300  // v-debounce:500 → arg = '500'
    const handler = binding.value               // Hàm callback

    let timer = null

    el._debounceHandler = (e) => {
      clearTimeout(timer)
      timer = setTimeout(() => handler(e.target.value, e), delay)
    }

    el._cleanupTimer = () => clearTimeout(timer)

    el.addEventListener('input', el._debounceHandler)
  },

  // Khi binding thay đổi (handler mới)
  updated(el, binding) {
    if (binding.value !== binding.oldValue) {
      el.removeEventListener('input', el._debounceHandler)

      const delay = parseInt(binding.arg) || 300
      const handler = binding.value
      let timer = null

      el._debounceHandler = (e) => {
        clearTimeout(timer)
        timer = setTimeout(() => handler(e.target.value, e), delay)
      }

      el.addEventListener('input', el._debounceHandler)
    }
  },

  unmounted(el) {
    el.removeEventListener('input', el._debounceHandler)
    el._cleanupTimer?.()
  }
}

// Đăng ký global (main.js)
// app.directive('debounce', vDebounce)
```

```vue
<!-- Sử dụng -->
<script setup>
import { ref } from 'vue'
import { vDebounce } from '@/directives/vDebounce'

const results = ref([])
const query   = ref('')

async function onSearch(value) {
  query.value = value
  if (!value.trim()) { results.value = []; return }

  const res = await fetch(`/api/search?q=${value}`)
  results.value = await res.json()
}
</script>

<template>
  <!-- Debounce 500ms -->
  <input v-debounce:500="onSearch" placeholder="Tìm kiếm..." />
  <p>Đang tìm: "{{ query }}"</p>
  <ul>
    <li v-for="r in results" :key="r.id">{{ r.name }}</li>
  </ul>
</template>
```

---

## VUE-06: Composable `useDebouncedSearch`

### 🎯 Yêu cầu
Kết hợp debounce + fetch thành 1 composable:
- `query` ref người dùng type vào
- Auto search sau 400ms không type tiếp
- Hiển thị `loading`, `results`, `error`

### ✅ Đáp Án

```javascript
// composables/useDebouncedSearch.js
import { ref, watch } from 'vue'

export function useDebouncedSearch(endpoint, { delay = 400, minLength = 2 } = {}) {
  const query   = ref('')
  const results = ref([])
  const loading = ref(false)
  const error   = ref(null)

  let timer = null
  let controller = null

  async function performSearch(q) {
    if (controller) controller.abort()
    controller = new AbortController()

    loading.value = true
    error.value   = null

    try {
      const res = await fetch(`${endpoint}?q=${encodeURIComponent(q)}`, {
        signal: controller.signal
      })
      const data = await res.json()
      results.value = data
    } catch (e) {
      if (e.name !== 'AbortError') error.value = e.message
    } finally {
      loading.value = false
    }
  }

  watch(query, (newQ) => {
    clearTimeout(timer)
    results.value = []

    if (!newQ || newQ.trim().length < minLength) return

    timer = setTimeout(() => performSearch(newQ.trim()), delay)
  })

  function clear() {
    query.value = ''
    results.value = []
    clearTimeout(timer)
    controller?.abort()
  }

  return { query, results, loading, error, clear }
}
```

---

## PINIA-01: Cart Store

### 🎯 Yêu cầu
Tạo `useCartStore` hoàn chỉnh:
- `addItem`, `removeItem`, `updateQty`, `clearCart`
- Getters: `totalItems`, `totalPrice`, `isEmpty`
- Persist items trong `localStorage`

### ✅ Đáp Án

```javascript
// stores/useCartStore.js
import { defineStore } from 'pinia'

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: JSON.parse(localStorage.getItem('cart') || '[]'),
  }),

  getters: {
    totalItems:  (state) => state.items.reduce((sum, i) => sum + i.qty, 0),
    totalPrice:  (state) => state.items.reduce((sum, i) => sum + i.price * i.qty, 0),
    isEmpty:     (state) => state.items.length === 0,

    // Getter dùng getter khác
    formattedTotal() {
      return this.totalPrice.toLocaleString('vi-VN') + 'đ'
    },

    // Getter nhận argument (trả về function)
    getItemById: (state) => (id) => state.items.find(i => i.id === id),
  },

  actions: {
    addItem(product, qty = 1) {
      const existing = this.items.find(i => i.id === product.id)
      if (existing) {
        existing.qty += qty
      } else {
        this.items.push({
          id:    product.id,
          name:  product.name,
          price: product.price,
          image: product.image,
          qty,
        })
      }
      this._saveToStorage()
    },

    removeItem(productId) {
      const idx = this.items.findIndex(i => i.id === productId)
      if (idx !== -1) {
        this.items.splice(idx, 1)
        this._saveToStorage()
      }
    },

    updateQty(productId, qty) {
      if (qty <= 0) { this.removeItem(productId); return }
      const item = this.items.find(i => i.id === productId)
      if (item) {
        item.qty = qty
        this._saveToStorage()
      }
    },

    clearCart() {
      this.items = []
      localStorage.removeItem('cart')
    },

    // Private helper (convention: prefix với _)
    _saveToStorage() {
      localStorage.setItem('cart', JSON.stringify(this.items))
    }
  }
})
```

```vue
<!-- CartIcon.vue -->
<script setup>
import { storeToRefs } from 'pinia'
import { useCartStore } from '@/stores/useCartStore'

const cartStore = useCartStore()
// storeToRefs: destructure reactive state + getters (giữ reactivity)
const { totalItems, totalPrice, isEmpty, formattedTotal } = storeToRefs(cartStore)
// Actions: lấy trực tiếp (không cần storeToRefs)
const { addItem, removeItem, clearCart } = cartStore
</script>

<template>
  <div class="cart-icon">
    🛒 <span v-if="!isEmpty" class="badge">{{ totalItems }}</span>
  </div>

  <div class="cart-summary">
    <p v-if="isEmpty">Giỏ hàng trống</p>
    <p v-else>Tổng: {{ formattedTotal }}</p>
    <button @click="clearCart" :disabled="isEmpty">Xóa tất cả</button>
  </div>
</template>
```

### 🔍 Giải Thích Sâu

**`storeToRefs` vs destructure thông thường:**
```javascript
const store = useCartStore()

// ❌ BAD – mất reactivity, là primitive value tại thời điểm destructure
const { totalItems, totalPrice } = store
// totalItems là số 3, không reactive

// ✅ GOOD – storeToRefs wrap thành ref
const { totalItems, totalPrice } = storeToRefs(store)
// totalItems.value = 3, reactive!

// Actions: lấy trực tiếp OK (function, không cần reactive)
const { addItem } = store
```

**Getter nhận argument:**
```javascript
// Getter trả về function (gọi là "getter factory")
getItemById: (state) => (id) => state.items.find(i => i.id === id)

// Trong component
const store = useCartStore()
const item = store.getItemById(123)  // Trả về item hoặc undefined
```

---

## PINIA-02: Auth Store với Persist

### 🎯 Yêu cầu
Tạo auth store dùng **Composition Store** syntax:
- Login/logout với API call
- Token lưu httpOnly cookie (simulate) hoặc memory
- `isLoggedIn`, `user` reactive
- Auto-fetch user khi app boot

### ✅ Đáp Án

```javascript
// stores/useAuthStore.js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  // ── State ──────────────────────────────
  const user  = ref(null)
  const token = ref(sessionStorage.getItem('token') || null)
  // sessionStorage: clear khi đóng tab (an toàn hơn localStorage)

  // ── Getters ────────────────────────────
  const isLoggedIn = computed(() => !!token.value && !!user.value)
  const isAdmin    = computed(() => user.value?.role === 'admin')
  const userName   = computed(() => user.value?.name || 'Guest')

  // ── Actions ────────────────────────────
  async function login(credentials) {
    try {
      const res = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials)
      })

      if (!res.ok) {
        const err = await res.json()
        throw new Error(err.message || 'Login failed')
      }

      const data = await res.json()
      token.value = data.token
      user.value  = data.user
      sessionStorage.setItem('token', data.token)

      return { success: true }
    } catch (e) {
      return { success: false, error: e.message }
    }
  }

  async function fetchCurrentUser() {
    if (!token.value) return

    try {
      const res = await fetch('/api/auth/me', {
        headers: { Authorization: `Bearer ${token.value}` }
      })

      if (!res.ok) { logout(); return }  // Token expired

      user.value = await res.json()
    } catch {
      logout()
    }
  }

  function logout() {
    user.value  = null
    token.value = null
    sessionStorage.removeItem('token')
  }

  // ── Return ─────────────────────────────
  return { user, token, isLoggedIn, isAdmin, userName, login, logout, fetchCurrentUser }
})
```

```javascript
// app.vue – Boot: fetch user khi app mount
import { onMounted } from 'vue'
import { useAuthStore } from '@/stores/useAuthStore'

const authStore = useAuthStore()
onMounted(() => authStore.fetchCurrentUser())
```

---

## NUXT-01: SEO Dynamic Meta

### 🎯 Yêu cầu
Tạo trang blog detail với Nuxt 3:
- Fetch bài viết theo `slug` từ route param
- Đặt dynamic SEO: title, description, og:image, canonical
- Xử lý trường hợp bài không tồn tại

### ✅ Đáp Án

```vue
<!-- pages/blog/[slug].vue -->
<script setup>
const route = useRoute()
const config = useRuntimeConfig()

// Fetch bài viết
const { data: post, error } = await useFetch(
  `/api/blog/${route.params.slug}`,
  { transform: (res) => res.data }
)

// 404 nếu bài không tồn tại
if (!post.value || error.value) {
  throw createError({ statusCode: 404, statusMessage: 'Bài viết không tồn tại' })
}

// Dynamic SEO
useSeoMeta({
  // Basic meta
  title: () => `${post.value?.title} | Blog`,
  description: () => post.value?.excerpt,

  // Open Graph (Facebook, Zalo)
  ogTitle: () => post.value?.title,
  ogDescription: () => post.value?.excerpt,
  ogImage: () => post.value?.thumbnail ?? `${config.public.siteUrl}/og-default.jpg`,
  ogType: 'article',
  ogUrl: () => `${config.public.siteUrl}/blog/${route.params.slug}`,

  // Twitter Card
  twitterCard: 'summary_large_image',
  twitterTitle: () => post.value?.title,
  twitterImage: () => post.value?.thumbnail,

  // Article meta
  articlePublishedTime: () => post.value?.published_at,
  articleAuthor: () => post.value?.author?.name,
})

// Canonical URL (tránh duplicate content)
useHead({
  link: [{ rel: 'canonical', href: `${config.public.siteUrl}/blog/${route.params.slug}` }]
})
</script>

<template>
  <article v-if="post">
    <img :src="post.thumbnail" :alt="post.title" />
    <h1>{{ post.title }}</h1>
    <p class="meta">
      Đăng bởi {{ post.author.name }} · {{ new Date(post.published_at).toLocaleDateString('vi-VN') }}
    </p>
    <div v-html="post.content" />
  </article>
</template>
```

### 🔍 Giải Thích Sâu

**Reactive SEO meta với arrow function:**
```javascript
// ❌ Không reactive – set 1 lần khi setup
useSeoMeta({ title: post.value?.title })

// ✅ Reactive – tự cập nhật khi post.value thay đổi
useSeoMeta({ title: () => post.value?.title })
// Dùng arrow function → Nuxt track dependency
```

**`createError` với statusCode:**
- Trả về trang lỗi với HTTP status code đúng
- Server sẽ response 404 (not 200 với content "not found") → SEO đúng
- Client sẽ hiển thị trang lỗi tùy chỉnh (`error.vue`)

---

## NUXT-02: Data Fetching & Error Handling

### 🎯 Yêu cầu
Tạo trang danh sách sản phẩm với:
- Pagination + search (persist trong URL query)
- Loading skeleton khi fetch
- Error boundary
- Refresh khi filter thay đổi

### ✅ Đáp Án

```vue
<!-- pages/products/index.vue -->
<script setup>
const route  = useRoute()
const router = useRouter()

// Sync với URL query params
const page   = computed(() => parseInt(route.query.page) || 1)
const search = computed(() => route.query.search || '')

// Fetch với watch: auto re-fetch khi page/search thay đổi
const {
  data,
  pending,
  error,
  refresh
} = await useFetch('/api/products', {
  query: computed(() => ({ page: page.value, search: search.value, limit: 12 })),
  lazy: true,   // Không block render, hiện skeleton trước
})

const products   = computed(() => data.value?.data || [])
const pagination = computed(() => data.value?.meta || {})

// Update URL khi filter thay đổi (không reload trang)
function goToPage(p) {
  router.push({ query: { ...route.query, page: p } })
}

function onSearch(q) {
  router.push({ query: { search: q, page: 1 } }) // Reset về trang 1
}
</script>

<template>
  <div>
    <!-- Search input -->
    <input :value="search" @input="onSearch($event.target.value)" placeholder="Tìm sản phẩm..." />

    <!-- Error state -->
    <div v-if="error" class="error">
      Lỗi tải dữ liệu: {{ error.message }}
      <button @click="refresh()">Thử lại</button>
    </div>

    <!-- Loading skeleton -->
    <div v-else-if="pending" class="grid">
      <div v-for="i in 12" :key="i" class="skeleton-card">
        <div class="skeleton" style="height: 200px" />
        <div class="skeleton" style="height: 20px; margin-top: 8px" />
        <div class="skeleton" style="height: 16px; width: 60%; margin-top: 6px" />
      </div>
    </div>

    <!-- Product list -->
    <div v-else class="grid">
      <ProductCard v-for="p in products" :key="p.id" :product="p" />
    </div>

    <!-- Pagination -->
    <div class="pagination" v-if="pagination.last_page > 1">
      <button :disabled="page <= 1" @click="goToPage(page - 1)">← Trước</button>
      <span>{{ page }} / {{ pagination.last_page }}</span>
      <button :disabled="page >= pagination.last_page" @click="goToPage(page + 1)">Sau →</button>
    </div>
  </div>
</template>
```

### 🔍 Giải Thích Sâu

**Tại sao dùng URL query params cho pagination/search?**
1. **Shareable**: Copy URL chia sẻ cho người khác → họ thấy cùng kết quả
2. **Browser history**: Back button hoạt động đúng
3. **SEO**: Crawler index từng trang
4. **Refresh safe**: F5 không mất trạng thái

**`lazy: true` và skeleton loading:**
```javascript
// lazy: false (default) – block render đến khi fetch xong
// → User thấy trang trắng, sau đó hiện content đột ngột

// lazy: true – render ngay, pending = true
// → User thấy skeleton ngay → UX mượt hơn
```

---

## LARAVEL-01: Eloquent Relationships

### 🎯 Yêu cầu
Hệ thống blog đơn giản:
- `User` hasMany `Post`
- `Post` belongsTo `User`, hasMany `Comment`, belongsToMany `Tag`
- `Comment` belongsTo `Post`, belongsTo `User`
- Query: lấy 10 posts mới nhất, kèm author name, tag names, comment count
- Tránh N+1

### ✅ Đáp Án

```php
// app/Models/User.php
class User extends Model
{
    public function posts(): HasMany    { return $this->hasMany(Post::class); }
    public function comments(): HasMany { return $this->hasMany(Comment::class); }
}

// app/Models/Post.php
class Post extends Model
{
    use SoftDeletes;

    protected $fillable = ['user_id', 'title', 'slug', 'content', 'published_at'];
    protected $casts    = ['published_at' => 'datetime'];

    public function user(): BelongsTo       { return $this->belongsTo(User::class); }
    public function comments(): HasMany     { return $this->hasMany(Comment::class); }
    public function tags(): BelongsToMany   { return $this->belongsToMany(Tag::class)->withTimestamps(); }

    // Scope: chỉ lấy bài đã publish
    public function scopePublished($q)
    {
        return $q->whereNotNull('published_at')
                 ->where('published_at', '<=', now());
    }

    // Scope: search theo title
    public function scopeSearch($q, $term)
    {
        return $q->where('title', 'like', "%{$term}%");
    }
}

// app/Models/Comment.php
class Comment extends Model
{
    protected $fillable = ['post_id', 'user_id', 'content'];

    public function post(): BelongsTo { return $this->belongsTo(Post::class); }
    public function user(): BelongsTo { return $this->belongsTo(User::class); }
}

// app/Models/Tag.php
class Tag extends Model
{
    protected $fillable = ['name', 'slug'];

    public function posts(): BelongsToMany { return $this->belongsToMany(Post::class); }
}
```

```php
// ✅ Query tối ưu – tránh N+1
$posts = Post::published()
    ->with([
        'user:id,name,avatar',      // Chỉ lấy các cột cần thiết
        'tags:id,name,slug',
    ])
    ->withCount('comments')         // Thêm comments_count tự động
    ->latest('published_at')
    ->paginate(10);

// Trong Resource/Controller
// $post->user->name     → OK – đã eager load
// $post->comments_count → OK – withCount
// $post->tags           → OK – đã eager load

// ❌ N+1 – LỖI phổ biến
$posts = Post::published()->latest()->get();
foreach ($posts as $post) {
    echo $post->user->name;       // N queries!
    echo $post->comments()->count(); // N queries!
    foreach ($post->tags as $tag) {}  // N queries!
}
```

```php
// Migration cho pivot table (tags_posts)
Schema::create('post_tag', function (Blueprint $table) {
    $table->foreignId('post_id')->constrained()->cascadeOnDelete();
    $table->foreignId('tag_id')->constrained()->cascadeOnDelete();
    $table->timestamps();
    $table->primary(['post_id', 'tag_id']);  // Composite primary key
});

// Sync tags (BelongsToMany)
$post->tags()->sync([1, 2, 3]);         // Replace tất cả tags
$post->tags()->attach([4, 5]);          // Thêm tags
$post->tags()->detach([1]);             // Xóa 1 tag
$post->tags()->syncWithoutDetaching([6]); // Thêm mà không xóa cũ
```

### 🔍 Giải Thích Sâu

**`with('user:id,name')` – tại sao cần select columns?**
```php
// Không select → lấy tất cả columns của user (kể cả password hash, etc.)
->with('user')

// Select columns cụ thể → performance + security
->with('user:id,name,avatar')
// ⚠️ PHẢI include 'id' (foreign key) để Eloquent map relationship đúng
```

**`withCount` vs custom query:**
```php
// withCount – được Eloquent tối ưu thành LEFT JOIN subquery
->withCount('comments')
// → Thêm column comments_count vào result

// Thay thế kém hơn:
$posts->each(fn($p) => $p->comment_count = $p->comments()->count())
// → N+1 queries
```

---

## LARAVEL-02: CRUD API Hoàn Chỉnh

### 🎯 Yêu cầu
Xây dựng Product API đầy đủ:
- Route: `apiResource`
- FormRequest riêng cho create/update
- API Resource với conditional fields
- Pagination, filter, search
- Xử lý lỗi nhất quán

### ✅ Đáp Án

```php
// routes/api.php
Route::middleware('auth:sanctum')->group(function () {
    Route::apiResource('products', ProductController::class);
    // GET    /api/products          → index
    // POST   /api/products          → store
    // GET    /api/products/{product} → show
    // PUT    /api/products/{product} → update
    // DELETE /api/products/{product} → destroy
});
```

```php
// app/Http/Controllers/ProductController.php
class ProductController extends Controller
{
    public function index(Request $request): JsonResponse
    {
        $products = Product::query()
            ->with('category:id,name')
            ->withCount('reviews')
            ->when($request->search, fn($q) => $q->where('name', 'like', "%{$request->search}%"))
            ->when($request->category_id, fn($q) => $q->where('category_id', $request->category_id))
            ->when($request->min_price, fn($q) => $q->where('price', '>=', $request->min_price))
            ->when($request->max_price, fn($q) => $q->where('price', '<=', $request->max_price))
            ->when(
                $request->sort,
                fn($q) => $q->orderBy($request->sort, $request->direction ?? 'asc'),
                fn($q) => $q->latest()    // Default: mới nhất
            )
            ->paginate($request->per_page ?? 15)
            ->withQueryString();   // Giữ query params trong pagination links

        return ProductResource::collection($products)->response();
    }

    public function store(StoreProductRequest $request): JsonResponse
    {
        $product = Product::create($request->validated());

        // Sync nhiều-nhiều
        if ($request->has('tag_ids')) {
            $product->tags()->sync($request->tag_ids);
        }

        $product->load(['category', 'tags']);
        return (new ProductResource($product))->response()->setStatusCode(201);
    }

    public function show(Product $product): JsonResponse
    {
        $product->load(['category', 'tags', 'reviews.user:id,name']);
        return new ProductResource($product);
    }

    public function update(UpdateProductRequest $request, Product $product): JsonResponse
    {
        $this->authorize('update', $product);   // Policy check

        $product->update($request->validated());

        if ($request->has('tag_ids')) {
            $product->tags()->sync($request->tag_ids);
        }

        $product->load(['category', 'tags']);
        return new ProductResource($product);
    }

    public function destroy(Product $product): JsonResponse
    {
        $this->authorize('delete', $product);
        $product->delete();   // SoftDelete
        return response()->json(['message' => 'Xóa thành công'], 200);
    }
}
```

```php
// app/Http/Requests/StoreProductRequest.php
class StoreProductRequest extends FormRequest
{
    public function authorize(): bool
    {
        return $this->user()->can('create', Product::class);
    }

    public function rules(): array
    {
        return [
            'name'        => ['required', 'string', 'max:255'],
            'description' => ['nullable', 'string'],
            'price'       => ['required', 'numeric', 'min:0'],
            'stock'       => ['required', 'integer', 'min:0'],
            'category_id' => ['required', 'exists:categories,id'],
            'tag_ids'     => ['nullable', 'array'],
            'tag_ids.*'   => ['integer', 'exists:tags,id'],
            'image'       => ['nullable', 'image', 'max:2048'],
        ];
    }
}

// app/Http/Requests/UpdateProductRequest.php
class UpdateProductRequest extends StoreProductRequest
{
    public function rules(): array
    {
        // Update: tất cả optional, nhưng nếu có thì phải valid
        return array_map(
            fn($rules) => array_filter($rules, fn($r) => $r !== 'required'),
            parent::rules()
        );
        // Hoặc viết explicit:
        return [
            'name'  => ['sometimes', 'string', 'max:255'],
            'price' => ['sometimes', 'numeric', 'min:0'],
            // ...
        ];
    }
}
```

---

## LARAVEL-03: Queue & Job

### 🎯 Yêu cầu
Sau khi đặt hàng thành công:
1. Gửi email xác nhận đặt hàng
2. Cập nhật inventory (trừ stock)
3. Notify admin qua Slack
4. Nếu payment fail → gửi email thử lại sau 5 phút (3 lần)

### ✅ Đáp Án

```php
// app/Jobs/ProcessOrder.php
class ProcessOrder implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public int $tries    = 1;      // Chỉ thử 1 lần
    public int $timeout  = 120;

    public function __construct(
        public readonly Order $order
    ) {}

    public function handle(PaymentService $payment, InventoryService $inventory): void
    {
        // 1. Charge payment
        $result = $payment->charge($this->order);

        if (!$result->success) {
            // Dispatch job khác để retry payment
            RetryPayment::dispatch($this->order)->delay(now()->addMinutes(5));
            return;
        }

        // 2. Update inventory (trong transaction)
        DB::transaction(function () use ($inventory) {
            foreach ($this->order->items as $item) {
                $inventory->decreaseStock($item->product_id, $item->qty);
            }
            $this->order->update(['status' => 'paid']);
        });

        // 3. Fire event → listeners tự xử lý
        event(new OrderPaid($this->order));
    }

    public function failed(\Throwable $e): void
    {
        Log::error('ProcessOrder failed', [
            'order_id' => $this->order->id,
            'error'    => $e->getMessage(),
        ]);

        $this->order->update(['status' => 'failed']);
        // Notify admin
        Notification::route('slack', config('services.slack.webhook'))
            ->notify(new OrderFailed($this->order, $e));
    }
}

// app/Jobs/RetryPayment.php
class RetryPayment implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public int $tries   = 3;           // Retry 3 lần
    public int $timeout = 60;

    // Backoff: lần 1 sau 5 phút, lần 2 sau 15 phút, lần 3 sau 30 phút
    public function backoff(): array
    {
        return [300, 900, 1800];
    }

    public function __construct(public readonly Order $order) {}

    public function handle(PaymentService $payment): void
    {
        $result = $payment->charge($this->order);

        if (!$result->success) {
            throw new \Exception('Payment retry failed: ' . $result->message);
            // → Sẽ retry theo backoff schedule
        }

        $this->order->update(['status' => 'paid']);
        event(new OrderPaid($this->order));
    }

    public function failed(\Throwable $e): void
    {
        // Tất cả retries đã thất bại
        $this->order->update(['status' => 'payment_failed']);
        Mail::to($this->order->user)->send(new PaymentFailedMail($this->order));
    }
}
```

```php
// app/Events/OrderPaid.php
class OrderPaid
{
    public function __construct(public readonly Order $order) {}
}

// app/Listeners/SendOrderConfirmationEmail.php
class SendOrderConfirmationEmail implements ShouldQueue
{
    public function handle(OrderPaid $event): void
    {
        Mail::to($event->order->user->email)
            ->send(new OrderConfirmationMail($event->order));
    }
}

// app/Listeners/NotifyAdminOrderPaid.php
class NotifyAdminOrderPaid implements ShouldQueue
{
    public function handle(OrderPaid $event): void
    {
        Notification::route('slack', config('services.slack.webhook'))
            ->notify(new NewOrderNotification($event->order));
    }
}

// app/Providers/EventServiceProvider.php
protected $listen = [
    OrderPaid::class => [
        SendOrderConfirmationEmail::class,  // Mỗi listener là 1 job riêng trong queue
        NotifyAdminOrderPaid::class,
        UpdateCustomerLoyaltyPoints::class,
    ],
];

// Dispatch từ controller sau khi tạo order
ProcessOrder::dispatch($order)->onQueue('orders');

// Chạy worker
// php artisan queue:work redis --queue=orders --tries=3
```

### �� Giải Thích Sâu

**Tại sao Event/Listener tốt hơn gọi trực tiếp?**
```php
// ❌ Tightly coupled – controller biết quá nhiều
public function store(Request $request)
{
    $order = Order::create($data);
    Mail::to($order->user)->send(new ConfirmationMail($order));    // Sync!
    SlackService::notify($order);
    LoyaltyService::addPoints($order);
    // → Controller làm quá nhiều, khó test, blocking
}

// ✅ Event-driven – Controller chỉ fire event
public function store(Request $request)
{
    $order = Order::create($data);
    event(new OrderPaid($order));  // Xong, Listener tự làm sau
    return response()->json($order, 201);
    // → Fast response, listeners chạy async trong queue
}
```

**`SerializesModels` trait:**
- Job được **serialize** để lưu vào queue (Redis/DB)
- `SerializesModels` tự động serialize Model thành `{ id, class }` thay vì toàn bộ object
- Khi worker pick up job → deserialize → fetch lại model từ DB với data mới nhất
- Tránh race condition: data trong job luôn fresh

---

## API-01: Axios Interceptor với JWT

### 🎯 Yêu cầu
Cài đặt Axios hoàn chỉnh cho Vue app:
- Tự động gắn token vào header
- Tự động refresh token khi 401
- Handle concurrent requests (queue chờ refresh)
- Loading indicator global
- Error toast global

### ✅ Đáp Án

```javascript
// lib/api.js
import axios from 'axios'

let isRefreshing = false
let pendingRequests = []

// Helper: resolve tất cả pending requests với token mới
function resolvePending(token) {
  pendingRequests.forEach(({ resolve }) => resolve(token))
  pendingRequests = []
}

// Helper: reject tất cả pending requests
function rejectPending(error) {
  pendingRequests.forEach(({ reject }) => reject(error))
  pendingRequests = []
}

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '/api',
  timeout: 15000,
  headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }
})

// ─── Request Interceptor ────────────────────────────────
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token')
    if (token) config.headers.Authorization = `Bearer ${token}`

    // Loading state quản lý ở đây hoặc trong store
    // loadingStore.increment()

    return config
  },
  (error) => Promise.reject(error)
)

// ─── Response Interceptor ───────────────────────────────
api.interceptors.response.use(
  (response) => {
    // loadingStore.decrement()
    return response
  },
  async (error) => {
    // loadingStore.decrement()

    const original = error.config
    const status   = error.response?.status

    // ── 401: Token expired → refresh ──
    if (status === 401 && !original._retry) {
      original._retry = true

      if (isRefreshing) {
        // Có request khác đang refresh → queue lại, chờ token mới
        return new Promise((resolve, reject) => {
          pendingRequests.push({ resolve, reject })
        }).then((token) => {
          original.headers.Authorization = `Bearer ${token}`
          return api(original)   // Retry với token mới
        })
      }

      isRefreshing = true

      try {
        const refreshToken = localStorage.getItem('refresh_token')
        const { data } = await axios.post('/api/auth/refresh', { refresh_token: refreshToken })

        const newToken = data.access_token
        localStorage.setItem('access_token', newToken)

        // Gắn token mới vào request gốc
        original.headers.Authorization = `Bearer ${newToken}`

        // Resolve tất cả pending requests
        resolvePending(newToken)

        return api(original)   // Retry request gốc
      } catch (refreshError) {
        rejectPending(refreshError)

        // Refresh thất bại → logout
        localStorage.clear()
        window.location.href = '/login'

        return Promise.reject(refreshError)
      } finally {
        isRefreshing = false
      }
    }

    // ── 422: Validation errors ──
    if (status === 422) {
      const errors = error.response?.data?.errors
      // toast.error('Dữ liệu không hợp lệ')
      return Promise.reject({ ...error, validationErrors: errors })
    }

    // ── 403: Forbidden ──
    if (status === 403) {
      // toast.error('Bạn không có quyền thực hiện hành động này')
    }

    // ── 500: Server error ──
    if (status >= 500) {
      // toast.error('Lỗi server, vui lòng thử lại sau')
    }

    // ── Network error ──
    if (!error.response) {
      // toast.error('Mất kết nối mạng')
    }

    return Promise.reject(error)
  }
)

// Typed API methods
export const productApi = {
  list:   (params) => api.get('/products', { params }),
  show:   (id)     => api.get(`/products/${id}`),
  create: (data)   => api.post('/products', data),
  update: (id, data) => api.put(`/products/${id}`, data),
  delete: (id)     => api.delete(`/products/${id}`),
}

export const authApi = {
  login:   (credentials) => api.post('/auth/login', credentials),
  logout:  ()            => api.post('/auth/logout'),
  me:      ()            => api.get('/auth/me'),
  refresh: (token)       => api.post('/auth/refresh', { refresh_token: token }),
}

export default api
```

```vue
<!-- Sử dụng trong component -->
<script setup>
import { productApi } from '@/lib/api'

const products = ref([])
const loading  = ref(false)
const error    = ref(null)

async function loadProducts() {
  loading.value = true
  try {
    const { data } = await productApi.list({ page: 1, limit: 10 })
    products.value = data.data
  } catch (e) {
    if (e.validationErrors) {
      // Validation errors
      console.log(e.validationErrors)
    } else {
      error.value = e.message
    }
  } finally {
    loading.value = false
  }
}

onMounted(loadProducts)
</script>
```

### 🔍 Giải Thích Sâu

**Concurrent request queue – vấn đề gì nếu không có?**
```javascript
// Scenario: 3 requests cùng lúc, token expired
// Request A → 401 → bắt đầu refresh
// Request B → 401 → cũng bắt đầu refresh (ĐỒNG THỜI!)
// Request C → 401 → cũng bắt đầu refresh (ĐỒNG THỜI!)
// → 3 refresh requests cùng lúc → race condition
// → Server có thể invalidate 2 token còn lại → logout oan

// ✅ Với queue:
// A → 401 → isRefreshing = true → start refresh
// B → 401 → isRefreshing = true → push vào pendingRequests (chờ)
// C → 401 → isRefreshing = true → push vào pendingRequests (chờ)
// Refresh xong → resolvePending(newToken) → B và C retry với token mới
```

---

## 💡 DEEP DIVE: Tại Sao Vue 3 Dùng Proxy Thay Vì Object.defineProperty?

### Vue 2 – `Object.defineProperty`

```javascript
// Vue 2 implement reactivity
function defineReactive(obj, key, val) {
  Object.defineProperty(obj, key, {
    get() {
      track(key)   // Đăng ký dependency
      return val
    },
    set(newVal) {
      val = newVal
      trigger(key) // Notify watchers
    }
  })
}

// ❌ Vấn đề 1: Dynamic properties không reactive
const state = { name: 'Tín' }
observe(state)
state.age = 25        // ❌ age không reactive → phải dùng Vue.set(state, 'age', 25)

// ❌ Vấn đề 2: Array methods không reactive
state.list.push(1)    // ❌ Không trigger update → phải patch Array prototype

// ❌ Vấn đề 3: Performance – cần traverse toàn bộ object khi init
```

### Vue 3 – `Proxy`

```javascript
// Vue 3 – Proxy bắt TẤT CẢ operations
function reactive(obj) {
  return new Proxy(obj, {
    get(target, key, receiver) {
      track(target, key)
      const val = Reflect.get(target, key, receiver)
      // Lazy deep reactive
      return typeof val === 'object' ? reactive(val) : val
    },
    set(target, key, value, receiver) {
      const result = Reflect.set(target, key, value, receiver)
      trigger(target, key)  // Trigger kể cả key mới!
      return result
    },
    deleteProperty(target, key) {
      const result = Reflect.deleteProperty(target, key)
      trigger(target, key)   // Track deletion!
      return result
    }
  })
}

// ✅ Dynamic properties tự động reactive
const state = reactive({ name: 'Tín' })
state.age = 25      // ✅ Reactive tự động!
state.list.push(1)  // ✅ Array methods work!
delete state.name   // ✅ Deletion reactive!
```

---

## 💡 DEEP DIVE: Laravel Service Container – Tại Sao Cần?

```php
// ❌ Without DI – tightly coupled, khó test
class OrderController extends Controller
{
    public function store(Request $request)
    {
        $stripe  = new StripeGateway(env('STRIPE_KEY'));   // Hardcoded
        $mailer  = new Mailer(config('mail.driver'));      // Hardcoded
        $logger  = new FileLogger('/var/log/orders.log'); // Hardcoded

        $order = Order::create($request->validated());
        $stripe->charge($order);
        $mailer->send(new InvoiceEmail($order));
    }
    // → Unit test: không thể mock StripeGateway mà không thật sự charge card!
}

// ✅ With DI – loosely coupled, testable
class OrderController extends Controller
{
    public function __construct(
        private PaymentGatewayInterface $payment,  // Interface, không phải class cụ thể
        private MailerInterface $mailer,
        private LoggerInterface $logger,
    ) {}

    public function store(StoreOrderRequest $request)
    {
        $order = Order::create($request->validated());
        $this->payment->charge($order);   // Không biết là Stripe hay PayPal
        $this->mailer->send(new InvoiceEmail($order));
    }
}

// AppServiceProvider: bind interface → implementation
$this->app->bind(PaymentGatewayInterface::class, function ($app) {
    return app()->environment('testing')
        ? new FakePaymentGateway()    // Trong test → dùng fake
        : new StripeGateway(config('services.stripe.key'));  // Production
});

// Unit test – swap implementation dễ dàng
public function test_order_is_created(): void
{
    $this->app->bind(PaymentGatewayInterface::class, FakePaymentGateway::class);

    $this->postJson('/api/orders', $orderData)->assertCreated();
    // → FakeGateway không charge card thật
}
```

---

## 🎯 SELF-TEST: Câu Hỏi Kiểm Tra

Sau khi làm xong các bài tập, hãy tự kiểm tra:

### Vue.js
1. Viết `usePagination` composable từ đầu (không xem code)
2. Giải thích tại sao cần `toRefs` khi destructure `reactive`
3. `v-model` thực chất là shorthand của gì? (hai-chiều)
4. Khi nào dùng `shallowRef` thay vì `ref`?

### Pinia
1. Sự khác biệt giữa `storeToRefs` và `toRefs`?
2. Tại sao action có thể gọi action khác bằng `this`?
3. Composition store syntax khác option store ở điểm nào?

### Laravel
1. Viết query lấy top 5 users có nhiều orders nhất với Eloquent
2. Giải thích `$fillable` vs `$guarded` – khi nào dùng cái nào?
3. Trong migration, `cascadeOnDelete` vs `nullOnDelete` – khác gì?
4. Tại sao Job cần implement `ShouldQueue` và dùng `SerializesModels`?

### API
1. Nếu access token là stateless, làm sao revoke (đăng xuất từ thiết bị khác)?
2. Sự khác biệt giữa 401 và 403?
3. Tại sao không nên dùng GET để xóa dữ liệu (dù về kỹ thuật có thể làm được)?

---

> 📌 **File học lý thuyết:** [ON_LUYEN_PHONG_VAN.md](./ON_LUYEN_PHONG_VAN.md)  
> 🔗 Sau khi làm xong tất cả, hãy build **Todo App fullstack** để thực hành!

---

## VUE-07: KeepAlive + Suspense + defineAsyncComponent

### 🎯 Yêu cầu
Xây dựng tab layout:
- 3 tabs: Dashboard, Users, Reports
- Mỗi tab là async component (lazy load)
- KeepAlive cho Dashboard và Users (giữ state khi chuyển tab)
- Fallback skeleton khi component chưa load xong
- Reports: không cache (data phải fresh mỗi lần vào)

### ✅ Đáp Án

```vue
<!-- AppTabs.vue -->
<script setup>
import { ref, shallowRef, defineAsyncComponent } from 'vue'

// ── defineAsyncComponent với loading/error handling ──
const DashboardTab = defineAsyncComponent({
  loader: () => import('./tabs/DashboardTab.vue'),
  loadingComponent: SkeletonTab,   // Hiển thị khi đang load
  errorComponent:  ErrorTab,       // Hiển thị khi lỗi
  delay: 200,                      // Chờ 200ms trước khi show loading (tránh flash)
  timeout: 10000,                  // Timeout sau 10s → show error
})

const UsersTab   = defineAsyncComponent(() => import('./tabs/UsersTab.vue'))
const ReportsTab = defineAsyncComponent(() => import('./tabs/ReportsTab.vue'))

// shallowRef: chỉ track reference change, không deep watch component internals
const activeTab = shallowRef(DashboardTab)
const activeKey = ref('dashboard')

const tabs = [
  { key: 'dashboard', label: 'Dashboard',  component: DashboardTab, keepAlive: true  },
  { key: 'users',     label: 'Users',      component: UsersTab,     keepAlive: true  },
  { key: 'reports',   label: 'Reports',    component: ReportsTab,   keepAlive: false },
]

function switchTab(tab) {
  activeTab.value = tab.component
  activeKey.value = tab.key
}
</script>

<template>
  <!-- Tab navigation -->
  <nav class="tabs">
    <button
      v-for="tab in tabs"
      :key="tab.key"
      :class="{ active: activeKey === tab.key }"
      @click="switchTab(tab)"
    >
      {{ tab.label }}
    </button>
  </nav>

  <!-- Suspense: hiện fallback khi async component loading -->
  <Suspense>
    <template #default>
      <!-- KeepAlive với include/exclude -->
      <KeepAlive :max="3" :include="['DashboardTab', 'UsersTab']">
        <!-- include: danh sách component name được cache -->
        <!-- max: tối đa 3 instances trong cache (LRU) -->
        <component :is="activeTab" :key="activeKey" />
        <!-- :key khác nhau cho tab không cache → force re-create -->
      </KeepAlive>
    </template>

    <template #fallback>
      <div class="skeleton-tabs">
        <div class="skeleton" style="height: 300px" />
      </div>
    </template>
  </Suspense>
</template>
```

```vue
<!-- tabs/DashboardTab.vue – sử dụng lifecycle của KeepAlive -->
<script setup>
import { ref, onMounted, onActivated, onDeactivated } from 'vue'

const chartData = ref(null)
let pollingInterval = null

// onMounted: chỉ chạy lần đầu tiên
onMounted(async () => {
  chartData.value = await fetchChartData()
})

// onActivated: chạy mỗi khi tab được activate (kể cả lần đầu)
onActivated(() => {
  console.log('Dashboard activated')
  // Bắt đầu polling mỗi 30s khi tab active
  pollingInterval = setInterval(refreshData, 30000)
})

// onDeactivated: khi tab bị ẩn (không destroy, chỉ deactivate)
onDeactivated(() => {
  console.log('Dashboard deactivated')
  // Dừng polling khi tab không active → tiết kiệm resource
  clearInterval(pollingInterval)
})

async function refreshData() {
  chartData.value = await fetchChartData()
}
</script>
```

### 🔍 Giải Thích Sâu

**KeepAlive `include` – tại sao cần đặt tên component?**
```vue
<!-- KeepAlive match theo component OPTIONS name, không phải file name -->
<!-- DashboardTab.vue phải có: -->
<script>
export default { name: 'DashboardTab' }  // Vue 2 style
</script>

<!-- Hoặc với <script setup>: -->
<script>
export default { name: 'DashboardTab' }  // Khai báo riêng
</script>
<script setup>
// Composition API code
</script>
```

**Suspense + async setup:**
```javascript
// Suspense bắt async operations trong setup()
// Component sẽ "suspend" cho đến khi tất cả await resolve

// ✅ Suspense-aware component
<script setup>
const data = await useFetch('/api/data')  // await trong setup → Suspense aware
</script>

// ❌ Không Suspense-aware (await bên trong function, không phải top-level)
<script setup>
const data = ref(null)
onMounted(async () => data.value = await fetch(...))
</script>
```

---

## VUE-08: Vue Router – Navigation Guards

### 🎯 Yêu cầu
Cài đặt routing bảo mật:
- Route `/dashboard/*` → cần đăng nhập
- Route `/admin/*` → cần role `admin`
- Redirect về `/login?redirect=/intended-url` khi chưa login
- Sau login → redirect về intended URL
- Scroll to top khi navigate

### ✅ Đáp Án

```javascript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/useAuthStore'

const routes = [
  { path: '/',          component: () => import('@/pages/HomePage.vue') },
  { path: '/login',     component: () => import('@/pages/LoginPage.vue'), meta: { guest: true } },

  // Protected routes – cần auth
  {
    path: '/dashboard',
    component: () => import('@/layouts/DashboardLayout.vue'),
    meta: { requiresAuth: true },
    children: [
      { path: '',         component: () => import('@/pages/dashboard/IndexPage.vue') },
      { path: 'profile',  component: () => import('@/pages/dashboard/ProfilePage.vue') },
      { path: 'orders',   component: () => import('@/pages/dashboard/OrdersPage.vue') },
    ]
  },

  // Admin routes – cần role admin
  {
    path: '/admin',
    component: () => import('@/layouts/AdminLayout.vue'),
    meta: { requiresAuth: true, requiresAdmin: true },
    children: [
      { path: 'users',    component: () => import('@/pages/admin/UsersPage.vue') },
      { path: 'products', component: () => import('@/pages/admin/ProductsPage.vue') },
    ]
  },

  { path: '/:pathMatch(.*)*', component: () => import('@/pages/NotFoundPage.vue') }
]

const router = createRouter({
  history: createWebHistory(),
  routes,

  // Scroll behavior
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition          // Browser back/forward → restore vị trí
    if (to.hash)       return { el: to.hash, behavior: 'smooth' }  // Hash link → scroll đến element
    return { top: 0, behavior: 'smooth' }           // Mặc định: về đầu trang
  }
})

// ── Global Navigation Guard ────────────────────────────
router.beforeEach(async (to, from) => {
  const auth = useAuthStore()

  // ── Ensure user là loaded (page refresh) ──
  if (!auth.user && auth.token) {
    await auth.fetchCurrentUser()
  }

  // ── Redirect về intended URL sau khi login ──
  if (to.meta.guest && auth.isLoggedIn) {
    return { path: from.query?.redirect as string || '/dashboard' }
  }

  // ── Yêu cầu đăng nhập ──
  if (to.meta.requiresAuth && !auth.isLoggedIn) {
    return {
      path: '/login',
      query: { redirect: to.fullPath }  // Lưu intended URL
    }
  }

  // ── Yêu cầu role admin ──
  if (to.meta.requiresAdmin && !auth.isAdmin) {
    return { path: '/dashboard', query: { error: 'forbidden' } }
  }

  // allow navigation
})

// ── Per-route guard ────────────────────────────────────
// Dùng trong component với definePageMeta (Nuxt) hoặc beforeRouteEnter:
// {
//   path: '/checkout',
//   component: CheckoutPage,
//   beforeEnter: (to, from) => {
//     const cart = useCartStore()
//     if (cart.isEmpty) return { path: '/cart', query: { warning: 'empty' } }
//   }
// }

export default router
```

```vue
<!-- LoginPage.vue – redirect về intended URL -->
<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/useAuthStore'

const route  = useRoute()
const router = useRouter()
const auth   = useAuthStore()

async function login(credentials) {
  const result = await auth.login(credentials)
  if (result.success) {
    // Redirect về intended URL hoặc dashboard
    const redirect = route.query.redirect || '/dashboard'
    router.replace(redirect)
  }
}
</script>
```

---

## VUE-09: Performance – Virtual List

### 🎯 Yêu cầu
Giải thích và implement Virtual Scrolling cho list 10,000 items.
Tại sao cần? Khi nào dùng?

### ✅ Đáp Án + Giải Thích

**Vấn đề với list lớn:**
```vue
<!-- ❌ Render 10,000 <div> vào DOM → browser lag, memory cao -->
<div v-for="item in tenThousandItems" :key="item.id">
  {{ item.name }}
</div>
```

**Virtual Scrolling – concept:**
```
Container: height = 600px (visible area)
Item height: 50px → visible = 12 items
Total: 10,000 items

→ Chỉ render ~15 items trong DOM (12 visible + buffer)
→ Khi scroll → tính startIndex/endIndex mới → render items khác
→ DOM luôn chỉ có ~15 nodes
```

```vue
<!-- VirtualList.vue – implementation đơn giản -->
<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  items:      { type: Array,  required: true },
  itemHeight: { type: Number, default: 50    },
  buffer:     { type: Number, default: 5     },  // Extra items ngoài viewport
})

const containerRef = ref(null)
const scrollTop    = ref(0)
const containerHeight = ref(600)

// Số items visible trong viewport
const visibleCount = computed(() =>
  Math.ceil(containerHeight.value / props.itemHeight) + props.buffer * 2
)

// Index bắt đầu render
const startIndex = computed(() =>
  Math.max(0, Math.floor(scrollTop.value / props.itemHeight) - props.buffer)
)

// Index kết thúc render
const endIndex = computed(() =>
  Math.min(props.items.length, startIndex.value + visibleCount.value)
)

// Items được render (chỉ ~15 items)
const visibleItems = computed(() =>
  props.items.slice(startIndex.value, endIndex.value).map((item, i) => ({
    ...item,
    _index: startIndex.value + i,
    // vị trí tuyệt đối trong list
    _top: (startIndex.value + i) * props.itemHeight,
  }))
)

// Tổng chiều cao nội dung (để thanh scroll đúng)
const totalHeight = computed(() => props.items.length * props.itemHeight)

// Khoảng cách từ đầu đến items đang render (offset)
const offsetY = computed(() => startIndex.value * props.itemHeight)

function onScroll(e) {
  scrollTop.value = e.target.scrollTop
}
</script>

<template>
  <!-- Container: overflow scroll, chiều cao cố định -->
  <div
    ref="containerRef"
    class="virtual-container"
    :style="{ height: containerHeight + 'px', overflowY: 'auto', position: 'relative' }"
    @scroll="onScroll"
  >
    <!-- Inner: chiều cao thật của toàn bộ list (để scrollbar đúng) -->
    <div :style="{ height: totalHeight + 'px', position: 'relative' }">
      <!-- Wrap items được render, dịch chuyển theo offset -->
      <div :style="{ transform: `translateY(${offsetY}px)` }">
        <div
          v-for="item in visibleItems"
          :key="item.id"
          :style="{ height: props.itemHeight + 'px' }"
          class="virtual-item"
        >
          <slot :item="item" :index="item._index" />
        </div>
      </div>
    </div>
  </div>
</template>
```

```vue
<!-- Sử dụng VirtualList -->
<script setup>
const bigList = Array.from({ length: 10000 }, (_, i) => ({
  id: i + 1,
  name: `Item #${i + 1}`,
  price: Math.floor(Math.random() * 1000000),
}))
</script>

<template>
  <VirtualList :items="bigList" :item-height="60">
    <template #default="{ item, index }">
      <div class="product-row">
        <span>#{{ index + 1 }}</span>
        <span>{{ item.name }}</span>
        <span>{{ item.price.toLocaleString('vi-VN') }}đ</span>
      </div>
    </template>
  </VirtualList>
</template>
```

> **📦 Production:** Dùng thư viện như `vue-virtual-scroller` hoặc `@tanstack/vue-virtual` thay vì tự implement.

---

## LARAVEL-04: Testing – Feature & Unit Tests

### 🎯 Yêu cầu
Viết test cho Product CRUD API:
- Guest không thể tạo/sửa/xóa
- User thường không thể sửa product của người khác
- Admin có thể làm mọi thứ
- Validation hoạt động đúng
- Pagination trả về đúng structure

### ✅ Đáp Án

```php
// tests/Feature/ProductApiTest.php
namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;
use App\Models\{User, Product, Category};

class ProductApiTest extends TestCase
{
    use RefreshDatabase;

    // ── Helper ───────────────────────────────────────────
    private function makeUser(string $role = 'user'): User
    {
        return User::factory()->create(['role' => $role]);
    }

    private function makeProduct(?User $owner = null): Product
    {
        return Product::factory()->create([
            'user_id'     => $owner?->id ?? $this->makeUser()->id,
            'category_id' => Category::factory()->create()->id,
        ]);
    }

    // ── Index ─────────────────────────────────────────────
    public function test_anyone_can_list_products(): void
    {
        Product::factory(20)->create(['category_id' => Category::factory()->create()->id]);

        $response = $this->getJson('/api/products?per_page=10');

        $response->assertOk()
                 ->assertJsonStructure([
                     'data' => [['id', 'name', 'price', 'category']],
                     'links',
                     'meta' => ['total', 'per_page', 'current_page', 'last_page'],
                 ])
                 ->assertJsonCount(10, 'data')
                 ->assertJsonPath('meta.total', 20);
    }

    public function test_products_can_be_filtered_by_search(): void
    {
        Product::factory()->create(['name' => 'Giày Nike', 'category_id' => Category::factory()->create()->id]);
        Product::factory()->create(['name' => 'Áo thun',   'category_id' => Category::factory()->create()->id]);

        $this->getJson('/api/products?search=Nike')
             ->assertOk()
             ->assertJsonCount(1, 'data')
             ->assertJsonPath('data.0.name', 'Giày Nike');
    }

    // ── Store ─────────────────────────────────────────────
    public function test_guest_cannot_create_product(): void
    {
        $this->postJson('/api/products', ['name' => 'Test'])->assertUnauthorized();
    }

    public function test_user_can_create_product_with_valid_data(): void
    {
        $user     = $this->makeUser('seller');
        $category = Category::factory()->create();
        $payload  = [
            'name'        => 'Giày Nike Air Max',
            'price'       => 2500000,
            'stock'       => 10,
            'category_id' => $category->id,
        ];

        $response = $this->actingAs($user)->postJson('/api/products', $payload);

        $response->assertCreated()                           // status 201
                 ->assertJsonPath('data.name', 'Giày Nike Air Max')
                 ->assertJsonPath('data.price', 2500000);

        $this->assertDatabaseHas('products', [
            'name'    => 'Giày Nike Air Max',
            'user_id' => $user->id,
        ]);
    }

    public function test_validation_fails_for_invalid_product(): void
    {
        $user = $this->makeUser('seller');

        $this->actingAs($user)
             ->postJson('/api/products', [
                 'name'  => '',      // required
                 'price' => -100,    // min:0
             ])
             ->assertUnprocessable()  // 422
             ->assertJsonValidationErrors(['name', 'price', 'category_id'])
             ->assertJsonStructure(['errors' => ['name', 'price', 'category_id']]);
    }

    // ── Update ────────────────────────────────────────────
    public function test_owner_can_update_their_product(): void
    {
        $user    = $this->makeUser('seller');
        $product = $this->makeProduct($user);

        $this->actingAs($user)
             ->putJson("/api/products/{$product->id}", ['name' => 'Updated Name'])
             ->assertOk()
             ->assertJsonPath('data.name', 'Updated Name');

        $this->assertDatabaseHas('products', ['id' => $product->id, 'name' => 'Updated Name']);
    }

    public function test_user_cannot_update_others_product(): void
    {
        $owner  = $this->makeUser('seller');
        $other  = $this->makeUser('seller');
        $product = $this->makeProduct($owner);

        $this->actingAs($other)
             ->putJson("/api/products/{$product->id}", ['name' => 'Hack'])
             ->assertForbidden();   // 403
    }

    public function test_admin_can_update_any_product(): void
    {
        $admin   = $this->makeUser('admin');
        $product = $this->makeProduct();  // owned by another user

        $this->actingAs($admin)
             ->putJson("/api/products/{$product->id}", ['name' => 'Admin Override'])
             ->assertOk()
             ->assertJsonPath('data.name', 'Admin Override');
    }

    // ── Destroy ───────────────────────────────────────────
    public function test_owner_can_soft_delete_product(): void
    {
        $user    = $this->makeUser('seller');
        $product = $this->makeProduct($user);

        $this->actingAs($user)
             ->deleteJson("/api/products/{$product->id}")
             ->assertOk()
             ->assertJsonPath('message', 'Xóa thành công');

        $this->assertSoftDeleted('products', ['id' => $product->id]);
        // assertSoftDeleted: kiểm tra deleted_at không null
    }
}
```

```php
// tests/Unit/ProductTest.php – Unit test cho Model
namespace Tests\Unit;

use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;
use App\Models\{Product, Category};

class ProductTest extends TestCase
{
    use RefreshDatabase;

    public function test_active_scope_filters_correctly(): void
    {
        Category::factory()->create(['id' => 1]);
        Product::factory()->create(['is_active' => true,  'category_id' => 1]);
        Product::factory()->create(['is_active' => false, 'category_id' => 1]);
        Product::factory()->create(['is_active' => true,  'category_id' => 1]);

        $activeProducts = Product::active()->get();
        $this->assertCount(2, $activeProducts);
        $this->assertTrue($activeProducts->every(fn($p) => $p->is_active));
    }

    public function test_price_accessor_converts_cents_to_vnd(): void
    {
        // Giả sử price lưu cents trong DB
        $product = Product::factory()->make(['price' => 250000_00]);  // 2.5M VND = 250000 cents
        $this->assertEquals(2500000, $product->price);
    }
}
```

### 🔍 Giải Thích Sâu

**`RefreshDatabase` vs `DatabaseTransactions`:**
```php
// RefreshDatabase: migrate ulại toàn bộ DB
// → Chậm hơn nhưng state sạch hoàn toàn
// → Dùng khi test tạo/xóa nhiều dữ liệu

// DatabaseTransactions: wrap mỗi test trong transaction rồi rollback
// → Nhanh hơn (không migrate lại)
// → Không hoạt động với jobs chạy trong process khác
use RefreshDatabase;   // Phổ biến hơn cho feature tests
```

**Factory stategy:**
```php
// Product::factory() → tạo state mặc định
// Product::factory()->for(User::factory()) → nested factory
// Product::factory(5)->create() → tạo 5 records
// Product::factory()->make() → tạo object nhưng không lưu DB

// Custom states
Product::factory()->inactive()->create()  // Nếu defineState
Product::factory()->withImages(3)->create()
```

---

## LARAVEL-05: Migration Best Practices

### 🎯 Yêu cầu
Thiết kế schema cho hệ thống e-commerce mini:
- Users, Products, Categories, Orders, OrderItems, Tags
- Đúng foreign keys, indexes, constraints
- SoftDeletes đúng chỗ

### ✅ Đáp Án

```php
// 1. categories (không phụ thuộc gì)
Schema::create('categories', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->string('slug')->unique();
    $table->unsignedBigInteger('parent_id')->nullable();  // Self-referential
    $table->foreign('parent_id')->references('id')->on('categories')->nullOnDelete();
    $table->timestamps();
});

// 2. users (không phụ thuộc gì)
Schema::create('users', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->string('email')->unique();
    $table->string('password');
    $table->enum('role', ['user', 'seller', 'admin'])->default('user');
    $table->timestamp('email_verified_at')->nullable();
    $table->rememberToken();
    $table->timestamps();
});

// 3. products (phụ thuộc users, categories)
Schema::create('products', function (Blueprint $table) {
    $table->id();
    $table->foreignId('user_id')->constrained()->cascadeOnDelete();
    $table->foreignId('category_id')->constrained()->restrictOnDelete(); // Không xuất cascade
    $table->string('name');
    $table->string('slug')->unique();
    $table->text('description')->nullable();
    $table->unsignedBigInteger('price');      // Lưu cents/đồng nhỏ → tránh float
    $table->unsignedInteger('stock')->default(0);
    $table->boolean('is_active')->default(true);
    $table->softDeletes();                    // deleted_at

    // Indexes quan trọng
    $table->index(['is_active', 'created_at']);  // Query: active products sorted by date
    $table->index(['category_id', 'is_active']); // Query: products by category
    $table->index('price');                       // Query: filter by price range
});

// 4. tags
Schema::create('tags', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->string('slug')->unique();
    $table->timestamps();
});

// 5. product_tag (pivot)
Schema::create('product_tag', function (Blueprint $table) {
    $table->foreignId('product_id')->constrained()->cascadeOnDelete();
    $table->foreignId('tag_id')->constrained()->cascadeOnDelete();
    $table->primary(['product_id', 'tag_id']);   // Composite PK (tránh duplicate)
});

// 6. orders
Schema::create('orders', function (Blueprint $table) {
    $table->id();
    $table->foreignId('user_id')->constrained()->restrictOnDelete(); // Không xóa user còn order
    $table->string('order_number')->unique();  // INV-2024-001234
    $table->enum('status', ['pending', 'paid', 'processing', 'shipped', 'delivered', 'cancelled', 'refunded'])
          ->default('pending');
    $table->unsignedBigInteger('subtotal');
    $table->unsignedBigInteger('shipping_fee')->default(0);
    $table->unsignedBigInteger('discount')->default(0);
    $table->unsignedBigInteger('total');
    $table->json('shipping_address');    // Lưu snapshot địa chỉ tại thời điểm đặt
    $table->string('payment_method')->nullable();
    $table->timestamp('paid_at')->nullable();
    $table->timestamps();
    $table->softDeletes();

    $table->index(['user_id', 'status']);
    $table->index('status');
});

// 7. order_items
Schema::create('order_items', function (Blueprint $table) {
    $table->id();
    $table->foreignId('order_id')->constrained()->cascadeOnDelete();
    $table->foreignId('product_id')->constrained()->restrictOnDelete();
    $table->string('product_name');       // Snapshot tên sản phẩm tại thời điểm mua
    $table->unsignedBigInteger('price');  // Snapshot giá
    $table->unsignedInteger('qty');
    $table->unsignedBigInteger('subtotal');   // price * qty
    $table->timestamps();
});
```

### 🔍 Giải Thích Sâu

**`cascadeOnDelete` vs `restrictOnDelete` vs `nullOnDelete` – chọn gì?**

| Quan hệ | Hành động | Giải thích |
|---|---|---|
| `product_tag` → `products` | `cascade` | Xóa product → xóa pivot luôn (dữ liệu không có ý nghĩa độc lập) |
| `orders` → `users` | `restrict` | Không cho xóa user còn order (bảo toàn lịch sử tài chính) |
| `categories` → `categories` | `nullOnDelete` | Xóa category cha → con thành root (không mất data) |
| `products` → `categories` | `restrict` | Không cho xóa category còn sản phẩm |

**Tại sao lưu snapshot trong order_items?**
```
Kịch bản không có snapshot:
- User mua sản phẩm "Giày Nike" giá 2.5M
- Shop sau đó đổi giá → 3M, đổi tên → "Nike Air Max"
- Order cũ bị thay đổi theo → sai!

→ Luôn lưu price, name tại thời điểm mua vào order_items
→ Sản phẩm gốc có thể thay đổi tùy ý
```

**Index strategy:**
```sql
-- Tạo index cho columns thường dùng trong WHERE, ORDER BY, JOIN
-- ❌ Không index: SELECT * FROM products WHERE price > 100000  → full table scan
-- ✅ Index 'price' → index scan

-- Composite index: thứ tự columns quan trọng
-- INDEX (is_active, created_at)
-- ✅ WHERE is_active = 1 ORDER BY created_at  → use index
-- ❌ WHERE created_at > '2024-01-01'          → không use index (phải có is_active trước)
```

---

## 💡 DEEP DIVE: Pinia vs Vuex – Tại Sao Migrate?

```javascript
// ── VUEX (Vue 2 style) ────────────────────────────────
const store = createStore({
  modules: {
    cart: {
      namespaced: true,
      state: () => ({ items: [] }),
      mutations: {
        ADD_ITEM(state, item) { state.items.push(item) }  // Mutations bắt buộc sync
      },
      actions: {
        addItem({ commit }, item) {
          // actions gọi mutations
          commit('ADD_ITEM', item)
        },
        async fetchCart({ commit }) {
          const items = await api.getCart()
          commit('SET_ITEMS', items)
        }
      },
      getters: {
        totalItems: (state) => state.items.reduce((s, i) => s + i.qty, 0)
      }
    }
  }
})

// Dùng trong component
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState('cart', ['items']),
    ...mapGetters('cart', ['totalItems'])
  },
  methods: {
    ...mapActions('cart', ['addItem']),
    add(item) { this.addItem(item) }  // Gọi qua string name
  }
}
// → Boilerplate nhiều, TypeScript phức tạp, dễ nhầm string

// ── PINIA (Vue 3) ─────────────────────────────────────
const useCartStore = defineStore('cart', {
  state: () => ({ items: [] }),
  getters: {
    totalItems: (state) => state.items.reduce((s, i) => s + i.qty, 0)
  },
  actions: {
    // Actions có thể async trực tiếp, không cần mutations!
    addItem(item) { this.items.push(item) },
    async fetchCart() {
      this.items = await api.getCart()  // Mutate state trực tiếp trong action
    }
  }
})

// Dùng trong component
const cartStore = useCartStore()
const { items } = storeToRefs(cartStore)   // Reactive destructure
cartStore.addItem(newItem)                  // TypeScript biết type!
```

**Ưu điểm Pinia:**
1. **Không cần mutations** – actions có thể mutate state trực tiếp → ít boilerplate
2. **TypeScript first** – kiểu type tự động suy luận, không cần `as string`
3. **Devtools tốt hơn** – timeline, time-travel debugging
4. **Modular tự nhiên** – mỗi store là 1 file, không cần namespacing phức tạp
5. **Nhẹ hơn** – ~1KB gzipped (Vuex ~4KB)

---

## 💡 DEEP DIVE: SSR Hydration – Cơ Chế Hoạt Động

```
Server (Node.js)
  ↓ Chạy Vue app với data
  ↓ Render ra HTML string
  ↓ Inject __NUXT_DATA__ vào <head>

Client (Browser)
  ↓ Nhận HTML → hiển thị ngay (FCP nhanh)
  ↓ Download JS bundle
  ↓ Vue "hydrate" – gắn reactivity vào HTML sẵn có
  ↓ App trở thành SPA bình thường
```

```vue
<!-- Hydration Mismatch – ví dụ thực tế -->
<script setup>
// ❌ Bài toán: Date khác nhau giữa server và client
const now = new Date().toLocaleTimeString()
// Server render: "08:30:00" (giờ server)
// Client hydrate: "15:30:00" (giờ local)
// → Mismatch warning → client re-render
</script>

<!-- ✅ Fix 1: ClientOnly component -->
<template>
  <ClientOnly>
    <p>{{ new Date().toLocaleTimeString() }}</p>
    <template #fallback>
      <p>Loading...</p>  <!-- Server render cái này -->
    </template>
  </ClientOnly>
</template>

<!-- ✅ Fix 2: useState trong Nuxt (shared server↔client) -->
<script setup>
const timestamp = useState('timestamp', () => Date.now())  // Init 1 lần trên server, hydrate đúng
</script>
```

```javascript
// ✅ Fix 3: Conditional check
const isClient = process.client  // false trên server

const now = isClient ? new Date().toLocaleTimeString() : null
// Server: null → không render
// Client: giờ thật → render
```

---

## 🚀 MINI PROJECT: Todo App Fullstack

### System Design

```
Frontend (Nuxt 3 + Pinia)
  ├── pages/
  │   ├── index.vue          ← redirect → /todos
  │   ├── login.vue          ← auth form
  │   └── todos/
  │       └── index.vue      ← main todo list
  ├── stores/
  │   ├── useAuthStore.js
  │   └── useTodoStore.js
  ├── composables/
  │   └── useApi.js          ← axios wrapper
  └── middleware/
      └── auth.global.js     ← protect all routes

Backend (Laravel + Sanctum)
  ├── routes/api.php
  ├── app/Http/Controllers/
  │   ├── AuthController.php
  │   └── TodoController.php
  ├── app/Models/
  │   └── Todo.php
  └── database/migrations/
      └── create_todos_table.php
```

### Backend – Laravel

```php
// Migration
Schema::create('todos', function (Blueprint $table) {
    $table->id();
    $table->foreignId('user_id')->constrained()->cascadeOnDelete();
    $table->string('title');
    $table->text('description')->nullable();
    $table->enum('priority', ['low', 'medium', 'high'])->default('medium');
    $table->boolean('completed')->default(false);
    $table->timestamp('due_date')->nullable();
    $table->timestamps();

    $table->index(['user_id', 'completed']);
});
```

```php
// Model
class Todo extends Model
{
    protected $fillable = ['title', 'description', 'priority', 'completed', 'due_date'];
    protected $casts    = ['completed' => 'boolean', 'due_date' => 'datetime'];

    public function user(): BelongsTo { return $this->belongsTo(User::class); }

    // Chỉ lấy todo của user hiện tại
    protected static function booted(): void
    {
        static::addGlobalScope('user', function ($query) {
            if (auth()->check()) $query->where('user_id', auth()->id());
        });
    }
}

// Controller
class TodoController extends Controller
{
    public function index(Request $request)
    {
        $todos = Todo::query()
            ->when($request->completed !== null, fn($q) =>
                $q->where('completed', filter_var($request->completed, FILTER_VALIDATE_BOOLEAN))
            )
            ->when($request->priority, fn($q) => $q->where('priority', $request->priority))
            ->orderByRaw('completed ASC, due_date ASC NULLS LAST, created_at DESC')
            ->paginate(20);

        return TodoResource::collection($todos);
    }

    public function store(StoreTodoRequest $request)
    {
        $todo = Todo::create([...$request->validated(), 'user_id' => auth()->id()]);
        return new TodoResource($todo);
    }

    public function update(UpdateTodoRequest $request, Todo $todo)
    {
        $todo->update($request->validated());
        return new TodoResource($todo);
    }

    public function toggleComplete(Todo $todo)
    {
        $todo->update(['completed' => !$todo->completed]);
        return new TodoResource($todo);
    }

    public function destroy(Todo $todo)
    {
        $todo->delete();
        return response()->json(['message' => 'Đã xóa'], 200);
    }
}

// Routes
Route::middleware('auth:sanctum')->group(function () {
    Route::apiResource('todos', TodoController::class);
    Route::patch('todos/{todo}/toggle', [TodoController::class, 'toggleComplete']);
});
```

### Frontend – Nuxt 3

```javascript
// stores/useTodoStore.js
export const useTodoStore = defineStore('todos', () => {
  const todos    = ref([])
  const loading  = ref(false)
  const error    = ref(null)
  const filters  = ref({ completed: null, priority: null })

  const pending  = computed(() => todos.value.filter(t => !t.completed))
  const done     = computed(() => todos.value.filter(t => t.completed))
  const stats    = computed(() => ({
    total:   todos.value.length,
    pending: pending.value.length,
    done:    done.value.length,
  }))

  async function fetchTodos() {
    loading.value = true
    try {
      const { data } = await useApi('/todos', { params: filters.value })
      todos.value = data.value?.data || []
    } finally {
      loading.value = false
    }
  }

  async function addTodo(payload) {
    const { data } = await useApi('/todos', { method: 'POST', body: payload })
    todos.value.unshift(data.value.data)
  }

  async function toggleTodo(id) {
    // Optimistic update: update UI ngay, rollback nếu fail
    const todo = todos.value.find(t => t.id === id)
    if (!todo) return

    todo.completed = !todo.completed  // Optimistic
    try {
      await useApi(`/todos/${id}/toggle`, { method: 'PATCH' })
    } catch {
      todo.completed = !todo.completed  // Rollback
    }
  }

  async function deleteTodo(id) {
    todos.value = todos.value.filter(t => t.id !== id)  // Optimistic
    try {
      await useApi(`/todos/${id}`, { method: 'DELETE' })
    } catch {
      fetchTodos()  // Rollback: re-fetch
    }
  }

  return { todos, loading, error, filters, pending, done, stats, fetchTodos, addTodo, toggleTodo, deleteTodo }
})
```

```vue
<!-- pages/todos/index.vue -->
<script setup>
definePageMeta({ middleware: 'auth' })

const store = useTodoStore()
const { todos, loading, stats, filters } = storeToRefs(store)

// Initial fetch
await store.fetchTodos()

// Re-fetch khi filter thay đổi
watch(filters, () => store.fetchTodos(), { deep: true })

const newTodo = ref({ title: '', priority: 'medium', due_date: null })

async function submit() {
  if (!newTodo.value.title.trim()) return
  await store.addTodo(newTodo.value)
  newTodo.value = { title: '', priority: 'medium', due_date: null }
}
</script>

<template>
  <div class="todo-app">
    <!-- Stats -->
    <div class="stats">
      <span>Tổng: {{ stats.total }}</span>
      <span>Chờ: {{ stats.pending }}</span>
      <span>Xong: {{ stats.done }}</span>
    </div>

    <!-- Filters -->
    <div class="filters">
      <select v-model="filters.priority">
        <option :value="null">Tất cả ưu tiên</option>
        <option value="high">Cao</option>
        <option value="medium">Trung bình</option>
        <option value="low">Thấp</option>
      </select>
      <button @click="filters.completed = null">Tất cả</button>
      <button @click="filters.completed = false">Chưa xong</button>
      <button @click="filters.completed = true">Đã xong</button>
    </div>

    <!-- Add form -->
    <form @submit.prevent="submit" class="add-form">
      <input v-model="newTodo.title" placeholder="Thêm todo mới..." required />
      <select v-model="newTodo.priority">
        <option value="low">Thấp</option>
        <option value="medium">Trung bình</option>
        <option value="high">Cao</option>
      </select>
      <input type="date" v-model="newTodo.due_date" />
      <button type="submit">Thêm</button>
    </form>

    <!-- List -->
    <div v-if="loading" class="loading">Loading...</div>
    <TransitionGroup name="list" tag="ul" class="todo-list">
      <li
        v-for="todo in todos"
        :key="todo.id"
        :class="{ completed: todo.completed, [`priority-${todo.priority}`]: true }"
      >
        <input type="checkbox" :checked="todo.completed" @change="store.toggleTodo(todo.id)" />
        <span class="title">{{ todo.title }}</span>
        <span v-if="todo.due_date" class="due">{{ new Date(todo.due_date).toLocaleDateString('vi-VN') }}</span>
        <button @click="store.deleteTodo(todo.id)">🗑</button>
      </li>
    </TransitionGroup>
  </div>
</template>

<style scoped>
.list-enter-active, .list-leave-active { transition: all 0.3s ease; }
.list-enter-from { opacity: 0; transform: translateX(-20px); }
.list-leave-to   { opacity: 0; transform: translateX(20px); }

.priority-high   { border-left: 4px solid #ef4444; }
.priority-medium { border-left: 4px solid #f59e0b; }
.priority-low    { border-left: 4px solid #10b981; }
.completed .title { text-decoration: line-through; opacity: 0.5; }
</style>
```

---

## 🎓 Tổng Kết – Mindmap Kiến Thức

```
Vue.js
├── Reactivity System
│   ├── ref / reactive / computed / watch / watchEffect
│   ├── toRefs / storeToRefs (preserve reactivity on destructure)
│   └── Proxy (Vue 3) vs defineProperty (Vue 2)
├── Component Model
│   ├── defineProps / defineEmits / defineExpose
│   ├── provide / inject (avoid prop drilling)
│   ├── v-model custom (:modelValue + @update:modelValue)
│   └── slots (default / named / scoped)
├── Composables (Reusable Logic)
│   ├── useCounter / useFetch / useDebouncedSearch
│   └── Pattern: return { state, computed, actions }
├── Performance
│   ├── KeepAlive (cache component instances)
│   ├── defineAsyncComponent (code splitting)
│   ├── v-memo / v-once (skip re-render)
│   └── Virtual Scrolling (DOM = ~15 items dù có 10k)
└── Advanced
    ├── Custom Directives (v-debounce, v-focus)
    ├── Teleport (render outside DOM tree)
    ├── Suspense (async component loading)
    └── TransitionGroup (animated lists)

Pinia
├── Option Store (state / getters / actions)
├── Composition Store (ref / computed / function)
├── storeToRefs (reactive destructure)
└── Plugin (persist, devtools)

Nuxt 3
├── Rendering Modes (SSR / SSG / ISR / CSR)
├── Data Fetching (useFetch / useAsyncData / $fetch)
├── SEO (useSeoMeta / useHead / canonical)
├── Routing (file-based / dynamic / layouts)
├── Middleware (route / global / server)
└── Server Routes (server/api/*.ts)

Laravel
├── Request Lifecycle (Kernel → Middleware → Controller)
├── Eloquent (hasMany/belongsTo/belongsToMany + N+1 fix)
├── Architecture (FormRequest / Resource / Repository / Observer)
├── Auth (Sanctum / Policy / Gate)
├── Queue (Job / Event / Listener)
├── Cache (remember / tags / flush)
└── Testing (Feature / Unit / Factory / RefreshDatabase)

API & Security
├── JWT (header.payload.signature)
├── Token Strategy (access short TTL + refresh long TTL)
├── Storage (httpOnly cookie > localStorage)
├── CSRF / CORS / Rate Limiting
├── OWASP (SQL Injection / Mass Assignment / BOLA / BFLA)
└── OAuth2 (Authorization Code + PKCE for SPA)
```

---

> ✅ **Checklist cuối cùng trước phỏng vấn:**
> - [ ] Tự implement useCounter, useFetch, useCart không xem code
> - [ ] Giải thích được N+1 và cách fix bằng ví dụ thực
> - [ ] Viết được FormRequest + Resource cho 1 endpoint
> - [ ] Giải thích JWT flow và tại sao cần refresh token
> - [ ] Deploy Todo App fullstack lên GitHub làm portfolio

---
---

# 🔥 PHẦN NÂNG CAO – Advanced Patterns & Real-World Scenarios

---

## VUE-10: Renderless Component Pattern

### 🎯 Yêu cầu
Xây dựng `<DataTable>` renderless component (headless UI):
- Quản lý sorting, pagination logic bên trong
- UI hoàn toàn do parent quyết định qua scoped slots
- Pattern này được dùng trong Headless UI, Radix Vue, VueUse

### ✅ Đáp Án

```vue
<!-- DataTable.vue – Renderless: không render bất cứ HTML nào -->
<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  data:       { type: Array,  required: true },
  pageSize:   { type: Number, default: 10    },
  searchKeys: { type: Array,  default: []    },  // columns để search
})

// ── State ───────────────────────────────────────
const page        = ref(1)
const searchQuery = ref('')
const sortKey     = ref(null)
const sortDir     = ref('asc')  // 'asc' | 'desc'

// ── Computed ────────────────────────────────────
const filtered = computed(() => {
  if (!searchQuery.value) return props.data

  const q = searchQuery.value.toLowerCase()
  return props.data.filter(row =>
    props.searchKeys.some(key =>
      String(row[key] ?? '').toLowerCase().includes(q)
    )
  )
})

const sorted = computed(() => {
  if (!sortKey.value) return filtered.value

  return [...filtered.value].sort((a, b) => {
    const aVal = a[sortKey.value]
    const bVal = b[sortKey.value]
    const factor = sortDir.value === 'asc' ? 1 : -1

    if (typeof aVal === 'number') return factor * (aVal - bVal)
    return factor * String(aVal).localeCompare(String(bVal))
  })
})

const totalPages  = computed(() => Math.ceil(sorted.value.length / props.pageSize))
const paginatedRows = computed(() => sorted.value.slice(
  (page.value - 1) * props.pageSize,
  page.value * props.pageSize
))

// ── Actions ─────────────────────────────────────
function sortBy(key) {
  if (sortKey.value === key) {
    sortDir.value = sortDir.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortDir.value = 'asc'
  }
  page.value = 1
}

function goToPage(p) {
  page.value = Math.min(Math.max(1, p), totalPages.value)
}

// ── Expose ra scoped slot ────────────────────────
</script>

<template>
  <!-- Renderless: chỉ expose slot với state + actions -->
  <slot
    :rows="paginatedRows"
    :total="sorted.length"
    :page="page"
    :totalPages="totalPages"
    :searchQuery="searchQuery"
    :sortKey="sortKey"
    :sortDir="sortDir"
    :sortBy="sortBy"
    :goToPage="goToPage"
    :onSearch="(q) => { searchQuery = q; page = 1 }"
  />
</template>
```

```vue
<!-- Sử dụng: UI hoàn toàn tùy chỉnh -->
<script setup>
const users = ref([
  { id: 1, name: 'Nguyễn Văn A', email: 'a@test.com', age: 25, role: 'admin' },
  { id: 2, name: 'Trần Thị B',   email: 'b@test.com', age: 30, role: 'user'  },
  // ...
])
</script>

<template>
  <DataTable
    :data="users"
    :pageSize="5"
    :searchKeys="['name', 'email']"
  >
    <template #default="{ rows, page, totalPages, sortKey, sortDir, sortBy, goToPage, onSearch }">
      <!-- Search -->
      <input @input="onSearch($event.target.value)" placeholder="Tìm kiếm..." />

      <!-- Table với sortable headers -->
      <table>
        <thead>
          <tr>
            <th @click="sortBy('name')" class="sortable">
              Tên
              <span v-if="sortKey === 'name'">{{ sortDir === 'asc' ? '↑' : '↓' }}</span>
            </th>
            <th @click="sortBy('age')" class="sortable">
              Tuổi
              <span v-if="sortKey === 'age'">{{ sortDir === 'asc' ? '↑' : '↓' }}</span>
            </th>
            <th>Email</th>
            <th>Role</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in rows" :key="user.id">
            <td>{{ user.name }}</td>
            <td>{{ user.age }}</td>
            <td>{{ user.email }}</td>
            <td><span :class="`badge-${user.role}`">{{ user.role }}</span></td>
          </tr>
        </tbody>
      </table>

      <!-- Pagination -->
      <div class="pagination">
        <button :disabled="page <= 1" @click="goToPage(page - 1)">←</button>
        <button
          v-for="p in totalPages"
          :key="p"
          :class="{ active: p === page }"
          @click="goToPage(p)"
        >{{ p }}</button>
        <button :disabled="page >= totalPages" @click="goToPage(page + 1)">→</button>
      </div>
    </template>
  </DataTable>
</template>
```

### 🔍 Giải Thích Sâu – Tại sao Renderless Component?

```
Vấn đề với Component thông thường:
✅ Logic đóng gói tốt
❌ UI bị cứng – không customize được style
❌ Phải truyền 20+ props để customize

Renderless Component (Headless UI pattern):
✅ Logic: nằm trong component (sorting, pagination, search)
✅ UI: do parent quyết định hoàn toàn qua scoped slots
✅ Reusable với bất kỳ design system nào
✅ Test logic độc lập với UI

→ Radix Vue, Headless UI, VueUse đều dùng pattern này
```

---

## VUE-11: useIntersectionObserver – Infinite Scroll & Lazy Image

### 🎯 Yêu cầu
Implement:
1. **Infinite scroll**: tự động load more khi scroll đến cuối list
2. **Lazy image**: chỉ load image khi vào viewport

### ✅ Đáp Án

```javascript
// composables/useIntersectionObserver.js
import { ref, onMounted, onUnmounted } from 'vue'

export function useIntersectionObserver(callback, options = {}) {
  const target = ref(null)  // Template ref

  let observer = null

  onMounted(() => {
    if (!target.value) return

    observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) callback(entry)
        })
      },
      {
        root: options.root || null,          // null = viewport
        rootMargin: options.rootMargin || '0px',
        threshold: options.threshold || 0.1  // 10% visible → trigger
      }
    )

    observer.observe(target.value)
  })

  onUnmounted(() => observer?.disconnect())

  return { target }
}
```

```vue
<!-- InfiniteScrollList.vue -->
<script setup>
import { ref } from 'vue'
import { useIntersectionObserver } from '@/composables/useIntersectionObserver'

const products = ref([])
const page     = ref(1)
const loading  = ref(false)
const hasMore  = ref(true)

async function loadMore() {
  if (loading.value || !hasMore.value) return

  loading.value = true
  try {
    const { data } = await $fetch('/api/products', { params: { page: page.value } })
    products.value.push(...data.data)
    hasMore.value = data.meta.current_page < data.meta.last_page
    page.value++
  } finally {
    loading.value = false
  }
}

// Sentinel element ở cuối list → trigger loadMore khi hiện ra
const { target: sentinel } = useIntersectionObserver(
  () => loadMore(),
  { rootMargin: '200px' }  // Trigger trước 200px khi đến cuối
)

// Load lần đầu
await loadMore()
</script>

<template>
  <div class="product-list">
    <ProductCard v-for="p in products" :key="p.id" :product="p" />

    <!-- Sentinel element: invisible, nằm cuối list -->
    <div ref="sentinel" class="sentinel">
      <div v-if="loading" class="loading-spinner">Loading...</div>
      <p v-else-if="!hasMore" class="end-message">Đã hết sản phẩm 🎉</p>
    </div>
  </div>
</template>
```

```vue
<!-- LazyImage.vue – chỉ load src khi vào viewport -->
<script setup>
import { ref, computed } from 'vue'
import { useIntersectionObserver } from '@/composables/useIntersectionObserver'

const props = defineProps({
  src:         { type: String, required: true },
  placeholder: { type: String, default: 'data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEAAAAALAAAAAABAAEAAAI=' },
  alt:         { type: String, default: '' },
})

const loaded = ref(false)
const imgSrc = computed(() => loaded.value ? props.src : props.placeholder)

const { target: imgEl } = useIntersectionObserver(
  (entry) => {
    if (entry.isIntersecting && !loaded.value) {
      loaded.value = true     // Trigger real src load
      // Sau khi loaded = true, observer không cần nữa
    }
  },
  { threshold: 0.01 }  // Bất cứ pixel nào vào viewport
)
</script>

<template>
  <img
    ref="imgEl"
    :src="imgSrc"
    :alt="alt"
    :class="{ 'img-loaded': loaded, 'img-loading': !loaded }"
    @load="loaded = true"
  />
</template>

<style scoped>
.img-loading { opacity: 0.3; filter: blur(8px); transition: opacity 0.3s, filter 0.3s; }
.img-loaded  { opacity: 1;   filter: blur(0); }
</style>
```

---

## VUE-12: Global Error Handling & Error Boundary

### 🎯 Yêu cầu
Cài đặt error handling toàn diện:
- Global error handler cho Vue
- Error boundary component (tránh crash toàn trang)
- Async error handling trong composables
- Report errors lên Sentry (giả lập)

### ✅ Đáp Án

```javascript
// plugins/errorHandler.js (Nuxt plugin hoặc main.js)
export default defineNuxtPlugin((nuxtApp) => {
  // Vue runtime errors (component errors)
  nuxtApp.vueApp.config.errorHandler = (error, instance, info) => {
    console.error('Vue Error:', error)
    console.error('Component:', instance?.$options.name || 'Unknown')
    console.error('Info:', info)

    // Report to monitoring service
    reportError({ error, context: 'vue-runtime', info })
  }

  // Unhandled Promise rejections
  if (process.client) {
    window.addEventListener('unhandledrejection', (event) => {
      console.error('Unhandled Promise:', event.reason)
      reportError({ error: event.reason, context: 'unhandled-promise' })
      event.preventDefault()  // Tránh browser default (console noise)
    })
  }

  // Nuxt app errors
  nuxtApp.hook('app:error', (error) => {
    console.error('Nuxt App Error:', error)
    reportError({ error, context: 'nuxt-app' })
  })
})

function reportError({ error, context, info }) {
  // Sentry.captureException(error, { extra: { context, info } })
  console.log('📊 Error reported:', { context, message: error.message })
}
```

```vue
<!-- ErrorBoundary.vue – ngăn component con làm crash toàn trang -->
<script setup>
import { ref, onErrorCaptured } from 'vue'

const props = defineProps({
  fallback: { type: String, default: 'Có lỗi xảy ra, vui lòng thử lại.' }
})

const emit = defineEmits(['error'])

const error  = ref(null)
const hasError = ref(false)

// onErrorCaptured: bắt errors từ tất cả component con
onErrorCaptured((err, instance, info) => {
  error.value  = err
  hasError.value = true

  emit('error', { error: err, instance, info })

  console.error('ErrorBoundary caught:', err)
  return false  // false = stop propagation lên trên
})

function reset() {
  error.value  = null
  hasError.value = false
}
</script>

<template>
  <slot v-if="!hasError" />

  <div v-else class="error-boundary">
    <div class="error-content">
      <span class="error-icon">⚠️</span>
      <p>{{ fallback }}</p>
      <details v-if="error">
        <summary>Chi tiết lỗi</summary>
        <pre>{{ error.message }}</pre>
      </details>
      <button @click="reset">Thử lại</button>
    </div>
  </div>
</template>
```

```vue
<!-- Sử dụng Error Boundary -->
<template>
  <ErrorBoundary fallback="Không thể tải danh sách sản phẩm" @error="logToSentry">
    <ProductList />  <!-- Nếu crash → hiện fallback, không crash trang -->
  </ErrorBoundary>

  <ErrorBoundary>
    <UserProfile />
  </ErrorBoundary>
</template>
```

---

## 💅 FIGMA → CODE: Quy Trình Chuẩn

### Bước 1: Phân Tích Figma Design

```
Khi mở Figma, cần xác định:
1. Design Tokens: colors, spacing, typography, breakpoints
2. Component inventory: button variants, input states, card types
3. Layout system: grid, columns, gaps
4. Responsive breakpoints: mobile (320px), tablet (768px), desktop (1280px)
5. Interactions: hover, focus, active states
6. Animation/transition specs

→ Export design tokens thành CSS variables TRƯỚC KHI code
```

### Bước 2: CSS Variables System

```css
/* tokens.css – Design tokens từ Figma */
:root {
  /* ── Colors ──────────────────────────── */
  --color-primary:     #6366f1;   /* Indigo 500 */
  --color-primary-hover: #4f46e5; /* Indigo 600 */
  --color-primary-light: #e0e7ff; /* Indigo 100 */

  --color-text-primary:   #111827;
  --color-text-secondary: #6b7280;
  --color-text-disabled:  #d1d5db;

  --color-bg:          #ffffff;
  --color-bg-subtle:   #f9fafb;
  --color-bg-dark:     #111827;

  --color-border:      #e5e7eb;
  --color-border-focus: #6366f1;

  --color-success:     #10b981;
  --color-warning:     #f59e0b;
  --color-error:       #ef4444;
  --color-info:        #3b82f6;

  /* ── Typography ──────────────────────── */
  --font-sans:    'Inter', 'Segoe UI', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Fira Code', monospace;

  --text-xs:   0.75rem;   /* 12px */
  --text-sm:   0.875rem;  /* 14px */
  --text-base: 1rem;      /* 16px */
  --text-lg:   1.125rem;  /* 18px */
  --text-xl:   1.25rem;   /* 20px */
  --text-2xl:  1.5rem;    /* 24px */
  --text-3xl:  1.875rem;  /* 30px */
  --text-4xl:  2.25rem;   /* 36px */

  --font-normal:  400;
  --font-medium:  500;
  --font-semibold: 600;
  --font-bold:    700;

  --leading-tight:  1.25;
  --leading-normal: 1.5;
  --leading-loose:  1.75;

  /* ── Spacing (8px Base Grid) ─────────── */
  --space-1:  0.25rem;   /* 4px */
  --space-2:  0.5rem;    /* 8px */
  --space-3:  0.75rem;   /* 12px */
  --space-4:  1rem;      /* 16px */
  --space-5:  1.25rem;   /* 20px */
  --space-6:  1.5rem;    /* 24px */
  --space-8:  2rem;      /* 32px */
  --space-10: 2.5rem;    /* 40px */
  --space-12: 3rem;      /* 48px */
  --space-16: 4rem;      /* 64px */
  --space-20: 5rem;      /* 80px */

  /* ── Border Radius ───────────────────── */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;

  /* ── Shadows ─────────────────────────── */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);

  /* ── Transitions ─────────────────────── */
  --transition-fast:   150ms ease;
  --transition-normal: 250ms ease;
  --transition-slow:   350ms ease;

  /* ── Z-Index Scale ───────────────────── */
  --z-base:    0;
  --z-dropdown: 100;
  --z-sticky:  200;
  --z-modal:   300;
  --z-toast:   400;
  --z-tooltip: 500;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg:           #111827;
    --color-bg-subtle:    #1f2937;
    --color-text-primary: #f9fafb;
    --color-border:       #374151;
  }
}
```

### Bước 3: Component Chuẩn Từ Figma

```vue
<!-- BaseButton.vue – Button variants từ Figma -->
<script setup>
defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (v) => ['primary', 'secondary', 'ghost', 'danger', 'outline'].includes(v)
  },
  size:   { type: String, default: 'md', validator: (v) => ['sm', 'md', 'lg'].includes(v) },
  loading:  { type: Boolean, default: false },
  disabled: { type: Boolean, default: false },
  fullWidth: { type: Boolean, default: false },
})

defineEmits(['click'])
</script>

<template>
  <button
    :class="['btn', `btn--${variant}`, `btn--${size}`, { 'btn--loading': loading, 'btn--full': fullWidth }]"
    :disabled="disabled || loading"
    @click="$emit('click', $event)"
  >
    <span v-if="loading" class="btn__spinner" aria-hidden="true" />
    <slot />
  </button>
</template>

<style scoped>
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  font-family: var(--font-sans);
  font-weight: var(--font-medium);
  border-radius: var(--radius-md);
  border: 1.5px solid transparent;
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
  line-height: 1;
}

/* Sizes */
.btn--sm { padding: var(--space-2) var(--space-3); font-size: var(--text-sm);  height: 32px; }
.btn--md { padding: var(--space-3) var(--space-4); font-size: var(--text-base); height: 40px; }
.btn--lg { padding: var(--space-4) var(--space-6); font-size: var(--text-lg);  height: 48px; }

/* Variants */
.btn--primary {
  background: var(--color-primary);
  color: #fff;
}
.btn--primary:hover:not(:disabled) { background: var(--color-primary-hover); }

.btn--outline {
  background: transparent;
  border-color: var(--color-primary);
  color: var(--color-primary);
}
.btn--outline:hover:not(:disabled) {
  background: var(--color-primary-light);
}

.btn--ghost {
  background: transparent;
  color: var(--color-text-secondary);
}
.btn--ghost:hover:not(:disabled) { background: var(--color-bg-subtle); }

.btn--danger {
  background: var(--color-error);
  color: #fff;
}

.btn--secondary {
  background: var(--color-bg-subtle);
  color: var(--color-text-primary);
  border-color: var(--color-border);
}

/* States */
.btn--full { width: 100%; }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }
.btn:focus-visible { outline: 2px solid var(--color-primary); outline-offset: 2px; }

/* Loading spinner */
.btn__spinner {
  width: 16px; height: 16px;
  border: 2px solid rgba(255,255,255,0.3);
  border-radius: 50%;
  border-top-color: currentColor;
  animation: spin 0.6s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
</style>
```

### Bước 4: Responsive Layout

```css
/* Breakpoints từ Figma specs */
/* Mobile first approach */

.container {
  width: 100%;
  padding-inline: var(--space-4);    /* 16px */
  margin-inline: auto;

  /* Tablet: 768px+ */
  @media (min-width: 768px) {
    padding-inline: var(--space-8);  /* 32px */
  }

  /* Desktop: 1280px+ */
  @media (min-width: 1280px) {
    max-width: 1280px;
    padding-inline: var(--space-16); /* 64px */
  }
}

/* CSS Grid – 12 column system */
.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-6);
}

/* Responsive grid areas */
.product-layout {
  display: grid;
  gap: var(--space-6);
  grid-template-areas:
    "image"
    "info"
    "sidebar";

  @media (min-width: 768px) {
    grid-template-columns: 1fr 1fr;
    grid-template-areas:
      "image info"
      "image sidebar";
  }

  @media (min-width: 1280px) {
    grid-template-columns: 1fr 1.5fr 300px;
    grid-template-areas: "image info sidebar";
  }
}
```

---

## 🎯 MOCK INTERVIEW: Câu Hỏi Khó – Trả Lời Chuẩn

### Scenario 1: "Hãy thiết kế architecture cho trang e-commerce có 100k users"

**✅ Trả lời tốt:**

```
Frontend (Nuxt 3 SSR):
├── CDN (Cloudflare) → cache static assets, SSG pages
├── SSR cho product pages → SEO + fast FCP
├── CSR/hydration cho user-specific content (cart, auth)
└── Code splitting theo route → bundle nhỏ

State Management:
├── Pinia: cart, auth, UI state
├── Server state: useFetch với cache keys
└── Optimistic updates cho cart

Performance:
├── Image optimization: NuxtImage → WebP + srcset
├── Lazy loading: defineAsyncComponent cho heavy components
├── Virtual scroll cho product lists
├── Service Worker (PWA): cache API responses
└── Prefetch: mouseover → prefetch product detail

Backend (Laravel):
├── Queue: email, notifications → không block response
├── Cache (Redis): product listings, categories (5-15 phút TTL)
├── Database: read replicas cho queries, primary cho writes
├── API Rate limiting: throttle per user
└── CDN cho media files
```

---

### Scenario 2: "Bạn phát hiện trang web load rất chậm. Cách debug?"

**✅ Trả lời có cấu trúc:**

```
Step 1: Đo lường (không đoán)
├── Chrome DevTools → Lighthouse audit
├── Network tab → xem request waterfall
├── Performance tab → record + phân tích flame chart
└── Web Vitals: LCP, FID, CLS

Step 2: Xác định bottleneck
├── LCP chậm → image không optimize, TTFB chậm (server slow)
├── CLS cao   → image không có width/height, font flash
├── FID cao   → JavaScript blocking, hydration lâu
└── Network   → large JS bundle, too many requests, no caching

Step 3: Fix theo thứ tự impact
Frontend:
├── Bundle: dùng vite-bundle-visualizer → xem chunk lớn
├── Images: NuxtImage + lazy + WebP + srcset
├── Fonts: preload + font-display: swap
├── Third-party: load async (Hotjar, chat widget)
└── Prefetch: critical routes

Backend:
├── EXPLAIN ANALYZE → tìm slow queries
├── Add missing indexes
├── N+1 → eager loading
├── Cache hot data (Redis remember)
└── Enable gzip/brotli compression
```

---

### Scenario 3: "Giải thích cách xử lý race condition trong Vue"

```javascript
// Scenario: User search nhanh → nhiều requests → response về không đúng thứ tự

// ❌ Vấn đề
async function search(q) {
  const results = await api.get('/search?q=' + q)
  displayResults.value = results  // Race condition: response cũ về sau → ghi đè kết quả mới
}

// ✅ Fix 1: AbortController
let controller = null

async function search(q) {
  controller?.abort()  // Hủy request trước
  controller = new AbortController()

  try {
    const results = await api.get('/search?q=' + q, { signal: controller.signal })
    displayResults.value = results
  } catch (e) {
    if (e.name !== 'AbortError') throw e
  }
}

// ✅ Fix 2: Request ID (nếu không dùng fetch/axios)
let requestId = 0

async function search(q) {
  const id = ++requestId   // Tăng ID mỗi request

  const results = await someOtherLib.search(q)

  if (id !== requestId) return  // Request cũ → ignore
  displayResults.value = results
}

// ✅ Fix 3: Debounce + AbortController (production pattern)
const { query, results, loading } = useDebouncedSearch('/api/search', { delay: 400 })
// useDebouncedSearch (bài VUE-06) đã handle cả debounce + abort
```

---

### Scenario 4: "Laravel app bị tấn công SQL Injection, phân tích và fix"

```php
// ❌ Vulnerable code trong legacy codebase
public function search(Request $request)
{
    $name = $request->input('name');
    // Attacker gửi: ' OR 1=1 --
    $products = DB::select("SELECT * FROM products WHERE name = '$name'");
    // Query thực tế: SELECT * FROM products WHERE name = '' OR 1=1 --'
    // → Trả về TẤT CẢ products!
}

// ✅ Fix 1: Parameterized query
$products = DB::select('SELECT * FROM products WHERE name = ?', [$name]);

// ✅ Fix 2: Eloquent (luôn parameterized)
$products = Product::where('name', $name)->get();

// ✅ Fix 3: nếu cần raw SQL với dynamic columns (ví dụ ORDER BY)
$allowedColumns = ['name', 'price', 'created_at'];  // Whitelist
$column = in_array($request->sort, $allowedColumns)
    ? $request->sort
    : 'created_at';
// → Không bao giờ dùng $request->sort trực tiếp trong query

$products = DB::select("SELECT * FROM products ORDER BY {$column} ASC");
```

---

### Scenario 5: "Làm sao để Vue app không bị re-render không cần thiết?"

```vue
<script setup>
// ❌ Tạo object/array inline trong template → ref mới mỗi render
// Mỗi lần parent re-render, Child nhận prop object mới (dù content giống)
// → Child re-render dù không cần thiết
</script>

<template>
  <!-- ❌ Options object tạo mới mỗi render -->
  <ExpensiveChild :options="{ size: 'lg', variant: 'primary' }" />

  <!-- ❌ Inline function tạo mới mỗi render -->
  <ExpensiveChild :onSelect="(item) => handleSelect(item)" />
</template>

<!-- ✅ Fix -->
<script setup>
import { computed, useCallback } from 'vue'

// Dùng computed để memoize object (chỉ tạo mới khi dependency thay đổi)
const childOptions = computed(() => ({ size: 'lg', variant: 'primary' }))

// Với function: define ở ngoài template (function reference stable)
function handleSelect(item) { /* ... */ }
</script>

<template>
  <ExpensiveChild :options="childOptions" :onSelect="handleSelect" />
</template>
```

```javascript
// v-memo: skip re-render nếu dependency không đổi
// Dùng cho list items đắt tiền
<div v-for="item in list" :key="item.id" v-memo="[item.id, item.name, isSelected(item.id)]">
  <ExpensiveItemRenderer :item="item" :selected="isSelected(item.id)" />
</div>
// → Nếu item.id, item.name, isSelected không đổi → skip re-render hoàn toàn
```

---

## 📊 HTTP Status Codes – Bảng Tra Cứu Phỏng Vấn

| Code | Tên | Dùng khi |
|---|---|---|
| **200** | OK | Request thành công (GET, PUT, PATCH, DELETE) |
| **201** | Created | Tạo resource thành công (POST) |
| **204** | No Content | Thành công, không có body (DELETE) |
| **301** | Moved Permanently | Redirect URL cũ → URL mới (SEO pass link juice) |
| **302** | Found | Temporary redirect |
| **304** | Not Modified | Cache valid, không gửi body lại |
| **400** | Bad Request | Request malformed, dữ liệu sai format |
| **401** | Unauthorized | Chưa xác thực (cần login/token) |
| **403** | Forbidden | Đã xác thực nhưng không có quyền |
| **404** | Not Found | Resource không tồn tại |
| **405** | Method Not Allowed | GET thay vì POST, etc. |
| **409** | Conflict | Resource đã tồn tại (duplicate email) |
| **422** | Unprocessable Entity | Validation errors (Laravel dùng cái này) |
| **429** | Too Many Requests | Rate limit exceeded |
| **500** | Internal Server Error | Server crash, lỗi không xử lý |
| **503** | Service Unavailable | Server maintenance, overload |

---

## 🔐 Security Checklist – Trước Khi Deploy

### Frontend
```
✅ Không lưu sensitive data trong localStorage (dùng httpOnly cookie hoặc memory)
✅ Sanitize user input trước khi render v-html (dùng DOMPurify)
✅ CSP (Content Security Policy) header
✅ HTTPS only (HSTS header)
✅ Không expose API keys trong frontend code (dùng env variables)
✅ Rate limit requests từ client (debounce search, disable button after submit)
```

### Backend (Laravel)
```
✅ Dùng Eloquent/parameterized queries – không raw string interpolation
✅ Mass assignment protection: $fillable hoặc $guarded
✅ Validate TẤT CẢ input (FormRequest)
✅ Auth:sanctum cho API routes
✅ Policy/Gate cho resource authorization
✅ Rate limiting: throttle middleware
✅ CORS: chỉ allow trusted origins
✅ Không log sensitive data (password, token, credit card)
✅ Dependency updates: composer audit
✅ Remove debug routes trong production (.env APP_DEBUG=false)
✅ Database backup + encryption at rest
```

---

## 📝 Câu Hỏi HR Thường Gặp – Trả Lời Khéo

**Q: "Tại sao bạn muốn ứng tuyển vào công ty chúng tôi?"**
```
✅ Tốt: Nghiên cứu sản phẩm công ty, đề cập cụ thể
"Tôi ấn tượng với [sản phẩm cụ thể], đặc biệt cách handle [vấn đề cụ thể].
Tech stack Vue.js + Laravel phù hợp với định hướng phát triển của tôi.
Tôi muốn contribute vào sản phẩm có real impact đến người dùng."

❌ Tệ: "Vì công ty có môi trường tốt và lương cao"
```

**Q: "Điểm yếu của bạn là gì?"**
```
✅ Tốt: Thật nhưng có cách khắc phục
"Tôi đôi khi overthink về architecture quá sớm (premature optimization).
Tôi đang học cách viết code đủ tốt cho hiện tại và refactor khi cần,
thay vì engineer mọi thứ từ đầu."

❌ Tệ: "Tôi làm việc quá chăm chỉ" (quá rõ là bịa)
```

**Q: "Kể về dự án khó khăn nhất và cách bạn giải quyết?"**
```
✅ Dùng STAR method:
S (Situation): "Trong dự án X, chúng tôi cần..."
T (Task): "Nhiệm vụ của tôi là..."
A (Action): "Tôi đã... [kỹ thuật cụ thể]"
R (Result): "Kết quả là... [số liệu cụ thể nếu có]"

Ví dụ: "Dự án cần real-time notification cho 500+ users đồng thời.
Thử WebSocket đầu tiên bị timeout issues.
Chuyển sang Server-Sent Events với Laravel Broadcasting.
Kết quả: latency giảm từ 2s xuống 200ms, không có timeout."
```

**Q: "5 năm tới bạn muốn ở đâu?"**
```
✅ Tốt: Thực tế + align với công ty
"Tôi muốn trở thành Senior Frontend/Fullstack developer với deep expertise
trong Vue/Laravel ecosystem. Muốn lead được small team và mentor junior devs.
Tôi thấy [công ty] có lộ trình phát triển phù hợp với mục tiêu này."
```

---

## ⚡ Quick Interview Cheat Sheet

```
Vue.js Reactivity:
  ref          → primitive + .value, works everywhere
  reactive     → object/array, no .value, mất reactivity khi destructure
  computed     → cached derived value, lazy eval
  watch        → side effects, lazy, oldVal/newVal
  watchEffect  → auto-track, eager, không có oldVal

Lifecycle:
  setup (composition) = beforeCreate + created
  onMounted           = DOM sẵn sàng, fetch data, DOM manipulation
  onUnmounted         = cleanup timers, observers, event listeners

v-model custom:
  :modelValue + @update:modelValue
  v-model:filters = :filters + @update:filters

Pinia:
  storeToRefs() để destructure state + getters (giữ reactivity)
  Actions: lấy trực tiếp (stable reference)

Nuxt fetch:
  useFetch    = useAsyncData + $fetch + auto-key từ URL, cached
  useAsyncData = custom key + custom fetcher, SSR-aware
  $fetch      = raw, no cache, no SSR, dùng trong events

Laravel:
  N+1 fix     = with(), withCount(), withAvg()
  Mass assign = $fillable (whitelist) > $guarded (blacklist)
  cascade     = xóa FK → xóa related (pivot tables)
  restrict    = xóa FK → lỗi nếu còn related (tài chính)
  Job         = async task, ShouldQueue, SerializesModels
  Event       = fire → nhiều Listeners, loose coupling

HTTP:
  401 = chưa login (Who are you?)
  403 = đã login nhưng không có quyền (I know you, but NO)
  422 = validation error (Unprocessable Entity)
  429 = too many requests (Rate limited)
```
