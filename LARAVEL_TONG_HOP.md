# 🔴 LARAVEL – LÝ THUYẾT TRỌNG TÂM PHỎNG VẤN

> **Covers:** MVC · Eloquent ORM · Middleware · Service Container · Migration · Queue · Job · Event

---

## 1. 🏗️ KIẾN TRÚC MVC & REQUEST LIFECYCLE

### 1.1 MVC là gì?

**MVC (Model – View – Controller)** là design pattern chia ứng dụng thành 3 tầng độc lập:

| Tầng | Vai trò | Trong Laravel |
|---|---|---|
| **Model** | Đại diện dữ liệu, tương tác DB | Eloquent Model (`app/Models/`) |
| **View** | Giao diện hiển thị cho user | Blade template (`resources/views/`) |
| **Controller** | Nhận request, điều phối M & V | `app/Http/Controllers/` |

> **Nguyên tắc**: Controller **gầy** (thin) – không chứa business logic. Logic nằm trong **Service class**, truy vấn CSDL nằm trong **Repository/Model**.

---

### 1.2 Request Lifecycle (Luồng xử lý request)

Đây là câu hỏi phỏng vấn rất phổ biến. Mỗi request Laravel đi qua các bước:

```
1. public/index.php       ← Entry point duy nhất (front controller)
2. bootstrap/app.php      ← Tạo Application instance, bind Kernel
3. HTTP Kernel            ← Quản lý middleware pipeline
4. Global Middleware      ← Chạy với MỌI request (CORS, Session, TrustProxies...)
5. Route Matching         ← Khớp URL với route đã định nghĩa
6. Route Middleware        ← Chạy với route cụ thể (auth, throttle...)
7. Controller@method      ← Xử lý logic chính
8. Response               ← Trả về client (JSON, HTML, redirect...)
```

**Tại sao chỉ có 1 entry point?**
→ Tập trung xử lý bootstrap, bảo mật, áp dụng middleware toàn cục một cách nhất quán.

---

### 1.3 Service Provider – "Trái tim khởi động" Laravel

`ServiceProvider` là nơi **đăng ký** mọi thứ vào container (binding, observer, event, route...).

- **`register()`**: Chỉ bind vào container. Chưa được dùng services khác (app chưa fully booted).
- **`boot()`**: Tất cả providers đã register xong → dùng được mọi service. Đăng ký Observer, Gate, Macro, Blade directive tại đây.

Các Provider quan trọng mặc định: `RouteServiceProvider`, `AuthServiceProvider`, `EventServiceProvider`, `AppServiceProvider`.

---

## 2. 🗄️ ELOQUENT ORM

### 2.1 Eloquent là gì?

**Eloquent ORM** (Object-Relational Mapping) là Active Record implementation của Laravel. Mỗi **Model** ánh xạ tới 1 bảng trong database. Mỗi **instance** ánh xạ tới 1 row.

> Active Record pattern: Model tự chứa logic truy vấn của chính nó (`Product::find(1)`, `$product->save()`).

---

### 2.2 Các khái niệm cốt lõi

#### `$fillable` vs `$guarded`
- **`$fillable`**: Whitelist – chỉ những field này được mass assignment (`create()`, `update()`).
- **`$guarded`**: Blacklist – những field này KHÔNG được mass assignment.
- **Best practice**: Luôn dùng `$fillable` để tránh lỗ hổng **Mass Assignment** (attacker truyền field `is_admin=1`).

#### `$casts` – Type casting
Tự động chuyển đổi kiểu dữ liệu khi đọc/ghi:
- `'is_active' => 'boolean'`: DB lưu `0/1`, PHP đọc ra `true/false`
- `'metadata' => 'array'`: DB lưu JSON string, PHP đọc ra array
- `'price' => 'decimal:2'`: Làm tròn số thực
- `'published_at' => 'datetime'`: String → Carbon instance

#### Accessor & Mutator (Laravel 9+ dùng `Attribute::make`)
- **Accessor**: Transform data **khi đọc** (`$product->price` → chia 100 để ra đơn vị đồng)
- **Mutator**: Transform data **khi ghi** (`$product->name = 'abc'` → tự ucwords)

