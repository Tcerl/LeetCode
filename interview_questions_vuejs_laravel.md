# 🎯 Tổng Hợp Kiến Thức Phỏng Vấn – Phạm Duy Tín

> **Vị trí ứng tuyển:** Frontend (Vue.js / Nuxt.js) | Fullstack (Vue.js + Laravel)  
> **Phân tích CV:** Background Python/Flask → cần bổ sung Vue.js & Laravel mạnh  
> **Mục tiêu:** Lấp đầy gap kiến thức + ôn trọng tâm theo JD

---

## ⚡ Phân Tích Gap CV vs Yêu Cầu JD

| Kỹ năng JD yêu cầu | CV của bạn | Mức độ cần ôn |
|---|---|---|
| Vue.js / Nuxt.js | JavaScript cơ bản, Next.js | 🔴 Cần học mới |
| Vuex / Pinia | Chưa có | 🔴 Cần học mới |
| Laravel Framework | Python/Flask (tương đồng MVC) | 🟡 Học framework mới |
| Eloquent ORM | SQLAlchemy (tương đồng) | 🟢 Dễ chuyển đổi |
| RESTful API | Có kinh nghiệm (Flask) | 🟢 Chỉ cần ôn lại |
| Docker | eCommerce project | 🟢 Có kinh nghiệm |
| PostgreSQL / MySQL | Đã dùng | 🟢 Có kinh nghiệm |
| JWT / OAuth2 | Chưa rõ | 🟡 Cần ôn |
| Figma → Code | Chưa đề cập | 🟡 Cần thực hành |

---

## 🗂️ Lộ Trình Ôn Tập Ưu Tiên

```
Tuần 1: Vue.js Core + Component patterns
Tuần 2: Pinia + Nuxt.js + SSR/SEO
Tuần 3: Laravel Core (MVC, Eloquent, Middleware)
Tuần 4: Laravel nâng cao (Queue, Job, Event) + JWT API
Tuần 5: Thực hành fullstack project + luyện câu hỏi phỏng vấn
```

---

## 📌 PHẦN 1 – VUE.JS (Ưu tiên cao nhất)

> 💡 Bạn biết JavaScript & Next.js → nền tốt để học Vue.js

### 1.1 Composition API (Bắt buộc biết)

```vue
<script setup>
import { ref, reactive, computed, watch, onMounted } from 'vue'

// ref cho primitive values
const count = ref(0)
const name = ref('Tín')

// reactive cho object
const user = reactive({ name: 'Tín', age: 23 })

// computed – chỉ tính lại khi dependency thay đổi
const greeting = computed(() => `Xin chào, ${name.value}!`)

// watch – theo dõi thay đổi
watch(count, (newVal, oldVal) => {
  console.log(`${oldVal} → ${newVal}`)
})

// lifecycle
onMounted(() => {
  // Gọi API, thao tác DOM ở đây
})
</script>

<template>
  <div>
    <p>{{ greeting }}</p>
    <button @click="count++">Count: {{ count }}</button>
  </div>
</template>
```

### 1.2 So sánh với React/Next.js (bạn đã biết)

| Khái niệm | React (Next.js) | Vue 3 |
|---|---|---|
| State | `useState` | `ref` / `reactive` |
| Side effects | `useEffect` | `watch` / `watchEffect` |
| Computed | `useMemo` | `computed` |
| Lifecycle | `useEffect(fn, [])` | `onMounted` |
| Props | `props` truyền xuống | `defineProps` |
| Emit events | `callback props` | `defineEmits` |
| Context | `useContext` | `provide` / `inject` |
| Custom hooks | `useXxx` hook | `useXxx` composable |

### 1.3 Component Communication

```vue
<!-- ChildComponent.vue -->
<script setup>
const props = defineProps({
  title: { type: String, required: true },
  items: { type: Array, default: () => [] }
})
const emit = defineEmits(['select', 'delete'])

function onSelect(item) {
  emit('select', item)
}
</script>

<!-- ParentComponent.vue -->
<ChildComponent
  title="Danh sách"
  :items="productList"
  @select="handleSelect"
/>
```

### 1.4 Directives quan trọng

