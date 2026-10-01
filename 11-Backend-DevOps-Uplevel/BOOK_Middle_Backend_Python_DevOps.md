# 📘 Cuốn Sách Lộ Trình Middle Backend Developer (Python) / DevOps

> **Mục đích:** Đây là cuốn sách tổng hợp **toàn bộ kiến thức cần ôn lại + cần mở rộng** để đi từ trình độ hiện tại (Fullstack Python với Frappe + Vue) lên **Middle Backend Developer (Python) có kỹ năng DevOps**. Sách **tự đủ (self-contained)** — mỗi chương gồm 4 phần: **Kiến thức cần học** (bullet point, chia theo 3 cấp độ 🟢/🟡/🔴), **Giải thích chi tiết** (vì sao quan trọng, hoạt động thế nào, dễ sai ở đâu — kèm code ví dụ), **📚 Nội dung đầy đủ** (khối thu gọn, bấm để mở — nhúng toàn bộ nội dung gốc từ ~30 tài liệu liên quan trong repo, không cần mở file khác), và **Đọc chi tiết** (link gốc để tra cứu/cập nhật sau này nếu tài liệu nguồn thay đổi).
>
> Dùng cùng với [README.md](README.md) (cách dùng folder) và [00-Lich-Hoc-Toi/Lich_Trinh_Toi_Den_Tet.md](00-Lich-Hoc-Toi/Lich_Trinh_Toi_Den_Tet.md) (lịch học tối 21h-22h/22h30) — sách này là "bản đồ kiến thức + toàn bộ nội dung" gộp làm một, lịch học là "thời gian biểu đọc".
>
> **Mỗi chương chia 3 cấp độ để ôn đúng tốc độ, không học dàn trải:**
> - 🟢 **Cơ bản** — nền tảng phải vững, phần lớn đã biết/chạm qua ở công việc hiện tại, chỉ cần ôn lại cho đúng chuẩn ngành.
> - 🟡 **Nâng cao** — trọng tâm của trình độ Middle, phần lớn kiến thức mới cần học chắc.
> - 🔴 **Chuyên sâu / Thực chiến** — mức phân biệt Middle với Senior: câu hỏi phỏng vấn khó, sự cố thực tế, trade-off cần tư duy sâu hơn là thuộc khái niệm.

---

## 🗺️ Mục lục