#### Scope – Tái sử dụng query conditions
- **Local Scope**: Method trên model, gọi theo chain (`Product::active()->priceRange(100, 500)->get()`)
- **Global Scope**: Tự động áp dụng cho **mọi query** trên model đó (ví dụ: SoftDeletes tự thêm `WHERE deleted_at IS NULL`)

---

### 2.3 Relationships – Quan hệ giữa các bảng

| Relationship | Ý nghĩa | Foreign Key ở đâu |
|---|---|---|
| `hasOne` | User có 1 Profile | Bảng `profiles` (profiles.user_id) |
| `belongsTo` | Profile thuộc về 1 User | Bảng **hiện tại** (profiles.user_id) |
| `hasMany` | User có nhiều Post | Bảng `posts` (posts.user_id) |
| `belongsToMany` | Post có nhiều Tag và ngược lại | Bảng pivot `post_tag` |
| `hasManyThrough` | Country có nhiều Post **qua** User | Qua bảng trung gian |
| `morphMany` | Comment thuộc về Post **hoặc** Video | Polymorphic (commentable_type, commentable_id) |

> ⚡ **Hay nhầm**: `hasOne` và `belongsTo` đều lấy 1 record, nhưng **FK nằm ở bảng khác nhau**.

---

### 2.4 N+1 Problem – Vấn đề hiệu năng quan trọng nhất

**N+1 là gì?**
Khi lấy 1 danh sách rồi duyệt từng item để lấy relation → gây ra 1 + N queries.

```php
// ❌ N+1: 1 query lấy products + N query cho mỗi category
$products = Product::all();
foreach ($products as $p) {
    echo $p->category->name;  // Mỗi lần gọi là 1 query riêng!
}

// ✅ Eager Loading: chỉ 2 queries tổng
$products = Product::with('category')->get();
```

**Cách phát hiện**: Dùng **Laravel Debugbar** hoặc `DB::listen()` để đếm số query.

---

### 2.5 SoftDeletes

Thay vì xóa thật, ghi `deleted_at = NOW()`. Query mặc định tự thêm `WHERE deleted_at IS NULL`.

- `withTrashed()`: Lấy cả record đã soft delete
- `onlyTrashed()`: Chỉ lấy record đã soft delete
- `restore()`: Khôi phục record
- `forceDelete()`: Xóa thật khỏi DB

---

## 3. 🔧 MIDDLEWARE

### 3.1 Middleware là gì?

**Middleware** là lớp lọc (*filter*) nằm giữa HTTP Request và Controller. Hoạt động theo mô hình **Pipeline (Onion)**.

```
Nhận Request → [MW-A trước] → [MW-B trước] → Controller
                                                   ↓
Trả Response ← [MW-A sau]  ← [MW-B sau]  ← Response
```

Mỗi middleware gọi `$next($request)` để chuyển request sang tầng tiếp theo. Nếu không gọi → request bị **chặn** tại đây (trả về response sớm).

---

### 3.2 Phân loại Middleware

| Loại | Đặc điểm | Ví dụ |
|---|---|---|
| **Global Middleware** | Chạy với MỌI request | `TrimStrings`, `HandleCors`, `TrustProxies` |
| **Route Middleware** | Chỉ khi được gán vào route | `auth`, `throttle`, `verified` |
| **Middleware Group** | Nhóm nhiều middleware | `web` (session, csrf), `api` (throttle) |

---

### 3.3 Before vs After Middleware

- **Before**: Xử lý **trước** khi request đến controller (kiểm tra auth, log request, modify headers)
- **After**: Xử lý **sau** khi controller trả về response (log response, add headers, compress)

Middleware vừa before vừa after thì code trước `$next()` là before, sau `$next()` là after.

---

### 3.4 Middleware có tham số

```php
// Khai báo
'role:admin'   // tham số $role = 'admin'
'throttle:60,1' // tham số $maxAttempts = 60, $decayMinutes = 1
```

---

## 4. 💉 SERVICE CONTAINER & DEPENDENCY INJECTION

### 4.1 Service Container là gì?

**Service Container** (còn gọi là IoC Container – Inversion of Control) là một **hộp đựng dependencies** biết cách tạo và inject objects tự động.

