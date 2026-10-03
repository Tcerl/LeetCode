> **Mục đích:** Đây là cuốn sách tổng hợp **toàn bộ kiến thức cần ôn lại + cần mở rộng** để nâng cao trình độ **Middle Backend Developer (Python - Django & Flask) có kỹ năng DevOps**. Sách **tự đủ (self-contained)** — mỗi chương gồm 5 phần chuẩn hóa:
> 1. **Kiến thức cần học** (bullet point, chia theo 3 cấp độ 🟢/🟡/🔴).
> 2. **🔬 Giải thích chuyên sâu & Cơ chế bên dưới**: Mổ xẻ chi tiết từng kiến thức theo chuẩn 4 câu hỏi thực chiến:
>    - 🎯 **Dùng để làm gì?** (Mục đích & Giá trị kỹ thuật mang lại trong hệ thống)
>    - 💡 **Khi nào dùng?** (Kịch bản áp dụng thực tế & Khi nào KHÔNG nên dùng)
>    - 🏭 **Thực tế sử dụng ra sao?** (Mẫu code / Lệnh terminal sản xuất thực tế)
>    - ⚙️ **Hoạt động ra sao?** (Cơ chế hoạt động sâu bên dưới / Inner mechanics)
> 3. **🛠️ Hướng dẫn thực hành & Verification** (các bước thực hành từng bước, terminal commands, phương pháp test & kiểm chứng code).
> 4. **📚 Nội dung đầy đủ** (khối thu gọn, bấm để mở — nhúng toàn bộ nội dung gốc từ ~30 tài liệu liên quan trong repo, không cần mở file khác).
> 5. **Đọc chi tiết** (link gốc để tra cứu/cập nhật sau này nếu tài liệu nguồn thay đổi).
>
> Dùng cùng với [README.md](README.md) (cách dùng folder) và [00-Lich-Hoc-Toi/Lich_Trinh_Toi_Den_Tet.md](00-Lich-Hoc-Toi/Lich_Trinh_Toi_Den_Tet.md) (lịch học tối 21h-22h/22h30) — sách này là "bản đồ kiến thức + toàn bộ nội dung" gộp làm một, lịch học là "thời gian biểu đọc và thực hành".
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
- OOP (class, inheritance, composition) — chuẩn hóa lại theo Python thuần (dataclass, property, classmethod/staticmethod).
- Type hinting (`typing`) — ngành đang chuẩn hóa dùng type hint, nên tập thói quen viết từ đầu.

🟡 **Nâng cao (trọng tâm Middle):**
- Decorator, generator/iterator, context manager (`with`) — kỹ năng cốt lõi hay bị hỏi khi phỏng vấn Middle Backend.
- `asyncio` cơ bản (coroutine, event loop) — nền cho Chương 10.
- **Design Pattern cơ bản cho Backend**: Factory Pattern, Strategy Pattern, Dependency Injection (DI) — không cần học hết Gang of Four, chỉ cần 2-3 pattern hay gặp nhất khi đọc code Django/Flask/FastAPI thực tế.
- **Quản lý dependency & môi trường chuyên nghiệp**: `venv`/`poetry` (khóa version bằng lock file), code style tự động (`black`/`ruff`), type check tĩnh (`mypy`).

🔴 **Chuyên sâu / Thực chiến:**
- GIL, memory model, mutable vs immutable, shallow/deep copy — câu hỏi kinh điển phỏng vấn Middle/Senior Python, dễ trả lời sai nếu chỉ học khái niệm suông.
- **Clean Architecture / Hexagonal Architecture** — tư tư tưởng tách business logic ra khỏi framework để dễ test và dễ đổi công nghệ sau này; đây là ranh giới rõ nhất giữa code Middle và code Junior.

**Giải thích chi tiết chuyên sâu:**

