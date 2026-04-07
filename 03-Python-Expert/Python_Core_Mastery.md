# 🐍 PYTHON CORE MASTERY: TỪ ZER0 ĐẾN HERO (CƠ BẢN - NÂNG CAO)

Tài liệu này tập trung vào ngôn ngữ Python thuần (Core). Hiểu sâu ngôn ngữ là điều kiện tiên quyết để trở thành một Senior sử dụng thành thạo mọi Framework.

---

## 📋 MỤC LỤC
1. [**CƠ BẢN: CÚ PHÁP VÀ KIỂU DỮ LIỆU TỐI ƯU**](#1-cơ-bản-cú-pháp-và-kiểu-dữ-liệu-tối-ưu)
2. [**TRUNG CẤP: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (OOP) VÀ DECORATORS**](#2-trung-cấp-lập-trình-hướng-đối-tượng-oop-và-decorators)
3. [**NÂNG CAO: ASYNCIO, METACLASS VÀ QUẢN LÝ BỘ NHỚ**](#3-nâng-cao-asyncio-metaclass-và-quản-lý-bộ-nhớ)
4. [**PHƯƠNG THỨC MA THUẬT: MAGIC METHODS (DUNDER)**](#4-phương-thức-ma-thuật-magic-methods-dunder)

---

## 🟢 1. CƠ BẢN: CÚ PHÁP VÀ KIỂU DỮ LIỆU TỐI ƯU

### 📦 A. List, Dict, Set Comprehension
Cách viết code "chuẩn Python" (Pythonic) tối ưu tốc độ và độ sạch:
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

### 🧱 B. Unpacking và *args, **kwargs
Linh hoạt trong việc nhận tham số không giới hạn:
```python
def senior_function(*args, **kwargs):
    # args là một tuple chứa các tham số không tên
    # kwargs là một dict chứa các tham số có tên
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

#### 💡 TÁC ĐỘNG THỰC TẾ (IMPACT):
- **Hiệu năng:** Comprehensions chạy nhanh hơn vòng lặp `for` thông thường vì nó được tối ưu hóa ở tầng C-Level của Python.
- **Duy trì (Maintenance):** Viết code trên 1 dòng giúp giảm "độ loãng" của file code, giúp đồng nghiệp nắm bắt logic nhanh hơn.
- **Linh hoạt:** `*args/**kwargs` cho phép bạn viết các hàm Wrapper hoặc Decorator cực kỳ mạnh mẽ mà không cần biết hàm gốc nhận bao nhiêu tham số.

---

## 🟡 2. TRUNG CẤP: OOP VÀ DECORATORS

### 🧬 A. Lập trình hướng đối tượng (OOP)
```python
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property # Biến hàm thành thuộc tính (chỉ đọc)
    def salary_info(self):
        return f"Employee {self._name} has salary {self._salary}"

# Kế thừa
class Manager(Employee):
    def get_role(self):
        return "Admin Manager"
```

### 🎨 B. Decorators (Cực kỳ quan trọng)
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

complex_task()
```

### 🚪 C. Context Managers (`with` statement)
```python
class DatabaseConnection:
    """Tự động đóng kết nối sau khi dùng xong"""
    def __enter__(self):
        print("Mở kết nối tới Database...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Đóng kết nối an toàn.")

#### 💡 TÁC ĐỘNG THỰC TẾ (IMPACT):
- **Kiến trúc (Architecture):** OOP giúp bạn đóng gói các logic nghiệp vụ phức tạp. `@property` giúp bạn thay đổi logic tính toán bên trong mà không làm hỏng giao thức bên ngoài.
- **Tái sử dụng (Reusability):** Decorators cho phép bạn "cấy" các tính năng như Logging, Auth, Caching vào hàng trăm hàm chỉ bằng 1 dòng code. Đây là đỉnh cao của DRY (Don't Repeat Yourself).
- **An toàn (Safety):** Context Managers đảm bảo file/kết nối DB luôn được đóng kể cả khi có lỗi xảy ra (Exception). Đây là cách Senior ngăn chặn lỗi rò rỉ bộ nhớ (Memory Leak).

---

## 🔴 3. NÂNG CAO: ASYNCIO VÀ METACLASS

### 🚀 A. AsyncIO (Xử lý bất đồng bộ)
```python
import asyncio

async def fetch_data(id):
    print(f"Bắt đầu lấy dữ liệu {id}...")
    await asyncio.sleep(2) # Giả lập chờ API
    return f"Data {id} xong!"

async def main():
    # Chạy song song nhiều tác vụ
    results = await asyncio.gather(fetch_data(1), fetch_data(2))
    print(results)

#### 💡 TÁC ĐỘNG THỰC TẾ (IMPACT):
- **Khả năng mở rộng (Scalability):** AsyncIO là sự khác biệt giữa một hệ thống phục vụ 100 người và một hệ thống phục vụ 100,000 người. Nó biến Python từ "chậm chân" thành "vận động viên marathon" trong thế giới Web.
- **Tự động hóa (Automation):** Metaclass cho phép bạn thực thi logic ngay khi bạn *viết* code (compile time/import time). Nó giúp xây dựng các hệ thống tự động kiểm tra lỗi cấu trúc trước khi app chạy.
- **Đóng gói (Encapsulation):** Magic methods giúp các đối tượng của bạn cư xử như tệp tin, như mảng, hoặc như hàm, tạo ra một giao thức (interface) cực kỳ thân thiện cho người dùng thư viện của bạn.

---

## 🧙 4. CÁC PHƯƠNG THỨC MA THUẬT (MAGIC METHODS)

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

sl = SuperList(["Python", "Flask", "Django"])
print(sl())     # Gọi __call__
print(sl[0])    # Gọi __getitem__
```

---
🚀 **Triết lý Python:** Beautiful is better than ugly. Explicit is better than implicit. Hãy viết code sạch, bạn sẽ thành công!