**PHẦN I — NỀN TẢNG**
1. [Python Core nâng cao](#chuong-1)
2. [Git nâng cao & Quy trình làm việc chuyên nghiệp](#chuong-2)
3. [Database nền tảng: SQL, NoSQL, Indexing, Transaction](#chuong-3)
4. [Cấu trúc dữ liệu & Giải thuật áp dụng cho Backend](#chuong-4)

**PHẦN II — BACKEND FRAMEWORK**
5. [Django sâu: ORM, Migration, Admin, Middleware, Signal](#chuong-5)
6. [Django REST Framework: API thực chiến](#chuong-6)
7. [Flask & FastAPI: So sánh với Django](#chuong-7)
8. [Testing: Unit, Integration, Mock](#chuong-8)
9. [API Design & Best Practices](#chuong-9)

**PHẦN III — KIẾN TRÚC & VẬN HÀNH HỆ THỐNG**
10. [Request Lifecycle, Concurrency & Async trong Production](#chuong-10)
11. [System Design cơ bản cho Middle](#chuong-11)
12. [Security cơ bản cho Backend](#chuong-12)
13. [Observability: Logging, Monitoring, Debugging Production](#chuong-13)

**PHẦN IV — DEVOPS**
14. [Linux/Shell & Docker](#chuong-14)
15. [CI/CD với GitHub Actions & GitLab CI](#chuong-15)
16. [Cloud: AWS cơ bản & So sánh nhanh GCP](#chuong-16)
17. [Container Orchestration: Kubernetes cơ bản](#chuong-17)
18. [Infrastructure as Code: Terraform, Ansible & GitOps](#chuong-18)
19. [Incident Response & Deployment Strategies](#chuong-19)

**PHẦN V — SẴN SÀNG PHỎNG VẤN & SỰ NGHIỆP**
20. [System Design Interview Playbook](#chuong-20)
21. [Bộ câu hỏi phỏng vấn Junior → Middle](#chuong-21)
22. [Xây Project Portfolio & Kể chuyện STAR](#chuong-22)
23. [Đàm phán lương & Định hướng sự nghiệp](#chuong-23)

---

<a id="chuong-1"></a>
## Chương 1 — Python Core nâng cao

> **Mục tiêu:** code Python ở mức "hiểu vì sao", không chỉ "biết cách dùng".

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- OOP (class, inheritance, composition) — bạn đã dùng qua Frappe DocType, giờ chuẩn hóa lại theo Python thuần (dataclass, property, classmethod/staticmethod).
- Type hinting (`typing`) — ngành đang chuẩn hóa dùng type hint, nên tập thói quen viết từ đầu.

🟡 **Nâng cao (trọng tâm Middle):**
- Decorator, generator/iterator, context manager (`with`) — Frappe ít bắt bạn tự viết decorator, đây là kỹ năng hay bị hỏi khi phỏng vấn Middle.
- `asyncio` cơ bản (coroutine, event loop) — nền cho Chương 10.
- **Design Pattern cơ bản cho Backend**: Factory Pattern, Strategy Pattern, Dependency Injection (DI) — không cần học hết Gang of Four, chỉ cần 2-3 pattern hay gặp nhất khi đọc code Django/FastAPI thực tế.
- **Quản lý dependency & môi trường chuyên nghiệp**: `venv`/`poetry` (khóa version bằng lock file), code style tự động (`black`/`ruff`), type check tĩnh (`mypy`).

🔴 **Chuyên sâu / Thực chiến:**
- GIL, memory model, mutable vs immutable, shallow/deep copy — câu hỏi kinh điển phỏng vấn Middle/Senior Python, dễ trả lời sai nếu chỉ học khái niệm suông.
- **Clean Architecture / Hexagonal Architecture** — tư duy tách business logic ra khỏi framework để dễ test và dễ đổi công nghệ sau này; đây là ranh giới rõ nhất giữa code Middle và code Junior.

**Giải thích chi tiết:**

🟢 *Cơ bản.* **OOP nâng cao (dataclass, property, classmethod/staticmethod).** Frappe đã cho bạn quen với class (DocType), nhưng Python thuần có vài công cụ gọn hơn: `@dataclass` tự sinh `__init__`, `__repr__`, `__eq__` cho class chỉ chứa data — khỏi viết tay; `@property` cho phép gọi `obj.full_name` như thuộc tính nhưng thực chất chạy 1 hàm phía sau (tính toán động, hoặc validate trước khi set); `classmethod` nhận `cls` (dùng để tạo object theo cách khác, VD `User.from_json(...)`), `staticmethod` không nhận `self`/`cls` gì cả (chỉ là hàm tiện ích nằm trong class cho gọn namespace). Dễ sai: dùng `@property` cho phép tính tốn kém (query DB) mà không ai ngờ — người gọi tưởng đọc thuộc tính là rẻ, hóa ra mỗi lần đọc là 1 query.

**Type hinting.** Viết `def get_user(id: int) -> User:` không bắt buộc Python kiểm tra lúc chạy (Python vẫn dynamic typing), nhưng `mypy` (check tĩnh, chạy riêng trước khi deploy) sẽ báo lỗi nếu truyền sai kiểu — bắt lỗi sớm hơn thay vì đợi lỗi lúc chạy production.

🟡 *Nâng cao.* **Decorator, generator/iterator, context manager.** Decorator là 1 hàm bọc quanh hàm khác để thêm hành vi mà không sửa code gốc — VD `@login_required`, `@cache_result`; về bản chất `@foo` trên hàm `bar` tương đương `bar = foo(bar)`. Generator (`yield`) tạo ra giá trị từng cái một thay vì tạo hết list trong RAM cùng lúc — quan trọng khi xử lý file/log hàng triệu dòng, nhưng dễ sai vì generator chỉ duyệt được **1 lần**, duyệt lần 2 sẽ ra rỗng (khác với list). Context manager (`with open(...) as f`) đảm bảo dọn dẹp tài nguyên (đóng file, đóng connection DB, release lock) dù code bên trong có lỗi hay không — tương đương `try/finally` nhưng gọn hơn.

```python
# Decorator — @foo trên bar tương đương bar = foo(bar)
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.3f}s")
        return result
    return wrapper

@log_time
def get_user(id: int) -> User: ...

# Generator — chỉ duyệt được 1 lần
def read_huge_log(path):
    with open(path) as f:          # context manager: tự đóng file dù lỗi hay không
        for line in f:
            yield line.strip()     # trả từng dòng, không load hết file vào RAM
```

Dễ sai: `for line in read_huge_log(...)` chạy lần 2 sẽ ra rỗng — generator đã "dùng hết" sau lần duyệt đầu.

**`asyncio` cơ bản.** `async def` tạo ra 1 coroutine — không chạy ngay, phải `await` hoặc đưa vào event loop mới chạy. Event loop là 1 vòng lặp duy nhất, luân phiên chạy nhiều coroutine, mỗi coroutine **tự nguyện nhường** quyền chạy tại điểm `await` (khác thread, nơi hệ điều hành ép ngắt). Async chỉ có lợi khi code đang **chờ I/O** — nếu code async mà tính toán CPU nặng không `await` ở đâu cả, nó sẽ chặn toàn bộ event loop, làm chậm mọi request khác.

**Design Pattern: Factory, Strategy, Dependency Injection.** Factory Pattern: thay vì gọi `User()` trực tiếp khắp nơi, gọi `UserFactory.create(type)` — nơi quyết định tạo loại User nào được gom về 1 chỗ, dễ đổi logic sau này. Strategy Pattern: đóng gói nhiều cách làm cùng 1 việc (VD nhiều cách tính phí ship) thành các class cùng interface, để đổi thuật toán lúc runtime mà không `if/elif` chằng chịt. Dependency Injection: thay vì 1 class tự tạo dependency của nó (VD tự `self.db = PostgresConnection()`), bạn **truyền** dependency vào từ bên ngoài — lợi ích lớn nhất là dễ test (truyền fake DB khi test) và dễ đổi implementation.

**Quản lý dependency & môi trường.** `requirements.txt` chỉ ghi `django==4.2`, không khóa version của package phụ thuộc gián tiếp, nên 2 máy cài có thể ra 2 bộ package hơi khác nhau ("works on my machine"). `poetry`/`pip-tools` tạo **lock file** ghi chính xác version toàn bộ cây dependency. `black`/`ruff` tự format code theo 1 chuẩn duy nhất (hết tranh cãi style trong code review). `mypy` check type tĩnh như trên.

🔴 *Chuyên sâu/Thực chiến.* **GIL, memory model, mutable/immutable, shallow/deep copy.** GIL (Global Interpreter Lock): tại 1 thời điểm chỉ 1 thread Python được thực thi bytecode — multi-thread Python **không** tăng tốc code CPU-bound (tính toán nặng), chỉ có lợi cho I/O-bound (chờ mạng/DB); đây là lý do Chương 10 phải phân biệt rõ Thread/Process/Async. Mutable (list, dict) đổi được nội dung tại chỗ; immutable (tuple, string, int) thì không — hệ quả: dùng list làm default argument (`def f(x=[])`) là bug kinh điển vì list đó bị **chia sẻ** giữa các lần gọi hàm. Shallow copy chỉ copy lớp ngoài cùng (list con bên trong vẫn là cùng 1 object); deep copy copy toàn bộ xuống tận cùng — `list.copy()` tưởng an toàn nhưng list lồng nhau vẫn bị ảnh hưởng chéo.

```python
# Bug kinh điển: mutable default argument
def add_item(item, cart=[]):   # cart=[] chỉ tạo 1 LẦN DUY NHẤT lúc định nghĩa hàm
    cart.append(item)
    return cart

add_item("apple")   # ['apple']
add_item("banana")  # ['apple', 'banana']  <- bug: cart cũ bị dùng lại, không rỗng!

# Cách đúng:
def add_item(item, cart=None):
    cart = cart if cart is not None else []
    cart.append(item)
    return cart
```

**Clean Architecture / Hexagonal Architecture.** Ý tưởng cốt lõi: **business logic không được phụ thuộc vào framework hay DB**. Framework/DB chỉ là "chi tiết kỹ thuật" nằm ở lớp ngoài, business logic nằm ở lõi trong cùng, giao tiếp qua interface. Lợi ích: đổi Django sang FastAPI, hoặc Postgres sang MongoDB, không phải viết lại logic nghiệp vụ. Đây là khác biệt rõ nhất giữa code Junior ("nhét hết logic vào view") và code Middle ("logic nằm ở service layer riêng, view chỉ gọi service").

**Đọc chi tiết:** [`03-Python-Expert/Python_Core_Mastery.md`](../03-Python-Expert/Python_Core_Mastery.md), bài tập thêm ở [`03-Python-Expert/Python_Mastery_Challenges.md`](../03-Python-Expert/Python_Mastery_Challenges.md). Phần Design Pattern/DI/Clean Architecture: [`03-Python-Expert/Python_Backend_Professional_Guide.md`](../03-Python-Expert/Python_Backend_Professional_Guide.md) mục 4B, 10, 11. Bộ câu hỏi OOP/SOLID/Design Patterns đầy đủ (Q61-75): [`interview_prep/07_Cau_Hoi_Phong_Van.md`](../interview_prep/07_Cau_Hoi_Phong_Van.md).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `03-Python-Expert/Python_Core_Mastery.md`, `03-Python-Expert/Python_Mastery_Challenges.md`, `03-Python-Expert/Python_Backend_Professional_Guide.md` (mục 1, 2, 6, 7, 10, 11), `interview_prep/07_Cau_Hoi_Phong_Van.md` (Q61-75, OOP & Design Patterns).

#### A. List, Dict, Set Comprehension
```python
# List comprehension: Lấy bình phương các số chẵn
nums = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in nums if x % 2 == 0]
# Kết quả: [4, 16, 36]

# Dict comprehension: Biến list thành từ điển ID -> Name
users = [("1", "mbw25"), ("2", "senior")]
user_dict = {uid: name for uid, name in users}
# Kết quả: {"1": "mbw25", "2": "senior"}
```

#### B. Unpacking và *args, **kwargs
```python
def senior_function(*args, **kwargs):
    # args là một tuple chứa các tham số không tên
    # kwargs là một dict chứa các tham số có tên
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
```
- **Hiệu năng:** Comprehensions chạy nhanh hơn vòng lặp `for` thông thường vì được tối ưu ở tầng C-Level.
- **Duy trì:** Viết code trên 1 dòng giúp giảm "độ loãng" của file, đồng nghiệp nắm logic nhanh hơn.
- **Linh hoạt:** `*args/**kwargs` cho phép viết hàm Wrapper/Decorator cực mạnh mà không cần biết hàm gốc nhận bao nhiêu tham số.

#### B2. Syntactic Sugar — so sánh Junior vs Senior
Comprehension — Junior viết 5 dòng, Senior viết 1 dòng mà vẫn dễ đọc:
```python
# Junior:
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)

# Senior:
squares = [x**2 for x in range(10) if x % 2 == 0]
```
Merge dictionaries (Python 3.9+) — dùng toán tử `|` thay vì `.update()`:
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # {"a": 1, "b": 3, "c": 4}
```
F-Strings formatting (số thập phân, phân tách hàng nghìn):
```python
price = 1200.5678
print(f"Giá sản phẩm: {price:,.2f} VNĐ")  # 1,200.57 VNĐ
```

#### C. OOP — class, property, kế thừa
```python
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property  # Biến hàm thành thuộc tính (chỉ đọc)
    def salary_info(self):
        return f"Employee {self._name} has salary {self._salary}"

class Manager(Employee):
    def get_role(self):
        return "Admin Manager"
```

#### D. Decorators
```python
import time

def timer_decorator(func):
    """Decorator đo thời gian chạy của hàm"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Hàm {func.__name__} chạy mất: {end-start}s")
        return result
    return wrapper

@timer_decorator
def complex_task():
    time.sleep(1)
```
- **Tái sử dụng:** Decorators cho phép "cấy" các tính năng như Logging, Auth, Caching vào hàng trăm hàm chỉ bằng 1 dòng code — đỉnh cao của DRY.

#### E. Context Managers (`with` statement)
```python
class DatabaseConnection:
    """Tự động đóng kết nối sau khi dùng xong"""
    def __enter__(self):
        print("Mở kết nối tới Database...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Đóng kết nối an toàn.")
```
- **An toàn:** Context Managers đảm bảo file/kết nối DB luôn được đóng kể cả khi có lỗi — cách senior ngăn Memory Leak.

#### F. AsyncIO cơ bản
```python
import asyncio

async def fetch_data(id):
    print(f"Bắt đầu lấy dữ liệu {id}...")
    await asyncio.sleep(2)  # Giả lập chờ API
    return f"Data {id} xong!"

async def main():
    results = await asyncio.gather(fetch_data(1), fetch_data(2))
    print(results)
```
- **Khả năng mở rộng:** AsyncIO là sự khác biệt giữa hệ thống phục vụ 100 người và 100,000 người.

#### G. Magic Methods (Dunder)
```python
class SuperList:
    def __init__(self, items):
        self.items = items

    def __call__(self):
        """Làm cho class có thể gọi như hàm: super_list()"""
        return f"Danh sách đang có {len(self.items)} phần tử"

    def __getitem__(self, index):
        """Giúp class truy cập bằng index: obj[0]"""
        return f"Phần tử thứ {index} là: {self.items[index]}"
```

#### H. Functional Magic — hàm hỗ trợ cực mạnh

| Hàm | Ý nghĩa | Ví dụ thực tế |
|---|---|---|
| `enumerate()` | Lấy cả index và giá trị | `for idx, val in enumerate(users): ...` |
| `zip()` | Kết hợp 2 mảng đồng thời | `for name, age in zip(names, ages): ...` |
| `any()` / `all()` | Kiểm tra điều kiện gộp | `if all(user.is_active for user in users): ...` |
| `lambda` | Hàm ẩn danh siêu nhanh | `sorted_data = sorted(data, key=lambda x: x['price'])` |

#### I. Python Internals — từ Code đến CPU
1. **Source Code (.py)** → Compiler.
2. **Bytecode (.pyc)**: Python chuyển code thành các lệnh trung gian.
3. **Python Virtual Machine (PVM)**: Chạy Bytecode trên CPU.

**GIL (Global Interpreter Lock)** — "Nút thắt cổ chai": tại 1 thời điểm chỉ 1 Thread chạy Bytecode → Python không chạy song song (Parallel) 2 tác vụ CPU nặng trên đa nhân → giải pháp: dùng **Multiprocessing** (mỗi process có 1 GIL riêng).

#### J. Metaprogramming
```python
def retry(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            try: return func(*args, **kwargs)
            except: pass
        return None
    return wrapper
```
`__call__` biến 1 Class thành có thể gọi được (`obj()`); `__getattr__` xử lý khi gọi thuộc tính không tồn tại — ứng dụng mạnh trong Dynamic API.

#### K. Clean Architecture (Hexagonal)
Chia code thành các lớp: **Entities** (Class Python thuần, VD `User`, `Order`) → **Use Cases** (logic ứng dụng, VD `CreateOrder`) → **Infrastructure** (nơi gọi Database, AWS S3, Email). Ưu điểm: đổi từ RDS sang MongoDB chỉ cần sửa lớp Infrastructure, lớp Nghiệp vụ không đổi.

#### L. Design Patterns
```python
# Factory Pattern — tạo nhiều loại Report (PDF, CSV, Excel)
class ReportFactory:
    @staticmethod
    def get_report(format_type):
        if format_type == "PDF": return PDFReport()
        if format_type == "CSV": return CSVReport()

# Strategy Pattern — nhiều cách xử lý cùng 1 vấn đề (Stripe, Paypal, MoMo)
def process_payment(payment_strategy: PaymentStrategy, amount: float):
    return payment_strategy.pay(amount)
```

#### L2. SOLID principles
**S**ingle Responsibility (1 class chỉ 1 lý do để thay đổi) · **O**pen/Closed (mở rộng được, không sửa code cũ) · **L**iskov Substitution (subclass thay thế được superclass mà không break behavior) · **I**nterface Segregation (nhiều interface nhỏ thay vì 1 interface lớn) · **D**ependency Inversion (phụ thuộc vào abstraction, không phụ thuộc vào implementation cụ thể).
```python
# Vi phạm SRP: 1 class làm quá nhiều việc
class UserManager:
    def create_user(self): ...
    def send_email(self): ...   # nên tách ra EmailService
    def save_to_db(self): ...   # nên tách ra UserRepository

# Tuân thủ OCP: thêm platform mới không sửa code cũ
class BaseConnector:
    def fetch_products(self): raise NotImplementedError

class ShopifyConnector(BaseConnector):
    def fetch_products(self): ...  # override, không sửa BaseConnector
```

#### L3. Abstract class vs Protocol, `__slots__`, Composition vs Inheritance
```python
from abc import ABC, abstractmethod
from typing import Protocol

class BaseConnector(ABC):
    def authenticate(self): return self._get_token()      # shared implementation
    @abstractmethod
    def fetch_products(self) -> list: ...                  # bắt buộc override

class Fetchable(Protocol):           # duck typing — không cần kế thừa
    def fetch_products(self) -> list: ...
```
Dùng **Abstract class** khi các subclass có code dùng chung; dùng **Protocol** khi chỉ cần định nghĩa hợp đồng (contract) mà không muốn ép kế thừa.
```python
class Point:
    __slots__ = ['x', 'y']   # chỉ cho phép đúng 2 attribute, không tạo __dict__
    def __init__(self, x, y):
        self.x, self.y = x, y
```
`__slots__` tiết kiệm ~40-50% RAM và truy cập attribute nhanh hơn — dùng khi tạo hàng triệu object (trading, game, parser); đánh đổi: không thể gán attribute động.

**"Favor composition over inheritance"** (Gang of Four): Inheritance là quan hệ "is-a" (Dog IS-A Animal); Composition là quan hệ "has-a" (Car HAS-A Engine). Kế thừa sâu nhiều tầng dễ tạo "fragile base class" (sửa lớp cha làm hỏng lớp con ở xa) và tight coupling — composition linh hoạt hơn vì có thể đổi "linh kiện" lúc runtime.

#### L4. Singleton, Observer, Decorator Pattern, Repository, Dependency Injection
```python
# Singleton — thread-safe, nhưng khó test (global state) nên cân nhắc DI thay thế
class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

# Observer/pub-sub — 1 sự kiện, nhiều listener độc lập
class EventEmitter:
    def __init__(self):
        self._listeners = defaultdict(list)
    def on(self, event, callback):
        self._listeners[event].append(callback)
    def emit(self, event, data=None):
        for cb in self._listeners[event]:
            cb(data)
# Ứng dụng: WebSocket events, Django signals, React state management

# Decorator Pattern (GoF) — bọc object để thêm hành vi, khác @decorator của Python
class CachedConnector:
    def __init__(self, connector):
        self._connector, self._cache = connector, {}
    def fetch_products(self):
        if 'products' not in self._cache:
            self._cache['products'] = self._connector.fetch_products()
        return self._cache['products']

# Repository Pattern — tách business logic khỏi data access, dễ test/swap DB
class UserRepository:
    def __init__(self, db_session): self.db = db_session
    def find_by_id(self, user_id): return self.db.query(User).filter_by(id=user_id).first()
    def save(self, user): self.db.add(user); self.db.commit(); return user

# Dependency Injection — truyền dependency từ ngoài vào thay vì tự tạo bên trong
class OrderService:
    def __init__(self, repo: OrderRepository, notifier: Notifier):
        self.repo, self.notifier = repo, notifier   # inject được mock khi test
```
**MVC vs MVP vs MVVM:** MVC (Flask/Django) — Controller cập nhật Model, View đọc Model trực tiếp. MVP — Presenter làm trung gian giữa View và Model, View hoàn toàn thụ động. MVVM (Vue/React+MobX) — ViewModel expose data stream, View tự bind theo dõi thay đổi.

**Event-driven architecture:** các thành phần giao tiếp qua event thay vì gọi trực tiếp nhau — VD `user_registered` → trigger song song `send_welcome_email`, `create_profile`, `notify_admin`; công cụ: Celery+Redis/RabbitMQ, Kafka, AWS EventBridge.

**Anti-pattern cần tránh:** God Object (1 class ôm hết, vi phạm SRP); Spaghetti Code (logic không có cấu trúc); Copy-paste programming (vi phạm DRY, sửa bug phải sửa nhiều chỗ); Premature Optimization (tối ưu trước khi có bottleneck thật); Magic Numbers (hardcode số vô nghĩa thay vì named constant); Callback Hell (nested callback sâu — dùng Promise/async-await thay thế).

#### M. Bài tập rèn luyện theo Tier (Python Mastery Challenges)

**🟢 Tier 1 — Foundation:** Palindrome Checker (string slicing, two-pointers), Frequency Dictionary (`collections.Counter`), Basic CRUD with JSON (file I/O, try-except), Prime Number Generator (generator). LeetCode: Two Sum, Valid Parentheses.

**🟡 Tier 2 — Advanced Logic & DS:** Custom Decorator `@audit_log` (`functools.wraps`), tự xây LRU Cache (Linked List + Dictionary, không dùng `functools.lru_cache`), Directory Tree Walker (đệ quy, `pathlib`), Sudoku Solver (Backtracking). LeetCode: Longest Substring Without Repeating Characters, Merge Intervals.

**🔴 Tier 3 — Concurrency & Optimization:** Async Web Scraper (`httpx`/`aiohttp`, 50 trang cùng lúc), Image Processor bằng `multiprocessing.Pool` (vượt GIL), Memory-Efficient Scanner (generator đọc file log GB không tràn RAM), Trie cho Autocomplete. LeetCode: Trapping Rain Water, Course Schedule.

**👑 Tier 4 — Expert & Architect:** Distributed Rate Limiter dùng Redis (sliding window), Custom ORM Mockup (Metaclass, `__getattr__`), Message Queue Worker (RabbitMQ/Redis Streams, retry logic), Plugin System (hot-reload qua `importlib`). LeetCode: Median of Two Sorted Arrays, Shortest Path in a Grid with Obstacles Elimination.

**Lời khuyên tiến bộ nhanh:** viết Unit Test cho mọi hàm (`pytest`); sau khi giải xong, so sánh độ phức tạp Time/Space với giải pháp người khác; viết Docstring chuẩn từ Tier 2 trở lên.

</details>

---

<a id="chuong-2"></a>
## Chương 2 — Git nâng cao & Quy trình làm việc chuyên nghiệp

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Git cơ bản (commit, branch, merge) — đã dùng hàng ngày.
- Commit message convention (Conventional Commits: `feat:`, `fix:`, `chore:`...).

🟡 **Nâng cao (trọng tâm Middle):**
- `rebase` vs `merge` — khi nào dùng loại nào, vì sao không rebase nhánh đã chia sẻ.
- Pre-commit hook (lint/test tự động trước khi commit).
- Quy trình PR chuẩn: code review checklist, squash vs preserve history.
- **Git workflow**: Git Flow (feature/develop/release/hotfix/main) vs Trunk-Based Development — Trunk-Based phổ biến hơn trong CI/CD hiện đại.

🔴 **Chuyên sâu / Thực chiến:**
- `git bisect` (tìm chính xác commit gây lỗi giữa hàng trăm commit), `cherry-pick` (lấy đúng 1 commit từ nhánh khác), `reflog` (cứu commit tưởng đã mất) — kỹ năng "cứu hỏa" ít dùng hàng ngày nhưng cực giá trị khi sự cố thật xảy ra.

**Giải thích chi tiết:**

🟢 *Cơ bản.* **Conventional Commits.** `feat:`, `fix:`, `chore:`... giúp tự sinh changelog và biết ngay loại thay đổi mà không cần đọc diff — thói quen nhỏ nhưng chuẩn hóa cách cả team đọc lịch sử Git.

🟡 *Nâng cao.* **`rebase` vs `merge`.** `merge` tạo thêm 1 commit "nối" 2 nhánh, giữ nguyên lịch sử thật (kể cả lộn xộn). `rebase` viết lại lịch sử bằng cách "đặt lại" các commit của nhánh bạn lên trên đầu nhánh chính — lịch sử thẳng, dễ đọc hơn, nhưng **không rebase nhánh đã push lên chung với người khác** vì sẽ làm commit hash đổi hết, gây xung đột lịch sử cho đồng đội.

**Pre-commit hook.** Script tự chạy **trước khi** commit được tạo (lint, format, chạy test nhanh) — chặn code lỗi/không đúng chuẩn trước khi nó vào lịch sử Git, thay vì để CI/CD phát hiện muộn hơn.

**Quy trình PR chuẩn.** Squash (gộp nhiều commit nháp thành 1 commit sạch khi merge) phù hợp khi lịch sử nháp không có giá trị; giữ nguyên lịch sử (merge commit) phù hợp khi mỗi commit đã có ý nghĩa riêng cần tra cứu sau này.

**Git Flow vs Trunk-Based Development.** Git Flow tách nhiều nhánh dài hạn (`develop`, `release`, `hotfix`) — rõ ràng nhưng nặng nề, dễ bị merge conflict lớn khi nhánh feature sống quá lâu. Trunk-Based Development: mọi người commit thẳng (hoặc qua PR rất ngắn ngày) vào 1 nhánh chính (`main`/`trunk`), dùng **feature flag** để ẩn tính năng chưa hoàn thiện thay vì giữ nhánh riêng — phù hợp hơn với CI/CD chạy liên tục vì luôn có 1 nhánh chính deploy-được, đây cũng là lý do hầu hết công ty áp dụng CI/CD hiện đại (Chương 15) đều nghiêng về Trunk-Based.

🔴 *Chuyên sâu/Thực chiến.* **`git bisect`.** Khi biết "commit A chạy đúng, commit Z đang lỗi" nhưng không biết lỗi bắt đầu từ đâu giữa hàng trăm commit — `git bisect` tự động chia đôi để tìm (binary search trên lịch sử commit), bạn chỉ cần trả lời "tốt" hay "lỗi" ở mỗi bước.

```bash
git bisect start
git bisect bad HEAD           # commit hiện tại đang lỗi
git bisect good v1.2.0        # tag/commit này từng chạy đúng
# Git tự checkout commit giữa khoảng good-bad -> bạn test rồi:
git bisect good               # hoặc: git bisect bad
# lặp lại tới khi Git chỉ đúng commit gây lỗi, rồi:
git bisect reset
```

**`cherry-pick`, `reflog`.** `cherry-pick` lấy đúng 1 commit từ nhánh khác áp vào nhánh hiện tại (không cần merge cả nhánh). `reflog` là "nhật ký mọi thứ HEAD từng trỏ tới" — cứu cánh khi lỡ `reset --hard` mất commit: commit vẫn còn trong Git, chỉ là không còn nhánh nào trỏ tới, `reflog` giúp tìm lại.

```bash
git cherry-pick a1b2c3d        # áp đúng 1 commit hotfix từ main sang release branch

git reset --hard HEAD~3        # lỡ tay mất 3 commit gần nhất
git reflog                     # xem lại mọi vị trí HEAD từng trỏ tới, tìm commit bị mất
git reset --hard a1b2c3d       # quay lại đúng commit vừa tìm thấy trong reflog
```

**Đọc chi tiết:** [`10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md`](../10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md) — Học phần Git nâng cao.
**Bài tập:** Exercise DO (xem [`03-DevOps-Exercises/Checklist_Bai_Tap.md`](03-DevOps-Exercises/Checklist_Bai_Tap.md)), mục "tự gây sự cố rồi dùng `git bisect` để tìm".

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md` (Học phần 5), `interview_prep/05_Docker_DevOps.md` (mục 5), `interview_prep/07_Cau_Hoi_Phong_Van.md` (Q76-85).

#### Cơ bản
Khái niệm Working Directory – Staging Area – Repository. Lệnh nền tảng: `init, clone, add, commit, status, log, diff`. Branch: `branch, checkout/switch, merge`. Remote: `push, pull, fetch`, `.gitignore`.

#### Git hooks & Semantic commit
Git hooks (`pre-commit`, `pre-push`) tự động lint/test trước khi commit. Semantic commit message (Conventional Commits) để tự động generate changelog/version.

```bash
git checkout -b feature/user-authentication
git add -p                          # interactive staging theo hunks
git commit -m "feat(auth): add JWT authentication

- Implement login/logout endpoints
- Add JWT token generation with claims
- Add @jwt_required decorator for protected routes
- Write tests for auth flow

Closes #123"

git push origin feature/user-authentication
# → Create Pull Request → Code Review → Merge

git log --oneline --graph --all     # visual branch history
git stash                           # tạm thời save changes
git stash pop                       # restore stashed changes
```

```
feat:     New feature
fix:      Bug fix
docs:     Documentation
style:    Formatting (no logic change)
refactor: Code restructure
test:     Add/fix tests
chore:    Build tools, dependencies
perf:     Performance improvements

Format: type(scope): description
feat(auth): add JWT refresh token endpoint
fix(migration): resolve MariaDB driver compatibility
chore(docker): optimize Dockerfile layer cache
```

#### Semantic Versioning (SemVer)
**MAJOR.MINOR.PATCH** (ví dụ: 2.4.1) — PATCH (bug fix, backward compatible), MINOR (new feature, backward compatible), MAJOR (breaking changes). Pre-release: `1.0.0-alpha.1`, `1.0.0-beta.2`, `1.0.0-rc.1`.

#### Lab thực chiến (Học phần 5 — GITS)
1. Mô phỏng 2 người cùng sửa 1 file, tạo conflict thật, thực hành resolve bằng cả `merge` và `rebase`, so sánh lịch sử commit (`git log --graph`).
2. Setup pre-commit hook chạy `lint` + `test` tự động trước khi cho phép commit.
3. Dùng `git bisect` để tìm ra commit nào làm hỏng 1 test case trong repo demo.

#### Sự cố thường gặp (Git)
- **`detached HEAD`** — checkout nhầm vào 1 commit thay vì branch, commit tiếp bị "mồ côi" nếu không tạo branch mới kịp thời.
- **Force push làm mất commit của đồng nghiệp** — luôn ưu tiên `git push --force-with-lease` thay vì `--force`.
- **Merge conflict lặp lại nhiều lần trên cùng 1 branch dài ngày** — dấu hiệu branch sống quá lâu, nên áp dụng Trunk-Based + feature flag thay vì giữ branch feature hàng tuần.
- **Commit nhầm secret (API key, `.env`)** — cần `git filter-repo` hoặc BFG Repo-Cleaner để xóa khỏi lịch sử, đồng thời **revoke key ngay lập tức** (xóa khỏi git chưa đủ, key đã lộ coi như "cháy").
- **`fatal: refusing to merge unrelated histories`** — khi merge 2 repo tách biệt, cần cờ `--allow-unrelated-histories` và hiểu rõ hệ quả.

#### `.gitignore` — những gì cần ignore
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

# IDE
.vscode/settings.json
.idea/

# OS
.DS_Store

# Docker local overrides
docker-compose.override.yml
```

#### Code review — checklist
✅ Logic đúng không? Edge cases được handle? ✅ Tests đủ chưa? ✅ Security: SQL injection, XSS, hardcoded secrets? ✅ Performance: N+1 queries? ✅ Naming rõ nghĩa? ✅ DRY? ✅ Error handling đúng chỗ? ✅ Documentation cho logic phức tạp?

#### Sự cố thường gặp (Học phần 5)
- **`detached HEAD`** — checkout nhầm vào 1 commit thay vì branch, commit tiếp bị "mồ côi" nếu không tạo branch mới kịp thời.
- **Force push làm mất commit của đồng nghiệp** — luôn ưu tiên `git push --force-with-lease` thay vì `--force`.
- **Merge conflict lặp lại nhiều lần trên cùng 1 branch dài ngày** — dấu hiệu branch sống quá lâu, nên áp dụng Trunk-Based + feature flag.
- **Commit nhầm secret (API key, `.env`)** — cần `git filter-repo` hoặc BFG Repo-Cleaner để xóa khỏi lịch sử, đồng thời **revoke key ngay lập tức**.
- **`fatal: refusing to merge unrelated histories`** — khi merge 2 repo tách biệt, cần cờ `--allow-unrelated-histories`.

#### Team member commit thẳng vào main gây bug — xử lý
**Technical:** `git revert <commit>` (không xóa history, an toàn hơn `git reset`) → deploy revert ngay → verify production. **Process (ngăn lần sau):** bật branch protection trên main, yêu cầu PR + Code Review, yêu cầu CI checks pass, viết blameless postmortem. **Communication:** không blame cá nhân, focus vào cải thiện quy trình.

</details>

---

<a id="chuong-3"></a>
## Chương 3 — Database nền tảng: SQL, NoSQL, Indexing, Transaction

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Viết query SQL cơ bản, hiểu bảng/quan hệ — đã quen qua Frappe (dùng MariaDB).
- PostgreSQL (khác MySQL/MariaDB ở JSONB, CTE, window function) vì hầu hết công ty Backend Python dùng PostgreSQL.
- **Backup & Restore** định kỳ (`pg_dump`/snapshot) — việc đầu tiên phải có trước khi "chơi lớn" với DB production.
- **NoSQL cơ bản (MongoDB)**: document vs table, schema-less — CRUD không khác nhiều so với SQL, chỉ đổi tư duy lưu trữ.

🟡 **Nâng cao (trọng tâm Middle):**
- **Index**: B-Tree index, composite index, khi nào index làm chậm write.
- **Normalization vs Denormalization** — khi nào nên phá chuẩn để tăng tốc đọc.
- `EXPLAIN ANALYZE` — đọc execution plan để tìm query chậm.
- **Khung quyết định SQL vs NoSQL** — câu hỏi đúng cần tự hỏi trước khi chọn, không phải chỉ dựa vào "dữ liệu có cấu trúc hay không".
- **MongoDB: Embedding vs Referencing** — tương đương câu hỏi Normalization vs Denormalization nhưng ở thế giới document.
- **Connection Pooling** — vì sao mỗi request không nên tự tạo connection DB mới (tốn ~5MB RAM + 100ms để thiết lập 1 connection).

🔴 **Chuyên sâu / Thực chiến:**
- **Transaction & Isolation level** (Read Committed, Repeatable Read, Serializable) — hiểu race condition, deadlock, và cách lock xử lý.
- **Replication** (primary-replica) để scale read — luôn là bước thử trước; **Sharding** chỉ là phương án cuối cùng khi replication không còn đủ.
- **Polyglot persistence** — dùng nhiều loại DB khác nhau cho đúng từng bài toán trong cùng 1 hệ thống, thay vì cố nhét mọi thứ vào 1 loại DB duy nhất.
- **Zero-downtime migration** — thêm/sửa cột trên bảng production triệu dòng mà không gây downtime hay breaking app cũ.

**Giải thích chi tiết:**

🟢 *Cơ bản.* **Backup & Restore.** Backup (`pg_dump` hoặc snapshot ổ đĩa) là việc đầu tiên phải có — không có backup thì không có "production" thực sự, chỉ là đang đùa với dữ liệu thật.

**NoSQL cơ bản (MongoDB).** Thay vì bảng với cột cố định, MongoDB lưu dữ liệu dạng **document** (giống JSON) trong 1 collection — các document trong cùng collection có thể có field khác nhau (schema-less), không cần `ALTER TABLE` mỗi khi thêm field mới như SQL. CRUD cơ bản gần giống SQL về tư duy (insert/find/update/delete), chỉ khác cú pháp — người đã quen SQL học MongoDB nhanh hơn người học từ đầu.

🟡 *Nâng cao.* **Index — B-Tree, composite index.** Không có index, tìm 1 dòng giữa 10 triệu dòng = quét hết bảng (full table scan, O(n)). Index giống mục lục cuối sách — tạo sẵn 1 cấu trúc (thường là B-Tree) sắp xếp theo cột được index, tìm theo cột đó nhanh gần O(log n). Composite index (index trên nhiều cột cùng lúc, VD `(user_id, created_at)`) chỉ tăng tốc khi query lọc **đúng thứ tự cột từ trái sang** — lọc theo `created_at` một mình sẽ không dùng được index này. Dễ sai: index làm **chậm write** (mỗi lần INSERT/UPDATE phải cập nhật thêm cấu trúc index) — không phải "thêm index là luôn tốt", mà là đánh đổi tốc độ đọc lấy tốc độ ghi.

**Normalization vs Denormalization.** Chuẩn hóa tách dữ liệu thành nhiều bảng để tránh trùng lặp; đọc cần JOIN nhiều bảng → chậm hơn ở hệ thống đọc nhiều. Denormalization (phá chuẩn có chủ đích) lưu trùng lặp 1 phần dữ liệu để đọc nhanh hơn, đánh đổi lấy việc phải đồng bộ dữ liệu trùng khi update — chỉ nên làm khi đã đo được bottleneck thật.

**`EXPLAIN ANALYZE`.** Lệnh yêu cầu DB giải thích **kế hoạch thực thi thật** của 1 query — có dùng index không, quét bao nhiêu dòng, tốn bao nhiêu thời gian ở từng bước. Công cụ số 1 để trả lời "tại sao query này chậm" thay vì đoán mò.

**Khung quyết định SQL vs NoSQL.** Câu trả lời sách vở "SQL cho dữ liệu có cấu trúc, NoSQL cho dữ liệu linh hoạt" không đủ để quyết định thật — cần tự hỏi: Có cần transaction đa bảng (chuyển tiền, đặt hàng trừ kho) không → cần ACID thật thì chọn PostgreSQL. Schema có đổi liên tục theo từng khách hàng (multi-tenant SaaS linh hoạt) không → nghiêng về MongoDB. Tỷ lệ ghi rất nhiều, ít join (log, event, IoT) không → nghiêng về MongoDB/Cassandra. Có cần full-text search/join nhiều bảng báo cáo phức tạp không → nghiêng về PostgreSQL.

**MongoDB: Embedding vs Referencing.** Embedding (nhúng dữ liệu con trực tiếp vào document cha, VD nhúng danh sách comment vào bài post) đọc nhanh (1 query lấy hết) nhưng document phình to và khó update riêng lẻ phần nhúng. Referencing (lưu `_id` tham chiếu sang collection khác, giống Foreign Key) giữ document gọn nhưng phải query thêm (giống JOIN, dù Mongo không có JOIN thật mạnh như SQL) — đây chính là bài toán Normalization vs Denormalization (đã học ở trên) nhưng dưới hình hài khác.

**Connection Pooling.** Mỗi lần mở 1 connection DB mới tốn khoảng 5MB RAM và ~100ms để thiết lập (bắt tay TCP + xác thực) — nếu mỗi request tự mở/đóng connection riêng, server vừa chậm vừa dễ hết connection khi tải cao ("too many connections"). Connection pool giữ sẵn 1 lượng connection đã mở (`pool_size`), request chỉ "mượn" rồi "trả lại" pool thay vì tạo mới:

```python
engine = create_engine(
    DATABASE_URL,
    pool_size=10,       # connection duy trì sẵn
    max_overflow=20,    # connection thêm khi pool đầy
    pool_timeout=30,    # giây chờ trước khi raise exception
    pool_recycle=3600,  # tự đóng connection cũ sau 1h, tránh bị DB timeout
    pool_pre_ping=True, # kiểm tra connection còn sống trước khi dùng
)
```

Khi số lượng app server tăng lên nhiều (VD chạy trên K8s với nhiều Pod), tổng connection từ tất cả Pod cộng lại có thể vượt giới hạn DB cho phép — lúc đó cần thêm **PgBouncer** (external pooler đứng giữa app và DB) để gộp hàng nghìn connection từ app xuống còn vài chục connection thật tới Postgres.

**Sự cố thật hay gặp:** Postgres mặc định `max_connections = 100`. Deploy nhiều instance app (auto-scaling) mà mỗi instance mở pool riêng — VD pool size 20 × 10 instance = 200 connection — sẽ **vượt giới hạn DB**, gây lỗi `"too many connections"` làm sập **toàn bộ** hệ thống, kể cả khi CPU/RAM của DB vẫn còn dư thừa. Luôn tính: `số instance × pool size mỗi instance ≤ max_connections DB - buffer cho admin/migration`. Set `pool_timeout` hợp lý — request chờ connection quá lâu nên fail nhanh (fail-fast) thay vì xếp hàng vô hạn làm nghẽn toàn hệ thống.

🔴 *Chuyên sâu/Thực chiến.* **Transaction & Isolation Level.** Transaction đảm bảo tính chất ACID — nhóm nhiều câu lệnh SQL thành 1 khối "tất cả thành công hoặc tất cả thất bại". Isolation level quyết định 2 transaction chạy song song nhìn thấy dữ liệu của nhau tới mức nào: `Read Committed` (mặc định ở Postgres) chỉ thấy dữ liệu đã commit, nhưng đọc 2 lần trong cùng transaction có thể ra kết quả khác nhau nếu ai đó commit ở giữa; `Repeatable Read` trong 1 transaction đọc lại luôn ra cùng kết quả; `Serializable` chặt nhất, giả lập như các transaction chạy tuần tự — an toàn nhất nhưng dễ bị **deadlock** (2 transaction cùng khóa chéo nhau, cả hai cùng chờ, phải có 1 cái bị DB hủy).

**Replication, Sharding.** Replication: 1 DB chính (primary, nhận write) đồng bộ dữ liệu sang 1+ bản sao (replica, chỉ đọc) — vừa tăng khả năng chịu lỗi, vừa san tải đọc sang replica. Sharding: chia dữ liệu theo 1 khóa (VD `user_id % N`) ra nhiều DB vật lý riêng biệt — chỉ làm khi đã hết cách scale bằng replication, vì sharding khiến JOIN giữa các shard gần như bất khả thi và vận hành phức tạp hơn hẳn. MongoDB có **Replica Set** (tương đương Replication) và hỗ trợ Sharding sẵn trong engine — dễ scale ghi hơn Postgres ở quy mô cực lớn, đánh đổi lấy việc mất transaction đa document mạnh như SQL.

**Polyglot persistence.** Thực tế senior hay gặp nhất không phải chọn 1 DB duy nhất cho toàn hệ thống, mà là dùng **nhiều công cụ khác nhau cho đúng bài toán**: PostgreSQL cho dữ liệu giao dịch lõi (cần ACID), Redis cho cache/session (Chương 11), Elasticsearch cho full-text search, MongoDB cho dữ liệu schema linh hoạt (log, config người dùng), S3 cho file lớn — mỗi công cụ giải quyết đúng 1 bài toán nó mạnh nhất, thay vì cố ép 1 loại DB làm mọi việc.

**Zero-downtime migration.** Thêm 1 cột `NOT NULL` trực tiếp vào bảng đang có hàng triệu dòng sẽ khóa bảng trong lúc migration chạy (downtime thật) — cách an toàn là chia nhỏ thành 3 bước triển khai riêng: (1) thêm cột ở dạng **nullable** trước (không breaking, không khóa bảng lâu), (2) chạy job riêng để populate dữ liệu cho cột mới (batch, không chạy 1 câu UPDATE khổng lồ), (3) chỉ thêm ràng buộc `NOT NULL` sau khi toàn bộ dữ liệu đã có giá trị. Nguy hiểm nhất là `DROP COLUMN`/`RENAME COLUMN` — app phiên bản cũ (đang chạy song song lúc rolling update, liên hệ Chương 19) sẽ lập tức lỗi vì vẫn tham chiếu tên cột cũ; luôn deploy theo thứ tự "app đọc được cả 2 dạng cũ+mới" trước, rồi mới xóa cột cũ ở lần deploy sau.

**Đọc chi tiết:** [`04-Database-Mastery/PostgreSQL_Expert_Guide.md`](../04-Database-Mastery/PostgreSQL_Expert_Guide.md), NoSQL: [`04-Database-Mastery/MongoDB_Expert_Guide.md`](../04-Database-Mastery/MongoDB_Expert_Guide.md), và phần DB scaling + khung quyết định SQL vs NoSQL ở [`Mastery/Backend-Mastery/03-Database-Choice-And-Scaling-Playbook`](../Mastery/Backend-Mastery/03-Database-Choice-And-Scaling-Playbook) mục 1 và 4. Connection Pooling (SQLAlchemy pool config, PgBouncer) và Zero-downtime migration (Alembic strategy): [`interview_prep/07_Cau_Hoi_Phong_Van.md`](../interview_prep/07_Cau_Hoi_Phong_Van.md) — phần Database & SQL nâng cao (Q83, Q115).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `04-Database-Mastery/PostgreSQL_Expert_Guide.md`, `04-Database-Mastery/MongoDB_Expert_Guide.md`, `interview_prep/03_Database.md`, `Mastery/Backend-Mastery/03-Database-Choice-And-Scaling-Playbook/README.md`.

#### Chuẩn hóa & Ràng buộc (Constraints)
**1NF, 2NF, 3NF:** đảm bảo không có dữ liệu dư thừa. Senior chấp nhận dư thừa dữ liệu ở 1 số bảng (phi chuẩn hóa) để tăng tốc Đọc cho báo cáo khổng lồ. **Check Constraint** (VD `CHECK (age > 18)`) bảo vệ logic nghiệp vụ ngay từ tầng DB. **Unique Constraint** đảm bảo không trùng lặp.

#### Index trong PostgreSQL
- **B-Tree:** mặc định, phổ biến nhất, dùng cho `=`, `>`, `<`.
- **GIN:** chìa khóa cho Full Text Search và dữ liệu JSONB.
- **BRIN:** dùng cho bảng khổng lồ (hàng tỷ dòng) sắp xếp theo thời gian.
- **Partial index:** `CREATE INDEX idx_active_users ON users(email) WHERE is_active = true;`

```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123 AND status = 'pending';
-- Seq Scan → BAD (đọc toàn bộ bảng, thiếu index)
-- Index Scan → GOOD (dùng index)
-- Index Only Scan → BEST (không cần đọc heap)
```

#### Full Text Search & Bitmap Index Scan (Postgres)
Thay vì `LIKE '%keyword%'` (quét toàn bảng, rất chậm), dùng `tsvector`/`tsquery` để tìm kiếm từ khóa trong tích tắc:
```sql
CREATE INDEX idx_posts_content_fts ON posts USING GIN(to_tsvector('english', content));
SELECT * FROM posts WHERE to_tsvector('english', content) @@ to_tsquery('postgres & index');
```
**Bitmap Index Scan:** khi query cần kết hợp nhiều index cùng lúc (VD `WHERE status = 'pending' AND category_id = 5`, mỗi điều kiện có index riêng), Postgres gộp kết quả nhiều index trước khi đọc dữ liệu thật — nhanh hơn Seq Scan nhưng chậm hơn 1 Index Scan đơn thuần.

#### Query Tuning — tránh `IN` với danh sách lớn
```sql
-- Chậm khi danh sách lớn
SELECT * FROM orders WHERE user_id IN (SELECT id FROM users WHERE is_vip = true);
-- Nhanh hơn — dùng EXISTS hoặc JOIN
SELECT * FROM orders o WHERE EXISTS (SELECT 1 FROM users u WHERE u.id = o.user_id AND u.is_vip = true);
```

#### JOINs — loại và khi nào dùng
```sql
-- INNER JOIN: chỉ lấy records có match ở CẢ HAI bảng
SELECT u.name, o.total FROM users u INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN: lấy TẤT CẢ từ bảng trái, NULL nếu không có match
SELECT u.name, COUNT(o.id) as order_count
FROM users u LEFT JOIN orders o ON u.id = o.user_id GROUP BY u.id, u.name;

-- CROSS JOIN: tích Descartes
SELECT * FROM colors CROSS JOIN sizes;
```
**Dùng khi nào:** INNER cho data analysis; LEFT cho báo cáo (users kể cả chưa mua hàng); FULL OUTER để so sánh 2 nguồn dữ liệu (migration verification).

#### CTE & Window Functions
```sql
WITH high_value_orders AS (
    SELECT user_id, SUM(total) as total_spent FROM orders
    GROUP BY user_id HAVING SUM(total) > 1000
)
SELECT u.name, hvo.total_spent FROM users u
JOIN high_value_orders hvo ON u.id = hvo.user_id;

-- Recursive CTE cho hierarchical data
WITH RECURSIVE category_tree AS (
    SELECT id, name, parent_id, 0 as level FROM categories WHERE parent_id IS NULL
    UNION ALL
    SELECT c.id, c.name, c.parent_id, ct.level + 1
    FROM categories c JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree ORDER BY level;

-- Window functions
SELECT name, salary, department,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank_in_dept,
    RANK() OVER (ORDER BY salary DESC) as overall_rank,
    LAG(salary) OVER (ORDER BY salary) as prev_salary,
    LEAD(salary) OVER (ORDER BY salary) as next_salary
FROM employees;

-- Running total & moving average
SELECT date, amount,
    SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING) as running_total,
    AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as moving_avg_7d
FROM sales;

-- Top N per group (VD: top 3 sản phẩm bán chạy mỗi category)
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY category_id ORDER BY sales DESC) as rn FROM products
)
SELECT * FROM ranked WHERE rn <= 3;
```
**Subquery vs CTE vs JOIN:** Subquery khó đọc, có thể chậm; CTE (`WITH`) dễ đọc hơn, tái sử dụng được trong cùng query, hợp với query nhiều bước/hierarchical data; JOIN hiệu quả nhất khi có index đúng — chỉ dùng Subquery khi không thể viết lại bằng JOIN. **Câu hỏi phỏng vấn hay:** "Tại sao query vẫn chậm dù đã có index?" → có thể query không dùng được index (bọc hàm lên cột trong `WHERE`, implicit type cast), hoặc do data skew (1 giá trị chiếm phần lớn bảng khiến planner chọn Seq Scan thay vì Index Scan).

#### Transaction, Locking, Deadlock
```sql
-- Dirty Read / Non-repeatable Read / Phantom Read
BEGIN;
SELECT COUNT(*) FROM orders WHERE status = 'pending'; -- 10
-- Transaction B INSERT 2 orders pending và COMMIT
SELECT COUNT(*) FROM orders WHERE status = 'pending'; -- 12 (phantom!)
COMMIT;

-- SELECT FOR UPDATE SKIP LOCKED — hàng đợi xử lý không chặn nhau
SELECT * FROM jobs WHERE status = 'pending'
ORDER BY created_at LIMIT 1 FOR UPDATE SKIP LOCKED;
```
Deadlock: Transaction A khóa row 1 đợi row 2, Transaction B khóa row 2 đợi row 1 → circular wait. **Tránh:** luôn khóa tài nguyên theo thứ tự nhất quán (VD: luôn khóa `id` nhỏ trước), giữ transaction ngắn, retry logic khi gặp deadlock.

**4 mức Isolation Level (tăng dần độ chặt):**

| Mức | Dirty Read | Non-repeatable Read | Phantom Read |
|---|---|---|---|
| READ UNCOMMITTED | Có thể | Có thể | Có thể |
| READ COMMITTED (mặc định Postgres) | Không | Có thể | Có thể |
| REPEATABLE READ | Không | Không | Có thể |
| SERIALIZABLE | Không | Không | Không |

Càng chặt càng an toàn nhưng càng giảm throughput (DB phải retry nhiều transaction xung đột hơn) — chỉ dùng `SERIALIZABLE` cho nghiệp vụ cực nhạy cảm (giao dịch tài chính, đặt vé giới hạn số lượng).

#### JSONB & Array trong Postgres
```sql
CREATE TABLE products (id SERIAL PRIMARY KEY, name VARCHAR(200), attributes JSONB);
SELECT * FROM products WHERE attributes->>'RAM' = '16GB';
SELECT * FROM products WHERE attributes @> '{"tags": ["sale"]}';
CREATE INDEX idx_products_attrs ON products USING GIN(attributes);

CREATE TABLE posts (id SERIAL PRIMARY KEY, title TEXT, tags TEXT[]);
SELECT * FROM posts WHERE 'python' = ANY(tags);
```
Dùng JSONB khi: schema linh hoạt (product attributes khác nhau mỗi loại), lưu config/metadata.

#### Partitioning
```sql
CREATE TABLE orders (id BIGSERIAL, created_at TIMESTAMP NOT NULL, amount DECIMAL(10,2))
    PARTITION BY RANGE (created_at);
CREATE TABLE orders_2024 PARTITION OF orders FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
```
Query tự động chỉ scan partition cần thiết (partition pruning). Use case: logs, time-series data.

#### MongoDB — Document, Schema-less, CRUD
Document (BSON) linh hoạt — thêm field bất kỳ mà không cần migration.
```javascript
db.users.insertOne({ name: "Tin", email: "tin@example.com", skills: ["Python", "Flask"] });
db.users.find({ age: { $gte: 18, $lte: 30 }, skills: { $in: ["Python", "JavaScript"] } });
db.users.updateOne({ _id: ObjectId("...") }, { $set: { name: "New Name" }, $push: { skills: "Vue.js" }, $inc: { loginCount: 1 } });
db.users.deleteMany({ isActive: false, lastLogin: { $lt: new Date("2024-01-01") } });
```

#### MongoDB Aggregation Pipeline
```javascript
db.orders.aggregate([
    { $match: { status: "completed" } },
    { $lookup: { from: "users", localField: "userId", foreignField: "_id", as: "user" } },
    { $unwind: "$user" },
    { $group: { _id: "$user.country", totalRevenue: { $sum: "$total" }, orderCount: { $sum: 1 } } },
    { $sort: { totalRevenue: -1 } },
    { $limit: 10 }
]);
```
`$match` (lọc, giống WHERE), `$group` (nhóm + tính toán), `$lookup` ("fake" JOIN giữa 2 collection), `$project` (chỉ lấy field cần thiết).

#### MongoDB Index — ESR Rule
**E**quality → **S**ort → **R**ange. Query `{ status: "active", age: { $gt: 18 } } sort by name` → index tốt: `{ status: 1, name: 1, age: 1 }`.
```javascript
db.users.createIndex({ email: 1 }, { unique: true });
db.orders.createIndex({ userId: 1, createdAt: -1 });  // Compound
db.products.createIndex({ name: "text", description: "text" });  // Full-text
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 });  // TTL — tự xóa
```

#### SQL vs NoSQL — bảng so sánh tổng hợp

| Đặc điểm | PostgreSQL (SQL) | MongoDB (NoSQL) |
|---|---|---|
| Schema | Cố định, chặt chẽ | Linh hoạt, dynamic |
| Giao dịch | ACID hoàn hảo | Hỗ trợ nhưng không phải thế mạnh |
| Mở rộng | Vertical (RAM/CPU) | Horizontal (thêm server) |
| Dự án phù hợp | Tài chính, kế toán, e-commerce | Logging, real-time chat, social |

#### Database Migration Pattern
```python
# Alembic migration
def upgrade():
    op.add_column("users", sa.Column("role", sa.String(50), nullable=False, server_default="user"))
    op.create_index("idx_users_role", "users", ["role"])

def downgrade():
    op.drop_index("idx_users_role", "users")
    op.drop_column("users", "role")
```
**Quy tắc:** luôn có cả `upgrade()` và `downgrade()`; không xóa column trong cùng release với code dùng nó; thêm column với default value, KHÔNG nullable ngay.

#### Thứ tự scale DB thật (từ rẻ nhất tới tốn kém nhất)
1. **Tối ưu query + đúng index** — rẻ nhất, hiệu quả nhất, luôn làm trước.
2. **Thêm cache layer (Redis)** trước các query đọc lặp lại nhiều (Chương 11) — giảm tải DB mà không cần đổi kiến trúc.
3. **Read Replica** — tách query `SELECT` báo cáo/dashboard sang bản sao chỉ đọc, giữ DB chính cho ghi.
4. **Connection pooler (PgBouncer)** — gộp hàng nghìn connection từ nhiều Pod xuống còn vài chục connection thật tới Postgres.
5. **Partitioning** — chia bảng lớn theo thời gian/khu vực, vẫn trong cùng 1 DB, quản lý đơn giản hơn sharding.
6. **Sharding** — chia dữ liệu ra nhiều DB vật lý, **phương án cuối cùng** vì mất khả năng JOIN/transaction xuyên shard, độ phức tạp vận hành tăng vọt. Nhiều công ty "sharding sớm" rồi hối hận vì độ phức tạp vượt xa lợi ích thật ở quy mô của họ.

**Câu hỏi senior hay hỏi khi review:** "Bạn chọn Mongo/Postgres cho service này dựa trên tiêu chí gì — hay chỉ vì quen tay?" / "2 transaction này có thể deadlock không? Thứ tự khóa tài nguyên có nhất quán trong toàn bộ codebase không?" / "Trước khi nghĩ tới sharding, đã thử cache + read replica + tối ưu index chưa?"

**Index — con dao hai lưỡi vận hành thật:** index không dùng vẫn tốn dung lượng + I/O khi ghi — senior định kỳ rà soát bằng `pg_stat_user_indexes` để dọn index thừa. Bảng ghi nhiều (event log) mà thêm quá nhiều index → ghi chậm hẳn, đây là sự cố thật khi "tối ưu đọc" vô tình phá "hiệu năng ghi".

#### Sự cố thực chiến — database full disk, query chậm
**Production DB full disk — xử lý ngay:** alert team, không panic → `du -sh /var/lib/postgresql/*` tìm nguồn (logs/temp/bloat) → xóa log cũ, `VACUUM FULL` nếu bloat lớn → extend disk (cloud resize không downtime) → archive dữ liệu cũ sang S3 → thiết lập alert disk >80%, log rotation.

**Query optimization checklist:** `EXPLAIN ANALYZE` trước tiên → kiểm tra Seq Scan trên bảng lớn (cần index) → kiểm tra N+1 với ORM → `SELECT *` → chỉ SELECT cột cần → tối ưu JOIN (INNER nhanh hơn LEFT nếu biết có match) → pagination dùng cursor-based thay vì OFFSET lớn → `VACUUM ANALYZE` sau DELETE/UPDATE nhiều.

</details>

---

<a id="chuong-4"></a>
## Chương 4 — Cấu trúc dữ liệu & Giải thuật áp dụng cho Backend

> Không cần luyện LeetCode kiểu thi đấu — chỉ cần hiểu đúng Big-O để **chọn đúng cấu trúc dữ liệu khi code thật**.

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Array, Dict/Hash Map — dùng hàng ngày nhưng ít khi nghĩ về độ phức tạp.
- Khi nào dùng Set thay List để check tồn tại (O(1) vs O(n)).

🟡 **Nâng cao (trọng tâm Middle):**
- Caching pattern dùng LRU Cache (`functools.lru_cache`), liên hệ tới Redis ở Chương 11.

🔴 **Chuyên sâu / Thực chiến:**
- Union-Find, Graph cơ bản (BFS/DFS) — ít dùng trực tiếp trong code CRUD hàng ngày nhưng hay bị hỏi lý thuyết ở vòng phỏng vấn sâu hơn.

**Giải thích chi tiết:**

🟢 *Cơ bản.* **Set vs List khi check tồn tại.** `x in my_list` là O(n) — Python phải duyệt từng phần tử. `x in my_set` là O(1) trung bình — set dùng hash table y hệt dict. Khi code có `if x in collection` chạy trong vòng lặp lớn, đổi `list` → `set` là tối ưu rẻ nhất, hay bị bỏ qua trong code thực tế.

```python
blocked_ids = [101, 205, 309, ...]        # list 10.000 phần tử
if user_id in blocked_ids: ...            # O(n) — duyệt tới khi tìm thấy hoặc hết list

blocked_ids = {101, 205, 309, ...}        # đổi sang set — chỉ thêm 1 ký tự khi khởi tạo
if user_id in blocked_ids: ...            # O(1) trung bình — tra thẳng qua hash
```

🟡 *Nâng cao.* **LRU Cache.** Cache "Least Recently Used": khi cache đầy, phần tử **lâu không được dùng tới nhất** bị loại bỏ trước. `@lru_cache(maxsize=128)` tự động nhớ lại kết quả theo tham số đầu vào — chính là nguyên lý đằng sau cache Redis ở Chương 11, chỉ khác là Redis cache ở ngoài process, dùng được cho nhiều server.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_exchange_rate(currency: str) -> float:
    return call_slow_external_api(currency)   # chỉ gọi thật khi chưa có trong cache

get_exchange_rate("USD")  # gọi API thật, tốn thời gian
get_exchange_rate("USD")  # trả ngay từ cache, không gọi lại API
```

🔴 *Chuyên sâu/Thực chiến.* **Union-Find, Graph cơ bản.** Union-Find trả lời nhanh "2 phần tử có cùng nhóm không" (VD: phát hiện gian lận). Graph cơ bản (BFS/DFS) ít dùng trực tiếp trong code CRUD hàng ngày, nhưng là nền cho các câu hỏi lý thuyết phỏng vấn.

**Đọc chi tiết:** [`Mastery/DSA-Mastery/01-Foundations`](../Mastery/DSA-Mastery/01-Foundations) → `02-Linear-Structures-And-Hashing`. Không cần học hết toàn bộ DSA-Mastery — ưu tiên 2 module này + `08-Junior-To-Senior-Problem-Playbook`.

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `Mastery/DSA-Mastery/01-Foundations/README.md`.

#### Big O — ngân sách hiệu năng, không phải bài tập hàn lâm
Senior dùng Big O để trả lời câu hỏi kinh doanh: "Tính năng này có sống được khi data tăng 100x không?" Trước khi viết code, luôn ước lượng: n hiện tại và sau 1-2 năm; request chạy bao nhiêu lần/giây (O(n²) chạy 1 lần/ngày chấp nhận được, trên mỗi HTTP request là thảm họa); latency hay throughput quan trọng hơn.

| Tình huống thực tế | Vấn đề Big O | Giải pháp |
|---|---|---|
| Tìm user theo email trong bảng 50 triệu dòng, không index | O(n) full table scan | Thêm B-Tree index (O(log n)) |
| `/friends/mutual` so 2 danh sách bạn bè | So sánh lồng nhau O(n·m) | Đổi 1 danh sách thành `set()` → O(n+m) |
| Autocomplete gọi API mỗi ký tự gõ | Mỗi lần gõ trigger query O(n) | Debounce + Trie/Elasticsearch |
| Dashboard tính tổng doanh thu mỗi lần load | O(n) quét lại toàn bộ đơn hàng | Pre-aggregate (materialized view/cache Redis) |

**Case thật:** gợi ý sản phẩm liên quan duyệt toàn bộ catalog O(n²) — 500 sản phẩm demo mượt (<1s), 2 triệu sản phẩm production → 4×10¹² phép tính → server treo, autoscaler bật hết vẫn timeout. **Bài học:** luôn hỏi "n trong môi trường thật lớn cỡ nào" TRƯỚC khi chọn thuật toán.

**Space Complexity:** RAM trên container (K8s pod, Lambda) luôn giới hạn cứng (VD 512MB) — thuật toán O(n) bộ nhớ thêm có thể làm pod **OOMKilled** dù CPU rảnh. Dùng streaming/generator thay vì load hết vào list khi n lớn.

#### Đệ quy — sức mạnh và bẫy Stack Overflow
Python giới hạn độ sâu đệ quy ~1000. Hàm đệ quy xử lý cây thư mục/bình luận lồng nhau có thể crash thật với dữ liệu người dùng tạo cấu trúc quá sâu (có thể là DoS cố ý).

```python
# ❌ Nguy hiểm: không kiểm soát độ sâu
def count_nested(data):
    if isinstance(data, dict):
        return 1 + sum(count_nested(v) for v in data.values())
    return 0

# ✅ Senior fix: chuyển sang lặp dùng stack tường minh
def count_nested_safe(data):
    stack = [data]
    count = 0
    while stack:
        item = stack.pop()
        if isinstance(item, dict):
            count += 1
            stack.extend(item.values())
    return count
```

**Python không tối ưu Tail Call** (khác Scheme/Erlang) — khi port logic từ ngôn ngữ khác hay dùng đệ quy đuôi, phải chuyển về vòng lặp `while`/`for`.

```python
from functools import lru_cache

@lru_cache(maxsize=1024)
def compute_shipping_cost(origin: str, destination: str, weight: int) -> float:
    ...  # gọi API bên thứ 3 tốn tiền mỗi lần gọi
```

**Pitfall:** mutable default argument trong hàm đệ quy:
```python
# ❌ Bug kinh điển — list "path" bị chia sẻ giữa các lần gọi
def find_paths(node, path=[]):
    path.append(node)

# ✅ Đúng
def find_paths(node, path=None):
    if path is None:
        path = []
    path = path + [node]  # tạo list mới, không mutate list cũ
```

#### Câu hỏi senior hay hỏi
1. "Complexity này là worst-case hay average-case? Có amortized cost nào không?" (VD: `list.append()` là O(1) amortized nhờ dynamic resizing).
2. "Nếu input tăng 1000 lần, hệ thống phản ứng thế nào — có SLA/benchmark chứng minh không?"
3. "Đệ quy này có thể bị stack overflow với input độc hại (adversarial input) không?"

</details>

---

## PHẦN II — BACKEND FRAMEWORK

<a id="chuong-5"></a>
## Chương 5 — Django sâu: ORM, Migration, Admin, Middleware, Signal

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- ORM, migration, quan hệ ForeignKey/ManyToMany — đã hiểu tư duy qua Frappe, chỉ cần đổi cú pháp.
- Admin interface — tương tự Frappe Desk, học nhanh.

🟡 **Nâng cao (trọng tâm Middle):**
- **Middleware** — nơi xử lý request/response xuyên suốt toàn app (auth, logging, CORS).
- Class-Based View vs Function-Based View — khi nào nên dùng loại nào.

🔴 **Chuyên sâu / Thực chiến:**
- **Signal** (post_save, pre_delete...) — khác với Frappe hook nhưng cùng ý tưởng; dễ lạm dụng khiến luồng xử lý bị "ẩn", khó debug.
- **N+1 query problem** + cách fix bằng `select_related`/`prefetch_related` — câu hỏi phỏng vấn Middle gần như chắc chắn gặp.

**Giải thích chi tiết:**

🟡 *Nâng cao.* **Middleware.** Lớp xử lý nằm giữa request đến và response trả về, chạy cho **mọi** request đi qua (auth check, log, thêm CORS header, nén response...). Middleware xếp thành chuỗi — request đi qua từng middleware theo thứ tự khai báo, response đi ngược lại.

**CBV vs FBV.** FBV viết tường minh, dễ đọc với logic đơn giản. CBV (VD `ListView`, `CreateView`) tận dụng kế thừa để tái sử dụng logic chuẩn — mạnh khi nhiều view giống nhau, nhưng "ảo thuật" (nhiều hành vi ẩn trong class cha) khiến người mới đọc khó theo dõi luồng chạy thật.

🔴 *Chuyên sâu/Thực chiến.* **Signal.** Cho phép 1 đoạn code tự chạy khi 1 sự kiện xảy ra ở model khác, **không cần** model đó biết tới code của bạn — VD: tự gửi email chào mừng mỗi khi có `User` mới, bằng cách lắng nghe signal `post_save` của model `User`. Giống ý tưởng Frappe hook (`doc_events`) nhưng cú pháp khác. Dễ sai: lạm dụng signal khiến luồng xử lý bị "ẩn" — đọc code tạo `User` không thấy gì, nhưng thực tế có 5 signal khác đang chạy ngầm, rất khó debug.

**N+1 query problem.** Lỗi kinh điển: lấy danh sách 100 đơn hàng (1 query), rồi với **mỗi** đơn hàng lại query thêm để lấy tên khách hàng (100 query nữa) → tổng 101 query thay vì 2. `select_related` (SQL JOIN, cho FK/OneToOne) và `prefetch_related` (query riêng rồi ghép ở Python, cho ManyToMany/reverse FK) gom lại thành 1-2 query duy nhất. Câu hỏi phỏng vấn Middle gần như chắc chắn sẽ gặp.

```python
# BAD: 1 query lấy orders + 100 query lấy customer (N+1)
orders = Order.objects.all()
for o in orders:
    print(o.customer.name)        # mỗi lần truy cập .customer -> 1 query mới

# GOOD: select_related dùng SQL JOIN (cho FK/OneToOne) -> chỉ 1 query
orders = Order.objects.select_related("customer").all()

# GOOD: prefetch_related cho ManyToMany/reverse FK -> 2 query, ghép ở Python
orders = Order.objects.prefetch_related("items").all()
```

**Đọc chi tiết:** [`03-Python-Expert/Django_Mastery_Guide.md`](../03-Python-Expert/Django_Mastery_Guide.md). Đọc code thật: [`09-Example-Projects/Django_RealWorld`](../09-Example-Projects/Django_RealWorld), [`09-Example-Projects/Django_Rest_Pro`](../09-Example-Projects/Django_Rest_Pro).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `03-Python-Expert/Django_Mastery_Guide.md`, `Mastery/Backend-Mastery/01-Request-Lifecycle-And-Architecture/README.md` (mục 2-3).

#### MVT & ORM
**MVT (Model-View-Template):** Model là dữ liệu, View là điều hướng/xử lý, Template là giao diện HTML. **Django ORM** hỗ trợ đầy đủ quan hệ ForeignKey, OneToOne, ManyToMany. **Django Admin:** trang quản trị giúp quản lý dữ liệu CMS ngay lập tức mà không tốn 1 dòng code UI.

#### Custom User Model
Bí kíp sống còn: luôn tạo User model riêng từ đầu dự án kế thừa từ `AbstractUser` để dễ mở rộng — đổi sau khi đã migrate dữ liệu thật là cực kỳ khó.

#### Signals & Middleware, WebSocket/Channels, Multi-tenancy
Signals (lắng nghe sự kiện) và Middleware (bộ lọc cổng vào) giúp quản lý logic toàn hệ thống tập trung. Django Channels xử lý Chat/thông báo real-time cho hàng ngàn người dùng. Multi-tenancy: cấu hình SaaS 1 ứng dụng nhiều công ty, tối ưu hiệu năng bằng Redis Caching + Celery Backend Workers.

#### Middleware thực tế — timing + cảnh báo slow request
```python
import time

async def timing_middleware(request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    response.headers["X-Process-Time"] = str(duration)
    if duration > 1.0:
        logger.warning(f"SLOW REQUEST: {request.url} took {duration:.2f}s")
    return response
```
**Bài học senior:** middleware chạy theo **thứ tự khai báo** — lỗi phổ biến nhất là đặt sai thứ tự (VD: middleware nén response chạy trước middleware auth → có thể rò rỉ dữ liệu lỗi chưa auth check).

#### N+1 Query — con quái vật âm thầm giết hiệu năng production
```python
# ❌ N+1: 1 query lấy orders + N query lấy customer cho MỖI order
orders = Order.objects.all()          # 1 query
for order in orders:
    print(order.customer.name)        # +1 query MỖI vòng lặp → 1 + N query!

# ✅ Senior fix: JOIN trước bằng select_related (foreign key) / prefetch_related (many-to-many)
orders = Order.objects.select_related("customer").all()   # đúng 1 query duy nhất
```
**Vì sao nguy hiểm hơn junior nghĩ:** với 20 đơn hàng demo, N+1 chỉ chậm thêm vài ms — không ai để ý. Với 50.000 đơn hàng trên production, đây là 50.001 lần round-trip tới DB → timeout, và tệ hơn: **rút cạn connection pool** (Chương 3), khiến các request KHÁC không liên quan cũng bị treo theo. Đây là lý do senior luôn bật **query logging** ở staging trước khi deploy tính năng liên quan tới danh sách dữ liệu.

**Câu hỏi senior hay hỏi khi review PR/thiết kế:** "Endpoint này trả về danh sách — đã kiểm tra query log xem có N+1 không?" / "Nếu traffic tăng 10x đột ngột, connection pool có bảo vệ được DB không, hay sẽ sập dây chuyền?" / "Middleware auth có chạy TRƯỚC middleware log response body không? Có rủi ro lộ dữ liệu nhạy cảm trong log không?"

#### Thử thách thực tế & giải pháp
- **Xung đột Migration:** khắc phục bằng `--merge` hoặc quản lý tập trung trong team.
- **Admin bị chậm:** tắt bộ đếm bản ghi (`show_full_result_count = False`) khi database quá lớn.
- **CORS Errors:** cấu hình `django-cors-headers`.

#### Senior's Knowledge — kinh nghiệm thực chiến
- **Squash Migrations:** nén hàng trăm file cũ để dọn dẹp hệ thống.
- **Fat Models vs Thin Views:** đẩy logic nghiệp vụ vào Model/Manager để tái sử dụng tối đa.
- **Tùy biến Admin:** dùng Inlines, Actions, Custom Forms thay vì viết Dashboard mới.

#### Security & Vulnerability Fixes
- **Raw SQL Injection:** không cộng chuỗi SQL, luôn truyền tham số `params=[...]`.
- **Debug on Prod:** luôn đặt `DEBUG = False` và dùng lệnh `check --deploy`.
- **Phân quyền IDOR:** luôn lọc dữ liệu theo `request.user` để chống user xem trộm dữ liệu nhau.

#### Database Interaction
**Lazy Evaluation:** hệ thống chỉ truy vấn SQL khi thực sự "chạm" vào dữ liệu. **Transactions:** dùng `ATOMIC_REQUESTS` để lỗi ở đâu, rollback ở đó. **Database Routers:** chia tải Read/Write splitting.

#### SQL Optimization trong Django ORM
1. **`only()` và `defer()`:** `only('name', 'email')` chỉ lấy 2 cột; `defer('content')` lấy tất cả trừ cột nặng.
2. **`.iterator()`:** xử lý hàng triệu bản ghi (export CSV) mà không tải hết vào RAM → tránh `MemoryError`.
3. **`.explain()`:** QuerySet hỗ trợ xem Execution Plan trực tiếp.
4. **`Meta.indexes`:** tạo composite index cho query phức tạp.
5. **Tránh đếm dữ liệu thừa:** `queryset.count()` thay vì `len(queryset)`; `queryset.exists()` thay vì `if queryset:`.

#### Request lifecycle đầy đủ qua Django
```
Client → Load Balancer/CDN → Web Server (Nginx/Gunicorn) → WSGI/ASGI
   → Framework (Django) → Middleware chain → View/Controller → Service layer
   → ORM → Connection Pool → Database → Cache layer (Redis, có thể chen TRƯỚC khi gọi DB)
```
**Vì sao senior phải nắm toàn bộ luồng:** khi API chậm, junior chỉ nhìn code trong view function; senior biết độ trễ có thể nằm ở bất kỳ tầng nào — DNS resolve, health-check sai, connection pool cạn, N+1 query, hay disk I/O của DB.

</details>
**Bài tập:** DJ-01 → DJ-04 trong [`01-Django-Exercises/Checklist_Bai_Tap.md`](01-Django-Exercises/Checklist_Bai_Tap.md).

---

<a id="chuong-6"></a>
## Chương 6 — Django REST Framework: API thực chiến

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Serializer (validate + transform data) — tương tự Pydantic nhưng gắn với Django ORM.
- Pagination, Filtering cơ bản.

🟡 **Nâng cao (trọng tâm Middle):**
- ViewSet + Router (giảm code lặp).
- Permission & Authentication class, JWT (access token/refresh token).
- Viết Unit Test cho API (happy path + lỗi validation + lỗi auth).

🔴 **Chuyên sâu / Thực chiến:**
- Throttling (rate limit) — chặn brute-force/lạm dụng API; thiết kế permission class tùy biến theo role phức tạp (không chỉ dùng class có sẵn).

**Giải thích chi tiết:**

🟢 *Cơ bản.* **Serializer.** Làm 2 việc ngược nhau: chuyển object Python (model instance) thành JSON để trả về client (serialize), và chuyển JSON client gửi lên thành object Python có validate (deserialize) — tương tự Pydantic nhưng gắn chặt với Django ORM.

```python
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "customer", "total", "created_at"]

    def validate_total(self, value):
        if value <= 0:
            raise serializers.ValidationError("total phải lớn hơn 0")
        return value
```

🟡 *Nâng cao.* **ViewSet + Router.** `ViewSet` gom các action CRUD vào 1 class, `Router` tự động sinh URL chuẩn REST cho các action đó — giảm code lặp (không cần viết tay 5 URL pattern cho mỗi resource).

```python
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related("customer").all()  # tránh N+1 (Chương 5)
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

router = DefaultRouter()
router.register("orders", OrderViewSet)
# tự sinh: GET/POST /orders/, GET/PUT/DELETE /orders/{id}/
```

**JWT access/refresh token.** Access token sống ngắn (VD 15 phút) — nếu bị lộ, thiệt hại giới hạn trong thời gian ngắn. Refresh token sống dài (VD 7 ngày), chỉ dùng để xin access token mới, không dùng để gọi API trực tiếp — giảm số lần phải gửi token "mạnh" qua mạng.

🔴 *Chuyên sâu/Thực chiến.* **Throttling.** Giới hạn số request/phút theo user hoặc IP — chặn 1 client gọi API quá dồn dập làm quá tải server hoặc để chống brute-force login.

```python
class OrderViewSet(viewsets.ModelViewSet):
    throttle_classes = [UserRateThrottle]  # "user": "100/min" khai báo trong settings.py
```

**Đọc chi tiết:** phần DRF trong [`03-Python-Expert/Django_Mastery_Guide.md`](../03-Python-Expert/Django_Mastery_Guide.md) + [`interview_prep/03_Database.md`](../interview_prep/03_Database.md) cho phần liên quan ORM/API.

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `03-Python-Expert/Django_Mastery_Guide.md` (mục 2), `interview_prep/07_Cau_Hoi_Phong_Van.md` (Q14-22).

**DRF (Django REST Framework):** công cụ tốt nhất để làm API JSON cho Vue/React — dùng Serializers biến Object Python thành JSON. **QuerySet Optimization:** khắc phục N+1 Query bằng `select_related()` (ForeignKey) và `prefetch_related()` (ManyToMany).

**Flask application context vs request context** (áp dụng được cho tư duy request-scoped data nói chung): Application context (`g`, `current_app`) tồn tại trong app lifecycle; Request context (`request`, `session`) tồn tại trong 1 request — `g` reset mỗi request, dùng để share data trong 1 request.

**Concurrent requests:** dev server mặc định single-threaded; production dùng Gunicorn (multi-worker), uWSGI, hoặc async. Connection pooling cho DB: `pool_size`, `max_overflow`.

```python
from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": ["https://your-frontend.com"], "methods": ["GET", "POST", "PUT", "DELETE"]}})
```

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(app, key_func=get_remote_address)

@api_bp.route("/login", methods=["POST"])
@limiter.limit("5 per minute")
def login():
    pass
```

**Database Transaction — khi nào rollback:**
```python
try:
    db.session.add(order)
    db.session.add(payment)
    deduct_inventory(order.items)
    db.session.commit()
except Exception:
    db.session.rollback()
    raise
```

**Test API:**
```python
def test_create_user(client, db):
    response = client.post("/api/users", json={"name": "Test", "email": "test@example.com", "password": "secure123"})
    assert response.status_code == 201
    user = User.query.filter_by(email="test@example.com").first()
    assert user is not None
```

</details>
**Bài tập:** DJ-05 → DJ-07.

---

<a id="chuong-7"></a>
## Chương 7 — Flask & FastAPI: So sánh với Django

> Mục tiêu không phải học lại backend, mà **cảm nhận sự khác biệt** giữa 3 framework để trả lời câu phỏng vấn senior rất hay gặp: "khi nào chọn Flask, khi nào chọn Django, khi nào chọn FastAPI".

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Flask thuần (route, request object) không có ORM/Admin có sẵn — phải tự viết nhiều hơn Django.
- **FastAPI**: framework async-first, dùng **Pydantic** để validate data tự động từ type hint — khác hẳn cách Django/Flask validate thủ công hoặc qua Serializer/Form riêng.

🟡 **Nâng cao (trọng tâm Middle):**
- Flask-SQLAlchemy (ORM khác cú pháp Django ORM), Flask-Migrate.
- Blueprint — cách tổ chức code Flask ở quy mô lớn hơn "hello world".
- **FastAPI Dependency Injection** (`Depends`) — cơ chế DI tích hợp sẵn trong framework, khác với DI tự thiết kế đã học ở Chương 1.

🔴 **Chuyên sâu / Thực chiến:**
- Dockerize Flask app (nền cho Chương 14); trả lời được câu hỏi senior kinh điển "khi nào chọn Flask, khi nào chọn Django, khi nào chọn FastAPI" kèm ví dụ cụ thể.
- **Sự cố thực tế khi dùng FastAPI sai cách**: gọi thư viện I/O đồng bộ (`requests`, `time.sleep()`, driver DB đồng bộ) bên trong `async def` — event loop bị block, toàn bộ server đứng hình dù code "trông có vẻ" bất đồng bộ.

**Giải thích chi tiết:**

🟢 *Cơ bản.* Flask không có ORM/Admin sẵn như Django — triết lý "micro-framework": bạn tự chọn thư viện, tự ghép lại theo ý mình. Đổi lại là tự do kiến trúc cao hơn, phù hợp project nhỏ/microservice; Django phù hợp hơn khi cần "có sẵn mọi thứ" để ra sản phẩm nhanh (CMS, admin dashboard nội bộ).

**FastAPI & Pydantic.** FastAPI được thiết kế **async-first** ngay từ đầu (chạy trên ASGI, nối trực tiếp với kiến thức WSGI vs ASGI ở Chương 10) — khác với Django/Flask vốn sync-first rồi mới thêm hỗ trợ async sau. Thay vì viết Serializer (DRF) hay Form (Flask) riêng để validate input, FastAPI dùng **Pydantic model** — chỉ cần khai báo type hint, framework tự validate + tự sinh tài liệu OpenAPI/Swagger (liên hệ Chương 9) mà không cần viết thêm gì.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class OrderIn(BaseModel):
    customer_id: int
    total: float            # FastAPI tự validate: gửi lên string "abc" -> tự trả lỗi 422

@app.post("/orders")
async def create_order(order: OrderIn):   # không cần viết Serializer/Form riêng
    return {"id": 1, **order.dict()}
```

🟡 *Nâng cao.* **Flask-SQLAlchemy, Flask-Migrate, Blueprint.** `Flask-SQLAlchemy` (ORM), `Flask-Migrate` (migration) là 2 extension bù lại phần Flask không có sẵn. **Blueprint** là cách chia code thành nhiều module độc lập (giống Django app) khi project lớn dần — không dùng Blueprint, mọi route dồn vào 1 file sẽ không scale được về mặt tổ chức code.

**FastAPI Dependency Injection.** `Depends()` cho phép khai báo 1 hàm/class là dependency của endpoint (VD lấy current user từ token, mở connection DB) — FastAPI tự gọi và inject kết quả vào tham số hàm, tương tự ý tưởng Dependency Injection đã học ở Chương 1 nhưng được framework hỗ trợ sẵn cú pháp thay vì tự thiết kế từ đầu.

```python
def get_current_user(token: str = Header(...)) -> User:
    return decode_jwt_and_fetch_user(token)

@app.get("/me")
async def read_me(user: User = Depends(get_current_user)):  # FastAPI tự gọi + inject
    return user
```

🔴 *Chuyên sâu/Thực chiến.* **So sánh 3 framework.** Django: "có sẵn mọi thứ" (ORM, Admin, Auth) — nhanh nhất để ra sản phẩm hoàn chỉnh, hợp CMS/dashboard nội bộ. Flask: tối giản, tự do kiến trúc cao nhất — hợp project nhỏ/microservice cần kiểm soát từng phần. FastAPI: async-first + validate tự động qua Pydantic + tự sinh docs — hợp API thuần túy (không cần UI render sẵn), đặc biệt khi cần throughput cao với nhiều I/O đồng thời (gọi nhiều service khác, websocket).

**Sự cố block event loop.** Đây là lỗi production có thật và rất phổ biến khi chuyển từ Flask (sync) sang FastAPI (async): dev quen tay dùng `requests`, `time.sleep()`, hoặc driver DB đồng bộ (`psycopg2`) bên trong `async def` — vì thư viện đó không `await` đúng cách, nó chặn đứng toàn bộ event loop (liên hệ trực tiếp cơ chế asyncio đã học ở Chương 1), khiến **mọi** request khác trên cùng worker bị đứng theo dù code "nhìn có vẻ" async. Khắc phục: mọi I/O trong code async phải dùng bản async thật (`httpx` thay `requests`, `asyncpg`/`motor` thay driver sync).

**Đọc chi tiết:** [`interview_prep/02_Flask_Backend.md`](../interview_prep/02_Flask_Backend.md). Đọc code thật: [`09-Example-Projects/Flask_RealWorld`](../09-Example-Projects/Flask_RealWorld), [`09-Example-Projects/Flask_SaaS_Boilerplate`](../09-Example-Projects/Flask_SaaS_Boilerplate). FastAPI: [`03-Python-Expert/Python_Backend_Professional_Guide.md`](../03-Python-Expert/Python_Backend_Professional_Guide.md) mục 3-4, [`Mastery/Backend-Mastery/02-Concurrency-And-Async-In-Production`](../Mastery/Backend-Mastery/02-Concurrency-And-Async-In-Production).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `interview_prep/02_Flask_Backend.md`, `03-Python-Expert/Python_Backend_Professional_Guide.md` (mục 3, 4, 5), `Mastery/Backend-Mastery/02-Concurrency-And-Async-In-Production/README.md`.

#### App Factory Pattern
```python
# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    return app
```
**Dùng khi nào:** tránh circular imports khi app lớn; cho phép tạo nhiều instance khác nhau (testing, prod, dev) — best practice cho Flask production apps.

#### Blueprint Pattern — chia code theo feature module
```python
# routes/auth.py
from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return jsonify({"token": generate_token()})

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    return jsonify({"message": "Logged out"})
```
**Dùng khi nào:** mỗi blueprint là 1 mini-app (auth, users, products, orders) — chia project lớn thành module độc lập thay vì nhét hết route vào 1 file.

#### SQLAlchemy — Query nâng cao, Pagination
```python
from sqlalchemy import and_, or_, desc, func

users = (User.query
    .filter(and_(User.is_active == True, User.age > 18))
    .order_by(desc(User.created_at))
    .limit(20).offset(0).all())

result = (db.session.query(User, Post)
    .join(Post, User.id == Post.author_id)
    .filter(User.is_active == True).all())

count = db.session.query(func.count(User.id)).scalar()
avg_age = db.session.query(func.avg(User.age)).scalar()

page = User.query.paginate(page=1, per_page=20, error_out=False)
# page.items, page.total, page.pages, page.has_next
```

#### Request Hooks — before/after/teardown
```python
@app.before_request
def log_request():
    g.start_time = time.time()
    logger.info(f"{request.method} {request.path}")

@app.after_request
def log_response(response):
    elapsed = time.time() - g.start_time
    logger.info(f"Response {response.status_code} in {elapsed:.3f}s")
    return response

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()   # cleanup DB session sau mỗi request
```

#### Error Handling & Logging tập trung
```python
from logging.handlers import RotatingFileHandler

def setup_logging(app):
    handler = RotatingFileHandler("app.log", maxBytes=10*1024*1024, backupCount=5)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
    app.logger.addHandler(handler)

@app.errorhandler(500)
def server_error(e):
    app.logger.error(f"Server error: {e}", exc_info=True)
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    app.logger.error(f"Unhandled exception: {e}", exc_info=True)
    return jsonify({"error": "Something went wrong"}), 500
```

#### SQLAlchemy ORM — Model, Query, Lazy vs Eager Loading
```python
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    posts = db.relationship("Post", back_populates="author", lazy="dynamic")

# LAZY (N+1 problem!)
users = User.query.all()
for user in users:
    print(user.posts.all())  # query thêm DB cho MỖI user → N+1!

# EAGER (joinedload) — 1 query duy nhất
from sqlalchemy.orm import joinedload
users = User.query.options(joinedload(User.posts)).all()
```

#### JWT Authentication & Role-based Access Control
```python
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import bcrypt

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    if not user or not bcrypt.checkpw(data["password"].encode(), user.password_hash):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(identity=user.id, additional_claims={"role": user.role})
    return jsonify({"access_token": token})

def require_role(*roles):
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if claims.get("role") not in roles:
                return jsonify({"error": "Insufficient permissions"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator
```
**Dùng khi nào:** JWT — stateless auth, mobile/microservices; Session — stateful, cần revoke ngay; JWT + Refresh Token — cân bằng security và UX.

#### WebSocket với Flask-SocketIO
```python
from flask_socketio import SocketIO, emit, join_room

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("join_room")
def handle_join(data):
    join_room(data["room"])
    emit("status", {"msg": f"Joined room {data['room']}"})

@socketio.on("send_message")
def handle_message(data):
    emit("receive_message", data, room=data["room"])
```

#### Celery — Background Tasks
```python
@celery.task(bind=True, max_retries=3)
def send_email_task(self, recipient, subject, body):
    try:
        send_email(recipient, subject, body)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
```
**Dùng khi nào:** gửi email/SMS (không block request); data migration; report generation; scheduled tasks (kết hợp Celery Beat).

#### FastAPI: Pydantic, Dependency Injection, Error Handling
```python
from pydantic import BaseModel, EmailStr

class UserProfile(BaseModel):
    username: str
    email: EmailStr
    age: int = 18

from fastapi import Depends
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def get_users(db = Depends(get_db_session)):
    return db.query(User).all()

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"error": "Security Alert", "message": exc.detail})
```

#### GIL không phải "Python chậm" — mà là threading không tăng tốc CPU-bound

| Loại tác vụ | Công cụ đúng | Vì sao |
|---|---|---|
| I/O-bound (API, DB, file) | `asyncio`/`threading` | GIL nhả khi chờ I/O |
| CPU-bound (ảnh, ML, nén) | `multiprocessing` | Mỗi process có GIL riêng, dùng nhiều lõi thật |
| Mixed | `asyncio` + `ProcessPoolExecutor` | Đẩy CPU-bound ra process pool, giữ event loop rảnh |

```python
# ❌ Sai lầm kinh điển: async nhưng gọi hàm BLOCKING
async def get_user_data(user_id: int):
    data = requests.get(f"https://api.example.com/users/{user_id}")  # BLOCKING!
    return data.json()

# ✅ Đúng: client HTTP bất đồng bộ thật
import httpx
async def get_user_data(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.example.com/users/{user_id}")
        return response.json()
```

#### Worker model — vì sao `gunicorn -w 4` quan trọng hơn code
Sync worker (Flask mặc định): mỗi worker xử lý 1 request/thời điểm — cần nhiều worker (`workers = 2 × số_lõi_CPU + 1`). Async worker (Uvicorn): 1 worker xử lý hàng nghìn kết nối I/O-bound trên 1 event loop — nhưng vẫn cần nhiều worker process để tận dụng nhiều lõi CPU. **Sự cố thật:** deploy FastAPI với `--workers 1` → chỉ dùng 1 lõi trên máy 8 lõi, throughput giảm 8 lần. Senior luôn benchmark số worker tối ưu bằng load test thật (Locust/k6, Chương 8), không đoán mò.

#### Background Task — giới hạn của `BackgroundTasks` (FastAPI)
```python
from fastapi import BackgroundTasks

@app.post("/register")
async def register(user: UserCreate, background_tasks: BackgroundTasks):
    new_user = create_user(user)
    background_tasks.add_task(send_welcome_email, new_user.email)  # không block response
    return {"id": new_user.id}
```
**Giới hạn cần biết:** `BackgroundTasks` chạy **trong cùng process** — server restart giữa lúc task đang chạy thì task **mất luôn**, không retry. Với tác vụ quan trọng (email xác nhận thanh toán), dùng **queue thật** (Celery + Redis/RabbitMQ, hoặc AWS SQS) có persistence + retry + dead-letter-queue thay vì BackgroundTasks.

**Câu hỏi senior hay hỏi khi review:** "Hàm `async def` này có gọi hàm blocking nào ẩn bên trong không (thư viện sync, `time.sleep`, driver DB đồng bộ)?" / "Bạn set bao nhiêu worker process — dựa trên benchmark thật hay đoán?" / "Nếu server crash giữa lúc xử lý background task, dữ liệu có bị mất không? Có cơ chế retry không?"

</details>
**Bài tập:** FL-01 → FL-04 trong [`02-Flask-Exercises/Checklist_Bai_Tap.md`](02-Flask-Exercises/Checklist_Bai_Tap.md). Nâng cao: viết lại 1 API đã làm ở Django/Flask bằng FastAPI + Pydantic, so sánh lượng code phải viết.

---

<a id="chuong-8"></a>
## Chương 8 — Testing: Unit, Integration, Mock

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Unit test (test 1 function/method độc lập) là gì, vì sao cần.
- Test coverage — hiểu ý nghĩa, không chạy theo % ảo.

🟡 **Nâng cao (trọng tâm Middle):**
- Integration test (test nhiều thành phần cùng chạy, VD: API + DB thật) — phân biệt rõ với Unit test.
- Mock/Patch (giả lập service bên ngoài — email, API thứ 3) để test không phụ thuộc mạng.

🔴 **Chuyên sâu / Thực chiến:**
- TDD (viết test trước code) — không cần theo cứng nhắc, nhưng phải hiểu tư duy để trả lời phỏng vấn và áp dụng đúng lúc.
- **Load testing** (Locust, k6) — kiểm tra hệ thống chịu được bao nhiêu request/giây trước khi gãy, khác hẳn mục tiêu của Unit/Integration test (đúng logic) — đây là loại test duy nhất trả lời được câu "hệ thống chịu tải được bao nhiêu" thay vì "code có đúng không".

**Giải thích chi tiết:**

🟢 *Cơ bản.* **Unit test, Test coverage.** Unit test kiểm tra 1 hàm/method độc lập, **giả lập (mock) hết** mọi thứ bên ngoài nó — chạy cực nhanh, chỉ fail khi chính logic đó sai. Test coverage là % dòng code được test chạy qua ít nhất 1 lần — con số này **không nói lên chất lượng test**, chỉ nói lên độ phủ; 100% coverage vẫn có thể thiếu test cho case lỗi quan trọng nếu assertion viết hời hợt.

```python
def calculate_discount(price: float, is_vip: bool) -> float:
    return price * 0.8 if is_vip else price

def test_calculate_discount_vip():
    assert calculate_discount(100, is_vip=True) == 80

def test_calculate_discount_regular():
    assert calculate_discount(100, is_vip=False) == 100
```

🟡 *Nâng cao.* **Integration test, Mock/Patch.** Integration test chạy nhiều phần thật cùng lúc — chậm hơn Unit test nhưng phát hiện được lỗi ở chỗ nối giữa các phần mà Unit test không thấy được. Mock/Patch thay thế tạm thời 1 function/object thật bằng 1 bản giả trong lúc test — VD test luồng "gửi email khi đăng ký" mà không thực sự gửi email thật.

```python
from unittest.mock import patch

def test_register_sends_welcome_email():
    with patch("app.services.send_email") as mock_send:   # không gửi email thật
        register_user(email="a@test.com")
        mock_send.assert_called_once_with(to="a@test.com", template="welcome")
```

🔴 *Chuyên sâu/Thực chiến.* **TDD.** Viết test trước khi viết code triển khai — ép bạn nghĩ rõ "hàm này cần làm gì" trước khi viết "nó làm thế nào", giúp code dễ test hơn ngay từ đầu thay vì phải chắp vá test sau.

**Load testing.** Locust/k6 giả lập hàng trăm/nghìn user gọi API đồng thời để đo throughput (request/giây), latency dưới tải, và tìm điểm hệ thống bắt đầu trả lỗi/timeout — dùng để trả lời câu hỏi thực tế "server hiện tại chịu được bao nhiêu traffic trước khi cần scale" (liên hệ trực tiếp Horizontal Scaling ở Chương 11), thay vì đoán mò hoặc đợi tới khi sập thật ở production mới biết giới hạn.

**Đọc chi tiết:** [`Mastery/Backend-Mastery/04-Testing-Observability-And-Debugging-Prod`](../Mastery/Backend-Mastery/04-Testing-Observability-And-Debugging-Prod). Load testing: [`Mastery/Backend-Mastery/02-Concurrency-And-Async-In-Production`](../Mastery/Backend-Mastery/02-Concurrency-And-Async-In-Production) (phần benchmark số worker bằng Locust/k6).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `03-Python-Expert/Python_Backend_Professional_Guide.md` (mục 9), `Mastery/Backend-Mastery/04-Testing-Observability-And-Debugging-Prod/README.md`, `interview_prep/07_Cau_Hoi_Phong_Van.md` (Q96-105).

#### Kim tự tháp kiểm thử
```
        ▲  E2E Tests (ít, chậm, tốn kém)
       ╱ ╲
      ╱   ╲  Integration Tests (vừa phải)
     ╱     ╲
    ╱───────╲ Unit Tests (nhiều, nhanh, rẻ)
```
**Rule:** 70% unit / 20% integration / 10% E2E. Sai lầm thường gặp: viết quá nhiều E2E vì "trông giống thật nhất" → suite chạy 45 phút, dev sợ chạy test nên bỏ qua, bug lọt production.

#### Pytest fixtures & conftest.py
```python
@pytest.fixture(scope='session')
def app():
    return create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})

@pytest.fixture(scope='function')
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.session.remove()
        _db.drop_all()
```

#### Mocking với `unittest.mock`
```python
from unittest.mock import Mock, patch, AsyncMock

@patch('app.services.requests.post')
def test_send_notification(mock_post):
    mock_post.return_value.status_code = 200
    result = send_notification('user@example.com', 'Hello')
    mock_post.assert_called_once()

@pytest.mark.asyncio
async def test_notification_service():
    mock_client = AsyncMock()
    mock_client.send.return_value = {'status': 'sent'}
    service = NotificationService(client=mock_client)
    await service.notify('user@example.com')
```

#### TDD — Red → Green → Refactor
```python
# Red: viết test trước
def test_calculate_discount():
    assert calculate_discount(100, 'vip') == 20

# Green: implement tối thiểu
def calculate_discount(price: float, tier: str) -> float:
    rates = {'vip': 0.2, 'regular': 0.1}
    return price * rates.get(tier, 0)
```

#### Property-based testing (Hypothesis)
```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sort_is_idempotent(lst):
    assert sorted(sorted(lst)) == sorted(lst)
# Hypothesis tự tìm edge case: empty list, max int, unicode chars
```

#### Load testing với Locust
```python
from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def get_products(self):
        self.client.get('/api/products')

    @task(1)
    def create_order(self):
        self.client.post('/api/orders', json={'product_id': 1, 'quantity': 2})
# Chạy: locust -f locustfile.py --host=http://localhost:5000
# Monitor: response time p50/p95/p99, error rate, RPS
```

#### Structured logging — log JSON thay vì print()
```python
import logging, json

def log_request(request_id: str, event: str, **kwargs):
    # Mỗi dòng log là JSON có thể query được — khác print() vô dụng khi cần
    # tìm 1 request cụ thể giữa hàng triệu dòng log/ngày trên production.
    logging.info(json.dumps({"request_id": request_id, "event": event, **kwargs}))
```
**Bẫy junior hay gặp:** chỉ có logs, không có metrics/traces → khi hệ thống chậm phải "mò" từng dòng log thủ công, không biết bottleneck nằm ở service nào. Structured logging (JSON, có `request_id` xuyên suốt service) phải thiết kế từ đầu — cực khó bổ sung sau khi hệ thống đã lớn.

#### Debug endpoint chậm trên production — quy trình senior
1. Xem metrics trước: chậm từ khi nào, trùng deploy gần nhất hay traffic tăng đột biến?
2. Xem trace của 1 request chậm cụ thể — thời gian tốn ở tầng nào?
3. Xem slow query log (`pg_stat_statements`).
4. Kiểm tra CPU/RAM/connection pool có bão hòa không.
5. Chỉ khi cần mới profile bằng `py-spy` (attach vào process đang chạy, không cần restart).
```bash
py-spy top --pid 12345
```

#### Alerting — tránh alert fatigue
Alert phải **actionable**; theo triệu chứng người dùng cảm nhận được (error rate, p99 latency) thay vì chỉ chỉ số nội bộ (CPU); có **runbook** đính kèm mỗi alert quan trọng.

#### Regression testing
```python
def test_migration_handles_null_sku():
    """Regression test for issue #456: Migration crashes on null SKU"""
    products = [{'name': 'Product A', 'sku': None}]
    result = migrate_products(products)
    assert result.success is True
    assert result.skipped_count == 1
```

</details>
**Bài tập:** DJ-07 (unit test cho API), và viết thêm test cho API Flask ở FL-01.

---

<a id="chuong-9"></a>
## Chương 9 — API Design & Best Practices

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- REST chuẩn (resource naming, HTTP method đúng ngữ nghĩa, status code đúng).
- Error handling chuẩn hóa (error response format nhất quán).

🟡 **Nâng cao (trọng tâm Middle):**
- Versioning API (`/api/v1/...`), backward compatibility khi đổi API.
- Rate limiting, pagination convention (cursor-based vs offset-based).
- **OpenAPI/Swagger** — tự sinh tài liệu API từ code (DRF có `drf-spectacular`).

🔴 **Chuyên sâu / Thực chiến:**
- Idempotency (quan trọng cho API thanh toán/retry) — thiết kế đúng tránh lỗi trừ tiền/tạo đơn trùng.
- So sánh nhanh REST vs **gRPC** (Protocol Buffers thay vì JSON, nhanh hơn cho giao tiếp service-to-service) — chỉ cần hiểu khái niệm, chưa cần tự viết.
- So sánh nhanh REST vs **GraphQL** (client tự quyết định data shape, tránh over-fetching/under-fetching) — khi nào thực sự cần, khi nào REST vẫn đủ.
- **WebSocket vs SSE (Server-Sent Events) vs Long Polling** — 3 cách làm tính năng real-time, chọn đúng theo chiều giao tiếp cần thiết.

**Giải thích chi tiết:**

🟡 *Nâng cao.* **Cursor-based vs offset-based pagination.** `offset/limit` (VD `?page=5`) đơn giản nhưng chậm dần khi offset lớn, và bị lệch dữ liệu nếu có dòng mới chèn vào giữa lúc đang phân trang. `cursor-based` (VD `?after=<id cuối cùng>`) ổn định hơn với dữ liệu thay đổi liên tục — đánh đổi là không nhảy thẳng tới "trang 5" được.

**OpenAPI/Swagger.** OpenAPI là bản mô tả API theo chuẩn (tự sinh từ code DRF), Swagger UI đọc bản mô tả đó ra giao diện test API trực quan — giảm việc phải viết tài liệu tay.

🔴 *Chuyên sâu/Thực chiến.* **Idempotency.** 1 request gửi lại nhiều lần (do mạng lỗi, client tự động retry) phải cho ra **cùng 1 kết quả**, không được tạo ra tác dụng phụ nhân đôi — cực quan trọng cho API thanh toán. Cách làm phổ biến: client gửi kèm `idempotency_key`, server lưu lại key đã xử lý để nhận diện request trùng.

```python
@app.post("/payments")
def create_payment(payload: PaymentIn, idempotency_key: str = Header(...)):
    existing = PaymentRequest.objects.filter(key=idempotency_key).first()
    if existing:
        return existing.response   # request trùng -> trả lại đúng kết quả cũ, không xử lý lại

    result = charge_card(payload)
    PaymentRequest.objects.create(key=idempotency_key, response=result)
    return result
```

**REST vs gRPC vs GraphQL — tra nhanh.**

| | REST | gRPC | GraphQL |
|---|---|---|---|
| Định dạng dữ liệu | JSON (text) | Protocol Buffers (nhị phân) | JSON |
| Tốc độ | Trung bình | Nhanh nhất | Trung bình |
| Client tự chọn field? | Không — server quyết định | Không | **Có** — tránh over/under-fetching |
| Dễ debug bằng trình duyệt? | Có | Không | Tạm được (qua tool riêng) |
| Hợp dùng cho | API public, CRUD thông thường | Service-to-service nội bộ, tốc độ cao | Nhiều loại client (web/mobile/dashboard) cần data khác nhau |

**REST vs gRPC.** gRPC dùng Protocol Buffers (dữ liệu nhị phân, nhỏ và nhanh hơn JSON) và HTTP/2, phù hợp giao tiếp nội bộ service-to-service tốc độ cao; REST/JSON vẫn thắng thế cho API public vì dễ đọc, dễ debug bằng trình duyệt.

**REST vs GraphQL.** Với REST, mỗi endpoint trả về 1 cấu trúc cố định — client nhiều khi phải gọi nhiều endpoint (under-fetching) hoặc nhận về dư thừa field không dùng tới (over-fetching). GraphQL cho client tự khai báo chính xác field cần lấy trong 1 query duy nhất, kể cả khi dữ liệu đó nằm rải rác ở nhiều "bảng" khác nhau — mạnh khi có nhiều loại client khác nhau cùng dùng chung 1 API (web, mobile, dashboard) với nhu cầu data khác nhau. Đánh đổi: khó cache ở tầng HTTP/CDN hơn REST (vì mọi request đều là `POST` tới cùng 1 endpoint), và dễ bị lạm dụng query lồng sâu gây tốn tài nguyên server nếu không giới hạn độ sâu.

**WebSocket vs SSE vs Long Polling.** WebSocket mở 1 kết nối **2 chiều** (bi-directional), giữ liên tục — phù hợp khi cả client và server đều cần chủ động gửi dữ liệu (chat, game, cập nhật trạng thái real-time 2 chiều). SSE (Server-Sent Events) chỉ **1 chiều** (server → client), chạy trên HTTP thường và tự động reconnect khi mất kết nối — đơn giản hơn WebSocket, đủ dùng cho thông báo/notification không cần client gửi ngược lại. Long Polling (client liên tục gọi lại API, server giữ request chờ tới khi có dữ liệu mới) là cách cũ, kém hiệu quả hơn 2 cách trên — chỉ nên biết để hiểu lịch sử, không nên chọn cho thiết kế mới.

**Đọc chi tiết:** tổng hợp trong [`01-Roadmaps/Expert_Mastery_Roadmap_Project.md`](../01-Roadmaps/Expert_Mastery_Roadmap_Project.md) phần API Design. GraphQL/WebSocket/SSE: [`interview_prep/07_Cau_Hoi_Phong_Van.md`](../interview_prep/07_Cau_Hoi_Phong_Van.md) (Q20, Q33).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `interview_prep/02_Flask_Backend.md` (mục 2), `interview_prep/07_Cau_Hoi_Phong_Van.md` (Q20, Q33).

#### Chuẩn RESTful
```
GET    /users          -> list users
GET    /users/{id}     -> get user by id
POST   /users          -> create user
PUT    /users/{id}     -> update (full replace)
PATCH  /users/{id}     -> update (partial)
DELETE /users/{id}     -> delete

200 OK / 201 Created / 204 No Content
400 Bad Request / 401 Unauthorized / 403 Forbidden / 404 Not Found
409 Conflict / 422 Unprocessable / 429 Too Many Requests / 500 Internal Server
```

#### Validation với Marshmallow (Flask)
```python
class UserCreateSchema(Schema):
    name = fields.Str(required=True, validate=lambda n: len(n) >= 2)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)

@users_bp.route("/", methods=["POST"])
def create_user():
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 422
```

**PUT vs PATCH:** PUT thay thế TOÀN BỘ resource (field không gửi bị coi là xóa); PATCH chỉ cập nhật MỘT PHẦN. Update chỉ riêng email nên dùng PATCH để tránh vô tình ghi đè field khác thành rỗng.

#### WebSocket vs SSE vs Long Polling (chi tiết)
- **WebSocket:** bi-directional, persistent, tốt cho chat/game.
- **SSE:** Server→Client only, HTTP, auto-reconnect, tốt cho notification.
- **Long Polling:** legacy, không hiệu quả.

```javascript
// Next.js WebSocket với reconnection
function useWebSocket(url) {
    const [status, setStatus] = useState('connecting');
    const connect = () => {
        wsRef.current = new WebSocket(url);
        wsRef.current.onopen = () => setStatus('connected');
        wsRef.current.onclose = () => {
            setStatus('disconnected');
            reconnectTimeout.current = setTimeout(connect, 3000);  // auto-reconnect
        };
    };
}
```

#### CORS — tại sao browser block, server không block
CORS là security của browser, server nhận request bình thường. Browser check `Access-Control-Allow-Origin` header trong response. Postman/curl không có CORS vì không phải browser.

</details>

---

## PHẦN III — KIẾN TRÚC & VẬN HÀNH HỆ THỐNG

<a id="chuong-10"></a>
## Chương 10 — Request Lifecycle, Concurrency & Async trong Production

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Request lifecycle đầy đủ (Nginx/WSGI/ASGI server → middleware → view → DB → response).

🟡 **Nâng cao (trọng tâm Middle):**
- WSGI (Gunicorn) vs ASGI (Uvicorn) — khi nào cần async thật (I/O-bound nhiều).
- Background task/queue (Celery hoặc RQ) — xử lý việc nặng ngoài request-response cycle.

🔴 **Chuyên sâu / Thực chiến:**
- Thread vs Process vs Async trong Python — vì sao GIL ảnh hưởng lựa chọn này; quyết định sai ở đây là nguyên nhân phổ biến của hệ thống "chậm mà không hiểu vì sao" trong production.
- **Tuning số worker process** (`--workers` ở Gunicorn/Uvicorn) — sự cố thật hay gặp khi nghĩ "đã dùng async rồi nên khỏi cần nhiều worker".
- **Giới hạn của `BackgroundTasks`** (FastAPI) so với queue thật (Celery) — chọn sai công cụ cho task quan trọng sẽ mất dữ liệu khi server restart.

**Giải thích chi tiết:**

🟢 *Cơ bản.* **Request lifecycle.** Nginx (nhận request từ internet, có thể cache/nén/terminate SSL) → forward vào WSGI/ASGI server (Gunicorn/Uvicorn — "dịch" request HTTP thành thứ code Python hiểu) → middleware → view → DB → response đi ngược lại.

🟡 *Nâng cao.* **WSGI vs ASGI.**

| | WSGI | ASGI |
|---|---|---|
| Server tiêu biểu | Gunicorn | Uvicorn |
| Mô hình xử lý | 1 request = 1 thread/process | 1 process xử lý nhiều request **đang chờ** cùng lúc |
| Khi chờ I/O | Chặn hoàn toàn (thread đứng yên) | Nhường cho request khác chạy (event loop) |
| Hợp với | App đơn giản, CRUD thông thường | I/O-bound nhiều: gọi nhiều API ngoài, WebSocket |
| Framework | Django, Flask (mặc định) | FastAPI (mặc định), Django/Flask (ASGI mode) |

Chỉ nên đổi sang ASGI khi app thực sự I/O-bound nhiều — đổi "cho sang" mà code vẫn gọi thư viện sync bên trong sẽ dính đúng lỗi block event loop đã nói ở Chương 7.

**Background task/queue.** Việc nặng/chậm (gửi email, xuất báo cáo PDF, gọi API bên thứ 3 chậm) không nên xử lý ngay trong request-response cycle — đẩy vào hàng đợi, 1 worker riêng xử lý ở "hậu trường", trả kết quả ngay cho user là "đã nhận, đang xử lý".

🔴 *Chuyên sâu/Thực chiến.* **Thread vs Process vs Async.** Nhiều **process**: mỗi process có GIL riêng → tận dụng được nhiều CPU core thật, phù hợp CPU-bound, nhưng tốn RAM hơn. Nhiều **thread**: chia sẻ RAM, bị GIL chặn — chỉ có lợi khi task chờ I/O (vì lúc chờ I/O, GIL được nhả ra cho thread khác). **Async**: không tốn chi phí tạo thread/process, cực nhẹ, nhưng chỉ hữu ích cho I/O-bound, và 1 hàm sync chặn ở giữa sẽ phá vỡ lợi ích của cả hệ thống async.

```python
# CPU-bound (tính toán nặng) -> ProcessPoolExecutor, không phải thread/async
with ProcessPoolExecutor() as pool:
    results = pool.map(resize_image, image_list)   # mỗi process dùng 1 CPU core riêng

# I/O-bound (gọi nhiều API/DB) -> asyncio, không tốn chi phí tạo thread
async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        return await asyncio.gather(*[client.get(u) for u in urls])  # chạy đồng thời, 1 thread
```

**Tuning số worker.** 1 worker async (Uvicorn) xử lý được hàng nghìn kết nối I/O-bound đồng thời trên **1 event loop** — nhưng 1 event loop chỉ chạy trên **1 lõi CPU**. Sự cố thật hay gặp: deploy với `--workers 1` vì nghĩ "async đã nhanh rồi", chạy trên máy 8 lõi nhưng chỉ dùng được 1 lõi, throughput giảm tới 8 lần so với khả năng thật của server — luôn cần nhiều worker process (mỗi worker chạy 1 event loop riêng) để tận dụng hết CPU, số lượng tối ưu nên benchmark bằng load test thật (Chương 8), không đoán mò.

**Giới hạn của `BackgroundTasks`.** `BackgroundTasks` của FastAPI chạy **trong cùng process** với request — tiện cho việc nhỏ, nhưng nếu server restart giữa lúc task đang chạy, task **mất luôn**, không có cơ chế retry. Với tác vụ quan trọng (gửi email xác nhận thanh toán, xử lý đơn hàng), phải dùng **queue thật** (Celery + Redis/RabbitMQ đã học ở Chương 11) có persistence + retry + dead-letter-queue — đừng nhầm "chạy nền được" với "chạy nền an toàn".

**Đọc chi tiết:** [`Mastery/Backend-Mastery/01-Request-Lifecycle-And-Architecture`](../Mastery/Backend-Mastery/01-Request-Lifecycle-And-Architecture), [`02-Concurrency-And-Async-In-Production`](../Mastery/Backend-Mastery/02-Concurrency-And-Async-In-Production) (phần tuning worker + BackgroundTasks vs Celery).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `Mastery/Backend-Mastery/01-Request-Lifecycle-And-Architecture/README.md`, `Mastery/Backend-Mastery/02-Concurrency-And-Async-In-Production/README.md` — nội dung đầy đủ 2 file này đã nhúng tại [Chương 5](#chuong-5) (luồng request/middleware) và [Chương 7](#chuong-7) (GIL/worker model/BackgroundTasks), không lặp lại ở đây để tránh trùng lặp 2 lần trong cùng cuốn sách.

#### Background Task — đừng để user chờ việc không cần chờ ngay
```python
from fastapi import BackgroundTasks

@app.post("/register")
async def register(user: UserCreate, background_tasks: BackgroundTasks):
    new_user = create_user(user)
    background_tasks.add_task(send_welcome_email, new_user.email)  # không block response
    return {"id": new_user.id}
```
**Giới hạn:** `BackgroundTasks` của FastAPI chạy **trong cùng process** — nếu server restart giữa lúc task đang chạy, task **mất luôn**, không retry. Với tác vụ quan trọng, dùng queue thật (Celery + Redis/RabbitMQ, hoặc AWS SQS) có persistence + retry + dead-letter-queue.

#### Câu hỏi senior hay hỏi khi review
1. "Hàm `async def` này có gọi hàm blocking nào ẩn bên trong không?"
2. "Bạn set bao nhiêu worker process — dựa trên benchmark thật hay đoán?"
3. "Nếu server crash giữa lúc xử lý background task, dữ liệu có bị mất không? Có cơ chế retry không?"

</details>

---

<a id="chuong-11"></a>
## Chương 11 — System Design cơ bản cho Middle

> **Mục tiêu:** đủ vốn từ + tư duy để không "đứng hình" khi được hỏi "thiết kế hệ thống X" — không cần biết hết mọi công nghệ, cần biết đúng khái niệm nền, vì sao chọn cái này thay vì cái kia, và nói được trade-off.
>
> **Chương này dài nhất sách (10 mục nhỏ) — đừng học trong 1 buổi.** Chia làm 3 buổi theo đúng nhịp Thứ 2/4 (lý thuyết) + Thứ 3/5 (code theo) đã quen:
> - **Buổi 1 — Hạ tầng dữ liệu:** [11.1 Caching](#chuong-11-1) → [11.2 Message Queue](#chuong-11-2) → [11.3 Celery](#chuong-11-3)
> - **Buổi 2 — Hạ tầng mạng & lý thuyết phân tán:** [11.4 Load Balancing](#chuong-11-4) → [11.5 CDN](#chuong-11-5) → [11.6 CAP/PACELC](#chuong-11-6) → [11.7 Replication lag](#chuong-11-7)
> - **Buổi 3 — Thực hành thiết kế (nặng nhất, cần đầu óc tỉnh táo):** [11.8 URL Shortener](#chuong-11-8) → [11.9 Rate Limiter](#chuong-11-9) → [11.10 Circuit Breaker](#chuong-11-10)

<a id="chuong-11-1"></a>
### 11.1 Caching sâu — 🟡 Nâng cao

**Kiến thức cần học:**
- 🟢 Cơ bản: Local cache (in-process, `lru_cache`) vs Distributed cache (Redis) — khi nào dùng loại nào; TTL là gì.
- 🟡 Nâng cao: 3 chiến lược ghi cache: **Cache-aside** (lazy loading), **Write-through**, **Write-behind** (write-back); eviction policy **LRU** vs **LFU**.
- 🔴 Chuyên sâu/Thực chiến: **Cache stampede** (thundering herd) và 2 cách chống phổ biến — lỗi gây sập DB thật trong production nếu không biết trước.

**Giải thích chi tiết:**
- **Cache-aside** (phổ biến nhất): app tự kiểm tra cache trước, miss thì query DB rồi tự ghi lại vào cache. Đơn giản, chỉ cache đúng data đã từng được đọc — nhưng có khoảng trống giữa lúc DB đổi và cache cập nhật (phải tự invalidate đúng lúc).
- **Write-through**: mọi lần ghi DB đều ghi đồng thời vào cache trong cùng 1 luồng xử lý — cache luôn mới, nhưng chậm hơn ở write path, hợp khi đọc nhiều hơn hẳn ghi và bắt buộc cache phải đúng.
- **Write-behind** (write-back): ghi vào cache trước, bất đồng bộ đẩy xuống DB sau — write cực nhanh, nhưng rủi ro **mất dữ liệu** nếu cache sập trước khi kịp flush xuống DB; ít dùng cho dữ liệu quan trọng (tiền, đơn hàng), hay dùng cho dữ liệu chấp nhận mất được (view count, like count).
- **Cache stampede**: khi 1 cache key rất "hot" hết hạn, hàng loạt request cùng lúc đều miss cache và cùng dồn vào DB truy vấn lại → có thể làm sập DB trong tích tắc. Chống bằng: (1) **probabilistic early expiration** — gia hạn/tính lại cache sớm hơn 1 chút một cách ngẫu nhiên trước khi hết hạn thật, tránh hàng loạt key cùng hết hạn 1 lúc; (2) **lock/mutex** — chỉ cho 1 request được phép đi query DB tính lại, các request khác đợi hoặc nhận tạm bản cache cũ (stale-while-revalidate).
- **Eviction**: LRU xóa phần tử lâu không được dùng tới nhất; LFU xóa phần tử ít được dùng tới nhất (đếm tần suất truy cập) — Redis hỗ trợ cả 2 qua cấu hình `maxmemory-policy`.

<a id="chuong-11-2"></a>
### 11.2 Message Queue vs Pub/Sub — phân biệt rõ, không gộp chung — 🟡 Nâng cao

**Kiến thức cần học:**
- 🟡 Nâng cao: **Message Queue** (point-to-point): RabbitMQ, SQS — 1 message chỉ được **đúng 1 consumer** xử lý.
- 🔴 Chuyên sâu/Thực chiến: **Pub/Sub / log-based streaming**: Kafka, SNS — 1 message được **nhiều consumer group độc lập** cùng đọc; so sánh RabbitMQ vs Kafka vs SQS/SNS để chọn đúng công cụ theo đúng nhu cầu, không phải "cái nào mạnh hơn".

**Giải thích chi tiết:**
Đây là điểm hay bị nhầm: "Message Queue" không phải là 1 khái niệm duy nhất.
- **RabbitMQ** (queue cổ điển): producer đẩy message vào queue, **1 consumer duy nhất** lấy ra xử lý rồi message biến mất — đúng mô hình "hàng đợi công việc" (task queue), dùng cho Celery. Có `exchange` để routing linh hoạt (fanout, topic, direct).
- **Kafka** (log-based pub/sub): message được ghi vào 1 log bền vững, giữ lại theo thời gian cấu hình (retention) thay vì biến mất sau khi đọc — **nhiều consumer group khác nhau** có thể đọc **độc lập** cùng 1 message (VD: 1 group ghi vào DB, 1 group khác tính metrics, cùng từ 1 sự kiện "đơn hàng được tạo"). Throughput cực cao, phù hợp event streaming, audit log, không phù hợp làm "task queue" đơn giản vì phức tạp hơn hẳn RabbitMQ.
- **SQS** (AWS managed queue): giống RabbitMQ về vai trò (point-to-point), nhưng AWS tự vận hành — không cần tự host/scale broker.
- **SNS** (AWS managed pub/sub): thường đi kèm SQS theo pattern **fan-out** — 1 event publish vào SNS, SNS tự động đẩy bản sao vào nhiều SQS queue khác nhau để nhiều service cùng xử lý độc lập.
Chọn công cụ nào phụ thuộc câu hỏi: "message này cần đúng 1 nơi xử lý, hay nhiều nơi cùng cần biết?" — câu đầu dùng Queue, câu sau dùng Pub/Sub.

<a id="chuong-11-3"></a>
### 11.3 Background Task với Celery — idempotent task cụ thể hơn — 🟡 Nâng cao

**Kiến thức cần học:**
- 🟡 Nâng cao: Celery cần 1 **broker** (Redis hoặc RabbitMQ) làm nơi trung chuyển task; retry với **exponential backoff**.
- 🔴 Chuyên sâu/Thực chiến: Task phải **idempotent** — ví dụ cụ thể cách làm đúng, không chỉ nói khái niệm suông; đây là lỗi thực tế hay gặp nhất khi dùng background task cho nghiệp vụ tiền/điểm thưởng.

**Giải thích chi tiết:**
Task **không idempotent** (sai): `increment_points(user_id, 10)` — nếu Celery retry task này 2 lần do lỗi mạng tạm thời (worker đã làm xong nhưng bị mất tín hiệu ACK), user bị cộng nhầm 20 điểm thay vì 10.
Task **idempotent** (đúng): `apply_points_transaction(user_id, transaction_id, 10)` — trước khi cộng điểm, kiểm tra `transaction_id` này đã được xử lý chưa (lưu vào bảng `processed_transactions` với unique constraint trên `transaction_id`, hoặc dùng Redis `SETNX` để đánh dấu "đã xử lý"). Retry bao nhiêu lần cũng chỉ cộng điểm đúng 1 lần.

```python
@app.task(bind=True, max_retries=5)
def apply_points_transaction(self, user_id, transaction_id, points):
    if ProcessedTransaction.objects.filter(id=transaction_id).exists():
        return  # đã xử lý rồi, retry lần 2/3 không làm gì thêm

    try:
        with transaction.atomic():
            User.objects.filter(id=user_id).update(points=F("points") + points)
            ProcessedTransaction.objects.create(id=transaction_id)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)  # exponential backoff
```

**Retry với backoff**: `countdown=2 ** retry_count` — thời gian chờ giữa các lần retry tăng dần theo cấp số nhân (exponential backoff), tránh việc hàng ngàn task cùng retry dồn dập làm quá tải 1 service đang gặp sự cố (càng làm sự cố nặng thêm).

<a id="chuong-11-4"></a>
### 11.4 Load Balancing — thuật toán cụ thể, không chỉ nói chung chung — 🟡 Nâng cao

**Kiến thức cần học:**
- 🟢 Cơ bản: Horizontal vs Vertical scaling — khái niệm chung.
- 🟡 Nâng cao: 3 thuật toán LB phổ biến: **Round Robin**, **Least Connections**, **IP Hash**; vì sao horizontal scaling đòi hỏi service phải **stateless**.
- 🔴 Chuyên sâu/Thực chiến: **Consistent Hashing** — vì sao quan trọng hơn hash thường (`key % N`) khi scale cache/DB phân tán (Redis Cluster, sharding).

**Giải thích chi tiết:**
- **Round Robin**: chia request lần lượt đều cho từng server — đơn giản, không quan tâm tải thực tế mỗi server đang gánh.
- **Least Connections**: gửi request tới server đang có ít connection đang xử lý nhất — tốt hơn Round Robin khi các request có độ nặng xử lý không đều nhau.
- **IP Hash / Consistent Hashing**: cùng 1 client luôn được route vào cùng 1 server ("session affinity"/"sticky session") — cần khi server giữ state cục bộ (VD session lưu trong RAM thay vì Redis). **Consistent Hashing** còn quan trọng hơn trong thiết kế cache phân tán (Redis Cluster) hoặc sharding: hash thường kiểu `key % N` khi đổi N (thêm/bớt node) sẽ làm xáo trộn gần như toàn bộ key sang node khác; Consistent Hashing chỉ làm xáo trộn 1 phần nhỏ key khi thêm/bớt 1 node — đây là lý do nó được dùng trong Redis Cluster, DynamoDB, Cassandra.
- **Horizontal vs Vertical scaling**: scale ngang (thêm server) được ưu tiên hơn scale dọc (nâng cấp 1 server mạnh hơn) ở hệ thống hiện đại vì không có giới hạn trên và chịu lỗi tốt hơn (1 server chết không sập cả hệ thống) — nhưng đòi hỏi service phải **stateless** (không lưu state cục bộ gắn với 1 server cụ thể, VD session/file upload tạm) để load balancer tự do phân phối request tới bất kỳ server nào.

<a id="chuong-11-5"></a>
### 11.5 CDN — 🟢 Cơ bản

**Kiến thức cần học:**
- 🟢 Cơ bản: CDN (CloudFront, Cloudflare) là gì, hoạt động thế nào, dùng cho loại nội dung nào.

**Giải thích chi tiết:**
CDN đặt bản sao nội dung tĩnh (ảnh, JS, CSS, video) ở nhiều điểm (edge location) gần người dùng về mặt địa lý — giảm độ trễ (không phải đi tới tận origin server ở xa) và giảm tải trực tiếp cho origin. Chỉ hiệu quả với nội dung ít đổi (static asset) hoặc cache được theo TTL ngắn; không thay thế được cache ở tầng ứng dụng (Redis) cho dữ liệu động/cá nhân hóa theo từng user.

<a id="chuong-11-6"></a>
### 11.6 CAP theorem — phiên bản chính xác hơn + PACELC — 🔴 Chuyên sâu/Thực chiến

**Kiến thức cần học:**
- 🔴 Chuyên sâu/Thực chiến: CAP theorem đúng bản chất (không phải "chọn 2 trong 3" một cách tùy ý); **CP vs AP** — ví dụ thực tế mỗi loại; **PACELC** — mở rộng chính xác hơn CAP, áp dụng cả lúc hệ thống bình thường. Đây là nội dung hay bị dạy sai nhất trong các tài liệu phổ thông — nắm đúng sẽ ghi điểm rõ rệt ở vòng phỏng vấn senior.

**Giải thích chi tiết:**
Phiên bản hay bị hiểu sai: "hệ thống phân tán chỉ chọn được 2 trong 3 giữa Consistency, Availability, Partition tolerance". Thực tế chính xác hơn: trong hệ thống phân tán thật, **network partition (P) sẽ luôn có thể xảy ra** — đây không phải là 1 lựa chọn, mà là thực tế phải chấp nhận (mạng lúc nào cũng có thể trục trặc). Lựa chọn thật sự chỉ xuất hiện **khi partition thực sự xảy ra**: hệ thống phải chọn giữa:
- **CP** (Consistency ưu tiên hơn Availability): khi mạng bị chia cắt, thà từ chối trả lời (tạm ngưng phục vụ 1 phần) còn hơn trả về dữ liệu cũ/sai — VD hệ thống ngân hàng, hệ thống đặt vé/đặt chỗ (không được bán trùng 1 vé cho 2 người).
- **AP** (Availability ưu tiên hơn Consistency): khi mạng bị chia cắt, vẫn tiếp tục trả lời (có thể bằng dữ liệu hơi cũ) thay vì từ chối phục vụ — VD newsfeed mạng xã hội, giỏ hàng thương mại điện tử.
Mở rộng chính xác hơn nữa là **PACELC**: "**nếu có Partition (P)** thì đánh đổi Availability và Consistency (giống CAP) — **Else** (lúc mạng hoạt động bình thường, không có partition) thì vẫn phải đánh đổi giữa **Latency (L)** và **Consistency (C)**". Lý do: ngay cả khi mạng ổn định hoàn toàn, muốn dữ liệu nhất quán tuyệt đối giữa nhiều node (phải chờ tất cả node xác nhận ghi xong) vẫn tốn thời gian hơn hẳn so với trả lời ngay từ node gần nhất (nhưng có thể hơi cũ). PACELC giải thích được nhiều quyết định thiết kế DB mà CAP một mình không giải thích nổi.

<a id="chuong-11-7"></a>
### 11.7 Consistency model & Replication lag (liên hệ trực tiếp Chương 3) — 🔴 Chuyên sâu/Thực chiến

**Kiến thức cần học:**
- 🔴 Chuyên sâu/Thực chiến: **Eventual consistency** khi dùng read replica — replication lag là gì; kỹ thuật "read-your-writes" để xử lý lag đúng chỗ cần — thường chỉ phát hiện ra vấn đề này sau khi đã gặp bug thật trong production.

**Giải thích chi tiết:**
Khi dùng read replica (Chương 3) để scale read, phải chấp nhận **eventual consistency**: dữ liệu vừa ghi vào primary có thể chưa kịp đồng bộ sang replica (replication lag thường vài chục mili-giây tới vài giây tùy tải). Hệ quả thực tế: user vừa tạo đơn hàng (ghi vào primary) rồi load lại trang ngay lập tức (đọc từ replica do cân bằng tải), có thể **tạm thời không thấy đơn hàng vừa tạo** — đây không phải bug, mà là đặc tính cố hữu của kiến trúc replica. Cách xử lý đúng: những màn hình cần đọc lại chính xác dữ liệu vừa ghi (VD trang xác nhận đơn hàng ngay sau khi submit) thì đọc từ **primary** ("read-your-writes"); các màn hình khác không cần tức thời tuyệt đối (VD danh sách sản phẩm) thì đọc từ **replica** để giảm tải cho primary.

<a id="chuong-11-8"></a>
### 11.8 Design walkthrough: URL Shortener — 🔴 Chuyên sâu/Thực chiến (bài phỏng vấn kinh điển)

**Giải thích chi tiết (đi từng bước thiết kế thật):**
1. API: `POST /shorten {long_url}` → trả về `short_code`; `GET /{short_code}` → redirect sang `long_url`.
2. Sinh `short_code`: cách phổ biến và rẻ nhất là lấy 1 **counter tăng dần** (ID auto-increment từ DB hoặc `INCR` trong Redis) rồi **encode sang base62** (gồm `0-9a-zA-Z`, 62 ký tự) để ra 1 chuỗi ngắn — tránh sinh ngẫu nhiên vì sinh ngẫu nhiên phải query kiểm tra trùng trước khi lưu, tốn thêm round-trip DB không cần thiết.
3. Lưu mapping `short_code → long_url` vào DB; **cache** các `short_code` hot bằng Redis theo kiểu cache-aside (mục 11.1), vì hành vi đọc (redirect) xảy ra nhiều hơn hành vi ghi (tạo link mới) gấp nhiều lần.
4. Chọn **301 (Permanent Redirect)** hay **302 (Temporary Redirect)**: 301 được trình duyệt/CDN tự cache lại — giảm tải cho server về sau nhưng mất khả năng đổi đích link hoặc đếm chính xác số lượt click (trình duyệt sẽ không gọi lại server những lần sau); 302 không bị cache, tốn tải hơn nhưng cho phép tracking/analytics chính xác mỗi lần click — hầu hết dịch vụ rút gọn link thật (bit.ly) dùng 302 vì cần đếm click.
5. Khi scale: nếu 1 DB không chịu nổi tải ghi/đọc, cân nhắc sharding theo khoảng giá trị của `short_code` (liên hệ Chương 3) — nhưng ở mức phỏng vấn Middle, nêu đúng "counter + base62 encode + cache-aside + trade-off 301 vs 302" là đã thể hiện đủ chiều sâu.

<a id="chuong-11-9"></a>
### 11.9 Design walkthrough: Rate Limiter — 🔴 Chuyên sâu/Thực chiến (nối trực tiếp thuật toán Token Bucket đã nêu ở Chương 12)

**Giải thích chi tiết (cách cài đặt thật bằng Redis):**
1. Mỗi user/IP có 1 key Redis lưu "số token hiện có" + "thời điểm nạp token gần nhất".
2. Mỗi khi có request tới: tính số token được nạp thêm kể từ lần trước tới giờ (theo tốc độ nạp cố định, VD 10 token/giây), cộng dồn vào (không vượt quá dung lượng bucket tối đa), rồi trừ đi 1 token cho request hiện tại.
3. Nếu số token còn lại ≥ 0 → cho request đi qua; nếu âm → từ chối, trả về **HTTP 429 Too Many Requests**.
4. Dùng **Redis** vì 2 lý do: (a) cần tốc độ cực cao vì **mọi** request đều phải check qua bước này; (b) cần **chia sẻ trạng thái giữa nhiều instance server** — không thể lưu số token trong RAM của 1 server vì load balancer có thể route cùng 1 user sang server khác ở request kế tiếp, khiến giới hạn bị vô hiệu.

```python
def is_allowed(user_id: str, rate: int = 10, capacity: int = 20) -> bool:
    key = f"rate_limit:{user_id}"
    now = time.time()
    tokens, last_refill = redis.hmget(key, "tokens", "last_refill") or (capacity, now)

    elapsed = now - float(last_refill)
    tokens = min(capacity, float(tokens) + elapsed * rate)  # nạp token theo thời gian trôi qua

    if tokens < 1:
        return False  # hết token -> HTTP 429

    redis.hmset(key, {"tokens": tokens - 1, "last_refill": now})
    return True
```

5. Thuật toán thay thế: **Sliding Window Log** (lưu lại timestamp của từng request trong cửa sổ thời gian, chính xác tuyệt đối nhưng tốn bộ nhớ theo số lượng request) vs **Sliding Window Counter** (xấp xỉ bằng cách nội suy có trọng số giữa số request ở window hiện tại và window ngay trước đó — tốn ít bộ nhớ hơn hẳn, đủ chính xác cho tuyệt đại đa số use case thực tế).

<a id="chuong-11-10"></a>
### 11.10 Circuit Breaker Pattern — 🔴 Chuyên sâu/Thực chiến

**Kiến thức cần học:**
- 🔴 Chuyên sâu/Thực chiến: Circuit Breaker — ngăn 1 service lỗi làm sập dây chuyền cả hệ thống; khác với retry/backoff ở mục 11.3 (retry giúp chịu lỗi **tạm thời**, circuit breaker giúp chịu lỗi **kéo dài**).

**Giải thích chi tiết:**
Khi service A gọi service B mà B đang lỗi/chết, nếu A cứ tiếp tục gọi và **chờ timeout** mỗi lần (VD 5 giây/request) — hàng trăm request đồng thời tới A sẽ đều bị giữ lại chờ B, làm cạn kiệt thread/connection pool của chính A, khiến A cũng sập theo dù lỗi gốc chỉ ở B (hiệu ứng lỗi dây chuyền). Circuit Breaker "ngắt mạch" sau khi phát hiện B lỗi liên tục quá 1 ngưỡng (VD 5 lần lỗi liên tiếp): trong khoảng thời gian tiếp theo (VD 30 giây), A **fail fast** — trả lỗi ngay lập tức cho mọi request gọi tới B mà **không cần chờ timeout**, tự bảo vệ tài nguyên của chính mình. Sau thời gian đó, circuit tự chuyển sang trạng thái "half-open" — cho phép 1 request thử lại; nếu thành công thì đóng mạch trở lại (hoạt động bình thường), nếu vẫn lỗi thì tiếp tục mở mạch.

```python
from circuitbreaker import circuit

@circuit(failure_threshold=5, recovery_timeout=30)
def call_payment_service(order_id):
    response = requests.post(PAYMENT_URL, json={"order": order_id}, timeout=5)
    return response.json()
# Sau 5 lần lỗi liên tiếp: mở mạch 30s, fail fast ngay (không chờ timeout 5s mỗi lần)
```

Đây là câu hỏi debug kinh điển ở vòng phỏng vấn senior: "1 microservice liên tục timeout, bạn debug thế nào" — quy trình chuẩn là kiểm tra health service → kiểm tra downstream nó gọi → xem distributed tracing (Chương 13) → kiểm tra timeout config → áp dụng circuit breaker nếu downstream không ổn định.

**Đọc chi tiết:** [`Mastery/Cloud-DevOps-Mastery/01-Cloud-Foundations-Real-Decisions`](../Mastery/Cloud-DevOps-Mastery/01-Cloud-Foundations-Real-Decisions) + [`Mastery/Career-Mastery/02-System-Design-Interview-Playbook`](../Mastery/Career-Mastery/02-System-Design-Interview-Playbook) (đọc trước phần nền tảng, phần luyện phỏng vấn để ở Chương 20). Phần Celery/Caching Strategy chi tiết: [`03-Python-Expert/Python_Backend_Professional_Guide.md`](../03-Python-Expert/Python_Backend_Professional_Guide.md) mục 8. Circuit Breaker + quy trình debug microservice timeout: [`interview_prep/07_Cau_Hoi_Phong_Van.md`](../interview_prep/07_Cau_Hoi_Phong_Van.md) (Q125).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `03-Python-Expert/Python_Backend_Professional_Guide.md` (mục 8), `interview_prep/07_Cau_Hoi_Phong_Van.md` (Q53-56, Q116-125), `Mastery/Cloud-DevOps-Mastery/01-Cloud-Foundations-Real-Decisions/README.md`. Khung 5 bước System Design Interview đầy đủ đã nhúng ở [Chương 20](#chuong-20) để tránh trùng lặp.

#### Scalability — xử lý hàng triệu request
**Background Tasks (Celery & Redis):** API nhận yêu cầu → gửi task vào hàng đợi Redis → trả "Đang xử lý" ngay. Celery Worker lấy task ra làm việc ngầm. **Caching Strategy:** thay vì query DB 1000 lần cho cùng dữ liệu, lưu vào Redis Cache với TTL ngắn — tốc độ tăng gấp 100 lần. **Database Optimization:** Indexing cho cột hay dùng trong WHERE; Connection Pooling (SQLAlchemy/asyncpg) giữ kết nối luôn sẵn sàng.

#### Thiết kế URL Shortener (bit.ly)
1. **Generate short ID:** Base62 encode, 7 ký tự = 62⁷ ≈ 3.5 tỷ.
2. **Store:** Redis (hot URLs) + PostgreSQL (cold storage).
3. **Redirect:** 301 (cached) vs 302 (analytics count).
4. **Scale:** CDN cho static assets, DB read replicas.

#### Thiết kế Notification System (email, SMS, push)
1. **Producer:** API nhận request → Kafka/RabbitMQ.
2. **Workers:** Celery worker riêng theo từng kênh (email/SMS/push).
3. **Retry:** Exponential backoff với dead-letter queue.
4. **Deduplication:** Redis tránh gửi trùng.

#### Horizontal vs Vertical scaling
Vertical (scale up): nâng cấu hình server — đơn giản nhưng có giới hạn. Horizontal (scale out): thêm server — không giới hạn nhưng cần app **stateless** (session trong Redis, file trong S3, không lưu trong RAM server).

#### Caching strategies — tổng hợp
Cache-aside (Lazy): app check cache, miss → query DB → store cache. Write-through: ghi cache+DB đồng thời (consistent, write latency cao hơn). Write-behind: ghi cache trước, async ghi DB sau (nhanh, rủi ro mất data). Cache invalidation là bài toán khó nhất — TTL, event-based, version keys.

#### Tình huống thực tế — API chậm bất ngờ, troubleshoot
1. Monitor trước: response time, error rate, CPU/RAM/DB metrics.
2. Isolate: endpoint nào chậm, chậm từ khi nào, có traffic spike không.
3. DB queries: enable slow query log, `EXPLAIN ANALYZE`.
4. External dependencies: API bên thứ 3 có chậm không (circuit breaker)?
5. Memory: memory leak? GC pause?
6. Code: deploy gần đây? Profile bằng `cProfile`/`py-spy`.

#### Xử lý task lớn (migrate 1 triệu record) — batch + idempotent
```python
def migrate_in_batches(batch_size=1000):
    offset = 0
    while True:
        batch = get_batch(offset, batch_size)
        if not batch:
            break
        process_batch(batch)
        offset += batch_size
        log_progress(offset)  # checkpoint

@celery.task(bind=True, max_retries=3)
def migrate_batch(self, offset, batch_size):
    try:
        process_batch(offset, batch_size)
    except Exception as exc:
        self.retry(exc=exc, countdown=60)
```
Nguyên tắc: batch processing, chạy dưới dạng background job, progress tracking (Redis), **idempotent** để resume được nếu crash giữa chừng, monitor logs/metrics/ETA.

#### Deploy xong bị lỗi production — rollback
```bash
# Kubernetes
kubectl rollout undo deployment/myapp
kubectl rollout history deployment/myapp

# Lesson: Blue-Green deployment → rollback = đổi traffic, không rollback DB
```

#### Estimate thời gian cho 1 task — breakdown trước, không estimate thẳng
```
Task: "Thêm feature export CSV"
1. Research/Understand requirements: 0.5h
2. Design DB query: 1h
3. Backend endpoint: 2h
4. Streaming file response: 1h (+1h buffer lần đầu làm)
5. Frontend download button: 1h
6. Tests: 1.5h
7. PR review + fixes: 0.5h
Total: ~8h → Communicate: "1.5 ngày để có buffer cho unknowns"
Rule: Estimate × 1.5 cho task quen thuộc, × 2 cho task chưa từng làm.
```

#### Một microservice liên tục timeout — debug thế nào
1. Check service health: CPU, RAM, threads, connection pool.
2. Check downstream: service này gọi service nào? DB? External API?
3. Distributed tracing: Jaeger, Zipkin, AWS X-Ray.
4. Timeout config: có đang wait quá lâu cho dependency không?
5. Circuit breaker: nếu downstream unreliable, fail fast thay vì wait.
6. Resource exhaustion: thread pool đầy? connection pool đầy?

*(VPC Design 3-tier "defense in depth" — xem [Chương 16](#chuong-16), không lặp lại ở đây để tránh trùng lặp.)*

</details>

---

<a id="chuong-12"></a>
## Chương 12 — Security cơ bản cho Backend

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- OWASP Top 10 (SQL Injection, XSS, CSRF, Broken Auth...) — hiểu cách framework (Django) đã chặn sẵn và chỗ vẫn phải tự lo.
- Authentication vs Authorization — phân biệt rõ, nhiều người nhầm.
- HTTPS/TLS cơ bản, CORS đúng cách (không set `*` cho production).

🟡 **Nâng cao (trọng tâm Middle):**
- **JWT** có cấu trúc 3 phần (header.payload.signature), access token (sống ngắn) + refresh token (sống dài).
- Secret management: không hardcode secret, dùng `.env`/vault, xoay secret định kỳ.
- **Logging security**: nên log gì (login event, authorization failure) và tuyệt đối không log gì (password, token, số thẻ) — lỗi tưởng vô hại nhưng gây lộ dữ liệu nhạy cảm qua chính hệ thống log.

🔴 **Chuyên sâu / Thực chiến:**
- **OAuth2** ở mức khái niệm (login bằng Google/Facebook hoạt động thế nào — Authorization Code flow).
- **Rate limiting algorithm**: Token Bucket vs Fixed Window — vì sao Fixed Window có thể bị lách ở biên thời gian (xem cài đặt thật ở Chương 11 mục 11.9).
- **Secret management ở quy mô production**: HashiCorp Vault, AWS Secrets Manager, Kubernetes Secrets (nên kết hợp Sealed Secrets/External Secrets Operator thay vì Secret thuần vì base64 không phải mã hóa).
- **Dependency vulnerability scanning**: tìm lỗ hổng bảo mật nằm trong chính thư viện bên thứ 3 đang dùng, không phải trong code tự viết.

**Giải thích chi tiết:**

🟢 *Cơ bản.* **OWASP Top 10 — Django đã chặn gì sẵn.** Django tự chống SQL Injection (ORM tự escape tham số, miễn không tự nối chuỗi SQL tay), tự chống CSRF (CSRF token trong form), tự escape HTML trong template (chống XSS cơ bản). Vẫn phải tự lo: XSS khi tự render HTML không qua template engine, broken auth nếu tự viết logic login thay vì dùng hệ thống auth có sẵn.

```python
# NGUY HIỂM — tự nối chuỗi SQL, dính SQL Injection
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
# attacker truyền user_id = "1 OR 1=1" -> lộ toàn bộ bảng users

# AN TOÀN — ORM tự escape tham số (hoặc raw SQL dùng params)
User.objects.filter(id=user_id)
cursor.execute("SELECT * FROM users WHERE id = %s", [user_id])
```

🟡 *Nâng cao.* **JWT structure.** JWT gồm 3 phần nối bằng dấu chấm: `header.payload.signature` — header/payload chỉ là base64 (ai cũng **đọc** được, không phải mã hóa), signature dùng để server xác minh token **không bị sửa**. Vì vậy không bao giờ nhét mật khẩu hay dữ liệu nhạy cảm vào payload JWT.

```
eyJhbGciOiJIUzI1NiJ9 . eyJ1c2VyX2lkIjoxMjN9 . 4f8a2c1e9b...
      header                 payload              signature
   (base64, đọc được)    (base64, đọc được)   (chứng minh token không bị sửa)
```

**Logging security.** Nên log: sự kiện authentication (login thành công/thất bại, logout), authorization failure (403), thao tác sửa/xóa dữ liệu nhạy cảm, lỗi hệ thống, API call kèm `timestamp`/`user_id`/`endpoint`. **Tuyệt đối không log**: password (kể cả đã hash), số thẻ/CVV, JWT token, API key/secret, dữ liệu cá nhân nhạy cảm — log quá chi tiết tưởng "để dễ debug" nhưng thực chất mở ra 1 kênh rò rỉ dữ liệu khác mà team security ít để ý tới vì không nghĩ log cũng là nơi cần bảo vệ.

🔴 *Chuyên sâu/Thực chiến.* **OAuth2.** Login bằng Google về cơ bản: app redirect user sang Google → user đồng ý → Google redirect lại kèm 1 "authorization code" → app dùng code đó đổi lấy access token từ Google (đổi ở backend, không lộ ra trình duyệt).

**Rate limiting: Token Bucket vs Fixed Window.** Fixed Window (VD giới hạn 100 request/phút theo khung phút tròn) có kẽ hở: user có thể gửi 100 request vào giây cuối của phút này + 100 request vào giây đầu phút sau = 200 request trong 2 giây. Token Bucket (bucket chứa token, mỗi request tiêu 1 token, token nạp lại đều theo thời gian) mượt hơn, không có hiện tượng dồn cục ở biên thời gian — cách cài đặt cụ thể bằng Redis xem Chương 11 mục 11.9.

**Secret management ở quy mô production.** `.env` chỉ đủ cho local/dev. Ở production: HashiCorp Vault (quản lý secret tập trung, hỗ trợ xoay vòng tự động và audit log ai đọc secret gì), AWS Secrets Manager (bản managed tương đương trên AWS, liên hệ Chương 16), Kubernetes Secret mặc định chỉ encode base64 (không phải mã hóa — ai có quyền đọc etcd đều đọc được) nên production nên dùng thêm Sealed Secrets (mã hóa secret ngay trong Git, chỉ cluster đích mới giải mã được) hoặc External Secrets Operator (đồng bộ secret từ Vault/AWS Secrets Manager vào K8s tự động thay vì lưu trực tiếp).

**Dependency vulnerability scanning.** Lỗ hổng bảo mật không chỉ nằm trong code tự viết mà còn nằm trong hàng trăm package bên thứ 3 project đang phụ thuộc (CVE đã công bố). `safety check`/`pip-audit` quét `requirements.txt` tìm CVE đã biết; GitHub Dependabot tự động tạo PR cập nhật khi phát hiện dependency có lỗ hổng; Snyk/OWASP Dependency-Check là lựa chọn mạnh hơn cho công ty lớn. Nguyên tắc: pin chính xác version trong `requirements.txt`/lock file (Chương 1), cập nhật định kỳ thay vì để quá cũ, đọc changelog trước khi nâng version lớn (major) để tránh breaking change bất ngờ.

**Đọc chi tiết:** [`interview_prep/05_Docker_DevOps.md`](../interview_prep/05_Docker_DevOps.md) phần security, bài tập DO-05 (Secret Management) trong [`03-DevOps-Exercises/Checklist_Bai_Tap.md`](03-DevOps-Exercises/Checklist_Bai_Tap.md). Logging security, Vault/K8s Secrets, Dependency scanning: [`interview_prep/07_Cau_Hoi_Phong_Van.md`](../interview_prep/07_Cau_Hoi_Phong_Van.md) (Q40, Q94, Q95).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `interview_prep/07_Cau_Hoi_Phong_Van.md` (Q86-95, Q40).

#### OWASP Top 10 — đầy đủ
1. Broken Access Control — User A truy cập data của User B.
2. Cryptographic Failures — dùng MD5/SHA1 cho password.
3. Injection — SQL/NoSQL/Command Injection.
4. Insecure Design — logic flaws trong business rules.
5. Security Misconfiguration — default password, debug mode in prod.
6. Vulnerable Components — thư viện cũ với CVE đã biết.
7. Authentication Failures — weak password, no rate limiting.
8. Data Integrity Failures — deserialize untrusted data.
9. Logging Failures — không log security events.
10. SSRF — server-side request forgery.

#### Password storage — đúng cách
```python
import bcrypt
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
# SAI: MD5, SHA1 (nhanh → dễ brute force), Plain text, Encrypt (có thể decrypt), Hash không salt
```
Best practices: minimum 12 rounds bcrypt; Argon2id cho ứng dụng mới (winner PHC); Pepper (server-side secret) + Salt (per-user).

#### XSS — các loại và phòng tránh
**Stored XSS:** script lưu vào DB, chạy khi load page. **Reflected XSS:** script trong URL parameter. **DOM XSS:** JS trực tiếp manipulate DOM không sanitize.
```javascript
// NGUY HIỂM
document.innerHTML = userInput;
// AN TOÀN
document.textContent = userInput;  // auto-escape
```

#### CSRF
Attacker trick user submit form tới site mà user đang authenticated. Phòng tránh: CSRF token (random, per-session), `SameSite=Strict` cookie, check `Origin`/`Referer` header.

#### HTTPS, TLS, HSTS, Certificate Pinning
```python
from flask_talisman import Talisman
Talisman(app, force_https=True, strict_transport_security=True,
    content_security_policy={'default-src': "'self'"})
```

#### API Security checklist
1. Authentication: JWT short expiry (15 phút) + refresh token.
2. Authorization: RBAC, check ownership.
3. Rate Limiting: chống brute force/DDoS.
4. Input Validation: whitelist > blacklist.
5. HTTPS only. 6. API versioning. 7. Error messages không leak stack trace. 8. Logging auth attempts. 9. CORS strict whitelist. 10. Secrets qua env vars, không trong code.

#### Secrets trong Docker — 4 cách
1. Docker Secrets (Swarm mode). 2. Environment variables từ `.env` (không commit). 3. Vault (HashiCorp) cho production. 4. Kubernetes Secrets (base64, nên dùng Sealed Secrets). **Không bao giờ:** hardcode trong Dockerfile hoặc commit `.env`.

</details>

---

<a id="chuong-13"></a>
## Chương 13 — Observability: Logging, Monitoring, Debugging Production

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Structured logging (log có format JSON, dễ query) thay vì `print()`.
- Metrics cơ bản (latency, error rate, throughput — "3 chỉ số vàng"), mở rộng thành Golden Signals.

🟡 **Nâng cao (trọng tâm Middle):**
- **Công cụ cụ thể**: Prometheus + Grafana + Alertmanager; ELK/EFK stack hoặc Grafana Loki.
- **Node Exporter / cAdvisor** — exporter thu thập metrics hệ thống (CPU/RAM/disk) và metrics container cho Prometheus đọc — không có 2 công cụ này, Prometheus chỉ thấy metrics do app tự expose, không thấy sức khỏe hạ tầng bên dưới.
- Debug production: đọc log để tái hiện lỗi không reproduce được ở local.

🔴 **Chuyên sâu / Thực chiến:**
- **Distributed Tracing** (Jaeger/OpenTelemetry) — theo dõi 1 request đi qua nhiều service.
- Alerting — SLO-based alerting (theo error budget), tránh "alert fatigue".

**Giải thích chi tiết:**

🟢 *Cơ bản.* **3 trụ cột: Metrics — Logs — Traces (phần Metrics & Logs).** Metrics là con số theo thời gian (latency, CPU, số request/giây). Logs là chi tiết từng sự kiện (biết **chuyện gì** đã xảy ra) — nên là structured logging (JSON) để query được, thay vì text tự do khó parse.

```python
logger.info("order_created", extra={
    "order_id": order.id,
    "user_id": user.id,
    "total": order.total,
})
# {"message": "order_created", "order_id": 42, "user_id": 7, "total": 150.0, "timestamp": "..."}
# -> query được: "tìm mọi log có order_id=42" thay vì grep text tự do
```

**Golden Signals.** Latency (độ trễ), Traffic (lượng request), Errors (tỉ lệ lỗi), Saturation (hệ thống đang "đầy" tới đâu — CPU/RAM/connection pool) — 4 chỉ số đầu tiên cần nhìn khi có sự cố, trước khi đào sâu hơn.

🟡 *Nâng cao.* **Công cụ cụ thể.** Prometheus thu thập metrics theo kiểu **pull** (chủ động tới hỏi app "/metrics endpoint" theo chu kỳ), Grafana vẽ thành dashboard; ELK/Loki dùng để tập trung và query log.

```python
from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter("http_requests_total", "Total requests", ["endpoint", "status"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Request latency")

@app.middleware("http")
async def track_metrics(request, call_next):
    with REQUEST_LATENCY.time():
        response = await call_next(request)
    REQUEST_COUNT.labels(endpoint=request.url.path, status=response.status_code).inc()
    return response
# Prometheus tới scrape /metrics theo chu kỳ, Grafana đọc từ Prometheus vẽ dashboard
```

🔴 *Chuyên sâu/Thực chiến.* **Distributed Tracing.** Traces theo dõi 1 request đi qua **nhiều service** mất bao lâu ở từng chặng — cần gắn `trace_id` xuyên suốt để nối log/span lại với nhau (Jaeger/OpenTelemetry).

**SLO-based alerting, alert fatigue.** Thay vì báo động ngay khi CPU > 80% (có thể chỉ là spike tạm thời, vô hại), SLO-based alerting báo động khi **error budget** (ngân sách lỗi cho phép, theo cam kết SLA) sắp cạn — giảm số lần báo động giả, tránh team "quen tay" bỏ qua alert vì bị spam quá nhiều.

**Đọc chi tiết:** [`Mastery/Backend-Mastery/04-Testing-Observability-And-Debugging-Prod`](../Mastery/Backend-Mastery/04-Testing-Observability-And-Debugging-Prod), [`Mastery/Cloud-DevOps-Mastery/05-Observability-Incident-Response`](../Mastery/Cloud-DevOps-Mastery/05-Observability-Incident-Response). Công cụ Prometheus/Grafana/ELK/Tracing: [`10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md`](../10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md) — Học phần 7 (Monitoring).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md` (Học phần 7), `Mastery/Cloud-DevOps-Mastery/05-Observability-Incident-Response/README.md`.

#### 3 trụ cột Observability

| Trụ cột | Trả lời câu hỏi | Công cụ thật |
|---|---|---|
| Logs | "Chuyện gì đã xảy ra?" | ELK Stack, CloudWatch Logs |
| Metrics | "Hệ thống đang khỏe không?" | Prometheus + Grafana |
| Traces | "Request đi qua bao nhiêu service, tốn bao lâu?" | Jaeger, AWS X-Ray, OpenTelemetry |

#### SLI / SLO / SLA

| Khái niệm | Ý nghĩa | Ví dụ |
|---|---|---|
| SLI | Chỉ số đo lường thực tế | "99.95% request < 200ms trong 30 ngày" |
| SLO | Mục tiêu nội bộ | "p99 latency < 300ms, uptime > 99.9%" |
| SLA | Cam kết khách hàng (có ràng buộc) | "uptime 99.9%, vi phạm hoàn tiền X%" |

SLO luôn phải **chặt hơn** SLA — là nền tảng của **Error Budget**: hệ thống chạy tốt hơn SLO nhiều → có "ngân sách rủi ro" để deploy nhanh hơn; sát ngưỡng SLO → ưu tiên ổn định hơn tính năng mới.

#### Quy trình xử lý sự cố (Incident Response)
```
1. PHÁT HIỆN (alert bắn / user báo cáo)
2. ĐÁNH GIÁ MỨC ĐỘ — ảnh hưởng bao nhiêu % user? Mất dữ liệu không?
3. GIẢM THIỂU NGAY — ƯU TIÊN SỐ 1, KHÔNG PHẢI tìm nguyên nhân gốc trước
   → rollback? tắt feature flag? scale thêm? failover region khác?
4. THÔNG BÁO (status page, nội bộ/khách hàng)
5. XÁC NHẬN ĐÃ ỔN — golden signals trở lại bình thường
6. ĐIỀU TRA NGUYÊN NHÂN GỐC — SAU KHI đã ổn định
7. POSTMORTEM — blameless, action item cụ thể
```
**Sai lầm senior cảnh báo junior:** cố fix "nguyên nhân gốc" NGAY trong lúc sự cố thay vì giảm thiểu tác động trước — rollback thường an toàn hơn "vá nóng" giữa sự cố.

#### Postmortem — văn hóa phân biệt team trưởng thành
**Blameless** (không quy trách nhiệm cá nhân) là nguyên tắc bắt buộc. Gồm: Timeline chi tiết, Impact (bao nhiêu user/bao lâu), 5 Whys để đào tới nguyên nhân gốc thật (thường là vấn đề quy trình — thiếu test/alert/review, không phải "dev đó code dở"), Action items cụ thể có người phụ trách + deadline.

#### Lab thực chiến (Học phần 7 — Monitoring)
1. Dựng bộ Prometheus + Grafana + Node Exporter bằng Docker Compose, tạo dashboard theo dõi CPU/RAM/Disk của server.
2. Cấu hình Alertmanager gửi cảnh báo qua Telegram khi CPU > 80% trong 5 phút.
3. Thêm `/metrics` endpoint tùy chỉnh (custom metrics) vào 1 app Node.js/Flask để Prometheus scrape (VD: số request/giây, latency).

**Node Exporter / cAdvisor** — exporter thu thập metrics hệ thống (Node Exporter) và container (cAdvisor) để Prometheus scrape; đây là cách Prometheus "nhìn thấy" CPU/RAM/Disk của host và container mà không cần sửa code app.

**ELK/EFK Stack** (Elasticsearch – Logstash/Fluentd – Kibana) hoặc **Grafana Loki** — 2 trường phái tập trung & tìm kiếm log: ELK mạnh về full-text search nhưng nặng tài nguyên; Loki index theo label (giống Prometheus) nên nhẹ hơn nhiều, phù hợp khi đã dùng sẵn Grafana.

**Distributed Tracing** (Jaeger/OpenTelemetry) — theo dõi 1 request đi qua nhiều microservice, mỗi service ghi lại 1 "span" gắn `trace_id` chung — đây là cách duy nhất debug được "request chậm ở đâu" khi hệ thống có hơn 1 service.

**SLO-based Alerting** — cảnh báo dựa trên error budget (vd: "đã dùng 80% error budget tháng này") thay vì ngưỡng CPU/Memory đơn thuần, giúp tránh "alert fatigue" vì chỉ báo khi thực sự ảnh hưởng tới cam kết SLO.

#### Sự cố thường gặp (Học phần 7 Monitoring)
- **Alert Fatigue** — ngưỡng quá nhạy khiến Slack/Telegram spam, team bỏ qua cả alert thật.
- **Dashboard đẹp nhưng vô dụng khi sự cố** — thiếu dashboard theo Golden Signals.
- **Prometheus mất data sau restart** — quên cấu hình persistent volume.
- **Log đầy ổ đĩa/tốn chi phí ELK** — thiếu retention policy.
- **Không tương quan được log-metric-trace** — thiếu `trace_id` xuyên suốt service.

</details>

---

## PHẦN IV — DEVOPS

> **Nền tảng trước khi vào công cụ (tương ứng Học phần 1 "Fundamental" trong lộ trình 9 học phần):** DevOps là **văn hóa** xóa bỏ ranh giới Dev (viết code) và Ops (vận hành), mục tiêu là release nhanh, ổn định, tự động hóa — không phải một công cụ cụ thể nào. Vòng đời phần mềm (SDLC) là vòng lặp vô hạn: **Plan → Code → Build → Test → Release → Deploy → Operate → Monitor** rồi quay lại Plan — mỗi chương 14-19 dưới đây tương ứng với 1-2 bước trong vòng lặp này (Ch.14-15 = Build/Test, Ch.16-18 = Release/Deploy, Ch.19 = Operate/Monitor). Agile/Scrum (Sprint, Backlog, Stand-up, Retro) là quy trình làm việc nhóm mà pipeline DevOps luôn gắn kèm — bạn đã va chạm qua ở công việc hiện tại nên không cần học lại từ đầu, chỉ cần biết thuật ngữ đúng chuẩn khi phỏng vấn.

<a id="chuong-14"></a>
## Chương 14 — Linux/Shell & Docker

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Lệnh Linux cơ bản (`cd`, `grep`, `ps`, `top`) — đã dùng qua.
- Đọc log hệ thống, quản lý process, quyền file (`chmod`/`chown`).
- **Networking nền tảng**: mô hình OSI (chỉ cần nhớ tầng 3-Network, 4-Transport, 7-Application), khái niệm IP/Port/DNS/HTTP-HTTPS — nền để hiểu mọi công cụ DevOps phía sau.
- **Virtualization (máy ảo) vs Containerization (container)** — máy ảo ảo hóa cả phần cứng + OS riêng (nặng, cô lập mạnh); container chỉ ảo hóa ở tầng process, dùng chung kernel OS (nhẹ, khởi động nhanh) — đây là lý do Docker phổ biến hơn VM cho microservice.
- **Docker**: image vs container, Dockerfile cơ bản.

🟡 **Nâng cao (trọng tâm Middle):**
- **Network troubleshooting cơ bản**: `netstat`/`ss -tulpn`, `curl`, `dig/nslookup`, `traceroute`, `iptables/ufw`.
- **Docker**: multi-stage build (giảm size image).
- **Docker Compose**: nhiều service cùng chạy (app + DB + Redis), volume (giữ data khi restart).

🔴 **Chuyên sâu / Thực chiến:**
- Phân biệt Load Balancer **Layer 4** vs **Layer 7**.
- Debug container: `docker logs`, `docker exec`, lỗi hết dung lượng ổ đĩa ảo — sự cố thực tế hay gặp nhất khi vận hành Docker lâu dài.

**Giải thích chi tiết:**

🟢 *Cơ bản.* **Networking nền tảng.** Mô hình OSI 7 tầng chỉ cần nhớ 3 tầng hay dùng: tầng 3 (Network — định tuyến theo IP), tầng 4 (Transport — TCP/UDP, nơi khái niệm "port" sống), tầng 7 (Application — HTTP/HTTPS, nơi code của bạn thực sự làm việc). Hiểu đúng tầng nào xử lý gì giúp đọc lỗi mạng (connection refused, timeout, DNS not found) nhanh hơn thay vì đoán mò.

**Virtualization vs Containerization.** Máy ảo (VM) chạy qua hypervisor, mỗi VM có kernel OS riêng — cô lập mạnh nhưng nặng, khởi động chậm (tính bằng phút). Container (Docker) dùng chung kernel của host, chỉ cô lập ở tầng process/filesystem — nhẹ hơn nhiều, khởi động nhanh (tính bằng giây), nhưng cô lập yếu hơn VM (nếu kernel host có lỗ hổng, ảnh hưởng tới mọi container).

**Docker: image vs container.** Image là "bản thiết kế đóng gói sẵn", container là "1 instance đang chạy" từ image đó — giống class vs object.

🟡 *Nâng cao.* **Network troubleshooting.** `ss -tulpn` xem port nào đang mở/process nào giữ port đó. `dig`/`nslookup` tra DNS (tên miền → IP).

**Docker multi-stage build.** Dùng 1 stage để build (đầy đủ compiler, dependency build) rồi chỉ copy **kết quả cuối cùng** sang stage runtime tối giản — giảm size image cuối cùng đáng kể.

```dockerfile
# Stage 1: build — có đầy đủ compiler, dependency chỉ cần lúc cài đặt
FROM python:3.11 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt   # copy requirements TRƯỚC code -> cache layer, build lại nhanh hơn
COPY . .

# Stage 2: runtime — image gốc tối giản, không mang theo compiler/cache build
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app .
ENV PATH=/root/.local/bin:$PATH
CMD ["gunicorn", "app:app", "--workers", "4"]
```

Dễ sai: copy toàn bộ code **trước** `pip install` khiến Docker cache bị miss liên tục mỗi lần sửa code (dù `requirements.txt` không đổi) — luôn copy `requirements.txt` riêng và cài đặt trước, copy code sau cùng.

**Docker Compose, volume.** Compose định nghĩa nhiều service chạy cùng lúc, tự tạo network nội bộ để chúng gọi nhau qua tên service. Volume là nơi lưu data **ngoài** vòng đời container — container bị xóa/restart thì data trong volume vẫn còn.

🔴 *Chuyên sâu/Thực chiến.* **Layer 4 vs Layer 7.** Load balancer **Layer 4** chỉ nhìn TCP/UDP (IP + port), chuyển tiếp gói tin nhanh, không đọc được nội dung HTTP — dùng khi cần tốc độ tối đa. **Layer 7** đọc được HTTP header/path, route thông minh hơn (VD `/api` vào service A, `/static` vào service B) nhưng chậm hơn 1 chút vì phải "mở gói" ra đọc.

**Đọc chi tiết:** [`10-DevOps-Architect/Docker_Kubernetes_Mastery.md`](../10-DevOps-Architect/Docker_Kubernetes_Mastery.md) (phần Docker). Network troubleshooting: [`10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md`](../10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md) — Học phần 2 (Basic Linux).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `10-DevOps-Architect/Docker_Kubernetes_Mastery.md` (mục 1-2), `10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md` (Học phần 1-2), `interview_prep/05_Docker_DevOps.md` (mục 1-4).

#### Image vs Container vs Volume vs Network
```bash
docker images; docker pull python:3.11-slim; docker build -t myapp:v1.0 .
docker run -d -p 8080:5000 myapp:v1.0; docker ps; docker exec -it container_id bash
docker volume create mydata; docker run -v mydata:/app/data myapp
docker network create mynet
```

#### Dockerfile Best Practices
```dockerfile
FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN adduser --disabled-password --gecos '' appuser
USER appuser
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://localhost:5000/health || exit 1
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:create_app()"]
```
**Layer caching rules:** layer chỉ invalidate khi nó hoặc layer trước thay đổi; instruction ít đổi nhất đặt TRÊN; `COPY source code` luôn đặt SAU `pip install`.

#### Docker Compose đầy đủ cho Flask app
```yaml
services:
  app:
    build: { context: ., target: production }
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      db: { condition: service_healthy }
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
  db:
    image: postgres:15-alpine
    environment: { POSTGRES_PASSWORD: ${DB_PASSWORD} }
    volumes: ["postgres_data:/var/lib/postgresql/data"]
  redis:
    image: redis:7-alpine
    command: redis-server --requirepass ${REDIS_PASSWORD}
  celery_worker:
    command: celery -A app.celery worker --loglevel=info --concurrency=4
  nginx:
    image: nginx:alpine
    ports: ["80:80", "443:443"]
volumes: { postgres_data: {}, redis_data: {} }
```
```bash
docker-compose up -d --build
docker-compose logs -f app
docker-compose up -d --scale celery_worker=3
docker-compose run --rm app flask db upgrade
docker-compose down -v   # kèm xóa volumes — NGUY HIỂM ở prod!
```

#### Linux commands cho phỏng vấn
```bash
find /app -name "*.py" -mtime -7
grep -rn "TODO" ./app
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10   # top 10 IP
ps aux | grep python; kill -9 <pid>; lsof -i :5000
systemctl status myapp; journalctl -u myapp -f
```

#### Nginx reverse proxy config
```nginx
server {
    listen 443 ssl http2;
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    location /api {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    location /static {
        alias /app/static;
        expires 30d;
    }
}
```

#### Virtualization vs Containerization, OSI, 12-Factor App (Học phần 1)
Kiến trúc client-server, mô hình OSI 7 tầng (tối thiểu tầng 3-Network, 4-Transport, 7-Application), khái niệm IP/Port/DNS/HTTP-HTTPS. Mô hình **12-Factor App** (config tách biệt code, stateless process, log as stream) — nền tảng thiết kế app "cloud-native". Tư duy **Infrastructure as Cattle, not Pet** — server hỏng thì thay chứ không "chữa bệnh" thủ công.

**Sự cố thường gặp (Học phần 1-2):**
- Nhầm "DevOps là công cụ" với "DevOps là văn hóa" — mua đủ tool nhưng Dev/Ops vẫn đổ lỗi nhau khi sập hệ thống.
- **Disk full** — log không rotate, Docker image/container rác (`docker system prune`).
- **Port đã bị chiếm** — `lsof -i :PORT` hoặc `ss -tulpn | grep PORT`.
- **Zombie/Defunct process** — quy trình cha không "reap" con đúng cách, cần hiểu init process (PID 1) trong container.
- **"Permission denied" khi chạy script** — quên `chmod +x`, hoặc chạy sai user (dùng `sudo` cho lệnh cần quyền root).
- **Cron job không chạy** — PATH trong cron khác với shell tương tác, hoặc quên `2>&1` để redirect log lỗi ra file mà debug.

#### Shell scripting, cron, systemd, SSH (Học phần 2 — Nâng cao)
```bash
# Bash script tự động backup /var/www thành .tar.gz gắn timestamp, đẩy lên S3, chạy cron 2h sáng
#!/bin/bash
TS=$(date +%Y%m%d_%H%M%S)
tar -czf /backup/www_$TS.tar.gz /var/www
aws s3 cp /backup/www_$TS.tar.gz s3://my-backup-bucket/
# crontab -e:
0 2 * * * /opt/scripts/backup_www.sh >> /var/log/backup.log 2>&1
```
```ini
# Unit file systemd để chạy app như 1 service
# /etc/systemd/system/myapp.service
[Unit]
Description=My Flask App
After=network.target

[Service]
User=appuser
WorkingDirectory=/app
ExecStart=/usr/bin/gunicorn app:app --bind 0.0.0.0:5000
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
```bash
systemctl enable myapp && systemctl start myapp
# SSH key-based auth (không cần mật khẩu)
ssh-keygen -t ed25519 -C "deploy@myapp"
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server   # hoặc append thủ công vào ~/.ssh/authorized_keys trên server
```
**Lab:** service Node.js bị "Out of Memory" và bị kill — debug bằng `dmesg | grep -i kill`, `journalctl -u <service>`.

</details>
**Bài tập:** FL-04, DO-01, DO-02 trong [`03-DevOps-Exercises/Checklist_Bai_Tap.md`](03-DevOps-Exercises/Checklist_Bai_Tap.md).

---

<a id="chuong-15"></a>
## Chương 15 — CI/CD với GitHub Actions & GitLab CI

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Pipeline là gì: trigger (push/PR) → test → build → deploy.
- So sánh nhanh **GitHub Actions** (`.github/workflows`, tích hợp sẵn với GitHub) vs **GitLab CI** (`.gitlab-ci.yml`, mạnh về self-hosted runner) — khác nền tảng nhưng cùng tư duy Pipeline → Job → Step.

🟡 **Nâng cao (trọng tâm Middle):**
- Viết `.github/workflows/*.yml`: job, step, matrix build.
- Cache dependency để pipeline chạy nhanh hơn.
- Viết tương đương bằng `.gitlab-ci.yml` (`stages`, `script`) — nắm được cú pháp khác nhưng ý tưởng y hệt giúp không bị phụ thuộc vào 1 nền tảng duy nhất.

🔴 **Chuyên sâu / Thực chiến:**
- Secret trong CI/CD (GitHub Secrets) — không bao giờ hardcode; thiết kế pipeline nhiều stage (test → staging → production) an toàn.
- **Security Scan (SAST)** — quét lỗ hổng bảo mật ngay trong code trước khi merge, là 1 bước chuẩn trong multi-stage pipeline chuyên nghiệp.
- **Self-hosted Runner** — khi cần build trong mạng nội bộ (không public ra internet) hoặc cần tài nguyên đặc thù (GPU, RAM lớn) mà runner mặc định của GitHub không đáp ứng.

**Giải thích chi tiết:**

🟢 *Cơ bản.* Pipeline là chuỗi bước tự động chạy khi có sự kiện (push/PR): test → build Docker image → deploy.

**GitHub Actions vs GitLab CI.** Cả 2 đều theo đúng mô hình Pipeline → Job (GitLab gọi là `stage`) → Step (GitLab gọi là `script`), chỉ khác cú pháp YAML và nơi chạy. GitHub Actions tiện nhất khi code đã nằm sẵn trên GitHub (không cần cấu hình thêm). GitLab CI mạnh hơn ở khả năng tự host runner trong hạ tầng riêng (phù hợp công ty cần build trong mạng nội bộ, không muốn code rời khỏi VPC) và có `.gitlab-ci.yml` khai báo gọn hơn cho pipeline nhiều stage phức tạp. Về bản chất tư duy, học vững 1 nền tảng là chuyển sang nền tảng còn lại (hay cả Azure DevOps/CircleCI) chỉ mất vài giờ làm quen cú pháp.

🟡 *Nâng cao.* Mỗi **job** chạy trên 1 máy ảo riêng (song song được nếu không phụ thuộc nhau), mỗi job gồm nhiều **step** tuần tự. **Matrix build** chạy cùng 1 job với nhiều tổ hợp biến (VD test trên Python 3.10 và 3.11 cùng lúc). Cache dependency giúp pipeline không phải tải lại toàn bộ package mỗi lần — tiết kiệm vài phút mỗi lần chạy, cộng dồn rất đáng kể.

```yaml
# .github/workflows/ci.yml
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11"]   # matrix build: chạy song song cả 2 version
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: "pip"                      # cache dependency theo hash của requirements.txt
      - run: pip install -r requirements.txt
      - run: pytest
      - run: docker build -t myapp:${{ github.sha }} .
```

🔴 *Chuyên sâu/Thực chiến.* Secret (GitHub Secrets) được inject vào lúc chạy, không bao giờ nằm trong code — tránh lộ khi push nhầm lên public repo; thiết kế pipeline nhiều stage (test → staging → production) để không deploy thẳng code chưa qua kiểm tra lên production. Pipeline chuyên nghiệp đầy đủ thường có thứ tự: Build → Test (unit + integration) → **Security Scan** → Deploy Staging → Manual Approval → Deploy Production — gồm 2 loại quét khác nhau, hay bị nhầm là 1: **SAST** (Static Application Security Testing) quét chính code bạn viết để tìm pattern nguy hiểm (SQL Injection do nối chuỗi tay, secret bị hardcode); **SCA** (Software Composition Analysis — `safety`/`pip-audit`/Dependabot đã học ở Chương 12) quét các package bên thứ 3 đang phụ thuộc để tìm CVE đã công bố. Self-hosted Runner là máy do chính bạn (hoặc công ty) tự quản lý để chạy job CI/CD thay vì dùng máy ảo mặc định của GitHub — cần khi job phải truy cập tài nguyên nội bộ (VD database chỉ mở trong VPC riêng) mà runner public không với tới được.

**Đọc chi tiết:** tài liệu CI/CD trong [`10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md`](../10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md) — Học phần 6 (có cả phần so sánh GitHub Actions/GitLab CI/Azure DevOps/CircleCI), thực hành thêm ở [`Mastery/Cloud-DevOps-Mastery/04-CICD-Deployment-Strategies`](../Mastery/Cloud-DevOps-Mastery/04-CICD-Deployment-Strategies).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md` (Học phần 6), `interview_prep/05_Docker_DevOps.md` (mục 6), `Mastery/Cloud-DevOps-Mastery/04-CICD-Deployment-Strategies/README.md`.

#### Pipeline đầy đủ — GitHub Actions
```yaml
name: Deploy to Production
on: { push: { branches: [main] } }
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        options: >-
          --health-cmd pg_isready --health-interval 10s
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with: { python-version: '3.11' }
      - run: pip install -r requirements.txt
      - run: pytest --cov=app tests/
  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_HOST }}
          script: |
            cd /app && git pull origin main
            docker-compose up -d --build
            docker-compose exec app flask db upgrade
```

#### Pipeline tương đương — GitLab CI (`.gitlab-ci.yml`)
```yaml
stages: [test, build, deploy]

test:
  stage: test
  image: python:3.11
  services: [postgres:15]
  variables:
    POSTGRES_DB: test_db
    DATABASE_URL: postgresql://postgres:postgres@postgres/test_db
  script:
    - pip install -r requirements.txt
    - pytest --cov=app tests/

build:
  stage: build
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

deploy_production:
  stage: deploy
  only: [main]
  when: manual        # Manual Approval tương đương GitHub Environments
  script:
    - ssh $SERVER_USER@$SERVER_HOST "cd /app && docker-compose pull && docker-compose up -d"
```
Khác biệt chính với GitHub Actions: GitLab CI dùng `stages`/`only`/`when: manual` thay vì `needs`/`if`/environment protection rule; cơ chế cache khai báo qua khối `cache:` cấp pipeline thay vì action `actions/cache`.

#### 4 nền tảng CI/CD phổ biến
- **GitHub Actions** — tích hợp sẵn GitHub, YAML trong `.github/workflows`.
- **GitLab CI** — `.gitlab-ci.yml`, mạnh self-hosted runner.
- **Azure DevOps** — Pipeline YAML hoặc Classic UI, mạnh hệ sinh thái Microsoft/Enterprise.
- **CircleCI** — SaaS, orb (package tái sử dụng step), build nhanh nhờ caching thông minh.

#### Feature Flag — tách "deploy code" khỏi "bật tính năng"
```python
if feature_flags.is_enabled("new_checkout_flow", user_id=current_user.id):
    return new_checkout_flow()
return legacy_checkout_flow()
```
Code mới nằm im trên production hàng ngày/tuần trước khi bật thật — tách rủi ro deploy khỏi rủi ro tính năng. Tắt flag tức thì khi có vấn đề, nhanh hơn rollback truyền thống rất nhiều.

#### Database Migration trong CI/CD — Expand-Contract pattern
```
Bước 1: Thêm cột mới (KHÔNG xóa cột cũ) — deploy, code cũ vẫn chạy bình thường
Bước 2: Deploy code MỚI, ghi vào CẢ 2 cột, đọc từ cột mới
Bước 3: Backfill dữ liệu cũ sang cột mới
Bước 4: Deploy code, ngừng ghi vào cột cũ
Bước 5: Migration riêng xóa cột cũ (sau khi chắc chắn ổn định)
```
**Sai lầm kinh điển:** migration đổi schema chạy đồng thời với deploy code mới — nếu rollback code do bug, code CŨ chạy với schema MỚI → crash toàn bộ.

#### Pipeline gates — không phải mọi merge nên tự động deploy production
```
Build → Unit Test → Integration Test → Security Scan (SAST/dependency check)
  → Deploy Staging → Smoke Test → [Manual Approval] → Deploy Production (Canary)
  → Theo dõi metric tự động → Auto rollback nếu error rate tăng bất thường
```

#### Sự cố thường gặp (Học phần 6)
- **Pipeline pass local, fail CI** — khác biệt version/biến môi trường/timezone.
- **Build chậm dần** — cache key thay đổi liên tục (VD hash `package-lock.json`).
- **Secret lộ trong log** — `echo $SECRET` để debug rồi quên xóa; luôn dùng cơ chế `mask`.
- **Race condition giữa nhiều pipeline song song** — cần concurrency group lock deployment.
- **`docker push` denied** — thiếu login registry hoặc sai quyền IAM/Role của CI runner.

</details>
**Bài tập:** DO-03, DO-04. Nâng cao: chuyển pipeline GitHub Actions đã viết sang `.gitlab-ci.yml` để tự so sánh cú pháp và cơ chế cache giữa 2 nền tảng.

---

<a id="chuong-16"></a>
## Chương 16 — Cloud: AWS cơ bản & So sánh nhanh GCP

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- EC2 (máy chủ ảo), S3 (lưu file), VPC (mạng riêng ảo) — 3 dịch vụ nền tảng nhất.
- Thực hành an toàn không mất tiền: dùng `localstack/` trước khi đụng tài khoản AWS thật.
- **Ánh xạ dịch vụ AWS ↔ GCP** — học sâu 1 cloud (AWS) là đủ, chỉ cần biết "tên gọi tương đương" bên GCP để không bỡ ngỡ khi công ty dùng nền tảng khác.

🟡 **Nâng cao (trọng tâm Middle):**
- Security Group (firewall của EC2) — lỗi cấu hình sai rất phổ biến khi mới học.
- RDS (Database as a Service) — khác gì so với tự cài DB trên EC2.
- **Load Balancer (ALB/NLB) + Auto Scaling Group** — scale instance theo tải thực tế, health check.
- **Route 53** — DNS management, routing policy (Weighted, Failover, Latency-based).
- **CloudWatch** — Metrics/Alarms/Logs, nền tảng để nối sang Chương 13 (Observability) khi chạy trên AWS thật.

🔴 **Chuyên sâu / Thực chiến:**
- IAM (quản lý quyền truy cập) — nguyên tắc least privilege; đây là kỹ năng hay bị đánh giá thấp nhưng gây hậu quả nặng nhất nếu làm sai.
- **ECR/ECS/EKS** — container registry + service chạy container trên AWS; EKS là bước đệm trực tiếp sang Chương 17 (K8s chạy trên cloud thật thay vì Minikube).
- **API Gateway** — cổng vào duy nhất cho API (quản lý route, auth, rate limit, Lambda integration) thay vì expose trực tiếp từng service; có **giới hạn timeout cứng 29 giây** — lỗi `504 Gateway Timeout` kinh điển khi backend xử lý lâu hơn.
- **Cost optimization**: Reserved Instance, Spot Instance, Savings Plan — kỹ năng hay bị bỏ qua lúc học nhưng ảnh hưởng trực tiếp tới đánh giá "tư duy vận hành" ở phỏng vấn Middle/Senior.
- **Security nâng cao**: KMS (mã hóa), Secrets Manager, WAF, VPC Peering.

**Giải thích chi tiết:**

🟢 *Cơ bản.* **EC2, S3, VPC.** EC2 là máy chủ ảo, bạn kiểm soát toàn bộ OS bên trong. S3 lưu file dạng object (ảnh, video, backup) — không phải ổ cứng gắn vào máy, mà là dịch vụ lưu trữ độc lập gọi qua API. VPC là mạng riêng ảo — ranh giới cô lập hạ tầng của bạn với phần còn lại của AWS.

**AWS ↔ GCP — bảng ánh xạ nhanh.** EC2 ↔ **Compute Engine**; S3 ↔ **Cloud Storage**; VPC ↔ **VPC** (tên giống nhau); RDS ↔ **Cloud SQL**; EKS ↔ **GKE** (Google Kubernetes Engine — thường được đánh giá là bản K8s managed mượt nhất thị trường vì Google là nơi khai sinh ra Kubernetes); Lambda ↔ **Cloud Functions**; IAM ↔ **IAM** (tên giống nhau, cơ chế tương tự); CloudWatch ↔ **Cloud Monitoring/Cloud Logging**; Route 53 ↔ **Cloud DNS**. Khác biệt lớn nhất về tư duy: GCP mạng mặc định là **global VPC** (1 VPC trải across mọi region), trong khi AWS VPC luôn gắn với 1 region cụ thể — ảnh hưởng tới cách thiết kế kiến trúc multi-region.

🟡 *Nâng cao.* **Security Group, RDS.** Security Group là firewall gắn vào từng EC2 — lỗi mở Security Group quá rộng (`0.0.0.0/0` cho port DB) là lỗi bảo mật phổ biến nhất của người mới. RDS là Database as a Service — AWS tự lo backup, patch, failover, đổi lại bạn không có quyền root vào máy DB.

**Load Balancer + Auto Scaling Group, Route 53, CloudWatch.** ALB (Layer 7) route theo path/domain, NLB (Layer 4) nhanh hơn nhưng không đọc được HTTP — liên hệ trực tiếp khái niệm L4/L7 đã học ở Chương 14. Auto Scaling Group tự thêm/bớt EC2 theo tải, luôn đi kèm Load Balancer để phân phối traffic tới các instance mới. Route 53 là DNS Service của AWS, hỗ trợ routing policy thông minh (VD Failover — tự chuyển traffic sang region dự phòng khi region chính chết). CloudWatch thu thập Metrics/Logs/Alarms của mọi service AWS — tương đương vai trò Prometheus+Grafana nhưng là bản managed của AWS.

🔴 *Chuyên sâu/Thực chiến.* **IAM.** Quản lý "ai được làm gì" — nguyên tắc least privilege: chỉ cấp đúng quyền cần thiết, không cấp `AdministratorAccess` cho mọi thứ vì tiện.

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject", "s3:PutObject"],
    "Resource": "arn:aws:s3:::my-app-uploads/*"
  }]
}
```

IAM Policy trên chỉ cho phép đọc/ghi đúng 1 bucket cụ thể — thay vì gắn `AmazonS3FullAccess` (truy cập được mọi bucket trong account) chỉ vì "cho tiện lúc setup", đúng tinh thần least privilege.

**ECR/ECS/EKS.** ECR là registry lưu Docker image (giống Docker Hub nhưng riêng tư, gắn với IAM). ECS là dịch vụ chạy container theo cách AWS tự quản lý (đơn giản hơn K8s nhưng chỉ chạy được trên AWS). EKS là Kubernetes managed của AWS — Control Plane do AWS vận hành, bạn chỉ quản lý Worker Node — đây chính là nơi áp dụng toàn bộ kiến thức K8s ở Chương 17 vào môi trường cloud thật.

**API Gateway.** Thay vì để client gọi thẳng vào từng service/Lambda, API Gateway đứng làm 1 cổng vào duy nhất — xử lý chung routing, authentication, rate limiting (liên hệ Token Bucket ở Chương 11), rồi mới chuyển tiếp vào backend thật. Sự cố thực tế hay gặp nhất: API Gateway có **timeout cố định 29 giây** — nếu backend (VD Lambda xử lý export báo cáo, gửi email hàng loạt) chạy lâu hơn, client nhận `504 Gateway Timeout` dù backend vẫn đang chạy bình thường phía sau. Cách xử lý đúng: không xử lý tác vụ nặng đồng bộ qua API Gateway — chuyển sang mô hình bất đồng bộ (liên hệ Background task ở Chương 10): API Gateway nhận request → đẩy vào queue (SQS/EventBridge) → trả về ngay `202 Accepted` cho client → worker xử lý ngầm phía sau, client poll hoặc nhận callback khi xong.

**Cost optimization.** Reserved Instance (cam kết dùng dài hạn để được giá rẻ hơn On-Demand), Spot Instance (dùng tài nguyên dư thừa của AWS, rẻ nhưng có thể bị thu hồi bất kỳ lúc nào — chỉ hợp với tải chịu được gián đoạn), Savings Plan (linh hoạt hơn Reserved Instance). Quên tắt EC2/NAT Gateway sau khi test là nguyên nhân phổ biến nhất khiến bill AWS tăng bất thường.

**Security nâng cao.** KMS quản lý khóa mã hóa tập trung cho các service khác dùng chung. Secrets Manager lưu secret có xoay vòng tự động (khác `.env` tĩnh ở Chương 12). WAF lọc request độc hại (SQL Injection, XSS, rate-based) ngay trước khi tới ALB/CloudFront. VPC Peering kết nối riêng tư giữa 2 VPC khác nhau mà không đi qua internet công cộng.

**Đọc chi tiết:** [`07-AWS-Mastery/AWS_90Days_Mastery_Plan.md`](../07-AWS-Mastery/AWS_90Days_Mastery_Plan.md) (chỉ cần phần nền tảng, không cần học hết 90 ngày). GCP hiện chưa có tài liệu chi tiết riêng trong repo — bảng ánh xạ trên là điểm khởi đầu, nên tra thêm docs chính thức của Google Cloud khi công ty mục tiêu thực sự dùng GCP.

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `07-AWS-Mastery/AWS_90Days_Mastery_Plan.md`, `10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md` (Học phần 3), `Mastery/Cloud-DevOps-Mastery/01-Cloud-Foundations-Real-Decisions/README.md`.

#### Kế hoạch 90 ngày — mốc theo tháng
**Tháng 1 — Building Blocks:** Tuần 1 IAM (Users/Groups/Roles/Policies/MFA); Tuần 2 EC2 + ALB (deploy Vue app lên Nginx trong EC2); Tuần 3 Auto Scaling + EBS Snapshot; Tuần 4 VPC (Public/Private subnet, NAT Gateway).
**Tháng 2 — Storage, Data, Monitoring:** Tuần 5 S3 + CloudFront; Tuần 6 RDS (Multi-AZ) + ElastiCache; Tuần 7 DynamoDB (`boto3` CRUD); Tuần 8 CloudWatch + CloudTrail.
**Tháng 3 — Serverless & DevOps:** Tuần 9 Lambda + API Gateway; Tuần 10 SQS + SNS (decoupling, pub/sub); Tuần 11 AWS CDK/Terraform (IaC); Tuần 12 Review + thi thử.

#### IAM & Least Privilege — thực hành đúng
1. Bắt đầu với AWS Managed Policy gần nhất (VD `AmazonS3ReadOnlyAccess`).
2. Bật **CloudTrail**, theo dõi thực tế service/user gọi API nào trong 2-4 tuần.
3. Dùng **IAM Access Analyzer** tự động sinh policy chỉ chứa quyền đã thực sự dùng.
4. Thay Managed Policy bằng Custom Policy hẹp dựa trên dữ liệu thật đó.

**Sự cố thật:** gán `AdministratorAccess` cho access key của script tự động "cho tiện, sửa sau" — key rò rỉ (commit nhầm GitHub public) = toàn bộ tài khoản AWS bị chiếm quyền. Luôn dùng **IAM Role** (credential tạm thời tự xoay vòng) thay vì Access Key tĩnh.

#### Chi phí (Cost) — sai lầm thường gặp

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Quên tắt NAT Gateway | Phí theo giờ + data transfer dù không traffic | Review định kỳ bằng Cost Explorer |
| Data transfer giữa AZ | Tính phí dù cùng 1 VPC | Đặt service hay giao tiếp nhau cùng AZ |
| Snapshot EBS/RDS tích lũy | Phí lưu trữ tăng âm thầm | Lifecycle policy tự xóa snapshot cũ |
| Over-provisioned EC2 | Trả tiền tài nguyên không dùng | Auto Scaling + benchmark tải thật |

#### Sự cố thường gặp (Học phần 3 AWS Basic)
- **EC2 không SSH được** — Security Group chưa mở port 22, `.pem` sai quyền (`chmod 400`), hoặc ở subnet private thiếu Internet Gateway.
- **App không truy cập được từ browser** — quên mở port ứng dụng trong Security Group, hoặc app chỉ bind `127.0.0.1` thay vì `0.0.0.0`.
- **RDS connection timeout** — Security Group RDS chưa cho phép inbound từ SG của EC2 (nên trỏ SG-to-SG thay vì IP cứng).
- **IAM Access Denied** — dùng **IAM Policy Simulator** để debug.

#### VPC Design — "defense in depth", không phải tạo cho có
```
Internet
   │
   ▼
Public Subnet (ALB/NAT Gateway)         ← chỉ đặt thứ BẮT BUỘC phải public
   │
   ▼
Private Subnet — App tier (EC2/ECS)     ← không có IP public, ra internet qua NAT
   │
   ▼
Private Subnet — Data tier (RDS)        ← chỉ App tier được phép kết nối vào, SG hẹp nhất
```
**Sự cố thật kinh điển:** đặt RDS ở **public subnet** để "dễ debug từ máy cá nhân" rồi quên đổi lại — nguyên nhân của rất nhiều vụ rò rỉ dữ liệu thật (DB bị bot quét tự động, brute-force password). Nguyên tắc bất di bất dịch: **data tier không bao giờ có route trực tiếp ra internet**, muốn truy cập từ xa phải qua Bastion Host/VPN/Session Manager.

**Câu hỏi senior hay hỏi khi review kiến trúc:** "Database của bạn có route trực tiếp ra internet không? Ai có thể SSH/kết nối trực tiếp vào nó?" / "IAM Role này có quyền gì — dựa vào managed policy mặc định hay đã audit theo usage thật?" / "Kiến trúc này chi phí bao nhiêu/tháng ở quy mô hiện tại, và ở quy mô gấp 10 lần?"

</details>
**Bài tập:** DO-04 (deploy qua pipeline lên localstack/EC2).

---

<a id="chuong-17"></a>
## Chương 17 — Container Orchestration: Kubernetes cơ bản

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Vì sao cần K8s khi đã có Docker Compose.
- **Kiến trúc K8s**: Control Plane (API Server, Scheduler, Controller Manager, etcd) vs Worker Node (Kubelet, Kube-proxy, Container Runtime) — biết rõ "ai làm gì" trước khi học object.
- Pod, Deployment, Service, **Namespace** (cô lập resource trong cùng 1 cluster, VD tách môi trường dev/staging trong cùng cluster) — nhóm khái niệm nền tảng nhất.
- Thực hành trên Minikube trước khi đụng cluster thật.

🟡 **Nâng cao (trọng tâm Middle):**
- **ConfigMap** vs **Secret** — inject cấu hình đúng chuẩn.
- `kubectl` cơ bản: apply, get, describe, logs, port-forward.
- Liveness/Readiness Probe — health check tự động.
- **Volume & PersistentVolumeClaim (PVC)** — lưu trữ dữ liệu bền vững, sống lâu hơn vòng đời Pod.
- **Helm** — package manager cho K8s, viết Helm Chart để tái sử dụng cấu hình thay vì copy YAML tay giữa các môi trường.
- **RBAC** — phân quyền truy cập cluster theo nguyên tắc least privilege (liên hệ IAM ở Chương 16).

🔴 **Chuyên sâu / Thực chiến:**
- **Ingress** — định tuyến HTTP từ bên ngoài vào đúng Service.
- **HPA (Horizontal Pod Autoscaler)** — tự động scale theo tải thực tế.
- **Service Mesh (Istio/Linkerd)** — lớp hạ tầng riêng xử lý giao tiếp giữa các service (mTLS tự động, retry, traffic shifting) mà không cần sửa code app — chỉ nên học khi đã vững Ingress/HPA, vì đây là tầng phức tạp thêm vào trên K8s, không phải thay thế.

**Giải thích chi tiết:**

🟢 *Cơ bản.* **Kiến trúc K8s.** Control Plane là "bộ não" của cluster: API Server nhận mọi lệnh (kể cả từ `kubectl`), Scheduler quyết định Pod mới chạy ở Node nào, Controller Manager đảm bảo trạng thái thực tế khớp trạng thái mong muốn (VD tự tạo lại Pod chết), etcd là nơi lưu toàn bộ state của cluster (mất etcd = mất cluster). Worker Node là nơi Pod thực sự chạy: Kubelet nhận lệnh từ Control Plane và điều khiển container runtime, Kube-proxy xử lý network rule để traffic tới đúng Pod.

**Vì sao cần K8s.** Compose chạy tốt trên **1 máy**. Khi cần chạy trên **nhiều máy** (cluster) và tự động hồi phục khi 1 container/máy chết, cần 1 "bộ não" điều phối — đó là K8s.

**Pod, Deployment, Service, Namespace.** Pod là đơn vị nhỏ nhất K8s triển khai, chứa 1+ container luôn chạy cùng nhau. Deployment khai báo "tôi muốn luôn có N Pod chạy phiên bản X" — K8s tự tạo/xóa Pod để giữ đúng trạng thái đó. Service là địa chỉ mạng **ổn định** trỏ tới nhóm Pod (Pod có thể chết/tái tạo liên tục với IP mới, Service che giấu sự thay đổi đó). Namespace chia 1 cluster vật lý thành nhiều "cluster ảo" logic — tiện cho việc tách quyền truy cập và resource quota giữa các team/môi trường mà không cần dựng nhiều cluster thật.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-api
spec:
  replicas: 3                        # luôn giữ đúng 3 Pod chạy
  selector:
    matchLabels: { app: backend-api } # phải khớp labels bên dưới — lỗi kinh điển khi không khớp
  template:
    metadata:
      labels: { app: backend-api }
    spec:
      containers:
        - name: api
          image: myapp:v1.2
          ports: [{ containerPort: 8000 }]
---
apiVersion: v1
kind: Service
metadata:
  name: backend-api-svc
spec:
  selector: { app: backend-api }      # Service tìm Pod qua labels này, không qua IP
  ports: [{ port: 80, targetPort: 8000 }]
```

Lỗi kinh điển nhất của người mới học K8s: `labels` trong Deployment và `selector` trong Service không khớp nhau — Service tồn tại nhưng không route được traffic tới Pod nào cả.

🟡 *Nâng cao.* **ConfigMap/Secret.** Inject cấu hình vào Pod mà không hardcode trong image — đổi cấu hình không cần build lại image.

**Liveness/Readiness Probe.** Liveness Probe trả lời "container này còn sống không" — fail thì K8s tự kill và tạo Pod mới. Readiness Probe trả lời "Pod đã sẵn sàng nhận traffic chưa" — fail thì Service tạm ngưng gửi request tới Pod đó (không kill).

**Volume & PVC.** Mặc định, dữ liệu ghi trong container mất khi Pod bị xóa/tái tạo (giống container Docker thường). PersistentVolumeClaim là "đơn xin cấp" 1 vùng lưu trữ bền vững (PersistentVolume) tồn tại độc lập với vòng đời Pod — cần cho mọi dữ liệu không được phép mất (DB chạy trong K8s, file upload).

**Helm.** Helm Chart đóng gói toàn bộ YAML (Deployment, Service, ConfigMap...) của 1 app thành 1 package có tham số hóa — deploy 1 app phức tạp chỉ bằng `helm install`, và dùng chung 1 chart cho dev/staging/prod chỉ bằng cách đổi file giá trị (`values.yaml`) thay vì copy-paste YAML.

**RBAC.** Role-Based Access Control quyết định ai (user/service account) được làm gì (verb: get/list/create/delete) trên resource nào (Pod/Secret/...) trong Namespace nào — áp dụng đúng nguyên tắc least privilege đã học ở Chương 16 nhưng ở cấp độ cluster thay vì cấp độ AWS account.

🔴 *Chuyên sâu/Thực chiến.* **Ingress, HPA.** Ingress đóng vai trò 1 Layer-7 load balancer ngay trong cluster, route theo domain/path vào đúng Service. HPA tự tăng/giảm số Pod theo CPU/Memory — bản chất giống Auto Scaling Group ở EC2 nhưng ở cấp độ Pod.

**Service Mesh.** Khi số lượng service tăng lên (kiến trúc microservice thật), mỗi service tự implement retry/timeout/mTLS/circuit breaker riêng sẽ trùng lặp và dễ sai. Service Mesh (Istio, Linkerd) gắn 1 "sidecar proxy" (thường là Envoy) vào mỗi Pod để xử lý toàn bộ phần giao tiếp mạng đó **bên ngoài** code app — app chỉ cần gọi service khác như bình thường, mesh tự lo retry/mã hóa/đo lường traffic. Đánh đổi: thêm 1 tầng hạ tầng phức tạp, chỉ nên áp dụng khi số lượng microservice đủ lớn để lợi ích vượt chi phí vận hành thêm.

**Đọc chi tiết:** [`10-DevOps-Architect/Docker_Kubernetes_Mastery.md`](../10-DevOps-Architect/Docker_Kubernetes_Mastery.md) (phần K8s), [`Mastery/Cloud-DevOps-Mastery/03-Container-Orchestration-In-Practice`](../Mastery/Cloud-DevOps-Mastery/03-Container-Orchestration-In-Practice).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md` (Học phần 4), `Mastery/Cloud-DevOps-Mastery/03-Container-Orchestration-In-Practice/README.md`.

#### Image nhẹ, chạy non-root — bề mặt tấn công nhỏ hơn
```dockerfile
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
RUN useradd -m appuser && chown -R appuser /app
USER appuser                                    # KHÔNG chạy container bằng root
CMD ["python", "app.py"]
```
Image nặng (chứa compiler/dev tool) mở rộng bề mặt tấn công (nhiều CVE tiềm ẩn) và tốn băng thông mỗi lần scale. Chạy container bằng root: nếu attacker khai thác lỗ hổng app, họ có ngay quyền root bên trong container.

#### Resource Requests & Limits
```yaml
resources:
  requests: { memory: "256Mi", cpu: "250m" }   # Scheduler dùng để đặt pod vào node nào
  limits: { memory: "512Mi", cpu: "500m" }     # vượt quá bị OOMKilled hoặc throttle CPU
```
Thiếu resources → 1 pod bug (memory leak) ăn hết RAM cả node, crash luôn pod KHÁC không liên quan ("noisy neighbor"). `limits` quá thấp → OOMKilled liên tục dù logic không bug, chỉ vì traffic tăng nhẹ.

#### Liveness vs Readiness Probe — nhầm lẫn gây outage dây chuyền

| Probe | Trả lời câu hỏi | Nếu fail |
|---|---|---|
| Liveness | "Process có bị deadlock/treo không?" | K8s **restart pod** |
| Readiness | "Pod đã sẵn sàng nhận traffic chưa?" | K8s **rút pod khỏi traffic** (không restart) |

**Sự cố kinh điển:** dùng chung 1 endpoint `/health` cho cả 2, endpoint đó kiểm tra luôn kết nối DB. DB chậm tạm thời → readiness fail đúng, nhưng nếu liveness dùng chung → K8s **restart toàn bộ pod** dù app không treo → vòng lặp restart liên tục (outage tự gây ra bởi chính cơ chế tự phục hồi). **Nguyên tắc:** Liveness chỉ kiểm tra process, không phụ thuộc dependency ngoài; Readiness mới kiểm tra DB/cache/service khác.

#### Rolling Update — vì sao vẫn thấy 502 thoáng qua
`preStop` hook + `terminationGracePeriodSeconds`: cho pod cũ thời gian hoàn thành request đang xử lý và tự rút khỏi LB trước khi bị kill hẳn. `maxUnavailable`/`maxSurge` hợp lý — không hạ hết pod cũ trước khi pod mới sẵn sàng.

#### Deploy app 3-tier lên Minikube (Lab)
Deploy Frontend + Backend API + Database lên Minikube/Kind, dùng Service để 3 tầng giao tiếp. Viết Helm Chart parameterize số replicas/image tag. Cấu hình HPA tự scale từ 2→10 khi CPU > 70%, test tải bằng `kubectl run -it load-generator`.

#### Sự cố thường gặp (Học phần 4 K8s)
- **`CrashLoopBackOff`** — app lỗi ngay khi start; debug `kubectl logs <pod> --previous`.
- **`ImagePullBackOff`** — sai tên image/tag, hoặc thiếu `imagePullSecrets` cho private registry.
- **Pod `Pending` mãi** — cluster không đủ tài nguyên, hoặc thiếu `nodeSelector`/taint-toleration.
- **Service không route tới Pod** — `labels` Deployment và `selector` Service không khớp (lỗi kinh điển nhất).
- **Config ConfigMap đổi nhưng Pod không nhận** — ConfigMap mount không tự reload, cần rolling restart Deployment.

**`requests` quá thấp so với nhu cầu thật** → Scheduler nhồi quá nhiều pod vào 1 node → node quá tải thật sự dù theo config "vẫn còn chỗ". Senior luôn xác định requests/limits dựa trên **load test thật** (Locust/k6, Chương 8), không đoán theo cảm tính, rồi tinh chỉnh lại sau khi lên production.

**Câu hỏi senior hay hỏi khi review:** "Container này chạy bằng user nào? Có set resource limits chưa?" / "Liveness và readiness probe có dùng chung endpoint không — nếu DB chậm, pod có bị restart oan không?" / "Khi rolling update, request đang xử lý dở trên pod cũ có bị cắt ngang không?"

</details>
**Bài tập:** DO-06.

---

<a id="chuong-18"></a>
## Chương 18 — Infrastructure as Code: Terraform, Ansible & GitOps

> Mục tiêu: định nghĩa hạ tầng bằng code thay vì click tay trên Console — kỹ năng phân biệt rõ DevOps Middle với người chỉ biết "làm theo hướng dẫn trên web AWS".

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Khái niệm IaC, **Terraform**: HCL syntax, Provider, Resource, quy trình `plan` → `apply` → `destroy`.
- **Ansible**: Playbook, Inventory, Module cơ bản.

🟡 **Nâng cao (trọng tâm Middle):**
- So sánh Terraform (provisioning) vs Ansible (cấu hình bên trong máy) — khi nào phối hợp cả hai.
- **Ansible Role** — tổ chức playbook lớn; nguyên tắc **idempotent**.

🔴 **Chuyên sâu / Thực chiến:**
- **State file** — nơi Terraform lưu trạng thái hạ tầng thực tế; **Remote State + State Locking** (S3 + DynamoDB) — bắt buộc khi làm việc nhóm.
- **Terraform Module** và **Workspace**.
- Sự cố thường gặp: state conflict khi 2 người `apply` cùng lúc, `apply` xóa nhầm resource do đổi tên code, drift hạ tầng khi ai đó sửa tay trên Console.
- **GitOps (ArgoCD/Flux)** — Git repo là **nguồn chân lý duy nhất** (single source of truth) cho trạng thái mong muốn của cluster K8s; 1 agent chạy trong cluster tự động đồng bộ theo repo thay vì CI "push" trực tiếp vào cluster — khác biệt tư duy quan trọng nhất so với CI/CD truyền thống ở Chương 15.

**Giải thích chi tiết:**

🟢 *Cơ bản.* **Vì sao cần IaC.** Tạo hạ tầng bằng tay trên Console AWS thì **không lặp lại được chính xác** và không có lịch sử thay đổi. Viết bằng code: review được qua PR như code thường, tạo lại y hệt ở môi trường khác chỉ bằng 1 lệnh.

**Terraform: HCL, Provider, Resource, plan/apply/destroy.** Bạn khai báo **kết quả mong muốn** bằng HCL — không khai báo từng bước thực hiện.

```hcl
provider "aws" {
  region = "ap-southeast-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "backend-api"
  }
}
```

```bash
terraform plan    # xem trước sẽ tạo/sửa/xóa gì — chưa làm gì thật, LUÔN chạy trước apply
terraform apply   # thực thi theo đúng những gì plan đã báo
terraform destroy # xóa toàn bộ resource đã tạo
```

🟡 *Nâng cao.* **Ansible: Playbook, Inventory, Role, idempotent.** Ansible không tạo hạ tầng (việc của Terraform) mà **cấu hình bên trong** máy đã có sẵn — theo mô hình **push-based** (SSH vào máy đích, không cần agent). Playbook phải idempotent: chạy lại N lần vẫn ra cùng 1 trạng thái cuối.

🔴 *Chuyên sâu/Thực chiến.* **State file, Remote State + Locking.** Terraform cần 1 nơi lưu "tôi đã tạo ra những gì". Nếu state nằm trên máy local của 1 người, người thứ 2 chạy `apply` sẽ không biết hạ tầng đã tồn tại, dễ tạo trùng/xóa nhầm. Remote State (S3) + Locking (DynamoDB) giải quyết vấn đề làm việc nhóm.

**Terraform Module, Workspace.** Module là 1 cục hạ tầng đóng gói sẵn, tái sử dụng được. Workspace cho phép dùng chung 1 bộ code Terraform để quản lý nhiều môi trường (dev/staging/prod) mà không copy-paste code 3 lần.

**GitOps.** Với CI/CD truyền thống (Chương 15), pipeline **chủ động push** thay đổi vào server/cluster — nếu pipeline có bug hoặc credential bị lộ, nó có quyền ghi trực tiếp vào production. Với GitOps, 1 agent (ArgoCD/Flux) chạy **bên trong** cluster liên tục so sánh "trạng thái Git repo khai báo" với "trạng thái cluster thực tế", tự động `apply` chênh lệch — không ai, kể cả pipeline CI, có quyền ghi trực tiếp vào cluster từ bên ngoài. Lợi ích: mọi thay đổi hạ tầng/app đều có lịch sử trong Git (audit tự nhiên), rollback chỉ là `git revert`, và phát hiện drift tự động (giống `terraform plan` nhưng chạy liên tục thay vì chạy tay). Thường dùng cho tầng K8s (app manifest/Helm chart), còn hạ tầng cloud nền (VPC, EKS cluster...) vẫn do Terraform quản lý — 2 công cụ bổ sung cho nhau chứ không thay thế.

**Đọc chi tiết:** [`10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md`](../10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md) — Học phần 8 (IaC). GitOps và Service Mesh (Chương 17) hiện là kiến thức mới hoàn toàn với repo này, chưa có tài liệu chi tiết riêng — phần giải thích trên là điểm khởi đầu, nên tìm hiểu thêm từ doc chính thức của ArgoCD khi thực hành.

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md` (Học phần 8-9).

#### Lab thực chiến
1. Viết Terraform tạo VPC + EC2 + Security Group (code hóa lại đúng những gì làm tay ở Chương 16).
2. Cấu hình Remote State trên S3 + lock DynamoDB, thử 2 terminal `apply` cùng lúc để thấy cơ chế lock hoạt động.
3. Dùng Ansible Playbook cài Docker + deploy container tự động lên EC2 vừa tạo bằng Terraform.

#### Sự cố thường gặp (Học phần 8 IaC)
- **State file mất/conflict** — 2 người `apply` cùng lúc không lock → hạ tầng thực tế lệch với state, lỗi khó lường.
- **`terraform apply` xóa nhầm resource production** — đổi tên resource khiến Terraform hiểu "xóa cũ + tạo mới" thay vì rename; luôn `terraform plan` kỹ, dùng `terraform state mv` khi đổi tên.
- **Secret bị commit vào state file** (lưu plaintext) — mã hóa S3 bucket chứa state, cân nhắc Vault cho secret thật sự nhạy cảm.
- **Ansible chạy không idempotent** — playbook viết ẩu khiến chạy lại nhiều lần cho kết quả khác nhau.
- **Drift hạ tầng** — ai đó sửa tay trên Console, lần sau `apply` sẽ cố "sửa lại" gây gián đoạn ngoài ý muốn.

#### Mock Project — ghép toàn bộ 9 học phần
```
Dev push code (Git) → CI/CD Pipeline (GitHub Actions/GitLab CI)
    → Run test + Build Docker Image → Push image lên ECR
    → Terraform apply hạ tầng: VPC, EKS cluster, RDS
    → Deploy lên Kubernetes qua Helm Chart
    → Prometheus + Grafana giám sát
```
**Checklist đồ án hoàn chỉnh:** branch strategy rõ ràng + pre-commit hook; pipeline CI scan bảo mật (`trivy image`); pipeline CD deploy staging có Manual Approval trước production; hạ tầng 100% code hóa bằng Terraform có Remote State; app K8s có Deployment/Service/Ingress/ConfigMap/Secret/HPA/health check; dashboard Grafana theo Golden Signals + Alert; `README.md` mô tả kiến trúc + Runbook; diễn tập 1 sự cố giả lập (kill Pod ngẫu nhiên — Chaos Engineering cơ bản) và viết postmortem.

**Sự cố thực chiến khi làm Mock Project:**
- **Thứ tự triển khai sai** — `helm install` khi EKS cluster chưa apply xong bằng Terraform.
- **Biến môi trường/secret không đồng bộ giữa các tầng** (Terraform output → K8s Secret → App env) — nên dùng 1 nguồn sự thật duy nhất (AWS Secrets Manager + External Secrets Operator).
- **Chi phí AWS vượt dự kiến** khi chạy EKS 24/7 cho đồ án cá nhân — nhớ `terraform destroy` sau demo.
- **Không ai đọc được hệ thống ngoài chính bạn** — thiếu Runbook/README, điểm bị trừ nhiều nhất khi phỏng vấn hỏi sâu.

</details>
**Bài tập:** viết Terraform tạo lại đúng VPC/EC2/Security Group đã làm tay ở Chương 16, sau đó dùng Ansible cài Docker + deploy container Flask (Chương 14) lên EC2 vừa tạo. Nâng cao: cài ArgoCD lên Minikube (Chương 17), trỏ vào 1 Git repo chứa Deployment YAML, sửa file trong repo và quan sát ArgoCD tự động đồng bộ vào cluster.

---

<a id="chuong-19"></a>
## Chương 19 — Incident Response & Deployment Strategies

**Kiến thức cần học:**

🟢 **Cơ bản (ôn nhanh):**
- Deployment strategy: rolling update, blue-green, canary — ưu/nhược mỗi loại.
- Rollback khi deploy lỗi — phải luôn có kế hoạch lùi lại được.

🟡 **Nâng cao (trọng tâm Middle):**
- Incident response cơ bản: phát hiện → giảm thiểu → khắc phục → viết postmortem.

🔴 **Chuyên sâu / Thực chiến:**
- Đọc war story thực tế để hiểu lỗi sản xuất thường xảy ra thế nào; áp dụng văn hóa postmortem blameless đúng cách trong thực tế (không chỉ biết khái niệm).
- **Chaos Engineering** (game day) — chủ động gây lỗi có kiểm soát để kiểm chứng hệ thống/quy trình thật sự chịu được sự cố, thay vì chỉ tin vào tài liệu "trên giấy".

**Giải thích chi tiết:**

🟢 *Cơ bản.* **Rolling update vs Blue-Green vs Canary.** Rolling update: thay dần từng Pod/server cũ bằng bản mới, không downtime, nhưng có khoảnh khắc cả bản cũ và mới cùng chạy song song. Blue-Green: dựng hẳn 1 môi trường mới (Green) chạy song song môi trường cũ (Blue), test xong mới chuyển 100% traffic sang Green — rollback cực nhanh nhưng tốn gấp đôi tài nguyên trong lúc chuyển. Canary: chuyển 1 phần nhỏ traffic (VD 5%) sang bản mới trước, theo dõi lỗi/metrics, ổn thì tăng dần lên 100% — rủi ro thấp nhất nhưng cần hạ tầng/monitoring tốt để tự động hóa.

```yaml
# Rolling update — khai báo ngay trong Deployment, K8s tự thực hiện
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1   # tối đa 1 Pod cũ bị gỡ cùng lúc
      maxSurge: 1         # tối đa 1 Pod mới được thêm vượt số replicas khai báo
```

```bash
# Rollback khi deploy lỗi — luôn phải có sẵn kế hoạch lùi lại
kubectl rollout undo deployment/backend-api
kubectl rollout status deployment/backend-api   # theo dõi tiến trình rollout/rollback
```

🟡 *Nâng cao.* **Incident response.** Quy trình chuẩn: phát hiện (alert) → giảm thiểu ngay (rollback/scale lên, chưa cần biết nguyên nhân gốc) → tìm nguyên nhân gốc → khắc phục triệt để → viết postmortem.

🔴 *Chuyên sâu/Thực chiến.* **Postmortem văn hóa blameless.** Postmortem ghi lại: chuyện gì xảy ra, tác động, nguyên nhân gốc, hành động phòng ngừa — văn hóa quan trọng nhất là **blameless** (không đổ lỗi cá nhân), vì mục tiêu là cải thiện hệ thống/quy trình, không phải tìm người để trách; áp dụng đúng văn hóa này trong thực tế khó hơn hẳn việc chỉ biết khái niệm.

**Chaos Engineering.** Kế hoạch disaster recovery "viết trên giấy" (VD quy trình failover sang region dự phòng) thường chứa giả định chưa từng bị kiểm chứng thật — khi sự cố thật xảy ra mới phát hiện ra 1 bước phụ thuộc (DNS chưa trỏ đúng, IAM Role ở vùng phụ thiếu quyền, dữ liệu chưa đồng bộ kịp) khiến quy trình "5 phút" thực tế mất hàng giờ. Chaos Engineering chủ động mô phỏng sự cố (VD tự kill 1 Pod ngẫu nhiên trong K8s, tự ngắt kết nối 1 service) trong môi trường kiểm soát được, biến mỗi lần diễn tập thành cơ hội tìm ra giả định sai **trước khi** sự cố thật xảy ra — độ tin cậy nằm ở việc kế hoạch đã được kiểm chứng bằng thực hành, không phải chỉ có tài liệu mô tả.

**Đọc chi tiết:** [`Mastery/Cloud-DevOps-Mastery/04-CICD-Deployment-Strategies`](../Mastery/Cloud-DevOps-Mastery/04-CICD-Deployment-Strategies), [`05-Observability-Incident-Response`](../Mastery/Cloud-DevOps-Mastery/05-Observability-Incident-Response), đọc 2-3 câu chuyện/tối ở [`07-Real-World-War-Stories-Fresher-To-Senior`](../Mastery/Cloud-DevOps-Mastery/07-Real-World-War-Stories-Fresher-To-Senior).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `Mastery/Cloud-DevOps-Mastery/04-CICD-Deployment-Strategies/README.md`, `Mastery/Cloud-DevOps-Mastery/07-Real-World-War-Stories-Fresher-To-Senior/README.md`.

#### So sánh chiến lược deploy đầy đủ

| Chiến lược | Cách hoạt động | Rollback | Phù hợp |
|---|---|---|---|
| Recreate | Tắt hết instance cũ, bật mới | Chậm, có downtime | Dev/staging |
| Rolling Update | Thay dần từng phần | Vừa phải | Đa số app web (mặc định K8s) |
| Blue-Green | Dựng môi trường mới song song | **Tức thì** | Cần rollback cực nhanh |
| Canary | Chuyển dần % traffic | Nhanh, chỉ ảnh hưởng % nhỏ | Traffic lớn, phát hiện bug trước khi ảnh hưởng toàn bộ |

**Vì sao Canary phát hiện bug mà staging không phát hiện được:** staging test với dữ liệu/traffic giả, quy mô nhỏ. Nhiều bug chỉ xuất hiện ở quy mô thật (race condition hàng nghìn user đồng thời). Canary cho 5% traffic THẬT chạy bản mới, theo dõi error rate/latency, tự động rollback trước khi ảnh hưởng 100% user — kỹ thuật Google/Netflix/Amazon dùng thường xuyên.

#### Chiến trường thực tế — 12 sự cố từ Fresher đến Senior

**🟢 Fresher:**
1. **Log không rotate, disk đầy crash server** — tăng dần không giới hạn chiếm hết dung lượng. Fix: `logrotate`, đẩy log ra hệ thống tập trung, alert khi disk >80%.
2. **Chứng chỉ TLS hết hạn lúc nửa đêm** — không có cơ chế gia hạn tự động. Fix: Let's Encrypt certbot cron, hoặc ACM tự gia hạn; cảnh báo khi cert còn <14 ngày.
3. **Rò rỉ AWS Access Key trên GitHub, bị dùng đào coin, hóa đơn hàng nghìn đô** — bot quét GitHub tìm key lộ, tạo EC2 GPU đào tiền trong vài phút. Fix: revoke key ngay, liên hệ AWS Support, bật GuardDuty + Billing Alert; không bao giờ dùng Access Key tĩnh — dùng IAM Role.

**🟡 Junior:**
4. **Docker image build kèm secret trong layer, dù đã "xóa" ở bước sau** — mỗi lệnh Dockerfile tạo 1 layer riêng, layer cũ vẫn lưu lại dù layer sau xóa file. Fix: không bao giờ copy secret vào image ở bất kỳ bước nào — dùng build secrets (`--secret` BuildKit) hoặc biến môi trường lúc runtime.
5. **SSH sửa lỗi khẩn, quên đồng bộ lại IaC** — tạo "configuration drift", lần deploy tiếp theo ghi đè lại cấu hình cũ. Fix: sửa tay chỉ để dừng chảy máu, BẮT BUỘC cập nhật IaC ngay sau đó.
6. **Deploy nhầm config staging lên production** — thiếu tách biệt environment trong pipeline. Fix: tách pipeline/approval flow theo environment, production luôn cần approval thủ công, đặt tên tài nguyên có tiền tố rõ ràng (`prod-`, `staging-`).

**🔴 Mid-level:**
7. **Pod bị OOMKilled liên tục dù traffic không tăng** — memory limit đặt quá sát mức dùng bình thường, GC tiệm cận giới hạn trước khi dọn dẹp. Fix: đặt limit có buffer dựa trên theo dõi dài hạn, không chỉ 1 lần test ngắn.
8. **TTL DNS quá dài, migrate server mới delay lan truyền nhiều giờ** — DNS resolver cache theo đúng TTL cũ. Fix: hạ TTL xuống thấp (60-300s) từ TRƯỚC vài ngày, giữ server cũ chạy song song.
9. **Tự khóa quyền của chính CI/CD pipeline khi siết IAM** — thu hẹp policy dựa trên đoán thay vì kiểm tra thực tế. Fix: dùng CloudTrail/IAM Access Analyzer xem action thực tế trước khi viết policy hẹp, luôn có break-glass account dự phòng.

**🔵 Senior:**
10. **Failover đa vùng chưa từng test thật, khi cần dùng thì không hoạt động** — kế hoạch chỉ tồn tại trên giấy. Fix: diễn tập failover định kỳ (game day/chaos engineering), coi mỗi lần diễn tập là cơ hội tìm giả định sai.
11. **Chi phí cloud tăng không kiểm soát, thiếu cost governance ở tầm tổ chức** — nhiều team tự tạo tài nguyên không theo chuẩn chung. Fix: tagging bắt buộc qua policy tự động, budget alert theo team, review chi phí định kỳ.
12. **1 database dùng chung cho 10 service, 1 migration lỗi làm sập toàn bộ nền tảng** — "trông như microservices" nhưng chia sẻ chung 1 tầng hạ tầng (single point of failure), blast radius rất lớn. Fix: tách database theo service (ít nhất instance riêng), giới hạn connection pool riêng từng service trong lúc chờ tách, review MỌI migration lớn trước khi chạy trên instance dùng chung.

</details>

---

## PHẦN V — SẴN SÀNG PHỎNG VẤN & SỰ NGHIỆP

<a id="chuong-20"></a>
## Chương 20 — System Design Interview Playbook

**Kiến thức cần học:**

🟢 **Cơ bản:** Khung trả lời câu hỏi System Design: Clarify → Ước lượng tải → Thiết kế high-level → Đi sâu 1-2 thành phần → Thảo luận trade-off — học thuộc khung này trước.

🔴 **Chuyên sâu / Thực chiến:** Luyện áp dụng khung vào đề bài thật cỡ Middle: URL shortener (Chương 11 mục 11.8), rate limiter (Chương 11 mục 11.9), hệ thống thông báo — luyện nói thành tiếng, không chỉ đọc hiểu.

**Giải thích chi tiết:**

🟢 *Cơ bản.* Khung trả lời chuẩn: **(1) Clarify** yêu cầu thật kỹ trước khi thiết kế (hỏi lại quy mô, giới hạn, ưu tiên) → **(2) Ước lượng tải** (back-of-envelope: bao nhiêu user, bao nhiêu request/giây, bao nhiêu dữ liệu/ngày) → **(3) Thiết kế high-level** (vẽ các khối chính: API, DB, cache, queue) → **(4) Đi sâu 1-2 thành phần** interviewer quan tâm nhất → **(5) Thảo luận trade-off** (không có thiết kế nào hoàn hảo, quan trọng là biết mình đang đánh đổi gì).

🔴 *Chuyên sâu/Thực chiến.* Khung chỉ có giá trị khi áp dụng được vào đề bài thật dưới áp lực thời gian — luyện nói thành tiếng với đề URL shortener/rate limiter (Chương 11) cho tới khi không còn phải nhớ từng bước, mà tự nhiên đi đúng thứ tự.

**Đọc chi tiết:** [`Mastery/Career-Mastery/02-System-Design-Interview-Playbook`](../Mastery/Career-Mastery/02-System-Design-Interview-Playbook).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `Mastery/Career-Mastery/02-System-Design-Interview-Playbook/README.md`.

#### Khung 5 bước — chi tiết thời gian
```
1. LÀM RÕ YÊU CẦU (5 phút) — Functional (hệ thống làm gì?); Non-functional (bao nhiêu user/request/giây? ưu tiên consistency hay availability?)
2. ƯỚC LƯỢNG QUY MÔ (5 phút) — QPS, dung lượng lưu trữ/năm, băng thông. Bước junior hay bỏ qua nhưng senior LUÔN làm.
3. THIẾT KẾ TỔNG QUAN (10 phút) — vẽ sơ đồ Client → LB → Service → DB/Cache
4. ĐÀO SÂU (15-20 phút) — chọn 1-2 điểm khó nhất: schema, chống race condition, scale bottleneck
5. XÁC ĐỊNH ĐIỂM YẾU & CẢI THIỆN (5 phút) — chủ động chỉ ra điểm yếu thiết kế của chính mình — dấu hiệu senior thật
```
**Sai lầm phổ biến khi luyện tập:** nhảy thẳng vào kiến trúc phức tạp (microservices, Kafka, sharding) mà chưa làm rõ quy mô thật. "Thiết kế Twitter" cho 1000 user và 1 tỷ user có đáp án hoàn toàn khác nhau.

#### Bộ câu hỏi làm rõ yêu cầu — dùng lại được
- "Hệ thống cần đọc nhiều hơn hay ghi nhiều hơn?" → quyết định SQL vs NoSQL, cần cache mạnh không.
- "Dữ liệu cần strong consistency hay eventual consistency chấp nhận được?" → số dư tài khoản vs số lượt like.
- "Có cần real-time không, hay batch định kỳ?" → quyết định WebSocket/queue hay cron job.
- "Traffic có tăng đột biến theo sự kiện không (flash sale)?" → ảnh hưởng auto-scaling, rate limiting.

#### Bản đồ: đề bài kinh điển → kiến thức cần dùng

| Đề bài | Kiến thức chính |
|---|---|
| URL Shortener | Hash Table (encode/decode); chọn DB đọc nhiều |
| Rate Limiter | Sliding Window + Hash Table |
| News Feed/Social Media | Graph (quan hệ follow); Queue cho fan-out |
| Autocomplete/Search | Trie |
| Đặt vé/Chống overselling | Transaction & Locking |
| Hệ thống thông báo | Queue, retry, idempotency |

**Cách luyện tập hiệu quả:** chọn 1 đề bài/tuần, tự làm đủ 5 bước trong 45 phút (đúng thời gian phỏng vấn thật), rồi tra bảng trên kiểm tra có bỏ sót khối kiến thức nào không.

#### Checklist tự đánh giá
1. Có ước lượng quy mô trước khi thiết kế không, hay nhảy thẳng vào vẽ sơ đồ?
2. Có tự chỉ ra điểm yếu/bottleneck của chính thiết kế mình không?
3. Có giải thích được TẠI SAO chọn công nghệ này thay vì công nghệ khác không (không chỉ liệt kê tên)?

</details>

---

<a id="chuong-21"></a>
## Chương 21 — Bộ câu hỏi phỏng vấn Junior → Middle

**Kiến thức cần học:**

🟢 **Cơ bản:** Tự hỏi-tự trả lời các câu hỏi lý thuyết (Python, Django/Flask, DB, Docker) theo đúng mức Middle.

🔴 **Chuyên sâu / Thực chiến:** Câu hỏi "vì sao chuyển từ Frappe sang Django/Flask" — chuẩn bị câu trả lời có chiều sâu, dùng chính note DJ-04 đã làm ở Chương 5; đây là câu hỏi riêng cho hồ sơ của bạn, không có sẵn đáp án mẫu nào dùng được.

**Giải thích chi tiết:**

🟢 *Cơ bản.* Mục tiêu không phải học thuộc câu trả lời mẫu, mà tập **trả lời ngắn gọn kèm ví dụ thực tế đã làm** — interviewer ở mức Middle thường hỏi tiếp "bạn đã gặp case này chưa, xử lý thế nào" ngay sau câu lý thuyết, trả lời suông không có ví dụ sẽ bị đánh giá là học vẹt.

🔴 *Chuyên sâu/Thực chiến.* Câu hỏi về lý do chuyển stack (Frappe → Django/Flask) không có đáp án mẫu dùng chung được — phải tự xây dựng từ đúng trải nghiệm cá nhân, nên đây luôn là câu khó chuẩn bị nhất dù nghe tưởng đơn giản nhất.

**Đọc chi tiết:** [`Mastery/Backend-Mastery/06-Fresher-To-Senior-Knowledge-And-Interview-Map`](../Mastery/Backend-Mastery/06-Fresher-To-Senior-Knowledge-And-Interview-Map), [`interview_prep/07_Cau_Hoi_Phong_Van.md`](../interview_prep/07_Cau_Hoi_Phong_Van.md), [`Mastery/Career-Mastery/03-Technical-Interview-Strategy-By-Stack`](../Mastery/Career-Mastery/03-Technical-Interview-Strategy-By-Stack).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `Mastery/Backend-Mastery/06-Fresher-To-Senior-Knowledge-And-Interview-Map/README.md`, `Mastery/Career-Mastery/03-Technical-Interview-Strategy-By-Stack/README.md`, `interview_prep/07_Cau_Hoi_Phong_Van.md` (Q1-13, Q57-60, Q120-123; Q61-65 OOP/SOLID đã nhúng ở [Chương 1](#chuong-1) để tránh trùng lặp; phần MATLAB/MCR nếu liên quan tới domain riêng).

#### Công thức trả lời câu hỏi lý thuyết — không chỉ định nghĩa suông
**Cấu trúc:** Định nghĩa ngắn → **Ví dụ thực tế đã áp dụng** → **Tradeoff/giới hạn**.

> ❌ Trả lời junior: "GIL là Global Interpreter Lock, nó khóa không cho nhiều thread chạy cùng lúc."
> ✅ Trả lời senior: "GIL đảm bảo chỉ 1 thread thực thi bytecode tại 1 thời điểm — KHÔNG ảnh hưởng I/O-bound vì GIL nhả khi chờ I/O, nhưng làm threading vô dụng cho CPU-bound. Trong dự án của em, khi cần resize hàng loạt ảnh, em chuyển từ `ThreadPoolExecutor` sang `ProcessPoolExecutor` và thấy tốc độ tăng gần 4 lần trên máy 4 lõi."

**Với câu "Tại sao chọn X thay vì Y":** luôn có ít nhất 2 tiêu chí so sánh, không trả lời 1 chiều. **Với câu debug/troubleshooting:** luôn trình bày theo QUY TRÌNH, không nhảy thẳng đáp án.

#### Bẫy thường gặp theo từng mảng

| Mảng | Bẫy hay gặp | Cách tránh |
|---|---|---|
| Python | Nhầm mutable default argument, nhầm `is` với `==` | Giải thích được VÌ SAO (tham chiếu bộ nhớ) |
| Database | "Index luôn tốt" không nhắc chi phí ghi | Luôn nêu tradeoff 2 chiều |
| Docker/K8s | Không phân biệt liveness vs readiness | Xem case study thật |
| Frontend/JS | Event Loop không phân biệt microtask/macrotask | Luôn có ví dụ code minh họa |

#### Bản đồ kiến thức theo cấp độ sự nghiệp

**🟢 Fresher (0-6 tháng):** Python nền tảng (list/tuple/dict/set, OOP cơ bản, try/except, context manager); SQL nền tảng (SELECT/JOIN, PK/FK); HTTP & REST cơ bản; Git cơ bản; 1 framework cơ bản (Flask/Django). *Mẫu trả lời "List vs tuple":* "List mutable, tuple immutable — nên tuple dùng được làm key dict còn list thì không; em dùng tuple khi muốn đảm bảo dữ liệu không bị vô tình sửa, ví dụ tọa độ (x, y)."

**🟡 Junior (6 tháng-2 năm):** ORM thành thạo; thiết kế REST API đúng chuẩn; N+1 query — nhận diện và fix; Testing với mock; Docker cơ bản; JWT/session auth. *Mẫu trả lời "N+1 problem":* "N+1 xảy ra khi lấy N bản ghi rồi với MỖI bản ghi query thêm 1 lần — 100 đơn hàng loop lấy `order.customer.name` tạo 101 query. Em phát hiện bằng bật query logging ở dev, fix bằng `select_related()`/`prefetch_related()`."

**🔴 Mid-level (2-4 năm):** Concurrency thật sự (GIL, asyncio/threading/multiprocessing); Database sâu (transaction, isolation, index strategy); Caching strategy; Message Queue; Observability cơ bản; CI/CD cơ bản. *Mẫu trả lời "Race condition":* "2 request đăng ký cùng username gần như đồng thời đều pass qua bước check tồn tại trước khi transaction nào commit. Em fix bằng unique constraint ở DB làm lớp bảo vệ cuối, bắt `IntegrityError` khi commit."

**⭐ Senior (4+ năm):** System Design toàn diện; kiến trúc microservices vs monolith (biết khi nào KHÔNG nên tách service); vận hành production (SLI/SLO, incident response, postmortem); kỹ năng lãnh đạo kỹ thuật. *Mẫu trả lời "Thiết kế rate limiter":* dùng khung 5 bước — làm rõ yêu cầu (theo user hay IP?) → ước lượng quy mô → dùng Redis cho counter dùng chung giữa nhiều instance (không lưu local) → chọn thuật toán sliding window log hoặc token bucket tùy độ chính xác cần.

#### Checklist trước khi vào phỏng vấn
1. Với mỗi công nghệ trong CV, có ít nhất 1 ví dụ THẬT đã áp dụng không?
2. Có thể giải thích tradeoff của MỌI quyết định kỹ thuật mình từng đưa ra không?
3. Đã chuẩn bị 2-3 câu hỏi ngược lại cho người phỏng vấn chưa?

#### Câu hỏi tình huống kỹ thuật + hành vi (Q120-123) — không có đáp án đúng tuyệt đối
**"Team member commit thẳng vào main và gây bug — xử lý thế nào?"** → Kỹ thuật: `git revert <commit>` (an toàn hơn `git reset` vì không xóa history), deploy revert ngay, verify production ổn. Quy trình (ngăn lần sau): bật branch protection trên `main`, bắt buộc Pull Request + Code Review, bắt buộc CI pass trước merge, viết postmortem blameless. Giao tiếp: không đổ lỗi cá nhân, tập trung cải thiện quy trình.

**"Nhận task không rõ requirements — làm sao?"** → Không code ngay khi mơ hồ: hỏi lại stakeholder ("Ai là người dùng? Đang giải quyết vấn đề gì?"), viết lại hiểu biết của mình để xác nhận ("Tôi hiểu task này là X, Y, Z — đúng không?"), xác định edge case, thống nhất scope (MVP trước, nice-to-have sau), chỉ estimate SAU khi đã rõ, ghi lại quyết định trong ticket/PR.

**"Nhận feedback code review rất tiêu cực — xử lý thế nào?"** → Mindset: review không phải công kích cá nhân, mà để cải thiện sản phẩm. Đọc kỹ xem reviewer đúng không; nếu đồng ý → sửa + cảm ơn; nếu không đồng ý → giải thích lý do, có thể đưa ra team thảo luận; nếu feedback không rõ → hỏi lại; không phòng thủ ("sao anh/chị không thích code em?"); nếu lặp lại nhiều lần → 1-1 với reviewer để thống nhất coding standard.

**"Deadline gấp nhưng chất lượng code phải hạ thấp — xử lý thế nào?"** → Đây là tradeoff, không có đáp án tuyệt đối: báo sớm cho lead/manager ngay khi thấy rủi ro; cắt scope (tính năng nào thực sự cần cho deadline, cái nào nice-to-have); lên kế hoạch technical debt rõ ràng (ship kèm TODO, tạo ticket, lên lịch dọn sau); ghi lại tradeoff đã chọn ("dùng cách X vì deadline, dự định refactor Y sau"); **không bao giờ** thỏa hiệp bảo mật/mất dữ liệu — có thể bỏ qua tối ưu hiệu năng, không được bỏ qua input validation.

</details>

---

<a id="chuong-22"></a>
## Chương 22 — Xây Project Portfolio & Kể chuyện STAR

**Kiến thức cần học:**

🟡 **Nâng cao:** Ghép API Django (Chương 6) + Flask (Chương 7) thành 1 mini mock project chạy end-to-end, deploy thật lên K8s/EC2 (Chương 16-17), code hóa hạ tầng bằng Terraform/Ansible (Chương 18); viết README/Runbook chuẩn chuyên nghiệp cho project.

🔴 **Chuyên sâu / Thực chiến:** Chuẩn bị 2-3 câu chuyện theo mô hình STAR (Situation - Task - Action - Result) — khó nhất vì phải tự rút ra từ kinh nghiệm thật, không có đáp án mẫu.

**Giải thích chi tiết:**

🟡 *Nâng cao.* Project portfolio là bằng chứng cụ thể thay vì chỉ nói "tôi biết Django/K8s" — ghép nhiều kỹ năng đã học thành 1 sản phẩm chạy thật, deploy thật, có README/Runbook chuyên nghiệp (người khác đọc vào là hiểu được chạy thế nào, không cần hỏi lại bạn).

🔴 *Chuyên sâu/Thực chiến.* STAR là khung kể chuyện giúp câu trả lời phỏng vấn có cấu trúc rõ ràng thay vì kể lan man — đặc biệt hữu ích khi kể lại kinh nghiệm thực tế ở công ty hiện tại, không chỉ project tự làm; khó vì phải tự rút ra câu chuyện đúng, khung chỉ giúp sắp xếp lại cho mạch lạc.

**Đọc chi tiết:** [`interview_prep/08_Du_An_Thuc_Te.md`](../interview_prep/08_Du_An_Thuc_Te.md).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> ⚠️ **Lưu ý quan trọng:** Các dự án dưới đây (eCommerce Migration, Viet Kiosk, MBW Suite, Traditional Medicine Platform) là **ví dụ mẫu từ tài liệu tham khảo trong repo — KHÔNG phải dự án thật của bạn**. Dùng để học **CÁCH trình bày** 1 dự án trong phỏng vấn (kiến trúc, câu hỏi hay gặp, code pattern, khung STAR), không phải để học thuộc nội dung cụ thể rồi nhận là của mình — người phỏng vấn senior sẽ hỏi xoáy sâu chi tiết thật ("con số cụ thể là bao nhiêu?") và lộ ngay nếu không phải trải nghiệm thật. Hãy áp dụng đúng KHUNG này cho dự án thật của chính bạn (Frappe + Vue, hoặc project portfolio tự xây ở Chương 22).
>
> Nguồn: `interview_prep/08_Du_An_Thuc_Te.md`, `interview_prep/07_Cau_Hoi_Phong_Van.md` (Q48-52).

#### Ví dụ 1: Nền tảng thương mại dược liệu (Flask, PostgreSQL + MongoDB)
**Kiến trúc:** Frontend → Flask Backend → PostgreSQL (Users/Orders) + MongoDB (Products/Categories).
**Câu hỏi hay gặp — "Tại sao dùng cả PostgreSQL lẫn MongoDB?"** → "PostgreSQL cho dữ liệu quan hệ chặt chẽ (users, orders); MongoDB cho product catalog vì mỗi loại sản phẩm có attributes khác nhau — schema linh hoạt phù hợp hơn."
```python
class UserRole(Enum):
    PRACTITIONER = "practitioner"
    BUSINESS = "business"

def require_roles(*roles):
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def wrapper(*args, **kwargs):
            if get_current_user().role not in roles:
                return jsonify({"error": "Access denied"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator
```
**"Scale platform thế nào nếu user tăng 10x?"** → Thêm Redis cache cho sản phẩm hay truy cập; PostgreSQL read replica cho query báo cáo; CDN cho static asset (ảnh sản phẩm); background job (Celery) cho email/report thay vì xử lý đồng bộ.

#### Ví dụ 2: Dịch vụ migrate dữ liệu eCommerce (Python, Docker, Adapter Pattern)
**Kiến trúc:** Source Platform APIs → Source Adapter → Extract/Transform/Load → Migration Engine → Job Queue (Celery+Redis) → Progress WebSocket.
```python
class ECommerceAdapter(ABC):
    @abstractmethod
    def get_products(self, page: int, page_size: int) -> list: ...
    @abstractmethod
    def get_orders(self, since: datetime) -> list: ...

class ShopifyAdapter(ECommerceAdapter):
    def get_products(self, page, page_size):
        return self.client.Product.find(page=page, limit=page_size)

def create_adapter(platform: str, credentials: dict) -> ECommerceAdapter:
    adapters = {"shopify": ShopifyAdapter, "woocommerce": WooCommerceAdapter}
    return adapters[platform](**credentials)
```
**"Làm sao đảm bảo migration không mất data?"** → Pre-migration: count + checksum nguồn. During: transaction per batch, log mọi record. Post: count + spot-check target. Rollback: giữ source không đổi, drop target nếu fail.

**"Tại sao dùng Docker trong dự án này?"** → Mỗi nguồn eCommerce cần SDK/client library khác nhau (Shopify SDK, Magento 2 API, WooCommerce REST client) — có thể xung đột dependency; Docker cô lập dependency theo từng service, đồng thời đảm bảo dev environment = production environment.

**"PrestaShop connection error — debug thế nào?"** → Bật logging verbose, test từng bước riêng lẻ → phát hiện driver version không tương thích với MariaDB → fix: pin đúng version driver, ghi lại cho team, thêm integration test để bắt sớm lần sau.
```python
class MigrationValidator:
    def validate_product(self, product: dict) -> ValidationResult:
        errors = []
        if not product.get("sku"):
            errors.append("SKU is required")
        if product.get("price", 0) < 0:
            errors.append("Price cannot be negative")
        if product.get("category_id") and not self.category_exists(product["category_id"]):
            errors.append(f"Category {product['category_id']} not found")
        return ValidationResult(is_valid=len(errors) == 0, errors=errors)
```

#### Ví dụ 3: Hệ thống kiosk (Next.js, WebSocket, tích hợp thanh toán)
```javascript
function useWebSocket(url) {
    const connect = () => {
        wsRef.current = new WebSocket(url);
        wsRef.current.onclose = () => {
            setStatus('disconnected');
            reconnectTimeout.current = setTimeout(connect, 3000);
        };
    };
}
```
**"Banking integration — security considerations?"** → HTTPS/TLS mọi giao tiếp; signature verification (HMAC) cho webhook; idempotency key tránh duplicate charge; audit log mọi transaction; timeout + retry với circuit breaker.

**"Kiosk bị offline thì xử lý thế nào?"** → Thiết kế offline-first: cache dữ liệu bệnh nhân vào LocalStorage; background sync khi reconnect; UI thông báo rõ trạng thái offline; tính năng tối quan trọng (in biên lai) phải hoạt động được cả khi offline.

#### Ví dụ 4: Nền tảng AI tuyển dụng (LLM integration, validation)
```python
class GeneratedCV(BaseModel):
    summary: str = Field(..., min_length=50, max_length=500)
    skills: List[str] = Field(..., min_items=3)

def generate_cv(self, candidate_info: dict) -> GeneratedCV:
    for attempt in range(3):
        try:
            response = self.client.chat.completions.create(..., response_format={"type": "json_object"})
            return GeneratedCV.model_validate_json(response.choices[0].message.content)
        except Exception:
            if attempt == 2:
                return self._template_cv(candidate_info)
```
**"Tránh hallucination khi LLM generate CV?"** → Structured output (yêu cầu JSON schema cụ thể); Few-shot prompting; Validation layer (reject nếu sai schema); Human review cho case nhạy cảm; Fallback template-based nếu LLM fail.

**"Làm sao integrate 6+ microservices trong 1 platform?"** → Dùng Frappe Framework làm application server chính (có sẵn authentication/permissions/REST API/real-time); mỗi app con là Frappe app riêng, dùng chung database và authentication; giao tiếp qua event system của Frappe và REST API nội bộ.

**"Làm sao ensure accuracy khi có phần tính toán ngoài (MATLAB MCR)?"** → Unit test với input/output đã biết trước; cross-validation chạy song song bản fallback Python và so sánh; monitoring log chênh lệch nếu vượt ngưỡng; regression test mỗi lần deploy; A/B test với mẫu nhỏ trước khi áp dụng production.

#### Template trả lời về dự án — khung STAR
```
S - Situation: Bối cảnh, vấn đề cần giải quyết
T - Task: Nhiệm vụ cụ thể của bạn
A - Action: Hành động cụ thể BẠN đã làm (dùng "tôi", không "chúng tôi")
R - Result: Kết quả định lượng được
```
**Ví dụ áp dụng (mẫu, không phải của bạn):**
```
S: "Client cần migrate 50.000 sản phẩm từ Shopify sang PrestaShop mà không downtime"
T: "Tôi phụ trách migration engine phía backend và tích hợp PrestaShop"
A: "Tôi thiết kế Adapter Pattern để trừu tượng hóa nhiều nguồn/đích khác nhau,
    implement batch processing có checkpoint/resume, debug lỗi driver không
    tương thích với MariaDB"
R: "Migration hoàn thành trong 8 tiếng, 0 data loss, nền tảng tái sử dụng
    được cho nhiều client khác"
```

</details>
**Bài tập:** đúng với Tuần 18-19 trong [`00-Lich-Hoc-Toi/Lich_Trinh_Toi_Den_Tet.md`](00-Lich-Hoc-Toi/Lich_Trinh_Toi_Den_Tet.md).

---

<a id="chuong-23"></a>
## Chương 23 — Đàm phán lương & Định hướng sự nghiệp

**Kiến thức cần học:**

🟢 **Cơ bản:** Đã có kinh nghiệm đi làm, chương này giúp chuẩn hóa lại cách định giá bản thân khi phỏng vấn công ty mới; Behavioral interview (câu hỏi về thái độ, xử lý xung đột) — khác hoàn toàn câu hỏi kỹ thuật.

🔴 **Chuyên sâu / Thực chiến:** Mặt bằng lương Middle Backend/DevOps tại Việt Nam, cách thương lượng thật, thời điểm nên/không nên nhận offer.

**Giải thích chi tiết:**

🟢 *Cơ bản.* Behavioral interview khác hoàn toàn câu hỏi kỹ thuật — hỏi về cách bạn xử lý xung đột, deadline gấp, sai lầm từng mắc phải; nên chuẩn bị trước bằng chính khung STAR ở Chương 22.

🔴 *Chuyên sâu/Thực chiến.* Đàm phán lương: biết mặt bằng thị trường **trước khi** vào phỏng vấn (không để công ty định giá một chiều), và hiểu rằng thời điểm tốt nhất để đàm phán là **sau khi có offer**, không phải trước đó — đây là kỹ năng chỉ luyện được qua thực chiến, không có công thức cố định.

**Đọc chi tiết:** [`Mastery/Career-Mastery/04-Behavioral-And-Salary-Negotiation`](../Mastery/Career-Mastery/04-Behavioral-And-Salary-Negotiation), [`05-Salary-Growth-Playbook`](../Mastery/Career-Mastery/05-Salary-Growth-Playbook).

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> Nguồn: `Mastery/Career-Mastery/04-Behavioral-And-Salary-Negotiation/README.md`, `Mastery/Career-Mastery/05-Salary-Growth-Playbook/README.md`, `01-Roadmaps/Expert_Mastery_Roadmap_Project.md`, `interview_prep/07_Cau_Hoi_Phong_Van.md` (Q57-60).

#### Khung STAR — ví dụ đầy đủ
> Câu hỏi: *"Kể về 1 lần bạn gặp bug khó và cách giải quyết."*
> - **S:** "Hệ thống thanh toán bị lỗi double-charge cho ~0.1% giao dịch, chỉ xảy ra khi user bấm submit nhanh liên tiếp."
> - **T:** "Em được giao điều tra và fix trong 2 ngày vì ảnh hưởng trực tiếp tới tiền khách hàng."
> - **A:** "Em xác định đây là race condition — 2 request gần như đồng thời cùng đọc trạng thái đơn hàng 'chưa thanh toán' trước khi cái nào kịp cập nhật. Em fix bằng unique constraint ở DB kết hợp idempotency key gửi từ client."
> - **R:** "Sau khi deploy, tỷ lệ lỗi giảm về 0 trong 3 tháng theo dõi, và em viết thêm postmortem để team áp dụng idempotency key cho toàn bộ API thanh toán khác."

#### 4-5 câu chuyện "lõi" — dùng linh hoạt cho nhiều câu hỏi

| Câu chuyện lõi | Dùng trả lời cho câu hỏi dạng |
|---|---|
| 1 lần bug khó đã giải quyết | "Thử thách kỹ thuật khó nhất", "Cách bạn debug vấn đề phức tạp" |
| 1 lần bất đồng quan điểm kỹ thuật với đồng nghiệp | "Xử lý xung đột" |
| 1 lần deadline gấp / ưu tiên công việc | "Quản lý thời gian", "Áp lực công việc" |
| 1 lần mắc lỗi và cách khắc phục | "Điểm yếu của bạn", "Bài học từ thất bại" |
| 1 lần chủ động đề xuất cải tiến ngoài phạm vi được giao | "Chủ động trong công việc" |

#### Đàm phán lương — nguyên tắc thực tế
- **Không nói con số trước nếu có thể tránh:** "Em muốn tìm hiểu thêm về phạm vi công việc trước, nhưng tin công ty có mức lương cạnh tranh — anh/chị có thể chia sẻ range không?" — người hỏi trước ở thế bất lợi hơn.
- **Luôn có khoảng (range)**, neo mức thấp nhất = mức thật sự chấp nhận được, không phải mức mong muốn tối đa.
- **Tổng thu nhập (Total Compensation):** thưởng, bảo hiểm, ngày nghỉ phép, remote policy, ngân sách học tập — đều quy đổi được giá trị.
- **Có offer khác là đòn bẩy mạnh nhất** — nhưng phải trung thực, không bịa offer giả (ngành công nghệ "nhỏ", tin đồn lan nhanh).
- **Im lặng là công cụ:** sau khi nêu số mong muốn, đừng vội giải thích/xin lỗi thêm — để khoảng lặng cho phía tuyển dụng phản hồi.

#### Câu hỏi ngược lại nhà tuyển dụng
- "Đâu là thử thách kỹ thuật lớn nhất team đang đối mặt trong 6 tháng tới?"
- "Quy trình xử lý sự cố (incident response) của team ra sao — có postmortem văn hóa không?"
- "Technical debt lớn nhất hiện tại của hệ thống là gì, và có kế hoạch giải quyết không?"

#### Sự thật đầu tiên: lương phản ánh RỦI RO công ty gánh khi thiếu bạn, không phản ánh nỗ lực
Công ty trả theo **mức độ khó thay thế bạn** và **quy mô thiệt hại nếu bạn làm sai/nghỉ việc**. Kỹ sư A làm đúng task được giao, ai cũng làm được tương tự → dễ thay thế → lương neo thấp. Kỹ sư B là người duy nhất hiểu tại sao hệ thống thiết kế như vậy, tự phát hiện và ngăn sự cố trước khi xảy ra → khó thay thế → lương phản ánh đúng rủi ro.

#### Bảng tín hiệu theo cấp độ

| Cấp độ | Tín hiệu kỹ thuật | Câu hỏi phỏng vấn điển hình |
|---|---|---|
| Fresher | Code chạy đúng logic được giao | "Giải thích code này làm gì" |
| Junior | Tự debug lỗi không rõ nguyên nhân, viết test cơ bản | "Kể 1 lần bạn tự tìm ra nguyên nhân 1 lỗi khó" |
| Mid | Tự ra quyết định kỹ thuật có tradeoff | "Tại sao bạn chọn X thay vì Y?" |
| Senior | Thiết kế kiến trúc/quy trình ngăn CẢ LỚP vấn đề lặp lại | "Kể 1 lần bạn thay đổi QUY TRÌNH của team" |

#### Ba bẫy tư duy khiến người có năng lực vẫn bị trả lương thấp
1. "Chờ được ghi nhận" thay vì chủ động tạo bằng chứng (kể lại giá trị bằng khung STAR).
2. Học dàn trải nhiều công nghệ nhưng không có dự án thật chứng minh — nhà tuyển dụng định giá "bạn từng tự tay giải quyết vấn đề gì", không phải "bạn biết gì".
3. Không bao giờ phỏng vấn công ty khác vì "đang ổn định" — mất cơ chế duy nhất để tự kiểm chứng giá trị thật trên thị trường.

#### Case study minh họa — 2 lộ trình khác nhau từ cùng 1 điểm xuất phát
*(Tình huống mang tính điển hình, tổng hợp từ các mẫu hình phổ biến trên thị trường, không phải 1 cá nhân cụ thể.)* Kỹ sư X và Y cùng vào nghề với mức lương 10-12 triệu, vị trí Junior Fullstack outsource. **X sau 2 năm vẫn ở mức ~14 triệu:** ở lại 1 công ty, nhận task đều đặn, hoàn thành đúng hạn — nhưng chưa từng chủ động đề xuất thay đổi kiến trúc, chưa viết test trừ khi được yêu cầu, chưa từng phỏng vấn công ty khác để biết mình đang được định giá bao nhiêu. **Y sau 18 tháng đạt ~28 triệu:** sau 6 tháng đầu tương tự X, Y bắt đầu tự làm 1 dự án cá nhân có CI/CD + test + deploy thật, chủ động đề xuất thêm cache khi phát hiện API chậm (dù không được giao), và **đi phỏng vấn 3 công ty khác ở tháng thứ 10** dù chưa chắc nghỉ — nhận ra mình đang bị trả dưới giá thị trường, dùng offer đó đàm phán lại, rồi nhảy việc. Khác biệt cốt lõi không phải "Y giỏi hơn X 2 lần" — mà là Y liên tục tạo ra **bằng chứng đo lường được** và **liên tục kiểm tra lại giá trị bản thân với thị trường thật**, thay vì tự đánh giá một mình rồi chờ công ty tự nhận ra.

**Câu hỏi tự đánh giá:** Trong 3 tháng gần nhất, bạn có làm điều gì mà **nếu nghỉ, người khác sẽ khó thay thế ngay** không? Bạn có đang giữ 1 dự án thật (không phải bài tập) làm bằng chứng năng lực, cập nhật định kỳ không? Lần gần nhất bạn phỏng vấn 1 công ty khác (kể cả không có ý định nghỉ) là khi nào?

#### Lộ trình Expert Mastery — tài nguyên học tập tham khảo
Giai đoạn 1 (Foundations, tháng 1-6): Vue 3, Python nâng cao (AsyncIO/Decorators/FastAPI), SQL nâng cao, chứng chỉ AWS SAA-C03. Giai đoạn 2 (Cloud-Native, tháng 7-18): CI/CD, Dockerize, IaC (CDK/Terraform), Lambda/API Gateway/SQS/SNS. Giai đoạn 3 (Master Architect, tháng 19+): Microservices, Event-Driven Architecture, AWS WAF/KMS, mentoring/code review.

**Thử thách Expert:** (1) Zero Downtime — cập nhật code không ngắt quãng (Blue-Green); (2) Cost Optimization — Lifecycle Policy tự xóa/nén file cũ; (3) High Security — DB không truy cập trực tiếp từ Internet, mọi truy cập qua API Gateway + Lambda.

#### Checklist chuẩn bị
1. Đã viết 4-5 câu chuyện lõi theo khung STAR, có số liệu kết quả cụ thể chưa?
2. Đã xác định rõ range lương chấp nhận được (dựa trên nghiên cứu thị trường thật) chưa?
3. Đã chuẩn bị 3 câu hỏi ngược lại thể hiện tư duy chủ động chưa?

</details>

---

## 📌 Cách dùng cuốn sách này

1. Đi theo đúng thứ tự Chương 1 → 23, khớp với 5 chặng trong [`Lich_Trinh_Toi_Den_Tet.md`](00-Lich-Hoc-Toi/Lich_Trinh_Toi_Den_Tet.md) (Chặng 1 ≈ Chương 1-5, Chặng 2 ≈ Chương 6+2, Chặng 3 ≈ Chương 7+14, Chặng 4 ≈ Chương 15-16, Chặng 5 ≈ Chương 17-22, trong đó Chương 18 — IaC — làm ngay sau K8s cơ bản, trước khi ghép project cuối khóa).
2. Mỗi chương đọc theo thứ tự: **Kiến thức cần học** (biết cần nắm gì, chia theo 3 cấp độ) → **Giải thích chi tiết** (hiểu vì sao quan trọng, hoạt động thế nào, dễ sai ở đâu, có code ví dụ) → nếu cần sâu hơn, bấm mở khối **📚 Nội dung đầy đủ** (đã nhúng sẵn toàn bộ tài liệu gốc liên quan — không cần rời khỏi sách) → **Đọc chi tiết** chỉ còn là link tham khảo/tra cứu khi tài liệu nguồn cập nhật sau này, không bắt buộc phải mở.
3. Dùng 3 cấp độ 🟢/🟡/🔴 để **ôn đúng tốc độ** thay vì đọc dàn trải như nhau cho mọi mục:
   - Lần ôn đầu tiên trong tuần: đọc hết 🟢, lướt nhanh 🟡, bỏ qua 🔴 — mục tiêu là có bản đồ tổng thể.
   - Lần học chính (code theo): tập trung 🟡 — đây là khối lượng kiến thức Middle thật sự cần nắm chắc.
   - Trước khi phỏng vấn hoặc khi đã thấy 🟡 vững: quay lại đọc kỹ 🔴 — đây là phần phân biệt Middle với Senior, và là phần hay bị hỏi xoáy sâu nhất.
4. Chương 20-23 (System Design, phỏng vấn, portfolio, lương) chỉ nên đọc kỹ vào Chặng 5 (sát Tết) — đọc quá sớm sẽ quên vì chưa có đủ nền ở Chương 1-19.
5. Nếu đọc xong phần "Giải thích chi tiết" của 1 mục mà vẫn chưa thấy rõ "vì sao quan trọng" — đó là dấu hiệu nên đọc kỹ tài liệu gốc ở mục "Đọc chi tiết" thay vì học thuộc khái niệm suông.

---

## 📖 Glossary — Tra cứu nhanh thuật ngữ

> Dùng `Ctrl+F` tìm đúng từ cần tra. Mỗi dòng chỉ 1 câu định nghĩa ngắn — nếu cần hiểu sâu, quay lại đúng chương ghi trong ngoặc để đọc phần "Giải thích chi tiết" đầy đủ. Không học thuộc bảng này — đây là nơi **ôn lại**, không phải nơi **học lần đầu**.

### Phần I — Nền tảng

| Thuật ngữ | Định nghĩa ngắn | Chương |
|---|---|---|
| **GIL** | Global Interpreter Lock — chỉ 1 thread Python chạy bytecode tại 1 thời điểm, multi-thread không tăng tốc CPU-bound | 1 |
| **Decorator** | Hàm bọc quanh hàm khác để thêm hành vi mà không sửa code gốc (`@foo`) | 1 |
| **Generator** | Trả giá trị từng cái một (`yield`), không load hết vào RAM, chỉ duyệt được 1 lần | 1 |
| **Context Manager** | `with` block — tự dọn tài nguyên dù có lỗi hay không | 1 |
| **Dataclass** | `@dataclass` tự sinh `__init__`/`__repr__`/`__eq__` cho class chỉ chứa data | 1 |
| **Factory Pattern** | Gom logic "tạo object loại nào" về 1 chỗ thay vì gọi constructor trực tiếp khắp nơi | 1 |
| **Strategy Pattern** | Đóng gói nhiều thuật toán cùng interface, đổi được lúc runtime | 1 |
| **Dependency Injection (DI)** | Truyền dependency từ ngoài vào thay vì class tự tạo — dễ test, dễ đổi implementation | 1 |
| **Clean/Hexagonal Architecture** | Business logic không phụ thuộc framework/DB, tách thành lớp lõi riêng | 1 |
| **Poetry / pip-tools** | Quản lý dependency bằng lock file, khóa version chính xác toàn bộ cây phụ thuộc | 1 |
| **`rebase` vs `merge`** | Rebase viết lại lịch sử (thẳng, không rebase nhánh đã chia sẻ); merge giữ lịch sử thật | 2 |
| **`git bisect`** | Binary search trên lịch sử commit để tìm chính xác commit gây lỗi | 2 |
| **Trunk-Based Development** | Commit thẳng vào `main`, dùng feature flag thay vì giữ nhánh dài hạn — hợp CI/CD liên tục | 2 |
| **ACID** | Tính chất transaction: Atomicity/Consistency/Isolation/Durability | 3 |
| **Isolation Level** | Read Committed / Repeatable Read / Serializable — mức 2 transaction thấy dữ liệu của nhau | 3 |
| **Deadlock** | 2 transaction khóa chéo nhau, cả hai cùng chờ, DB phải hủy 1 cái | 3 |
| **B-Tree Index / Composite Index** | Cấu trúc tăng tốc tìm kiếm theo cột; composite index chỉ hiệu quả đúng thứ tự cột trái sang phải | 3 |
| **Normalization / Denormalization** | Chuẩn hóa tách bảng tránh trùng lặp; phá chuẩn có chủ đích để đọc nhanh hơn | 3 |
| **Replication / Sharding** | Replication nhân bản DB để scale đọc; sharding chia dữ liệu ra nhiều DB vật lý (phương án cuối) | 3 |
| **Connection Pooling / PgBouncer** | Giữ sẵn connection DB để tái dùng thay vì mở mới mỗi request; PgBouncer gộp connection ở tầng ngoài | 3 |
| **Zero-downtime migration** | Thêm cột: nullable trước → populate data → thêm NOT NULL sau, tránh khóa bảng/breaking app cũ | 3 |
| **Polyglot persistence** | Dùng nhiều loại DB khác nhau, mỗi loại giải quyết đúng 1 bài toán nó mạnh nhất | 3 |
| **Document / Embedding vs Referencing** | MongoDB lưu dữ liệu dạng JSON schema-less; embedding nhúng dữ liệu con, referencing tham chiếu riêng | 3 |
| **LRU Cache** | Loại bỏ phần tử lâu không dùng nhất khi cache đầy | 4 |

### Phần II — Backend Framework

| Thuật ngữ | Định nghĩa ngắn | Chương |
|---|---|---|
| **Signal** | Code tự chạy khi có sự kiện ở model khác, không cần model đó biết tới | 5 |
| **Middleware** | Lớp xử lý request/response chạy cho mọi request, xếp thành chuỗi | 5 |
| **N+1 query** | Lấy N dòng rồi query thêm N lần cho từng dòng thay vì gộp 1-2 query | 5 |
| **`select_related` / `prefetch_related`** | Gộp N+1 query thành 1-2 query bằng JOIN (FK) hoặc query riêng ghép ở Python (M2M) | 5 |
| **Serializer** | Chuyển model ↔ JSON, kèm validate — tương tự Pydantic nhưng gắn với Django ORM | 6 |
| **JWT access/refresh token** | Access token sống ngắn để gọi API; refresh token sống dài chỉ để xin access token mới | 6 |
| **Throttling** | Giới hạn số request/phút theo user/IP | 6 |
| **FastAPI / Pydantic** | Framework async-first; Pydantic validate input tự động từ type hint | 7 |
| **Blueprint** | Chia code Flask thành module độc lập khi project lớn dần | 7 |
| **Unit test vs Integration test** | Unit test mock hết, chạy nhanh; integration test chạy nhiều phần thật, chậm hơn nhưng bắt lỗi chỗ nối | 8 |
| **TDD** | Viết test trước code triển khai | 8 |
| **Load testing (Locust/k6)** | Giả lập nhiều user đồng thời để đo throughput/latency dưới tải | 8 |
| **Idempotency** | Request gửi lại nhiều lần vẫn cho cùng 1 kết quả, không tác dụng phụ nhân đôi | 9 |
| **Cursor-based pagination** | Phân trang bằng `?after=<id>` thay vì `?page=N`, ổn định hơn với dữ liệu đổi liên tục | 9 |
| **OpenAPI/Swagger** | Bản mô tả API tự sinh từ code, Swagger UI đọc ra giao diện test trực quan | 9 |
| **gRPC** | Giao tiếp service-to-service dùng Protocol Buffers, nhanh hơn REST/JSON | 9 |
| **GraphQL** | Client tự khai báo field cần lấy trong 1 query, tránh over/under-fetching | 9 |
| **WebSocket / SSE** | WebSocket 2 chiều liên tục; SSE 1 chiều server→client, tự reconnect | 9 |

### Phần III — Kiến trúc & Vận hành

| Thuật ngữ | Định nghĩa ngắn | Chương |
|---|---|---|
| **WSGI vs ASGI** | WSGI: 1 request = 1 thread/process, chặn khi chờ I/O; ASGI hỗ trợ async, xử lý nhiều request chờ cùng lúc | 10 |
| **BackgroundTasks (FastAPI)** | Chạy nền trong cùng process — mất task nếu server restart, khác queue thật (Celery) | 10 |
| **Cache-aside / Write-through / Write-behind** | 3 chiến lược ghi cache: tự check-miss-ghi / ghi đồng thời DB+cache / ghi cache trước rồi flush DB sau | 11 |
| **Cache stampede** | Key hot hết hạn, hàng loạt request cùng miss dồn vào DB — chống bằng early expiration/lock | 11 |
| **RabbitMQ vs Kafka** | RabbitMQ: 1 message → 1 consumer (task queue); Kafka: log bền vững, nhiều consumer group đọc độc lập | 11 |
| **Consistent Hashing** | Hash ít xáo trộn key khi thêm/bớt node, dùng trong cache/sharding phân tán | 11 |
| **CAP theorem / PACELC** | Khi có network partition: chọn CP hay AP; PACELC mở rộng thêm trade-off Latency vs Consistency lúc bình thường | 11 |
| **Eventual consistency / Read-your-writes** | Replica có thể trễ so với primary; đọc lại dữ liệu vừa ghi nên đọc từ primary | 11 |
| **Circuit Breaker** | Ngắt mạch khi service downstream lỗi liên tục, fail fast thay vì chờ timeout, tránh lỗi dây chuyền | 11 |
| **OWASP Top 10** | Danh sách lỗ hổng bảo mật web phổ biến nhất (SQL Injection, XSS, CSRF...) | 12 |
| **OAuth2** | Chuẩn ủy quyền (login bằng Google) qua Authorization Code flow | 12 |
| **Token Bucket vs Fixed Window** | Token Bucket nạp đều theo thời gian, mượt hơn Fixed Window (vốn bị lách ở biên khung thời gian) | 12 |
| **Vault / Sealed Secrets** | HashiCorp Vault quản lý secret tập trung có xoay vòng; Sealed Secrets mã hóa secret ngay trong Git | 12 |
| **SCA (Dependency scanning)** | Quét package bên thứ 3 tìm CVE đã công bố (`safety`, `pip-audit`, Dependabot) | 12 |
| **Golden Signals** | Latency, Traffic, Errors, Saturation — 4 chỉ số đầu tiên cần nhìn khi có sự cố | 13 |
| **Prometheus / Grafana** | Prometheus thu thập metrics kiểu pull; Grafana vẽ dashboard | 13 |
| **Distributed Tracing** | Theo dõi 1 request qua nhiều service bằng `trace_id` xuyên suốt (Jaeger/OpenTelemetry) | 13 |
| **SLO-based alerting** | Báo động theo error budget còn lại, thay vì ngưỡng CPU/Memory đơn thuần | 13 |

### Phần IV — DevOps

| Thuật ngữ | Định nghĩa ngắn | Chương |
|---|---|---|
| **Virtualization vs Containerization** | VM ảo hóa cả OS (nặng); container dùng chung kernel host (nhẹ, nhanh) | 14 |
| **Multi-stage build** | Build ở 1 stage đầy đủ, chỉ copy kết quả cuối sang stage runtime tối giản | 14 |
| **Layer 4 vs Layer 7 (Load Balancer)** | L4 chỉ nhìn TCP/UDP (nhanh); L7 đọc được HTTP header/path (route thông minh hơn) | 14 |
| **SAST vs SCA** | SAST quét code tự viết tìm pattern nguy hiểm; SCA quét dependency tìm CVE | 15 |
| **GitHub Actions vs GitLab CI** | 2 nền tảng CI/CD khác cú pháp, cùng tư duy Pipeline → Job/Stage → Step | 15 |
| **EC2 / S3 / VPC** | Máy chủ ảo / lưu file dạng object / mạng riêng ảo trên AWS | 16 |
| **ALB/NLB + Auto Scaling Group** | Load balancer + tự thêm/bớt EC2 theo tải | 16 |
| **IAM / Least Privilege** | Quản lý quyền; chỉ cấp đúng quyền cần thiết, không cấp quyền thừa | 16 |
| **ECR/ECS/EKS** | Registry image / chạy container quản lý bởi AWS / Kubernetes managed của AWS | 16 |
| **AWS ↔ GCP** | EC2↔Compute Engine, S3↔Cloud Storage, EKS↔GKE, RDS↔Cloud SQL | 16 |
| **Control Plane vs Worker Node** | Control Plane là "bộ não" cluster (API Server/Scheduler/etcd); Worker Node chạy Pod thật | 17 |
| **Pod / Deployment / Service** | Đơn vị nhỏ nhất / khai báo trạng thái mong muốn / địa chỉ mạng ổn định trỏ tới nhóm Pod | 17 |
| **ConfigMap / Secret** | Inject cấu hình/secret vào Pod không hardcode trong image | 17 |
| **Ingress / HPA** | Layer-7 LB trong cluster / tự scale Pod theo CPU-Memory | 17 |
| **Helm / RBAC** | Package manager cho K8s / phân quyền truy cập cluster | 17 |
| **Service Mesh (Istio/Linkerd)** | Sidecar proxy xử lý giao tiếp giữa service (mTLS, retry) bên ngoài code app | 17 |
| **Terraform / HCL / State file** | IaC khai báo kết quả mong muốn; state file lưu trạng thái hạ tầng thực tế | 18 |
| **Remote State + Locking** | Lưu state trên S3 + khóa bằng DynamoDB, tránh 2 người `apply` cùng lúc | 18 |
| **Ansible / Idempotent** | Config management push-based; chạy lại N lần vẫn ra cùng 1 kết quả | 18 |
| **GitOps (ArgoCD/Flux)** | Git là nguồn chân lý duy nhất, agent trong cluster tự đồng bộ, không ai push trực tiếp | 18 |
| **Rolling / Blue-Green / Canary** | 3 chiến lược deploy: thay dần / đổi nguyên môi trường / tăng dần % traffic | 19 |
| **Postmortem / Blameless** | Tài liệu mổ xẻ sự cố tập trung cải thiện hệ thống, không đổ lỗi cá nhân | 19 |

### Phần V — Phỏng vấn & Sự nghiệp

| Thuật ngữ | Định nghĩa ngắn | Chương |
|---|---|---|
| **Back-of-envelope estimation** | Ước lượng nhanh tải hệ thống (user, request/giây, dữ liệu/ngày) trước khi thiết kế | 20 |
| **STAR** | Situation - Task - Action - Result — khung kể chuyện phỏng vấn có cấu trúc | 22 |
| **Behavioral interview** | Câu hỏi về thái độ/xử lý tình huống, khác hoàn toàn câu hỏi kỹ thuật | 23 |
