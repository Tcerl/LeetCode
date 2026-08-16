## PHẦN 1: PYTHON & BACKEND (40 câu)

### 🔹 Câu hỏi cơ bản Python

**Q1. GIL (Global Interpreter Lock) trong Python là gì?**
> GIL là mutex lock ngăn nhiều threads Python chạy bytecode cùng lúc trong cùng process.
> - **Hệ quả**: Threading không giúp tăng tốc CPU-bound tasks
> - **Giải pháp**: Dùng `multiprocessing` cho CPU-bound, `asyncio`/`threading` cho I/O-bound
> - **Khi bỏ qua GIL**: NumPy operations, C extensions

---

**Q2. Giải thích `@staticmethod` vs `@classmethod` vs `@property`**
> - `@staticmethod`: Không nhận `self` hay `cls`, utility function thuần túy
> - `@classmethod`: Nhận `cls` (class reference), dùng làm factory methods
> - `@property`: Biến method thành attribute, có getter/setter/deleter
> - **Ví dụ thực tế**: `Temperature.from_fahrenheit(98.6)` dùng `@classmethod`

---

**Q3. Generator vs List comprehension - khi nào dùng cái nào?**
> - **List**: Cần random access, dùng nhiều lần, dataset nhỏ/vừa
> - **Generator**: Dataset lớn (file GB), streaming, một lần duyệt, pipeline transforms
> - **Ví dụ**: Trong eCommerce migration, đọc từng batch sản phẩm = generator

---

**Q4. Decorator là gì? Viết 1 decorator logging từ đầu.**
```python
import functools, logging

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper
```

---

**Q5. `__init__` vs `__new__` khác nhau như thế nào?**
> - `__new__`: Tạo object mới (allocate memory) - ít dùng
> - `__init__`: Khởi tạo object đã tạo (initialize attributes)
> - Dùng `__new__` khi: Singleton pattern, immutable types (int, str)

---

**Q6. Python memory management hoạt động thế nào?**
> - **Reference counting**: Mỗi object có counter, = 0 thì free
> - **Garbage collector**: Xử lý circular references mà ref counting không bắt được
> - **Memory pools**: CPython reuse memory blocks cho objects nhỏ
> - **Integer caching**: -5 đến 256 được cache sẵn

---

**Q7. `*args` và `**kwargs` - khi nào dùng?**
> - `*args`: Số lượng positional arguments không xác định → tuple
> - `**kwargs`: Số lượng keyword arguments không xác định → dict
> - Dùng trong: Decorators, wrapper functions, Django CBVs

---

**Q8. Giải thích `with` statement và context manager**
> `with` gọi `__enter__` khi vào block và `__exit__` khi ra (kể cả exception).
> Đảm bảo cleanup luôn xảy ra.
> Ví dụ: File I/O, DB connections, thread locks, timing code

---

**Q9. Shallow copy vs Deep copy - sự khác biệt?**
> - **Shallow**: Copy container, các elements vẫn trỏ cùng objects
> - **Deep**: Clone hoàn toàn, recursive
> - **Dùng khi nào**: Shallow đủ nếu elements là immutable (số, string), deep khi có nested mutable objects

---

**Q10. `is` vs `==` khác nhau thế nào?**
> - `is`: So sánh identity (cùng object trong memory, cùng `id()`)
> - `==`: So sánh value (gọi `__eq__`)
> - Lưu ý: `None` luôn dùng `is None` không dùng `== None`

---

### 🔹 Câu hỏi nâng cao Python

**Q11. Metaclass trong Python là gì?**
> Metaclass là "class của class". `type` là metaclass mặc định.
> Dùng để: Validate class definition, tự động đăng ký subclasses, ORM (SQLAlchemy dùng metaclass!)
```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
```

---

**Q12. Asyncio - event loop hoạt động thế nào?**
> Event loop chạy trong 1 thread, quản lý coroutines.
> Khi coroutine `await` I/O, event loop chạy coroutine khác.
> **Không dùng** cho CPU-bound tasks (cần `run_in_executor` với process pool)

---

**Q13. Descriptor protocol là gì?**
> Object implementing `__get__`, `__set__`, `__delete__`.
> `@property` dùng descriptor protocol.
> SQLAlchemy Column là descriptor → truy cập `user.name` trigger query

---

### 🔹 Flask & API

**Q14. Flask application context vs request context**
> - **Application context** (`g`, `current_app`): Tồn tại trong app lifecycle
> - **Request context** (`request`, `session`): Tồn tại trong 1 request
> - `g` reset mỗi request, dùng để share data trong 1 request

---

**Q15. Làm sao handle concurrent requests trong Flask?**
> Flask WSGI server (dev) = single-threaded.
> Production: Gunicorn (multi-worker), uWSGI, hoặc async với asyncio
> Connection pooling cho DB: SQLAlchemy pool_size, max_overflow

---

**Q16. CORS - Cross-Origin Resource Sharing là gì? Cấu hình trong Flask?**
```python
from flask_cors import CORS

CORS(app, resources={
    r"/api/*": {
        "origins": ["https://your-frontend.com"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
```
> CORS ngăn browser gửi request từ origin khác. Cần configure trong Flask cho React/Next.js frontend.

---

**Q17. JWT token - structure và security considerations?**
> JWT = Header.Payload.Signature (base64 encoded)
> - **Header**: algorithm (RS256/HS256)
> - **Payload**: claims (user_id, exp, role)
> - **Signature**: verify token không bị sửa
> - Không lưu sensitive data trong payload (plaintext!)
> - Dùng short-lived access token + refresh token

---

**Q18. N+1 Query Problem là gì? Cách fix?**
> 1 query để lấy danh sách + N queries cho mỗi item = N+1 queries.
> **Fix**: `joinedload()` hoặc `subqueryload()` trong SQLAlchemy.
> **Detect**: Flask-SQLAlchemy-Debugtoolbar, query logging

---

**Q19. Database Transaction - khi nào cần rollback?**
```python
try:
    db.session.add(order)
    db.session.add(payment)
    deduct_inventory(order.items)  # có thể fail
    db.session.commit()
except Exception:
    db.session.rollback()
    raise
```

---

**Q20. RESTful API vs GraphQL - khi nào chọn cái nào?**
> - **REST**: Simple, cacheable, well-known, phù hợp CRUD
> - **GraphQL**: Client quyết định data shape, tránh over/under-fetching, nhiều consumers
> - Trong dự án của bạn: REST đủ cho eCommerce, có thể GraphQL cho recruitment dashboard

---

**Q21. Rate limiting - cách implement?**
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(app, key_func=get_remote_address)

@api_bp.route("/login", methods=["POST"])
@limiter.limit("5 per minute")  # 5 lần/phút
def login():
    pass
```

---

**Q22. Làm sao test Flask API?**
```python
def test_create_user(client, db):
    response = client.post("/api/users", json={
        "name": "Test",
        "email": "test@example.com",
        "password": "secure123"
    })
    assert response.status_code == 201
    assert response.json["email"] == "test@example.com"
    
    # Verify DB
    user = User.query.filter_by(email="test@example.com").first()
    assert user is not None
```

---

### 🔹 Database

**Q23. Index - B-tree vs Hash index?**
> - **B-tree** (default): Tốt cho range queries (`WHERE age > 18`), ORDER BY, inequality
> - **Hash**: Chỉ tốt cho equality (`WHERE id = 5`), nhanh hơn B-tree cho equality
> - PostgreSQL: GIN cho full-text/JSONB, GiST cho geometric/range types

---

**Q24. Explain ANALYZE output - làm sao đọc query plan?**
```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123;
-- Seq Scan → BAD (đọc toàn bộ bảng)
-- Index Scan → GOOD (dùng index)
-- Index Only Scan → BEST (không cần đọc heap)
-- Hash Join → OK cho 2 bảng vừa
-- Nested Loop → Tốt khi inner table nhỏ/có index
```

---

**Q25. Database Sharding là gì?**
> Chia data horizontally qua nhiều DB servers.
> - **Shard key**: Quyết định record nào đến server nào (user_id % n_shards)
> - **Vấn đề**: Cross-shard queries, rebalancing, hotspot shards
> - **Thay thế**: PostgreSQL partitioning cho data lớn một server

---

**Q26. Indexing trong MongoDB - ESR Rule?**
> **E**quality → **S**ort → **R**ange
> Index các field equality trước, sort tiếp, range sau
```javascript
// Query: { status: "active", age: { $gt: 18 } } sort by name
// Good index: { status: 1, name: 1, age: 1 }
// Equality (status) → Sort (name) → Range (age)
```

---

---

## PHẦN 2: FRONTEND & JAVASCRIPT (20 câu)

**Q27. Event Loop trong JavaScript hoạt động thế nào?**
> Call Stack → Web APIs → Callback Queue → Event Loop (chuyển callback vào stack)
> Microtask queue (Promise) ưu tiên hơn Macrotask queue (setTimeout)

---

**Q28. Promise vs async/await - khi nào dùng cái nào?**
```javascript
// Promise - tốt khi parallel
Promise.all([fetch(url1), fetch(url2)])
  .then(([res1, res2]) => { /* process */ })