```vue
<template>
  <!-- Conditional -->
  <div v-if="isAdmin">Admin panel</div>
  <div v-else-if="isMod">Mod panel</div>
  <div v-else>User view</div>

  <!-- v-show: toggle display:none, không xóa DOM -->
  <Modal v-show="isOpen" />

  <!-- Loop – LUÔN cần :key -->
  <li v-for="item in list" :key="item.id">
    {{ item.name }}
  </li>

  <!-- Two-way binding -->
  <input v-model="searchQuery" placeholder="Tìm kiếm..." />

  <!-- Events -->
  <button @click.prevent="submit">Gửi</button>
  <input @keyup.enter="search" />

  <!-- Dynamic binding -->
  <div :class="{ active: isActive, 'text-red': hasError }"></div>
  <img :src="imageUrl" :alt="imageTitle" />
</template>
```

### 1.5 Composables – Tái sử dụng logic

```javascript
// composables/useApi.js – tương tự Service trong Flask
export function useApi(endpoint) {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const fetchData = async (params = {}) => {
    loading.value = true
    error.value = null
    try {
      const res = await fetch(endpoint + '?' + new URLSearchParams(params))
      data.value = await res.json()
    } catch (e) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  return { data, loading, error, fetchData }
}

// Sử dụng trong component
const { data: products, loading, fetchData } = useApi('/api/products')
onMounted(() => fetchData({ page: 1 }))
```

---

## 📌 PHẦN 2 – PINIA STATE MANAGEMENT

> 💡 Giống như "global context" trong Flask - biến dùng chung toàn app

```javascript
// stores/useCartStore.js
import { defineStore } from 'pinia'

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: [],
    discount: 0,
  }),

  getters: {
    // Computed properties
    totalItems: (state) => state.items.reduce((sum, i) => sum + i.qty, 0),
    totalPrice: (state) => {
      const subtotal = state.items.reduce((sum, i) => sum + i.price * i.qty, 0)
      return subtotal * (1 - state.discount / 100)
    },
  },

  actions: {
    // Methods – có thể async
    addItem(product) {
      const existing = this.items.find(i => i.id === product.id)
      if (existing) {
        existing.qty++
      } else {
        this.items.push({ ...product, qty: 1 })
      }
    },
    removeItem(productId) {
      this.items = this.items.filter(i => i.id !== productId)
    },
    async checkout() {
      const res = await api.post('/orders', { items: this.items })
      this.items = []
      return res.data
    }
  }
})
```

```vue
<!-- Sử dụng store -->
<script setup>
import { useCartStore } from '@/stores/useCartStore'
const cart = useCartStore()
</script>
<template>
  <span>🛒 {{ cart.totalItems }} items – {{ cart.totalPrice }}đ</span>
  <button @click="cart.addItem(product)">Thêm vào giỏ</button>
</template>
```

---

## 📌 PHẦN 3 – NUXT.JS & SSR

> 💡 Next.js bạn đã biết → Nuxt.js là "Next.js của Vue"

### 3.1 So sánh Nuxt vs Next.js

| Tính năng | Next.js (React) | Nuxt.js (Vue) |
|---|---|---|
| File routing | `pages/` hoặc `app/` | `pages/` |
| Data fetching | `getServerSideProps` / `fetch` | `useFetch` / `useAsyncData` |
| API routes | `pages/api/` | `server/api/` |
| Auto import | Không | Có (components, composables) |
| SSR config | Per-page | Per-page hoặc `routeRules` |

### 3.2 Data Fetching

```vue
<script setup>
// useFetch – cách thông dụng nhất
const { data: posts, pending, error, refresh } = await useFetch('/api/posts', {
  query: { page: 1, limit: 10 },
  transform: (res) => res.data,    // Transform response
})

// useAsyncData – khi cần key tùy chỉnh
const { data: user } = await useAsyncData(
  'current-user',                  // Key để cache
  () => $fetch('/api/auth/me'),
  { server: true }
)
</script>
```

### 3.3 SEO Meta Tags

```vue
<script setup>
// Trang blog detail
const route = useRoute()
const { data: post } = await useFetch(`/api/posts/${route.params.slug}`)

useSeoMeta({
  title: () => post.value?.title,
  description: () => post.value?.excerpt,
  ogImage: () => post.value?.thumbnail,
  ogTitle: () => post.value?.title,
})
</script>
```

---

## 📌 PHẦN 4 – LARAVEL FRAMEWORK