> **Ý tưởng cốt lõi**: Thay vì class tự `new` dependency của mình, Container sẽ tạo và "tiêm" (inject) vào.

**Lợi ích**:
- Code **loosely coupled** (không phụ thuộc cụ thể vào implementation)
- Dễ **thay thế implementation** (chỉ rebind trong ServiceProvider)
- Dễ **test** (inject mock/fake thay implementation thật)

---

### 4.2 Binding – Đăng ký vào Container

| Method | Ý nghĩa | Khi nào dùng |
|---|---|---|
| `bind()` | Tạo **instance mới** mỗi lần resolve | Mỗi request cần object riêng |
| `singleton()` | Tạo **1 lần**, dùng lại mãi | DB connection, Config, Cache |
| `scoped()` | 1 instance **per HTTP request** | Per-request state, session |
| `instance()` | Bind **object đã tạo sẵn** | Inject object thủ công |

---

### 4.3 Auto Dependency Injection

Laravel tự động đọc **type-hint** trong constructor/method và resolve từ Container.

```php
// Laravel tự tạo PaymentService và OrderRepository, inject vào
class OrderController extends Controller
{
    public function __construct(
        private PaymentService $payment,    // ← Auto inject
        private OrderRepository $orders,   // ← Auto inject
    ) {}
}
```

> Đây là lý do tại sao Controller có thể nhận bất kỳ class nào trong constructor mà không cần `new`.

---

### 4.4 Binding Interface → Implementation

Pattern quan trọng nhất trong DI:

```php
// AppServiceProvider::register()
$this->app->bind(
    PaymentGatewayInterface::class,  // Depend on abstraction
    StripePaymentGateway::class      // Concrete implementation
);

// Muốn đổi sang VNPay? Chỉ đổi 1 dòng ở đây!
// $this->app->bind(PaymentGatewayInterface::class, VNPayGateway::class);
```

Controller vẫn type-hint `PaymentGatewayInterface`, không biết đang dùng Stripe hay VNPay → **Open/Closed principle**.

---

## 5. 📋 MIGRATION

### 5.1 Migration là gì?

**Migration** là version control cho database schema. Thay vì viết SQL thuần, dùng PHP code để định nghĩa schema → có thể **track bằng git**, **rollback**, **rollforward** nhất quán trên mọi môi trường.

---

### 5.2 Quy tắc Migration

| Quy tắc | Giải thích |
|---|---|
| Mỗi migration làm **1 việc** | Dễ rollback, dễ debug |
| Luôn viết `down()` | Cần thiết khi rollback |
| **Không sửa migration đã chạy production** | Gây mất đồng bộ. Tạo migration mới thay thế |
| Đặt tên rõ ràng | `add_sku_to_products_table`, `create_orders_table` |
| Thêm index đúng chỗ | Fields dùng trong `WHERE`, `JOIN`, FK columns |

---

### 5.3 Cơ chế hoạt động

Laravel lưu file migration đã chạy trong bảng **`migrations`** (tên file + batch number). Khi `migrate`, chỉ chạy file chưa có trong bảng này. `rollback` xóa batch cuối và chạy `down()`.

---

### 5.4 Index – Khi nào cần?

- **`index()`**: Tăng tốc `WHERE`, `ORDER BY` trên column đó
- **`unique()`**: Unique index (vừa unique constraint vừa index)
- **`foreignId()->constrained()`**: FK index tự động
- **Composite index**: `$table->index(['category_id', 'is_active'])` → tối ưu cho query `WHERE category_id = ? AND is_active = 1`

> ⚠️ Index tốn thêm storage và làm **chậm INSERT/UPDATE** – chỉ đặt ở cột thực sự hay query.

---

### 5.5 Factory & Seeder

- **Factory**: Tạo fake data có cấu trúc giống thật để test (dùng `Faker`)
- **Seeder**: Script chạy Factory hoặc insert data cố định vào DB
- `RefreshDatabase` trong test: Migrate lại + seed trước mỗi test

---

## 6. 📬 QUEUE & JOB

### 6.1 Queue là gì? Tại sao cần?