// async/await - tốt khi sequential, dễ đọc
async function loadData() {
    const user = await fetch('/user');           // đợi
    const orders = await fetch(`/orders/${user.id}`); // rồi mới fetch
    return { user, orders };
}
```

---

**Q29. Closure trong JavaScript là gì? Ứng dụng?**
```javascript
// Module pattern - encapsulate state
function createCounter() {
    let count = 0;  // private
    return {
        increment: () => ++count,
        decrement: () => --count,
        getCount: () => count
    };
}
const counter = createCounter();
```

---

**Q30. React hooks - useEffect cleanup function?**
```javascript
useEffect(() => {
    const subscription = dataStream.subscribe(handler);
    
    // Cleanup: chạy trước khi effect re-run hoặc unmount
    return () => {
        subscription.unsubscribe();  // tránh memory leak
    };
}, [dependency]);
```

---

**Q31. Next.js - SSR vs SSG vs ISR vs CSR?**
> - **SSG** (Static): HTML build time, CDN cacheable, blog/docs
> - **SSR** (Server): HTML per request, luôn fresh, dashboard phức tạp
> - **ISR** (Incremental): SSG + revalidate sau N giây
> - **CSR** (Client): spa, user-specific, cần authentication
> Trong dự án Viet Kiosk của bạn: Next.js + CSR cho real-time patient data

---

**Q32. Vue 3 - Composition API vs Options API?**
```javascript
// Options API (Vue 2 style)
export default {
    data() { return { count: 0 } },
    methods: { increment() { this.count++ } }
}

// Composition API (Vue 3) - tái sử dụng logic dễ hơn
import { ref, computed } from 'vue'
export default {
    setup() {
        const count = ref(0)
        const doubled = computed(() => count.value * 2)
        const increment = () => count.value++
        return { count, doubled, increment }
    }
}
```

---

**Q33. WebSocket vs HTTP Polling vs SSE?**
> - **WebSocket**: Bi-directional, persistent, tốt cho chat/game
> - **SSE**: Server→Client only, HTTP, auto-reconnect, tốt cho notifications
> - **Long Polling**: Legacy, không hiệu quả
> Trong Viet Kiosk: WebSocket cho real-time patient updates (bi-directional cần thiết)

---

**Q34. CORS - tại sao browser block, server không block?**
> CORS là security của browser, server nhận request bình thường.
> Browser check `Access-Control-Allow-Origin` header trong response.
> Postman/curl không có CORS vì không phải browser.

---

---

## PHẦN 3: DOCKER & DEVOPS (15 câu)

**Q35. Docker image vs container?**
> - **Image**: Template read-only (blueprint)
> - **Container**: Instance đang chạy từ image (có writable layer)
> - `docker build` → image, `docker run` → container

---

**Q36. Docker layer caching - tối ưu Dockerfile?**
```dockerfile
# BAD: copy toàn bộ code trước → pip install bị cache miss thường xuyên
COPY . .
RUN pip install -r requirements.txt

# GOOD: copy requirements trước → pip install chỉ re-run khi requirements thay đổi
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

---

**Q37. docker-compose vs Kubernetes?**
> - **docker-compose**: Local dev, simple multi-container, ít services
> - **Kubernetes**: Production orchestration, auto-scaling, self-healing, nhiều services

---

**Q38. Làm sao debug container đang chạy?**
```bash
docker exec -it container_name bash   # interactive shell
docker logs container_name -f          # follow logs
docker inspect container_name          # full JSON info
docker stats                           # resource usage
```

---

**Q39. Multi-stage Docker build?**
```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Production (chỉ copy artifacts, bỏ node_modules dev)
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
# Image cuối nhỏ hơn nhiều!
```

---

**Q40. Làm sao handle secrets trong Docker?**
> 1. **Docker Secrets** (Swarm mode)
> 2. **Environment variables** từ `.env` file (không commit lên git)
> 3. **Vault** (HashiCorp) cho production
> 4. **Kubernetes Secrets** (base64, nên dùng Sealed Secrets)
> **Không bao giờ**: Hardcode trong Dockerfile hoặc commit `.env`

---

---

## PHẦN 4: MATLAB & MCR (15 câu)

**Q41. Tại sao chọn MATLAB thay vì PyTorch/scikit-learn cho thuật toán scoring?**
> Thuật toán đã được validate trong MATLAB bởi domain experts.
> Porting sang Python: risk số học sai, mất thời gian re-validate.
> MCR cho phép deploy free license + tích hợp seamlessly.

---

**Q42. MCR (MATLAB Compiler Runtime) là gì?**
> MCR là runtime environment cho phép chạy compiled MATLAB code mà không cần MATLAB license.
> Developer compile `.m` files → shared library → deploy MCR + library lên server.
> MCR cùng version với MATLAB compiler dùng để build.

---

**Q43. Làm sao share data giữa Python và MATLAB?**
> 1. **matlab.engine**: Direct function calls, cần MATLAB installed
> 2. **Compiled Python package**: `mcc -W python`, chỉ cần MCR
> 3. **File-based**: JSON/CSV temp files, subprocess call → production-safe nhất
> 4. **Shared memory**: Nâng cao, tốc độ cao

---

**Q44. Thread safety khi nhiều requests gọi MATLAB?**
> MCR không thread-safe by default.
> Giải pháp 1: `threading.Lock()` serialize calls
> Giải pháp 2: Worker pool với multiple MCR instances
> Giải pháp 3: Queue-based: requests → queue → single MATLAB worker

---

**Q45. Làm sao convert NumPy arrays → MATLAB và ngược lại?**
```python
import matlab, numpy as np
# NumPy → MATLAB
ml_array = matlab.double(np_array.tolist())

# MATLAB → NumPy (chú ý column-major!)
np_result = np.array(ml_result._data).reshape(ml_result.size, order='F')
```

---

**Q46. MATLAB index từ 1 có gây bug khi tích hợp với Python không?**
> Có thể! Cần cẩn thận khi:
> - Truyền index/offset giữa hai ngôn ngữ
> - MATLAB `A(1)` = Python `A[0]`
> - Giải pháp: Document rõ convention, unit tests verify edge cases
> - Tạo wrapper functions xử lý conversion

---

**Q47. Giải MATLAB performance vs Python performance?**
> MATLAB nhanh hơn Python trong:
> - Vectorized matrix operations (tối ưu BLAS/LAPACK)
> - Signal processing (built-in Toolboxes)
> Python nhanh hơn (với NumPy) trong:
> - String processing, file I/O
> - Machine learning (PyTorch GPU)
> - Web/API handling

---

---

## PHẦN 5: CÁC DỰ ÁN TRONG CV (20 câu)

**Q48. Mô tả dự án eCommerce Migration Services và technical challenges?**
> "Tôi xây dựng hệ thống migrate data từ nhiều nền tảng eCommerce (Shopify, Magento, WooCommerce, PrestaShop).
> - **Challenge 1**: Mỗi platform có schema khác nhau → Abstract adapter pattern
> - **Challenge 2**: Data inconsistency (duplicate SKUs, invalid references) → Validation pipeline
> - **Challenge 3**: Migration phải không downtime → Incremental migration với delta sync
> - **Challenge 4**: PrestaShop connection issue → Debug driver compatibility"

