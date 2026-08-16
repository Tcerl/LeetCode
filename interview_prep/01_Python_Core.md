# 🐍 PYTHON CORE - ÔN THI PHỎNG VẤN

---

## 1. KIỂU DỮ LIỆU CƠ BẢN

### 1.1 Mutable vs Immutable
```python
# IMMUTABLE (không thể thay đổi sau khi tạo)
x = "hello"     # str
y = (1, 2, 3)   # tuple
z = 42          # int
f = 3.14        # float
b = True        # bool

# MUTABLE (có thể thay đổi)
lst = [1, 2, 3]   # list
d = {"a": 1}      # dict
s = {1, 2, 3}     # set
```

> **🎯 Dùng khi nào?**
> - **Immutable**: Dùng làm dictionary key, thread-safe, bảo vệ dữ liệu không bị thay đổi ngoài ý muốn
> - **Mutable**: Khi cần thêm/xóa/sửa dữ liệu linh hoạt trong runtime

> **❓ Câu hỏi hay gặp:** "Tại sao tuple nhanh hơn list?"
> → Vì tuple được lưu ở bộ nhớ cố định, ít overhead hơn. Python cũng cache tuple nhỏ.

---

### 1.2 List Comprehension vs Generator Expression
```python
# List comprehension - tạo ngay toàn bộ list trong RAM
squares = [x**2 for x in range(1000000)]  # chiếm nhiều RAM

# Generator expression - lazy evaluation, tiết kiệm RAM
squares_gen = (x**2 for x in range(1000000))  # chỉ tính khi cần
next(squares_gen)  # lấy từng phần tử

# Dictionary comprehension
d = {k: v for k, v in zip("abc", [1, 2, 3])}
# {'a': 1, 'b': 2, 'c': 3}

# Set comprehension
unique = {x % 3 for x in range(10)}
# {0, 1, 2}
```

> **🎯 Dùng khi nào?**
> - **List comprehension**: Khi cần toàn bộ kết quả ngay, dataset nhỏ/vừa
> - **Generator**: Khi xử lý file lớn, streaming data, pipeline transform

---

## 2. HÀM VÀ CLOSURES

### 2.1 *args và **kwargs
```python
def func(*args, **kwargs):
    """
    args  -> tuple các positional arguments
    kwargs -> dict các keyword arguments
    """
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

func(1, 2, 3, name="Tin", age=22)
# 1, 2, 3
# name = Tin, age = 22
```

> **🎯 Dùng khi nào?**
> - Viết hàm linh hoạt (wrapper, middleware)
> - Kế thừa và mở rộng hàm cha mà không biết trước tham số

---

### 2.2 Closures
```python
def make_multiplier(n):
    """Closure: hàm bên trong nhớ biến của hàm bên ngoài"""
    def multiplier(x):
        return x * n  # nhớ 'n' từ outer scope
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15
```

> **🎯 Dùng khi nào?**
> - Tạo factory functions
> - Encapsulate state mà không cần class
> - Dùng trong decorators

---

### 2.3 Lambda Functions
```python
### 2.3 Lambda Functions
Lambda là **hàm ẩn danh** (anonymous function), không có tên, dùng cho các biểu thức ngắn gọn.
**Cú pháp:** `lambda arguments: expression`

> **🎯 Dùng trong trường hợp nào?**
> 1. **Custom Sorting (Phổ biến nhất):** Làm `key` cho `sorted()`, `min()`, `max()`. 
>    *Ví dụ:* `sorted(data, key=lambda x: x['age'])`
> 2. **Higher-order Functions:** Kết hợp với `map()`, `filter()`, `reduce()` để xử lý list nhanh.
> 3. **Callbacks:** Truyền vào các hàm nhận tham số là hàm (như `df.apply()` trong Pandas hoặc các nút bấm trong giao diện GUI).
> 4. **Hàm dùng một lần:** Khi logic quá đơn giản, không cần thiết phải định nghĩa bằng `def`.

> **⚠️ Khi nào KHÔNG nên dùng?**
> - Khi logic phức tạp (có nhiều câu lệnh `if/else` hoặc vòng lặp).
> - Khi cần tái sử dụng hàm ở nhiều nơi khác nhau.
> - Khi việc dùng lambda làm code trở nên khó đọc (vi phạm triết lý "Readability counts" của Python).

```python
# Ví dụ thực tế
data = [{"name": "B", "age": 25}, {"name": "A", "age": 20}]
# Sắp xếp danh sách theo tuổi
sorted_data = sorted(data, key=lambda x: x["age"])

# map và filter
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, nums))     # [2, 4, 6, 8, 10]
evens = list(filter(lambda x: x%2==0, nums)) # [2, 4]
``````