#### 1. Decorators & Context Managers (`with`)
* 🎯 **Dùng để làm gì?** 
  * Decorator dùng để can thiệp / mở rộng hành vi của một hàm mà không cần sửa mã nguồn của hàm đó (DRY - Don't Repeat Yourself).
  * Context Manager dùng để quản lý vòng đời tài nguyên (File, DB Connection, Lock), đảm bảo tự động dọn dẹp (cleanup) dù có exception xảy ra.
* ⏰ **Khi nào sử dụng?**
  * **Decorator:** Dùng khi muốn tái sử dụng logic cắt ngang (Cross-cutting Concerns) như `@login_required`, `@permission_check`, `@rate_limit`, `@cache_result`, `@log_execution_time`.
  * **Context Manager:** Dùng khi thao tác với File I/O, mở kết nối Database Transaction, Acquire/Release Lock trong Concurrency.
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  ```python
  import time
  from functools import wraps

  # Decorator đo thời gian thực thi API/Function trong Production
  def measure_performance(func):
      @wraps(func)  # Giữ lại metadata (__name__, __doc__) của hàm gốc
      def wrapper(*args, **kwargs):
          start_time = time.perf_counter()
          result = func(*args, **kwargs)
          execution_time = time.perf_counter() - start_time
          print(f"[METRIC] {func.__name__} executed in {execution_time:.4f}s")
          return result
      return wrapper

  @measure_performance
  def process_payment(amount: float):
      time.sleep(0.1) # Giả lập xử lý DB
      return True

  # Context Manager tự động đóng DB Connection
  class DatabaseTransaction:
      def __enter__(self):
          print("BEGIN TRANSACTION")
          return self
      def __exit__(self, exc_type, exc_val, exc_tb):
          if exc_type:
              print(f"ROLLBACK due to {exc_val}")
          else:
              print("COMMIT TRANSACTION")
          return False  # Không swallow exception
  ```
* ⚙️ **Cơ chế hoạt động ra sao?**
  * **Decorator:** Khi Python dịch code, `@measure_performance` trên `def process_payment` tương đương với câu lệnh: `process_payment = measure_performance(process_payment)`. Hàm `process_payment` bị ghi đè bởi hàm `wrapper`, tạo thành một closure lưu trữ tham chiếu tới hàm gốc.
  * **Context Manager:** Lệnh `with DatabaseTransaction() as tx:` thực chất gọi method `__enter__()` trước khi vào block code, và luôn luôn tự động gọi `__exit__()` trong khối `finally` ngầm định khi thoát ra (dù code trong block throw error hay return).

---

#### 2. Generators & Iterators (`yield`)
* 🎯 **Dùng để làm gì?** Giúp xử lý các tập dữ liệu khổng lồ (Stream Data / Large Datasets) với dung lượng RAM tiệm cận 0 (O(1) Memory Complexity), tránh crash OOM (Out of Memory).
* ⏰ **Khi nào sử dụng?** Dùng khi đọc log file hàng triệu dòng, export file CSV/Excel lớn từ DB, hoặc đọc data theo chunk từ S3/Stream API. KHÔNG dùng khi cần truy cập ngẫu nhiên theo index (`gen[5]`) hoặc cần duyệt danh sách nhiều lần.
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  ```python
  def read_large_log_file(file_path: str):
      with open(file_path, "r") as file:
          for line in file:
              if "ERROR" in line:
                  yield line.strip()  # Trả từng dòng lỗi, không nạp cả file 2GB vào RAM

  # Sử dụng trong Service
  for error_log in read_large_log_file("/var/log/nginx/access.log"):
      send_alert_to_slack(error_log)
  ```
* ⚙️ **Cơ chế hoạt động ra sao?** Khi hàm chứa từ khóa `yield`, Python biến hàm đó thành một **Generator Function**. Gọi hàm này không chạy code ngay mà trả về một **Generator Object** tuân theo Iterator Protocol (`__iter__` và `__next__`). Mỗi khi hàm `next()` được gọi, code chạy tới lệnh `yield`, đóng đống (freeze) toàn bộ stack frame (biến cục bộ, con trỏ lệnh) và trả về giá trị. Lần `next()` tiếp theo sẽ khôi phục stack frame và chạy tiếp từ dòng sau `yield`.

---

#### 3. GIL (Global Interpreter Lock) & Python Memory Model
* 🎯 **Dùng để làm gì?** 
  * GIL là cơ chế khóa của CPython đảm bảo chỉ một Native Thread thực thi Python Bytecode tại một thời điểm để bảo vệ thread-safety cho bộ nhớ (Reference Counting).
* ⏰ **Khi nào sử dụng / Ảnh hưởng ra sao?**
  * Ảnh hưởng trực tiếp đến việc lựa chọn kiến trúc Concurrency:
    * Với tác vụ **I/O-bound** (Chờ DB, Chờ Network REST API): Dùng **Multi-threading** hoặc **Asyncio** (GIL được release khi chờ I/O).
    * Với tác vụ **CPU-bound** (Xử lý ảnh, mã hóa, nén dữ liệu): Phải dùng **Multi-processing** (mỗi process có CPython instance & GIL riêng) để tận dụng Multi-core CPU.
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  ```python
  # Bug kinh điển: Dùng Mutable Default Argument
  def append_to_cart(item: str, cart: list = []) -> list:  # cart=[] tạo 1 LẦN DUY NHẤT lúc load module
      cart.append(item)
      return cart

  print(append_to_cart("Apple"))   # ['Apple']
  print(append_to_cart("Banana"))  # ['Apple', 'Banana'] -> Bug: Dữ liệu user trước rò sang user sau!

  # Cách viết chuẩn Production:
  def append_to_cart_correct(item: str, cart: list | None = None) -> list:
      if cart is None:
          cart = []
      cart.append(item)
      return cart
  ```
* ⚙️ **Cơ chế hoạt động ra sao?**
  * **GIL Mechanics:** CPython sử dụng Reference Counting cho Garbage Collection. Nếu không có GIL, 2 thread cùng tăng/giảm `sys.getrefcount(obj)` sẽ bị race condition dẫn đến rò rỉ bộ nhớ hoặc deallocate nhầm object đang dùng.
  * **Mutable Default Argument:** Khi Python parse định nghĩa hàm `def`, nó evaluate tham số mặc định `cart=[]` **ngay lúc load file lần đầu** và lưu trong thuộc tính `append_to_cart.__defaults__`. Mọi lần gọi hàm tiếp theo nếu không truyền `cart` đều dùng chung reference tới cùng 1 list trong bộ nhớ Heap.

---

#### 4. Design Patterns: Dependency Injection (DI) & Factory Pattern
* 🎯 **Dùng để làm gì?** Tách rời (Decouple) sự phụ thuộc giữa các class, giúp hệ thống dễ mở rộng, dễ bảo trì và dễ viết Unit Test (Mocking).
* ⏰ **Khi nào sử dụng?** Dùng khi xây dựng Service Layer trong Django/Flask/FastAPI, khi ứng dụng cần giao tiếp với các dịch vụ bên ngoài (Payment Gateway, Email Service, Cloud Storage) mà có thể thay đổi provider trong tương lai.
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  ```python
  from abc import ABC, abstractmethod

  # Abstract Interface
  class PaymentGateway(ABC):
      @abstractmethod
      def pay(self, amount: float) -> bool: pass

  class StripePayment(PaymentGateway):
      def pay(self, amount: float) -> bool:
          print(f"Paid ${amount} via Stripe")
          return True

  class PaypalPayment(PaymentGateway):
      def pay(self, amount: float) -> bool:
          print(f"Paid ${amount} via Paypal")
          return True

  # Dependency Injection Service
  class OrderService:
      def __init__(self, payment_gateway: PaymentGateway):  # Inject dependency từ bên ngoài
          self.payment_gateway = payment_gateway

      def checkout(self, amount: float):
          return self.payment_gateway.pay(amount)

  # Trong Production code: order_service = OrderService(StripePayment())
  # Trong Unit Test code:   order_service = OrderService(MockPayment())
  ```
* ⚙️ **Cơ chế hoạt động ra sao?** Thay vì `OrderService` tự mình khởi tạo `self.payment_gateway = StripePayment()` bên trong `__init__` (gắn chặt cứng vào Stripe), dependency được "tiêm" (inject) vào qua constructor. Lớp `OrderService` chỉ phụ thuộc vào `PaymentGateway` Abstraction (Inversion of Control - IoC Principle thuộc SOLID), không phụ thuộc vào Concrete Class.

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

**Giải thích chi tiết chuyên sâu:**

#### 1. `rebase` vs `merge` & Git Workflow (Git Flow vs Trunk-Based)
* 🎯 **Dùng để làm gì?** Hợp nhất công việc của nhiều dev vào nhánh chính. `merge` giữ nguyên lịch sử thật; `rebase` viết lại lịch sử thành 1 đường thẳng dễ đọc. Workflow quy định cách cả team tổ chức nhánh.
* 💡 **Khi nào dùng?**
  - `rebase`: cập nhật nhánh feature **của riêng bạn** theo `main` mới nhất trước khi mở PR. **KHÔNG** rebase nhánh đã push chung với người khác (đổi commit hash → đồng đội bị xung đột lịch sử).
  - `merge`: gộp PR vào `main` khi muốn giữ nguyên dấu vết thật.
  - **Trunk-Based** (commit nhỏ, PR ngắn ngày + feature flag): phù hợp CI/CD liên tục. **Git Flow** (develop/release/hotfix): phù hợp sản phẩm có chu kỳ release cố định (mobile app, phần mềm đóng gói).
* 🏭 **Thực tế sử dụng ra sao?**
  ```bash
  git switch feature/payment
  git fetch origin
  git rebase origin/main          # đặt commit của bạn lên đầu main mới nhất
  # có conflict -> sửa file -> git add . -> git rebase --continue
  git push --force-with-lease     # chỉ force push nhánh CỦA BẠN, an toàn hơn --force
  ```
* ⚙️ **Hoạt động ra sao?** `merge` tạo 1 *merge commit* có 2 cha. `rebase` lấy từng commit của nhánh bạn, **tạo commit mới** (hash mới) áp lần lượt lên đỉnh `main` — nên lịch sử thẳng, nhưng commit cũ bị thay thế. Đó là lý do không được rebase nhánh dùng chung.

#### 2. Pre-commit Hook & Conventional Commits
* 🎯 **Dùng để làm gì?** Chặn code sai chuẩn (lint, format, secret lộ) **trước khi** vào lịch sử Git; Conventional Commits chuẩn hóa message để tự sinh changelog/version.
* 💡 **Khi nào dùng?** Mọi dự án làm nhóm. Không nhét test nặng (chạy >30 giây) vào pre-commit vì dev sẽ `--no-verify` bỏ qua — test nặng để CI chạy.
* 🏭 **Thực tế sử dụng ra sao?**
  ```yaml
  # .pre-commit-config.yaml
  repos:
    - repo: https://github.com/astral-sh/ruff-pre-commit
      rev: v0.4.4
      hooks: [{ id: ruff }, { id: ruff-format }]
  ```
  ```bash
  pip install pre-commit && pre-commit install   # từ giờ mỗi lần git commit sẽ tự chạy hook
  git commit -m "feat(order): thêm API hủy đơn"  # Conventional Commit
  ```
* ⚙️ **Hoạt động ra sao?** `pre-commit install` ghi script vào `.git/hooks/pre-commit`. Khi `git commit`, Git chạy script đó trước; nếu exit code ≠ 0, commit bị hủy. Message dạng `feat:`/`fix:` được công cụ (semantic-release) đọc để quyết định tăng minor/patch version.

#### 3. Quy trình PR: Squash vs Preserve History
* 🎯 **Dùng để làm gì?** Quyết định lịch sử `main` trông thế nào sau khi merge PR — gọn gàng 1 commit/tính năng hay chi tiết từng bước.
* 💡 **Khi nào dùng?** **Squash**: PR có nhiều commit nháp ("fix typo", "wip") → gộp thành 1 commit sạch, dễ `revert` cả tính năng. **Merge commit/Rebase-merge**: mỗi commit có ý nghĩa riêng cần tra cứu (refactor lớn chia nhiều bước).
* 🏭 **Thực tế sử dụng ra sao?** Trên GitHub: nút *Squash and merge* trong PR. Checklist review: có test chưa? có migration không? có ảnh hưởng backward-compat không? có log/metric chưa?
* ⚙️ **Hoạt động ra sao?** Squash tạo 1 commit mới trên `main` chứa tổng diff của PR, rồi bỏ các commit nháp. Hệ quả: `git revert <hash>` hoàn tác trọn vẹn tính năng chỉ bằng 1 lệnh.

#### 4. Công cụ "cứu hỏa": `bisect`, `cherry-pick`, `reflog`
* 🎯 **Dùng để làm gì?** `bisect`: tìm commit gây lỗi. `cherry-pick`: lấy đúng 1 commit sang nhánh khác. `reflog`: cứu commit tưởng đã mất.
* 💡 **Khi nào dùng?** `bisect` khi biết "bản cũ chạy đúng, bản mới lỗi" nhưng không biết commit nào. `cherry-pick` khi cần đưa hotfix từ `main` sang nhánh `release`. `reflog` ngay sau khi lỡ `reset --hard`/xóa nhầm nhánh.
* 🏭 **Thực tế sử dụng ra sao?**
  ```bash
  git bisect start && git bisect bad HEAD && git bisect good v1.2.0
  git bisect run pytest tests/test_order.py   # tự động tìm commit lỗi, không cần tự test tay
  git bisect reset

  git cherry-pick a1b2c3d                      # áp 1 hotfix sang nhánh hiện tại
  git reflog && git reset --hard a1b2c3d       # cứu lại commit vừa mất
  ```
* ⚙️ **Hoạt động ra sao?** `bisect` là **binary search** trên lịch sử: 1000 commit chỉ cần ~10 bước. `reflog` là nhật ký cục bộ mọi vị trí HEAD đã trỏ tới; commit "mất" thực ra vẫn nằm trong Git tới khi bị garbage-collect (mặc định ~30-90 ngày).

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
- Viết query SQL cơ bản, hiểu bảng/quan hệ (DML, DDL, Foreign Keys).
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

**Giải thích chi tiết chuyên sâu:**

#### 1. Index (B-Tree, Composite) & `EXPLAIN ANALYZE`
* 🎯 **Dùng để làm gì?** Tăng tốc truy vấn đọc từ quét toàn bảng O(n) xuống tìm kiếm ~O(log n); `EXPLAIN ANALYZE` cho biết query thực sự chạy thế nào để biết cần index ở đâu.
* 💡 **Khi nào dùng?** Index cột xuất hiện trong `WHERE`, `JOIN`, `ORDER BY` của query chạy thường xuyên trên bảng lớn. **Không** index bừa: mỗi index làm chậm `INSERT/UPDATE/DELETE` và tốn dung lượng; bảng nhỏ (<vài nghìn dòng) hoặc cột có ít giá trị phân biệt (vd `is_active`) thường không đáng.
* 🏭 **Thực tế sử dụng ra sao?**
  ```sql
  EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123 AND status = 'pending';
  -- Seq Scan  -> quét cả bảng (xấu nếu bảng lớn)
  CREATE INDEX idx_orders_user_status ON orders (user_id, status);
  -- chạy lại EXPLAIN ANALYZE -> Index Scan, thời gian giảm từ giây xuống mili-giây
  ```
  Ở production dùng `CREATE INDEX CONCURRENTLY` để không khóa bảng khi đang có traffic.
* ⚙️ **Hoạt động ra sao?** B-Tree là cây cân bằng đã sắp xếp theo giá trị cột; DB đi từ gốc xuống lá để tìm đúng vị trí thay vì đọc hết. Composite index `(a, b)` sắp xếp theo `a` rồi `b`, nên chỉ dùng được khi lọc theo `a` (hoặc `a` + `b`) — lọc riêng `b` thì không tận dụng được (quy tắc *leftmost prefix*).

#### 2. Transaction, ACID & Isolation Level
* 🎯 **Dùng để làm gì?** Gom nhiều câu lệnh thành 1 khối "tất cả hoặc không gì cả", đảm bảo dữ liệu luôn nhất quán dù lỗi giữa chừng hoặc nhiều người cùng ghi.
* 💡 **Khi nào dùng?** Bất kỳ thao tác nhiều bước ảnh hưởng tiền/kho/trạng thái (chuyển tiền, đặt hàng + trừ kho). Chọn isolation: `Read Committed` (mặc định, đủ cho đa số), `Repeatable Read` khi báo cáo cần đọc nhất quán, `Serializable` khi sai sót không chấp nhận được (chấp nhận retry khi conflict).
* 🏭 **Thực tế sử dụng ra sao?**
  ```python
  from django.db import transaction
  with transaction.atomic():
      order = Order.objects.create(user=user, total=total)
      Product.objects.select_for_update().filter(id=pid).update(stock=F('stock') - 1)
  # exception bất kỳ trong khối -> ROLLBACK toàn bộ
  ```
* ⚙️ **Hoạt động ra sao?** Postgres dùng **MVCC**: mỗi transaction thấy 1 "ảnh chụp" dữ liệu theo isolation level, ghi tạo phiên bản dòng mới thay vì ghi đè ngay. Khi 2 transaction khóa chéo nhau → **deadlock**, DB tự hủy 1 bên; app cần bắt lỗi và retry.

#### 3. Connection Pooling & PgBouncer
* 🎯 **Dùng để làm gì?** Tái sử dụng connection DB đã mở thay vì mở/đóng mỗi request (mỗi connection tốn ~5MB RAM + ~100ms thiết lập).
* 💡 **Khi nào dùng?** Luôn dùng ở production. Thêm **PgBouncer** khi nhiều instance/Pod app cộng lại có nguy cơ vượt `max_connections` của Postgres.
* 🏭 **Thực tế sử dụng ra sao?** Công thức an toàn: `số instance × pool_size ≤ max_connections − buffer cho admin/migration`. Ví dụ 10 Pod × pool 20 = 200 > 100 mặc định → lỗi `too many connections` sập toàn hệ thống dù CPU DB còn rảnh. Cấu hình `pool_size`, `max_overflow`, `pool_timeout` (fail-fast), `pool_pre_ping=True` (xem code ở phần diễn giải bên dưới).
* ⚙️ **Hoạt động ra sao?** Pool giữ sẵn N connection "nóng"; request mượn → dùng → trả lại. PgBouncer đứng giữa app và Postgres, gom hàng nghìn connection phía app thành vài chục connection thật phía DB (transaction pooling).

#### 4. Replication, Sharding & Zero-downtime Migration
* 🎯 **Dùng để làm gì?** Replication: san tải đọc + chịu lỗi. Sharding: chia dữ liệu ra nhiều DB khi 1 máy không chứa/ghi nổi. Zero-downtime migration: đổi schema bảng lớn mà không ngắt dịch vụ.
* 💡 **Khi nào dùng?** Theo thứ tự: tối ưu index/query → cache → read replica → **cuối cùng mới** sharding (JOIN xuyên shard gần như bất khả thi, vận hành rất phức tạp). Migration an toàn dùng cho mọi thay đổi schema trên bảng đang có traffic.
* 🏭 **Thực tế sử dụng ra sao?** Thêm cột `NOT NULL` trên bảng triệu dòng: (1) thêm cột nullable → (2) backfill theo batch bằng job riêng → (3) thêm ràng buộc `NOT NULL`. `DROP/RENAME COLUMN`: deploy app đọc được cả 2 dạng trước, xóa cột cũ ở lần deploy sau.
* ⚙️ **Hoạt động ra sao?** Replica nhận WAL (nhật ký ghi) từ primary và replay → có **độ trễ replication**, nên đọc ngay sau khi ghi có thể thấy dữ liệu cũ (cần đọc từ primary với luồng nhạy cảm). `ALTER TABLE` kiểu cũ giữ khóa độc quyền lên bảng → mọi query chờ → downtime; chia nhỏ bước giúp mỗi bước chỉ giữ khóa rất ngắn.

<details>
<summary>📖 Diễn giải bổ sung chi tiết (Backup, NoSQL/MongoDB, Normalization, SQL vs NoSQL, Polyglot...)</summary>

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

</details>

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Big-O & chọn cấu trúc dữ liệu: `list` vs `set` vs `dict`
* 🎯 **Dùng để làm gì?** Ước lượng code sẽ chậm đi thế nào khi dữ liệu tăng, từ đó chọn đúng cấu trúc dữ liệu ngay từ đầu thay vì "chạy được là xong".
* 💡 **Khi nào dùng?** `set`/`dict` khi cần kiểm tra tồn tại/tra cứu theo khóa trong vòng lặp lớn (O(1)); `list` khi cần giữ thứ tự/cho phép trùng lặp và dữ liệu nhỏ. Không cần tối ưu khi dữ liệu chỉ vài chục phần tử — đọc dễ hiểu quan trọng hơn.
* 🏭 **Thực tế sử dụng ra sao?** Lọc 100.000 bản ghi theo danh sách `blocked_ids` 10.000 phần tử: dùng `list` → ~10⁹ phép so sánh (vài chục giây); đổi sang `set` → ~10⁵ phép tra (mili-giây). (Code minh họa ngay bên dưới.)
* ⚙️ **Hoạt động ra sao?** `set`/`dict` là **hash table**: tính `hash(x)` → nhảy thẳng tới ô nhớ tương ứng, không duyệt. `list` phải so sánh từng phần tử từ đầu. Đánh đổi của hash table: tốn thêm RAM, không giữ thứ tự đảm bảo như list.

#### 2. LRU Cache (`functools.lru_cache`)
* 🎯 **Dùng để làm gì?** Nhớ kết quả của hàm theo tham số để lần gọi sau trả ngay, không tính/gọi API lại; khi đầy thì loại phần tử **lâu không dùng nhất**.
* 💡 **Khi nào dùng?** Hàm thuần (cùng input → cùng output), tốn kém, được gọi lặp lại với cùng tham số (tỷ giá, cấu hình, kết quả tra cứu ít đổi). **Không** dùng cho dữ liệu hay đổi (số dư tài khoản) hoặc khi chạy nhiều server — mỗi process có cache riêng, luôn lệch nhau (khi đó dùng Redis, Chương 11).
* 🏭 **Thực tế sử dụng ra sao?** `@lru_cache(maxsize=128)` quanh hàm gọi API tỷ giá; `get_exchange_rate.cache_info()` xem hit/miss; `.cache_clear()` khi cần làm mới.
* ⚙️ **Hoạt động ra sao?** Bên trong là dict (key = tham số) + danh sách liên kết hai chiều để đưa phần tử vừa dùng lên đầu và bỏ phần cuối khi đầy → mọi thao tác O(1). Tham số phải *hashable*.

#### 3. Union-Find & Graph (BFS/DFS)
* 🎯 **Dùng để làm gì?** Union-Find trả lời nhanh "2 phần tử có cùng nhóm không" và gộp nhóm; BFS/DFS duyệt quan hệ dạng mạng lưới.
* 💡 **Khi nào dùng?** Phát hiện tài khoản liên quan/gian lận, nhóm bạn bè, phụ thuộc giữa module/task (BFS/DFS), tìm đường ngắn nhất (BFS). Hiếm dùng trong CRUD thuần; chủ yếu gặp ở phỏng vấn và bài toán quan hệ.
* 🏭 **Thực tế sử dụng ra sao?** Gộp các tài khoản dùng chung thiết bị/IP vào 1 nhóm để đánh dấu rủi ro; sắp xếp thứ tự chạy migration/task theo đồ thị phụ thuộc.
* ⚙️ **Hoạt động ra sao?** Union-Find giữ cây cha cho mỗi phần tử; `find` tìm gốc (có *path compression*), `union` nối hai gốc → gần O(1) trung bình. BFS dùng hàng đợi (duyệt theo lớp), DFS dùng ngăn xếp/đệ quy (đi sâu trước).

<details>
<summary>📖 Diễn giải bổ sung & code minh họa</summary>

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

</details>

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
- ORM, migration, quan hệ ForeignKey/ManyToMany — so sánh với SQLAlchemy (Flask).
- Admin interface — Django Admin (sinh tự động) vs Flask (tự dựng hoặc dùng Flask-Admin).

🟡 **Nâng cao (trọng tâm Middle):**
- **Middleware** — nơi xử lý request/response xuyên suốt toàn app (auth, logging, CORS).
- Class-Based View vs Function-Based View — khi nào nên dùng loại nào.

🔴 **Chuyên sâu / Thực chiến:**
- **Signal** (post_save, pre_delete...) — cơ chế Event-driven decoupling của Django; dễ lạm dụng khiến luồng xử lý bị "ẩn", khó debug.
- **N+1 query problem** + cách fix bằng `select_related`/`prefetch_related` — câu hỏi phỏng vấn Middle gần như chắc chắn gặp.

**Giải thích chi tiết chuyên sâu:**

#### 1. Xử lý Lỗi N+1 Query (`select_related` vs `prefetch_related`)
* 🎯 **Dùng để làm gì?** Tối ưu số lượng truy vấn SQL gửi tới Database, giải quyết hiện tượng suy giảm hiệu năng nghiêm trọng (rút cạn DB connection pool) khi lấy danh sách dữ liệu có quan hệ.
* ⏰ **Khi nào sử dụng?** 
  * Dùng `select_related`: Cho quan hệ **Single-valued** (ForeignKey, OneToOne).
  * Dùng `prefetch_related`: Cho quan hệ **Multi-valued** (ManyToMany, Reverse ForeignKey).
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  ```python
  # ❌ BAD (N+1 Query): 1 query lấy 100 posts + 100 query lấy author cho từng post
  posts = Post.objects.all()
  for post in posts:
      print(post.author.name)  # Truy cập .author gây ra 1 query mới mỗi vòng lặp!

  # ✅ GOOD (Tối ưu bằng SQL JOIN): Chỉ đúng 1 query duy nhất
  posts = Post.objects.select_related('author').all()
  for post in posts:
      print(post.author.name)  # Author đã được JOIN nạp sẵn vào memory!

  # ✅ GOOD (Tối ưu cho Many-to-Many): Đúng 2 queries, join bằng Python Memory
  posts = Post.objects.prefetch_related('tags').all()
  ```
* ⚙️ **Cơ chế hoạt động ra sao?**
  * `select_related`: Django ORM tự động sinh ra câu lệnh SQL `INNER JOIN` hoặc `LEFT OUTER JOIN` để gộp bảng `blog_post` và `blog_author` lại trong **đúng 1 query**.
  * `prefetch_related`: Django chạy **2 query độc lập**: Query 1 lấy danh sách Post IDs, Query 2 lấy Tags có `post_id IN (1, 2, 3...)`. Sau đó Django ORM ghép 2 tập kết quả lại với nhau trong bộ nhớ Python RAM.

---

#### 2. Django Middleware Pipeline
* 🎯 **Dùng để làm gì?** Đóng vai trò là chuỗi bộ lọc cắm vào HTTP Request/Response Lifecycle để thực thi các tác vụ dùng chung toàn hệ thống (Authentication, Logging, CORS, Security Headers, Rate Limiting).
* ⏰ **Khi nào sử dụng?** Dùng khi cần can thiệp trước khi request tới được View hoặc sau khi View đã trả về Response (VD: Bắt exception toàn cục, đính kèm Header security, verify JWT Token).
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  ```python
  import time
  import logging

  logger = logging.getLogger(__name__)

  class RequestTimingMiddleware:
      def __init__(self, get_response):
          self.get_response = get_response  # Callable response handler tiếp theo

      def __call__(self, request):
          # 1. Code chạy TRƯỚC KHI View xử lý (Request Phase)
          start_time = time.time()

          response = self.get_response(request)  # Chuyển request cho view/middleware tiếp theo

          # 2. Code chạy SẠU KHI View đã trả về (Response Phase)
          duration = time.time() - start_time
          response['X-Process-Time'] = f"{duration:.3f}s"
          if duration > 1.0:
              logger.warning(f"SLOW REQUEST: {request.path} took {duration:.2f}s")

          return response
  ```
* ⚙️ **Cơ chế hoạt động ra sao?** Middleware được tổ chức dưới dạng cấu trúc vỏ hành (Onion Architecture). Khi WSGI Server nhận request, request sẽ chạy lồng qua lần lượt từng middleware trong `MIDDLEWARE` setting từ trên xuống dưới. Response trả về sẽ chạy ngược lại từ dưới lên trên qua các middleware đó.

---

#### 3. Django Signals (`post_save`, `pre_delete`)
* 🎯 **Dùng để làm gì?** Tạo cơ chế Event-driven Publisher/Subscriber nội bộ ứng dụng, giúp gỡ bỏ sự phụ thuộc trực tiếp (Decoupling) giữa các module.
* ⏰ **Khi nào sử dụng?** Dùng khi một hành động ở Model A cần kích hoạt tự động các xử lý phụ ở Module B (VD: Tạo `User` xong tự động tạo `UserProfile`, hoặc tự xóa file trên S3 khi `ImageModel` bị delete). KHÔNG dùng cho core business logic phức tạp vì dễ làm ẩn luồng chạy (Implicit flow).
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  ```python
  from django.db.models.signals import post_save
  from django.dispatch import receiver
  from django.contrib.auth.models import User
  from .models import UserProfile

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:  # Chỉ chạy khi bản ghi mới được INSERT
          UserProfile.objects.create(user=instance)
  ```
* ⚙️ **Cơ chế hoạt động ra sao?** Khi method `instance.save()` của Model kết thúc thành công, Django Dispatcher sẽ duyệt qua danh sách các hàm được đăng ký decorator `@receiver` đối với sender `User` và thực thi lần lượt các callback function đó **đồng bộ (synchronously)** trong cùng thread/transaction ngoại trừ khi được đẩy sang Celery async task.

### 🛠️ Hướng dẫn thực hành từng bước (Bài tập DJ-01 → DJ-04):

#### 1. Thực hành DJ-01 — Khởi tạo App & Chạy Migration:
```bash
python -m venv venv && source venv/bin/activate
pip install django
django-admin startproject myproject .
python manage.py startapp blog
```
- **Code `blog/models.py`:**
  ```python
  from django.db import models

  class Author(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField(unique=True)

  class Post(models.Model):
      title = models.CharField(max_length=200)
      content = models.TextField()
      author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
  ```
- **Chạy Migration & Verify:** `python manage.py makemigrations blog` -> `python manage.py sqlmigrate blog 0001` (xem SQL JOIN/INDEX) -> `python manage.py migrate`.

#### 2. Thực hành DJ-02 — FBV vs CBV:
- **Tạo FBV & CBV (`blog/views.py`):**
  ```python
  # FBV
  def post_list_fbv(request):
      return render(request, 'blog/post_list.html', {'posts': Post.objects.all()})

  # CBV (Generic)
  from django.views.generic import ListView
  class PostListView(ListView):
      model = Post
      template_name = 'blog/post_list.html'
  ```

#### 3. Thực hành DJ-03 — Bật Debug Toolbar & Fix N+1 Query:
- **Tạo lỗi N+1:** Render `{% for p in posts %}{{ p.author.name }}{% endfor %}` không dùng `select_related`. Đếm SQL Queries hiển thị **N+1 queries** trên Debug Toolbar.
- **Fix lỗi:** `posts = Post.objects.select_related('author').all()[:20]` -> Verify trên Debug Toolbar chỉ còn **1 SQL query JOIN duy nhất**!

#### 4. Thực hành DJ-04 — Bảng tổng hợp so sánh Django vs Flask:
- Ghi chép note so sánh: Architecture (Batteries-included vs Micro-framework), ORM (Django ORM Active Record vs Flask-SQLAlchemy Data Mapper), Routing (Django URLs/CBV vs Flask Route Decorators/Blueprints).

**Đọc chi tiết:** [`03-Python-Expert/Django_Mastery_Guide.md`](../03-Python-Expert/Django_Mastery_Guide.md). Đọc code thật: [`09-Example-Projects/Django_RealWorld`](../09-Example-Projects/Django_RealWorld), [`09-Example-Projects/Django_Rest_Pro`](../09-Example-Projects/Django_Rest_Pro). Dẫn chiếu thực hành: [`01-Django-Exercises/Checklist_Bai_Tap.md`](01-Django-Exercises/Checklist_Bai_Tap.md).

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

**Giải thích chi tiết chuyên sâu:**

#### 1. DRF Serializer & Validation Engine
* 🎯 **Dùng để làm gì?** Chuyển đổi dữ liệu hai chiều (Two-way Data Transformation): Serialize Python Model Instance thành JSON payload cho Frontend và Deserialize/Validate JSON payload đầu vào thành Python Object hợp lệ.
* 💡 **Khi nào dùng?** Dùng bắt buộc trong mọi DRF API Endpoint để đảm bảo contract dữ liệu giữa Client-Server và bảo vệ Database khỏi bẩn dữ liệu. KHÔNG dùng khi xây dựng Server-side Rendering HTML (dùng Django Form).
* 🏭 **Thực tế sử dụng ra sao?**
  ```python
  from rest_framework import serializers
  from .models import Order

  class OrderSerializer(serializers.ModelSerializer):
      class Meta:
          model = Order
          fields = ["id", "customer", "total", "created_at"]

      def validate_total(self, value):
          if value <= 0:
              raise serializers.ValidationError("total phải lớn hơn 0")
          return value
  ```
* ⚙️ **Hoạt động ra sao?** Khi gọi `serializer.is_valid()`, DRF chạy qua 3 tầng validation: Field-level validation -> Object-level `validate()` -> Model clean execution. Nếu thất bại, ném `ValidationError` chứa dict thông báo chi tiết cấu trúc JSON lỗi (400 Bad Request).

#### 2. ViewSet & Router Automation
* 🎯 **Dùng để làm gì?** Gom toàn bộ logic CRUD (List, Create, Retrieve, Update, Destroy) của 1 Resource vào một Class duy nhất và tự động hóa sinh chuẩn RESTful URL Routes.
* 💡 **Khi nào dùng?** Khi xây dựng các chuẩn REST resource tuân thủ mô hình CRUD tiêu chuẩn. KHÔNG dùng khi endpoint mang tính chất RPC hoặc thao tác xử lý đặc thù không thuộc 5 hành vi CRUD chuẩn (nên dùng `APIView` hoặc `@action`).
* 🏭 **Thực tế sử dụng ra sao?**
  ```python
  from rest_framework import viewsets
  from rest_framework.routers import DefaultRouter
  from rest_framework.permissions import IsAuthenticated

  class OrderViewSet(viewsets.ModelViewSet):
      queryset = Order.objects.select_related("customer").all()  # Tối ưu N+1
      serializer_class = OrderSerializer
      permission_classes = [IsAuthenticated]

  router = DefaultRouter()
  router.register("orders", OrderViewSet, basename="order")
  # Tự động map: GET/POST /orders/, GET/PUT/PATCH/DELETE /orders/{id}/
  ```
* ⚙️ **Hoạt động ra sao?** Router đứng ở tầng `urls.py`, sử dụng Regex/Path converters bóc tách HTTP Verb và URL Path để map chính xác vào các handler method tương ứng (`list`, `create`, `retrieve`, `update`, `destroy`) trong ViewSet instance.

#### 3. JWT Authentication (Access & Refresh Tokens)
* 🎯 **Dùng để làm gì?** Xác thực Stateless (không lưu session trên RAM/DB server), giúp API scale dễ dàng qua hàng chục server đằng sau Load Balancer.
* 💡 **Khi nào dùng?** Khi làm hệ thống Microservices, Single Page Application (React/Vue), Mobile App. KHÔNG nên dùng nếu cần thu hồi quyền tức thì trong milliseconds ngoại trừ có Blacklist Redis hỗ trợ.
* 🏭 **Thực tế sử dụng ra sao?** Header đính kèm: `Authorization: Bearer <access_token>`. Khi Access token hết hạn (15 phút), Client gửi Refresh Token đến `/api/token/refresh/` để lấy Access Token mới mà không bắt user login lại.
* ⚙️ **Hoạt động ra sao?** JWT gồm 3 phần `Header.Payload.Signature`. Server verify token bằng cách băm lại `Header.Payload` với `SECRET_KEY`. Nếu khớp chữ ký và `exp` chưa quá hạn, Request được cấp quyền đi tiếp mà Server KHÔNG cần query Database tìm User Session.

#### 4. Rate Limiting & Throttling
* 🎯 **Dùng để làm gì?** Bảo vệ API Server khỏi tấn công DoS, Brute-force Login và lạm dụng tài nguyên mạng bằng cách giới hạn số lượng HTTP request trong khoảng thời gian.
* 💡 **Khi nào dùng?** Bắt buộc cho Public APIs, Login Endpoint, Payment Gateway integrations.
* 🏭 **Thực tế sử dụng ra sao?**
  ```python
  from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

  class LoginViewSet(viewsets.GenericViewSet):
      throttle_classes = [AnonRateThrottle] # Cấu hình anon: 5/min trong settings.py
  ```
* ⚙️ **Hoạt động ra sao?** DRF Throttling dùng thuật toán Leaky Bucket / Sliding Window lưu trên Cache backend (Redis/Memcached). Đếm số lượt truy cập gắn với IP Client hoặc User ID trong cửa sổ thời gian. Nếu vượt ngưỡng, ném ngay `HTTP 429 Too Many Requests`.

### 🛠️ Hướng dẫn thực hành từng bước (Bài tập DJ-05 & DJ-06):

#### 1. Thực hành DJ-05 — DRF ViewSet & Router:
- **Khai báo Serializer & ViewSet (`blog/serializers.py` & `blog/views.py`):**
  ```python
  from rest_framework import serializers, viewsets
  from rest_framework.routers import DefaultRouter
  from .models import Post

  class PostSerializer(serializers.ModelSerializer):
      class Meta:
          model = Post
          fields = ['id', 'title', 'content', 'author', 'published_at']

  class PostViewSet(viewsets.ModelViewSet):
      queryset = Post.objects.select_related('author').all()
      serializer_class = PostSerializer
  ```
- **Cấu hình Router (`blog/urls.py`):**
  ```python
  router = DefaultRouter()
  router.register('posts', PostViewSet, basename='post')
  urlpatterns = router.urls
  ```

#### 2. Thực hành DJ-06 — JWT Authentication & Permission:
- **Cài đặt SimpleJWT:** `pip install djangorestframework-simplejwt`
- **Thêm Auth endpoints (`urls.py`):**
  ```python
  from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
  path('api/token/', TokenObtainPairView.as_view())
  path('api/token/refresh/', TokenRefreshView.as_view())
  ```
- **Áp dụng Permission:** Thêm `permission_classes = [IsAuthenticatedOrReadOnly]` vào `PostViewSet`.
- **Verify:** Send request `POST /api/posts/` không đính kèm `Authorization: Bearer <token>` -> Nhận `401 Unauthorized`. Đính kèm Token -> Tạo mới `201 Created`.

**Đọc chi tiết:** phần DRF trong [`03-Python-Expert/Django_Mastery_Guide.md`](../03-Python-Expert/Django_Mastery_Guide.md) + [`interview_prep/03_Database.md`](../interview_prep/03_Database.md) cho phần liên quan ORM/API. Dẫn chiếu thực hành: [`01-Django-Exercises/Checklist_Bai_Tap.md`](01-Django-Exercises/Checklist_Bai_Tap.md).

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Architecture Comparison: Django vs Flask vs FastAPI
* 🎯 **Dùng để làm gì?** Giúp kiến trúc sư hệ thống lựa chọn đúng Python Web Framework phù hợp nhất với quy mô, bài toán kinh doanh và yêu cầu hiệu năng của dự án.
* 💡 **Khi nào dùng?** 
  - **Django:** Chọn khi cần làm ứng dụng Enterprise, CMS, E-commerce, Admin Portal cần sẵn ORM, Admin Interface, Authentication, Security out-of-the-box để ra sản phẩm nhanh (Time-to-market).
  - **Flask:** Chọn khi làm Microservices nhỏ gọn, Utility APIs, hoặc project đòi hỏi tự do lựa chọn kiến trúc (Clean Architecture, ORM tùy chọn như SQLAlchemy).
  - **FastAPI:** Chọn khi xây dựng High-performance REST/GraphQL APIs, Microservices giao tiếp I/O dồn dập (WebSockets, Real-time Streaming, ML Model Serving), yêu cầu tự động hóa OpenAPI/Swagger doc.
* 🏭 **Thực tế sử dụng ra sao?**
  - Django: Monolith architecture cho startup giai đoạn 0 -> 1.
  - Flask: Lightweight Gateway hoặc Cronjob Worker Service.
  - FastAPI: Microservices Async đón hàng trăm ngàn request/phút.
* ⚙️ **Hoạt động ra sao?** Django và Flask chạy mặc định trên chuẩn **WSGI** (Synchronous, 1 Request/Thread). FastAPI chạy trên chuẩn **ASGI** (Asynchronous Server Gateway Interface) kết hợp với **uvicorn/starlette** event loop, xử lý non-blocking I/O hiệu năng vượt trội.

#### 2. FastAPI Pydantic Validation Engine
* 🎯 **Dùng để làm gì?** Tự động ép kiểu (Type Casting), Validate dữ liệu đầu vào HTTP Request theo Python Type Hints và sinh tự động tài liệu OpenAPI/Swagger UI `/docs`.
* 💡 **Khi nào dùng?** Dùng trong 100% endpoint của FastAPI thay cho việc viết validation thủ công.
* 🏭 **Thực tế sử dụng ra sao?**
  ```python
  from fastapi import FastAPI
  from pydantic import BaseModel, Field

  app = FastAPI()

  class OrderIn(BaseModel):
      customer_id: int = Field(..., gt=0)
      total: float = Field(..., gt=0)

  @app.post("/orders")
  async def create_order(order: OrderIn):
      return {"id": 1, **order.model_dump()}
  ```
* ⚙️ **Hoạt động ra sao?** Khi Client nộp JSON, Pydantic parse các field theo type hint. Nếu gửi sai kiểu (ví dụ `total: "abc"`), FastAPI tự chặn ngay ở tầng middleware và trả về HTTP `422 Unprocessable Entity` với thông tin chi tiết lỗi field nào mà dev không cần viết `try...except`.

#### 3. FastAPI Dependency Injection System (`Depends`)
* 🎯 **Dùng để làm gì?** Tách rời các mối phụ thuộc (Database Session, Auth User Token, Shared Config), tái sử dụng code sạch sẽ và hỗ trợ Override Dependencies cực kỳ dễ dàng khi viết Unit Test.
* 💡 **Khi nào dùng?** Dùng để extract logic dùng chung như Authenticate User, Check Permissions, Open/Close DB Session per request.
* 🏭 **Thực tế sử dụng ra sao?**
  ```python
  from fastapi import Depends, Header, HTTPException

  def get_current_user(token: str = Header(...)) -> dict:
      if token != "secret-token":
          raise HTTPException(status_code=401, detail="Invalid Token")
      return {"user_id": 42, "role": "admin"}

  @app.get("/me")
  async def read_me(current_user: dict = Depends(get_current_user)):
      return current_user
  ```
* ⚙️ **Hoạt động ra sao?** FastAPI xây dựng một Dependency Graph trước khi gọi route handler. Nó tự giải quyết các tầng phụ thuộc lồng nhau, gọi các hàm dependency, inject kết quả vào tham số và tự động dọn dẹp tài nguyên (nếu dùng `yield`).

#### 4. Sự cố nguy hiểm: Blocking Event Loop trong FastAPI
* 🎯 **Dùng để làm gì?** Nhận biết và phòng tránh thảm họa treo toàn bộ Server FastAPI Production khi lỡ dùng thư viện đồng bộ (Sync I/O) trong hàm `async def`.
* 💡 **Khi nào dùng?** Áp dụng quy tắc kiểm thử code review bắt buộc đối với mọi dự án Async Python.
* 🏭 **Thực tế sử dụng ra sao?**
  - ❌ **Code sai gây sập server:**
    ```python
    @app.get("/slow")
    async def slow_endpoint():
        time.sleep(5) # HOẶC requests.get("https://api.external.com")
        return {"status": "done"}
    ```
  - ✅ **Code đúng chuẩn Async:**
    ```python
    import asyncio, httpx

    @app.get("/fast")
    async def fast_endpoint():
        await asyncio.sleep(5)
        async with httpx.AsyncClient() as client:
            res = await client.get("https://api.external.com")
        return {"status": "done"}
    ```
* ⚙️ **Hoạt động ra sao?** `async def` chạy trực tiếp trên **Main Event Loop Thread**. Nếu gọi lệnh Blocking Sync (`time.sleep` hay `psycopg2`), Thread duy nhất này bị phong tỏa hoàn toàn. Mọi request của các User khác gửi tới Server đều bị đứng hình đợt timeout. Nếu buộc phải dùng thư viện Sync, phải đẩy sang ThreadPool bằng `def` thường (không có `async`) hoặc `anyio.to_thread.run_sync()`.

### 🛠️ Hướng dẫn thực hành từng bước (Bài tập FL-01 → FL-03):

#### 1. Thực hành FL-01 — Flask Thuần không ORM:
- **Viết API (`app.py`):**
  ```python
  from flask import Flask, request, jsonify
  app = Flask(__name__)
  posts_db = [{"id": 1, "title": "Flask Basics"}]

  @app.route('/api/posts', methods=['GET', 'POST'])
  def handle_posts():
      if request.method == 'POST':
          data = request.get_json()
          new_post = {"id": len(posts_db) + 1, "title": data['title']}
          posts_db.append(new_post)
          return jsonify(new_post), 201
      return jsonify(posts_db), 200
  ```
- **Chạy & Verify:** `python app.py` và test cURL `GET /api/posts` và `POST /api/posts`.

#### 2. Thực hành FL-02 — Tích hợp Flask-SQLAlchemy:
- **Cài đặt & Code:** `pip install flask-sqlalchemy`
  ```python
  from flask_sqlalchemy import SQLAlchemy
  db = SQLAlchemy(app)
  class Post(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      title = db.Column(db.String(100))

  with app.app_context(): db.create_all()
  ```

#### 3. Thực hành FL-03 — Blueprints & Application Factory Pattern:
- **Tổ chức Module (`app/posts/routes.py`):**
  ```python
  from flask import Blueprint, jsonify
  posts_bp = Blueprint('posts', __name__, url_prefix='/api/posts')
  @posts_bp.route('/', methods=['GET'])
  def get_posts(): return jsonify([])
  ```
- **Factory (`app/__init__.py`):**
  ```python
  def create_app():
      app = Flask(__name__)
      app.register_blueprint(posts_bp)
      return app
  ```

**Đọc chi tiết:** [`interview_prep/02_Flask_Backend.md`](../interview_prep/02_Flask_Backend.md). Đọc code thật: [`09-Example-Projects/Flask_RealWorld`](../09-Example-Projects/Flask_RealWorld), [`09-Example-Projects/Flask_SaaS_Boilerplate`](../09-Example-Projects/Flask_SaaS_Boilerplate). FastAPI: [`03-Python-Expert/Python_Backend_Professional_Guide.md`](../03-Python-Expert/Python_Backend_Professional_Guide.md) mục 3-4. Dẫn chiếu thực hành: [`02-Flask-Exercises/Checklist_Bai_Tap.md`](02-Flask-Exercises/Checklist_Bai_Tap.md).

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Unit Test & Test Coverage
* 🎯 **Dùng để làm gì?** Kiểm tra từng hàm/method độc lập đúng logic, chạy cực nhanh, làm "lưới an toàn" khi refactor.
* 💡 **Khi nào dùng?** Mọi logic nghiệp vụ thuần (tính giá, validate, phân quyền). Coverage chỉ là độ phủ — không chạy theo 100%; ưu tiên test các nhánh lỗi/biên (giá trị 0, âm, rỗng).
* 🏭 **Thực tế sử dụng ra sao?** `pytest --cov=app --cov-report=term-missing` trong CI, đặt ngưỡng (vd 80%) để chặn PR tụt coverage nghiêm trọng.
* ⚙️ **Hoạt động ra sao?** pytest tự tìm `test_*.py`, chạy từng hàm `test_*`, `assert` sai → fail kèm diff dễ đọc. Coverage đánh dấu dòng nào đã được thực thi — dòng được chạy qua ≠ được kiểm chứng đúng.

#### 2. Integration Test & Mock/Patch
* 🎯 **Dùng để làm gì?** Integration: kiểm tra các phần thật nối đúng nhau (API + DB). Mock/Patch: thay thế tạm thành phần bên ngoài (email, thanh toán) để test chạy nhanh, ổn định, không gây tác dụng phụ thật.
* 💡 **Khi nào dùng?** Integration cho các luồng quan trọng (đăng ký, thanh toán) với DB test thật. Mock cho dịch vụ bên thứ 3 (gửi mail, gọi API ngoài). Đừng mock quá tay: mock hết mọi thứ thì test chỉ kiểm tra chính cái mock.
* 🏭 **Thực tế sử dụng ra sao?** `patch("app.services.send_email")` rồi `assert_called_once_with(...)`; Integration dùng `APIClient` (DRF) / `client` fixture + DB test tự rollback sau mỗi test.
* ⚙️ **Hoạt động ra sao?** `patch` thay tên `send_email` trong module bằng `MagicMock` chỉ trong phạm vi `with`, rồi khôi phục. Lưu ý patch đúng nơi **được dùng** (`app.services.send_email`), không phải nơi định nghĩa.

#### 3. TDD & Load Testing (Locust/k6)
* 🎯 **Dùng để làm gì?** TDD: viết test trước để ép nghi rõ yêu cầu. Load test: trả lời "hệ thống chịu được bao nhiêu request/giây trước khi gãy".
* 💡 **Khi nào dùng?** TDD khi logic phức tạp/bug-fix (viết test tái hiện bug trước). Load test trước mùa cao điểm, trước khi chọn số replica/`requests-limits` K8s, sau thay đổi kiến trúc lớn.
* 🏭 **Thực tế sử dụng ra sao?** Locust mô tả hành vi user bằng Python, tăng dần 100 → 1000 user; theo dõi p95 latency, error rate; chạy trên môi trường giống production (không phải prod thật).
* ⚙️ **Hoạt động ra sao?** TDD theo vòng Red → Green → Refactor. Load test sinh nhiều user ảo gọi song song để đo throughput/latency và tìm "điểm gãy" (CPU, pool DB, timeout), từ đó biết cần scale ở đâu.

<details>
<summary>📖 Diễn giải bổ sung & code minh họa</summary>

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

</details>

### 🛠️ Hướng dẫn thực hành từng bước (Bài tập DJ-07):

#### 1. Thực hành DJ-07 — Integration Test API với DRF (`APITestCase`):
- **Viết Test Suite (`blog/tests.py`):**
  ```python
  from rest_framework.test import APITestCase
  from rest_framework import status
  from django.contrib.auth.models import User
  from .models import Author, Post

  class PostAPITestCase(APITestCase):
      def setUp(self):
          self.user = User.objects.create_user(username='tester', password='pass')
          self.author = Author.objects.create(name='Author 1', email='a1@test.com')

      def test_get_posts_list_unauthenticated(self):
          res = self.client.get('/api/posts/')
          self.assertEqual(res.status_code, status.HTTP_200_OK)

      def test_create_post_unauthenticated_fails(self):
          res = self.client.post('/api/posts/', {'title': 'New', 'content': 'C', 'author': self.author.id})
          self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

      def test_create_post_authenticated_success(self):
          self.client.force_authenticate(user=self.user)
          res = self.client.post('/api/posts/', {'title': 'New', 'content': 'C', 'author': self.author.id})
          self.assertEqual(res.status_code, status.HTTP_201_CREATED)
  ```
- **Chạy Test Suite & Verify:** `python manage.py test blog` hoặc `pytest`.

**Đọc chi tiết:** [`Mastery/Backend-Mastery/04-Testing-Observability-And-Debugging-Prod`](../Mastery/Backend-Mastery/04-Testing-Observability-And-Debugging-Prod). Load testing: [`Mastery/Backend-Mastery/02-Concurrency-And-Async-In-Production`](../Mastery/Backend-Mastery/02-Concurrency-And-Async-In-Production). Dẫn chiếu thực hành: [`01-Django-Exercises/Checklist_Bai_Tap.md`](01-Django-Exercises/Checklist_Bai_Tap.md).

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

**Giải thích chi tiết chuyên sâu:**

#### 1. REST chuẩn, Versioning & Pagination (cursor vs offset)
* 🎯 **Dùng để làm gì?** Thiết kế API nhất quán, dễ dùng, đổi được mà không phá client cũ; phân trang để không trả cả triệu dòng 1 lần.
* 💡 **Khi nào dùng?** Mọi API public/nội bộ có nhiều client. Versioning (`/api/v1/`) khi cần thay đổi *breaking*. `offset/limit` cho danh sách nhỏ/admin cần nhảy trang; `cursor` cho feed/danh sách lớn, dữ liệu thay đổi liên tục.
* 🏭 **Thực tế sử dụng ra sao?** `GET /api/v1/orders?after=<id_cuối>&limit=20` → trả `{ "results": [...], "next_cursor": "..." }`. Thêm field mới = không breaking; đổi tên/xóa field = breaking → ra `v2`, giữ `v1` một thời gian.
* ⚙️ **Hoạt động ra sao?** `OFFSET 100000` buộc DB đọc rồi bỏ 100000 dòng → chậm dần, và dòng mới chèn vào làm lệch trang. Cursor dùng `WHERE id > :cursor ORDER BY id LIMIT 20` tận dụng index → luôn nhanh và ổn định.

#### 2. Idempotency (API thanh toán/retry)
* 🎯 **Dùng để làm gì?** Gửi cùng 1 request nhiều lần (mạng lỗi, client retry) vẫn chỉ tạo **1 kết quả** — tránh trừ tiền/tạo đơn trùng.
* 💡 **Khi nào dùng?** Mọi `POST` có tác dụng phụ quan trọng (thanh toán, tạo đơn, gửi tiền). `GET/PUT/DELETE` vốn đã idempotent theo thiết kế REST.
* 🏭 **Thực tế sử dụng ra sao?** Client sinh `Idempotency-Key` (UUID) cho mỗi *ý định* thanh toán, gửi kèm header; retry dùng lại đúng key. Stripe/các cổng thanh toán dùng cách này. (Code minh họa bên dưới.)
* ⚙️ **Hoạt động ra sao?** Server lưu `key → response` (có ràng buộc UNIQUE trên key). Request đầu: xử lý + lưu. Request trùng: thấy key đã có → trả lại response cũ, **không xử lý lại**. Phải xử lý cả trường hợp 2 request đến cùng lúc (khóa/UNIQUE) để không race condition.

#### 3. REST vs gRPC vs GraphQL
* 🎯 **Dùng để làm gì?** Chọn giao thức giao tiếp phù hợp giữa client–server/service–service.
* 💡 **Khi nào dùng?** **REST**: API public, CRUD thông thường (mặc định an toàn). **gRPC**: service-to-service nội bộ, cần tốc độ cao/streaming. **GraphQL**: nhiều loại client (web/mobile) cần hình dạng dữ liệu khác nhau, tránh over/under-fetching. Không dùng GraphQL cho API đơn giản — thêm phức tạp cache/bảo mật.
* 🏭 **Thực tế sử dụng ra sao?** Thường kết hợp: REST/GraphQL ra ngoài, gRPC giữa các microservice (bảng so sánh ngay bên dưới).
* ⚙️ **Hoạt động ra sao?** gRPC: Protocol Buffers (nhị phân) + HTTP/2 → nhỏ, nhanh. GraphQL: 1 endpoint, client gửi query nêu rõ field, server “ghép” dữ liệu từ nhiều nguồn; đánh đổi là khó cache HTTP và phải giới hạn độ sâu query.

#### 4. WebSocket vs SSE vs Long Polling
* 🎯 **Dùng để làm gì?** Đẩy dữ liệu real-time từ server tới client mà không phải client hỏi liên tục.
* 💡 **Khi nào dùng?** **WebSocket**: cần 2 chiều (chat, game, cộng tác). **SSE**: chỉ server→client (thông báo, tiến độ job, giá realtime) — đơn giản hơn, tự reconnect. **Long Polling**: chỉ khi môi trường không hỗ trợ 2 cách trên.
* 🏭 **Thực tế sử dụng ra sao?** Thông báo "đơn hàng đã giao" → SSE là đủ; chat nhóm → WebSocket (cần sticky session hoặc pub/sub Redis khi nhiều server).
* ⚙️ **Hoạt động ra sao?** WebSocket nâng cấp HTTP thành kết nối TCP 2 chiều giữ mở. SSE giữ 1 HTTP response mở, server ghi từng `event:`/`data:`. Long polling: client gọi, server giữ request đến khi có dữ liệu rồi trả, client gọi lại — tốn kết nối.

<details>
<summary>📖 Diễn giải bổ sung & code minh họa (OpenAPI, bảng so sánh...)</summary>

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

</details>

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Request Lifecycle (Nginx → WSGI/ASGI → Middleware → View → DB)
* 🎯 **Dùng để làm gì?** Hiểu 1 request đi qua những tầng nào để biết lỗi/chậm nằm ở tầng nào (Nginx 502/504, app lỗi 500, DB chậm).
* 💡 **Khi nào dùng?** Mỗi khi debug production, cấu hình timeout, thêm middleware/auth/log, hoặc tính toán điểm nghẽn.
* 🏭 **Thực tế sử dụng ra sao?** `Client → Nginx (SSL, gzip, static) → Gunicorn/Uvicorn → Middleware → View → ORM → DB`. Nginx trả `502` = không nối được app server; `504` = app trả lời quá timeout; `500` = exception trong code.
* ⚙️ **Hoạt động ra sao?** Nginx là reverse proxy nhận kết nối từ internet rồi chuyển tiếp. WSGI/ASGI server "dịch" HTTP thành lời gọi Python; middleware chạy theo thứ tự vào và ngược lại khi ra; response đi ngược chiều.

#### 2. WSGI (Gunicorn) vs ASGI (Uvicorn)
* 🎯 **Dùng để làm gì?** Quy định cách server xử lý nhiều request cùng lúc: 1 request = 1 thread/process (WSGI) hay nhiều request đang chờ I/O chia sẻ 1 event loop (ASGI).
* 💡 **Khi nào dùng?** WSGI cho CRUD thông thường (Django/Flask mặc định — đơn giản, ổn định). ASGI khi I/O-bound nặng (gọi nhiều API ngoài, WebSocket, SSE). Đừng đổi "cho sang" nếu code vẫn gọi thư viện sync bên trong.
* 🏭 **Thực tế sử dụng ra sao?** `gunicorn app:app -w 4` (WSGI) hoặc `gunicorn -k uvicorn.workers.UvicornWorker app:app -w 4` (ASGI, mỗi worker 1 event loop).
* ⚙️ **Hoạt động ra sao?** WSGI: thread chờ I/O thì đứng yên. ASGI: khi `await` I/O, event loop đổi sang request khác; 1 lời gọi sync chặn giữa chừng sẽ chặn toàn bộ loop (xem Chương 7).

#### 3. Thread vs Process vs Async & Tuning số Worker
* 🎯 **Dùng để làm gì?** Chọn mô hình song song phù hợp bài toán (CPU-bound hay I/O-bound) và đặt số worker để tận dụng hết CPU.
* 💡 **Khi nào dùng?** **Process**: tính toán nặng (resize ảnh, xử lý dữ liệu) — mỗi process 1 GIL riêng. **Thread/Async**: chờ I/O (gọi API, DB). Quy tắc khởi điểm worker: ~`2 × số core + 1` (WSGI), rồi **load test** để chốt.
* 🏭 **Thực tế sử dụng ra sao?** Sự cố hay gặp: chạy `--workers 1` vì nghi "async đã nhanh" trên máy 8 lõi → chỉ dùng 1 lõi, thông lượng thấp gần 8 lần so với khả năng.
* ⚙️ **Hoạt động ra sao?** GIL chỉ cho 1 thread chạy bytecode tại 1 thời điểm trong 1 process → thread không tăng tốc CPU-bound. 1 event loop chạy trên 1 lõi → muốn dùng nhiều lõi phải nhiều process (worker).

#### 4. Background Task: `BackgroundTasks` vs Celery Queue
* 🎯 **Dùng để làm gì?** Đẩy việc nặng/chậm (gửi email, xuất PDF, gọi API chậm) ra khỏi vòng request–response để trả user ngay.
* 💡 **Khi nào dùng?** `BackgroundTasks`: việc nhỏ, mất cũng được (ghi log phụ). **Celery/RQ + Redis/RabbitMQ**: việc quan trọng (email xác nhận thanh toán, xử lý đơn) cần retry, persistence, theo dõi.
* 🏭 **Thực tế sử dụng ra sao?** View `POST /reports` → `generate_report.delay(user_id)` → trả `202 Accepted` + `task_id`; client poll `/reports/<task_id>`. Worker riêng: `celery -A app worker -l info`.
* ⚙️ **Hoạt động ra sao?** `BackgroundTasks` chạy **cùng process** → server restart là mất task, không retry. Celery: producer đẩy message vào broker (persistent), worker lấy ra xử lý, lỗi thì retry/đẩy vào dead-letter queue.

<details>
<summary>📖 Diễn giải bổ sung & code minh họa</summary>

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

</details>

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

### 🧭 Tóm tắt 4 câu hỏi cho từng chủ đề (đọc trước khi vào chi tiết)

#### 11.1 Caching (Cache-aside / Write-through / Write-behind)
* 🎯 **Dùng để làm gì?** Giảm tải DB và giảm latency bằng cách giữ kết quả hay đọc ở nơi truy cập nhanh (RAM/Redis).
* 💡 **Khi nào dùng?** Dữ liệu đọc nhiều – ghi ít, tính toán/truy vấn tốn kém (trang chủ, cấu hình, profile). **Không** cache dữ liệu bắt buộc luôn đúng tức thì (số dư, tồn kho cuối) nếu chưa có cơ chế invalidate chắc chắn.
* 🏭 **Thực tế?** Cache-aside: `v = redis.get(k); if v is None: v = db.query(); redis.setex(k, 300, v)`. Luôn đặt TTL; xóa key khi dữ liệu gốc đổi.
* ⚙️ **Hoạt động?** Cache-aside: app tự đọc/ghi cache. Write-through: ghi DB + cache cùng lúc (chậm ghi, cache luôn mới). Write-behind: ghi cache trước, đẩy DB sau (nhanh nhưng có thể mất dữ liệu). Stampede: key hot hết hạn → hàng loạt request đổ vào DB → chống bằng lock/gia hạn sớm ngẫu nhiên.

#### 11.2 Message Queue vs Pub/Sub
* 🎯 **Dùng để làm gì?** Tách rời hai phía (producer/consumer), làm đệm khi tải đột biến và xử lý bất đồng bộ.
* 💡 **Khi nào dùng?** Queue (RabbitMQ/SQS): mỗi message cần **đúng 1** nơi xử lý (task nền). Pub/Sub, Kafka/SNS: **nhiều** nơi cùng cần biết 1 sự kiện (đơn hàng được tạo → kho, email, thống kê).
* 🏭 **Thực tế?** Celery dùng RabbitMQ/Redis làm broker; sự kiện nghiệp vụ lớn đẩy qua Kafka hoặc SNS→SQS (fan-out).
* ⚙️ **Hoạt động?** Queue: message bị xóa sau khi 1 consumer xác nhận (ack). Kafka: ghi vào log bền vững, mỗi consumer group giữ offset riêng → đọc độc lập và có thể đọc lại.

#### 11.3 Celery & Task Idempotent
* 🎯 **Dùng để làm gì?** Chạy việc nặng/chậm ở worker riêng, có retry, lịch chạy (beat).
* 💡 **Khi nào dùng?** Gửi email, xuất báo cáo, đồng bộ dữ liệu. Task phải **idempotent** vì có thể chạy lại (retry, worker crash sau khi xử lý nhưng trước khi ack).
* 🏭 **Thực tế?** `@shared_task(bind=True, max_retries=3, autoretry_for=(Exception,), retry_backoff=True)`; truyền **ID** vào task thay vì object lớn; kiểm tra "đã xử lý chưa" bằng khóa/trạng thái trước khi tác động.
* ⚙️ **Hoạt động?** `.delay()` serialize tham số → đẩy vào broker → worker nhận, chạy, ack. Mặc định ack *sau khi chạy xong* (at-least-once) → có thể chạy 2 lần → cần idempotent.

#### 11.4 Load Balancing
* 🎯 **Dùng để làm gì?** Phân phối request tới nhiều server để chịu tải và không có điểm chết đơn lẻ.
* 💡 **Khi nào dùng?** Khi 1 server không đủ tải hoặc cần HA. L4 cho tốc độ/TCP thuần; L7 cho routing theo path/host, SSL termination.
* 🏭 **Thực tế?** Nginx/ALB trước nhiều instance; health check tự loại instance lỗi; thuật toán round-robin / least-connections; sticky session chỉ khi bắt buộc (app stateless thì không cần).
* ⚙️ **Hoạt động?** LB nhận kết nối, chọn backend theo thuật toán, chuyển tiếp; backend không qua health check bị rút khỏi pool tạm thời.

#### 11.5 CDN
* 🎯 **Dùng để làm gì?** Phục vụ nội dung tĩnh từ máy chủ gần người dùng nhất → nhanh hơn, giảm tải origin.
* 💡 **Khi nào dùng?** Ảnh, JS/CSS, video, file tải về. Không cache nội dung riêng tư theo user nếu không cấu hình đúng `Cache-Control`/`Vary`.
* 🏭 **Thực tế?** CloudFront/Cloudflare trước S3/Nginx; đặt `Cache-Control: public, max-age=31536000, immutable` cho file có hash trong tên; invalidate khi đổi.
* ⚙️ **Hoạt động?** Request tới edge gần nhất → có cache thì trả luôn (HIT), không thì lấy từ origin rồi lưu lại (MISS).

#### 11.6–11.7 CAP/PACELC & Replication lag
* 🎯 **Dùng để làm gì?** Hiểu đánh đổi khi dữ liệu nằm trên nhiều node: khi mạng bị chia cắt phải chọn **nhất quán (C)** hay **sẵn sàng (A)**; khi bình thường vẫn đánh đổi **độ trễ vs nhất quán**.
* 💡 **Khi nào dùng?** Chọn DB/kiến trúc multi-region; quyết định luồng nào được đọc từ replica (chấp nhận dữ liệu cũ vài giây) và luồng nào phải đọc từ primary.
* 🏭 **Thực tế?** Sau khi user cập nhật hồ sơ, trang kế tiếp đọc từ replica có thể thấy dữ liệu cũ → đọc từ primary trong vài giây đầu ("read-your-writes").
* ⚙️ **Hoạt động?** Replica nhận log thay đổi bất đồng bộ nên luôn trễ chút; CP: từ chối phục vụ để giữ đúng; AP: vẫn phục vụ nhưng có thể thấy dữ liệu cũ.

#### 11.8 Thiết kế URL Shortener
* 🎯 **Dùng để làm gì?** Bài mẫu để tập quy trình thiết kế: yêu cầu → ước lượng tải → API → lưu trữ → scale → trade-off.
* 💡 **Khi nào dùng?** Phỏng vấn system design; mẫu tư duy cho mọi dịch vụ đọc nhiều (read-heavy).
* 🏭 **Thực tế?** `POST /shorten` sinh mã base62 từ ID tăng dần hoặc hash; `GET /{code}` → 301/302; cache mã nóng bằng Redis; DB khóa chính theo `code`.
* ⚙️ **Hoạt động?** Đọc >> ghi nên cache chặn đa số truy vấn; mã sinh từ bộ đếm phân tán/Snowflake để tránh trùng giữa nhiều server.

#### 11.9 Rate Limiter
* 🎯 **Dùng để làm gì?** Chặn lạm dụng/brute-force, bảo vệ backend khỏi quá tải.
* 💡 **Khi nào dùng?** Login, OTP, API public, endpoint tốn kém. Đặt ở API Gateway/Nginx và/hoặc tầng ứng dụng.
* 🏭 **Thực tế?** Token Bucket trên Redis: key theo `user_id/IP`; vượt ngưỡng trả `429` kèm `Retry-After`.
* ⚙️ **Hoạt động?** Token Bucket: xô chứa token, nạp đều theo thời gian, mỗi request lấy 1 token; hết token thì từ chối. Dùng thao tác nguyên tử (Lua/`INCR`+`EXPIRE`) để đúng khi nhiều server cùng đếm.

#### 11.10 Circuit Breaker
* 🎯 **Dùng để làm gì?** Ngăn lỗi lan chuyền: khi service phụ thuộc đang hỏng/chậm, ngừng gọi nó để không treo luôn service của mình.
* 💡 **Khi nào dùng?** Mọi lời gọi tới service ngoài/microservice khác có thể chậm hoặc chết (thanh toán, gửi SMS, API đối tác).
* 🏭 **Thực tế?** Thư viện (`pybreaker`, Resilience4j...) + timeout + retry có backoff + fallback (trả dữ liệu cache/giá trị mặc định).
* ⚙️ **Hoạt động?** 3 trạng thái: **Closed** (gọi bình thường) → vượt ngưỡng lỗi → **Open** (từ chối ngay, không gọi) → sau thời gian chờ → **Half-open** (thử vài request): thành công thì về Closed, thất bại thì quay lại Open.

<a id="chuong-11-1"></a>
### 11.1 Caching sâu — 🟡 Nâng cao

**Kiến thức cần học:**
- 🟢 Cơ bản: Local cache (in-process, `lru_cache`) vs Distributed cache (Redis) — khi nào dùng loại nào; TTL là gì.
- 🟡 Nâng cao: 3 chiến lược ghi cache: **Cache-aside** (lazy loading), **Write-through**, **Write-behind** (write-back); eviction policy **LRU** vs **LFU**.
- 🔴 Chuyên sâu/Thực chiến: **Cache stampede** (thundering herd) và 2 cách chống phổ biến — lỗi gây sập DB thật trong production nếu không biết trước.

**Giải thích chi tiết chuyên sâu:**

#### 1. Distributed Caching & Cache Strategies (Cache-Aside, Write-Through, Write-Behind, Stampede)
* 🎯 **Dùng để làm gì?** Tăng tốc độ đọc dữ liệu gấp 10-100 lần bằng cách nạp dữ liệu hot vào bộ nhớ RAM (Redis/Memcached), giảm tải trực tiếp cho Database chính.
* ⏰ **Khi nào sử dụng?**
  * **Cache-aside (Lazy Loading):** Phổ biến nhất. App check Redis trước, miss thì query DB rồi ghi lại vào Redis. Dùng cho dữ liệu đọc nhiều ghi ít (User Profile, Product Catalog).
  * **Write-through:** App ghi vào Cache + DB đồng thời. Dùng cho hệ thống yêu cầu Cache luôn nhất quán với DB (User Session, Auth Token).
  * **Write-behind (Write-back):** Ghi vào Cache trước, async ghi xuống DB sau. Dùng cho dữ liệu ghi cực lớn nhưng chấp nhận mất mát rủi ro (View count, Like count, Page Analytics).
  * **Chống Cache Stampede (Thundering Herd):** Dùng Mutex/Lock hoặc Probabilistic Early Expiration khi có 1 key cực hot bị hết hạn.
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  ```python
  import json
  import time
  from django.core.cache import cache

  def get_user_profile(user_id: int):
      cache_key = f"user_profile:{user_id}"
      
      # 1. Try get from Cache-aside
      data = cache.get(cache_key)
      if data:
          return json.loads(data)
      
      # 2. Lock / Mutex để chống Cache Stampede
      lock_acquired = cache.add(f"lock:{cache_key}", "1", timeout=5)
      if lock_acquired:
          try:
              profile = DB.query_user_profile(user_id)  # Query DB nặng
              cache.set(cache_key, json.dumps(profile), timeout=3600)
              return profile
          finally:
              cache.delete(f"lock:{cache_key}")
      else:
          time.sleep(0.05)
          return get_user_profile(user_id)  # Retry sau khi thread chính ghi cache xong
  ```
* ⚙️ **Cơ chế hoạt động ra sao?**
  * LRU (Least Recently Used) tự động xóa key lâu nhất không được đọc khi RAM đầy. LFU (Least Frequently Used) xóa key có tần suất đọc thấp nhất.
  * Mutex Lock đảm bảo chỉ **1 request duy nhất** đi xuống DB tính toán lại key hot khi hết hạn, các request khác chờ vài mili-giây để đọc bản cache mới.

---

#### 2. Message Queue vs Pub/Sub (RabbitMQ vs Kafka vs AWS SQS/SNS)
* 🎯 **Dùng để làm gì?** Giúp giao tiếp bất đồng bộ (Asynchronous Communication) giữa các service, san phẳng lưu lượng truy cập (Traffic Leveling / Rate Smoothing) và gỡ bỏ phụ thuộc trực tiếp (Decoupling).
* ⏰ **Khi nào sử dụng?**
  * **Message Queue (Point-to-Point - RabbitMQ, AWS SQS):** Một message gửi ra chỉ được **đúng 1 worker** lấy xử lý rồi xóa bỏ (Task queue cho Celery, gửi Email/SMS, xử lý thanh toán).
  * **Pub/Sub & Log-based Streaming (Kafka, AWS SNS):** Một message/event phát ra được **nhiều Subscriber / Consumer Groups** cùng đọc độc lập (Event-driven Architecture, Audit Log, Real-time Analytics).
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  * Khi đơn hàng tạo thành công: Event `OrderCreated` được publish lên Kafka Topic. Group 1 (Order Service) lưu DB, Group 2 (Inventory Service) trừ kho, Group 3 (Notification Service) gửi SMS — cả 3 chạy song song không block lẫn nhau.
* ⚙️ **Cơ chế hoạt động ra sao?**
  * **RabbitMQ:** Sử dụng `Exchange` (Direct, Fanout, Topic) đính kèm `Routing Key` để đẩy message vào các `Queue` nằm trên RAM worker.
  * **Kafka:** Lưu trữ message dưới dạng Append-only Commit Log ghi trên đĩa cứng (Disk Persistence), các Consumer quản lý vị trí đọc thông qua `Offset`.

---

#### 3. Background Task với Celery & Idempotent Execution
* 🎯 **Dùng để làm gì?** Đẩy các tác vụ tốn thời gian (Gửi email, Export PDF, xử lý video, gọi API bên thứ 3) ra khỏi luồng HTTP Request/Response chính để trả về phản hồi lập tức cho client.
* ⏰ **Khi nào sử dụng?** Bắt buộc sử dụng cho mọi tác vụ I/O chậm (> 200ms) hoặc dễ gặp sự cố gián đoạn mạng.
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  ```python
  @celery_app.task(bind=True, max_retries=5)
  def apply_points_transaction(self, user_id: int, transaction_id: str, points: int):
      # Idempotency Check: Đảm bảo retry không bị cộng điểm 2 lần
      if ProcessedTransaction.objects.filter(id=transaction_id).exists():
          return  # Đã xử lý rồi -> Bỏ qua an toàn

      try:
          with transaction.atomic():
              User.objects.filter(id=user_id).update(points=F("points") + points)
              ProcessedTransaction.objects.create(id=transaction_id)
      except Exception as exc:
          # Exponential Backoff: 2s, 4s, 8s, 16s...
          raise self.retry(exc=exc, countdown=2 ** self.request.retries)
  ```
* ⚙️ **Cơ chế hoạt động ra sao?**
  * Celery Producer gửi payload (JSON) mô tả tên task và tham số vào Broker (Redis/RabbitMQ). Worker process lắng nghe Broker, nhặt payload ra thực thi ngầm.
  * **Idempotency:** Kết hợp `transaction_id` duy nhất và DB Unique Constraint để đảm bảo dù Celery retry nhiều lần do rớt mạng (network ACK fail), kết quả hệ thống vẫn chính xác tuyệt đối.

---

#### 4. Load Balancing, Stateful vs Stateless & Consistent Hashing
* 🎯 **Dùng để làm gì?** Phân phối đều lưu lượng HTTP/TCP tới cụm các máy chủ (App Instances) phía sau, nâng cao khả năng mở rộng ngang (Horizontal Scaling) và tính sẵn sàng cao (High Availability).
* ⏰ **Khi nào sử dụng?** Dùng Nginx/HAProxy/AWS ALB đứng trước hệ thống Backend khi lưu lượng tăng vượt quá khả năng xử lý của 1 máy chủ đơn lẻ.
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  * Thuật toán **Round Robin** cho các app instance đồng đều.
  * Thuật toán **Least Connections** khi các request có thời gian xử lý lệch nhau lớn.
  * **Consistent Hashing** trong cụm Redis Cluster hoặc DB Sharding để giảm thiểu 90% số key bị map lại khi thêm/bớt node.
* ⚙️ **Cơ chế hoạt động ra sao?**
  * **Stateless App:** Không lưu Session trong bộ nhớ RAM của Server mà lưu trong Redis hay JWT Token, giúp Load Balancer đẩy request tới bất kỳ máy chủ nào cũng xử lý được.
  * **Consistent Hashing:** Hash các node server và data key lên một vòng tròn băm 360 độ (`Ring`). Khi 1 node sập, chỉ các key thuộc về node đó bị rehash sang node kế tiếp, không ảnh hưởng tới toàn bộ hệ thống như `key % N`.

---

#### 5. CAP / PACELC Theorem & Eventual Consistency
* 🎯 **Dùng để làm gì?** Cung cấp khung lý thuyết nền tảng giúp Software Architect lựa chọn cơ sở dữ liệu (PostgreSQL vs MongoDB vs Cassandra) và thiết kế chiến lược nhân bản (Replication).
* ⏰ **Khi nào sử dụng?** Khi thiết kế hệ thống phân tán đa vùng (Multi-region) hoặc hệ thống đọc ghi phân tách (Read Replicas).
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  * **CP System (Consistency / Partition Tolerance):** Ngân hàng, Ví điện tử, Hệ thống Đặt vé — Thà từ chối giao dịch (Fail fast) chứ nhất quyết không trả về số dư/vé sai.
  * **AP System (Availability / Partition Tolerance):** Social Newsfeed, Giỏ hàng E-commerce, Like Count — Thà hiển thị tin tức chậm 1 vài giây còn hơn báo lỗi sập trang.
  * **Read-Your-Writes Pattern:** Sau khi User sửa Profile (Ghi vào Primary DB), lần đọc ngay tiếp theo sẽ bắt buộc đọc từ Primary DB thay vì Read Replica để tránh dính Replication Lag.
* ⚙️ **Cơ chế hoạt động ra sao?**
  * PACELC mở rộng CAP: Nếu có Partition (P) -> chọn A hay C; Else (Mạng bình thường) -> chọn Latency (L) hay Consistency (C).

---

#### 6. System Design Walkthrough: Rate Limiter & Circuit Breaker
* 🎯 **Dùng để làm gì?** Bảo vệ hệ thống khỏi bị quá tải (DoS/DDoS) và ngăn ngừa lỗi dây chuyền (Cascading Failure) khi các microservice gọi lẫn nhau.
* ⏰ **Khi nào sử dụng?** Đặt Rate Limiter ở API Gateway để giới hạn request theo IP/User ID. Đặt Circuit Breaker ở các HTTP Client / Service Call đểfail fast khi downstream service bị rớt.
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  ```python
  from circuitbreaker import circuit

  # Circuit Breaker ngắt mạch sau 5 lần lỗi liên tiếp, thử lại sau 30s
  @circuit(failure_threshold=5, recovery_timeout=30)
  def call_third_party_payment(order_id: str):
      response = requests.post("https://payment-api.com/v1/charge", json={"id": order_id}, timeout=3)
      return response.json()
  ```
* ⚙️ **Cơ chế hoạt động ra sao?**
  * **Token Bucket (Rate Limiter):** Mỗi request đến tốn 1 token trong xô (Bucket). Xô được nạp thêm token theo tốc độ cố định `R`. Nếu xô hết token -> Trả HTTP 429 Too Many Requests.
  * **Circuit Breaker States:** Closed (Bình thường) -> Open (Ngắt mạch, fail fast ngay trong 0ms không chờ timeout 3s) -> Half-Open (Cho 1 request chạy thử để xem downstream khôi phục chưa).

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

**Giải thích chi tiết chuyên sâu:**

#### 1. OWASP Top 10: SQL Injection, XSS, CSRF
* 🎯 **Dùng để làm gì?** Danh sách rủi ro bảo mật web phổ biến nhất — dùng làm checklist để không mắc lỗi cơ bản gây lộ/mất dữ liệu.
* 💡 **Khi nào dùng?** Mọi lần nhận input từ người dùng, render HTML, xử lý form/cookie, viết login. Django chặn sẵn nhiều thứ nhưng **chỉ khi bạn dùng đúng cách** (ORM, template, `{% csrf_token %}`).
* 🏭 **Thực tế sử dụng ra sao?** Không nối chuỗi SQL tay → dùng ORM/tham số `%s`; không `mark_safe()`/`|safe` với dữ liệu user; bật `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, `SECURE_HSTS_SECONDS` ở production; chạy `python manage.py check --deploy`.
* ⚙️ **Hoạt động ra sao?** ORM gửi tham số *tách riêng* khỏi câu SQL (prepared statement) nên `1 OR 1=1` chỉ là chuỗi thường. Template auto-escape `<script>` thành `&lt;script&gt;`. CSRF token gắn vào form và được server so với cookie → trang web lạ không thể giả request thay bạn.

#### 2. Authentication vs Authorization & JWT
* 🎯 **Dùng để làm gì?** Authentication = *bạn là ai*; Authorization = *bạn được làm gì*. JWT là cách mang danh tính *stateless* giữa client–server.
* 💡 **Khi nào dùng?** JWT cho API/SPA/mobile/microservices. Session cookie phù hợp web server-rendered. Không nhét dữ liệu nhạy cảm vào payload JWT (ai cũng đọc được).
* 🏭 **Thực tế sử dụng ra sao?** Access token ~15 phút + refresh token ~7 ngày; kiểm quyền ở **mỗi** endpoint (`permission_classes`), không chỉ ẩn nút ở frontend. Trả `401` khi chưa đăng nhập, `403` khi đăng nhập nhưng không đủ quyền.
* ⚙️ **Hoạt động ra sao?** JWT = `header.payload.signature`; server ký bằng secret/private key. Nhận token: tính lại chữ ký + kiểm `exp` → không cần tra DB. Đánh đổi: khó thu hồi ngay (cần blacklist/đổi key).

#### 3. Secret Management & Logging Security
* 🎯 **Dùng để làm gì?** Giữ bí mật (mật khẩu DB, API key) không lọt vào Git/log/image; log đủ để điều tra nhưng không tự tạo kênh rò rỉ.
* 💡 **Khi nào dùng?** Mọi dự án. `.env` cho local; production dùng Vault/AWS Secrets Manager/K8s Secret (kèm Sealed/External Secrets). **Log**: login thành công/thất bại, 403, thao tác sửa/xóa dữ liệu nhạy cảm. **Không log**: mật khẩu, token, số thẻ, API key.
* 🏭 **Thực tế sử dụng ra sao?** `.gitignore` chứa `.env`; quét repo bằng `gitleaks`/`trufflehog`; lỡ commit secret → **xoay (rotate) secret ngay** rồi mới dọn lịch sử Git (xem LAB-02).
* ⚙️ **Hoạt động ra sao?** App đọc secret từ biến môi trường/secret store lúc khởi động thay vì nằm trong code. K8s Secret mặc định chỉ base64 (không phải mã hóa) nên cần thêm lớp mã hóa/đồng bộ từ Vault.

#### 4. OAuth2, Rate Limiting & Dependency Scanning
* 🎯 **Dùng để làm gì?** OAuth2: "đăng nhập bằng Google/Facebook" mà không chia sẻ mật khẩu. Rate limit: chặn brute-force/lạm dụng. Dependency scanning: phát hiện CVE trong thư viện bên thứ 3.
* 💡 **Khi nào dùng?** OAuth2 khi muốn SSO/giảm ma sát đăng ký. Rate limit cho login/OTP/API public. Quét dependency trong CI mỗi PR.
* 🏭 **Thực tế sử dụng ra sao?** Authorization Code flow (backend đổi `code` lấy token); Token Bucket cho rate limit; `pip-audit`/`safety`/Dependabot chạy tự động, pin version trong lock file.
* ⚙️ **Hoạt động ra sao?** OAuth2: app → redirect sang Google → user đồng ý → Google trả `code` về backend → backend đổi lấy access token (token không lộ ra trình duyệt). Fixed Window có kẽ hở ở biên thời gian (200 request trong 2 giây) nên Token Bucket mượt hơn. Scanner đối chiếu version package với cơ sở dữ liệu CVE.

<details>
<summary>📖 Diễn giải bổ sung & code minh họa</summary>

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

</details>

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Structured Logging
* 🎯 **Dùng để làm gì?** Ghi log dạng JSON có trường rõ ràng để *truy vấn* được (vd tìm mọi log của `order_id=42`) thay vì `print()` vô dụng khi có hàng triệu dòng.
* 💡 **Khi nào dùng?** Mọi service production, thiết kế **từ đầu** (rất khó bổ sung khi hệ thống đã lớn). Luôn kèm `request_id`/`trace_id`, không log dữ liệu nhạy cảm.
* 🏭 **Thực tế sử dụng ra sao?** `logger.info("order_created", extra={"order_id":..., "user_id":...})` → đẩy về ELK/Loki; query `order_id=42` ra ngay toàn bộ hành trình.
* ⚙️ **Hoạt động ra sao?** Formatter JSON biến mỗi bản ghi thành object → agent (Promtail/Filebeat) thu thập → đẩy vào kho log → index theo field để lọc/thống kê.

#### 2. Metrics & Golden Signals (Prometheus + Grafana)
* 🎯 **Dùng để làm gì?** Đo *sức khỏe hệ thống theo thời gian* bằng con số (latency, traffic, errors, saturation) để phát hiện và cảnh báo sự cố sớm.
* 💡 **Khi nào dùng?** Luôn bật cho production; nhìn 4 Golden Signals trước khi đào sâu. Logs trả lời *chuyện gì xảy ra*; metrics trả lời *có bất thường không/bất thường từ lúc nào*.
* 🏭 **Thực tế sử dụng ra sao?** App expose `/metrics` (`Counter`, `Histogram`); Prometheus scrape mỗi 15s; Grafana vẽ dashboard; Node Exporter/cAdvisor cung cấp CPU/RAM/disk của host/container; Alertmanager gửi cảnh báo Telegram/Slack.
* ⚙️ **Hoạt động ra sao?** Prometheus kiểu **pull**: định kỳ gọi HTTP vào `/metrics`, lưu chuỗi thời gian; Grafana truy vấn bằng PromQL; Alertmanager gom/chống trùng cảnh báo.

#### 3. Debug Production
* 🎯 **Dùng để làm gì?** Tìm nguyên nhân lỗi/chậm không tái hiện được ở local mà *không* làm hệ thống tệ hơn.
* 💡 **Khi nào dùng?** Khi có alert/than phiền. Quy trình: metrics (chậm từ khi nào, trùng deploy không?) → trace 1 request chậm → slow query log → CPU/RAM/connection pool → chỉ khi cần mới profile (`py-spy`).
* 🏭 **Thực tế sử dụng ra sao?** `kubectl logs <pod> --previous`, `py-spy top --pid <pid>` (không cần restart), `pg_stat_statements` tìm query chậm; luôn ưu tiên *giảm thiểu tác động* (rollback) trước khi tìm nguyên nhân gốc.
* ⚙️ **Hoạt động ra sao?** Thu hẹp theo tầng (mạng → app → DB → hạ tầng) dựa trên dữ liệu thay vì đoán; `py-spy` lấy mẫu stack của process đang chạy để thấy hàm nào tốn thời gian.

#### 4. Distributed Tracing & SLO-based Alerting
* 🎯 **Dùng để làm gì?** Tracing: thấy 1 request đi qua nhiều service mất bao lâu ở từng chặng. SLO alerting: chỉ báo khi thực sự đe dọa cam kết chất lượng, tránh alert fatigue.
* 💡 **Khi nào dùng?** Tracing khi có ≥2 service (microservices). SLO alerting khi team bị spam cảnh báo CPU/RAM vô thưởng và đã có SLO/SLA rõ ràng.
* 🏭 **Thực tế sử dụng ra sao?** OpenTelemetry gắn `trace_id` vào header, Jaeger hiển thị "cây span"; alert theo *tốc độ tiêu thụ error budget* (vd "dùng hết 2% ngân sách tháng trong 1 giờ") thay vì "CPU > 80%".
* ⚙️ **Hoạt động ra sao?** Mỗi service tạo 1 *span* (bắt đầu/kết thúc) cùng `trace_id`, gửi về collector; UI ghép thành biểu đồ thác nước. Error budget = 100% − SLO (vd SLO 99.9% → được lỗi 0.1%).

<details>
<summary>📖 Diễn giải bổ sung & code minh họa</summary>

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

</details>

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Virtualization (VM) vs Containerization (Docker)
* 🎯 **Dùng để làm gì?** Đóng gói ứng dụng kèm đầy đủ môi trường thực thi (Dependencies, System Libraries, Config) để đảm bảo "chạy đúng trên máy dev thì chắc chắn chạy đúng trên production".
* 💡 **Khi nào dùng?** Dùng Container (Docker) cho 95% dự án Microservices, Web APIs hiện đại. Dùng Virtualization (VMware/KVM) khi cần cô lập phần cứng tuyệt đối (Multi-tenant Security), hoặc chạy các OS Kernel khác nhau trên cùng Host.
* 🏭 **Thực tế sử dụng ra sao?**
  - VM: Nặng vài GB, khởi động tính bằng phút (chạy cả OS kernel riêng).
  - Docker Container: Nặng vài MB/GB, khởi động trong 1-2 giây (dùng chung Linux Host Kernel).
* ⚙️ **Hoạt động ra sao?** Docker dùng 2 tính năng có sẵn của Linux Kernel: **cgroups** (giới hạn tài nguyên CPU/RAM) và **namespaces** (cô lập Process ID, Network, Filesystem, User ID).

#### 2. Docker Multi-Stage Build & Layer Caching Optimization
* 🎯 **Dùng để làm gì?** Giảm kích thước Image từ vài GB xuống còn vài chục MB và tăng tốc độ Build Image gấp 10 lần nhờ tối ưu Layer Caching.
* 💡 **Khi nào dùng?** Bắt buộc cho mọi ứng dụng Production để giảm cước phí lưu trữ Container Registry và tăng tốc Deployment CI/CD.
* 🏭 **Thực tế sử dụng ra sao?**
  ```dockerfile
  # Stage 1: Build stage (Chứa đầy đủ Compiler & Dev Header)
  FROM python:3.11 AS builder
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --user --no-cache-dir -r requirements.txt

  # Stage 2: Runtime stage (Chỉ giữ lại binary nhẹ nhất)
  FROM python:3.11-slim
  WORKDIR /app
  COPY --from=builder /root/.local /root/.local
  COPY --from=builder /app .
  ENV PATH=/root/.local/bin:$PATH
  CMD ["gunicorn", "app:app", "-w", "4", "-b", "0.0.0.0:5000"]
  ```
* ⚙️ **Hoạt động ra sao?** Mỗi lệnh trong Dockerfile (`COPY`, `RUN`) tạo ra một Read-Only Image Layer. Docker chỉ rebuild lại layer khi file nguồn của layer đó thay đổi. Copy `requirements.txt` và `pip install` TRƯỚC khi `COPY . .` giúp tận dụng cache layer khi sửa source code Python.

#### 3. Docker Volume Persistence & Compose Internal DNS
* 🎯 **Dùng để làm gì?** Lưu giữ dữ liệu bền vững (Data Persistence) cho Database/Upload files vượt ngoài vòng đời Container và cho phép các Container giao tiếp nội bộ qua tên Service.
* 💡 **Khi nào dùng?** Khi chạy các Service có trạng thái (Stateful) như Postgres, Redis, MinIO trong Docker.
* 🏭 **Thực tế sử dụng ra sao?**
  ```yaml
  version: '3.8'
  services:
    web:
      build: .
      environment:
        - DB_HOST=db  # Docker Compose tự resolve DNS 'db' -> IP Container db
      depends_on: [db]
    db:
      image: postgres:15
      volumes:
        - postgres_data:/var/lib/postgresql/data
  volumes:
    postgres_data:    # Data còn nguyên ngay cả khi container db bị hủy
  ```
* ⚙️ **Hoạt động ra sao?** Docker Volume mount trực tiếp một thư mục trên Host OS (`/var/lib/docker/volumes/`) vào bên trong Container Filesystem, bypass qua Storage Driver layer của Docker nên đạt tốc độ I/O đĩa tối đa.

#### 4. Load Balancer Layer 4 (Transport) vs Layer 7 (Application)
* 🎯 **Dùng để làm gì?** Phân phối lưu lượng truy cập HTTP/TCP đến danh sách Backend Servers để chịu tải và nâng cao tính sẵn sàng (High Availability).
* 💡 **Khi nào dùng?** 
  - **Layer 4 (TCP/UDP):** Chọn khi làm Database Proxy (PgBouncer), Gaming Server, DNS, hoặc cần throughput cực khủng (triệu req/s) mà không quan tâm nội dung HTTP payload.
  - **Layer 7 (HTTP/HTTPS):** Chọn cho Web APIs, Microservices cần Path-based routing (`/api` -> Service A, `/auth` -> Service B), SSL Termination, Cookie Sticky Sessions.
* 🏭 **Thực tế sử dụng ra sao?** Layer 4: AWS NLB (Network Load Balancer). Layer 7: Nginx, Traefik, HAProxy, AWS ALB (Application Load Balancer).
* ⚙️ **Hoạt động ra sao?** Layer 4 chỉ mở header TCP (IP + Port) để forwarding gói tin (packet fast-forwarding). Layer 7 giải mã hoàn toàn HTTP/HTTPS Request (Terminates SSL), đọc Header, Path, Cookies rồi mới thiết lập 1 Connection mới tới Backend Server.

**Đọc chi tiết:** [`10-DevOps-Architect/Docker_Kubernetes_Mastery.md`](../10-DevOps-Architect/Docker_Kubernetes_Mastery.md) (phần Docker). Network troubleshooting: [`10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md`](../10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md).

### 🛠️ Hướng dẫn thực hành từng bước (Bài tập FL-04, DO-01, DO-02 & LAB-01):

#### 1. Thực hành FL-04 — Dockerize Flask App:
- **Tạo Dockerfile:**
  ```dockerfile
  FROM python:3.11-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt gunicorn
  COPY . .
  CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
  ```
- **Build & Run:** `docker build -t flask-app:v1 .` -> `docker run -d -p 5000:5000 --name flask_running flask-app:v1`.

#### 2. Thực hành DO-01 — Docker Compose & Persistence Volume:
- **Khai báo `docker-compose.yml` (Flask + Postgres + Redis):**
  ```yaml
  version: '3.8'
  services:
    web:
      build: .
      ports: ["5000:5000"]
      environment: [- DATABASE_URL=postgresql://user:pass@db:5432/mydb]
      depends_on: [db]
    db:
      image: postgres:15-alpine
      environment: {POSTGRES_USER: user, POSTGRES_PASSWORD: pass, POSTGRES_DB: mydb}
      volumes: [postgres_data:/var/lib/postgresql/data]
  volumes:
    postgres_data:
  ```
- **Verify Persistence:** `docker-compose up -d` -> Tạo dữ liệu -> `docker-compose down` -> `docker-compose up -d` -> Verify dữ liệu vẫn còn nguyên vẹn trong Named Volume.

#### 3. Thực hành DO-02 — Debug Startup Failure:
- **Cố tình đổi pass DB:** `docker-compose up -d` -> Container web crash -> Debug qua `docker logs flask_app_web_1` -> Thấy lỗi DB connection auth failure -> Khắc phục lại pass.

#### 4. Thực hành LAB-01 — Xử lý lỗi `No space left on device`:
- **Tạo rác ổ đĩa:** `dd if=/dev/zero of=huge.img bs=1M count=2000`
- **Debug & Cleanup:** `df -h` kiểm tra -> `du -sh /* | sort -rh | head -n 5` tìm file rác -> Dọn dẹp Docker bằng `docker system prune -a --volumes`. Dẫn chiếu thực hành: [`03-DevOps-Exercises/Checklist_Bai_Tap.md`](03-DevOps-Exercises/Checklist_Bai_Tap.md).

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

**Giải thích chi tiết chuyên sâu:**

🟢 *Cơ bản.* Pipeline là chuỗi bước tự động chạy khi có sự kiện (push/PR): test → build Docker image → deploy.

#### 1. Pipeline Architecture: GitHub Actions vs GitLab CI
* 🎯 **Dùng để làm gì?** Tự động hóa toàn bộ chuỗi kiểm thử, đóng gói và triển khai ứng dụng (CI/CD Pipeline) mỗi khi có thay đổi code, đảm bảo chất lượng phần mềm đồng nhất và loại bỏ sai sót thủ công.
* 💡 **Khi nào dùng?** Bắt buộc dùng cho mọi dự án phát triển phần mềm hiện đại từ cá nhân tới Enterprise.
* 🏭 **Thực tế sử dụng ra sao?**
  - **GitHub Actions:** Sử dụng `.github/workflows/ci.yml` khai báo các Workflows -> Jobs -> Steps. Tích hợp sâu với GitHub Pull Requests.
  - **GitLab CI:** Sử dụng `.gitlab-ci.yml` khai báo `stages` -> `jobs` -> `script`. Rất mạnh về Self-hosted runner và On-premise deployment.
* ⚙️ **Hoạt động ra sao?** Khi nhận Event (Push/PR), Webhook kích hoạt CI Server khởi tạo Container/VM Runner sạch, checkout code, thực thi lần lượt các câu lệnh trong `script`/`run` và trả trạng thái (Success/Failed) về cho PR/Commit.

#### 2. Matrix Builds & Cache Dependency Optimization
* 🎯 **Dùng để làm gì?** Chạy kiểm thử song song trên nhiều phiên bản môi trường (Python 3.10, 3.11, 3.12) và tăng tốc thời gian thực thi CI Pipeline nhờ bộ nhớ tạm (Cache).
* 💡 **Khi nào dùng?** Dùng Matrix Build khi duy trì Thư viện/Open Source/SDK cần tương thích nhiều bản runtime. Dùng Caching trong mọi pipeline để tiết kiệm băng thông và chi phí runner.
* 🏭 **Thực tế sử dụng ra sao?**
  ```yaml
  jobs:
    test:
      runs-on: ubuntu-latest
      strategy:
        matrix:
          python-version: ["3.10", "3.11"]  # Chạy song song 2 job độc lập
      steps:
        - uses: actions/checkout@v4
        - uses: actions/setup-python@v5
          with:
            python-version: ${{ matrix.python-version }}
            cache: "pip"                   # Tự động cache pip packages theo hash requirements.txt
        - run: pip install -r requirements.txt
        - run: pytest
  ```
* ⚙️ **Hoạt động ra sao?** Matrix sinh ra một đồ thị công việc (Job Graph) chạy song song trên các Worker node khác nhau. Cache lưu trữ thư mục `~/.cache/pip` lên Storage của CI Server và tự động khôi phục (Restore) ở lần chạy tiếp theo dựa trên Cache Key (MD5 Hash của file `requirements.txt`).

#### 3. Security Scanning: SAST vs SCA trong Production Pipeline
* 🎯 **Dùng để làm gì?** Phát hiện lỗ hổng bảo mật ngay trong quá trình phát triển (Shift-Left Security), ngăn chặn mã độc hoặc thư viện dính lỗi CVE lọt vào Production.
* 💡 **Khi nào dùng?** Tích hợp làm bước bắt buộc (Quality Gate) trong Pipeline trước khi cho phép Merge code vào nhánh `main` hoặc `production`.
* 🏭 **Thực tế sử dụng ra sao?**
  - **SAST (Static Application Security Testing):** Dùng Bandit (`bandit -r .`) quét trực tiếp code Python tìm lỗi nối chuỗi SQL, dùng hardcoded passwords.
  - **SCA (Software Composition Analysis):** Dùng Safety (`safety check`) hoặc Dependabot quét file `requirements.txt` tìm các package đang dùng bị dính lỗ hổng công bố công khai.
* ⚙️ **Hoạt động ra sao?** Công cụ phân tích cú pháp (AST Parser) hoặc đối chiếu bảng băm hash của dependency với cơ sở dữ liệu lỗi (NVD - National Vulnerability Database). Nếu mức độ nghiêm trọng vượt ngưỡng (High/Critical), Job CI trả về trạng thái Exit Code 1 và khóa việc Deploy.

#### 4. Secrets Security & Self-Hosted Runner Infrastructure
* 🎯 **Dùng để làm gì?** Bảo vệ tuyệt đối thông tin nhạy cảm (API Keys, SSH Keys, Database Passwords) và cho phép chạy CI/CD trong mạng nội bộ kín (Private VPC/On-Premise).
* 💡 **Khi nào dùng?** Dùng Secrets cho 100% biến môi trường nhạy cảm. Dùng Self-Hosted Runner khi ứng dụng cần truy cập DB nội bộ không mở IP ra Internet hoặc cần Server có GPU/RAM cực khủng.
* 🏭 **Thực tế sử dụng ra sao?** Khai báo trong GitHub Settings -> Secrets. Trong YAML truy xuất qua `${{ secrets.DOCKER_PASSWORD }}`. Giá trị này tự động bị mã hóa masking (`***`) trong toàn bộ màn hình Console Logs của CI.
* ⚙️ **Hoạt động ra sao?** Runner tự quản lý thiết lập một luồng Long-Polling WebSocket bảo mật đi TỪ TRONG MẠNG NỘI BỘ RA NGOÀI tới GitHub API. Do đó, Firewall nội bộ KHÔNG CẦN mở bất kỳ Inbound Port nào mà vẫn nhận được lệnh Build an toàn.

**Đọc chi tiết:** tài liệu CI/CD trong [`10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md`](../10-DevOps-Architect/DevOps_Roadmap_9_HocPhan.md) — Học phần 6.

### 🛠️ Hướng dẫn thực hành từng bước (Bài tập DO-03, DO-04 & LAB-04):

#### 1. Thực hành DO-03 — CI Pipeline Automation với GitHub Actions:
- **Tạo workflow `.github/workflows/ci.yml`:**
  ```yaml
  name: Python Backend CI
  on: [push, pull_request]
  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with: {python-version: '3.11'}
      - run: pip install -r requirements.txt pytest flake8
      - run: flake8 . --max-line-length=100
      - run: pytest
      - run: docker build -t myapp:${{ github.sha }} .
  ```
- **Push & Verify:** Push lên GitHub và xem tab Actions xanh hết các bước.

#### 2. Thực hành DO-04 — Continuous Deployment (CD) via SSH:
- **Thêm secrets:** `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `HOST_IP`, `SSH_PRIVATE_KEY` vào Repo Settings.
- **Bổ sung CD step vào workflow:**
  ```yaml
      - uses: docker/build-push-action@v4
        with: {push: true, tags: "${{ secrets.DOCKER_USERNAME }}/app:latest"}
      - uses: appleboy/ssh-action@v0.1.10
        with:
          host: ${{ secrets.HOST_IP }}
          username: ubuntu
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          script: |
            docker pull ${{ secrets.DOCKER_USERNAME }}/app:latest
            docker stop app || true && docker rm app || true
            docker run -d -p 5000:5000 --name app ${{ secrets.DOCKER_USERNAME }}/app:latest
  ```

#### 3. Thực hành LAB-04 — Debug CI Build Fail:
- **Cố tình đổi dependency lỗi trong `requirements.txt`:** Push code -> Tab Actions báo đỏ ở step `Install Dependencies` -> Đọc log pip error -> Sửa lại version đúng -> Push lại. Dẫn chiếu thực hành: [`03-DevOps-Exercises/Checklist_Bai_Tap.md`](03-DevOps-Exercises/Checklist_Bai_Tap.md).

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

**Giải thích chi tiết chuyên sâu:**

#### 1. AWS Cloud Core Infrastructure (EC2, S3, VPC & GCP Equivalents)
* 🎯 **Dùng để làm gì?** Cung cấp tài nguyên ảo hóa linh hoạt (Compute, Storage, Networking) trên đám mây để vận hành hệ thống phần mềm mà không cần đầu tư máy chủ vật lý (Datacenter).
* 💡 **Khi nào dùng?** Dùng EC2 khi cần tự do cài đặt OS/Runtime. Dùng S3 cho file tĩnh/Upload/Backup. Dùng VPC để cô lập mạng bảo mật cho dự án.
* 🏭 **Thực tế sử dụng ra sao?**
  - **AWS ↔ GCP Mapping:** EC2 ↔ Compute Engine | S3 ↔ Cloud Storage | VPC ↔ VPC | RDS ↔ Cloud SQL | EKS ↔ GKE | Lambda ↔ Cloud Functions.
* ⚙️ **Hoạt động ra sao?** AWS phân chia theo Region (vùng địa lý) và Availability Zone (AZ - Datacenter vật lý cô lập điện/mạng). VPC tạo một dải mạng ảo riêng (`10.0.0.0/16`) nằm trên các AZs để bảo mật traffic nội bộ.

#### 2. Network & Identity Security: Security Groups & IAM Least Privilege
* 🎯 **Dùng để làm gì?** Bảo vệ máy chủ EC2 ở tầng Network và kiểm soát quyền hạn thao tác API (Who can access What) ở tầng Identity.
* 💡 **Khi nào dùng?** Áp dụng ngay khi khởi tạo bất kỳ tài nguyên Cloud nào.
* 🏭 **Thực tế sử dụng ra sao?**
  - **IAM Policy chuẩn Least Privilege:**
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
* ⚙️ **Hoạt động ra sao?** Security Group đóng vai trò là **Stateful Firewall** gắn ở tầng Network Interface (ENI) của EC2 (nếu cho phép Inbound Port 80 thì Outbound tự động được phép). IAM băm hóa Signature của Request bằng Access/Secret Key để verify quyền hạn với IAM Policy trước khi cho phép gọi AWS API.

#### 3. AWS API Gateway & Thảm họa 29s Hard Timeout
* 🎯 **Dùng để làm gì?** Đóng vai trò làm Single Entry Point cho toàn bộ hệ thống APIs, quản lý Routing, Throttling, Authentication, CORS và API Versioning.
* 💡 **Khi nào dùng?** Khi làm kiến trúc Microservices, Serverless APIs (Lambda).
* 🏭 **Thực tế sử dụng ra sao?**
  - ⚠️ **Sự cố 29s Timeout:** API Gateway trả về `HTTP 504 Gateway Timeout` cứng nếu backend xử lý quá 29 giây.
  - ✅ **Giải pháp:** Đối với tác vụ nặng (Export Excel 100k dòng, gửi email hàng loạt), API Gateway nộp công việc vào **AWS SQS** hoặc **Celery Redis Queue**, trả ngay `202 Accepted` cho Frontend kèm `job_id`, xử lý ngầm dưới Background Worker.
* ⚙️ **Hoạt động ra sao?** API Gateway nhận HTTP Request từ Client, thực thi Custom Authorizer (JWT), kiểm tra Quotas/Rate limits, biến đổi Header/Payload nếu cần rồi mới proxy tới HTTP Backend / AWS Lambda.

#### 4. AWS Cost Optimization Strategy
* 🎯 **Dùng để làm gì?** Tối ưu chi phí hạ tầng Cloud hàng tháng, giảm từ 30% đến 70% bill AWS mà không làm giảm hiệu năng hệ thống.
* 💡 **Khi nào dùng?** Áp dụng bắt buộc khi ứng dụng lên giai đoạn Production ổn định.
* 🏭 **Thực tế sử dụng ra sao?**
  - **On-Demand Instance:** Trả tiền theo giờ/giây. Dùng cho dự án thử nghiệm, tải biến động không đoán trước.
  - **Reserved Instances (RI) / Savings Plans:** Cam kết sử dụng 1 hoặc 3 năm. Tiết kiệm tới 60-72%. Dùng cho Production DB, Master Nodes chạy 24/7.
  - **Spot Instances:** Dùng tài nguyên dư thừa của AWS với giá rẻ tới 90%, nhưng có thể bị AWS thu hồi trước 2 phút. Dùng cho Celery Batch Workers, CI/CD Runner, ML Training.
* ⚙️ **Hoạt động ra sao?** AWS Billing Engine tính toán dựa trên mức độ cam kết tài nguyên trong tài khoản. Nếu dùng Spot Instance, daemon `ec2-spot-interrupted-notice` lắng nghe thông báo thu hồi để Graceful Shutdown worker trước khi VM bị xóa.

**Đọc chi tiết:** [`07-AWS-Mastery/AWS_90Days_Mastery_Plan.md`](../07-AWS-Mastery/AWS_90Days_Mastery_Plan.md).

### 🛠️ Hướng dẫn thực hành từng bước (Bài tập DO-05 & LAB-02):

#### 1. Thực hành DO-05 — Secret Management Hygiene:
- **Tạo `.gitignore`:** Khai báo `.env`, `*.pem`, `*.sqlite3` không commit vào Git.
- **Tích hợp `python-dotenv`:**
  ```python
  import os
  from dotenv import load_dotenv
  load_dotenv()
  SECRET_KEY = os.getenv("SECRET_KEY")
  ```

#### 2. Thực hành LAB-02 — Purge Secret khỏi Git History (`git filter-repo`):
- **Cố tình commit nhầm secret:** File `passwords.txt` bị lỡ push.
- **Cleanup Lịch sử Commit:**
  ```bash
  pip install git-filter-repo
  git filter-repo --path passwords.txt --invert-paths
  git push origin --force --all
  ```
- **Hành động bắt buộc:** Lập tức Rotate secret đã lộ. Dẫn chiếu thực hành: [`03-DevOps-Exercises/Checklist_Bai_Tap.md`](03-DevOps-Exercises/Checklist_Bai_Tap.md).

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Kubernetes Architecture: Control Plane vs Worker Node
* 🎯 **Dùng để làm gì?** Tự động hóa điều phối (Orchestration), mở rộng (Auto-scaling), tự phục hồi (Self-healing) và quản lý vòng đời hàng trăm microservices chạy trên một cụm máy chủ (Cluster).
* 💡 **Khi nào dùng?** Dùng khi hệ thống mở rộng thành nhiều Microservices chạy trên nhiều máy chủ mà Docker Compose 1 máy không chịu nổi.
* 🏭 **Thực tế sử dụng ra sao?**
  - **Control Plane (Master Node - Bộ não):** `kube-apiserver` (Cổng giao tiếp), `etcd` (Lưu trạng thái Cluster), `kube-scheduler` (Xếp Pod vào Node), `kube-controller-manager` (Duy trì mong muốn trạng thái).
  - **Worker Node (Nơi thực thi):** `kubelet` (Đại lý quản lý Container), `kube-proxy` (Mạng & Rule NAT), `containerd/cri-o` (Container Runtime).
* ⚙️ **Hoạt động ra sao?** Người dùng nộp file YAML qua `kubectl`. API Server ghi thông số vào `etcd`. Controller Manager phát hiện chênh lệch (ví dụ: mong muốn 3 Pod mà hiện có 2 Pod) và lệnh cho Scheduler chọn Node thích hợp. Kubelet tại Node đó kéo Image và khởi động Pod mới.

#### 2. K8s Core Abstractions: Pod, Deployment, Service, Namespace
* 🎯 **Dùng để làm gì?** Tạo ra các lớp trừu tượng để quản lý ứng dụng một cách khai báo (Declarative Infrastructure).
* 💡 **Khi nào dùng?** 
  - **Pod:** Đơn vị tính toán nhỏ nhất (chứa 1 hoặc nhiều container cùng namespace network).
  - **Deployment:** Quản lý bản nâng cấp (Rolling Update), Rollback và số lượng bản sao Replicas.
  - **Service:** Địa chỉ IP & DNS ảo cố định cho nhóm Pods biến động.
  - **Namespace:** Cô lập tài nguyên giữa các môi trường (dev/staging/prod) trên cùng 1 Cluster.
* 🏭 **Thực tế sử dụng ra sao?**
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata: { name: backend-api, namespace: production }
  spec:
    replicas: 3
    selector: { matchLabels: { app: backend-api } } # PHẢI KHỚP LBL BÊN DƯỚI
    template:
      metadata: { labels: { app: backend-api } }
      spec:
        containers:
        - name: api
          image: myregistry.com/backend:v1.2.0
          ports: [{ containerPort: 8000 }]
  ---
  apiVersion: v1
  kind: Service
  metadata: { name: backend-api-svc, namespace: production }
  spec:
    selector: { app: backend-api }                  # Match label trỏ tới Pods
    ports: [{ port: 80, targetPort: 8000 }]
  ```
* ⚙️ **Hoạt động ra sao?** Service lắng nghe iptables/IPVS rules được sinh ra bởi `kube-proxy`. Khi Pod bị hỏng và được tái tạo với IP mới, Service tự động cập nhật danh sách Endpoint IP thông qua Label Selector mà không làm gián đoạn kết nối của Client.

#### 3. Container Health Checks: Liveness vs Readiness Probes
* 🎯 **Dùng để làm gì?** Tự động phát hiện ứng dụng bị treo (Deadlock) hoặc ngưng nhận traffic khi chưa khởi động xong (Warming up).
* 💡 **Khi nào dùng?** Bắt buộc cấu hình cho mọi Production Container.
* 🏭 **Thực tế sử dụng ra sao?**
  - **Liveness Probe:** Trả lời "Ứng dụng còn sống không?". Nếu FAIL -> K8s restart (kill) Pod.
  - **Readiness Probe:** Trả lời "Ứng dụng sẵn sàng nhận Request chưa?". Nếu FAIL -> K8s rút Pod ra khỏi danh sách Service Endpoints (KHÔNG kill Pod).
  ```yaml
  livenessProbe:
    httpGet: { path: /healthz, port: 8000 }
    initialDelaySeconds: 15
    periodSeconds: 10
  readinessProbe:
    httpGet: { path: /ready, port: 8000 }
    initialDelaySeconds: 5
    periodSeconds: 5
  ```
* ⚙️ **Hoạt động ra sao?** Kubelet định kỳ gửi HTTP Get/TCP Socket/Exec command tới Container. Nếu số lần thất bại vượt ngưỡng `failureThreshold`, Kubelet thực hiện hành động restart hoặc rút Pod khỏi Load Balancer.

#### 4. Helm Package Manager & Ingress Gateway
* 🎯 **Dùng để làm gì?** Helm quản lý các bản phát hành K8s (Package Manager) thông qua Templating YAML. Ingress quản lý định tuyến HTTP/HTTPS Inbound ở tầng Layer 7 vào Cluster.
* 💡 **Khi nào dùng?** Dùng Helm khi cần triển khai 1 ứng dụng lên nhiều môi trường (Dev/Staging/Prod) chỉ bằng việc thay đổi file `values.yaml`. Dùng Ingress làm Single Domain Router & SSL Termination point cho Cluster.
* 🏭 **Thực tế sử dụng ra sao?** 
  - Triển khai Prometheus Stack qua Helm: `helm install prometheus prometheus-community/kube-prometheus-stack`.
  - Ingress Routing:
    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata: { name: main-ingress }
    spec:
      rules:
      - host: api.example.com
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service: { name: backend-api-svc, port: { number: 80 } }
    ```
* ⚙️ **Hoạt động ra sao?** Ingress Controller (như Nginx Ingress) lắng nghe K8s API Server. Khi có Ingress mới được nộp, Nginx Controller tự động ghi lại file `nginx.conf` bên trong Pod và thực thi `nginx -s reload` để mở đường truyền traffic công khai.

**Đọc chi tiết:** [`10-DevOps-Architect/Docker_Kubernetes_Mastery.md`](../10-DevOps-Architect/Docker_Kubernetes_Mastery.md) (phần K8s).

### 🛠️ Hướng dẫn thực hành từng bước (Bài tập DO-06 & LAB-03):

#### 1. Thực hành DO-06 — Minikube Deployment & Service:
- **Khởi động Minikube:** `minikube start`
- **Tạo Deployment & Service Manifest (`app.yaml`):**
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata: { name: flask-deployment }
  spec:
    replicas: 2
    selector: { matchLabels: { app: flask-web } }
    template:
      metadata: { labels: { app: flask-web } }
      spec:
        containers: [{ name: flask, image: "nginx:alpine", ports: [{ containerPort: 80 }] }]
  ---
  apiVersion: v1
  kind: Service
  metadata: { name: flask-service }
  spec:
    type: ClusterIP
    selector: { app: flask-web }
    ports: [{ port: 80, targetPort: 80 }]
  ```
- **Deploy & Port Forward:** `kubectl apply -f app.yaml` -> `kubectl port-forward service/flask-service 8080:80` -> Truy cập `http://localhost:8080`.

#### 2. Thực hành LAB-03 — Debug Mismatch Selector:
- **Tạo sự cố:** Sửa `selector: app: wrong-tag` trong `Service`.
- **Debug:** Lệnh `kubectl port-forward` báo lỗi hoặc `kubectl get endpoints flask-service` trả `<none>`. Sửa lại `selector` khớp với `template.labels` của Deployment. Dẫn chiếu thực hành: [`03-DevOps-Exercises/Checklist_Bai_Tap.md`](03-DevOps-Exercises/Checklist_Bai_Tap.md).

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Terraform (IaC): `plan` → `apply` → `destroy`
* 🎯 **Dùng để làm gì?** Mô tả hạ tầng (VPC, EC2, RDS...) bằng code để tạo lại y hệt, review qua PR, có lịch sử thay đổi — thay vì click tay trên Console (không lặp lại được, không audit được).
* 💡 **Khi nào dùng?** Mọi hạ tầng cloud ngoài thử nghiệm nhanh; khi cần nhiều môi trường giống nhau (dev/staging/prod). Không dùng để cấu hình *bên trong* máy (cài package, sửa file) — việc của Ansible.
* 🏭 **Thực tế sử dụng ra sao?** Khai báo `resource "aws_instance" ...` → `terraform plan` (xem trước, **luôn chạy trước apply**) → `terraform apply` → xong demo chạy `terraform destroy` để không tốn tiền.
* ⚙️ **Hoạt động ra sao?** Terraform đọc code (trạng thái **mong muốn**) + file state (trạng thái **đã tạo**) + hỏi API cloud (trạng thái **thực tế**), tính ra đồ thị phụ thuộc rồi gọi API tạo/sửa/xóa theo đúng thứ tự.

#### 2. State file, Remote State & Locking
* 🎯 **Dùng để làm gì?** State là "sổ ghi nhớ" Terraform đã tạo những gì; remote state + lock cho phép cả nhóm làm chung mà không dẫm chân nhau.
* 💡 **Khi nào dùng?** Bắt buộc khi >1 người/CI cùng chạy Terraform. State local chỉ dùng khi học cá nhân.
* 🏭 **Thực tế sử dụng ra sao?** `backend "s3" { bucket=..., key=..., dynamodb_table="tf-lock", encrypt=true }`; bật versioning cho bucket; chỉ CI/người được phép `apply` mới có quyền ghi.
* ⚙️ **Hoạt động ra sao?** Trước `apply`, Terraform ghi 1 bản ghi khóa vào DynamoDB; người thứ 2 thấy khóa sẽ phải chờ/báo lỗi → không có chuyện 2 `apply` ghi đè state của nhau. State có thể chứa secret dạng plaintext nên phải mã hóa bucket.

#### 3. Ansible: Playbook, Role & Idempotency
* 🎯 **Dùng để làm gì?** Tự động cấu hình **bên trong** nhiều máy (cài Docker, copy file, khởi động service) theo kịch bản lặp lại được.
* 💡 **Khi nào dùng?** Sau khi Terraform tạo xong máy; quản lý cấu hình VM truyền thống. Nếu toàn bộ chạy container trên K8s thì nhu cầu Ansible giảm đi.
* 🏭 **Thực tế sử dụng ra sao?** `ansible-playbook -i inventory.ini site.yml`; dùng module (`apt`, `service`, `copy`) thay vì `shell` để được idempotent; chia theo `roles/` khi playbook lớn.
* ⚙️ **Hoạt động ra sao?** Push-based: Ansible SSH vào máy đích (không cần agent), chạy từng *task*. **Idempotent**: module kiểm tra trạng thái hiện tại — đã đúng thì báo `ok` và không làm gì, chỉ `changed` khi cần sửa → chạy lại N lần vẫn cùng kết quả.

#### 4. GitOps (ArgoCD/Flux) & Drift
* 🎯 **Dùng để làm gì?** Git là *nguồn chân lý duy nhất* cho trạng thái cluster; agent trong cluster tự đồng bộ theo Git — mọi thay đổi có lịch sử, rollback chỉ là `git revert`.
* 💡 **Khi nào dùng?** Triển khai app lên Kubernetes, nhiều môi trường, cần audit/an toàn (pipeline CI không cần quyền ghi thẳng vào cluster). Hạ tầng cloud nền (VPC, EKS) vẫn do Terraform quản lý — hai công cụ bổ trợ nhau.
* 🏭 **Thực tế sử dụng ra sao?** CI build image + sửa tag trong repo manifest (Git); ArgoCD thấy khác biệt → `sync` vào cluster; ai `kubectl edit` tay sẽ bị ArgoCD phát hiện (*OutOfSync*) và có thể tự sửa lại.
* ⚙️ **Hoạt động ra sao?** Agent **pull** (không push từ ngoài), liên tục so sánh "Git khai báo" với "cluster thực tế" rồi `apply` chênh lệch — giống `terraform plan` chạy liên tục. Drift = thực tế lệch khỏi khai báo do sửa tay.

<details>
<summary>📖 Diễn giải bổ sung & code minh họa</summary>

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Zero-Downtime Deployment Strategies: Rolling vs Blue-Green vs Canary
* 🎯 **Dùng để làm gì?** Cập nhật phiên bản phần mềm mới lên môi trường Production mà không gây gián đoạn dịch vụ (Zero Downtime) và tối thiểu rủi ro sự cố.
* 💡 **Khi nào dùng?** 
  - **Rolling Update:** Mặc định cho Web APIs thông thường (Thay thế dần Pod cũ bằng Pod mới).
  - **Blue-Green:** Khi triển khai nâng cấp Database Schema phức tạp hoặc ứng dụng đòi hỏi khả năng Instant Rollback trong 1 giây.
  - **Canary:** Khi ra mắt tính năng lớn cho ứng dụng có hàng triệu User, mở dần 5% -> 25% -> 100% traffic để kiểm tra tỉ lệ lỗi thực tế.
* 🏭 **Thực tế sử dụng ra sao?**
  ```yaml
  # Rolling Update trong Kubernetes Manifest
  spec:
    strategy:
      type: RollingUpdate
      rollingUpdate:
        maxUnavailable: 1  # Tối đa 1 pod cũ ngắt kết nối
        maxSurge: 1        # Tối đa 1 pod mới được dựng thêm
  ```
* ⚙️ **Hoạt động ra sao?** Rolling Update gỡ 1 Pod cũ và thêm 1 Pod mới cho đến khi hoàn tất. Blue-Green duy trì 2 cụm độc lập (Blue = v1, Green = v2) và hoán đổi DNS/Load Balancer target group. Canary dùng Service Mesh (Istio) phân luồng Weighted Traffic (`weight: 5%` sang v2, `weight: 95%` sang v1).

#### 2. Incident Response Workflow: Alerting -> Mitigation -> Resolution
* 🎯 **Dùng để làm gì?** Phản ứng chuẩn xác, bình tĩnh và nhanh chóng khi sự cố sập hệ thống xảy ra trên Production để cứu dịch vụ về trạng thái hoạt động trong thời gian ngắn nhất.
* 💡 **Khi nào dùng?** Áp dụng ngay khi PagerDuty / Telegram / Slack nổ chuông cảnh báo P0/P1 Incident.
* 🏭 **Thực tế sử dụng ra sao?**
  - **Quy trình 4 bước:**
    1. **Phát hiện & Xác nhận (Detection):** Đọc Golden Signals (Error rate > 5%, Latency spike).
    2. **Giảm thiểu tác động (Mitigation - QUAN TRỌNG NHẤT):** Rollback phiên bản mới nhất về phiên bản cũ ngay lập tức, tắt Feature Flag, hoặc scale up tài nguyên. KHÔNG ĐƯỢC cố ngồi tìm nguyên nhân gốc (RCA) trong khi dịch vụ vẫn đang sập.
    3. **Điều tra nguyên nhân gốc (Root Cause Analysis - RCA):** Đọc Log, Trace ID, Git CommitDiff sau khi dịch vụ đã ổn định.
    4. **Thông báo (Communication):** Cập nhật Status Page công khai cho khách hàng.
* ⚙️ **Hoạt động ra sao?** On-call Engineer nhận thông báo -> Kích hoạt Incident Command Structure -> Thực hiện lệnh `kubectl rollout undo` hoặc bật Maintenance Mode -> Theo dõi Grafana khôi phục lại 200 OK -> Đóng Incident ticket.

#### 3. Blameless Postmortem & Văn hóa 5 Whys
* 🎯 **Dùng để làm gì?** Học hỏi từ thất bại sản xuất, nâng cấp quy trình hạ tầng/code để đảm bảo CÙNG MỘT LỖI SẼ KHÔNG BAO GIỜ LẶP LẠI.
* 💡 **Khi nào dùng?** Thực hiện trong vòng 48h sau khi sự cố P0/P1 đã được khắc phục hoàn toàn.
* 🏭 **Thực tế sử dụng ra sao?**
  - **Mô hình 5 Whys (5 Câu hỏi Tại sao):**
    - Sập DB? -> Vì quá tải connection.
    - Tại sao quá tải connection? -> Vì API `/search` bị nổ request.
    - Tại sao API nổ request? -> Vì thiếu Rate Limiting Throttling.
    - Tại sao thiếu Throttling? -> Vì PR không qua bước Review Security Checklist. -> **Action Item:** Thêm Linter & PR Template bắt buộc Check Rate Limit.
* ⚙️ **Hoạt động ra sao?** Biên bản Postmortem Blameless tuyệt đối KHÔNG chỉ trích cá nhân "Dev A code dở làm sập". Thay vào đó, tập trung vào **lỗ hổng hệ thống và quy trình** đã cho phép code lỗi lọt qua CI/CD lên Production.

#### 4. Chaos Engineering & Diễn tập Game Days
* 🎯 **Dùng để làm gì?** Chủ động tạo ra các đợt đứt gãy hạ tầng giả lập (Kill random Pods, Inject latency network, sập Redis) để kiểm thử tính chịu lỗi (Resilience) của hệ thống thực tế.
* 💡 **Khi nào dùng?** Diễn tập định kỳ (Game Day) trên môi trường Staging/Production vào khung giờ thấp điểm.
* 🏭 **Thực tế sử dụng ra sao?** Sử dụng các công cụ như **Chaos Mesh** hay **LitmusChaos** trong K8s để inject fault.
* ⚙️ **Hoạt động ra sao?** Chaos Agent phát ngẫu nhiên lệnh kill Pod trong Cluster. Nếu hệ thống thiết kế đúng (có Replicas=3, Health check đúng, Circuit Breaker chuẩn), Load Balancer tự động chuyển traffic sang 2 Pod còn lại và User KHÔNG nhận thấy bất kỳ lỗi nào.

**Đọc chi tiết:** [`Mastery/Cloud-DevOps-Mastery/04-CICD-Deployment-Strategies`](../Mastery/Cloud-DevOps-Mastery/04-CICD-Deployment-Strategies).

### 🛠️ Hướng dẫn thực hành từng bước (Bài tập LAB-05):

#### 1. Thực hành LAB-05 — Debug & Fix Race Condition (Transaction Locking):
- **Giả lập sự cố:** 2 request concurrent cùng giảm tồn kho `inventory = inventory - 1` không dùng Lock -> Tồn kho giảm sai (Lost update).
- **Khắc phục bằng Pessimistic Locking trong Django (`select_for_update`):**
  ```python
  from django.db import transaction

  with transaction.atomic():
      # Lock row trong Database trong suốt transaction (FOR UPDATE)
      product = Product.objects.select_for_update().get(id=1)
      product.inventory -= 1
      product.save()
  ```
- **Verify:** Chạy script gửi 50 concurrent requests đạn đồng thời -> Verify inventory tính chuẩn xác 100%. Dẫn chiếu thực hành: [`03-DevOps-Exercises/Checklist_Bai_Tap.md`](03-DevOps-Exercises/Checklist_Bai_Tap.md).

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Quy trình 5 bước Chinh phục Phỏng vấn System Design (System Design Framework)
* 🎯 **Dùng để làm gì?** Giúp ứng viên dẫn dắt buổi phỏng vấn thiết kế hệ thống một cách chủ động, bài bản, tránh bẫy vẽ sơ đồ phức tạp quá sớm mà không hiểu rõ bối cảnh.
* ⏰ **Khi nào sử dụng?** Áp dụng trực tiếp trong vòng phỏng vấn System Design (45-60 phút) cho các vị trí Middle/Senior Backend & DevOps Engineer.
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  * **Bước 1 — Clarify Requirements (5 phút):** Làm rõ Functional (tính năng) & Non-Functional (QPS, DAU, Latency, Storage, Consistency).
  * **Bước 2 — Back-of-the-envelope Estimation (5 phút):** Tính toán dung lượng RAM, Disk, Bandwidth (QPS * KB/request) để chọn kích thước Cluster.
  * **Bước 3 — High-Level Design (10 phút):** Vẽ sơ đồ tổng quan `Client` ➔ `CDN/DNS` ➔ `API Gateway / Load Balancer` ➔ `App Instances` ➔ `Distributed Cache (Redis)` ➔ `Database (Primary/Replica)`.
  * **Bước 4 — Deep Dive (15-20 phút):** Đi sâu vào 1-2 điểm nghẽn khó nhất (Data Schema, Sharding Key, Chống Race Condition, Rate Limiter).
  * **Bước 5 — Identify Bottlenecks & Trade-offs (5 phút):** Chủ động tự chỉ ra điểm yếu của thiết kế (SPOF - Single Point of Failure) và hướng khắc phục.
* ⚙️ **Cơ chế hoạt động ra sao?** Nhà tuyển dụng không tìm kiếm một "đáp án đúng duy nhất" mà đánh giá tư duy kỹ thuật dựa trên **khả năng phân tích Trade-off** và **bộ câu hỏi Clarifying Questions** mà ứng viên đặt ra.

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

🔴 **Chuyên sâu / Thực chiến:** Câu hỏi "Khi nào chọn Django, khi nào chọn Flask/FastAPI" — chuẩn bị câu trả lời có chiều sâu dựa trên quy mô dự án, kiến trúc (Batteries-included vs Microservice), hiệu năng I/O và time-to-market, dùng chính note DJ-04 đã làm ở Chương 5.

**Giải thích chi tiết chuyên sâu:**

#### 1. Phương pháp Trả lời Lý thuyết & So sánh Framework (Django vs Flask vs FastAPI)
* 🎯 **Dùng để làm gì?** Giúp ứng viên thể hiện tư duy kỹ sư Middle/Senior qua khả năng phân tích Trade-off, lựa chọn đúng công cụ theo quy mô và bối cảnh dự án thay vì học thuộc lòng định nghĩa suông.
* ⏰ **Khi nào sử dụng?** Áp dụng ngay trong vòng phỏng vấn kỹ thuật (Technical Interview) khi được hỏi các câu hỏi lý thuyết cốt lõi ("Tại sao chọn X thay vì Y", "GIL là gì", "N+1 Problem fix thế nào").
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  * **Công thức trả lời chuẩn Senior:** `Định nghĩa ngắn gọn` ➔ `Ví dụ thực tế đã làm trong dự án` ➔ `Trade-off & Giới hạn kỹ thuật`.
  * **Khi so sánh Framework:**
    * **Django:** "Batteries-included" — Dùng cho sản phẩm Monolith, E-commerce, ERP cần làm nhanh (Time-to-market), có sẵn ORM, Auth, Admin UI.
    * **Flask / FastAPI:** "Micro-framework" — Dùng cho Microservices, High-performance Async APIs, AI/ML Serving nhờ khả năng tùy biến cao và tối ưu bộ nhớ.
* ⚙️ **Cơ chế hoạt động ra sao?**
  * Nhà tuyển dụng đánh giá ứng viên dựa trên **Rủi ro khi tuyển dụng**: Người trả lời kèm ví dụ thực tế và chỉ ra được điểm yếu của giải pháp chứng tỏ đã trực tiếp chinh chiến Production, không phải học vẹt qua sách vở.

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Xây dựng Project Portfolio & Kể chuyện Kỹ thuật theo Mô hình STAR
* 🎯 **Dùng để làm gì?** 
  * Project Portfolio là bằng chứng sản phẩm thật (Show, don't tell) minh chứng cho kỹ năng làm Backend/DevOps.
  * Mô hình **STAR** (Situation - Task - Action - Result) giúp cấu trúc câu trả lời phỏng vấn kinh nghiệm thực tế một cách chuyên nghiệp, thuyết phục.
* ⏰ **Khi nào sử dụng?** Dùng khi viết CV, chuẩn bị GitHub Repository cá nhân và trả lời các câu hỏi phỏng vấn hành vi / kinh nghiệm thực tế (Behavioral / Experience Questions).
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  * **Portfolio Chuẩn:** Không làm Web Todo App đơn giản. Phải ghép Django REST API (Auth/Business) + Redis (Cache/Limiter) + Celery (Async Task) + Docker/K8s + GitHub Actions CI/CD + Prometheus Logging. Có file `README.md` mô tả Architecture Diagram, API Docs và Runbook cách chạy `docker-compose up`.
  * **STAR Method:**
    * **S (Situation):** Bối cảnh sự cố / yêu cầu (VD: API checkout bị châm 3s lúc Peak Traffic).
    * **T (Task):** Nhiệm vụ của bạn (VD: Giảm Latency xuống dưới 300ms và không làm rớt order).
    * **A (Action):** Hành động kỹ thuật cụ thể (VD: Dùng `cProfile` phát hiện N+1 query ➔ Thêm `select_related` + Redis Cache-aside).
    * **R (Result):** Kết quả đo lường được (VD: Latency giảm từ 3.2s xuống 180ms, Throughput tăng 4x).
* ⚙️ **Cơ chế hoạt động ra sao?** Nhà tuyển dụng đánh giá năng lực giải quyết vấn đề qua con số định lượng (Metrics) ở bước **Result** và các quyết định kiến trúc cụ thể ở bước **Action**.

<details>
<summary>📚 Nội dung đầy đủ từ tài liệu gốc (bấm để mở)</summary>

> ⚠️ **Lưu ý quan trọng:** Các dự án dưới đây (eCommerce Migration, Viet Kiosk, MBW Suite, Traditional Medicine Platform) là **ví dụ mẫu từ tài liệu tham khảo trong repo — KHÔNG phải dự án thật của bạn**. Dùng để học **CÁCH trình bày** 1 dự án trong phỏng vấn (kiến trúc, câu hỏi hay gặp, code pattern, khung STAR), không phải để học thuộc nội dung cụ thể rồi nhận là của mình — người phỏng vấn senior sẽ hỏi xoáy sâu chi tiết thật ("con số cụ thể là bao nhiêu?") và lộ ngay nếu không phải trải nghiệm thật. Hãy áp dụng đúng KHUNG này cho dự án thật của chính bạn (hoặc project portfolio tự xây ở Chương 22).
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

**"Làm sao integrate 6+ microservices trong 1 platform?"** → Dùng API Gateway làm cổng vào duy nhất (xử lý authentication/permissions/routing); các service con giao tiếp qua gRPC hoặc REST API nội bộ, dùng Message Queue (RabbitMQ/Kafka) cho event-driven communication.

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

**Giải thích chi tiết chuyên sâu:**

#### 1. Chiến lược Đàm phán Lương & Định hình Giá trị Bản thân (Career Growth)
* 🎯 **Dùng để làm gì?** Tối đa hóa Total Compensation (Lương cứng, Thưởng, Remoteness, Học tập) và chọn đúng thời điểm chuyển việc/thăng tiến để tối ưu hóa sự nghiệp.
* ⏰ **Khi nào sử dụng?** Khi bắt đầu tìm kiếm cơ hội mới, chuẩn bị đàm phán sau khi nhận Written Offer hoặc trong các đợt Review thăng tiến hàng năm (Performance Review).
* 🏢 **Thực tế doanh nghiệp dùng như thế nào?**
  * **Nguyên tắc Đàm phán thực chiến:**
    1. **Không né tránh nhưng không đưa con số cụ thể trước:** Hỏi ngược lại Range của công ty ("Range ngân sách cho vị trí này là bao nhiêu?").
    2. **Đòn bẩy mạnh nhất là Multi-Offers:** Đi phỏng vấn 2-3 nơi cùng lúc để có phương án dự phòng thực tế.
    3. **Định giá theo Rủi ro:** Công ty trả lương theo **chi phí thay thế bạn** và **quy mô thiệt hại khi bạn nghỉ việc**, không phải số giờ bạn ngồi làm việc.
* ⚙️ **Cơ chế hoạt động ra sao?** Nhà tuyển dụng sẽ luôn chọn mức lương thấp nhất trong khoảng kỳ vọng của bạn. Do đó, mức thấp nhất trong Range bạn đưa ra phải là mức bạn **hoàn toàn hài lòng** nếu nhận offer.

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