---

**Q49. Tại sao bạn dùng Docker trong eCommerce Migration?**
> "Mỗi eCommerce platform cần different client libraries (Shopify API, Magento 2 API).
> Docker cho phép:
> - Isolate dependencies (không conflict giữa Shopify và Magento libs)
> - Reproducible environment (dev = prod)
> - Deploy dễ dàng: `docker-compose up`
> - Scale specific services khi cần"

---

**Q50. Viet Kiosk - Làm sao integrate với hệ thống Viettel?**
> "Viettel cung cấp backend API (RESTful). Chúng tôi implement:
> 1. Authentication với Viettel's OAuth2
> 2. Webhook để nhận patient data updates real-time
> 3. Data sync với retry mechanism khi connection drop
> 4. Circuit breaker để không spam Viettel khi họ down"

---

**Q51. MBW Suite - LLM Integration hoạt động thế nào?**
> "Chúng tôi dùng LLM (GPT-4/Claude) để auto-generate CV từ candidate information.
> - Candidate điền form → data vào prompt template
> - LLM generate structured CV text
> - Post-processing: parse, format, validate
> - Anti-hallucination: Few-shot prompting + output validation schema
> Challenge: LLM costs và latency → cache similar prompts, async generation"

---

**Q52. Smart URL Data Parsing hoạt động thế nào?**
> "Candidate nhập LinkedIn/portfolio URL → hệ thống tự crawl và extract thông tin.
> 1. **Spider** (Scrapy/BeautifulSoup) crawl URL
> 2. **LLM extraction**: Yêu cầu LLM extract structured data từ HTML
> 3. **Validation**: Verify extracted data, fill candidate profile
> Challenge: Anti-bot measures → rotating proxies, rate limiting, Playwright cho JS-heavy sites"

---

---

## PHẦN 6: SYSTEM DESIGN (10 câu)

**Q53. Thiết kế URL shortener (bit.ly)?**
> 1. **Generate short ID**: Base62 encode, 7 chars = 62^7 ~= 3.5 tỉ
> 2. **Store**: Redis (hot URLs) + PostgreSQL (cold storage)
> 3. **Redirect**: 301 (cached) vs 302 (analytics count)
> 4. **Scale**: CDN cho static assets, DB read replicas

---

**Q54. Thiết kế notification system (email, SMS, push)?**
> 1. **Producer**: API nhận notification request → Kafka/RabbitMQ
> 2. **Workers**: Celery workers per channel (email/SMS/push)
> 3. **Retry**: Exponential backoff với dead-letter queue
> 4. **Template**: Jinja2 templates per event type
> 5. **Deduplication**: Redis để tránh duplicate sends

---

**Q55. Horizontal vs Vertical scaling?**
> - **Vertical (scale up)**: Nâng cấu hình server (CPU, RAM) - đơn giản nhưng có giới hạn
> - **Horizontal (scale out)**: Thêm servers - không giới hạn nhưng cần stateless app
> **Stateless**: Sessions trong Redis (không trong memory server), files trong S3

---

**Q56. Caching strategies - Cache-aside vs Write-through vs Write-behind?**
> - **Cache-aside** (Lazy): App check cache, miss → query DB → store cache
> - **Write-through**: Write vào cache và DB đồng thời (consistent, write latency)
> - **Write-behind**: Write vào cache, async write vào DB (fast, risk data loss)
> - **Cache invalidation**: Hardest problem - TTL, event-based, version keys

---

---

## PHẦN 7: SOFT SKILLS & BEHAVIOR (10 câu)

**Q57. Kể về 1 lần gặp bug khó nhất và cách bạn giải quyết?**
```
Gợi ý STAR:
- Situation: Dự án eCommerce Migration, PrestaShop connection fail production
- Task: Fix trong 24h vì client đang đợi
- Action: Add verbose logging, isolate to driver version incompatibility,
          test với nhiều PrestaShop versions, tìm workaround, deploy fix
- Result: Migration thành công, document issue cho team
```

---

**Q58. Bạn làm việc trong team như thế nào?**
```
- Code review: Tôi review kỹ và cho feedback constructive
- Git workflow: Feature branches, meaningful commits, PR description rõ ràng
- Pair programming: Khi stuck hoặc review complex logic
- Communication: Daily standup, document decisions, async-first
```

---

**Q59. Bạn học công nghệ mới thế nào?**
```
1. Official documentation first
2. Build small proof-of-concept
3. Đọc source code của libraries
4. Practice với real project
5. Viết blog/notes để consolidate knowledge
Ví dụ: MATLAB integration - không ai trong team biết, tự research, setup,
test, document cho team
```

---

**Q60. Điểm mạnh và điểm yếu của bạn?**
```
Mạnh:
- Full-stack capability: Tự handle frontend + backend + deployment
- Problem-solving: Không nản với vấn đề khó (MATLAB + Python integration)
- Adaptability: Học công nghệ mới nhanh (từ Flask → Frappe Framework)

Yếu (và cách cải thiện):
- Testing (unit/integration tests): Đang học pytest, TDD practice
- Ma trận kiến trúc lớn (microservices): Đang study patterns
```

---

---

## PHẦN 8: OOP & DESIGN PATTERNS (15 câu)

### 🔹 OOP Principles

**Q61. 4 tính chất OOP - giải thích và ví dụ thực tế?**
> - **Encapsulation**: Gói data + behavior lại, ẩn implementation (private fields, public methods)
> - **Inheritance**: Subclass kế thừa từ superclass, tái sử dụng code
> - **Polymorphism**: Cùng interface, nhiều implementations (method overriding, duck typing)
> - **Abstraction**: Ẩn complexity, chỉ expose interface cần thiết
> - **Ví dụ thực tế**: Trong eCommerce migration, mỗi platform (Shopify, Magento) là subclass của `BaseConnector`, override method `fetch_products()`

---

**Q62. SOLID principles - giải thích từng nguyên tắc?**
> - **S** - Single Responsibility: 1 class chỉ có 1 lý do để thay đổi
> - **O** - Open/Closed: Open for extension, closed for modification (dùng abstraction)
> - **L** - Liskov Substitution: Subclass có thể thay thế superclass mà không break behavior
> - **I** - Interface Segregation: Nhiều interface nhỏ hơn 1 interface lớn
> - **D** - Dependency Inversion: Depend on abstractions, not concretions
```python
# Vi phạm SRP: Class làm quá nhiều thứ
class UserManager:
    def create_user(self): ...
    def send_email(self): ...   # nên tách ra EmailService
    def save_to_db(self): ...   # nên tách ra UserRepository

# Tuân thủ OCP: Thêm platform mới không sửa code cũ
class BaseConnector:
    def fetch_products(self): raise NotImplementedError

class ShopifyConnector(BaseConnector):
    def fetch_products(self): ...  # override, không sửa BaseConnector
```

---

**Q63. Abstract class vs Interface (Protocol trong Python)?**
> - **Abstract class**: Có thể có implementation, dùng `ABC`, `@abstractmethod`
> - **Interface/Protocol** (Python 3.8+): Structural subtyping, duck typing
> - **Khi dùng Abstract class**: Khi có shared code giữa các subclasses
> - **Khi dùng Protocol**: Khi muốn định nghĩa contract mà không force inheritance
```python
from abc import ABC, abstractmethod
from typing import Protocol

class BaseConnector(ABC):
    def authenticate(self):  # shared implementation
        return self._get_token()
    
    @abstractmethod
    def fetch_products(self) -> list: ...  # must override

class Fetchable(Protocol):  # duck typing - không cần kế thừa
    def fetch_products(self) -> list: ...
```

---

**Q64. `__slots__` trong Python là gì và khi nào dùng?**
> `__slots__` giới hạn attributes của class, tránh tạo `__dict__` cho mỗi instance.
> - **Lợi ích**: Tiết kiệm memory (~40-50%), truy cập attribute nhanh hơn
> - **Nhược điểm**: Không thể add attribute động, kế thừa phức tạp hơn
```python
class Point:
    __slots__ = ['x', 'y']  # chỉ cho phép x và y
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Khi tạo hàng triệu objects (trading, game, parser) → dùng __slots__
```