> **🎯 Dùng khi nào?**
> - Hàm đơn giản, dùng 1 lần, không cần đặt tên
> - Làm tham số cho `sorted()`, `map()`, `filter()`

---

## 3. DECORATORS

### 3.1 Decorator cơ bản
```python
import functools
import time

def timer(func):
    """Decorator đo thời gian thực thi hàm"""
    @functools.wraps(func)  # giữ lại metadata của func gốc
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()  # slow_function took 1.0001s
```

### 3.2 Decorator có tham số
```python
def retry(max_attempts=3, delay=1):
    """Decorator retry khi hàm thất bại"""
    def decorator(func):
        @functools.wraps(func)
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
def call_api():
    # Có thể fail, sẽ tự retry
    pass
```

### 3.3 Class-based Decorator
```python
class cache:
    """Decorator cache kết quả hàm"""
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

> **🎯 Dùng khi nào?**
> - **Logging/Timing**: Theo dõi performance
> - **Authentication**: `@login_required` trong Flask
> - **Caching**: Cache kết quả tốn kém
> - **Retry**: Gọi API không ổn định
> - **Rate limiting**: Giới hạn tốc độ gọi hàm

---

## 4. GENERATORS VÀ ITERATORS

### 4.1 Generator Functions (yield)
```python
def read_large_file(filepath):
    """Generator đọc file lớn từng dòng - không load hết vào RAM"""
    with open(filepath) as f:
        for line in f:
            yield line.strip()  # trả về từng dòng

# Xử lý file log gigabyte mà không hết RAM
for line in read_large_file("huge_log.txt"):
    process(line)

# Generator pipeline
def parse_json_lines(lines):
    import json
    for line in lines:
        yield json.loads(line)

def filter_errors(records):
    for record in records:
        if record.get("level") == "ERROR":
            yield record

# Kết hợp pipeline
lines = read_large_file("app.log")
records = parse_json_lines(lines)
errors = filter_errors(records)
```

### 4.2 Generator với send()
```python
def accumulator():
    """Generator 2 chiều - nhận và gửi dữ liệu"""
    total = 0
    while True:
        value = yield total  # yield trả giá trị, nhận giá trị mới
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)        # khởi động generator
gen.send(10)     # total = 10
gen.send(20)     # total = 30
gen.send(5)      # total = 35
```

> **🎯 Dùng khi nào?**
> - Xử lý file/data lớn (ETL pipeline)
> - Streaming response từ API
> - Infinite sequences (ID generator, timestamp stream)
> - Khi bạn làm **eCommerce migration** - đọc hàng nghìn records mà không OOM

---

## 5. OOP - LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG

### 5.1 4 Tính chất OOP
```python
# 1. ENCAPSULATION - đóng gói
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private (name mangling: _BankAccount__balance)
        self._owner = "Tin"       # protected (convention)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    @property
    def balance(self):  # getter
        return self.__balance


# 2. INHERITANCE - kế thừa
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# 3. POLYMORPHISM - đa hình
animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())  # gọi đúng method của từng class


# 4. ABSTRACTION - trừu tượng hóa
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount): pass

    @abstractmethod
    def refund(self, transaction_id): pass

class StripeGateway(PaymentGateway):
    def pay(self, amount):
        # gọi Stripe API
        pass
    def refund(self, transaction_id):
        pass
```

### 5.2 Dunder Methods (Magic Methods)
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):  # repr cho developer
        return f"Vector({self.x}, {self.y})"

    def __str__(self):   # str cho user
        return f"({self.x}, {self.y})"

    def __add__(self, other):  # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):   # len(v)
        return 2

    def __eq__(self, other):  # v1 == v2
        return self.x == other.x and self.y == other.y

    def __iter__(self):  # for val in v
        yield self.x
        yield self.y
```