**Queue** (hàng đợi) cho phép **trì hoãn** các tác vụ nặng/chậm ra background, không làm block HTTP response.

**Ví dụ thực tế**:
- Gửi email xác nhận đơn hàng (không cần chờ ngay)
- Resize ảnh sau khi upload
- Đồng bộ dữ liệu sang hệ thống bên thứ 3
- Push notification

> Không có queue: User phải **chờ** server gửi email xong mới nhận response → UX kém.
> Có queue: Server nhận request → đẩy job vào queue → trả response ngay → worker xử lý sau.

---

### 6.2 Queue Architecture

```
HTTP Request
    ↓
Dispatch Job ──────────────────→ Queue Driver (Redis/DB/SQS)
    ↓                                        ↓
HTTP Response ← (trả ngay)        Queue Worker (process background)
                                             ↓
                                       Execute Job logic
```

---

### 6.3 Queue Driver

| Driver | Đặc điểm | Dùng khi |
|---|---|---|
| `sync` | Chạy **đồng bộ ngay** (không queue thật) | Local development, testing |
| `database` | Lưu job vào bảng `jobs` trong DB | App nhỏ, không có Redis |
| `redis` | Hiệu năng cao, hỗ trợ Horizon | **Production chuẩn** |
| `sqs` | AWS managed queue, auto-scale | AWS infrastructure |
| `beanstalkd` | Lightweight queue server | Ít dùng |

---

### 6.4 Job Class – Đơn vị công việc

**Job** là class đại diện cho 1 tác vụ cụ thể cần xử lý.

Các property quan trọng:
- **`$tries`**: Số lần retry khi job fail (default: 1)
- **`$timeout`**: Thời gian tối đa được chạy (giây) trước khi bị kill
- **`$backoff`**: Số giây chờ giữa các lần retry
- **`$queue`**: Tên queue mà job sẽ đẩy vào

**`failed(Throwable $e)`**: Method được gọi khi job thất bại hết số retry → cleanup, notify.

---

### 6.5 Các cách Dispatch Job

| Cách | Ý nghĩa |
|---|---|
| `dispatch($job)` | Push vào queue, chạy async |
| `dispatchSync($job)` | Chạy ngay trong request (bỏ qua queue) |
| `dispatch($job)->delay(now()->addMinutes(10))` | Delay 10 phút mới chạy |
| `dispatch($job)->onQueue('emails')` | Đẩy vào queue tên 'emails' |
| `dispatch($job)->afterCommit()` | Chỉ dispatch sau khi DB transaction commit |
| `Bus::chain([...])` | Chain nhiều job theo thứ tự tuần tự |
| `Bus::batch([...])` | Chạy song song, có callback khi tất cả xong |

---

### 6.6 Queue Worker

Worker là process chạy ngầm, liên tục poll queue và execute job:

```bash
php artisan queue:work redis --queue=high,default,emails
```

- `queue:work`: Chạy daemon, cache code (cần `queue:restart` khi deploy)
- `queue:listen`: Reload mỗi job (dùng khi dev, chậm hơn)
- **Laravel Horizon**: Dashboard monitor Redis queues (throughput, failed jobs, workers)

---

### 6.7 Race Condition trong Queue

Khi nhiều worker chạy cùng lúc có thể xử lý cùng 1 job (race condition).

**Fix bằng Atomic Lock**:
```php
Cache::lock("process-order-{$orderId}", 10)->block(5, function() {
    // Chỉ 1 worker chạy đoạn này tại 1 thời điểm
});
```

**Fix bằng Middleware `WithoutOverlapping`**:
```php
public function middleware(): array
{
    return [new WithoutOverlapping($this->order->id)];
}
```

---

## 7. 📣 EVENT & LISTENER

### 7.1 Event System là gì?

**Event** (sự kiện): Thông báo rằng "điều gì đó vừa xảy ra" trong hệ thống.
**Listener**: Component lắng nghe và phản ứng với event đó.

Đây là hiện thực của **Observer pattern** → giúp decoupling giữa các phần của hệ thống.

---

### 7.2 Tại sao dùng Event thay vì gọi trực tiếp?