---

**Q65. Composition vs Inheritance - khi nào dùng cái nào?**
> **"Favor composition over inheritance"** - Gang of Four
> - **Inheritance**: Quan hệ "is-a" (Dog IS-A Animal)
> - **Composition**: Quan hệ "has-a" (Car HAS-A Engine)
> - **Vấn đề với deep inheritance**: Fragile base class, tight coupling
```python
# Inheritance (khi IS-A thực sự đúng)
class Animal:
    def breathe(self): ...

class Dog(Animal):
    def bark(self): ...

# Composition (linh hoạt hơn)
class Logger:
    def log(self, msg): ...

class UserService:
    def __init__(self):
        self.logger = Logger()  # HAS-A, không kế thừa Logger
```

---

### 🔹 Design Patterns

**Q66. Singleton Pattern - implement và rủi ro?**
```python
class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:  # thread-safe
                if not cls._instance:  # double-check
                    cls._instance = super().__new__(cls)
        return cls._instance

# Rủi ro: Khó test (global state), hidden dependencies
# Thay thế: Dependency Injection
```

---

**Q67. Factory Pattern là gì? Ứng dụng thực tế?**
```python
# Tạo object mà không cần biết class cụ thể
class ConnectorFactory:
    _registry = {
        'shopify': ShopifyConnector,
        'magento': MagentoConnector,
        'woocommerce': WooCommerceConnector,
    }

    @classmethod
    def create(cls, platform: str) -> BaseConnector:
        connector_class = cls._registry.get(platform)
        if not connector_class:
            raise ValueError(f"Unsupported platform: {platform}")
        return connector_class()

# Dùng: connector = ConnectorFactory.create('shopify')
# Thêm platform mới: chỉ thêm vào _registry, không sửa code khác
```

---

**Q68. Observer Pattern - pub/sub là gì?**
```python
# Subject notify tất cả Observers khi state thay đổi
class EventEmitter:
    def __init__(self):
        self._listeners = defaultdict(list)

    def on(self, event: str, callback):
        self._listeners[event].append(callback)

    def emit(self, event: str, data=None):
        for callback in self._listeners[event]:
            callback(data)

# Ứng dụng: WebSocket events, Django signals, React state management
emitter = EventEmitter()
emitter.on('migration_complete', send_email_notification)
emitter.on('migration_complete', update_dashboard)
emitter.emit('migration_complete', {'status': 'success'})
```

---

**Q69. Strategy Pattern - khi nào dùng?**
```python
# Đóng gói algorithm, có thể swap runtime
from typing import Protocol

class SortStrategy(Protocol):
    def sort(self, data: list) -> list: ...

class QuickSort:
    def sort(self, data): return sorted(data)  # simplified

class MergeSort:
    def sort(self, data): ...

class DataProcessor:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def process(self, data):
        return self.strategy.sort(data)

# Ứng dụng: Payment methods, compression algorithms, validation strategies
processor = DataProcessor(QuickSort())
processor.strategy = MergeSort()  # swap mà không sửa DataProcessor
```

---

**Q70. Decorator Pattern vs Python Decorator?**
> - **GoF Decorator Pattern**: Wrap object để thêm behavior (structural)
> - **Python `@decorator`**: Wrap function/class (functional approach)
```python
# GoF Decorator Pattern
class CachedConnector:
    def __init__(self, connector: BaseConnector):
        self._connector = connector
        self._cache = {}

    def fetch_products(self):
        if 'products' not in self._cache:
            self._cache['products'] = self._connector.fetch_products()
        return self._cache['products']

# Thêm caching mà không sửa ShopifyConnector
shopify = CachedConnector(ShopifyConnector())
```

---

**Q71. Repository Pattern - tại sao dùng trong web app?**
```python
# Tách business logic khỏi data access
class UserRepository:
    def __init__(self, db_session):
        self.db = db_session

    def find_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter_by(id=user_id).first()

    def find_active_users(self) -> list[User]:
        return self.db.query(User).filter_by(is_active=True).all()

    def save(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        return user

# Lợi ích: Dễ test (mock repository), swap DB engine, centralize queries
```

---

**Q72. Dependency Injection là gì? Ứng dụng trong Python/Flask?**
> DI = Truyền dependencies từ bên ngoài vào thay vì tự tạo bên trong.
> - **Lợi ích**: Dễ test (inject mock), loose coupling, dễ swap implementation
```python
# BAD: Hard dependency
class OrderService:
    def __init__(self):
        self.repo = OrderRepository(db)  # tight coupling

# GOOD: Dependency Injection
class OrderService:
    def __init__(self, repo: OrderRepository, notifier: Notifier):
        self.repo = repo          # injected
        self.notifier = notifier  # injected

# Test: inject mock objects
service = OrderService(repo=MockOrderRepo(), notifier=MockNotifier())
```

---

**Q73. MVC vs MVP vs MVVM?**
> - **MVC**: Model-View-Controller (Flask, Django) - Controller update Model, View đọc Model
> - **MVP**: Model-View-Presenter - Presenter mediates giữa View và Model, View passive
> - **MVVM**: Model-View-ViewModel (Vue, React+MobX) - ViewModel expose data streams, View bind tự động
> - **Trong Flask**: Routes = Controller, SQLAlchemy Models = Model, Jinja2/React = View

---

**Q74. Event-driven architecture là gì?**
> Components giao tiếp qua events thay vì direct calls.
> - **Lợi ích**: Loose coupling, async processing, easy to scale
> - **Ví dụ**: `user_registered` event → trigger: send_welcome_email, create_profile, notify_admin
> - **Tools**: Celery + Redis/RabbitMQ, Kafka, AWS EventBridge
> - **Trong dự án**: Migration completion → emit event → update dashboard, send email

---

**Q75. Anti-patterns cần tránh?**
> - **God Object**: 1 class làm quá nhiều thứ → vi phạm SRP
> - **Spaghetti Code**: Logic không có structure, khó trace
> - **Copy-paste programming**: Không DRY, bug fix phải sửa nhiều chỗ
> - **Premature Optimization**: Tối ưu trước khi có bottleneck thực sự
> - **Magic Numbers**: Hardcode số vô nghĩa → dùng named constants
> - **Callback Hell**: Nested callbacks → dùng Promise/async-await

---

## PHẦN 9: GIT & CI/CD (10 câu)

**Q76. Git rebase vs merge - khi nào dùng cái nào?**
```bash
# Merge: Giữ history đầy đủ, tạo merge commit
git checkout main
git merge feature/user-auth
# History: A - B - C - M (merge commit)
#               \   /
#                D - E

# Rebase: Linear history, sạch hơn nhưng rewrite commits
git checkout feature/user-auth
git rebase main
# History: A - B - C - D' - E'

# Rule: rebase cho local branches, merge cho public branches
# NEVER rebase shared/public branches
```

---

**Q77. Git cherry-pick, stash, bisect dùng khi nào?**
```bash
# cherry-pick: Lấy 1 commit cụ thể từ branch khác
git cherry-pick abc1234  # apply commit này vào current branch
# Use case: Hotfix trên main, muốn apply lên release branch

# stash: Tạm lưu changes chưa commit
git stash               # lưu
git stash pop           # restore
git stash list          # xem danh sách

# bisect: Binary search tìm commit gây bug
git bisect start
git bisect bad          # current commit có bug
git bisect good v1.0    # version này OK
# Git tự checkout commit giữa → test → mark good/bad
```

---

**Q78. Git workflow - GitFlow vs Trunk-Based Development?**
> - **GitFlow**: `main` + `develop` + `feature/*` + `release/*` + `hotfix/*`
>   - Phù hợp: Release theo schedule, phần mềm versioned
>   - Nhược: Phức tạp, merge conflicts nhiều
> - **Trunk-Based**: Tất cả commit vào `main`, dùng feature flags
>   - Phù hợp: CI/CD liên tục, team nhỏ nhanh
>   - Ưu: Ít conflicts, deploy thường xuyên
> - **Thực tế**: GitHub Flow (main + short-lived feature branches) - cân bằng tốt

---

