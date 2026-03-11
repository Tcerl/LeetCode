# 🎯 Tài Liệu Ôn Tập Phỏng Vấn — Odoo ERP Developer

> **Ứng viên:** Phạm Duy Tín | **Vị trí:** Odoo ERP Developer
> **Cấu trúc:** Cơ bản → Trung bình → Nâng cao

---

## 📊 Phân Tích GAP: CV vs JD

| Kỹ năng JD yêu cầu | Trạng thái CV | Mức độ cần chuẩn bị |
|---|---|---|
| Python (backend) | ✅ Flask, SQLAlchemy | 🟡 Cần nâng lên Odoo ORM |
| PostgreSQL | ✅ Đã có kinh nghiệm | 🟢 Ôn query nâng cao |
| JavaScript / Frontend | ✅ jQuery, Backbone, Next.js | 🟡 Cần học Odoo OWL/QWeb |
| XML (Odoo views) | ❌ Chưa có | 🔴 Phải học mới |
| Odoo Framework | ❌ Chưa có | 🔴 Kiến thức cốt lõi |
| API Integration | ✅ eCommerce migration | 🟢 Ôn REST/JSON-RPC |
| Git | ✅ GitHub projects | 🟢 Ôn workflow |
| ERP / Business Process | ❌ Chưa có | 🔴 Cần hiểu cơ bản |
| Viết tài liệu kỹ thuật | ❌ Chưa rõ | 🟡 Cần chuẩn bị |

---

# PHẦN A: NỀN TẢNG LẬP TRÌNH

---

## 🐍 PHẦN 1: PYTHON CƠ BẢN

### 1.1 Kiểu Dữ Liệu & Biến

```python
# Kiểu dữ liệu cơ bản
name = "Odoo"           # str
version = 16             # int
price = 99.99            # float
is_active = True         # bool
value = None             # NoneType

# Type checking
type(name)      # <class 'str'>
isinstance(name, str)  # True

# Type conversion
int("123")      # 123
str(456)        # "456"
float("3.14")   # 3.14
bool(0)         # False — 0, "", [], None → False
bool(1)         # True
```

### 1.2 Cấu Trúc Dữ Liệu

```python
# ── LIST (có thứ tự, thay đổi được, cho phép trùng) ──
products = ["Laptop", "Phone", "Tablet"]
products.append("Watch")        # Thêm cuối
products.insert(0, "TV")        # Thêm vị trí 0
products.remove("Phone")       # Xóa theo giá trị
products.pop(1)                 # Xóa theo index, trả về giá trị
products.sort()                 # Sắp xếp tại chỗ
len(products)                   # Số phần tử

# Slicing
products[1:3]    # Lấy index 1, 2
products[::-1]   # Đảo ngược list

# List comprehension
squares = [x**2 for x in range(10)]
even = [x for x in range(20) if x % 2 == 0]

# ── TUPLE (có thứ tự, KHÔNG thay đổi được) ──
point = (10, 20)
x, y = point    # Unpacking

# ── DICTIONARY (key-value, thay đổi được) ──
product = {
    "name": "Laptop",
    "price": 1500,
    "stock": 50
}
product["name"]                 # "Laptop"
product.get("color", "N/A")    # "N/A" — default nếu key không tồn tại
product.keys()                  # dict_keys
product.values()                # dict_values
product.items()                 # dict_items — list of (key, value) tuples

# Dict comprehension
prices = {k: v["price"] for k, v in catalog.items()}

# ── SET (không thứ tự, không trùng lặp) ──
tags = {"sale", "new", "featured"}
tags.add("hot")
tags.discard("new")
set_a & set_b   # Giao (intersection)
set_a | set_b   # Hợp (union)
set_a - set_b   # Hiệu (difference)
```

### 1.3 Control Flow

```python
# if / elif / else
if order.amount > 1000:
    discount = 0.1
elif order.amount > 500:
    discount = 0.05
else:
    discount = 0

# Ternary
status = "VIP" if order.amount > 1000 else "Normal"

# for loop
for product in products:
    print(product)

for i, product in enumerate(products):  # index + value
    print(f"{i}: {product}")

for key, value in product.items():  # iterate dict
    print(f"{key} = {value}")

# while
count = 0
while count < 10:
    count += 1

# break, continue, pass
for x in range(100):
    if x == 50:
        break       # Thoát vòng lặp
    if x % 2 == 0:
        continue    # Bỏ qua iteration
    pass            # Không làm gì (placeholder)
```

### 1.4 Functions

```python
# Hàm cơ bản
def calculate_total(price, quantity, tax=0.1):
    """Tính tổng tiền với thuế."""
    return price * quantity * (1 + tax)

# *args, **kwargs
def create_order(*items, **options):
    print(items)     # tuple: ("Laptop", "Phone")
    print(options)   # dict: {"discount": 0.1, "rush": True}

create_order("Laptop", "Phone", discount=0.1, rush=True)

# Lambda
sort_by_price = sorted(products, key=lambda p: p["price"])

# Map, Filter, Reduce
prices = list(map(lambda p: p["price"], products))
expensive = list(filter(lambda p: p["price"] > 100, products))

from functools import reduce
total = reduce(lambda a, b: a + b, [10, 20, 30])  # 60
```

### 1.5 String Methods Thường Dùng

```python
s = "  Hello, Odoo World!  "
s.strip()           # "Hello, Odoo World!" — bỏ khoảng trắng đầu/cuối
s.lower()           # "  hello, odoo world!  "
s.upper()           # "  HELLO, ODOO WORLD!  "
s.replace("Odoo", "ERP")
s.split(",")        # ["  Hello", " Odoo World!  "]
",".join(["a","b"]) # "a,b"
s.startswith("Hello")
s.find("Odoo")      # Index đầu tiên, -1 nếu không tìm thấy

# f-string (Python 3.6+)
name = "Tín"
f"Xin chào, {name}!"
f"Giá: {price:,.2f} VND"  # Format số: "1,500.00 VND"
```

### 1.6 Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Lỗi chia cho 0: {e}")
except (TypeError, ValueError) as e:
    print(f"Lỗi kiểu dữ liệu: {e}")
except Exception as e:       # Bắt tất cả
    print(f"Lỗi không xác định: {e}")
else:
    print("Không có lỗi")    # Chạy nếu không có exception
finally:
    print("Luôn chạy")       # Cleanup code

# Raise exception
def validate_age(age):
    if age < 0:
        raise ValueError("Tuổi không được âm")
```

---

## 🏛️ PHẦN 2: PYTHON TRUNG BÌNH — OOP

### 2.1 Class & Object

```python
class Product:
    # Class attribute (shared)
    company = "My Company"
    
    def __init__(self, name, price, stock=0):
        # Instance attributes
        self.name = name
        self.price = price
        self.stock = stock
        self._internal = "private convention"  # _ = protected
        self.__hidden = "name mangled"         # __ = name mangling
    
    def __str__(self):
        return f"Product({self.name}, {self.price})"
    
    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.stock})"
    
    def sell(self, quantity):
        if quantity > self.stock:
            raise ValueError("Không đủ hàng!")
        self.stock -= quantity
        return self.price * quantity

laptop = Product("Laptop", 1500, stock=10)
print(laptop)        # Product(Laptop, 1500)
laptop.sell(2)       # 3000
```

### 2.2 Kế Thừa (Inheritance) — Quan trọng cho Odoo

```python
class BaseModel:
    """Tương tự cách Odoo tổ chức models"""
    def __init__(self, name):
        self.name = name
    
    def save(self):
        print(f"Saving {self.name}")