**Không dùng Event (tight coupling)**:
```
OrderService::checkout()
    → gọi EmailService::send()
    → gọi InventoryService::update()
    → gọi NotificationService::push()
    → gọi AnalyticsService::track()
```
Thêm 1 tính năng mới → phải sửa `OrderService`.

**Dùng Event (loose coupling)**:
```
OrderService::checkout()
    → fire event OrderPlaced

EmailService    → lắng nghe OrderPlaced
InventoryService → lắng nghe OrderPlaced
NotificationService → lắng nghe OrderPlaced
```
Thêm tính năng mới chỉ cần thêm **Listener mới**, không đụng `OrderService`.

---

### 7.3 Luồng hoạt động

```
1. Định nghĩa Event class (data container)
2. Định nghĩa Listener class (xử lý logic)
3. Đăng ký trong EventServiceProvider ($listen array)
4. Fire event: event(new OrderPlaced($order))
5. Laravel tự gọi tất cả Listener đã đăng ký
```

---

### 7.4 Queued Listener

Listener implement `ShouldQueue` → tự động push vào queue thay vì chạy sync.

**Khi nào queue listener?** Khi logic trong listener chậm (gửi email, call API bên ngoài).
**Khi nào sync?** Khi cần đảm bảo xảy ra ngay (update inventory trước khi response).

---

### 7.5 Event vs Observer – Khi nào dùng cái nào?

| | **Observer** | **Event/Listener** |
|---|---|---|
| **Hook vào** | Eloquent model lifecycle | Domain/business events |
| **Trigger bởi** | `creating`, `created`, `updated`, `deleted`... | `event(new OrderPlaced(...))` thủ công |
| **Coupling** | Gắn với Model cụ thể | Decoupled hoàn toàn |
| **Dùng khi** | Xử lý data lifecycle (auto slug, cache invalidate) | Business events phức tạp, nhiều listener |

---

### 7.6 Model Events & Observer

Eloquent tự động fire các event trong lifecycle: `creating → created → updating → updated → saving → saved → deleting → deleted → restoring → restored`

**Observer** là class tập trung xử lý tất cả lifecycle events của 1 Model:

```
ProductObserver::creating()  ← trước khi INSERT
ProductObserver::created()   ← sau khi INSERT thành công
ProductObserver::updating()  ← trước khi UPDATE
ProductObserver::deleting()  ← trước khi DELETE
```

---

## 8. ❓ Q&A PHỎNG VẤN TRỌNG TÂM

### MVC & Lifecycle

**Q: Request đi qua những bước nào trong Laravel?**
> `index.php` → Bootstrap App → HTTP Kernel → Global Middleware → Route Matching → Route Middleware → Controller → Response.

**Q: `register()` vs `boot()` trong ServiceProvider?**
> `register()`: chỉ bind vào container, chưa được dùng service khác. `boot()`: tất cả providers đã ready → đăng ký Observer, Gate, Event, Macro tại đây.

---

### Eloquent

**Q: N+1 problem là gì?**
> 1 query lấy list + N query cho mỗi item khi access relation. Fix bằng eager loading `with(['relation'])`.

**Q: `HasOne` vs `BelongsTo` khác nhau thế nào?**
> Cả hai đều là quan hệ 1-1, nhưng **foreign key nằm khác bảng**: `hasOne` → FK ở bảng kia. `belongsTo` → FK ở bảng **hiện tại**.

**Q: SoftDeletes là gì và hoạt động thế nào?**
> Không xóa thật, chỉ set `deleted_at`. Query tự thêm `WHERE deleted_at IS NULL`. Dùng `withTrashed()`, `restore()`, `forceDelete()`.

**Q: `$fillable` và `$guarded` để làm gì?**
> Bảo vệ khỏi **Mass Assignment vulnerability**. `$fillable` = whitelist field được phép gán hàng loạt. `$guarded` = blacklist field bị cấm.

---

### Middleware

**Q: Middleware pipeline hoạt động thế nào?**
> Mô hình **Onion**: request đi vào từng lớp middleware (trước), đến controller, response đi ngược ra (sau). Mỗi middleware gọi `$next($request)` để chuyển tiếp hoặc return sớm để chặn.