**Q79. CI/CD pipeline - giải thích các stages?**
```yaml
# GitHub Actions example
stages:
  - lint:        # Kiểm tra code style (flake8, eslint)
  - test:        # Unit + integration tests (pytest, jest)
  - security:    # SAST scan (bandit, snyk)
  - build:       # docker build, npm build
  - staging:     # Deploy lên staging environment
  - e2e-test:    # End-to-end tests (Playwright, Cypress)
  - production:  # Deploy production (manual approval hoặc auto)
  - notify:      # Slack/email notification
```

---

**Q80. Làm sao viết commit message tốt?**
```bash
# Conventional Commits format
<type>(<scope>): <short description>

feat(auth): add JWT refresh token endpoint
fix(migration): handle null product SKU in Magento adapter
docs(api): update OpenAPI spec for /users endpoint
refactor(db): extract query logic to UserRepository
test(orders): add integration test for bulk order creation
chore(deps): upgrade SQLAlchemy to 2.0

# Rules:
# - Imperative mood: "add", không phải "added" hay "adds"
# - Max 72 chars per line
# - Body giải thích WHY, không phải WHAT
# - Reference issue: "Closes #123"
```

---

**Q81. Semantic Versioning (SemVer) là gì?**
> **MAJOR.MINOR.PATCH** (ví dụ: 2.4.1)
> - **PATCH** (2.4.1 → 2.4.2): Bug fixes, backward compatible
> - **MINOR** (2.4.1 → 2.5.0): New features, backward compatible
> - **MAJOR** (2.4.1 → 3.0.0): Breaking changes
> - **Pre-release**: `1.0.0-alpha.1`, `1.0.0-beta.2`, `1.0.0-rc.1`

---

**Q82. Blue-Green Deployment vs Canary Deployment?**
> - **Blue-Green**: 2 identical environments (Blue=live, Green=new). Switch traffic 100% cùng lúc. Rollback = switch back. Zero downtime.
> - **Canary**: Release từng phần nhỏ (5% → 25% → 100%). Monitor metrics ở mỗi bước. Detect issues trước khi ảnh hưởng tất cả users.
> - **Rolling**: Update instances lần lượt, không có idle environment.

---

**Q83. Làm sao handle database migrations trong CI/CD?**
```python
# Alembic migration strategy
# 1. Migration file được version control
# 2. CI: chạy `alembic upgrade head` trên test DB
# 3. Backward-compatible migrations:
#    - Thêm column nullable trước (không breaking)
#    - Populate data
#    - Thêm NOT NULL constraint sau

# NGUY HIỂM - Không rollback được dễ:
# - DROP TABLE, DROP COLUMN
# - Rename column (app cũ sẽ fail)

# SAFE:
# - ADD COLUMN nullable
# - CREATE TABLE
# - CREATE INDEX CONCURRENTLY (PostgreSQL)
```

---

**Q84. `.gitignore` - những gì cần ignore?**
```gitignore
# Secrets (QUAN TRỌNG NHẤT)
.env
*.env.local
secrets.json

# Python
__pycache__/
*.pyc
.venv/
dist/
*.egg-info/

# Node
node_modules/
.next/
dist/

# IDE
.vscode/settings.json
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Docker local overrides
docker-compose.override.yml
```

---

**Q85. Code review - bạn check những gì?**
> **Checklist khi review:**
> - ✅ Logic đúng không? Edge cases được handle?
> - ✅ Tests đủ chưa? Happy path + error cases
> - ✅ Security: SQL injection, XSS, hardcoded secrets?
> - ✅ Performance: N+1 queries? Unnecessary loops?
> - ✅ Naming: Variables/functions có tên rõ nghĩa?
> - ✅ DRY: Code lặp lại không?
> - ✅ Error handling: Exceptions được catch đúng chỗ?
> - ✅ Documentation: Complex logic có comment giải thích không?

---

## PHẦN 10: SECURITY (10 câu)

**Q86. OWASP Top 10 - các lỗ hổng phổ biến nhất?**
> 1. **Broken Access Control**: User A truy cập data của User B
> 2. **Cryptographic Failures**: Dùng MD5/SHA1 cho password
> 3. **Injection**: SQL Injection, NoSQL Injection, Command Injection
> 4. **Insecure Design**: Logic flaws trong business rules
> 5. **Security Misconfiguration**: Default passwords, debug mode in prod
> 6. **Vulnerable Components**: Outdated libraries với known CVEs
> 7. **Authentication Failures**: Weak passwords, no rate limiting
> 8. **Data Integrity Failures**: Deserialize untrusted data
> 9. **Logging Failures**: Không log security events
> 10. **SSRF**: Server-side request forgery

---

**Q87. SQL Injection - cách phòng tránh?**
```python
# NGUY HIỂM - SQL Injection
user_id = request.args.get('id')
query = f"SELECT * FROM users WHERE id = {user_id}"
# Attacker: id=1 OR 1=1 → lấy toàn bộ users
# Attacker: id=1; DROP TABLE users --

# AN TOÀN - Parameterized queries
# SQLAlchemy ORM (auto-escaped)
user = User.query.filter_by(id=user_id).first()

# Raw SQL với params
db.execute("SELECT * FROM users WHERE id = :id", {"id": user_id})

# Ngoài ra:
# - Input validation (whitelist)
# - Least privilege DB user (SELECT only nếu chỉ cần read)
# - WAF (Web Application Firewall)
```

---

**Q88. Password storage - cách đúng?**
```python
from werkzeug.security import generate_password_hash, check_password_hash
# hoặc
import bcrypt

# ĐÚNG: Hash + Salt với bcrypt/argon2/scrypt
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))

# SAI: MD5, SHA1 (nhanh → dễ brute force)
# SAI: Plain text
# SAI: Encrypt (có thể decrypt)
# SAI: Hash không có salt (rainbow table attack)

# Best practices:
# - Minimum 12 rounds bcrypt
# - Argon2id cho các ứng dụng mới (winner PHC)
# - Pepper (server-side secret) + Salt (per-user, stored in DB)
```

---

**Q89. XSS (Cross-Site Scripting) - các loại và phòng tránh?**
> **Stored XSS**: Script được lưu vào DB, chạy khi user load page
> **Reflected XSS**: Script trong URL parameter, reflect về response
> **DOM XSS**: JavaScript trực tiếp manipulate DOM không sanitize
```javascript
// NGUY HIỂM
document.innerHTML = userInput;
eval(userInput);

// AN TOÀN
document.textContent = userInput;  // auto-escape
// Hoặc sanitize: DOMPurify library

// Backend: Content-Security-Policy header
// Flask: flask-talisman
// Template engines: Jinja2 auto-escape {{ var }} (dùng |safe cẩn thận)
```

---

**Q90. CSRF (Cross-Site Request Forgery) là gì?**
> Attacker trick user submit form đến site mà user đang authenticated.
> **Phòng tránh:**
> - CSRF token (random, per-session, verify server-side)
> - `SameSite=Strict` cookie attribute
> - Check `Origin`/`Referer` header
```python
# Flask-WTF tự động thêm CSRF protection
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)

# Frontend gửi token trong header
# axios.defaults.headers['X-CSRFToken'] = getCookie('csrftoken')
```

---

**Q91. HTTPS, TLS, và certificate pinning?**
> - **TLS**: Transport Layer Security, mã hóa data in transit
> - **Certificate**: Xác thực server là ai mình nghĩ
> - **HSTS**: HTTP Strict Transport Security - force HTTPS
> - **Certificate Pinning**: App chỉ accept specific cert (chống MITM)
```python
# Flask với flask-talisman
from flask_talisman import Talisman
Talisman(app,
    force_https=True,
    strict_transport_security=True,
    content_security_policy={
        'default-src': "'self'",
        'script-src': "'self'"
    }
)
```

---

**Q92. API Security best practices?**
> 1. **Authentication**: JWT với short expiry (15 phút), refresh tokens
> 2. **Authorization**: RBAC (Role-Based Access Control), check ownership
> 3. **Rate Limiting**: Chống brute force, DDoS
> 4. **Input Validation**: Validate tất cả input, whitelist > blacklist
> 5. **HTTPS only**: Không accept HTTP
> 6. **API versioning**: `/api/v1/`, không break old clients
> 7. **Error messages**: Không leak stack traces, internal info
> 8. **Logging**: Log authentication attempts, suspicious activity
> 9. **CORS**: Strict origin whitelist
> 10. **Secrets**: Environment variables, không trong code