> 💡 Bạn có nền Flask/Python → Laravel PHP cùng pattern MVC, dễ chuyển đổi

### 4.1 So sánh Flask vs Laravel

| Khái niệm | Python/Flask | Laravel (PHP) |
|---|---|---|
| Routing | `@app.route()` | `Route::get()` |
| ORM | SQLAlchemy | Eloquent |
| Migration | Alembic | `php artisan migrate` |
| Middleware | `@app.before_request` | Middleware class |
| Validation | WTForms / Marshmallow | FormRequest |
| Job Queue | Celery | Laravel Queue |
| Templates | Jinja2 | Blade |

### 4.2 Routing & Controller

```php
// routes/api.php
Route::prefix('v1')->middleware('auth:sanctum')->group(function () {
    Route::get('/products', [ProductController::class, 'index']);
    Route::post('/products', [ProductController::class, 'store']);
    Route::get('/products/{product}', [ProductController::class, 'show']);
    Route::put('/products/{product}', [ProductController::class, 'update']);
    Route::delete('/products/{product}', [ProductController::class, 'destroy']);
    
    // Hoặc gộp thành apiResource
    Route::apiResource('categories', CategoryController::class);
});
```

```php
// app/Http/Controllers/ProductController.php
class ProductController extends Controller
{
    // Dependency Injection – giống Flask inject service
    public function __construct(private ProductService $service) {}

    public function index(Request $request)
    {
        $products = Product::with('category')
            ->when($request->search, fn($q) => $q->where('name', 'like', "%{$request->search}%"))
            ->paginate(15);

        return ProductResource::collection($products);
    }

    public function store(StoreProductRequest $request)
    {
        $product = $this->service->create($request->validated());
        return new ProductResource($product);
    }
}
```

### 4.3 Eloquent ORM (giống SQLAlchemy)

```php
// app/Models/Product.php
class Product extends Model
{
    protected $fillable = ['name', 'price', 'category_id', 'description'];
    protected $casts = ['price' => 'decimal:2', 'is_active' => 'boolean'];

    // Relationships
    public function category(): BelongsTo
    {
        return $this->belongsTo(Category::class);
    }

    public function tags(): BelongsToMany
    {
        return $this->belongsToMany(Tag::class);
    }

    // Scope – tái sử dụng query
    public function scopeActive($query)
    {
        return $query->where('is_active', true);
    }

    public function scopePriceRange($query, $min, $max)
    {
        return $query->whereBetween('price', [$min, $max]);
    }
}

// ⚠️ TRÁNH N+1 QUERY – lỗi phổ biến nhất
// BAD:
$products = Product::all();
foreach ($products as $p) {
    echo $p->category->name; // Query mỗi vòng lặp!
}

// GOOD: Eager loading
$products = Product::with(['category', 'tags'])->active()->get();
```

### 4.4 Middleware

```php
// Tạo: php artisan make:middleware RoleMiddleware
class RoleMiddleware
{
    public function handle(Request $request, Closure $next, string ...$roles): Response
    {
        if (!in_array(auth()->user()->role, $roles)) {
            return response()->json(['message' => 'Forbidden'], 403);
        }
        return $next($request);
    }
}

// Dùng trong route
Route::middleware(['auth:sanctum', 'role:admin,manager'])->group(...);
```

### 4.5 Migration

```php
// php artisan make:migration create_products_table
Schema::create('products', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->string('slug')->unique();
    $table->decimal('price', 10, 2);
    $table->unsignedBigInteger('category_id');
    $table->foreign('category_id')->references('id')->on('categories')->cascadeOnDelete();
    $table->boolean('is_active')->default(true);
    $table->json('metadata')->nullable();
    $table->timestamps();
    $table->softDeletes();

    $table->index(['category_id', 'is_active']); // Performance
});
```

### 4.6 Queue & Job

```php
// php artisan make:job ProcessOrder

class ProcessOrder implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public int $tries = 3;      // Retry 3 lần nếu thất bại
    public int $timeout = 120;  // Timeout 2 phút

    public function __construct(private Order $order) {}

    public function handle(PaymentService $payment): void
    {
        // Xử lý đơn hàng bất đồng bộ
        $payment->charge($this->order);
        $this->order->update(['status' => 'paid']);
        event(new OrderPaid($this->order));
    }

    public function failed(\Throwable $e): void
    {
        Log::error('Order processing failed', [
            'order_id' => $this->order->id,
            'error' => $e->getMessage()
        ]);
    }
}

// Dispatch
ProcessOrder::dispatch($order);                           // Vào queue ngay
ProcessOrder::dispatch($order)->delay(now()->addMinutes(2)); // Delay 2 phút
ProcessOrder::dispatch($order)->onQueue('high-priority');    // Queue cụ thể
```