**Q: Sự khác biệt Global Middleware và Route Middleware?**
> Global: chạy với **mọi** request (`TrimStrings`, CORS). Route: chỉ khi được gán vào route/controller (`auth`, `throttle`, `role`).

---

### Service Container

**Q: Service Container là gì?**
> IoC container tự động tạo và inject dependencies. Bind interface → implementation, Laravel tự resolve khi type-hint trong constructor.

**Q: `bind` vs `singleton` vs `scoped`?**
> `bind`: instance mới mỗi lần resolve. `singleton`: 1 instance suốt vòng đời app. `scoped`: 1 instance per HTTP request.

**Q: Tại sao nên bind Interface thay vì Class cụ thể?**
> Loose coupling – dễ swap implementation (Stripe ↔ VNPay), dễ mock khi test, tuân theo Dependency Inversion Principle.

---

### Queue & Job

**Q: Queue giải quyết vấn đề gì?**
> Xử lý tác vụ nặng (email, resize ảnh, API call) ở background → không block HTTP response → UX tốt hơn, server không bị timeout.

**Q: `dispatch()` vs `dispatchSync()`?**
> `dispatch()`: async, đẩy vào queue. `dispatchSync()`: chạy ngay trong request, bỏ qua queue (dùng test, debug).

**Q: Queue driver nào nên dùng production?**
> **Redis + Laravel Horizon**: hiệu năng cao, có dashboard monitor. `database` cho app nhỏ không cần Redis.

**Q: Job thất bại thì xảy ra gì?**
> Retry theo `$tries` lần với `$backoff` giây giữa các lần. Hết retry → gọi `failed()` và lưu vào bảng `failed_jobs`. Dùng `queue:retry` để retry thủ công.

---

### Event & Listener

**Q: Event/Listener vs Observer – dùng khi nào?**
> **Observer**: data lifecycle của Model (auto-slug, cache clear). **Event/Listener**: business events, 1 event nhiều listener, listener có thể queue riêng.

**Q: Vì sao dùng Event thay vì gọi thẳng Service?**
> **Loose coupling**: thêm listener mới không đụng code cũ. **Single Responsibility**: mỗi listener làm 1 việc. **Dễ queue**: Listener `ShouldQueue` → async tự động.

**Q: Queued Listener khác Queued Job thế nào?**
> Về bản chất tương tự – cả hai đều implement `ShouldQueue`. Listener được trigger bởi event, Job được dispatch thủ công. Listener phù hợp khi gắn với 1 domain event cụ thể.

---

## 9. 📊 CHEAT SHEET NHANH

### Artisan Commands

```bash
# Code generation
php artisan make:model Product -mcr        # Model + Migration + Controller (resource)
php artisan make:job SendOrderEmail
php artisan make:event OrderPlaced
php artisan make:listener HandleOrder --event=OrderPlaced
php artisan make:middleware CheckRole
php artisan make:request StoreProductRequest
php artisan make:resource ProductResource
php artisan make:observer ProductObserver --model=Product
php artisan make:policy ProductPolicy --model=Product

# Database
php artisan migrate
php artisan migrate:fresh --seed           # Drop all + re-migrate + seed
php artisan migrate:rollback --step=2
php artisan migrate:status
php artisan db:seed --class=ProductSeeder

# Queue
php artisan queue:work redis --queue=high,default
php artisan queue:failed                   # Xem failed jobs
php artisan queue:retry all                # Retry tất cả
php artisan queue:flush                    # Xóa failed jobs
php artisan horizon                        # Dashboard Redis queue
```

### So sánh nhanh

| Khái niệm | Before | After |
|---|---|---|
| Mass Assignment | `create($request->all())` ❌ | `create($request->validated())` ✅ |
| N+1 | `Product::all()` rồi duyệt | `Product::with('category')->get()` ✅ |
| Async task | Xử lý trong request ❌ | `dispatch(new Job(...))` ✅ |
| Fat Controller | Logic trong Controller ❌ | Service + Repository + FormRequest ✅ |
| Hard coupling | `$this->payment = new Stripe()` ❌ | Inject `PaymentInterface` ✅ |