---

**Q93. Environment variables vs Secrets management?**
```python
# ENV VARS - đủ cho most cases
import os
DB_URL = os.environ.get('DATABASE_URL')

# Không commit .env vào git
# .env.example là template an toàn để commit

# Production-grade secrets management:
# - AWS Secrets Manager / Parameter Store
# - HashiCorp Vault
# - Kubernetes Secrets (+ Sealed Secrets hoặc External Secrets Operator)
# - Azure Key Vault, GCP Secret Manager

# Rotate secrets định kỳ
# Audit who accessed what secrets
```

---

**Q94. Dependency security - cách kiểm tra?**
```bash
# Python
pip install safety
safety check                    # kiểm tra CVEs trong requirements.txt

pip install pip-audit
pip-audit                        # audit dependencies

# Node.js
npm audit
npm audit fix

# GitHub: Dependabot alerts (tự động)
# Snyk, OWASP Dependency-Check

# Best practices:
# - Pin exact versions trong requirements.txt
# - Regular updates (không để quá cũ)
# - Review changelogs khi update major versions
```

---

**Q95. Logging security - nên log gì và không log gì?**
```python
# NÊN LOG:
# - Authentication events (login success/fail, logout)
# - Authorization failures (403 errors)
# - Data modifications (create/update/delete sensitive data)
# - System errors, exceptions
# - API calls với timestamp, user_id, endpoint

# KHÔNG BAO GIỜ LOG:
# - Passwords (kể cả hashed)
# - Credit card numbers, CVV
# - Social security numbers
# - JWT tokens, API keys, secrets
# - Personal health information (PHI)

import logging
logger = logging.getLogger(__name__)

# Structured logging (dễ query hơn)
logger.info("User login", extra={
    "user_id": user.id,
    "ip": request.remote_addr,
    "user_agent": request.user_agent.string
})
```

---

## PHẦN 11: TESTING (10 câu)

**Q96. Unit test vs Integration test vs E2E test - pyramid?**
> **Testing Pyramid** (từ dưới lên):
> - 🔺 **E2E** (ít nhất, chậm nhất): Simulate user thực sự, test toàn bộ flow
> - 🔶 **Integration** (vừa): Test nhiều components cùng nhau, real DB
> - 🟩 **Unit** (nhiều nhất, nhanh nhất): Test 1 function/class cô lập, mock dependencies
>
> **Rule**: 70% unit / 20% integration / 10% E2E

---

**Q97. Pytest fixtures và conftest.py?**
```python
# conftest.py - shared fixtures
import pytest
from app import create_app, db as _db

@pytest.fixture(scope='session')
def app():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    return app

@pytest.fixture(scope='function')
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.session.remove()
        _db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

# test_users.py
def test_create_user(client, db):
    response = client.post('/api/users', json={'name': 'Test'})
    assert response.status_code == 201
```

---

**Q98. Mocking - khi nào và cách dùng `unittest.mock`?**
```python
from unittest.mock import Mock, patch, MagicMock

# Mock external API calls (không gọi thật)
@patch('app.services.requests.post')
def test_send_notification(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {'status': 'sent'}

    result = send_notification('user@example.com', 'Hello')
    
    assert result is True
    mock_post.assert_called_once()  # verify nó được gọi

# Mock DB calls
def test_get_user():
    mock_repo = Mock()
    mock_repo.find_by_id.return_value = User(id=1, name='Test')
    
    service = UserService(repo=mock_repo)
    user = service.get_user(1)
    assert user.name == 'Test'
```

---

**Q99. TDD (Test-Driven Development) workflow?**
> **Red → Green → Refactor**
> 1. **Red**: Viết test fail trước (test chưa có implementation)
> 2. **Green**: Viết code tối thiểu để pass test
> 3. **Refactor**: Cải thiện code mà không break tests
```python
# Bước 1: Viết test trước
def test_calculate_discount():
    assert calculate_discount(100, 'vip') == 20  # 20% off
    assert calculate_discount(100, 'regular') == 10  # 10% off
    assert calculate_discount(100, 'unknown') == 0   # no discount

# Bước 2: Implement
def calculate_discount(price: float, tier: str) -> float:
    rates = {'vip': 0.2, 'regular': 0.1}
    return price * rates.get(tier, 0)

# Bước 3: Refactor nếu cần (extract constants, etc.)
```

---

**Q100. Test coverage - có ý nghĩa gì và pitfalls?**
```bash
pytest --cov=app --cov-report=html

# Coverage % không thay thế cho quality tests!
# 100% coverage nhưng test không verify behavior = vô nghĩa

# Good coverage target: 70-80% là practical
# Focus vào:
# - Business logic critical paths
# - Error handling / edge cases
# - Regression tests cho bugs đã fix

# Pitfalls:
# - Test implementation, không test behavior
# - Không test error cases
# - Flaky tests (pass/fail ngẫu nhiên) → mất trust
```

---

**Q101. Property-based testing là gì?**
```python
# Hypothesis library - generate test cases tự động
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sort_is_idempotent(lst):
    # Sort 2 lần = sort 1 lần
    assert sorted(sorted(lst)) == sorted(lst)

@given(st.text(), st.text())
def test_string_concat(s1, s2):
    assert len(s1 + s2) == len(s1) + len(s2)

# Hypothesis tự tìm edge cases: empty list, max int, unicode chars
# Rất tốt để test algorithms, parsers, data transformations
```

---

**Q102. Làm sao test asynchronous code?**
```python
import pytest
import asyncio

@pytest.mark.asyncio
async def test_async_fetch():
    result = await fetch_user_data(user_id=1)
    assert result['name'] == 'Test User'

# Mock async functions
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_notification_service():
    mock_client = AsyncMock()
    mock_client.send.return_value = {'status': 'sent'}
    
    service = NotificationService(client=mock_client)
    await service.notify('user@example.com')
    
    mock_client.send.assert_called_once()
```

---

**Q103. Performance testing - cách approach?**
```python
# Locust - load testing tool
from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)  # nghỉ 1-3 giây giữa requests

    @task(3)  # weight: chạy 3x nhiều hơn
    def get_products(self):
        self.client.get('/api/products')

    @task(1)
    def create_order(self):
        self.client.post('/api/orders', json={
            'product_id': 1, 'quantity': 2
        })

# Chạy: locust -f locustfile.py --host=http://localhost:5000
# Monitor: response time p50/p95/p99, error rate, RPS

# k6 (JavaScript) cũng phổ biến
```

---

**Q104. Regression testing là gì?**
> Test đảm bảo bugs đã fix không tái xuất hiện, và features cũ vẫn hoạt động sau khi thêm code mới.
> **Workflow:**
> 1. Bug được report → reproduce bằng failing test
> 2. Fix bug → test pass
> 3. Test được giữ lại trong test suite
> 4. Mỗi CI run, test này chạy lại → prevent regression
```bash
# Tạo test case cho bug #456
# test_bug_456_null_sku.py
def test_migration_handles_null_sku():
    """Regression test for issue #456: Migration crashes on null SKU"""
    products = [{'name': 'Product A', 'sku': None}]
    result = migrate_products(products)
    assert result.success is True
    assert result.skipped_count == 1  # null SKU được skip, không crash
```

---

**Q105. Snapshot testing - khi nào dùng?**
```javascript
// Jest snapshot testing (React components)
import { render } from '@testing-library/react'

test('renders ProductCard correctly', () => {
    const { asFragment } = render(
        <ProductCard name="iPhone 15" price={999} />
    )
    expect(asFragment()).toMatchSnapshot()
    // Lần đầu: tạo snapshot file
    // Các lần sau: so sánh với snapshot cũ
})

// Tốt cho: UI components, API response shapes
// Nhược: Snapshot dễ bị update mà không review kỹ
// Rule: Snapshot nhỏ gọn, review kỹ khi update
```

---

## PHẦN 12: SQL NÂNG CAO (10 câu)