class SaleOrder(BaseModel):
    def __init__(self, name, total):
        super().__init__(name)  # Gọi __init__ của parent
        self.total = total
    
    def save(self):
        self.validate()
        super().save()  # Gọi save() của parent — ĐÚNG PATTERN Odoo

    def validate(self):
        if self.total <= 0:
            raise ValueError("Tổng tiền phải > 0")

# Đa kế thừa (Odoo dùng rất nhiều: _inherit = ['mail.thread', ...])
class Trackable:
    def log_change(self, field, old, new):
        print(f"{field}: {old} -> {new}")

class TrackedSaleOrder(SaleOrder, Trackable):
    pass  # Kế thừa cả SaleOrder và Trackable

# MRO (Method Resolution Order) — thứ tự tìm method
print(TrackedSaleOrder.__mro__)
```

### 2.3 Decorators & Special Methods

```python
# ── @staticmethod vs @classmethod ──
class OrderManager:
    _count = 0
    
    @staticmethod
    def validate_email(email):
        """Không cần self/cls — utility function"""
        return "@" in email
    
    @classmethod
    def create(cls, data):
        """Nhận cls — factory method"""
        cls._count += 1
        return cls(data)
    
    @classmethod
    def get_count(cls):
        return cls._count

# ── @property (getter/setter) ──
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Bán kính không được âm")
        self._radius = value
    
    @property
    def area(self):  # Read-only computed property
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.area)     # 78.53975 — truy cập như attribute
c.radius = 10     # Setter được gọi
```

### 2.4 Context Managers & Generators

```python
# ── Context Manager (with statement) ──
class DatabaseConnection:
    def __enter__(self):
        print("Opening connection")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        if exc_type:
            print(f"Error: {exc_val}")
        return False  # True = suppress exception

with DatabaseConnection() as db:
    print("Working with DB")

# ── Generator — lazy evaluation, tiết kiệm memory ──
def read_large_file(filepath):
    """Đọc file lớn không load toàn bộ vào RAM"""
    with open(filepath) as f:
        for line in f:
            yield line.strip()

# Generator expression
total = sum(order.amount for order in orders)  # Không tạo list trung gian
```

### 2.5 Modules & Virtual Environment

```python
# Cấu trúc package
# my_package/
# ├── __init__.py      ← Đánh dấu là package
# ├── models.py
# └── utils.py

# Import patterns
from my_package.models import Product      # Import cụ thể
from my_package import utils               # Import module
import my_package.utils as u               # Alias

# __init__.py có thể export
# from .models import Product
# from .utils import helper_func
```

```bash
# Virtual environment
python3 -m venv odoo_env
source odoo_env/bin/activate   # Linux/Mac
pip install -r requirements.txt
pip freeze > requirements.txt
deactivate
```

---

## ⚡ PHẦN 3: PYTHON NÂNG CAO

### 3.1 Decorators Tự Viết

```python
from functools import wraps
import time

# Decorator đo thời gian — hữu ích debug Odoo performance
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} mất {elapsed:.4f}s")
        return result
    return wrapper

# Decorator với tham số
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def call_external_api(url):
    return requests.get(url).json()
```

### 3.2 Comprehensions & Functional Programming

```python
# Nested comprehension
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [x for row in matrix for x in row]  # [1,2,3,4,5,6,7,8,9]

# Dict comprehension với điều kiện
active_products = {
    p.id: p.name 
    for p in products 
    if p.active and p.stock > 0
}

# zip — kết hợp nhiều iterables
names = ["A", "B", "C"]
prices = [100, 200, 300]
product_dict = dict(zip(names, prices))  # {"A": 100, "B": 200, "C": 300}

# any() / all()
has_expensive = any(p.price > 1000 for p in products)
all_active = all(p.active for p in products)
```

### 3.3 GIL, Threading & Async

```python
# GIL (Global Interpreter Lock): chỉ 1 thread Python chạy tại 1 thời điểm

# Threading: phù hợp I/O bound (API calls, DB queries)
import threading
def fetch_data(url):
    response = requests.get(url)
    return response.json()

threads = [threading.Thread(target=fetch_data, args=(url,)) for url in urls]
[t.start() for t in threads]
[t.join() for t in threads]

# Multiprocessing: phù hợp CPU bound
from multiprocessing import Pool
with Pool(4) as p:
    results = p.map(process_record, records)

# Async/Await (Python 3.5+)
import asyncio
import aiohttp