### 5.3 Class Methods vs Static Methods vs Properties
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        """Instance method giả thành attribute"""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Factory method - tạo instance từ Fahrenheit"""
        return cls((fahrenheit - 32) * 5/9)

    @staticmethod
    def is_freezing(celsius):
        """Utility method - không cần self hay cls"""
        return celsius <= 0

t = Temperature(100)
print(t.fahrenheit)              # 212.0
t.fahrenheit = 32               # setter
t2 = Temperature.from_fahrenheit(98.6)  # classmethod
print(Temperature.is_freezing(-5))      # True
```

> **🎯 Dùng khi nào?**
> - `@property`: Computed attributes, validate khi set giá trị
> - `@classmethod`: Factory pattern, alternative constructors
> - `@staticmethod`: Utility functions liên quan đến class nhưng không cần state

---

## 6. CONTEXT MANAGERS

```python
# Cách 1: Dùng class
class DatabaseConnection:
    def __enter__(self):
        self.conn = connect_to_db()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()  # luôn đóng dù có lỗi hay không
        return False  # không suppress exception

with DatabaseConnection() as conn:
    conn.execute("SELECT * FROM users")

# Cách 2: Dùng contextlib
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield  # code trong 'with' block chạy ở đây
    print(f"Elapsed: {time.time()-start:.4f}s")

with timer():
    time.sleep(1)
```

> **🎯 Dùng khi nào?**
> - **File I/O**: `with open(...) as f`
> - **Database**: Mở/đóng connection, transaction
> - **Locks**: Thread/process locking
> - **Temporary state**: Thay đổi config tạm thời

---

## 7. EXCEPTION HANDLING

```python
class AppError(Exception):
    """Base exception cho ứng dụng"""
    pass

class ValidationError(AppError):
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"Validation error on {field}: {message}")

class DatabaseError(AppError):
    pass

# Xử lý exception đúng cách
def process_payment(amount):
    try:
        if amount <= 0:
            raise ValidationError("amount", "Must be positive")
        result = payment_gateway.charge(amount)
        return result
    except ValidationError:
        raise  # re-raise, không nuốt
    except ConnectionError as e:
        raise DatabaseError(f"Payment gateway down: {e}") from e
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        raise
    finally:
        logger.info(f"Payment attempt for {amount} completed")
```

> **🎯 Dùng khi nào?**
> - Tạo exception hierarchy cho từng module
> - `finally`: Cleanup (đóng file, connection)
> - `raise ... from e`: Chain exception giữ traceback gốc

---

## 8. CONCURRENCY

### 8.1 Threading vs Multiprocessing vs AsyncIO
```python
import threading
import multiprocessing
import asyncio

# THREADING - I/O bound tasks
def fetch_data(url):
    import requests
    return requests.get(url).json()

threads = [threading.Thread(target=fetch_data, args=(url,))
           for url in urls]
for t in threads: t.6start()
for t in threads: t.join()

# MULTIPROCESSING - CPU bound tasks
def compute(n):
    return sum(i*i for i in range(n))

with multiprocessing.Pool() as pool:
    results = pool.map(compute, [10**6, 10**6, 10**6])

# ASYNCIO - Many concurrent I/O (best for APIs)
async def fetch_async(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
```

> **🎯 Dùng khi nào?**
> - **Threading**: Gọi nhiều API cùng lúc, I/O bound (bị GIL hạn chế CPU)
> - **Multiprocessing**: Xử lý ảnh, ML inference, tính toán nặng
> - **AsyncIO**: Web server, chat app, many concurrent connections (Flask async, FastAPI)

---

## 9. TYPE HINTS & DATACLASSES

```python
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class Candidate:
    name: str
    email: str
    age: int
    skills: List[str] = field(default_factory=list)
    score: Optional[float] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        """Validation sau khi __init__"""
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        self.email = self.email.lower()

# Type hints cho functions
def calculate_match_score(
    candidate: Candidate,
    job_requirements: List[str]
) -> float:
    """Tính điểm phù hợp của ứng viên"""
    matching = set(candidate.skills) & set(job_requirements)
    return len(matching) / len(job_requirements) * 100
```

> **🎯 Dùng khi nào?**
> - **Dataclass**: Data containers, DTOs, replace simple classes
> - **Type hints**: Mọi hàm trong production code, IDE support, mypy checking

---

## 10. PYTHON MEMORY MODEL

```python
# is vs ==
a = [1, 2, 3]
b = a       # cùng object trong memory
c = a[:]    # copy mới

print(a is b)   # True - cùng địa chỉ memory
print(a is c)   # False - khác địa chỉ
print(a == c)   # True - cùng giá trị

# Shallow copy vs Deep copy
import copy

lst = [[1, 2], [3, 4]]
shallow = lst.copy()      # List mới nhưng elements vẫn refer cùng objects
deep = copy.deepcopy(lst) # Clone hoàn toàn

lst[0].append(99)
print(shallow[0])  # [1, 2, 99] - bị ảnh hưởng!
print(deep[0])     # [1, 2] - không bị ảnh hưởng

# Integer caching (-5 đến 256)
a = 256
b = 256
print(a is b)  # True (cached)

a = 257
b = 257
print(a is b)  # False (not cached)
```

> **🎯 Quan trọng khi phỏng vấn:** Biết phân biệt `is` (identity) và `==` (equality)

---

## ✅ CHECKLIST PYTHON CORE

- [ ] Phân biệt mutable/immutable và hậu quả
- [ ] Viết được decorator từ đầu
- [ ] Giải thích generator vs list comprehension
- [ ] 4 tính chất OOP với ví dụ thực tế
- [ ] Khi nào dùng threading vs multiprocessing vs asyncio
- [ ] Context manager với `__enter__`/`__exit__`
- [ ] `is` vs `==`, shallow vs deep copy