**Q106. Window Functions - ứng dụng thực tế?**
```sql
-- ROW_NUMBER, RANK, DENSE_RANK
SELECT
    employee_id,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank,
    salary - AVG(salary) OVER (PARTITION BY department) as diff_from_avg,
    SUM(salary) OVER (ORDER BY hire_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_total
FROM employees;

-- LAG/LEAD: So sánh với row trước/sau
SELECT
    date,
    revenue,
    revenue - LAG(revenue) OVER (ORDER BY date) as day_over_day_change
FROM daily_sales;
```

---

**Q107. CTE (Common Table Expressions) vs Subquery?**
```sql
-- Subquery (khó đọc khi phức tạp)
SELECT * FROM orders
WHERE user_id IN (
    SELECT id FROM users WHERE created_at > '2024-01-01'
);

-- CTE (dễ đọc, reusable trong cùng query)
WITH new_users AS (
    SELECT id FROM users WHERE created_at > '2024-01-01'
),
user_orders AS (
    SELECT * FROM orders WHERE user_id IN (SELECT id FROM new_users)
)
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN user_orders o ON u.id = o.user_id
GROUP BY u.name;

-- Recursive CTE: Tree structures (category hierarchy, org chart)
WITH RECURSIVE category_tree AS (
    SELECT id, name, parent_id, 0 as depth
    FROM categories WHERE parent_id IS NULL
    UNION ALL
    SELECT c.id, c.name, c.parent_id, ct.depth + 1
    FROM categories c
    JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree;
```

---

**Q108. ACID properties - giải thích?**
> - **A**tomicity: Transaction là all-or-nothing. Partial failure → rollback toàn bộ
> - **C**onsistency: DB luôn ở trạng thái valid sau transaction (constraints, triggers)
> - **I**solation: Concurrent transactions không ảnh hưởng nhau
> - **D**urability: Committed data không bị mất dù crash
>
> **Isolation levels** (tăng dần):
> - READ UNCOMMITTED → Dirty reads
> - READ COMMITTED → No dirty reads (PostgreSQL default)
> - REPEATABLE READ → No dirty/non-repeatable reads
> - SERIALIZABLE → No dirty/non-repeatable/phantom reads

---

**Q109. Transaction Isolation levels - phantom read là gì?**
```sql
-- Dirty Read: Đọc data chưa commit của transaction khác
-- Non-repeatable Read: Đọc cùng row 2 lần, kết quả khác
-- Phantom Read: Query trả về số rows khác do transaction khác INSERT/DELETE

-- SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN;
SELECT COUNT(*) FROM orders WHERE status = 'pending'; -- 10
-- Transaction B INSERT 2 orders pending và COMMIT
SELECT COUNT(*) FROM orders WHERE status = 'pending'; -- 12 (phantom!)
COMMIT;

-- Giải quyết: SERIALIZABLE isolation (chậm hơn) hoặc SELECT FOR UPDATE
SELECT * FROM inventory WHERE product_id = 5 FOR UPDATE; -- lock row
```

---

**Q110. Partitioning trong PostgreSQL?**
```sql
-- Range partitioning theo thời gian (phổ biến nhất)
CREATE TABLE orders (
    id BIGSERIAL,
    created_at TIMESTAMP NOT NULL,
    amount DECIMAL(10,2)
) PARTITION BY RANGE (created_at);

CREATE TABLE orders_2024 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');

CREATE TABLE orders_2025 PARTITION OF orders
    FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');

-- Query tự động chỉ scan partition cần thiết (partition pruning)
-- Index: Tạo index trên từng partition
-- Use case: Logs, time-series data, orders history
```

---

**Q111. Deadlock là gì và cách tránh?**
```sql
-- Deadlock: Transaction A lock row 1 đợi row 2,
--           Transaction B lock row 2 đợi row 1 → circular wait

-- TRÁNH DEADLOCK:
-- 1. Lock resources theo thứ tự nhất quán
-- Transaction A và B đều: lock user trước, rồi lock account

-- 2. Giữ transactions ngắn, commit sớm

-- 3. Dùng SELECT FOR UPDATE SKIP LOCKED (hàng đợi processing)
SELECT * FROM jobs
WHERE status = 'pending'
ORDER BY created_at
LIMIT 1
FOR UPDATE SKIP LOCKED;  -- skip rows đang bị lock

-- 4. Retry logic khi gặp deadlock
```

---

**Q112. Full-text search trong PostgreSQL?**
```sql
-- Tạo index
CREATE INDEX idx_products_fts ON products
USING GIN (to_tsvector('english', name || ' ' || description));

-- Query
SELECT name, ts_rank(
    to_tsvector('english', name || ' ' || description),
    to_tsquery('english', 'laptop & gaming')
) as rank
FROM products
WHERE to_tsvector('english', name || ' ' || description)
    @@ to_tsquery('english', 'laptop & gaming')
ORDER BY rank DESC;

-- Khi cần Elasticsearch: Scale lớn, fuzzy search, faceted search, multi-index
```

---

**Q113. Query optimization - checklist?**
```sql
-- 1. EXPLAIN ANALYZE để xem query plan
EXPLAIN (ANALYZE, BUFFERS) SELECT ...;

-- 2. Kiểm tra Seq Scan trên bảng lớn → cần index
-- 3. Kiểm tra N+1 với ORM → joinedload / eager loading
-- 4. SELECT * → chỉ SELECT cột cần thiết (covering index)

-- 5. Optimize JOINs
-- INNER JOIN nếu biết có match (nhanh hơn LEFT JOIN)
-- JOIN condition trên indexed columns

-- 6. Pagination: OFFSET lớn = slow, dùng cursor-based
-- SLOW: ORDER BY id LIMIT 20 OFFSET 10000
-- FAST: WHERE id > last_seen_id ORDER BY id LIMIT 20

-- 7. VACUUM ANALYZE sau DELETE/UPDATE nhiều
-- 8. Connection pooling: PgBouncer
```

---

**Q114. NoSQL - khi nào chọn MongoDB thay PostgreSQL?**
> **Chọn MongoDB khi:**
> - Schema thay đổi thường xuyên (flexible schema)
> - Document-oriented data (nested, hierarchical)
> - Horizontal sharding từ đầu
> - Real-time analytics trên unstructured data
>
> **Chọn PostgreSQL khi:**
> - Cần ACID transactions
> - Data có relationships rõ ràng
> - Complex queries (JOINs)
> - Cần audit trail, data integrity
>
> **Trong eCommerce**: PostgreSQL cho orders/payments (ACID), MongoDB cho product catalog (flexible attributes), Redis cho sessions/cart

---

**Q115. Database connection pooling - tại sao quan trọng?**
```python
# Mỗi DB connection: ~5MB RAM, 100ms để establish
# Without pooling: Mỗi request tạo connection mới → chậm, out of connections

# SQLAlchemy connection pool
engine = create_engine(
    DATABASE_URL,
    pool_size=10,           # connections duy trì sẵn
    max_overflow=20,        # extra connections khi pool đầy
    pool_timeout=30,        # giây chờ trước khi raise exception
    pool_recycle=3600,      # recycle connections sau 1 giờ (tránh timeout)
    pool_pre_ping=True      # kiểm tra connection còn sống trước khi dùng
)

# PgBouncer: External connection pooler
# - Transaction pooling: connection chỉ held trong transaction
# - Cho phép hàng nghìn app connections → vài chục DB connections
```

---

## PHẦN 13: CÂU HỎI TÌNH HUỐNG THỰC TẾ (10 câu)

**Q116. API của bạn bị chậm bất ngờ - troubleshoot thế nào?**
> **Systematic approach:**
> 1. **Monitor first**: Check response times, error rates, CPU/RAM/DB metrics
> 2. **Isolate**: Endpoint nào chậm? Chậm từ khi nào? Có traffic spike không?
> 3. **DB queries**: Enable slow query log, check EXPLAIN ANALYZE
> 4. **External dependencies**: API third-party có chậm không? (circuit breaker)
> 5. **Memory**: Memory leak? Garbage collection pause?
> 6. **Code**: Recent deploys? Profile code với cProfile/py-spy
> 7. **Fix + Verify**: Deploy fix, confirm metrics improve

---