---

## 📌 PHẦN 5 – RESTful API & JWT

> 💡 Bạn đã làm API với Flask → phần này chủ yếu ôn thêm JWT & best practices

### 5.1 JWT Flow

```
1. POST /api/login  { email, password }
         ↓
2. Server verify → tạo JWT (header.payload.signature)
         ↓
3. Client nhận token → lưu vào localStorage / httpOnly cookie
         ↓
4. Mọi request tiếp theo: Authorization: Bearer <token>
         ↓
5. Server verify signature → xác thực → xử lý request
         ↓
6. Token hết hạn (15-60 phút) → dùng refresh token để lấy token mới
```

```javascript
// Vue.js – Setup Axios với JWT
import axios from 'axios'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

// Tự động gắn token vào mọi request
api.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

// Tự động refresh token khi 401
api.interceptors.response.use(
  res => res,
  async err => {
    if (err.response?.status === 401 && !err.config._retry) {
      err.config._retry = true
      try {
        const { data } = await axios.post('/api/refresh', {
          refresh_token: localStorage.getItem('refresh_token')
        })
        localStorage.setItem('access_token', data.access_token)
        return api(err.config) // Retry request gốc
      } catch {
        // Refresh thất bại → logout
        localStorage.clear()
        router.push('/login')
      }
    }
    return Promise.reject(err)
  }
)
```

```php
// Laravel – JWT với Laravel Sanctum (đơn giản hơn JWT thuần)
// routes/api.php
Route::post('/login', function (Request $request) {
    $request->validate(['email' => 'required|email', 'password' => 'required']);

    if (!Auth::attempt($request->only('email', 'password'))) {
        return response()->json(['message' => 'Invalid credentials'], 401);
    }

    $user = Auth::user();
    $token = $user->createToken('api-token')->plainTextToken;

    return response()->json([
        'token' => $token,
        'user' => new UserResource($user),
    ]);
});

Route::middleware('auth:sanctum')->post('/logout', function (Request $request) {
    $request->user()->currentAccessToken()->delete();
    return response()->json(['message' => 'Logged out']);
});
```

### 5.2 HTTP Status Codes (Phải thuộc lòng)

```
2xx Success:
  200 OK               – GET thành công
  201 Created          – POST tạo mới thành công
  204 No Content       – DELETE thành công

4xx Client Error:
  400 Bad Request      – Request sai format
  401 Unauthorized     – Chưa đăng nhập / token hết hạn
  403 Forbidden        – Đã đăng nhập nhưng không có quyền
  404 Not Found        – Resource không tồn tại
  422 Unprocessable    – Validation failed (form data sai)
  429 Too Many Requests – Rate limit exceeded

5xx Server Error:
  500 Internal Server Error – Bug trong server
  503 Service Unavailable   – Server đang maintain
```

---

## 📌 PHẦN 6 – CẮT GIAO DIỆN TỪ FIGMA

> 💡 CV của bạn có nền HTML/CSS → cần luyện thêm responsive và pixel-perfect

### 6.1 Quy trình chuẩn

```
1. Mở Figma → Inspect panel (Ctrl+Shift+I)
2. Ghi lại: màu sắc, font, spacing, border-radius, shadow
3. Tạo CSS variables từ design tokens
4. Code mobile-first → thêm breakpoints cho tablet/desktop
5. So sánh với Figma ở các breakpoint
6. Test browser: Chrome, Firefox, Safari mobile
```

### 6.2 CSS Variables & Responsive

```css
:root {
  --primary: #3B82F6;
  --text-primary: #1F2937;
  --font: 'Inter', sans-serif;
  --radius: 8px;
  --shadow: 0 1px 3px rgba(0,0,0,0.1);
}

/* Mobile first */
.card {
  width: 100%;
  padding: 16px;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}

@media (min-width: 768px) {
  .card { max-width: 400px; }
}
```