async def fetch_async(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
```

### 3.4 Dataclasses & Type Hints

```python
from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class OrderLine:
    product_name: str
    quantity: int
    unit_price: float
    discount: float = 0.0
    
    @property
    def subtotal(self) -> float:
        return self.quantity * self.unit_price * (1 - self.discount)

@dataclass
class Order:
    partner_id: int
    lines: List[OrderLine] = field(default_factory=list)
    notes: Optional[str] = None
    
    @property
    def total(self) -> float:
        return sum(line.subtotal for line in self.lines)

# Type hints (rất phổ biến trong Odoo 16+)
def search_partner(name: str, limit: int = 10) -> List[Dict[str, any]]:
    """Tìm khách hàng theo tên."""
    pass
```

---

# PHẦN B: CƠ SỞ DỮ LIỆU

---

## 🗄️ PHẦN 4: SQL / POSTGRESQL CƠ BẢN

### 4.1 CRUD Operations

```sql
-- CREATE TABLE (Odoo tự tạo từ models, nhưng cần hiểu)
CREATE TABLE res_partner (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20),
    is_company BOOLEAN DEFAULT FALSE,
    create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- INSERT
INSERT INTO res_partner (name, email, is_company)
VALUES ('Công ty ABC', 'abc@company.com', TRUE);

-- INSERT nhiều dòng
INSERT INTO res_partner (name, email) VALUES
    ('Nguyễn Văn A', 'a@mail.com'),
    ('Trần Thị B', 'b@mail.com');

-- SELECT cơ bản
SELECT name, email FROM res_partner WHERE is_company = TRUE;

-- UPDATE
UPDATE res_partner SET phone = '0123456789' WHERE id = 1;

-- DELETE
DELETE FROM res_partner WHERE id = 5;
```

### 4.2 WHERE, ORDER BY, LIMIT

```sql
-- Comparison operators
SELECT * FROM sale_order WHERE amount_total > 1000;
SELECT * FROM sale_order WHERE state IN ('sale', 'done');
SELECT * FROM sale_order WHERE name LIKE 'SO%';      -- Bắt đầu bằng SO
SELECT * FROM sale_order WHERE name ILIKE '%abc%';    -- Case-insensitive
SELECT * FROM res_partner WHERE email IS NOT NULL;

-- AND / OR
SELECT * FROM sale_order
WHERE state = 'sale' AND amount_total > 500
   OR state = 'done';

-- BETWEEN
SELECT * FROM sale_order
WHERE date_order BETWEEN '2024-01-01' AND '2024-12-31';

-- ORDER BY
SELECT * FROM sale_order ORDER BY date_order DESC, name ASC;

-- LIMIT + OFFSET (phân trang)
SELECT * FROM sale_order ORDER BY id LIMIT 20 OFFSET 40;  -- Trang 3
```

### 4.3 Aggregate Functions & GROUP BY

```sql
-- COUNT, SUM, AVG, MIN, MAX
SELECT COUNT(*) as total_orders FROM sale_order WHERE state = 'sale';
SELECT SUM(amount_total) as revenue FROM sale_order WHERE state = 'sale';
SELECT AVG(amount_total) as avg_order FROM sale_order;

-- GROUP BY
SELECT partner_id, COUNT(*) as order_count, SUM(amount_total) as total
FROM sale_order
WHERE state = 'sale'
GROUP BY partner_id
ORDER BY total DESC;

-- HAVING (filter sau GROUP BY)
SELECT partner_id, SUM(amount_total) as total
FROM sale_order
GROUP BY partner_id
HAVING SUM(amount_total) > 10000;
```

### 4.4 JOIN — Kết Nối Bảng

```sql
-- INNER JOIN: chỉ lấy row khớp cả 2 bảng
SELECT so.name, rp.name as customer
FROM sale_order so
INNER JOIN res_partner rp ON so.partner_id = rp.id;

-- LEFT JOIN: lấy TẤT CẢ từ bảng trái, NULL nếu không khớp
SELECT rp.name, COUNT(so.id) as order_count
FROM res_partner rp
LEFT JOIN sale_order so ON rp.id = so.partner_id
GROUP BY rp.name;

-- Multi JOIN
SELECT so.name, rp.name as partner, sol.product_id, pt.name as product
FROM sale_order so
JOIN res_partner rp ON so.partner_id = rp.id
JOIN sale_order_line sol ON sol.order_id = so.id
JOIN product_template pt ON sol.product_id = pt.id
WHERE so.state = 'sale';
```

### 4.5 Subqueries

```sql
-- Subquery trong WHERE
SELECT * FROM res_partner
WHERE id IN (
    SELECT partner_id FROM sale_order WHERE amount_total > 5000
);

-- Subquery trong FROM
SELECT partner_name, total_amount
FROM (
    SELECT rp.name as partner_name, SUM(so.amount_total) as total_amount
    FROM sale_order so
    JOIN res_partner rp ON so.partner_id = rp.id
    GROUP BY rp.name
) as partner_totals
WHERE total_amount > 10000;
```

---

## 📊 PHẦN 5: POSTGRESQL NÂNG CAO

### 5.1 Window Functions

```sql
-- ROW_NUMBER: đánh số thứ tự
SELECT name, amount_total,
    ROW_NUMBER() OVER (ORDER BY amount_total DESC) as rank
FROM sale_order WHERE state = 'sale';

-- PARTITION BY: group trong window
SELECT partner_id, name, amount_total,
    SUM(amount_total) OVER (PARTITION BY partner_id) as partner_total,
    RANK() OVER (PARTITION BY partner_id ORDER BY amount_total DESC) as rank_in_partner
FROM sale_order;

-- Running total (tổng lũy kế)
SELECT date_order, amount_total,
    SUM(amount_total) OVER (ORDER BY date_order) as cumulative_sales
FROM sale_order WHERE state = 'sale';
```

### 5.2 CTE & Recursive Queries

```sql
-- CTE (Common Table Expression) — dễ đọc hơn subquery
WITH top_customers AS (
    SELECT partner_id, SUM(amount_total) as total
    FROM sale_order WHERE state = 'sale'
    GROUP BY partner_id
    ORDER BY total DESC LIMIT 10
)
SELECT rp.name, tc.total
FROM top_customers tc
JOIN res_partner rp ON tc.partner_id = rp.id;

-- Recursive CTE — duyệt cây (category cha-con trong Odoo)
WITH RECURSIVE category_tree AS (
    SELECT id, name, parent_id, 0 as level
    FROM product_category WHERE parent_id IS NULL
    UNION ALL
    SELECT c.id, c.name, c.parent_id, ct.level + 1
    FROM product_category c
    JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree ORDER BY level, name;
```

### 5.3 Index & Performance

```sql
-- Tạo index (tăng tốc query)
CREATE INDEX idx_sale_order_partner ON sale_order(partner_id);
CREATE INDEX idx_sale_order_state_date ON sale_order(state, date_order);  -- Composite

-- Unique index
CREATE UNIQUE INDEX idx_partner_email ON res_partner(email) WHERE email IS NOT NULL;

-- EXPLAIN ANALYZE — phân tích query performance
EXPLAIN ANALYZE SELECT * FROM sale_order WHERE partner_id = 123;
-- Kết quả: Seq Scan (chậm) vs Index Scan (nhanh)

-- VACUUM ANALYZE — thu hồi space + cập nhật statistics
VACUUM ANALYZE sale_order;
```

### 5.4 Transactions & Locking

```sql
-- Transaction
BEGIN;
UPDATE account_move SET state = 'posted' WHERE id = 100;
UPDATE res_partner SET credit = credit - 1000 WHERE id = 42;
-- Nếu OK:
COMMIT;
-- Nếu lỗi:
ROLLBACK;

-- Deadlock: 2 transaction chờ lock của nhau
-- PostgreSQL tự detect và hủy 1 transaction
-- Giải pháp: luôn lock theo thứ tự nhất quán (ORDER BY id trước khi UPDATE)
```

---

# PHẦN C: ERP & ODOO

---

## 🏢 PHẦN 6: ERP & BUSINESS PROCESS

### 6.1 ERP Là Gì?

ERP (Enterprise Resource Planning) = Hệ thống quản lý tổng thể doanh nghiệp, tích hợp tất cả quy trình vào 1 nền tảng:

```
┌─────────────────────────────────────────────┐
│                  ODOO ERP                   │
├──────────┬──────────┬──────────┬────────────┤
│  Sales   │ Purchase │Inventory │ Accounting │
│  Bán hàng│ Mua hàng │ Kho hàng │ Kế toán    │
├──────────┼──────────┼──────────┼────────────┤
│    HR    │   MRP    │   CRM    │  Website   │
│ Nhân sự  │ Sản xuất │ KH hàng  │ Web/eShop  │
└──────────┴──────────┴──────────┴────────────┘
```

### 6.2 Odoo Modules Chính — Cần Hiểu Nghiệp Vụ

**Sales (Bán hàng):**
```
Quotation (Báo giá) → Sale Order (Đơn bán) → Delivery (Giao hàng) → Invoice (Hóa đơn) → Payment (Thanh toán)
   [draft]              [sale]                  [done]               [posted]           [paid]
```

**Purchase (Mua hàng):**
```
Purchase Request → RFQ (Yêu cầu báo giá) → Purchase Order → Receipt (Nhận hàng) → Vendor Bill (Hóa đơn NCC)
```

**Inventory (Kho hàng):**
- Location: Kho vật lý (Stock, Input, Output, Scrap)
- Picking: Phiếu xuất/nhập kho
- Move: Dòng di chuyển hàng hóa
- Quant: Số lượng tồn kho thực tế

**Accounting (Kế toán):**
- Journal Entry (Bút toán) — core concept
- Account Move Line (Dòng bút toán: Nợ/Có)
- Reconciliation (Đối soát)

### 6.3 Các Thuật Ngữ ERP Quan Trọng

| Thuật ngữ | Giải thích |
|---|---|
| **Quotation** | Báo giá — chưa xác nhận |
| **Sale Order** | Đơn hàng — đã xác nhận |
| **Invoice** | Hóa đơn |
| **Journal** | Sổ nhật ký (kế toán) |
| **Picking** | Phiếu xuất/nhập kho |
| **BoM** | Bill of Materials — Định mức nguyên vật liệu |
| **Lead/Opportunity** | Cơ hội bán hàng (CRM) |
| **Workflow** | Luồng xử lý — trạng thái chuyển đổi |

---

## 🦁 PHẦN 7: ODOO FRAMEWORK — KIẾN TRÚC & CƠ BẢN

### 7.1 Kiến Trúc Tổng Quan

```
Odoo Architecture:
┌─────────────────────────────────────┐
│           Browser (JS/OWL)          │  ← Frontend
├─────────────────────────────────────┤
│     Web Controllers (Python)        │  ← HTTP/API Layer
├─────────────────────────────────────┤
│     ORM / Business Logic (Python)   │  ← Core Logic
├─────────────────────────────────────┤
│     PostgreSQL Database             │  ← Data
└─────────────────────────────────────┘
```

### 7.2 Cấu Trúc Module

```
my_module/
├── __init__.py          ← Import models, controllers
├── __manifest__.py      ← Module metadata (tên, version, depends)
├── models/
│   ├── __init__.py
│   └── my_model.py      ← Python models (ORM)
├── views/
│   └── my_view.xml      ← Form, List, Search views
├── security/
│   ├── ir.model.access.csv   ← Quyền CRUD theo group
│   └── security.xml          ← Record rules
├── data/
│   └── data.xml         ← Dữ liệu khởi tạo, cron jobs
├── controllers/
│   └── main.py          ← HTTP endpoints / API
├── wizard/              ← Transient models (dialog)
├── report/              ← PDF/QWeb reports
└── static/
    └── src/
        ├── js/          ← OWL components
        ├── xml/         ← QWeb templates
        └── css/
```

### 7.3 __manifest__.py

```python
{
    'name': 'Custom Project Tasks',
    'version': '16.0.1.0.0',        # odoo_ver.major.minor.patch.fix
    'category': 'Project',
    'summary': 'Enhanced project task management',
    'description': """Long description here""",
    'author': 'Phạm Duy Tín',
    'depends': ['project', 'mail', 'base'],  # Module phụ thuộc
    'data': [
        'security/ir.model.access.csv',      # Load trước
        'security/security.xml',
        'views/project_task_views.xml',
        'data/data.xml',
    ],
    'assets': {                              # JS/CSS assets (Odoo 15+)
        'web.assets_backend': [
            'my_module/static/src/js/**/*',
            'my_module/static/src/xml/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
```

### 7.4 Models — Các Loại Model

```python
from odoo import models, fields, api

# 1. models.Model — Persistent (lưu DB)
class SaleOrder(models.Model):
    _name = 'sale.order'
    _description = 'Sale Order'

# 2. models.TransientModel — Temporary (tự xóa sau vài giờ)
# Dùng cho wizard/dialog
class SaleOrderConfirm(models.TransientModel):
    _name = 'sale.order.confirm.wizard'

# 3. models.AbstractModel — Base class (không tạo bảng DB)
# Dùng để share logic giữa nhiều models
class MailThread(models.AbstractModel):
    _name = 'mail.thread'
```

### 7.5 Fields — Tất Cả Các Loại

```python
class ProjectTask(models.Model):
    _name = 'project.task.custom'
    _description = 'Custom Project Task'
    _order = 'priority desc, date_deadline asc'  # Sắp xếp mặc định

    # ── BASIC FIELDS ──
    name = fields.Char(string='Task Name', required=True, tracking=True)
    description = fields.Text()
    note = fields.Html()                    # Rich text HTML
    sequence = fields.Integer(default=10)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'High'),
        ('2', 'Critical'),
    ], default='0', string='Priority')
    progress = fields.Float(digits=(6, 2))  # 6 chữ số, 2 thập phân
    amount = fields.Monetary(currency_field='currency_id')
    active = fields.Boolean(default=True)   # False = archived (auto-filter)
    date_deadline = fields.Date()
    datetime_start = fields.Datetime()
    attachment = fields.Binary()
    filename = fields.Char()

    # ── RELATIONAL FIELDS ──
    # Many2one: FK — mỗi task thuộc 1 project
    project_id = fields.Many2one(
        'project.project', string='Project',
        ondelete='cascade',   # cascade / set null / restrict
        required=True,
        index=True            # Tạo DB index
    )
    
    # One2many: Inverse — 1 task có nhiều timesheets
    timesheet_ids = fields.One2many(
        'account.analytic.line', 'task_id',
        string='Timesheets'
    )
    
    # Many2many: Bảng trung gian — 1 task có nhiều tags, 1 tag có nhiều tasks
    tag_ids = fields.Many2many(
        'project.tags',
        'project_task_tag_rel',     # Tên bảng trung gian (optional)
        'task_id', 'tag_id',        # Column names (optional)
        string='Tags'
    )

    # ── COMPUTED FIELDS ──
    total_hours = fields.Float(
        compute='_compute_total_hours',
        store=True,        # True: lưu DB, query được | False: tính real-time
        readonly=True
    )
    
    # ── RELATED FIELD (shortcut qua relation) ──
    partner_id = fields.Many2one(
        related='project_id.partner_id',
        store=True,        # Lưu vào DB để query
        readonly=True
    )
```

### 7.6 API Decorators — Hiểu Rõ Từng Loại

```python
class ProjectTask(models.Model):
    _inherit = 'project.task.custom'

    # @api.depends — Computed field, chạy khi dependency thay đổi
    # ✓ Chạy cả khi write() qua code
    # ✓ Có thể store=True
    @api.depends('timesheet_ids.unit_amount')
    def _compute_total_hours(self):
        for task in self:
            task.total_hours = sum(task.timesheet_ids.mapped('unit_amount'))

    # @api.onchange — CHỈ chạy trên UI khi user thay đổi field
    # ✗ KHÔNG chạy khi write() qua code
    # ✗ KHÔNG lưu DB
    @api.onchange('project_id')
    def _onchange_project(self):
        if self.project_id:
            self.priority = self.project_id.default_priority
        # Trả về domain, warning:
        return {
            'domain': {'tag_ids': [('project_ids', 'in', [self.project_id.id])]},
            'warning': {'title': 'Warning', 'message': 'Project changed!'}
        }

    # @api.constrains — Validation khi create/write
    @api.constrains('date_deadline')
    def _check_deadline(self):
        for task in self:
            if task.date_deadline and task.date_deadline < fields.Date.today():
                raise ValidationError("Deadline không được trong quá khứ!")

    # @api.model — Method cấp model (không cần recordset)
    @api.model
    def get_default_project(self):
        return self.env['project.project'].search([], limit=1)

    # @api.model_create_multi — Override create (Odoo 14+)
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name'):
                vals['name'] = self.env['ir.sequence'].next_by_code('project.task')
        return super().create(vals_list)
```

---

## 🔥 PHẦN 8: ODOO FRAMEWORK — NÂNG CAO

### 8.1 Kế Thừa Model (Inheritance) — Khái Niệm Cốt Lõi

```python
from odoo import models, fields, api

# ── CÁCH 1: _inherit (Mở rộng model có sẵn — cùng bảng DB) ──
# Thêm field/method vào model sẵn có
class ResPartner(models.Model):
    _inherit = 'res.partner'         # Mở rộng res.partner
    loyalty_points = fields.Integer(default=0)
    
    def add_loyalty(self, points):
        self.loyalty_points += points

# ── CÁCH 2: _inherit + _name (Tạo model MỚI kế thừa — bảng DB riêng) ──
class CustomerVIP(models.Model):
    _name = 'customer.vip'
    _inherit = 'res.partner'         # Copy toàn bộ fields + methods
    vip_level = fields.Selection([('gold', 'Gold'), ('platinum', 'Platinum')])

# ── CÁCH 3: _inherits (Delegation — bảng riêng + FK) ──
# Employee "là một" res.partner, có bảng riêng + foreign key
class HrEmployee(models.Model):
    _name = 'hr.employee'
    _inherits = {'res.partner': 'address_id'}
    address_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
    department_id = fields.Many2one('hr.department')
```

### 8.2 Domain — Search Logic

```python
# Domain syntax: [(field, operator, value)]
# Operators: =, !=, >, >=, <, <=, like, ilike, in, not in, child_of, parent_of

# AND (ngầm định khi có nhiều tuples)
domain = [('state', '=', 'sale'), ('amount_total', '>', 1000)]

# OR: prefix '|'
domain = ['|', ('state', '=', 'sale'), ('state', '=', 'done')]

# NOT: prefix '!'
domain = ['!', ('active', '=', False)]

# Phức tạp: (A AND B) OR C
domain = ['|', '&', ('state', '=', 'sale'), ('amount', '>', 1000), ('partner_id', '=', 5)]

# ORM search methods
records = self.env['sale.order'].search(domain, limit=100, offset=0, order='date_order desc')
count = self.env['sale.order'].search_count(domain)
records = self.env['sale.order'].search_read(domain, fields=['name', 'state'], limit=50)

# Đặc biệt
self.env['sale.order'].browse(42)              # Lấy record theo id
self.env['sale.order'].browse([1, 2, 3])       # Lấy nhiều records
record.exists()                                 # Kiểm tra record tồn tại
self.env['sale.order'].sudo().search([])        # Bỏ qua access rights
self.env['sale.order'].with_context(lang='vi_VN').search([])  # Thêm context
```

### 8.3 CRUD Override Pattern

```python
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Logic TRƯỚC create
            if not vals.get('name') or vals['name'] == '/':
                vals['name'] = self.env['ir.sequence'].next_by_code('sale.order')
        records = super().create(vals_list)
        # Logic SAU create
        for record in records:
            record.message_post(body="Order created!")
        return records

    def write(self, vals):
        # Logic TRƯỚC write
        old_states = {rec.id: rec.state for rec in self}
        result = super().write(vals)
        # Logic SAU write
        if 'state' in vals:
            for rec in self:
                if old_states[rec.id] != vals['state']:
                    rec._log_state_change(old_states[rec.id], vals['state'])
        return result

    def unlink(self):
        for record in self:
            if record.state not in ('draft', 'cancel'):
                raise UserError("Chỉ xóa được đơn ở trạng thái Draft hoặc Cancel!")
        return super().unlink()

    def copy(self, default=None):
        """Override duplicate"""
        default = dict(default or {})
        default['name'] = f"{self.name} (Copy)"
        return super().copy(default)
```

### 8.4 XML Views

```xml
<odoo>
    <!-- FORM VIEW -->
    <record id="view_task_form" model="ir.ui.view">
        <field name="name">project.task.custom.form</field>
        <field name="model">project.task.custom</field>
        <field name="arch" type="xml">
            <form string="Task">
                <header>
                    <button name="action_mark_done" type="object" 
                            string="Mark Done" class="btn-primary"
                            attrs="{'invisible': [('state', '=', 'done')]}"/>
                    <field name="state" widget="statusbar" 
                           statusbar_visible="draft,in_progress,done"/>
                </header>
                <sheet>
                    <div class="oe_title">
                        <h1><field name="name" placeholder="Task name..."/></h1>
                    </div>
                    <group>
                        <group string="General">
                            <field name="project_id"/>
                            <field name="date_deadline"/>
                            <field name="user_id"/>
                        </group>
                        <group string="Status">
                            <field name="priority" widget="priority"/>
                            <field name="progress" widget="progressbar"/>
                            <field name="tag_ids" widget="many2many_tags"/>
                        </group>
                    </group>
                    <notebook>
                        <page string="Description">
                            <field name="description"/>
                        </page>
                        <page string="Timesheets">
                            <field name="timesheet_ids">
                                <tree editable="bottom">
                                    <field name="date"/>
                                    <field name="name"/>
                                    <field name="unit_amount" sum="Total Hours"/>
                                </tree>
                            </field>
                        </page>
                    </notebook>
                </sheet>
                <div class="oe_chatter">
                    <field name="message_follower_ids"/>
                    <field name="activity_ids"/>
                    <field name="message_ids"/>
                </div>
            </form>
        </field>
    </record>

    <!-- LIST VIEW -->
    <record id="view_task_list" model="ir.ui.view">
        <field name="name">project.task.custom.list</field>
        <field name="model">project.task.custom</field>
        <field name="arch" type="xml">
            <tree decoration-danger="date_deadline &lt; current_date"
                  decoration-muted="state == 'done'">
                <field name="name"/>
                <field name="project_id"/>
                <field name="date_deadline"/>
                <field name="state"/>
                <field name="priority" widget="priority"/>
            </tree>
        </field>
    </record>

    <!-- SEARCH VIEW -->
    <record id="view_task_search" model="ir.ui.view">
        <field name="name">project.task.custom.search</field>
        <field name="model">project.task.custom</field>
        <field name="arch" type="xml">
            <search>
                <field name="name"/>
                <field name="project_id"/>
                <filter name="my_tasks" string="My Tasks"
                        domain="[('user_id', '=', uid)]"/>
                <filter name="overdue" string="Overdue"
                        domain="[('date_deadline', '&lt;', context_today().strftime('%Y-%m-%d'))]"/>
                <separator/>
                <group expand="0" string="Group By">
                    <filter name="by_project" string="Project" context="{'group_by': 'project_id'}"/>
                    <filter name="by_state" string="Status" context="{'group_by': 'state'}"/>
                </group>
            </search>
        </field>
    </record>

    <!-- ACTION + MENU -->
    <record id="action_task_custom" model="ir.actions.act_window">
        <field name="name">Tasks</field>
        <field name="res_model">project.task.custom</field>
        <field name="view_mode">list,form,kanban</field>
        <field name="context">{'search_default_my_tasks': 1}</field>
    </record>
    <menuitem id="menu_task_custom" name="My Tasks"
              parent="project.menu_main_pm" action="action_task_custom"/>
</odoo>
```

### 8.5 Kế Thừa View (View Inheritance)

```xml
<!-- Thêm field vào form view có sẵn -->
<record id="view_partner_form_inherit" model="ir.ui.view">
    <field name="name">res.partner.form.inherit.custom</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="base.view_partner_form"/>
    <field name="arch" type="xml">
        <!-- Thêm field SAU field phone -->
        <field name="phone" position="after">
            <field name="loyalty_points"/>
        </field>
        <!-- Thay thế field -->
        <field name="website" position="replace">
            <field name="website" widget="url" placeholder="https://..."/>
        </field>
        <!-- Thêm vào cuối group -->
        <xpath expr="//group[@name='sale']" position="inside">
            <field name="custom_field"/>
        </xpath>
    </field>
</record>
```

### 8.6 Security — Access Rights & Record Rules

```csv
# security/ir.model.access.csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_task_user,task.user,model_project_task_custom,base.group_user,1,1,1,0
access_task_manager,task.manager,model_project_task_custom,project.group_project_manager,1,1,1,1
```

```xml
<!-- security/security.xml -->
<odoo>
    <!-- Tạo group mới -->
    <record id="group_task_admin" model="res.groups">
        <field name="name">Task Administrator</field>
        <field name="category_id" ref="base.module_category_project"/>
    </record>

    <!-- Record Rule: User chỉ thấy task của mình -->
    <record id="rule_task_user" model="ir.rule">
        <field name="name">Task: See own only</field>
        <field name="model_id" ref="model_project_task_custom"/>
        <field name="domain_force">[('user_id', '=', user.id)]</field>
        <field name="groups" eval="[(4, ref('base.group_user'))]"/>
    </record>

    <!-- Record Rule: Manager thấy tất cả -->
    <record id="rule_task_manager" model="ir.rule">
        <field name="name">Task: Manager sees all</field>
        <field name="model_id" ref="model_project_task_custom"/>
        <field name="domain_force">[(1, '=', 1)]</field>
        <field name="groups" eval="[(4, ref('project.group_project_manager'))]"/>
    </record>
</odoo>
```

### 8.7 Controllers (HTTP / API)

```python
from odoo import http
from odoo.http import request
import json

class TaskController(http.Controller):

    # type='json': nhận/trả JSON — header Content-Type: application/json
    @http.route('/api/tasks', type='json', auth='user', methods=['POST'])
    def get_tasks(self, **kwargs):
        domain = kwargs.get('domain', [])
        tasks = request.env['project.task.custom'].search(domain)
        return {'tasks': tasks.read(['name', 'state', 'date_deadline'])}

    # type='http': nhận form data / query params — trả HTML hoặc Response
    @http.route('/web/task/<int:task_id>', type='http', auth='user')
    def task_page(self, task_id, **kwargs):
        task = request.env['project.task.custom'].browse(task_id)
        return request.render('my_module.task_template', {'task': task})

    # auth='public': không cần login — dùng cho webhook
    @http.route('/webhook/notify', type='json', auth='public', csrf=False, methods=['POST'])
    def webhook(self, **kwargs):
        data = json.loads(request.httprequest.data)
        request.env['mail.message'].sudo().create({
            'body': f"Webhook received: {data.get('event')}",
        })
        return {'status': 'ok'}
```

---

## 🌐 PHẦN 9: JAVASCRIPT / OWL FRAMEWORK

### 9.1 OWL Component (Odoo Web Library)

```javascript
/** @odoo-module **/
import { Component, useState, onMounted, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class TaskDashboard extends Component {
    static template = "my_module.TaskDashboard";
    static props = {};  // Khai báo props nhận từ parent
    
    setup() {
        // Reactive state
        this.state = useState({
            tasks: [],
            loading: true,
            filter: 'all',
        });
        
        // Services (Dependency Injection)
        this.orm = useService("orm");
        this.action = useService("action");
        this.notification = useService("notification");
        
        // Lifecycle hooks
        onWillStart(async () => {
            await this.loadTasks();  // Trước khi render
        });
        onMounted(() => {
            console.log("Component mounted");
        });
    }
    
    async loadTasks() {
        this.state.loading = true;
        try {
            this.state.tasks = await this.orm.searchRead(
                "project.task",
                this.getDomain(),
                ["name", "state", "date_deadline", "priority"],
                { limit: 100, order: "priority desc" }
            );
        } catch (e) {
            this.notification.add("Error loading tasks", { type: "danger" });
        }
        this.state.loading = false;
    }
    
    getDomain() {
        const base = [["user_id", "=", this.env.session.uid]];
        if (this.state.filter === 'overdue') {
            return [...base, ["date_deadline", "<", new Date().toISOString().split('T')[0]]];
        }
        return base;
    }
    
    async markDone(taskId) {
        await this.orm.call("project.task", "action_mark_done", [taskId]);
        await this.loadTasks();
        this.notification.add("Task completed!", { type: "success" });
    }
    
    openTask(taskId) {
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: "project.task",
            res_id: taskId,
            views: [[false, "form"]],
        });
    }
}

// Register as action
registry.category("actions").add("task_dashboard", TaskDashboard);
```

### 9.2 QWeb Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<templates>
    <t t-name="my_module.TaskDashboard">
        <div class="o_task_dashboard p-3">
            <h2>Task Dashboard</h2>
            
            <!-- Filter buttons -->
            <div class="btn-group mb-3">
                <button class="btn btn-outline-primary"
                        t-att-class="{'active': state.filter === 'all'}"
                        t-on-click="() => { state.filter = 'all'; loadTasks(); }">
                    All
                </button>
                <button class="btn btn-outline-danger"
                        t-att-class="{'active': state.filter === 'overdue'}"
                        t-on-click="() => { state.filter = 'overdue'; loadTasks(); }">
                    Overdue
                </button>
            </div>

            <!-- Loading -->
            <t t-if="state.loading">
                <div class="text-center p-5">
                    <i class="fa fa-spinner fa-spin fa-3x"/> Loading...
                </div>
            </t>
            
            <!-- Task list -->
            <t t-else="">
                <div class="row">
                    <t t-foreach="state.tasks" t-as="task" t-key="task.id">
                        <div class="col-md-4 mb-3">
                            <div class="card" t-on-click="() => this.openTask(task.id)">
                                <div class="card-body">
                                    <h5 t-esc="task.name"/>
                                    <span class="badge" t-att-class="{
                                        'bg-success': task.state === 'done',
                                        'bg-warning': task.state === 'in_progress',
                                        'bg-secondary': task.state === 'draft'
                                    }" t-esc="task.state"/>
                                    <button class="btn btn-sm btn-primary float-end"
                                            t-on-click.stop="() => this.markDone(task.id)">
                                        ✓ Done
                                    </button>
                                </div>
                            </div>
                        </div>
                    </t>
                </div>
                <t t-if="!state.tasks.length">
                    <p class="text-muted">No tasks found.</p>
                </t>
            </t>
        </div>
    </t>
</templates>
```

---

## 🔌 PHẦN 10: TÍCH HỢP API

### 10.1 Gọi API Bên Ngoài từ Odoo

```python
import requests
import logging
from odoo import models, api, fields
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class ExternalIntegration(models.Model):
    _name = 'external.integration'

    @api.model
    def sync_orders(self):
        """Đồng bộ đơn hàng từ hệ thống bên ngoài"""
        config = self.env['ir.config_parameter'].sudo()
        api_key = config.get_param('external.api_key')
        base_url = config.get_param('external.base_url')
        
        try:
            response = requests.get(
                f"{base_url}/api/orders",
                headers={'Authorization': f'Bearer {api_key}'},
                timeout=30
            )
            response.raise_for_status()
            orders = response.json().get('data', [])
            
            for order_data in orders:
                existing = self.env['sale.order'].search([
                    ('external_ref', '=', order_data['id'])
                ], limit=1)
                if not existing:
                    self._create_order_from_external(order_data)
                    
            _logger.info(f"Synced {len(orders)} orders from external system")
            return True
            
        except requests.exceptions.Timeout:
            _logger.error("External API timeout")
            raise UserError("API timeout! Vui lòng thử lại sau.")
        except requests.exceptions.HTTPError as e:
            _logger.error(f"HTTP Error: {e.response.status_code}")
            raise UserError(f"API Error: {e.response.status_code}")
        except Exception as e:
            _logger.exception(f"Unexpected error: {e}")
            raise UserError(f"Lỗi: {str(e)}")
```

### 10.2 Odoo XML-RPC / JSON-RPC (Expose cho bên ngoài)

```python
# Gọi Odoo API từ Python client bên ngoài
import xmlrpc.client

# 1. Authenticate
url = "http://localhost:8069"
db = "mydb"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

# 2. Call methods
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Search + Read
orders = models.execute_kw(db, uid, password, 'sale.order', 'search_read',
    [[['state', '=', 'sale']]],
    {'fields': ['name', 'amount_total'], 'limit': 10}
)

# Create
new_id = models.execute_kw(db, uid, password, 'res.partner', 'create',
    [{'name': 'New Customer', 'email': 'new@customer.com'}]
)

# Write
models.execute_kw(db, uid, password, 'res.partner', 'write',
    [[new_id], {'phone': '0123456789'}]
)
```

### 10.3 Cron Jobs (Scheduled Actions)

```python
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _cron_auto_cancel_expired(self):
        """Tự động hủy quotation quá 30 ngày"""
        expired = self.search([
            ('state', '=', 'draft'),
            ('date_order', '<', fields.Datetime.subtract(fields.Datetime.now(), days=30))
        ])
        expired.action_cancel()
        _logger.info(f"Auto-cancelled {len(expired)} expired quotations")
```

```xml
<record id="cron_auto_cancel" model="ir.cron">
    <field name="name">Auto Cancel Expired Quotations</field>
    <field name="model_id" ref="sale.model_sale_order"/>
    <field name="state">code</field>
    <field name="code">model._cron_auto_cancel_expired()</field>
    <field name="interval_number">1</field>
    <field name="interval_type">days</field>
    <field name="numbercall">-1</field>  <!-- -1 = vô hạn -->
    <field name="active">True</field>
</record>
```

---

## 🐛 PHẦN 11: ODOO UPGRADE & DEBUGGING

### 11.1 Quy Trình Nâng Cấp Version Odoo

```
1. Backup database + filestore
   $ pg_dump mydb > mydb_backup.sql

2. Kiểm tra module compatibility
   - Đọc changelog Odoo (Breaking changes)
   - Kiểm tra OCA modules cho version mới

3. Dùng Odoo Upgrade Tool (https://upgrade.odoo.com)
   - Upload database → nhận DB mới

4. Test trên staging
   - Kiểm tra custom modules
   - Fix deprecated APIs

5. Fix code thay đổi phổ biến:
   - Odoo 15→16: attrs → invisible/readonly/required trực tiếp
   - Odoo 14→15: OWL thay thế Widget cũ
   - API thay đổi: @api.multi bị loại bỏ từ Odoo 13
```

### 11.2 Debug Tools

```python
# 1. Logging
import logging
_logger = logging.getLogger(__name__)

_logger.debug("Debug info: %s", data)
_logger.info("Processing order: %s", order.name)
_logger.warning("Deprecated method called")
_logger.error("Failed to sync: %s", str(e))
_logger.exception("Unexpected error")  # Kèm traceback

# 2. Shell
# $ odoo-bin shell -d mydb
# >>> self.env['sale.order'].search_count([])

# 3. pdb (Python debugger)
import pdb; pdb.set_trace()  # Dừng code tại đây
# Hoặc: breakpoint()  # Python 3.7+
# Commands: n (next), s (step into), c (continue), p variable, l (list code)

# 4. Odoo Developer Mode
# Settings → Activate Developer Mode
# Hoặc: thêm ?debug=1 vào URL
```

### 11.3 Performance Optimization

```python
# ❌ CHẬM: N+1 query problem
for order in self.env['sale.order'].search([]):
    partner_name = order.partner_id.name  # Mỗi lần = 1 query

# ✅ NHANH: Prefetch tự động hoặc dùng read()
orders = self.env['sale.order'].search([])
data = orders.read(['name', 'partner_id'])  # 1 query lấy hết

# ✅ mapped() thay vì loop
partner_names = orders.mapped('partner_id.name')  # Tối ưu hơn list comp

# ✅ SQL trực tiếp khi cần performance cao
self.env.cr.execute("""
    SELECT partner_id, SUM(amount_total)
    FROM sale_order
    WHERE state = 'sale'
    GROUP BY partner_id
""")
results = self.env.cr.dictfetchall()

# ✅ Batch processing
for batch in self.env.cr.split_every(100, records):
    batch.write({'processed': True})
    self.env.cr.commit()  # Commit từng batch

# ✅ Index cho field hay filter
project_id = fields.Many2one('project.project', index=True)
```

---

## 🔧 PHẦN 12: GIT & WORKFLOW

### 12.1 Git Commands Cần Thuộc

```bash
# Branch workflow
git checkout -b feature/TICKET-123-add-task-module
git add -p                    # Staging từng phần (review trước khi add)
git commit -m "feat: add custom task module with ORM"
git push origin feature/TICKET-123-add-task-module

# Rebase (giữ history sạch — thay vì merge)
git fetch origin
git rebase origin/main        # Đặt commits của mình lên đầu main

# Xử lý khi rebase conflict
git rebase origin/main
# Sửa file conflict
git add <file>
git rebase --continue

# Cherry-pick (lấy 1 commit cụ thể từ branch khác)
git cherry-pick abc1234

# Stash (lưu tạm thay đổi)
git stash push -m "WIP: task form"
git stash list
git stash pop                 # Lấy lại thay đổi mới nhất

# Squash commits (gộp commit trước khi merge)
git rebase -i HEAD~3          # Interactive rebase 3 commits

# Tìm ai thay đổi dòng code
git blame -L 50,80 models/task.py

# Tìm commit gây bug
git bisect start
git bisect bad HEAD
git bisect good v13.0
```

### 12.2 Commit Message Convention

```
feat: thêm module quản lý task
fix: sửa lỗi compute total hours
refactor: tách logic validate ra function riêng
chore: cập nhật requirements.txt
docs: thêm docstring cho API methods

# Odoo version convention: 16.0.1.0.0
# (odoo_version.major.minor.patch.fix)
```

---

## 📝 PHẦN 13: VIẾT TÀI LIỆU KỸ THUẬT

### 13.1 Docstring Convention (Python)

```python
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def calculate_discount(self, partner_id, amount):
        """Calculate discount based on partner loyalty level.
        
        Áp dụng chiết khấu theo cấp độ khách hàng:
        - Gold: 5%
        - Platinum: 10%
        - Mặc định: 0%
        
        Args:
            partner_id (int): ID của khách hàng
            amount (float): Tổng tiền đơn hàng
            
        Returns:
            float: Số tiền chiết khấu
            
        Raises:
            UserError: Nếu partner_id không tồn tại
            
        Example:
            >>> order.calculate_discount(42, 1000.0)
            50.0
        """
        pass
```

### 13.2 Cấu Trúc Tài Liệu Module

```markdown
# Module: Custom Project Tasks

## Mục đích
Mở rộng chức năng quản lý task với tính năng tracking giờ và deadline.

## Models
| Model | Mô tả | Bảng DB |
|-------|--------|---------|
| project.task.custom | Task mở rộng | project_task_custom |

## API Endpoints
| Method | URL | Mô tả |
|--------|-----|--------|
| POST | /api/tasks | Lấy danh sách tasks |
| POST | /api/tasks/<id> | Cập nhật task |

## Cài đặt
1. Copy module vào addons path
2. Cập nhật danh sách module
3. Cài đặt từ Apps menu

## Dependencies
- project, mail, base
```

---

# PHẦN D: PHỎNG VẤN

---

## ❓ PHẦN 14: CÂU HỎI PHỎNG VẤN TỔNG HỢP

### 14.1 Python Cơ Bản

**Q1: Mutable vs Immutable trong Python?**
> - Mutable (thay đổi được): list, dict, set
> - Immutable (không thay đổi): int, float, str, tuple, frozenset
> - Quan trọng: khi truyền mutable object vào function → thay đổi ảnh hưởng bên ngoài

**Q2: `==` vs `is` trong Python?**
> - `==`: so sánh giá trị
> - `is`: so sánh identity (cùng object trong memory)
> ```python
> a = [1, 2, 3]
> b = [1, 2, 3]
> a == b  # True (cùng giá trị)
> a is b  # False (khác object)
> ```

**Q3: `*args` và `**kwargs` là gì?**
> - `*args`: nhận arguments dạng tuple
> - `**kwargs`: nhận keyword arguments dạng dict
> - Thứ tự: `def func(a, b, *args, **kwargs)`

**Q4: Deep copy vs Shallow copy?**
> ```python
> import copy
> a = [[1, 2], [3, 4]]
> b = copy.copy(a)       # Shallow: b[0] is a[0] → cùng reference
> c = copy.deepcopy(a)   # Deep: hoàn toàn independent
> ```

### 14.2 Python Nâng Cao

**Q5: GIL là gì và ảnh hưởng thế nào?**
> Global Interpreter Lock: chỉ 1 thread Python chạy tại 1 thời điểm.
> - Threading vẫn hữu ích cho I/O bound (network, DB)
> - CPU bound → dùng multiprocessing hoặc C extensions

**Q6: Decorator là gì? Viết ví dụ?**
> Function nhận function → trả function mới. Dùng `@` syntax.
> Odoo dùng rất nhiều: `@api.depends`, `@api.onchange`, `@api.constrains`

**Q7: Generator vs List — khi nào dùng cái nào?**
> - Generator: dữ liệu lớn, chỉ duyệt 1 lần, tiết kiệm RAM
> - List: cần random access, duyệt nhiều lần, dữ liệu nhỏ

### 14.3 PostgreSQL

**Q8: Index là gì? Khi nào dùng?**
> Cấu trúc dữ liệu tăng tốc query (B-tree). Dùng cho cột hay WHERE/JOIN/ORDER BY.
> Trade-off: tăng tốc đọc nhưng chậm ghi (INSERT/UPDATE).

**Q9: ACID là gì?**
> - **A**tomicity: Transaction là đơn vị — thành công hết hoặc rollback hết
> - **C**onsistency: DB luôn ở trạng thái hợp lệ
> - **I**solation: Transaction không ảnh hưởng nhau
> - **D**urability: Commit xong thì dữ liệu không mất

**Q10: Normalize vs Denormalize?**
> - Normalize: tách thành nhiều bảng, giảm redundancy (Odoo dùng)
> - Denormalize: gộp bảng, tăng tốc đọc, chấp nhận redundancy

### 14.4 Odoo Framework

**Q11: `_inherit` vs `_inherits`?**
> - `_inherit`: mở rộng model có sẵn, cùng bảng DB
> - `_inherits`: delegation, tạo bảng mới + FK (như composition)

**Q12: `@api.depends` vs `@api.onchange`?**
> - `depends`: computed field, chạy cả khi write() qua code, có thể store=True
> - `onchange`: chỉ chạy trên UI, không trigger khi write() qua code

**Q13: `ensure_one()` dùng khi nào?**
> Trong business method chỉ hoạt động trên 1 record. Raise ValueError nếu recordset có != 1 record.

**Q14: Odoo security có mấy tầng?**
> 1. **Access Rights** (ir.model.access.csv): CRUD theo group
> 2. **Record Rules** (ir.rule): Filter record theo domain
> 3. **Field-level access**: `groups` attribute trên field

**Q15: `sudo()` dùng khi nào? Cẩn thận gì?**
> Bỏ qua access rights — dùng khi system cần truy cập data không thuộc user hiện tại.
> Cẩn thận: không dùng sudo() cho data user nhập vào → security risk.

**Q16: Performance optimization trong Odoo?**
> - `mapped()` thay vì loop Python
> - `read()` thay `browse()` khi chỉ đọc
> - `store=True` cho computed fields hay query
> - SQL trực tiếp cho report phức tạp
> - Thêm `index=True` cho Many2one hay field hay filter

**Q17: Wizard (TransientModel) dùng khi nào?**
> Dùng cho dialog popup yêu cầu user nhập thêm thông tin trước khi thực hiện action.
> Data tự động xóa sau vài giờ — không chiếm DB lâu dài.

### 14.5 Soft Skills & Kinh Nghiệm

**Q18: Bạn chưa có kinh nghiệm Odoo, sao đảm bảo hiệu quả?**
> 💡 "Nền tảng Python vững (Flask/SQLAlchemy) giúp tiếp cận Odoo ORM nhanh — cả hai dùng Python + PostgreSQL. Backbone.js tôi đã dùng có kiến trúc tương tự OWL. Tôi đã dành thời gian nghiên cứu tài liệu Odoo và build module thực hành."

**Q19: Kể về dự án eCommerce Migration — relevance với Odoo?**
> 💡 "Dự án yêu cầu hiểu schema nhiều platform (Shopify, Magento 2, WooCommerce) và transform data. Rất tương đồng với tích hợp Odoo với bên thứ ba — hiểu data model cả 2 phía, xây dựng mapping logic, xử lý error, đảm bảo consistency."

**Q20: JD yêu cầu 3 năm kinh nghiệm nhưng bạn mới có ~1 năm?**
> 💡 "Tôi hiểu đây là baseline. Trong thời gian làm việc, tôi đã full-stack từ backend Python, PostgreSQL đến frontend, tích hợp API multi-platform. Tôi muốn được đánh giá qua kỹ năng thực tế."

**Q21: Debug bug production như thế nào?**
> �� STAR: Situation → Task → Action (Reproduce → Logs → Isolate → Fix → Test → Deploy) → Result + Lessons learned

---

## 📅 KẾ HOẠCH ÔN TẬP 2 TUẦN

### Tuần 1: Nền Tảng

| Ngày | Chủ đề | Hành động |
|---|---|---|
| T2 | Python cơ bản + OOP | Ôn Phần 1-2, code lại ví dụ |
| T3 | SQL + PostgreSQL | Ôn Phần 4-5, luyện query |
| T4 | ERP concepts + Setup Odoo | Đọc Phần 6 + Cài Docker |
| T5 | Odoo Models, Fields, ORM | Code Phần 7 |
| T6 | Odoo Views, Security | Code Phần 8.4-8.6 |
| T7 | Mini project: tạo 1 Odoo module hoàn chỉnh | Tự code |

### Tuần 2: Nâng Cao & Phỏng Vấn

| Ngày | Chủ đề | Hành động |
|---|---|---|
| T2 | Odoo nâng cao: Inheritance, Domain | Phần 8.1-8.3 |
| T3 | OWL / QWeb + Controllers | Phần 9 + 8.7 |
| T4 | API Integration + Cron | Phần 10 |
| T5 | Python nâng cao + Debugging | Phần 3 + 11 |
| T6 | Mock interview: tất cả câu hỏi | Phần 14 |
| T7 | Nghiên cứu công ty + chuẩn bị câu chuyện CV | Research |

---

## 🛠️ SETUP MÔI TRƯỜNG THỰC HÀNH

```bash
# Cài Odoo 16 bằng Docker (nhanh nhất)
docker run -d \
  -e POSTGRES_USER=odoo \
  -e POSTGRES_PASSWORD=odoo \
  -e POSTGRES_DB=postgres \
  --name db postgres:15

docker run -d \
  -p 8069:8069 \
  --name odoo \
  --link db:db \
  -v $(pwd)/custom_addons:/mnt/extra-addons \
  odoo:16.0

# Truy cập: http://localhost:8069
# Login: admin / admin

# Tạo module skeleton
cd custom_addons
mkdir -p my_module/{models,views,security,data,controllers,wizard,static/src/{js,xml,css}}
touch my_module/__init__.py
touch my_module/__manifest__.py
touch my_module/models/__init__.py
```

---

## 📚 TÀI LIỆU THAM KHẢO

| Tài liệu | Link | Ưu tiên |
|---|---|---|
| Odoo Developer Docs | https://www.odoo.com/documentation/16.0/developer.html | 🔴 Bắt buộc |
| OWL Framework | https://github.com/odoo/owl | 🟡 Quan trọng |
| Odoo Community (OCA) | https://github.com/OCA | 🟢 Code thực tế |
| PostgreSQL Docs | https://www.postgresql.org/docs/15/ | 🟡 Quan trọng |

---

> **Điểm mạnh nhấn mạnh:**
> ✅ Python thực tiễn (Flask, SQLAlchemy, Docker)
> ✅ Database đa dạng (PostgreSQL, MySQL, MongoDB)
> ✅ Tích hợp multi-platform (eCommerce Migration)
> ✅ Full-stack (backend + frontend)

> **Điểm cần chuẩn bị trả lời:**
> ⚠️ Chưa có kinh nghiệm Odoo → Nền tảng Python vững + khả năng học nhanh
> ⚠️ Kinh nghiệm < 3 năm → Nhấn chất lượng dự án, không chỉ số năm
> ⚠️ Chưa biết ERP → Đọc Phần 6, tìm hiểu Sales/Purchase/Inventory/Accounting