**Q117. Production DB bị full disk - bạn làm gì ngay lập tức?**
> **Immediate actions (thứ tự ưu tiên):**
> 1. **Alert team**, không panic
> 2. **Identify source**: `du -sh /var/lib/postgresql/*` - logs? temp files? bloat?
> 3. **Quick wins**: Xóa old log files, VACUUM FULL nếu bloat lớn
> 4. **Extend disk** (nếu cloud): Resize EBS/PD không downtime
> 5. **Archive old data** sang cold storage (S3)
> 6. **Prevent**: Set up disk usage alerts (>80%), log rotation, data retention policy

---

**Q118. Deploy xong bị lỗi production - rollback thế nào?**
```bash
# Docker/docker-compose: rollback image cũ
docker-compose down
git checkout v1.2.3  # tag version cũ
docker-compose up -d

# Kubernetes: rollback deployment
kubectl rollout undo deployment/myapp
kubectl rollout history deployment/myapp  # xem versions

# Database migrations: Điều phức tạp nhất
# Nếu migration backward-compatible: không cần rollback
# Nếu không: cần down migration script chuẩn bị trước

# Lesson: Blue-Green deployment → rollback = đổi traffic, không rollback DB
```

---

**Q119. Làm sao handle một task lớn (ví dụ: migrate 1 triệu records)?**
```python
# Không migrate 1M records trong 1 request/process
# Approach:
# 1. Batch processing
def migrate_in_batches(batch_size=1000):
    offset = 0
    while True:
        batch = get_batch(offset, batch_size)
        if not batch:
            break
        process_batch(batch)
        offset += batch_size
        log_progress(offset)  # checkpoint

# 2. Background job (Celery)
@celery.task(bind=True, max_retries=3)
def migrate_batch(self, offset, batch_size):
    try:
        process_batch(offset, batch_size)
    except Exception as exc:
        self.retry(exc=exc, countdown=60)

# 3. Progress tracking: Redis store progress
# 4. Idempotent: Có thể resume nếu crash giữa chừng
# 5. Monitor: Logs, metrics, ETA
```

---

**Q120. Team member commit thẳng vào main và gây bug - bạn xử lý thế nào?**
> **Technical:**
> 1. `git revert <commit>` (không xóa history, an toàn hơn `git reset`)
> 2. Deploy revert ngay
> 3. Verify production hoạt động bình thường
>
> **Process (prevent lần sau):**
> 1. Enable **branch protection** trên main (GitHub/GitLab)
> 2. Require **Pull Request + Code Review** trước khi merge
> 3. Require **CI checks pass** (tests, lint)
> 4. Blameless **postmortem**: Tại sao xảy ra? Process fix gì?
>
> **Communication**:
> - Không blame cá nhân, focus vào process improvement
> - Document trong team wiki

---

**Q121. Bạn nhận task không rõ requirements - làm sao?**
> **Không code ngay khi requirements mơ hồ!**
> 1. **Clarify**: Hỏi lại stakeholder - "Who is the user? What problem are we solving?"
> 2. **Write down understanding**: "Tôi hiểu task này là X, Y, Z - đúng không?"
> 3. **Identify edge cases**: "Điều gì xảy ra khi...?"
> 4. **Agree on scope**: MVP trước, nice-to-have sau
> 5. **Time estimate**: Estimate sau khi đã rõ requirements
> 6. **Document decision**: Ghi lại trong ticket/PR description

---

**Q122. Code review - bạn nhận feedback rất negative - làm sao?**
> **Mindset**: Code review không phải personal attack, là improve product.
> 1. **Đọc kỹ**: Reviewer có đúng không? Học từ feedback
> 2. **Nếu đồng ý**: "Good catch, fixed!" + fix + update PR
> 3. **Nếu không đồng ý**: Giải thích reasoning của mình, có thể mang lên team discuss
> 4. **Nếu feedback unclear**: Hỏi clarification
> 5. **Không defensive**: "Sao anh/chị không thích code của em?" = sai
> 6. **Nếu pattern lặp lại**: 1-on-1 với reviewer để align về coding standards

---

**Q123. Deadline gấp nhưng code quality thấp - bạn xử lý thế nào?**
> **Không có câu trả lời đúng tuyệt đối - đây là tradeoff discussion.**
> 1. **Communicate early**: Báo lead/manager sớm khi thấy risk
> 2. **Scope cut**: Tính năng nào thực sự cần cho deadline? Nice-to-have?
> 3. **Technical debt plan**: Ship với TODO, tạo ticket, schedule cleanup sau
> 4. **Document tradeoffs**: "Tôi dùng approach X vì deadline, plan Y để refactor sau"
> 5. **Không compromise security/data loss**: Chấp nhận skip performance optimization, không chấp nhận skip input validation

---

**Q124. Làm sao estimate time cho một task?**
> **Không estimate thẳng - break down trước!**
```
Task: "Thêm feature export CSV"

Breakdown:
1. Research/Understand requirements: 0.5h
2. Design DB query: 1h (có thể phức tạp?)
3. Backend endpoint: 2h
4. Streaming file response: 1h (lần đầu làm: +1h buffer)
5. Frontend download button: 1h
6. Tests: 1.5h
7. PR review + fixes: 0.5h

Total estimate: ~8h (1 day)
Communicate: "Tôi estimate 1.5 ngày để có buffer cho unknowns"

Rule: Estimate * 1.5 cho familiar tasks, * 2 cho unfamiliar
Always include: Review time, testing time, PR iteration
```

---

**Q125. Một microservice liên tục timeout - debug thế nào?**
> **Systematic debugging:**
> 1. **Check service health**: CPU, RAM, threads, connection pool
> 2. **Check downstream**: Service này gọi service nào? DB? External API?
> 3. **Distributed tracing**: Jaeger, Zipkin, AWS X-Ray - trace từng request
> 4. **Timeout config**: Có đang wait quá lâu cho dependency không?
> 5. **Circuit breaker**: Nếu downstream unreliable, fail fast thay vì wait
> 6. **Resource exhaustion**: Thread pool đầy? Connection pool đầy?
```python
# Circuit breaker pattern
from circuitbreaker import circuit

@circuit(failure_threshold=5, recovery_timeout=30)
def call_payment_service(order_id):
    response = requests.post(PAYMENT_URL, json={'order': order_id}, timeout=5)
    return response.json()
# Sau 5 failures: open circuit 30s, fail fast, không wait
```

---

## 💡 CÂU HỎI BẠN NÊN HỎI NGƯỢC LẠI

```
1. "Tech stack hiện tại của team là gì? Có kế hoạch migration không?"
2. "Team làm việc theo quy trình nào? Agile/Scrum hay Kanban?"
3. "Code review process như thế nào?"
4. "Thách thức kỹ thuật lớn nhất team đang đối mặt là gì?"
5. "Cơ hội học hỏi và growth trong vị trí này như thế nào?"
6. "Vị trí này expect deliver gì trong 30/60/90 ngày đầu?"
```

---

## 📊 MA TRẬN CÂU HỎI THEO MỨC ĐỘ

| Level | Chủ đề | Câu hỏi |
|-------|--------|----------|
| 🟢 Dễ | Python basics | Q1-Q10 |
| 🟡 Trung | Flask, DB design | Q11-Q30 |
| 🔴 Khó | System design, MCR | Q31-Q56 |
| 📁 Project | Dự án thực tế | Q48-Q52 |
| 🎯 OOP | OOP & Design Patterns | Q61-Q75 |
| 🔧 Git | Git & CI/CD | Q76-Q85 |
| 🔒 Security | Web Security | Q86-Q95 |
| 🧪 Testing | Testing strategies | Q96-Q105 |
| 🗄️ SQL | SQL nâng cao | Q106-Q115 |
| 💼 Situation | Câu hỏi tình huống | Q116-Q125 |
| ⭐ Behavior | Soft skills | Q57-Q60 |

---

> **📌 Lộ trình ôn tập theo cấp độ:**
> - **Junior**: Q1-Q30, Q61-Q65, Q76-Q80, Q86-Q90, Q96-Q100, Q57-Q60
> - **Middle**: Tất cả phần trên + Q31-Q56, Q66-Q75, Q81-Q85, Q91-Q95, Q101-Q125
