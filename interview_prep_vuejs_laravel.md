# 📚 Giáo Trình Phỏng Vấn: Vue.js + Laravel Fullstack

> **Mục tiêu:** Chuẩn bị kiến thức đầy đủ cho vị trí Frontend (Vue.js / Nuxt.js) hoặc Fullstack (Vue.js + Laravel)  
> **Kinh nghiệm yêu cầu:** 1–2 năm  
> **Ngày tạo:** 2026-03-03

---

## 📋 Mục Lục

1. [Vue.js Core](#1-vuejs-core)
2. [State Management – Vuex & Pinia](#2-state-management--vuex--pinia)
3. [Component Patterns & Performance](#3-component-patterns--performance)
4. [Nuxt.js – SSR & SEO](#4-nuxtjs--ssr--seo)
5. [Cắt giao diện từ Figma](#5-cắt-giao-diện-từ-figma)
6. [Laravel Framework](#6-laravel-framework)
7. [RESTful API & Bảo mật](#7-restful-api--bảo-mật)
8. [Câu hỏi phỏng vấn thường gặp](#8-câu-hỏi-phỏng-vấn-thường-gặp)

---

## 1. Vue.js Core

### 1.1 Options API vs Composition API

| Tính năng         |Options API                     | Composition API              |
|-------------------|---------------------------------|------------------------------|
| Cú pháp           | `data()`, `methods`, `computed` | `setup()`, `ref`, `reactive` |
| Tái sử dụng logic | Mixins (dễ xung đột)            | Composables (sạch hơn)       |
| TypeScript        | Hạn chế                         | Hỗ trợ tốt                   |
| Vue version       | Vue 2 & 3                       | Vue 3+                       |

```vue
<!-- Composition API – Vue 3 -->
<script setup>
import { ref, computed, onMounted } from 'vue'

const count = ref(0)
const double = computed(() => count.value * 2)

onMounted(() => console.log('Component mounted'))
</script>
```

### 1.2 Reactivity System

```javascript
import { ref, reactive, toRefs, watch, watchEffect } from 'vue'

// ref – dùng cho primitive
const name = ref('Tín')

// reactive – dùng cho object
const user = reactive({ name: 'Tín', age: 25 })

// watch – theo dõi source cụ thể
watch(name, (newVal, oldVal) => {
  console.log(`${oldVal} → ${newVal}`)
})

// watchEffect – tự động track dependency
watchEffect(() => {
  console.log('name is:', name.value)
})
```

### 1.3 Lifecycle 


```
beforeCreate → created → beforeMount → mounted
→ beforeUpdate → updated
→ beforeUnmount → unmounted
```

| Hook            | Dùng khi                    |
|-----------------|-----------------------------|
| `onMounted`     | Gọi API, thao tác DOM       |
| `onUnmounted`   | Dọn event listener, timer   |
| `onUpdated`     | Phản ứng sau DOM update     |
| `onBeforeMount` | Logic trước khi render      |

### 1.4 Component Communication

```vue
<!-- Props & Emits -->
<script setup>
// Child component
const props = defineProps({
  title: { type: String, required: true },
  count: { type: Number, default: 0 }
})
const emit = defineEmits(['update', 'delete'])
emit('update', { id: 1 })
</script>
```

```javascript
// Provide / Inject (thay thế prop drilling)
// Parent
provide('theme', ref('dark'))

// Child (bất kỳ cấp nào)
const theme = inject('theme')
```

### 1.5 Directives Quan Trọng

```vue
<template>
  <!-- Conditional -->
  <div v-if="isLoggedIn">Welcome</div>
  <div v-else>Please login</div>
  
  <!-- Loop – luôn thêm :key -->
  <li v-for="item in list" :key="item.id">{{ item.name }}</li>
  
  <!-- Two-way binding -->
  <input v-model="searchQuery" />
  
  <!-- Event -->
  <button @click.prevent="submit">Submit</button>
  
  <!-- Dynamic class/style -->
  <div :class="{ active: isActive, 'text-red': hasError }"></div>
</template>
```

---

## 2. State Management – Vuex & Pinia

### 2.1 Pinia (Khuyên dùng cho Vue 3)

```javascript
// stores/useUserStore.js
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    currentUser: null,
    token: localStorage.getItem('token') || null,
  }),
  
  getters: {
    isLoggedIn: (state) => !!state.token,
    fullName: (state) => `${state.currentUser?.firstName} ${state.currentUser?.lastName}`,
  },
  
  actions: {
    async login(credentials) {
      const res = await api.post('/auth/login', credentials)
      this.token = res.data.token
      this.currentUser = res.data.user
      localStorage.setItem('token', this.token)
    },
    logout() {
      this.token = null
      this.currentUser = null
      localStorage.removeItem('token')
    }
  }
})
```

```vue
<!-- Sử dụng trong component -->
<script setup>
import { useUserStore } from '@/stores/useUserStore'
const userStore = useUserStore()
</script>
<template>
  <span v-if="userStore.isLoggedIn">{{ userStore.fullName }}</span>
</template>
```

### 2.2 Vuex (Vue 2 / Legacy)

```javascript
// store/index.js
export default new Vuex.Store({
  state: { count: 0 },
  mutations: {
    INCREMENT(state) { state.count++ }      // Đồng bộ
  },
  actions: {
    fetchData({ commit }) {                  // Bất đồng bộ
      return api.get('/data').then(res => commit('SET_DATA', res.data))
    }
  },
  getters: {
    doubleCount: state => state.count * 2
  },
  modules: { user, product }               // Tách module
})
```

> **🔑 Quy tắc:** Mutation = đồng bộ | Action = bất đồng bộ

### 2.3 Khi nào dùng Global State?

- Dữ liệu chia sẻ nhiều component không liên quan (user session, cart)
- Không dùng cho state chỉ dùng trong 1 component → dùng `ref` local

---

## 3. Component Patterns & Performance

### 3.1 Composables (Tái sử dụng logic)

```javascript
// composables/useFetch.js
import { ref } from 'vue'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)
  const loading = ref(false)

  const fetch = async () => {
    loading.value = true
    try {
      const res = await api.get(url)
      data.value = res.data
    } catch (e) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  return { data, error, loading, fetch }
}
```

### 3.2 Performance Optimization

```vue
<script setup>
import { computed, shallowRef, defineAsyncComponent } from 'vue'

// Lazy load component
const HeavyChart = defineAsyncComponent(() =>
  import('./HeavyChart.vue')
)

// v-memo – cache template khi deps không đổi
</script>
<template>
  <!-- v-once: render 1 lần duy nhất -->
  <header v-once>{{ appTitle }}</header>

  <!-- v-memo: skip re-render nếu deps không đổi -->
  <div v-memo="[item.id, item.updatedAt]" v-for="item in list" :key="item.id">
    {{ item.title }}
  </div>

  <!-- Lazy load component -->
  <Suspense>
    <HeavyChart />
    <template #fallback>Loading...</template>
  </Suspense>
</template>
```

```javascript
// Tối ưu computed – chỉ chạy lại khi dependency thay đổi
const filteredList = computed(() =>
  products.value.filter(p => p.category === selectedCategory.value)
)

// keepAlive – giữ state khi chuyển tab
// <KeepAlive><component :is="activeTab" /></KeepAlive>
```

### 3.3 Slots

```vue
<!-- BaseCard.vue -->
<template>
  <div class="card">
    <slot name="header" />       <!-- Named slot -->
    <slot />                     <!-- Default slot -->
    <slot name="footer" :data="cardData" />  <!-- Scoped slot -->
  </div>
</template>

<!-- Sử dụng -->
<BaseCard>
  <template #header><h2>Title</h2></template>
  <p>Content</p>
  <template #footer="{ data }">{{ data.label }}</template>
</BaseCard>
```

---

## 4. Nuxt.js – SSR & SEO

### 4.1 Rendering Modes

| Mode        | Mô tả                          | Dùng khi                         |
|-------------|--------------------------------|----------------------------------|
| **SSR**     | Server-side render mỗi request | Blog, e-commerce, SEO critical  |
| **SSG**     | Static generation lúc build    | Trang tĩnh, docs                |
| **CSR**     | Client-side (SPA)              | Dashboard nội bộ                 |
| **ISR**     | Incremental Static Regen       | Nội dung cập nhật thường xuyên   |

```javascript
// nuxt.config.ts
export default defineNuxtConfig({
  ssr: true,               // Bật SSR
  routeRules: {
    '/dashboard/**': { ssr: false },    // CSR cho dashboard
    '/blog/**': { prerender: true },    // SSG cho blog
  }
})
```

### 4.2 Data Fetching trong Nuxt 3

```vue
<script setup>
// useFetch – auto SSR + client hydration
const { data: posts, pending, error } = await useFetch('/api/posts', {
  lazy: false,         // false = await trước khi render
  server: true,        // fetch cả ở server
  transform: (data) => data.items
})

// useAsyncData – khi cần key hoặc custom fetcher
const { data } = await useAsyncData('user', () => $fetch('/api/user'))
</script>
```

### 4.3 SEO với Nuxt

```vue
<script setup>
useHead({
  title: 'Trang chủ – MyApp',
  meta: [
    { name: 'description', content: 'Mô tả trang chủ ngắn gọn, 150-160 ký tự' },
    { property: 'og:title', content: 'Trang chủ' },
    { property: 'og:image', content: '/og-image.png' },
  ],
  link: [{ rel: 'canonical', href: 'https://myapp.com/' }]
})
</script>
```

### 4.4 File-based Routing Nuxt 3

```
pages/
├── index.vue            → /
├── about.vue            → /about
├── blog/
│   ├── index.vue        → /blog
│   └── [slug].vue       → /blog/:slug
└── [...404].vue         → catch-all
```

```vue
<script setup>
const route = useRoute()
const slug = route.params.slug   // /blog/hello → 'hello'
</script>
```

### 4.5 Tối ưu tốc độ tải trang

- **Image optimization:** Dùng `<NuxtImg>` với lazy loading + WebP
- **Code splitting:** Nuxt tự động split theo route
- **Caching:** `Cache-Control` headers, `stale-while-revalidate`
- **Bundle size:** Phân tích với `nuxt build --analyze`

---

## 5. Cắt Giao Diện Từ Figma

### 5.1 Quy trình chuẩn

```
1. Inspect Figma → lấy: font, color, spacing, border-radius
2. Tạo Design Tokens (CSS variables)
3. Chia layout: Container → Section → Component → Element
4. Code HTML cấu trúc trước, CSS sau
5. Test responsive: 320px → 768px → 1024px → 1440px
6. So sánh pixel-perfect với Figma
```

### 5.2 CSS Variables từ Figma

```css
:root {
  /* Colors */
  --color-primary: #3B82F6;
  --color-secondary: #10B981;
  --color-text: #1F2937;
  --color-bg: #F9FAFB;
  
  /* Typography */
  --font-family: 'Inter', sans-serif;
  --text-sm: 14px;
  --text-base: 16px;
  --text-lg: 18px;
  --text-xl: 24px;
  
  /* Spacing */
  --spacing-4: 16px;
  --spacing-8: 32px;
  
  /* Border radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}
```

### 5.3 Responsive Breakpoints

```css
/* Mobile first */
.container { width: 100%; padding: 0 16px; }

@media (min-width: 768px) { /* Tablet */
  .container { max-width: 768px; margin: 0 auto; }
}
@media (min-width: 1024px) { /* Desktop */
  .container { max-width: 1280px; }
}
```

---

## 6. Laravel Framework

### 6.1 Kiến trúc MVC

```
Request → Route → Middleware → Controller → Service/Repository → Model → Response
```

```php
// routes/api.php
Route::middleware(['auth:sanctum'])->group(function () {
    Route::apiResource('products', ProductController::class);
    Route::get('/user', [UserController::class, 'profile']);
});
```

```php
// app/Http/Controllers/ProductController.php
class ProductController extends Controller
{
    public function __construct(private ProductService $productService) {}

    public function index(Request $request)
    {
        $products = $this->productService->getAll($request->validated());
        return ProductResource::collection($products);
    }

    public function store(StoreProductRequest $request)
    {
        $product = $this->productService->create($request->validated());
        return new ProductResource($product);
    }
}
```

### 6.2 Eloquent ORM

```php
// Model relationships
class User extends Model
{
    // One to Many
    public function posts(): HasMany
    {
        return $this->hasMany(Post::class);
    }
    
    // Many to Many
    public function roles(): BelongsToMany
    {
        return $this->belongsToMany(Role::class)->withPivot('assigned_at');
    }
    
    // Scopes
    public function scopeActive($query)
    {
        return $query->where('status', 'active');
    }
}

// Queries
$users = User::with(['posts', 'roles'])   // Eager loading – tránh N+1
    ->active()
    ->where('created_at', '>=', now()->subMonth())
    ->orderBy('name')
    ->paginate(15);
```

> **⚠️ N+1 Problem:** Luôn dùng `with()` để eager load relations

```php
// BAD – N+1
$users = User::all();
foreach ($users as $user) {
    echo $user->posts->count(); // Query cho mỗi user!
}

// GOOD – Eager loading
$users = User::with('posts')->get(); // 2 queries tổng cộng
```

### 6.3 Middleware

```php
// Tạo middleware
php artisan make:middleware CheckPermission

// app/Http/Middleware/CheckPermission.php
class CheckPermission
{
    public function handle(Request $request, Closure $next, string $permission)
    {
        if (!auth()->user()->hasPermission($permission)) {
            return response()->json(['message' => 'Forbidden'], 403);
        }
        return $next($request);
    }
}

// Đăng ký và dùng
Route::middleware(['auth', 'permission:edit-posts'])->group(...);
```

### 6.4 Service Container & Dependency Injection

```php
// Service Provider binding
public function register(): void
{
    $this->app->singleton(PaymentGateway::class, function ($app) {
        return new StripePaymentGateway(config('services.stripe.key'));
    });
    
    // Interface binding
    $this->app->bind(UserRepositoryInterface::class, UserRepository::class);
}

// Auto-inject qua constructor
class OrderController extends Controller
{
    public function __construct(
        private UserRepositoryInterface $userRepo,
        private PaymentGateway $payment
    ) {}
}
```

### 6.5 Migrations

```php
// Tạo migration
php artisan make:migration create_orders_table

// database/migrations/xxxx_create_orders_table.php
public function up(): void
{
    Schema::create('orders', function (Blueprint $table) {
        $table->id();
        $table->foreignId('user_id')->constrained()->cascadeOnDelete();
        $table->decimal('total', 10, 2);
        $table->enum('status', ['pending', 'paid', 'cancelled'])->default('pending');
        $table->json('metadata')->nullable();
        $table->timestamps();
        $table->softDeletes();           // deleted_at
        
        $table->index(['user_id', 'status']);  // Composite index
    });
}

public function down(): void
{
    Schema::dropIfExists('orders');
}
```

### 6.6 Queue, Job, Event

```php
// Tạo Job
php artisan make:job SendWelcomeEmail

// app/Jobs/SendWelcomeEmail.php
class SendWelcomeEmail implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;
    
    public int $tries = 3;          // Retry 3 lần nếu thất bại
    public int $timeout = 60;

    public function __construct(private User $user) {}

    public function handle(): void
    {
        Mail::to($this->user->email)->send(new WelcomeMail($this->user));
    }
    
    public function failed(\Throwable $e): void
    {
        Log::error('SendWelcomeEmail failed', ['user' => $this->user->id]);
    }
}

// Dispatch job
SendWelcomeEmail::dispatch($user);                   // Ngay lập tức vào queue
SendWelcomeEmail::dispatch($user)->delay(now()->addMinutes(5));  // Delay
```

```php
// Events & Listeners
php artisan make:event UserRegistered
php artisan make:listener SendWelcomeNotification --event=UserRegistered

// Trigger event
event(new UserRegistered($user));

// Listener
class SendWelcomeNotification
{
    public function handle(UserRegistered $event): void
    {
        SendWelcomeEmail::dispatch($event->user);
    }
}
```

---

## 7. RESTful API & Bảo Mật

### 7.1 RESTful API Principles

| Method    | Endpoint             | Mô tả             |
|-----------|----------------------|-------------------|
| GET       | `/api/products`      | Lấy danh sách     |
| GET       | `/api/products/{id}` | Lấy chi tiết      |
| POST      | `/api/products`      | Tạo mới           |
| PUT       | `/api/products/{id}` | Cập nhật toàn bộ  |
| PATCH     | `/api/products/{id}` | Cập nhật một phần |
| DELETE    | `/api/products/{id}` | Xoá               |

```php
// HTTP Status Codes quan trọng
200 OK        – Thành công
201 Created   – Tạo mới thành công
400 Bad Request – Dữ liệu không hợp lệ
401 Unauthorized – Chưa xác thực
403 Forbidden    – Không có quyền
404 Not Found    – Không tìm thấy
422 Unprocessable – Validation failed
429 Too Many Requests – Rate limit
500 Server Error  – Lỗi server
```

### 7.2 JWT Authentication

```
Luồng JWT:
1. User login → Server tạo JWT (header.payload.signature)
2. Client lưu token (localStorage / httpOnly cookie)
3. Client gửi: Authorization: Bearer <token>
4. Server verify signature → xác thực user
5. Token hết hạn → dùng refresh token để lấy token mới
```

```php
// Laravel với JWT (tymon/jwt-auth)
Route::post('/login', function (Request $request) {
    $credentials = $request->only('email', 'password');
    
    if (!$token = auth('api')->attempt($credentials)) {
        return response()->json(['error' => 'Unauthorized'], 401);
    }
    
    return response()->json([
        'access_token' => $token,
        'token_type' => 'bearer',
        'expires_in' => auth('api')->factory()->getTTL() * 60,
    ]);
});
```

```javascript
// Vue.js – Axios interceptor gắn token
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

// Xử lý 401 – tự động logout
axios.interceptors.response.use(
  res => res,
  err => {
    if (err.response?.status === 401) {
      userStore.logout()
      router.push('/login')
    }
    return Promise.reject(err)
  }
)
```

### 7.3 OAuth2 (Khái niệm)

```
Flows phổ biến:
1. Authorization Code (Web apps) – an toàn nhất
2. Client Credentials (Server-to-server) – không có user
3. PKCE (Mobile/SPA) – thay thế Implicit Flow

Entities:
- Resource Owner: User
- Client: App của bạn
- Authorization Server: Google, Facebook, Keycloak...
- Resource Server: API backend của bạn
```

### 7.4 API Security Best Practices

```php
// 1. Validation input
$request->validate([
    'email' => 'required|email|max:255',
    'amount' => 'required|numeric|min:0|max:999999',
]);

// 2. Rate Limiting
Route::middleware('throttle:60,1')->group(...); // 60 req/phút

// 3. CORS config (config/cors.php)
'allowed_origins' => ['https://yourfrontend.com'],
'allowed_methods' => ['GET', 'POST', 'PUT', 'DELETE'],

// 4. Luôn dùng HTTPS
// 5. Không lộ stack trace trong production
// 6. Dùng API Resource để kiểm soát data trả về
```

```php
// API Resource – kiểm soát output
class UserResource extends JsonResource
{
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            // Không trả về: password, secret_key, ...
        ];
    }
}
```

---

## 8. Câu Hỏi Phỏng Vấn Thường Gặp

### 🟦 Vue.js

**Q: Sự khác biệt giữa `v-show` và `v-if`?**
> `v-if` tạo/xoá DOM element. `v-show` toggle `display: none`. Dùng `v-show` khi component toggle thường xuyên, dùng `v-if` khi ít thay đổi.

**Q: `ref` vs `reactive` khi nào dùng cái nào?**
> `ref` cho primitive (string, number, boolean) và cần `.value`. `reactive` cho object phức tạp, không cần `.value` nhưng bị mất reactivity khi destructure → dùng `toRefs()`.

**Q: Giải thích Virtual DOM là gì?**
> Vue dùng Virtual DOM (JS object đại diện DOM thật). Khi state thay đổi, Vue so sánh Virtual DOM cũ và mới (diffing) → chỉ update phần thực sự thay đổi → hiệu năng tốt hơn.

**Q: Làm sao tránh prop drilling?**
> Dùng `provide/inject` cho component tree, hoặc Pinia store cho global state.

**Q: Composable khác Mixin ở chỗ nào?**
> Mixin dễ gây xung đột tên, không rõ nguồn gốc của property. Composable dùng function rõ ràng hơn, TypeScript-friendly, không xung đột namespace.

---

### 🟧 Nuxt.js

**Q: Nuxt.js giải quyết vấn đề gì mà Vue thuần không có?**
> SSR (Server-Side Rendering) cho SEO, file-based routing tự động, auto-import components/composables, image optimization, và nhiều module tích sẵn.

**Q: `useFetch` vs `$fetch` vs `useAsyncData` khác nhau thế nào?**
> `useFetch` = wrapper của `useAsyncData` + `$fetch`, tự động cache theo URL. `useAsyncData` cho phép custom key và fetcher phức tạp. `$fetch` là raw HTTP client (clone của ofetch), dùng trong actions/events.

---

### 🟥 Laravel

**Q: Giải thích Service Container là gì?**
> IoC Container của Laravel quản lý class dependencies và thực hiện Dependency Injection. Khi bạn type-hint interface trong constructor, Laravel tự resolve implementation đã bind.

**Q: N+1 query problem là gì? Giải quyết thế nào?**
> Khi loop qua collection và gọi relation cho từng item → N+1 query. Giải quyết bằng eager loading: `User::with('posts')->get()` hoặc dùng `->load('posts')` sau khi query.

**Q: Queue vs Job vs Event khác nhau thế nào?**
> **Job** = class thực hiện task cụ thể. **Queue** = hàng đợi chạy jobs bất đồng bộ. **Event** = thông báo "điều gì đó đã xảy ra", Listener lắng nghe và phản ứng (có thể dispatch Job).

**Q: Middleware dùng để làm gì?**
> Xử lý request trước/sau khi vào Controller: auth check, logging, CORS, rate limit, format response...

**Q: Migration rollback có ảnh hưởng gì không?**
> `php artisan migrate:rollback` chạy hàm `down()` → xóa table/column. Trong production cần cẩn thận, nên backup trước.

---

### 🔐 API & Security

**Q: JWT khác Session Authentication thế nào?**
> **Session:** server lưu state (stateful), dùng cookie session ID. **JWT:** stateless, server không lưu gì, verify bằng signature → phù hợp microservices, mobile apps.

**Q: Refresh token dùng để làm gì?**
> Access token có TTL ngắn (15-60 phút) để bảo mật. Refresh token TTL dài hơn → dùng để lấy access token mới mà không cần đăng nhập lại.

**Q: CORS là gì? Sao phải cấu hình?**
> Cross-Origin Resource Sharing – browser block request từ origin khác vì security. Backend phải set header `Access-Control-Allow-Origin` để cho phép frontend domain gọi API.

---

## 🎯 Checklist Trước Phỏng Vấn

### Vue.js
- [ ] Thực hành Composition API với `<script setup>`
- [ ] Xây dựng 1 Composable (ví dụ: `usePagination`)
- [ ] Demo State Management với Pinia
- [ ] Tối ưu một list lớn với `v-memo` hoặc virtual scroll

### Nuxt.js
- [ ] Setup dự án Nuxt 3 với SSR
- [ ] Cấu hình SEO meta tags
- [ ] Dùng `useFetch` + error handling

### Laravel
- [ ] Xây dựng CRUD API hoàn chỉnh với Resource + FormRequest
- [ ] Implement JWT auth flow
- [ ] Tạo Job gửi email qua Queue
- [ ] Viết migration có index và foreign key

### Bài tập thực hành
- [ ] Clone giao diện từ Figma (pixel-perfect + responsive)
- [ ] Fullstack mini project: Todo App với Vue 3 + Laravel API + JWT
- [ ] Deploy lên server hoặc Vercel/Railway

---

> 📝 **Tài liệu tham khảo:**
> - [Vue 3 Docs](https://vuejs.org/guide/)
> - [Nuxt 3 Docs](https://nuxt.com/docs)
> - [Pinia Docs](https://pinia.vuejs.org/)
> - [Laravel Docs](https://laravel.com/docs)
> - [JWT.io](https://jwt.io/)