---

## ❓ Câu Hỏi Phỏng Vấn Thường Gặp

### Vue.js

| Câu hỏi | Trả lời ngắn gọn |
|---|---|
| `v-if` vs `v-show`? | `v-if` xóa/tạo DOM. `v-show` toggle CSS display. |
| `ref` vs `reactive`? | `ref` cho primitive + cần `.value`. `reactive` cho object. |
| Composable là gì? | Function tái sử dụng logic (stateful), thay thế Mixin. |
| Tại sao cần `:key` trong `v-for`? | Giúp Vue track DOM element khi list thay đổi, tránh bug. |
| `computed` vs `method`? | `computed` cache kết quả. `method` luôn chạy lại. |
| Virtual DOM là gì? | JS object đại diện DOM thật, Vue diff để update tối thiểu. |

### Laravel

| Câu hỏi | Trả lời ngắn gọn |
|---|---|
| N+1 query là gì? | Loop + gọi relation mỗi vòng → dùng `with()` eager loading. |
| Service Container? | IoC container tự động inject dependencies khi được bind. |
| Middleware dùng để làm gì? | Xử lý request trước Controller: auth, CORS, rate limit. |
| Queue vs Job? | Job = task cụ thể. Queue = hàng đợi chạy Job bất đồng bộ. |
| Migration rollback an toàn? | Luôn backup DB trước, không rollback migration có data. |

### API & Security

| Câu hỏi | Trả lời ngắn gọn |
|---|---|
| JWT vs Session? | JWT stateless (server không lưu). Session stateful (server lưu). |
| Refresh token dùng để làm gì? | Lấy access token mới không cần login lại khi token hết hạn. |
| CORS là gì? | Browser block cross-origin request – server cần set header cho phép. |
| Cách bảo mật API? | Validate input, rate limit, HTTPS, không lộ stack trace, API Resource. |

---

## 🏆 Điểm Mạnh Cần Nhấn Mạnh Khi Phỏng Vấn

> Dựa trên CV của bạn, đây là những điểm nên highlight:

1. **Kinh nghiệm thực tế với Docker** → đề cập khi nói về deployment
2. **Đã làm eCommerce migration** → hiểu đa nền tảng (Shopify, Magento, WooCommerce)
3. **SQLAlchemy → Eloquent** → "Tôi đã dùng SQLAlchemy trong Flask, pattern tương tự Eloquent nên tôi học nhanh"
4. **Flask REST API** → "Tôi đã xây dựng RESTful API với Flask, hiểu nguyên lý request/response cycle"
5. **Full-stack background** → UI/UX + Backend + Database

---

## ✅ Checklist Chuẩn Bị

### Kiến thức nền (Phải biết)
- [ ] Vue 3 Composition API (`ref`, `reactive`, `computed`, `watch`)
- [ ] Component: `props`, `emit`, `slots`, `provide/inject`
- [ ] Pinia: `state`, `getters`, `actions`
- [ ] Vue Router: navigation guards, dynamic routes
- [ ] Nuxt 3: `useFetch`, `useHead`, file routing, SSR concept

### Laravel (Phải biết)
- [ ] CRUD API với Controller + FormRequest + Resource
- [ ] Eloquent: relationships, eager loading, scopes
- [ ] Middleware authentication
- [ ] Migration + Seeder
- [ ] Queue + Job (ít nhất thuộc lý thuyết)

### Thực hành (Nên có portfolio)
- [ ] **Project 1:** Todo App – Vue 3 + Pinia + Laravel API + JWT auth
- [ ] **Project 2:** Clone 1 trang từ Figma (responsive hoàn chỉnh)
- [ ] Đẩy lên GitHub với README rõ ràng

### Kỹ năng mềm (Hay được hỏi)
- [ ] Giải thích quy trình làm việc với BA và Tester
- [ ] Cách báo cáo tiến độ cho Project Manager
- [ ] Cách tự học công nghệ mới (ví dụ: chuyển từ Python sang PHP/Vue)

---

> 📌 **File giáo trình chi tiết hơn:** xem `interview_prep_vuejs_laravel.md`  
> 🔗 **Tài liệu chính thống:** [vuejs.org](https://vuejs.org) | [nuxt.com/docs](https://nuxt.com/docs) | [laravel.com/docs](https://laravel.com/docs)
