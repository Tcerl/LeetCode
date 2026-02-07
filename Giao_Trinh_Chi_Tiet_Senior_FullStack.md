# GIÁO TRÌNH CHI TIẾT - SENIOR FULL STACK DEVELOPER

> Giáo trình đầy đủ và chi tiết dựa trên Roadmap Tăng Tốc, bao gồm lý thuyết, ví dụ code, best practices và bài tập thực hành.

---

# MỤC LỤC

1. [GIAI ĐOẠN 1: NỀN TẢNG TỐC ĐỘ](#giai-đoạn-1-nền-tảng-tốc-độ)
2. [GIAI ĐOẠN 2: FULL STACK WEB](#giai-đoạn-2-full-stack-web)
3. [GIAI ĐOẠN 3: MOBILE DEVELOPMENT](#giai-đoạn-3-mobile-development)
4. [GIAI ĐOẠN 4: NÂNG CAO &amp; CHUYÊN SÂU](#giai-đoạn-4-nâng-cao--chuyên-sâu)
5. [GIAI ĐOẠN 5: PORTFOLIO &amp; CHUYÊN NGHIỆP](#giai-đoạn-5-portfolio--chuyên-nghiệp)

---

# GIAI ĐOẠN 1: NỀN TẢNG TỐC ĐỘ (Tháng 1-3)

## TUẦN 1-2: Tư duy lập trình + Python cơ bản

### 1.1. Python Cơ Bản

#### Variables và Data Types

**Kiến thức:**

- **Định nghĩa:** Biến là tên tham chiếu tới giá trị trong bộ nhớ; kiểu dữ liệu (int/float/string/bool/None) mô tả dạng giá trị và cách thao tác với nó.
- Variables: Biến lưu trữ dữ liệu
- Data Types: int, float, string, bool, None
- Type conversion: int(), float(), str(), bool()
- Dynamic typing: Python tự động xác định kiểu

**Ví dụ code:**

```python
# Variables
name = "Nguyen Van A"
age = 25
height = 1.75
is_student = True

# Type conversion
age_str = str(age)  # "25"
age_int = int("25")  # 25

# Multiple assignment
x, y, z = 1, 2, 3
```

**Best Practices:**

- Đặt tên biến có ý nghĩa (snake_case)
- Sử dụng type hints khi có thể
- Tránh đặt tên biến trùng với keywords

**Bài tập:**

1. Tạo biến lưu thông tin cá nhân (tên, tuổi, địa chỉ)
2. Thực hiện các phép toán cơ bản
3. Chuyển đổi giữa các kiểu dữ liệu

#### Operators

**Kiến thức:**

- **Định nghĩa:** Toán tử là ký hiệu thực hiện phép tính trên toán hạng (số/chuỗi/biến), trả về giá trị mới.
- Arithmetic: +, -, *, /, //, %, **
- Comparison: ==, !=, <, >, <=, >=
- Logical: and, or, not
- Assignment: =, +=, -=, *=, /=
- Membership: in, not in
- Identity: is, is not

**Ví dụ code:**

```python
# Arithmetic
result = 10 + 5  # 15
result = 10 // 3  # 3 (floor division)
result = 10 % 3  # 1 (modulo)
result = 2 ** 3  # 8 (exponentiation)

# Logical
if age >= 18 and is_student:
    print("Adult student")

# Membership
if "a" in "apple":
    print("Found")
```

#### Control Flow: If/Else và Loops

**Kiến thức:**

- **Định nghĩa:** Cấu trúc điều khiển quyết định đường đi của chương trình (rẽ nhánh if/else, lặp for/while) dựa trên điều kiện và số lần lặp.
- if/elif/else: Điều kiện rẽ nhánh
- for loop: Lặp qua iterable
- while loop: Lặp khi điều kiện đúng
- break, continue: Điều khiển vòng lặp
- range(): Tạo dãy số

**Ví dụ code:**

```python
# If/Else
age = 20
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# For loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for item in [1, 2, 3, 4, 5]:
    print(item)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break và Continue
for i in range(10):
    if i == 3:
        continue  # Bỏ qua 3
    if i == 7:
        break  # Dừng tại 7
    print(i)
```

**Best Practices:**

- Sử dụng list comprehension khi có thể
- Tránh nested loops quá sâu
- Sử dụng enumerate() khi cần index

**Bài tập:**

1. Viết chương trình kiểm tra số chẵn/lẻ
2. Tính tổng từ 1 đến n
3. Tìm số lớn nhất trong list

#### Functions

**Kiến thức:**

- **Định nghĩa:** Hàm là khối mã có tên, nhận tham số, trả về giá trị, giúp tái sử dụng và đóng gói logic.
- Function definition: def
- Parameters và Arguments
- Return values
- Default parameters
- *args và **kwargs
- Lambda functions
- Scope: local, global, nonlocal

**Ví dụ code:**

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default parameters
def power(base, exponent=2):
    return base ** exponent

# *args và **kwargs
def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda
square = lambda x: x ** 2

# Scope
x = 10  # global

def func():
    x = 20  # local
    print(x)  # 20

func()
print(x)  # 10
```

**Best Practices:**

- Một function chỉ làm một việc (Single Responsibility)
- Đặt tên function mô tả rõ ràng
- Sử dụng type hints
- Giữ function ngắn gọn (< 50 dòng)

**Bài tập:**

1. Viết function tính giai thừa
2. Viết function kiểm tra số nguyên tố
3. Viết function tìm số lớn nhất trong list

#### Modules và Packages

**Kiến thức:**

- **Định nghĩa:** Module là file Python chứa hàm/lớp/biến; Package là tập hợp modules có `__init__.py`, giúp tổ chức và tái sử dụng code.
- Import modules: import, from...import
- Tạo module riêng
- Standard library: os, sys, datetime, json, etc.
- Package structure

**Ví dụ code:**

```python
# Import
import math
from math import sqrt, pi
import datetime as dt

# Sử dụng
result = math.sqrt(16)
result = sqrt(16)
now = dt.datetime.now()

# Tạo module riêng
# file: utils.py
def add(a, b):
    return a + b

# file: main.py
from utils import add
result = add(1, 2)
```

**Best Practices:**

- Tổ chức code thành modules hợp lý
- Sử dụng __init__.py cho packages
- Tránh circular imports

#### List và Dictionary

**Kiến thức:**

- **Định nghĩa:** List là cấu trúc có thứ tự, thay đổi được; Dictionary là ánh xạ key → value (key duy nhất), tra cứu nhanh theo key.

**List:**

- Tạo list: [], list()
- Indexing và slicing
- Methods: append(), extend(), insert(), remove(), pop()
- List comprehension
- Nested lists

**Dictionary:**

- Tạo dict: {}, dict()
- Keys và values
- Methods: get(), keys(), values(), items()
- Dictionary comprehension
- Nested dictionaries

**Ví dụ code:**

```python
# List
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.extend([7, 8])
first = numbers[0]
last = numbers[-1]
sublist = numbers[1:4]  # [2, 3, 4]

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]

# Dictionary
person = {
    "name": "Nguyen Van A",
    "age": 25,
    "city": "Hanoi"
}
person["email"] = "a@example.com"
age = person.get("age", 0)  # 25

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}

# Nested
students = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 21}
]
```

**Best Practices:**

- Sử dụng list comprehension cho code ngắn gọn
- Sử dụng .get() thay vì [] để tránh KeyError
- Hiểu về mutability của list và dict

**Bài tập:**

1. Tạo list và thực hiện các operations
2. Tạo dictionary lưu thông tin sinh viên
3. Sử dụng list/dict comprehension

#### File I/O

**Kiến thức:**

- **Định nghĩa:** Đọc/ghi dữ liệu từ/đến file (text/binary) thông qua hàm open và các phương thức đọc/ghi; dùng context manager để tự động đóng file.
- Mở file: open()
- Đọc file: read(), readline(), readlines()
- Ghi file: write(), writelines()
- Context manager: with statement
- JSON: json.load(), json.dump()
- CSV: csv.reader(), csv.writer()

**Ví dụ code:**

```python
# Đọc file
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
    lines = f.readlines()

# Ghi file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello World\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# JSON
import json
data = {"name": "A", "age": 25}
with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    data = json.load(f)

# CSV
import csv
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

**Best Practices:**

- Luôn sử dụng with statement
- Chỉ định encoding (utf-8)
- Xử lý exceptions khi đọc/ghi file

**Bài tập:**

1. Đọc file và đếm số dòng
2. Ghi danh sách vào file JSON
3. Đọc CSV và xử lý dữ liệu

#### Exception Handling

**Kiến thức:**

- **Định nghĩa:** Cơ chế bắt và xử lý lỗi runtime (exceptions) để chương trình không sập; có thể log, phục hồi, hoặc dừng an toàn.
- try/except/else/finally
- Các loại exceptions: ValueError, TypeError, FileNotFoundError, etc.
- Raise exceptions: raise
- Custom exceptions
- Exception chaining

**Ví dụ code:**

```python
# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions
try:
    number = int(input("Enter number: "))
    result = 10 / number
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")
finally:
    print("Always executed")

# Raise exception
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Custom exception
class CustomError(Exception):
    pass

raise CustomError("Custom error message")
```

**Best Practices:**

- Cụ thể hóa exception types
- Không bỏ qua exceptions (silent failures)
- Log exceptions đầy đủ
- Sử dụng finally cho cleanup

**Bài tập:**

1. Xử lý exception khi đọc file không tồn tại
2. Validate input và raise custom exception
3. Xử lý multiple exceptions

### 1.2. LeetCode Practice

**Mục tiêu:** Giải 20 bài LeetCode Easy

**Các bài đề xuất:**

1. Two Sum
2. Reverse Integer
3. Palindrome Number
4. Roman to Integer
5. Valid Parentheses
6. Merge Two Sorted Lists
7. Remove Duplicates from Sorted Array
8. Remove Element
9. Implement strStr()
10. Search Insert Position
11. Plus One
12. Add Binary
13. Sqrt(x)
14. Climbing Stairs
15. Remove Duplicates from Sorted List
16. Same Tree
17. Maximum Depth of Binary Tree
18. Symmetric Tree
19. Best Time to Buy and Sell Stock
20. Single Number

**Chiến lược:**

- Đọc kỹ đề bài
- Nghĩ về edge cases
- Viết pseudocode trước
- Implement và test
- Optimize nếu cần

### 1.3. Projects

#### Project 1: Calculator App

**Yêu cầu:**

- Cộng, trừ, nhân, chia
- Xử lý lỗi (chia cho 0)
- Lịch sử tính toán
- Lưu vào file

**Ví dụ code:**

```python
class Calculator:
    def __init__(self):
        self.history = []
  
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
  
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
  
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
  
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
  
    def save_history(self, filename):
        with open(filename, "w") as f:
            for entry in self.history:
                f.write(entry + "\n")
```

#### Project 2: Todo List

**Yêu cầu:**

- Thêm, xóa, sửa task
- Đánh dấu hoàn thành
- Lưu vào file JSON
- Tìm kiếm task

**Ví dụ code:**

```python
import json
from datetime import datetime

class TodoList:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
  
    def load_todos(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
  
    def save_todos(self):
        with open(self.filename, "w") as f:
            json.dump(self.todos, f, indent=2)
  
    def add(self, task):
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.todos.append(todo)
        self.save_todos()
        return todo
  
    def complete(self, todo_id):
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                self.save_todos()
                return todo
        return None
  
    def delete(self, todo_id):
        self.todos = [t for t in self.todos if t["id"] != todo_id]
        self.save_todos()
  
    def search(self, keyword):
        return [t for t in self.todos if keyword.lower() in t["task"].lower()]
```

---

## TUẦN 3-4: Cấu trúc dữ liệu cơ bản

### 2.1. Array (Mảng)

**Kiến thức:**

- Array là cấu trúc dữ liệu lưu trữ các phần tử liên tiếp trong bộ nhớ
- Index bắt đầu từ 0
- Time complexity:
  - Access: O(1) - Truy cập trực tiếp qua index
  - Search: O(n) - Phải duyệt từng phần tử
  - Insert: O(n) - Phải dịch chuyển các phần tử sau vị trí chèn
  - Delete: O(n) - Phải dịch chuyển các phần tử sau vị trí xóa

**Giải thích chi tiết:**

1. **Cách hoạt động:**
   - Array lưu các phần tử ở các vị trí bộ nhớ liên tiếp
   - Mỗi phần tử có địa chỉ = địa chỉ đầu + index × kích thước phần tử
   - Truy cập O(1) vì tính toán trực tiếp địa chỉ, không cần duyệt

2. **Khi nào dùng Array:**
   - Cần truy cập nhanh qua index
   - Kích thước cố định hoặc biết trước
   - Dữ liệu đồng nhất (cùng kiểu)
   - Không cần insert/delete thường xuyên

3. **Ưu điểm:**
   - Truy cập nhanh O(1)
   - Cache-friendly (dữ liệu liên tiếp)
   - Đơn giản, dễ hiểu

4. **Nhược điểm:**
   - Kích thước cố định (trong một số ngôn ngữ)
   - Insert/Delete chậm O(n)
   - Tốn bộ nhớ nếu không dùng hết

**Implement từ đầu:**

```python
class Array:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
  
    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of range")
  
    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")
  
    def append(self, value):
        if self.size >= self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1
  
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size >= self.capacity:
            self._resize()
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = value
        self.size += 1
  
    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i+1]
        self.size -= 1
  
    def _resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
  
    def __len__(self):
        return self.size
  
    def __str__(self):
        return str([self.data[i] for i in range(self.size)])
```

**Hướng giải quyết bài toán với Array:**

#### Bài toán 1: Two Sum (LeetCode 1)
**Đề bài:** Tìm 2 số trong mảng có tổng bằng target.

**Phân tích:**
- Dùng hash map để lưu số đã xem và index của nó
- Duyệt mảng, với mỗi số kiểm tra xem (target - số hiện tại) có trong map không

**Giải pháp:**
```python
def two_sum(nums, target):
    """
    Time: O(n) - Duyệt mảng 1 lần
    Space: O(n) - Hash map lưu tối đa n phần tử
    """
    seen = {}  # {value: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

# Ví dụ
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # [0, 1] vì nums[0] + nums[1] = 2 + 7 = 9
```

**Giải thích từng bước:**
1. Khởi tạo hash map `seen` để lưu số đã xem
2. Duyệt từng phần tử trong mảng
3. Với mỗi số, tính `complement = target - num`
4. Nếu `complement` đã có trong map → tìm thấy cặp số
5. Nếu chưa, lưu số hiện tại vào map để dùng sau

#### Bài toán 2: Best Time to Buy and Sell Stock (LeetCode 121)
**Đề bài:** Tìm lợi nhuận tối đa khi mua bán cổ phiếu (chỉ được mua 1 lần, bán 1 lần).

**Phân tích:**
- Duyệt mảng giá, lưu giá mua thấp nhất
- Với mỗi giá, tính lợi nhuận nếu bán ở giá này
- Cập nhật lợi nhuận tối đa

**Giải pháp:**
```python
def max_profit(prices):
    """
    Time: O(n) - Duyệt mảng 1 lần
    Space: O(1) - Chỉ dùng biến
    """
    if not prices:
        return 0
    
    min_price = prices[0]  # Giá mua thấp nhất
    max_profit = 0  # Lợi nhuận tối đa
    
    for price in prices[1:]:
        # Cập nhật giá mua thấp nhất
        min_price = min(min_price, price)
        # Tính lợi nhuận nếu bán ở giá hiện tại
        profit = price - min_price
        # Cập nhật lợi nhuận tối đa
        max_profit = max(max_profit, profit)
    
    return max_profit

# Ví dụ
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))  # 5 (mua ở 1, bán ở 6)
```

**Giải thích từng bước:**
1. Khởi tạo `min_price` = giá đầu tiên, `max_profit` = 0
2. Duyệt từ giá thứ 2 trở đi
3. Cập nhật `min_price` nếu giá hiện tại thấp hơn
4. Tính lợi nhuận = giá hiện tại - min_price
5. Cập nhật max_profit nếu lợi nhuận lớn hơn

#### Bài toán 3: Container With Most Water (LeetCode 11)
**Đề bài:** Tìm 2 cột nước tạo thành container có thể tích lớn nhất.

**Phân tích:**
- Dùng Two Pointers: bắt đầu từ 2 đầu mảng
- Thể tích = min(height[left], height[right]) × (right - left)
- Di chuyển pointer có chiều cao nhỏ hơn

**Giải pháp:**
```python
def max_area(height):
    """
    Time: O(n) - Two pointers duyệt mảng 1 lần
    Space: O(1) - Chỉ dùng biến
    """
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # Tính diện tích hiện tại
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)
        
        # Di chuyển pointer có chiều cao nhỏ hơn
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Ví dụ
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))  # 49
```

**Giải thích từng bước:**
1. Khởi tạo 2 pointers ở đầu và cuối mảng
2. Tính diện tích = min(2 cột) × khoảng cách
3. Cập nhật max_area
4. Di chuyển pointer có chiều cao nhỏ hơn (vì giữ cột cao hơn sẽ có cơ hội tạo diện tích lớn hơn)
5. Lặp lại cho đến khi 2 pointers gặp nhau

### 2.2. Linked List

**Kiến thức:**

- Linked List là cấu trúc dữ liệu gồm các node liên kết với nhau
- Mỗi node chứa data và pointer đến node tiếp theo
- Types: Singly, Doubly, Circular
- Time complexity:
  - Access: O(n) - Phải duyệt từ đầu đến vị trí cần
  - Search: O(n) - Phải duyệt từng node
  - Insert: O(1) - Nếu đã có pointer đến vị trí chèn
  - Delete: O(1) - Nếu đã có pointer đến node cần xóa

**Giải thích chi tiết:**

1. **Cách hoạt động:**
   - Mỗi node chứa data và pointer (next) đến node tiếp theo
   - Head pointer trỏ đến node đầu tiên
   - Node cuối có next = None
   - Không cần bộ nhớ liên tiếp như Array

2. **Khi nào dùng Linked List:**
   - Cần insert/delete thường xuyên ở giữa danh sách
   - Kích thước không biết trước
   - Không cần truy cập ngẫu nhiên qua index
   - Cần implement Stack/Queue

3. **Ưu điểm:**
   - Insert/Delete nhanh O(1) nếu có pointer
   - Kích thước động, không lãng phí bộ nhớ
   - Dễ thêm/xóa phần tử

4. **Nhược điểm:**
   - Truy cập chậm O(n)
   - Tốn thêm bộ nhớ cho pointers
   - Không cache-friendly

**Implement Singly Linked List:**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
  
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
  
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
  
    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1
  
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
  
    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
  
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)
```

**Hướng giải quyết bài toán với Linked List:**

#### Bài toán 1: Reverse Linked List (LeetCode 206)
**Đề bài:** Đảo ngược linked list.

**Phân tích:**
- Dùng 3 pointers: prev, current, next
- Lặp qua list, đảo ngược từng pointer

**Giải pháp:**
```python
def reverse_list(head):
    """
    Time: O(n) - Duyệt list 1 lần
    Space: O(1) - Chỉ dùng biến
    """
    prev = None
    current = head
    
    while current:
        # Lưu next node trước khi đảo pointer
        next_node = current.next
        # Đảo pointer
        current.next = prev
        # Di chuyển pointers
        prev = current
        current = next_node
    
    return prev  # prev là head mới

# Ví dụ: 1 -> 2 -> 3 -> None
# Sau khi reverse: None <- 1 <- 2 <- 3
# Return: 3 -> 2 -> 1 -> None
```

**Giải thích từng bước:**
1. Khởi tạo `prev = None`, `current = head`
2. Lưu `next_node = current.next` trước khi đảo
3. Đảo pointer: `current.next = prev`
4. Di chuyển: `prev = current`, `current = next_node`
5. Lặp cho đến khi `current = None`

#### Bài toán 2: Merge Two Sorted Lists (LeetCode 21)
**Đề bài:** Merge 2 linked list đã sắp xếp thành 1 list đã sắp xếp.

**Phân tích:**
- Dùng dummy node để đơn giản hóa code
- So sánh 2 node hiện tại, chọn node nhỏ hơn
- Di chuyển pointer tương ứng

**Giải pháp:**
```python
def merge_two_lists(list1, list2):
    """
    Time: O(n + m) - Duyệt cả 2 list
    Space: O(1) - Chỉ tạo nodes mới
    """
    # Dummy node để đơn giản hóa
    dummy = Node(0)
    current = dummy
    
    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Nối phần còn lại
    current.next = list1 if list1 else list2
    
    return dummy.next

# Ví dụ:
# list1: 1 -> 2 -> 4
# list2: 1 -> 3 -> 4
# Kết quả: 1 -> 1 -> 2 -> 3 -> 4 -> 4
```

**Giải thích từng bước:**
1. Tạo dummy node để tránh xử lý edge case
2. So sánh 2 node đầu của 2 list
3. Chọn node nhỏ hơn, nối vào result
4. Di chuyển pointer của list vừa chọn
5. Lặp cho đến khi 1 trong 2 list hết
6. Nối phần còn lại của list chưa hết

#### Bài toán 3: Detect Cycle (LeetCode 141)
**Đề bài:** Kiểm tra linked list có cycle không.

**Phân tích:**
- Dùng Floyd's Cycle Detection (Tortoise and Hare)
- 2 pointers: slow (1 bước), fast (2 bước)
- Nếu có cycle, 2 pointers sẽ gặp nhau

**Giải pháp:**
```python
def has_cycle(head):
    """
    Time: O(n) - Tối đa duyệt 1 lần
    Space: O(1) - Chỉ dùng 2 pointers
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next  # 1 bước
        fast = fast.next.next  # 2 bước
    
    return False

# Ví dụ:
# 1 -> 2 -> 3 -> 4 -> 2 (cycle)
# slow và fast sẽ gặp nhau tại node 2
```

**Giải thích từng bước:**
1. Khởi tạo `slow` và `fast` pointers
2. `slow` di chuyển 1 bước, `fast` di chuyển 2 bước
3. Nếu có cycle, `fast` sẽ "đuổi kịp" `slow`
4. Nếu `fast` đến None → không có cycle

### 2.3. Stack

**Kiến thức:**

- Stack là LIFO (Last In First Out) - Phần tử vào sau ra trước
- Operations: push (thêm), pop (lấy ra), peek (xem), isEmpty (kiểm tra rỗng)
- Applications: Expression evaluation, Undo/Redo, Function calls, Backtracking
- Time complexity: O(1) cho tất cả operations

**Giải thích chi tiết:**

1. **Cách hoạt động:**
   - Giống như chồng đĩa: đĩa trên cùng được lấy ra trước
   - Push: Thêm phần tử vào đỉnh stack
   - Pop: Lấy phần tử ở đỉnh stack ra
   - Peek: Xem phần tử ở đỉnh mà không lấy ra

2. **Khi nào dùng Stack:**
   - Kiểm tra dấu ngoặc đúng
   - Tính toán biểu thức (infix, postfix, prefix)
   - Undo/Redo operations
   - Backtracking algorithms
   - Function call stack
   - DFS (Depth-First Search)

3. **Ưu điểm:**
   - Tất cả operations đều O(1)
   - Đơn giản, dễ implement
   - Phù hợp cho backtracking

4. **Nhược điểm:**
   - Chỉ truy cập được phần tử trên cùng
   - Không thể truy cập phần tử ở giữa

**Implement Stack:**

```python
class Stack:
    def __init__(self):
        self.items = []
  
    def push(self, item):
        self.items.append(item)
  
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
  
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
  
    def is_empty(self):
        return len(self.items) == 0
  
    def size(self):
        return len(self.items)
```

**Ứng dụng: Expression Parser**

```python
def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
  
    for char in expression:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
  
    return stack.is_empty()

def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}
  
    for token in expression.split():
        if token not in operators:
            stack.push(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
  
    return stack.pop()
```

**Hướng giải quyết bài toán với Stack:**

#### Bài toán 1: Valid Parentheses (LeetCode 20)
**Đề bài:** Kiểm tra chuỗi dấu ngoặc có hợp lệ không.

**Phân tích:**
- Dùng stack để lưu dấu ngoặc mở
- Khi gặp dấu ngoặc đóng, kiểm tra xem có khớp với dấu mở trên cùng stack không
- Stack phải rỗng sau khi duyệt xong

**Giải pháp:**
```python
def is_valid(s):
    """
    Time: O(n) - Duyệt chuỗi 1 lần
    Space: O(n) - Stack lưu tối đa n/2 phần tử
    """
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs.values():  # Dấu mở
            stack.append(char)
        elif char in pairs:  # Dấu đóng
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0

# Ví dụ
print(is_valid("()[]{}"))  # True
print(is_valid("([)]"))    # False
print(is_valid("(]"))      # False
```

**Giải thích từng bước:**
1. Tạo stack và map các cặp dấu ngoặc
2. Duyệt từng ký tự trong chuỗi
3. Nếu là dấu mở → push vào stack
4. Nếu là dấu đóng → kiểm tra stack có rỗng không và phần tử trên cùng có khớp không
5. Sau khi duyệt xong, stack phải rỗng

#### Bài toán 2: Daily Temperatures (LeetCode 739)
**Đề bài:** Với mỗi ngày, tìm số ngày phải đợi để có nhiệt độ cao hơn.

**Phân tích:**
- Dùng stack lưu index của các ngày chưa tìm được ngày nóng hơn
- Khi gặp nhiệt độ cao hơn, pop các index trong stack và tính số ngày

**Giải pháp:**
```python
def daily_temperatures(temperatures):
    """
    Time: O(n) - Mỗi phần tử vào/ra stack 1 lần
    Space: O(n) - Stack và result array
    """
    stack = []  # Lưu index
    result = [0] * len(temperatures)
    
    for i, temp in enumerate(temperatures):
        # Nếu nhiệt độ hiện tại > nhiệt độ của index trong stack
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    
    return result

# Ví dụ
temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(temps))  # [1, 1, 4, 2, 1, 1, 0, 0]
```

**Giải thích từng bước:**
1. Tạo stack lưu index và result array
2. Duyệt từng nhiệt độ
3. Nếu nhiệt độ hiện tại > nhiệt độ của index trên cùng stack:
   - Pop index đó ra
   - Tính số ngày = index hiện tại - index đã pop
   - Lưu vào result
4. Push index hiện tại vào stack
5. Lặp lại cho đến hết

#### Bài toán 3: Largest Rectangle in Histogram (LeetCode 84)
**Đề bài:** Tìm diện tích hình chữ nhật lớn nhất trong histogram.

**Phân tích:**
- Dùng stack để lưu index của các cột tăng dần
- Khi gặp cột nhỏ hơn, tính diện tích với các cột trước đó

**Giải pháp:**
```python
def largest_rectangle_area(heights):
    """
    Time: O(n) - Mỗi phần tử vào/ra stack 1 lần
    Space: O(n) - Stack
    """
    stack = []
    max_area = 0
    
    for i, height in enumerate(heights):
        # Pop các cột cao hơn cột hiện tại
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)
    
    # Xử lý các cột còn lại trong stack
    while stack:
        h = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * width)
    
    return max_area

# Ví dụ
heights = [2, 1, 5, 6, 2, 3]
print(largest_rectangle_area(heights))  # 10
```

**Giải thích từng bước:**
1. Dùng stack lưu index của cột tăng dần
2. Khi gặp cột nhỏ hơn:
   - Pop cột cao hơn ra
   - Tính diện tích = chiều cao × chiều rộng
   - Chiều rộng = khoảng cách từ vị trí pop đến vị trí hiện tại
3. Sau khi duyệt xong, xử lý các cột còn lại trong stack

### 2.4. Queue

**Kiến thức:**

- Queue là FIFO (First In First Out) - Phần tử vào trước ra trước
- Operations: enqueue (thêm vào cuối), dequeue (lấy từ đầu), front (xem phần tử đầu), isEmpty (kiểm tra rỗng)
- Types: Simple Queue, Circular Queue, Priority Queue
- Applications: Task scheduling, BFS, Print queue, Message queue
- Time complexity: O(1) cho enqueue/dequeue

**Giải thích chi tiết:**

1. **Cách hoạt động:**
   - Giống như hàng đợi: người vào trước được phục vụ trước
   - Enqueue: Thêm phần tử vào cuối queue
   - Dequeue: Lấy phần tử ở đầu queue ra

2. **Khi nào dùng Queue:**
   - BFS (Breadth-First Search)
   - Task scheduling
   - Message queue
   - Level-order traversal của tree
   - Cache replacement (FIFO)

3. **Ưu điểm:**
   - Enqueue/Dequeue đều O(1)
   - Đơn giản, dễ hiểu
   - Phù hợp cho BFS

4. **Nhược điểm:**
   - Chỉ truy cập được phần tử đầu và cuối
   - Không thể truy cập phần tử ở giữa

**Implement Queue:**

```python
class Queue:
    def __init__(self):
        self.items = []
  
    def enqueue(self, item):
        self.items.append(item)
  
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
  
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
  
    def is_empty(self):
        return len(self.items) == 0
  
    def size(self):
        return len(self.items)
```

**Circular Queue:**

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
  
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.size += 1
  
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
  
    def is_empty(self):
        return self.size == 0
  
    def is_full(self):
        return self.size == self.capacity
```

**Hướng giải quyết bài toán với Queue:**

#### Bài toán 1: Binary Tree Level Order Traversal (LeetCode 102)
**Đề bài:** Duyệt cây nhị phân theo từng level.

**Phân tích:**
- Dùng queue để lưu các node ở mỗi level
- BFS: xử lý node hiện tại, thêm children vào queue

**Giải pháp:**
```python
from collections import deque

def level_order(root):
    """
    Time: O(n) - Duyệt tất cả nodes
    Space: O(n) - Queue lưu tối đa n/2 nodes (level cuối)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        # Xử lý tất cả nodes ở level hiện tại
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            # Thêm children vào queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Ví dụ:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Kết quả: [[3], [9, 20], [15, 7]]
```

**Giải thích từng bước:**
1. Khởi tạo queue với root
2. Lặp cho đến khi queue rỗng
3. Xử lý tất cả nodes ở level hiện tại (theo kích thước queue)
4. Với mỗi node, thêm giá trị vào level và thêm children vào queue
5. Thêm level vào result

#### Bài toán 2: Design Circular Queue (LeetCode 622)
**Đề bài:** Implement circular queue với kích thước cố định.

**Phân tích:**
- Dùng array với 2 pointers: front và rear
- Sử dụng modulo để tạo vòng tròn

**Giải pháp:**
```python
class MyCircularQueue:
    def __init__(self, k):
        self.capacity = k
        self.queue = [None] * k
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, value):
        if self.is_full():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True
    
    def front(self):
        return -1 if self.is_empty() else self.queue[self.front]
    
    def rear(self):
        return -1 if self.is_empty() else self.queue[self.rear]
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
```

**Giải thích từng bước:**
1. Khởi tạo array với kích thước cố định
2. Dùng modulo để di chuyển pointers trong vòng tròn
3. Enqueue: di chuyển rear, gán giá trị
4. Dequeue: di chuyển front, xóa giá trị
5. Kiểm tra full/empty dựa trên size

### 2.5. Hash Table

**Kiến thức:**

- Hash Table sử dụng hash function để map keys vào values
- Collision handling: Chaining (danh sách liên kết), Open Addressing (linear probing, quadratic probing)
- Time complexity:
  - Average: O(1) cho insert, delete, search
  - Worst: O(n) khi tất cả keys hash vào cùng bucket
- Load factor: số phần tử / số buckets (thường giữ < 0.75)

**Giải thích chi tiết:**

1. **Cách hoạt động:**
   - Hash function chuyển key thành index trong array
   - Nếu có collision (2 keys cùng index), dùng chaining hoặc probing
   - Chaining: lưu danh sách các cặp (key, value) trong mỗi bucket
   - Open Addressing: tìm bucket trống tiếp theo

2. **Khi nào dùng Hash Table:**
   - Cần tìm kiếm, insert, delete nhanh O(1)
   - Lưu trữ key-value pairs
   - Đếm tần suất xuất hiện
   - Loại bỏ duplicates

3. **Ưu điểm:**
   - Tìm kiếm, insert, delete trung bình O(1)
   - Linh hoạt, không cần sắp xếp

4. **Nhược điểm:**
   - Worst case O(n) khi hash function kém
   - Tốn bộ nhớ hơn array
   - Không giữ thứ tự (trong Python 3.7+ dict giữ thứ tự)

**Implement Hash Table:**

```python
class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0
  
    def _hash(self, key):
        return hash(key) % self.capacity
  
    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
      
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
      
        bucket.append((key, value))
        self.size += 1
  
    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
      
        for k, v in bucket:
            if k == key:
                return v
      
        raise KeyError(f"Key {key} not found")
  
    def delete(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
      
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return
      
        raise KeyError(f"Key {key} not found")
  
    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False
```

**Hướng giải quyết bài toán với Hash Table:**

#### Bài toán 1: Group Anagrams (LeetCode 49)
**Đề bài:** Nhóm các từ là anagram của nhau.

**Phân tích:**
- Dùng hash map với key là sorted string
- Các từ có cùng sorted string là anagram

**Giải pháp:**
```python
def group_anagrams(strs):
    """
    Time: O(n * k log k) - n từ, mỗi từ sort k ký tự
    Space: O(n * k) - Hash map lưu tất cả từ
    """
    groups = {}
    
    for word in strs:
        # Sorted string làm key
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    
    return list(groups.values())

# Ví dụ
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

#### Bài toán 2: Longest Consecutive Sequence (LeetCode 128)
**Đề bài:** Tìm độ dài dãy số liên tiếp dài nhất.

**Phân tích:**
- Dùng set để lưu tất cả số
- Với mỗi số, tìm dãy liên tiếp bắt đầu từ số đó

**Giải pháp:**
```python
def longest_consecutive(nums):
    """
    Time: O(n) - Mỗi số được xử lý tối đa 2 lần
    Space: O(n) - Set lưu tất cả số
    """
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Chỉ bắt đầu từ số đầu tiên của dãy
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Tìm dãy liên tiếp
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

# Ví dụ
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # 4 (dãy 1, 2, 3, 4)
```

### 2.6. Binary Tree

**Kiến thức:**

- Binary Tree: Mỗi node có tối đa 2 children (left và right)
- Types: 
  - Full: Mỗi node có 0 hoặc 2 children
  - Complete: Tất cả levels đầy (trừ level cuối), level cuối lấp từ trái sang phải
  - Perfect: Tất cả levels đầy
  - Balanced: Chiều cao 2 subtree chênh lệch ≤ 1
- Traversal: 
  - Inorder (Left-Root-Right): Duyệt BST cho thứ tự tăng dần
  - Preorder (Root-Left-Right): Copy cây, prefix expression
  - Postorder (Left-Right-Root): Xóa cây, postfix expression
  - Level-order: Duyệt theo từng level (BFS)
- Applications: Expression trees, Decision trees, Heap, BST

**Giải thích chi tiết:**

1. **Cách hoạt động:**
   - Mỗi node có data và 2 pointers (left, right)
   - Root là node gốc
   - Leaf là node không có children
   - Height: số edges từ root đến node xa nhất

2. **Khi nào dùng Binary Tree:**
   - Biểu diễn cấu trúc phân cấp
   - Tìm kiếm (BST)
   - Sắp xếp (Heap)
   - Expression evaluation

3. **Ưu điểm:**
   - Tìm kiếm nhanh O(log n) trong BST cân bằng
   - Linh hoạt, dễ mở rộng

4. **Nhược điểm:**
   - Có thể mất cân bằng → O(n) worst case
   - Phức tạp hơn array/linked list

**Implement Binary Tree:**

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
  
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)
  
    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = TreeNode(data)
  
    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)
  
    def preorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
  
    def postorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
  
    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```

**Hướng giải quyết bài toán với Binary Tree:**

#### Bài toán 1: Maximum Depth of Binary Tree (LeetCode 104)
**Đề bài:** Tìm chiều cao (depth) lớn nhất của cây nhị phân.

**Phân tích:**
- Dùng DFS (recursive hoặc iterative)
- Chiều cao = 1 + max(chiều cao left, chiều cao right)

**Giải pháp:**
```python
def max_depth(root):
    """
    Time: O(n) - Duyệt tất cả nodes
    Space: O(h) - h là chiều cao cây (call stack)
    """
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Iterative với BFS
def max_depth_bfs(root):
    if not root:
        return 0
    
    queue = [(root, 1)]
    max_depth = 0
    
    while queue:
        node, depth = queue.pop(0)
        max_depth = max(max_depth, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth
```

#### Bài toán 2: Same Tree (LeetCode 100)
**Đề bài:** Kiểm tra 2 cây nhị phân có giống nhau không.

**Phân tích:**
- So sánh từng node: giá trị và 2 subtree

**Giải pháp:**
```python
def is_same_tree(p, q):
    """
    Time: O(min(m, n)) - m, n là số nodes
    Space: O(min(m, n)) - Call stack
    """
    # Cả 2 đều None
    if not p and not q:
        return True
    
    # Một trong 2 là None hoặc giá trị khác nhau
    if not p or not q or p.val != q.val:
        return False
    
    # So sánh 2 subtree
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
```

#### Bài toán 3: Invert Binary Tree (LeetCode 226)
**Đề bài:** Đảo ngược cây nhị phân (swap left và right của mỗi node).

**Phân tích:**
- Duyệt cây, swap left và right của mỗi node

**Giải pháp:**
```python
def invert_tree(root):
    """
    Time: O(n) - Duyệt tất cả nodes
    Space: O(h) - Call stack
    """
    if not root:
        return None
    
    # Swap left và right
    root.left, root.right = root.right, root.left
    
    # Đệ quy cho 2 subtree
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root
```

### 2.7. Projects

#### Project: Stack-based Calculator

**Yêu cầu:**

- Chuyển đổi infix sang postfix
- Tính toán biểu thức sử dụng stack
- Hỗ trợ +, -, *, /, (, )

**Ví dụ code:**

```python
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    output = []
  
    for token in expression:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (not stack.is_empty() and 
                   stack.peek() != '(' and 
                   precedence.get(stack.peek(), 0) >= precedence.get(token, 0)):
                output.append(stack.pop())
            stack.push(token)
  
    while not stack.is_empty():
        output.append(stack.pop())
  
    return ' '.join(output)
```

---

## TUẦN 5-6: Thuật toán cơ bản

### 3.1. Search Algorithms

#### Linear Search

**Kiến thức:**

- Duyệt tuần tự từ đầu đến cuối
- Time complexity: O(n) - Trường hợp xấu nhất phải duyệt hết
- Space complexity: O(1) - Chỉ dùng biến

**Giải thích chi tiết:**

1. **Cách hoạt động:**
   - Duyệt từng phần tử trong mảng
   - So sánh với giá trị cần tìm
   - Trả về index nếu tìm thấy, -1 nếu không

2. **Khi nào dùng:**
   - Mảng chưa sắp xếp
   - Mảng nhỏ
   - Chỉ tìm kiếm 1 lần

3. **Ưu điểm:**
   - Đơn giản, dễ implement
   - Không cần sắp xếp trước
   - Hoạt động với mọi cấu trúc dữ liệu

4. **Nhược điểm:**
   - Chậm O(n) với mảng lớn
   - Không tối ưu cho tìm kiếm nhiều lần

**Ví dụ code:**

```python
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
```

#### Binary Search

**Kiến thức:**

- Chỉ áp dụng cho mảng đã sắp xếp
- Chia đôi mảng và so sánh với phần tử giữa
- Time complexity: O(log n) - Mỗi lần giảm một nửa không gian tìm kiếm
- Space complexity: O(1) (iterative), O(log n) (recursive - call stack)

**Giải thích chi tiết:**

1. **Cách hoạt động:**
   - So sánh target với phần tử giữa
   - Nếu bằng → tìm thấy
   - Nếu nhỏ hơn → tìm bên trái
   - Nếu lớn hơn → tìm bên phải
   - Lặp lại cho đến khi tìm thấy hoặc không còn phần tử

2. **Khi nào dùng:**
   - Mảng đã sắp xếp
   - Cần tìm kiếm nhanh O(log n)
   - Tìm kiếm nhiều lần

3. **Ưu điểm:**
   - Rất nhanh O(log n)
   - Hiệu quả với mảng lớn

4. **Nhược điểm:**
   - Phải sắp xếp trước (O(n log n))
   - Chỉ áp dụng cho mảng đã sắp xếp
   - Không hiệu quả với mảng nhỏ

**Ví dụ code:**

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
  
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
  
    return -1

# Recursive
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
  
    if left > right:
        return -1
  
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

**Hướng giải quyết bài toán với Binary Search:**

#### Bài toán 1: Search in Rotated Sorted Array (LeetCode 33)
**Đề bài:** Tìm target trong mảng đã xoay (rotated).

**Phân tích:**
- Mảng xoay có 2 phần đã sắp xếp
- Xác định phần nào đã sắp xếp, sau đó binary search trong phần đó

**Giải pháp:**
```python
def search_rotated(nums, target):
    """
    Time: O(log n) - Binary search
    Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Xác định phần nào đã sắp xếp
        if nums[left] <= nums[mid]:  # Left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Ví dụ
nums = [4, 5, 6, 7, 0, 1, 2]
print(search_rotated(nums, 0))  # 4
```

#### Bài toán 2: Find Peak Element (LeetCode 162)
**Đề bài:** Tìm peak element (lớn hơn neighbors).

**Phân tích:**
- Dùng binary search với điều kiện đặc biệt
- Nếu mid < mid+1 → peak ở bên phải
- Nếu mid > mid+1 → peak ở bên trái

**Giải pháp:**
```python
def find_peak_element(nums):
    """
    Time: O(log n)
    Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

# Ví dụ
nums = [1, 2, 3, 1]
print(find_peak_element(nums))  # 2 (index của 3)
```

### 3.2. Sorting Algorithms

#### Bubble Sort

**Kiến thức:**

- So sánh các phần tử liền kề và đổi chỗ nếu sai thứ tự
- Time complexity: O(n²)
- Space complexity: O(1)
- Stable: Yes

**Ví dụ code:**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

#### Selection Sort

**Kiến thức:**

- Tìm phần tử nhỏ nhất và đặt ở đầu
- Time complexity: O(n²)
- Space complexity: O(1)
- Stable: No

**Ví dụ code:**

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

#### Insertion Sort

**Kiến thức:**

- Giống như sắp xếp bài trong tay
- Time complexity: O(n²) worst, O(n) best
- Space complexity: O(1)
- Stable: Yes

**Ví dụ code:**

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

#### Merge Sort

**Kiến thức:**

- Divide and Conquer: Chia nhỏ bài toán, giải từng phần, kết hợp kết quả
- Chia mảng thành 2 phần, sắp xếp từng phần, rồi merge
- Time complexity: O(n log n) - Luôn luôn, kể cả worst case
- Space complexity: O(n) - Cần mảng phụ để merge
- Stable: Yes - Giữ nguyên thứ tự các phần tử bằng nhau

**Giải thích chi tiết:**

1. **Cách hoạt động:**
   - Divide: Chia mảng thành 2 nửa
   - Conquer: Sắp xếp đệ quy 2 nửa
   - Combine: Merge 2 nửa đã sắp xếp

2. **Khi nào dùng:**
   - Cần stable sort
   - Cần đảm bảo O(n log n) worst case
   - Sắp xếp linked list (không cần random access)

3. **Ưu điểm:**
   - Luôn O(n log n)
   - Stable
   - Dễ parallelize

4. **Nhược điểm:**
   - Tốn bộ nhớ O(n)
   - Không in-place

**Ví dụ code:**

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
  
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
  
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
  
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
  
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

#### Quick Sort

**Kiến thức:**

- Divide and Conquer
- Chọn pivot, chia mảng thành 2 phần (nhỏ hơn và lớn hơn pivot), sắp xếp từng phần
- Time complexity: 
  - Average: O(n log n) - Khi pivot chia đều
  - Worst: O(n²) - Khi pivot luôn là phần tử nhỏ nhất/lớn nhất
- Space complexity: O(log n) - Call stack
- Stable: No - Có thể đổi thứ tự các phần tử bằng nhau

**Giải thích chi tiết:**

1. **Cách hoạt động:**
   - Chọn pivot (thường là phần tử giữa hoặc random)
   - Partition: Chia mảng thành 2 phần (≤ pivot và > pivot)
   - Đệ quy sắp xếp 2 phần

2. **Khi nào dùng:**
   - Cần in-place sort
   - Average case tốt
   - Không cần stable

3. **Ưu điểm:**
   - Average O(n log n) nhanh
   - In-place (tiết kiệm bộ nhớ)
   - Cache-friendly

4. **Nhược điểm:**
   - Worst case O(n²)
   - Không stable
   - Phụ thuộc vào cách chọn pivot

**Ví dụ code:**

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
  
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
  
    return quick_sort(left) + middle + quick_sort(right)

# In-place version
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
  
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
  
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

### 3.3. Recursion

**Kiến thức:**

- Function gọi chính nó
- Base case: Điều kiện dừng
- Recursive case: Gọi lại function với input nhỏ hơn
- Call stack: Lưu trữ các function calls

**Ví dụ code:**

```python
# Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Fibonacci với memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Tower of Hanoi
def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, destination, source)
```

**Best Practices:**

- Luôn có base case - Điều kiện dừng đệ quy
- Đảm bảo recursive case tiến về base case - Tránh vòng lặp vô hạn
- Sử dụng memoization để tránh tính toán lại - Tối ưu performance
- Cẩn thận với stack overflow - Giới hạn độ sâu đệ quy

**Hướng giải quyết bài toán với Recursion:**

#### Bài toán 1: Climbing Stairs (LeetCode 70)
**Đề bài:** Có n bậc thang, mỗi lần bước 1 hoặc 2 bậc. Có bao nhiêu cách lên?

**Phân tích:**
- F(n) = F(n-1) + F(n-2) - Giống Fibonacci
- Base case: F(1) = 1, F(2) = 2

**Giải pháp:**
```python
def climb_stairs(n):
    """
    Time: O(n) với memoization
    Space: O(n) - Memo và call stack
    """
    memo = {}
    
    def dp(i):
        if i <= 2:
            return i
        if i in memo:
            return memo[i]
        memo[i] = dp(i-1) + dp(i-2)
        return memo[i]
    
    return dp(n)

# Iterative (tối ưu hơn)
def climb_stairs_iterative(n):
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1
```

#### Bài toán 2: Generate Parentheses (LeetCode 22)
**Đề bài:** Tạo tất cả chuỗi ngoặc đơn hợp lệ với n cặp.

**Phân tích:**
- Dùng backtracking
- Thêm '(' nếu số '(' < n
- Thêm ')' nếu số ')' < số '('

**Giải pháp:**
```python
def generate_parenthesis(n):
    """
    Time: O(4^n / sqrt(n)) - Số lượng Catalan
    Space: O(n) - Call stack
    """
    result = []
    
    def backtrack(current, open_count, close_count):
        # Base case: đủ n cặp
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Thêm '(' nếu còn chỗ
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        # Thêm ')' nếu số ')' < số '('
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result

# Ví dụ: n = 3
# ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

### 3.4. Big O Notation

**Kiến thức:**

- Mô tả độ phức tạp thời gian và không gian của thuật toán
- Common complexities:
  - O(1): Constant
  - O(log n): Logarithmic
  - O(n): Linear
  - O(n log n): Linearithmic
  - O(n²): Quadratic
  - O(2ⁿ): Exponential

**Ví dụ:**

```python
# O(1)
def get_first(arr):
    return arr[0]

# O(n)
def find_max(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val

# O(n²)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(log n)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 3.5. Project: Sorting Visualizer

**Yêu cầu:**

- Visualize các thuật toán sắp xếp
- So sánh performance
- Hiển thị số lần so sánh và đổi chỗ

**Gợi ý sử dụng:**

- matplotlib hoặc pygame cho visualization
- Tạo animation cho từng bước sắp xếp

---

## TUẦN 7-8: OOP và Design Patterns

### 4.1. Object-Oriented Programming

#### Class và Object

**Kiến thức:**

- Class: Blueprint cho objects
- Object: Instance của class
- Attributes: Biến của class/object
- Methods: Functions của class/object

**Ví dụ code:**

```python
class Person:
    # Class attribute
    species = "Homo sapiens"
  
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
  
    def introduce(self):
        return f"I'm {self.name}, {self.age} years old"
  
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)
  
    @staticmethod
    def is_adult(age):
        return age >= 18

# Usage
person1 = Person("Nguyen Van A", 25)
person2 = Person.from_birth_year("Tran Thi B", 1995)
print(person1.introduce())
print(Person.is_adult(20))
```

#### Inheritance

**Kiến thức:**

- Class con kế thừa từ class cha
- Method overriding: Ghi đè method của class cha
- super(): Gọi method của class cha
- Multiple inheritance: Kế thừa từ nhiều class

**Ví dụ code:**

```python
class Animal:
    def __init__(self, name):
        self.name = name
  
    def speak(self):
        raise NotImplementedError("Subclass must implement")
  
    def move(self):
        return f"{self.name} is moving"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())
```

#### Polymorphism

**Kiến thức:**

- Cùng một interface nhưng hành vi khác nhau
- Method overriding
- Duck typing: "If it walks like a duck and quacks like a duck, it's a duck"

**Ví dụ code:**

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
  
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
  
    def area(self):
        return 3.14159 * self.radius ** 2

# Polymorphism
shapes = [Rectangle(5, 4), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}")
```

#### Encapsulation

**Kiến thức:**

- Ẩn implementation details
- Public, Protected (_), Private (__)
- Getters và Setters
- Properties

**Ví dụ code:**

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number  # Protected
        self.__balance = balance  # Private
  
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
  
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
  
    @property
    def balance(self):
        return self.__balance
  
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            raise ValueError("Balance cannot be negative")
```

### 4.2. Design Patterns

#### Singleton Pattern

**Kiến thức:**

- Đảm bảo chỉ có một instance của class
- Sử dụng khi cần một điểm truy cập global

**Ví dụ code:**

```python
class Singleton:
    _instance = None
  
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

#### Factory Pattern

**Kiến thức:**

- Tạo objects mà không cần chỉ định class cụ thể
- Tách logic tạo object khỏi code sử dụng

**Ví dụ code:**

```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage
dog = AnimalFactory.create_animal("dog", "Buddy")
cat = AnimalFactory.create_animal("cat", "Whiskers")
```

#### Observer Pattern

**Kiến thức:**

- Một object (subject) thông báo cho nhiều objects (observers) khi có thay đổi
- Loose coupling giữa subject và observers

**Ví dụ code:**

```python
class Subject:
    def __init__(self):
        self._observers = []
  
    def attach(self, observer):
        self._observers.append(observer)
  
    def detach(self, observer):
        self._observers.remove(observer)
  
    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

class Observer:
    def update(self, event):
        raise NotImplementedError

class EmailObserver(Observer):
    def update(self, event):
        print(f"Email: {event}")

class SMSObserver(Observer):
    def update(self, event):
        print(f"SMS: {event}")

# Usage
subject = Subject()
subject.attach(EmailObserver())
subject.attach(SMSObserver())
subject.notify("Order placed")
```

### 4.3. SOLID Principles

**Kiến thức:**

- **S**ingle Responsibility: Một class chỉ có một lý do để thay đổi
- **O**pen/Closed: Mở để mở rộng, đóng để sửa đổi
- **L**iskov Substitution: Objects của class con có thể thay thế objects của class cha
- **I**nterface Segregation: Nhiều interfaces nhỏ tốt hơn một interface lớn
- **D**ependency Inversion: Phụ thuộc vào abstractions, không phụ thuộc vào concretions

**Ví dụ:**

```python
# Single Responsibility
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        # Save to database
        pass

# Open/Closed
class PaymentProcessor:
    def process(self, amount):
        raise NotImplementedError

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        # Process credit card
        pass

class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        # Process PayPal
        pass
```

### 4.4. Project: Library Management System

**Yêu cầu:**

- Quản lý sách, thành viên, mượn/trả
- Sử dụng OOP principles
- Implement design patterns phù hợp

**Gợi ý cấu trúc:**

```python
class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_available = True

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
  
    def add_book(self, book):
        self.books[book.isbn] = book
  
    def register_member(self, member):
        self.members[member.member_id] = member
  
    def borrow_book(self, member_id, isbn):
        # Implementation
        pass
  
    def return_book(self, member_id, isbn):
        # Implementation
        pass
```

---

## TUẦN 9-12: Database và Git

### 5.1. SQL Cơ Bản

#### SELECT

**Kiến thức:**

- **Định nghĩa:** Câu lệnh truy vấn dữ liệu từ bảng; có thể lọc (WHERE), sắp xếp (ORDER BY), giới hạn (LIMIT).
- SELECT: Lấy dữ liệu từ bảng
- WHERE: Lọc dữ liệu
- ORDER BY: Sắp xếp
- LIMIT: Giới hạn số dòng

**Ví dụ:**

```sql
-- Basic SELECT
SELECT * FROM users;

-- SELECT với điều kiện
SELECT name, email FROM users WHERE age > 18;

-- Sắp xếp
SELECT * FROM users ORDER BY age DESC;

-- Giới hạn
SELECT * FROM users LIMIT 10;
```

#### INSERT, UPDATE, DELETE

**Kiến thức:**

- **Định nghĩa:** Bộ ba lệnh thao tác dữ liệu: INSERT (thêm), UPDATE (cập nhật), DELETE (xóa) trên bảng.
- INSERT: Thêm dữ liệu mới
- UPDATE: Cập nhật dữ liệu
- DELETE: Xóa dữ liệu

**Ví dụ:**

```sql
-- INSERT
INSERT INTO users (name, email, age) 
VALUES ('Nguyen Van A', 'a@example.com', 25);

-- UPDATE
UPDATE users 
SET age = 26 
WHERE email = 'a@example.com';

-- DELETE
DELETE FROM users 
WHERE age < 18;
```

#### JOIN

**Kiến thức:**

- **Định nghĩa:** Kết hợp nhiều bảng theo khóa liên quan để lấy dữ liệu liên quan; INNER/LEFT/RIGHT/FULL xác định cách giữ/từ bỏ các hàng không khớp.
- INNER JOIN: Chỉ lấy dòng có match ở cả 2 bảng
- LEFT JOIN: Lấy tất cả dòng từ bảng trái
- RIGHT JOIN: Lấy tất cả dòng từ bảng phải
- FULL OUTER JOIN: Lấy tất cả dòng từ cả 2 bảng

**Ví dụ:**

```sql
-- INNER JOIN
SELECT u.name, o.order_id, o.total
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id;

-- LEFT JOIN
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id;
```

#### Aggregate Functions

**Kiến thức:**

- **Định nghĩa:** Hàm tổng hợp (COUNT/SUM/AVG/MAX/MIN) tính toán trên nhiều dòng, thường kết hợp GROUP BY/HAVING để nhóm và lọc nhóm.
- COUNT: Đếm số dòng
- SUM: Tổng
- AVG: Trung bình
- MAX, MIN: Giá trị lớn nhất/nhỏ nhất
- GROUP BY: Nhóm dữ liệu
- HAVING: Lọc sau GROUP BY

**Ví dụ:**

```sql
-- Aggregate
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users;
SELECT MAX(age) FROM users;

-- GROUP BY
SELECT department, COUNT(*) as employee_count
FROM employees
GROUP BY department;

-- HAVING
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

#### Index

**Kiến thức:**

- **Định nghĩa:** Cấu trúc dữ liệu (thường B-Tree) giúp tăng tốc tìm kiếm/ORDER BY bằng cách tránh quét toàn bảng; trade-off: tăng chi phí ghi và tốn space.
- Index tăng tốc độ truy vấn
- Tạo index trên các cột thường được tìm kiếm
- Trade-off: Tăng tốc đọc, giảm tốc ghi

**Ví dụ:**

```sql
-- Tạo index
CREATE INDEX idx_email ON users(email);

-- Composite index
CREATE INDEX idx_name_age ON users(name, age);

-- Unique index
CREATE UNIQUE INDEX idx_email_unique ON users(email);
```

### 5.2. PostgreSQL/MySQL

**Kiến thức:**

- **Định nghĩa:** Hệ quản trị CSDL quan hệ; PostgreSQL mạnh về tính năng, MySQL phổ biến, hiệu năng tốt; dùng để lưu trữ dữ liệu có cấu trúc, hỗ trợ ACID.
- Setup database
- Tạo bảng với constraints
- Data types
- Transactions
- Stored procedures (cơ bản)

**Ví dụ:**

```sql
-- Tạo database
CREATE DATABASE myapp;

-- Tạo bảng
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    age INTEGER CHECK (age > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Transaction
BEGIN;
INSERT INTO users (name, email) VALUES ('A', 'a@example.com');
UPDATE users SET age = 25 WHERE email = 'a@example.com';
COMMIT;
```

---

## DATABASE OPTIMIZATION - TƯ DUY SENIOR

> Phần này bao gồm tư duy và kỹ thuật tối ưu database như một Senior Developer, dựa trên kinh nghiệm thực tế từ production systems.

### 1. DATABASE DESIGN PATTERNS

#### 1.1. Normalization vs Denormalization

**Khi nào Normalize (3NF):**

- Dữ liệu ít thay đổi
- Cần data integrity cao
- Write operations nhiều hơn read
- Storage quan trọng

**Khi nào Denormalize:**

- Read operations nhiều hơn write
- Cần performance cao cho queries
- Có thể chấp nhận data inconsistency tạm thời
- Cần giảm số lượng JOINs

**Ví dụ thực tế:**

```sql
-- ✅ Normalized (3NF) - Tốt cho write-heavy
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);

CREATE TABLE user_profiles (
    user_id INTEGER REFERENCES users(id),
    bio TEXT,
    avatar_url VARCHAR(255),
    location VARCHAR(100)
);

-- ✅ Denormalized - Tốt cho read-heavy
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255),
    bio TEXT,              -- Denormalized từ user_profiles
    avatar_url VARCHAR(255), -- Denormalized
    location VARCHAR(100)    -- Denormalized
);

-- Trade-off: Khi update profile, cần update cả users table
-- Nhưng khi query user info, không cần JOIN
```

**📚 GIẢI THÍCH CHI TIẾT - NORMALIZATION vs DENORMALIZATION:**

**Normalization là gì?**
Normalization là quá trình tổ chức database để giảm redundancy (trùng lặp) và dependency (phụ thuộc). Mục tiêu: Mỗi fact chỉ lưu ở một nơi.

**Normal Forms:**

- **1NF**: Mỗi cell chỉ chứa 1 value, không có duplicate rows
- **2NF**: 1NF + không có partial dependencies
- **3NF**: 2NF + không có transitive dependencies
- **BCNF**: 3NF + mọi determinant là candidate key

**Ví dụ Normalization:**

```sql
-- ❌ Unnormalized (1NF violation)
CREATE TABLE orders (
    id INT,
    user_name VARCHAR(100),  -- Duplicate data
    user_email VARCHAR(255),  -- Duplicate data
    product_name VARCHAR(100), -- Duplicate data
    quantity INT,
    price DECIMAL
);

-- ✅ Normalized (3NF)
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL
);

CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT REFERENCES users(id),
    product_id INT REFERENCES products(id),
    quantity INT
);
```

**Trade-offs chi tiết:**

**Normalized (3NF):**

```
Ưu điểm:
✅ Data integrity cao (không duplicate)
✅ Tiết kiệm storage (1 fact = 1 nơi)
✅ Dễ update (chỉ update 1 chỗ)
✅ Phù hợp write-heavy

Nhược điểm:
❌ Cần nhiều JOINs (chậm)
❌ Queries phức tạp
❌ Không phù hợp read-heavy

Performance:
- Write: Fast (chỉ update 1 table)
- Read: Slow (cần JOINs)
```

**Denormalized:**

```
Ưu điểm:
✅ Queries nhanh (ít JOINs)
✅ Queries đơn giản
✅ Phù hợp read-heavy

Nhược điểm:
❌ Data duplication (tốn storage)
❌ Khó maintain consistency
❌ Update phức tạp (phải update nhiều chỗ)
❌ Risk data inconsistency

Performance:
- Write: Slow (phải update nhiều nơi)
- Read: Fast (không cần JOINs)
```

**Khi nào dùng gì - Decision Matrix:**

```
Read/Write Ratio:
- Read >> Write (90/10): → Denormalize
- Read ≈ Write (50/50): → Normalize
- Read << Write (10/90): → Normalize

Data Change Frequency:
- Thay đổi thường xuyên: → Normalize
- Ít thay đổi: → Có thể denormalize

Data Size:
- Small: → Normalize (JOINs không chậm)
- Large: → Cân nhắc denormalize

Consistency Requirements:
- High: → Normalize
- Medium/Low: → Có thể denormalize
```

**Hybrid Approach (Best Practice):**

```sql
-- Normalize cho write (source of truth)
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);

CREATE TABLE user_profiles (
    user_id INT REFERENCES users(id),
    bio TEXT,
    avatar_url VARCHAR(255)
);

-- Denormalize cho read (materialized view)
CREATE MATERIALIZED VIEW users_denormalized AS
SELECT 
    u.id,
    u.name,
    u.email,
    p.bio,
    p.avatar_url
FROM users u
LEFT JOIN user_profiles p ON u.id = p.user_id;

-- Refresh định kỳ
REFRESH MATERIALIZED VIEW CONCURRENTLY users_denormalized;
```

**Lưu ý quan trọng:**

- **Start với Normalized**: Dễ refactor sau
- **Denormalize khi cần**: Khi có performance issues
- **Document decisions**: Ghi lại lý do denormalize
- **Monitor**: Theo dõi consistency và performance

#### 1.2. Partitioning Strategy

**Range Partitioning:**

```sql
-- Partition orders theo tháng
CREATE TABLE orders (
    id SERIAL,
    user_id INTEGER,
    total DECIMAL(10,2),
    created_at TIMESTAMP
) PARTITION BY RANGE (created_at);

CREATE TABLE orders_2024_01 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE orders_2024_02 PARTITION OF orders
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');

-- Benefits:
-- 1. Queries chỉ scan partition cần thiết
-- 2. Dễ dàng archive/drop old partitions
-- 3. Indexes nhỏ hơn cho mỗi partition
```

**Hash Partitioning:**

```sql
-- Partition users theo user_id (distribute load)
CREATE TABLE users (
    id SERIAL,
    name VARCHAR(100),
    email VARCHAR(255)
) PARTITION BY HASH (id);

CREATE TABLE users_0 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 0);

CREATE TABLE users_1 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 1);

CREATE TABLE users_2 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 2);

CREATE TABLE users_3 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

#### 1.3. Materialized Views

**Khi nào dùng:**

- Aggregations phức tạp được query thường xuyên
- Data không cần real-time
- Có thể refresh định kỳ

```sql
-- Tạo materialized view cho dashboard
CREATE MATERIALIZED VIEW user_stats AS
SELECT 
    DATE_TRUNC('day', created_at) as date,
    COUNT(*) as new_users,
    COUNT(DISTINCT country) as countries
FROM users
GROUP BY DATE_TRUNC('day', created_at);

-- Tạo index trên materialized view
CREATE INDEX idx_user_stats_date ON user_stats(date);

-- Refresh định kỳ (cron job)
REFRESH MATERIALIZED VIEW CONCURRENTLY user_stats;

-- Query từ materialized view (nhanh hơn nhiều)
SELECT * FROM user_stats WHERE date >= '2024-01-01';
```

### 2. INDEXING STRATEGY - NÂNG CAO

**Định nghĩa:** Index là cấu trúc dữ liệu (thường B-Tree/GiST/GIN) giúp tăng tốc truy vấn bằng cách tránh quét toàn bộ bảng; đánh đổi ở chi phí ghi và dung lượng.

#### 2.1. Index Types và Khi Nào Dùng

**B-Tree Index (Default):**
**Định nghĩa:** Cấu trúc cây cân bằng, tối ưu cho so sánh phạm vi (=, <, >, BETWEEN, LIKE prefix).

```sql
-- Tốt cho: =, <, >, <=, >=, BETWEEN, LIKE 'prefix%'
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_created_at ON orders(created_at);

-- Composite index - order matters!
CREATE INDEX idx_user_status_created ON users(status, created_at DESC);
-- ✅ Good: WHERE status = 'active' ORDER BY created_at DESC
-- ✅ Good: WHERE status = 'active' AND created_at > '2024-01-01'
-- ❌ Bad: WHERE created_at > '2024-01-01' (không dùng được index)
```

**Partial Index:**
**Định nghĩa:** Index chỉ trên một phần dữ liệu thỏa điều kiện WHERE, giảm size và tăng hiệu quả cho các truy vấn thường xuyên dùng filter đó.

```sql
-- Chỉ index một phần data (tiết kiệm space)
CREATE INDEX idx_active_users ON users(email) 
WHERE status = 'active';

-- Chỉ index recent data
CREATE INDEX idx_recent_orders ON orders(user_id, created_at)
WHERE created_at > '2024-01-01';
```

**Covering Index (Include columns):**
**Định nghĩa:** Index chứa thêm các cột được SELECT, cho phép Index Only Scan (không cần đọc table).

```sql
-- PostgreSQL: Include columns không cần sort nhưng cần select
CREATE INDEX idx_user_email_covering ON users(email) 
INCLUDE (name, avatar_url);

-- Query chỉ cần đọc index, không cần đọc table
SELECT name, avatar_url FROM users WHERE email = 'user@example.com';
```

**GIN Index (Full-text search):**
**Định nghĩa:** Generalized Inverted Index, tối ưu tìm kiếm full-text trên dữ liệu văn bản lớn.

```sql
-- PostgreSQL: Full-text search
CREATE INDEX idx_content_gin ON posts USING GIN(to_tsvector('english', content));

SELECT * FROM posts 
WHERE to_tsvector('english', content) @@ to_tsquery('english', 'search term');
```

**GiST Index (Geospatial):**
**Định nghĩa:** Generalized Search Tree, hỗ trợ dữ liệu không gian/địa lý, khoảng cách, hình học.

```sql
-- PostgreSQL: Geospatial queries
CREATE INDEX idx_location_gist ON users USING GIST(location);

SELECT * FROM users 
WHERE ST_DWithin(location, ST_MakePoint(-74.0, 40.7)::geography, 1000);
```

#### 2.2. Index Maintenance

```sql
-- Analyze để update statistics
ANALYZE users;

-- Rebuild index (PostgreSQL)
REINDEX INDEX idx_email;

-- Xem index usage
SELECT 
    schemaname,
    tablename,
    indexname,
    idx_scan as index_scans,
    idx_tup_read as tuples_read,
    idx_tup_fetch as tuples_fetched
FROM pg_stat_user_indexes
ORDER BY idx_scan;

-- Tìm unused indexes
SELECT 
    schemaname,
    tablename,
    indexname
FROM pg_stat_user_indexes
WHERE idx_scan = 0
AND indexname NOT LIKE 'pg_toast%';
```

**📚 GIẢI THÍCH CHI TIẾT - INDEXES:**

**Index hoạt động như thế nào?**

**B-Tree Index Structure:**

```
        [50]
       /    \
   [25]      [75]
   /  \      /  \
[10][30]  [60][90]
```

**Quá trình tìm kiếm:**

1. Bắt đầu từ root node
2. So sánh giá trị với root
3. Nếu nhỏ hơn → đi left, lớn hơn → đi right
4. Lặp lại cho đến khi tìm thấy hoặc đến leaf node
5. Time complexity: O(log n) thay vì O(n)

**Ví dụ: Tìm email = 'user@example.com'**

```
Without Index:
- Scan 1,000,000 rows
- Time: ~1000ms

With Index:
- Traverse B-Tree: ~20 nodes (log2(1M) ≈ 20)
- Time: ~1ms
- Speedup: 1000x!
```

**Tại sao Composite Index order quan trọng?**

```sql
CREATE INDEX idx_status_created ON users(status, created_at DESC);
```

**Index được sắp xếp như:**

```
(status='active', created_at='2024-01-01')
(status='active', created_at='2024-01-02')
(status='active', created_at='2024-01-03')
(status='inactive', created_at='2024-01-01')
```

**Query có thể dùng index:**

- ✅ `WHERE status = 'active'` - Có thể dùng (prefix match)
- ✅ `WHERE status = 'active' ORDER BY created_at DESC` - Perfect match
- ❌ `WHERE created_at > '2024-01-01'` - Không dùng được (không có status)

**Lý do:** Index được sort theo (status, created_at). Không có status, database không thể binary search hiệu quả.

**Index Selectivity:**

- **High Selectivity**: Ít duplicate values → Index hiệu quả
  - Ví dụ: email (unique), user_id (primary key)
- **Low Selectivity**: Nhiều duplicate values → Index ít hiệu quả
  - Ví dụ: gender (chỉ có M/F), status (active/inactive)

**Rule of thumb:** Chỉ index columns có selectivity > 10% (ít nhất 10 giá trị khác nhau trên 100 rows)

**Index Maintenance Overhead:**

```
Mỗi INSERT/UPDATE/DELETE:
1. Update table data
2. Update tất cả indexes trên table
3. Rebalance B-Tree nếu cần

Ví dụ: Table có 5 indexes
- 1 INSERT = 1 table write + 5 index writes = 6 operations
- Nếu có 10 indexes = 11 operations!
```

**Khi nào không nên tạo index:**

- ❌ Table nhỏ (< 1000 rows) - Sequential scan nhanh hơn
- ❌ Column ít được query
- ❌ Column thay đổi thường xuyên (write-heavy)
- ❌ Column có low selectivity (nhiều duplicate)

### 3. QUERY OPTIMIZATION - SENIOR LEVEL

**Định nghĩa:** Tập kỹ thuật giảm thời gian/chi phí truy vấn bằng cách dùng index đúng, viết query tối ưu, và đọc execution plan.

#### 3.1. EXPLAIN và Query Analysis

**Định nghĩa:** EXPLAIN cho biết kế hoạch thực thi; EXPLAIN ANALYZE thực thi thật và đo thời gian/rows; dùng để phát hiện Seq Scan, join đắt, thiếu index.

```sql
-- EXPLAIN để xem execution plan
EXPLAIN SELECT * FROM users WHERE email = 'user@example.com';

-- EXPLAIN ANALYZE để xem thời gian thực tế
EXPLAIN ANALYZE 
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.name;

-- Xem execution plan với format
EXPLAIN (FORMAT JSON, BUFFERS, VERBOSE) 
SELECT * FROM users WHERE email = 'user@example.com';
```

**Đọc Execution Plan:**

```
Seq Scan (Sequential Scan) - ❌ Chậm, scan toàn bộ table
Index Scan - ✅ Tốt, dùng index
Index Only Scan - ✅✅ Tốt nhất, chỉ đọc index
Bitmap Heap Scan - ✅ Tốt cho multiple conditions
Nested Loop - ✅ Tốt cho small datasets
Hash Join - ✅ Tốt cho large datasets
Merge Join - ✅ Tốt cho sorted data
```

**📚 GIẢI THÍCH CHI TIẾT - EXPLAIN PLAN:**

**Đọc Execution Plan như Senior:**

**Ví dụ EXPLAIN ANALYZE:**

```sql
EXPLAIN ANALYZE
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.name;
```

**Kết quả:**

```
HashAggregate  (cost=1500.00..1600.00 rows=1000 width=64) (actual time=50.123..60.456 rows=500 loops=1)
  Group Key: u.id, u.name
  ->  Hash Left Join  (cost=800.00..1400.00 rows=10000 width=64) (actual time=10.123..40.456 rows=5000 loops=1)
        Hash Cond: (o.user_id = u.id)
        ->  Seq Scan on orders o  (cost=0.00..500.00 rows=10000 width=8) (actual time=0.123..5.456 rows=10000 loops=1)
        ->  Hash  (cost=600.00..600.00 rows=1000 width=64) (actual time=8.123..8.123 rows=1000 loops=1)
              ->  Index Scan using idx_users_created on users u  (cost=0.00..600.00 rows=1000 width=64) (actual time=0.123..5.456 rows=1000 loops=1)
                    Index Cond: (created_at > '2024-01-01'::timestamp)
Planning Time: 1.234 ms
Execution Time: 60.789 ms
```

**Giải thích từng phần:**

**1. HashAggregate:**

- **cost**: Ước tính cost (không phải thời gian)
- **actual time**: Thời gian thực tế (ms)
- **rows**: Số rows được process
- **loops**: Số lần operation được thực hiện

**2. Hash Left Join:**

- **Hash Cond**: Điều kiện JOIN
- Tạo hash table từ một bên, probe từ bên kia
- Tốt cho large datasets

**3. Seq Scan:**

- ❌ **Sequential Scan**: Scan toàn bộ table
- Chậm với large tables
- Cần optimize: Thêm index hoặc filter sớm hơn

**4. Index Scan:**

- ✅ Dùng index để tìm rows
- Nhanh hơn Seq Scan nhiều lần
- **Index Cond**: Điều kiện dùng index

**Các loại Scan và khi nào dùng:**

**Seq Scan:**

- Khi: Table nhỏ, không có index phù hợp, scan toàn bộ nhanh hơn
- Cost: O(n) - scan tất cả rows
- Optimize: Thêm index hoặc filter

**Index Scan:**

- Khi: Có index phù hợp, cần đọc table data
- Cost: O(log n) + số rows match
- Tốt cho: Point queries, range queries

**Index Only Scan:**

- Khi: Tất cả columns cần thiết đều trong index
- Cost: O(log n) - chỉ đọc index
- Tốt nhất: Không cần đọc table

**Bitmap Heap Scan:**

- Khi: Multiple conditions, nhiều rows match
- Cost: Tạo bitmap từ index, scan table theo bitmap
- Tốt cho: OR conditions, multiple indexes

**Các loại Join:**

**Nested Loop:**

```
For each row in outer table:
    For each row in inner table:
        If match: output
```

- Tốt cho: Small datasets
- Cost: O(n × m)
- Khi: Một bên rất nhỏ

**Hash Join:**

```
1. Build hash table từ một bên
2. Probe hash table với bên kia
```

- Tốt cho: Large datasets
- Cost: O(n + m)
- Khi: Cả hai bên đều lớn

**Merge Join:**

```
1. Sort cả hai bên
2. Merge như merge sort
```

- Tốt cho: Sorted data
- Cost: O(n log n + m log m)
- Khi: Data đã sorted hoặc có index sorted

**Red Flags trong Execution Plan:**

- ❌ **Seq Scan trên large table**: Cần index
- ❌ **Nested Loop với large datasets**: Cần Hash Join
- ❌ **High cost nhưng low rows**: Query không efficient
- ❌ **Multiple sequential scans**: Cần optimize

#### 3.2. Common Query Anti-patterns

**Định nghĩa:** Những mẫu truy vấn gây chậm/khó scale (SELECT *, N+1, hàm trên cột, OR không hiệu quả, subquery tệ), cần tránh hoặc viết lại tối ưu hơn.

**Anti-pattern 1: SELECT ***

```sql
-- ❌ Bad: Lấy tất cả columns
SELECT * FROM users WHERE id = 1;

-- ✅ Good: Chỉ lấy columns cần thiết
SELECT id, name, email FROM users WHERE id = 1;

-- Benefits:
-- 1. Giảm network traffic
-- 2. Có thể dùng covering index
-- 3. Dễ maintain khi schema thay đổi
```

**Anti-pattern 2: N+1 Query Problem**

```sql
-- ❌ Bad: N+1 queries
-- Application code:
for user in users:
    orders = SELECT * FROM orders WHERE user_id = user.id  -- N queries!

-- ✅ Good: Single query với JOIN
SELECT u.*, o.id as order_id, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01';

-- ✅ Good: Batch query
SELECT * FROM orders WHERE user_id IN (1, 2, 3, ...);
```

**📚 GIẢI THÍCH CHI TIẾT - N+1 QUERY PROBLEM:**

**Vấn đề:**

- Query 1: Lấy danh sách users (1 query)
- Query 2-N: Với mỗi user, query orders (N queries)
- **Tổng: 1 + N queries**

**Ví dụ thực tế:**

```javascript
// ❌ Bad: N+1 queries
const users = await db.query('SELECT * FROM users LIMIT 100');
// 1 query

for (const user of users) {
    const orders = await db.query(
        'SELECT * FROM orders WHERE user_id = $1',
        [user.id]
    );
    // 100 queries!
}
// Tổng: 101 queries
// Time: 1ms * 101 = 101ms (nếu mỗi query 1ms)
```

**Tại sao chậm?**

- **Network overhead**: Mỗi query = 1 round trip đến database
- **Connection overhead**: Mỗi query cần connection từ pool
- **Query parsing**: Database phải parse 100 queries riêng biệt

**Giải pháp:**

```javascript
// ✅ Good: 1 query với JOIN
const result = await db.query(`
    SELECT u.*, o.id as order_id, o.total
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    WHERE u.created_at > '2024-01-01'
`);
// 1 query
// Time: ~5ms (JOIN phức tạp hơn nhưng vẫn nhanh hơn 101 queries!)

// Process trong application
const userMap = new Map();
result.rows.forEach(row => {
    if (!userMap.has(row.id)) {
        userMap.set(row.id, {
            ...row,
            orders: []
        });
    }
    if (row.order_id) {
        userMap.get(row.id).orders.push({
            id: row.order_id,
            total: row.total
        });
    }
});
```

**Khi nào dùng JOIN vs Batch Query?**

**Dùng JOIN khi:**

- ✅ Cần tất cả data trong 1 query
- ✅ Relationship 1-to-many không quá lớn
- ✅ Cần filter/sort trên joined data

**Dùng Batch Query khi:**

- ✅ Relationship có thể rất lớn (nhiều orders per user)
- ✅ Chỉ cần subset của related data
- ✅ Cần pagination cho related data

```javascript
// ✅ Batch query với pagination
const userIds = users.map(u => u.id);
const orders = await db.query(
    'SELECT * FROM orders WHERE user_id = ANY($1) ORDER BY created_at DESC LIMIT 20',
    [userIds]
);
// 1 query, chỉ lấy 20 orders mới nhất
```

**Performance Comparison:**

```
N+1 Queries:
- 100 users × 1ms/query = 100ms
- Plus network overhead = ~150ms

JOIN:
- 1 query với JOIN = 5ms
- Plus processing = ~10ms

Speedup: 15x!
```

**Anti-pattern 3: Functions trong WHERE**

```sql
-- ❌ Bad: Function trên column (không dùng được index)
SELECT * FROM users WHERE UPPER(email) = 'USER@EXAMPLE.COM';
SELECT * FROM users WHERE DATE(created_at) = '2024-01-01';

-- ✅ Good: Function trên value
SELECT * FROM users WHERE email = UPPER('user@example.com');
SELECT * FROM users WHERE created_at >= '2024-01-01' 
    AND created_at < '2024-01-02';

-- ✅ Good: Functional index
CREATE INDEX idx_upper_email ON users(UPPER(email));
SELECT * FROM users WHERE UPPER(email) = 'USER@EXAMPLE.COM';
```

**Anti-pattern 4: OR trong WHERE**

```sql
-- ❌ Bad: OR thường không dùng được index tốt
SELECT * FROM users WHERE email = 'a@example.com' OR phone = '123456';

-- ✅ Good: UNION
SELECT * FROM users WHERE email = 'a@example.com'
UNION
SELECT * FROM users WHERE phone = '123456';

-- ✅ Good: Multiple queries và merge trong application
```

**Anti-pattern 5: Subquery không tối ưu**

```sql
-- ❌ Bad: Correlated subquery (chậm)
SELECT u.*, 
    (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) as order_count
FROM users u;

-- ✅ Good: JOIN với aggregation
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;
```

#### 3.3. Query Optimization Techniques

**1. Use LIMIT early:**

```sql
-- ❌ Bad: Sort toàn bộ rồi mới limit
SELECT * FROM orders ORDER BY created_at DESC LIMIT 10;

-- ✅ Good: Nếu có index trên created_at DESC
CREATE INDEX idx_orders_created_desc ON orders(created_at DESC);
SELECT * FROM orders ORDER BY created_at DESC LIMIT 10;
```

**2. Pagination với Cursor:**

```sql
-- ❌ Bad: OFFSET chậm với large datasets
SELECT * FROM orders ORDER BY id LIMIT 10 OFFSET 10000;
-- Database phải skip 10000 rows

-- ✅ Good: Cursor-based pagination
SELECT * FROM orders 
WHERE id > 10000 
ORDER BY id 
LIMIT 10;
```

**📚 GIẢI THÍCH CHI TIẾT - PAGINATION:**

**Tại sao OFFSET chậm?**

**Cơ chế OFFSET:**

```
Database phải:
1. Sort toàn bộ result set
2. Skip N rows (OFFSET)
3. Return M rows (LIMIT)

Ví dụ: OFFSET 10000 LIMIT 10
- Sort 1M rows
- Skip 10000 rows (vẫn phải process)
- Return 10 rows

Time: O(n log n) + O(offset)
```

**Vấn đề:**

- OFFSET càng lớn → càng chậm
- Không stable: Nếu có data mới, có thể skip hoặc duplicate
- Không scalable với large datasets

**Cursor-based Pagination:**

**Cơ chế:**

```
1. Query với WHERE id > cursor
2. Return LIMIT rows
3. Use last row's id as next cursor

Time: O(log n) + O(limit)
- Index scan đến cursor
- Return limit rows
```

**Ưu điểm:**

- ✅ Performance consistent (không phụ thuộc offset)
- ✅ Stable (không bị ảnh hưởng bởi data mới)
- ✅ Scalable với large datasets

**Nhược điểm:**

- ❌ Không thể jump đến page cụ thể
- ❌ Cần unique, sequential cursor
- ❌ Phức tạp hơn implement

**Implementation:**

```javascript
// Cursor-based pagination
async function getOrders(cursor = null, limit = 20) {
    const query = cursor
        ? 'SELECT * FROM orders WHERE id > $1 ORDER BY id LIMIT $2'
        : 'SELECT * FROM orders ORDER BY id LIMIT $1';
  
    const params = cursor ? [cursor, limit] : [limit];
    const orders = await db.query(query, params);
  
    const nextCursor = orders.length === limit 
        ? orders[orders.length - 1].id 
        : null;
  
    return {
        orders,
        nextCursor,
        hasMore: nextCursor !== null
    };
}

// Usage
const page1 = await getOrders(); // cursor = null
const page2 = await getOrders(page1.nextCursor);
```

**Khi nào dùng gì:**

- **OFFSET**: Cần jump đến page cụ thể, dataset nhỏ
- **Cursor**: Large datasets, infinite scroll, performance critical

**3. Batch Operations:**

```sql
-- ❌ Bad: Multiple individual inserts
INSERT INTO orders (user_id, total) VALUES (1, 100);
INSERT INTO orders (user_id, total) VALUES (2, 200);
-- ... 1000 times

-- ✅ Good: Batch insert
INSERT INTO orders (user_id, total) VALUES
    (1, 100),
    (2, 200),
    -- ... 1000 rows
    (1000, 500);

-- ✅ Good: Bulk insert với COPY (PostgreSQL)
COPY orders(user_id, total) FROM '/path/to/file.csv' CSV;
```

### 4. CONNECTION POOLING - PRODUCTION READY

#### 4.1. Connection Pool Configuration

```javascript
// Node.js với pg-pool
const { Pool } = require('pg');

const pool = new Pool({
    host: process.env.DB_HOST,
    database: process.env.DB_NAME,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
  
    // Connection pool settings
    max: 20,                    // Maximum pool size
    min: 5,                     // Minimum pool size
    idleTimeoutMillis: 30000,   // Close idle connections after 30s
    connectionTimeoutMillis: 2000, // Timeout khi tạo connection mới
  
    // Statement timeout
    statement_timeout: 5000,    // Query timeout 5s
  
    // Application name (for monitoring)
    application_name: 'myapp-api'
});

// Health check
setInterval(async () => {
    try {
        await pool.query('SELECT 1');
        console.log('Database connection healthy');
    } catch (error) {
        console.error('Database connection failed:', error);
        // Alert team
    }
}, 60000);
```

#### 4.2. Connection Pool Monitoring

```javascript
// Monitor pool stats
setInterval(() => {
    const stats = {
        total: pool.totalCount,
        idle: pool.idleCount,
        waiting: pool.waitingCount
    };
  
    console.log('Pool stats:', stats);
  
    // Alert nếu có vấn đề
    if (stats.waiting > 10) {
        logger.warn('High number of waiting connections', stats);
        // Send alert
    }
  
    if (stats.idle === 0 && stats.total === pool.options.max) {
        logger.error('Connection pool exhausted!', stats);
        // Send critical alert
    }
}, 5000);
```

**📚 GIẢI THÍCH CHI TIẾT - CONNECTION POOLING:**

**Tại sao cần Connection Pool?**

**Vấn đề không có Pool:**

```
Mỗi request tạo connection mới:
1. TCP handshake: ~10ms
2. SSL/TLS handshake: ~30ms
3. Authentication: ~10ms
4. Query: ~5ms
5. Close connection: ~5ms
Total: ~60ms overhead mỗi request

Với 1000 requests/second:
- 1000 connections/second
- 60ms × 1000 = 60 seconds overhead/second
- Không thể scale!
```

**Giải pháp: Connection Pool**

```
Pool giữ sẵn connections:
1. Reuse connections: 0ms overhead
2. Query: ~5ms
Total: ~5ms mỗi request

Với 1000 requests/second:
- Chỉ cần 20 connections
- 5ms × 1000 = 5 seconds/second
- Có thể scale!
```

**Pool Size Calculation:**

**Công thức cơ bản:**

```
Pool Size = (Number of CPU cores × 2) + Effective spindle count

Ví dụ:
- Server: 4 cores
- Database: 1 instance
- Pool size = (4 × 2) + 1 = 9 connections
```

**Thực tế:**

- **Web applications**: 10-20 connections
- **Heavy applications**: 20-50 connections
- **Quá nhiều**: Context switching overhead, database overload

**Pool States:**

```
Pool có 3 states:
1. Idle: Connection sẵn sàng, không được dùng
2. Active: Connection đang được dùng
3. Waiting: Request đang chờ connection available

Ideal state:
- Có một số idle connections (ready)
- Không có waiting requests
- Active connections < max
```

**Pool Exhaustion - Dấu hiệu:**

- `waiting > 0`: Requests đang chờ
- `idle = 0` và `total = max`: Pool đầy
- Response time tăng đột ngột
- Database connections tăng

**Giải pháp khi Pool Exhausted:**

1. Tăng pool size (nhưng không quá nhiều)
2. Optimize queries (giảm thời gian query)
3. Add read replicas (distribute load)
4. Implement connection queuing với timeout

### 5. CACHING STRATEGY

#### 5.1. Multi-level Caching

```javascript
// Level 1: Application memory cache
const NodeCache = require('node-cache');
const memoryCache = new NodeCache({ stdTTL: 300 }); // 5 minutes

// Level 2: Redis cache
const redis = require('redis');
const redisClient = redis.createClient();

// Level 3: Database

async function getUser(userId) {
    // Level 1: Memory cache
    const cached = memoryCache.get(`user:${userId}`);
    if (cached) {
        return cached;
    }
  
    // Level 2: Redis cache
    const redisCached = await redisClient.get(`user:${userId}`);
    if (redisCached) {
        const user = JSON.parse(redisCached);
        memoryCache.set(`user:${userId}`, user);
        return user;
    }
  
    // Level 3: Database
    const user = await db.query('SELECT * FROM users WHERE id = $1', [userId]);
  
    // Cache results
    memoryCache.set(`user:${userId}`, user);
    await redisClient.setEx(
        `user:${userId}`,
        3600, // 1 hour
        JSON.stringify(user)
    );
  
    return user;
}
```

#### 5.2. Cache Invalidation Patterns

```javascript
// Write-through: Update cache khi write
async function updateUser(userId, data) {
    // Update database
    const user = await db.query(
        'UPDATE users SET ... WHERE id = $1 RETURNING *',
        [userId]
    );
  
    // Update cache immediately
    await redisClient.setEx(
        `user:${userId}`,
        3600,
        JSON.stringify(user)
    );
    memoryCache.set(`user:${userId}`, user);
  
    return user;
}

// Write-behind: Update cache sau khi write
async function createOrder(orderData) {
    // Write to database
    const order = await db.query('INSERT INTO orders ...');
  
    // Invalidate related cache
    await redisClient.del(`user:${order.user_id}:orders`);
    await redisClient.del(`user:${order.user_id}:stats`);
  
    return order;
}

// TTL-based: Let cache expire naturally
// Good for data that doesn't change often
```

**📚 GIẢI THÍCH CHI TIẾT - CACHING STRATEGIES:**

**Tại sao cần Multi-level Caching?**

**Latency Comparison:**

```
Memory (L1): ~0.1ms
Redis (L2): ~1ms
Database (L3): ~10ms

Speedup:
- Memory vs Database: 100x
- Redis vs Database: 10x
```

**Cache Hit Rate:**

```
Ideal: > 80% cache hit rate

Ví dụ với 1000 requests:
- 800 cache hits (0.1ms) = 80ms
- 200 cache misses (10ms) = 2000ms
- Total: 2080ms

Without cache:
- 1000 requests (10ms) = 10000ms

Speedup: ~5x!
```

**Cache-Aside Pattern:**

**Cơ chế:**

1. Application check cache
2. Cache hit → Return
3. Cache miss → Query DB → Store cache → Return

**Ưu điểm:**

- ✅ Đơn giản implement
- ✅ Cache chỉ chứa data được đọc
- ✅ Database là source of truth

**Nhược điểm:**

- ❌ Cache miss penalty (2 trips)
- ❌ Có thể có stale data
- ❌ Race condition nếu 2 requests cùng miss

**Write-Through Pattern:**

**Cơ chế:**

1. Write to database
2. Write to cache immediately
3. Return

**Ưu điểm:**

- ✅ Data luôn consistent
- ✅ Cache luôn có latest data

**Nhược điểm:**

- ❌ Write chậm hơn (2 writes)
- ❌ Cache có thể chứa data không được đọc
- ❌ Wasted cache space

**Write-Behind Pattern:**

**Cơ chế:**

1. Write to cache immediately
2. Return (fast!)
3. Write to database async (background)

**Ưu điểm:**

- ✅ Write rất nhanh
- ✅ Better user experience

**Nhược điểm:**

- ❌ Risk mất data nếu cache crash
- ❌ Phức tạp implement
- ❌ Cần handle failures

**Khi nào dùng gì:**

- **Cache-Aside**: Read-heavy, có thể chấp nhận stale data
- **Write-Through**: Cần consistency cao
- **Write-Behind**: Write-heavy, performance critical

**Cache Invalidation:**

**Strategies:**

1. **TTL-based**: Để cache expire tự nhiên
   - Đơn giản
   - Có thể có stale data
2. **Event-based**: Invalidate khi data thay đổi
   - Consistent
   - Phức tạp hơn
3. **Version-based**: Cache với version, invalidate khi version thay đổi
   - Flexible
   - Cần maintain versions

### 6. READ REPLICAS - SCALE READS

#### 6.1. Read Replica Setup

```javascript
// Master (write)
const masterDB = new Pool({
    host: 'master-db.example.com',
    // ... write operations
});

// Replica (read)
const replicaDB = new Pool({
    host: 'replica-db.example.com',
    // ... read operations
});

// Route queries
async function getUsers() {
    // Read from replica
    return await replicaDB.query('SELECT * FROM users');
}

async function createUser(userData) {
    // Write to master
    return await masterDB.query(
        'INSERT INTO users ...',
        userData
    );
}

// Load balancing multiple replicas
const replicas = [
    new Pool({ host: 'replica-1.example.com' }),
    new Pool({ host: 'replica-2.example.com' }),
    new Pool({ host: 'replica-3.example.com' })
];

function getReplica() {
    // Round-robin
    return replicas[Math.floor(Math.random() * replicas.length)];
}
```

#### 6.2. Replication Lag Handling

```javascript
// Read-after-write consistency
async function createUserAndGet(userData) {
    // Write to master
    const user = await masterDB.query('INSERT INTO users ...');
  
    // Read from master (not replica) để đảm bảo consistency
    const createdUser = await masterDB.query(
        'SELECT * FROM users WHERE id = $1',
        [user.id]
    );
  
    return createdUser;
}

// Sticky session: Route user's reads to same replica
const userReplicaMap = new Map();

function getReplicaForUser(userId) {
    if (!userReplicaMap.has(userId)) {
        userReplicaMap.set(userId, getReplica());
    }
    return userReplicaMap.get(userId);
}
```

### 7. DATABASE MONITORING - PRODUCTION ESSENTIALS

#### 7.1. Slow Query Logging

```sql
-- PostgreSQL: Enable slow query log
ALTER SYSTEM SET log_min_duration_statement = 1000; -- Log queries > 1s
ALTER SYSTEM SET log_statement = 'all';
SELECT pg_reload_conf();

-- MySQL: Enable slow query log
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 1; -- Log queries > 1s
```

#### 7.2. Query Performance Monitoring

```sql
-- PostgreSQL: pg_stat_statements
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Top slow queries
SELECT 
    query,
    calls,
    total_exec_time,
    mean_exec_time,
    max_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- Queries using most I/O
SELECT 
    query,
    calls,
    shared_blks_hit,
    shared_blks_read,
    shared_blks_dirtied
FROM pg_stat_statements
ORDER BY shared_blks_read DESC
LIMIT 10;
```

#### 7.3. Table và Index Statistics

```sql
-- Table sizes
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Index sizes
SELECT 
    schemaname,
    tablename,
    indexname,
    pg_size_pretty(pg_relation_size(indexrelid)) AS index_size
FROM pg_stat_user_indexes
ORDER BY pg_relation_size(indexrelid) DESC;

-- Table bloat (wasted space)
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS total_size,
    pg_size_pretty(pg_relation_size(schemaname||'.'||tablename)) AS table_size,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename) - 
                   pg_relation_size(schemaname||'.'||tablename)) AS wasted
FROM pg_tables
WHERE schemaname = 'public';
```

### 8. TRANSACTION MANAGEMENT - BEST PRACTICES

#### 8.1. Transaction Isolation Levels

```sql
-- Read Uncommitted (PostgreSQL không support)
-- Read Committed (Default)
BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT * FROM users WHERE id = 1;
COMMIT;

-- Repeatable Read
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SELECT * FROM users WHERE id = 1;
-- Read again sẽ giữ nguyên giá trị
COMMIT;

-- Serializable (Highest isolation)
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
-- Đảm bảo không có phantom reads
COMMIT;
```

#### 8.2. Deadlock Prevention

```sql
-- Always lock resources in same order
-- ❌ Bad: Different order có thể gây deadlock
-- Transaction 1: Lock user 1, then user 2
-- Transaction 2: Lock user 2, then user 1

-- ✅ Good: Always lock by ID order
BEGIN;
SELECT * FROM users WHERE id IN (1, 2) ORDER BY id FOR UPDATE;
-- Process...
COMMIT;

-- Set lock timeout
SET lock_timeout = '5s';
```

#### 8.3. Long-running Transactions

```javascript
// ❌ Bad: Long transaction
async function processLargeBatch() {
    await db.query('BEGIN');
    for (const item of largeArray) {
        await db.query('INSERT INTO ...', item);
    }
    await db.query('COMMIT'); // Transaction quá lâu!
}

// ✅ Good: Batch transactions
async function processLargeBatch() {
    const batchSize = 1000;
    for (let i = 0; i < largeArray.length; i += batchSize) {
        const batch = largeArray.slice(i, i + batchSize);
        await db.query('BEGIN');
        for (const item of batch) {
            await db.query('INSERT INTO ...', item);
        }
        await db.query('COMMIT');
    }
}
```

### 9. DATABASE MAINTENANCE

#### 9.1. Vacuum và Analyze

```sql
-- PostgreSQL: VACUUM (reclaim space)
VACUUM;                      -- Regular vacuum
VACUUM FULL;                 -- Full vacuum (locks table)
VACUUM ANALYZE;              -- Vacuum + update statistics

-- Auto-vacuum configuration
ALTER TABLE users SET (
    autovacuum_vacuum_scale_factor = 0.1,
    autovacuum_analyze_scale_factor = 0.05
);

-- Analyze để update statistics
ANALYZE users;
ANALYZE VERBOSE users;       -- Với thông tin chi tiết
```

#### 9.2. Index Maintenance

```sql
-- Rebuild index
REINDEX INDEX idx_email;
REINDEX TABLE users;

-- Concurrent reindex (không lock table)
REINDEX INDEX CONCURRENTLY idx_email;

-- Update statistics cho index
ANALYZE users;
```

### 10. SECURITY BEST PRACTICES

#### 10.1. SQL Injection Prevention

```javascript
// ❌ Bad: String concatenation
const query = `SELECT * FROM users WHERE email = '${email}'`;

// ✅ Good: Parameterized queries
const query = 'SELECT * FROM users WHERE email = $1';
await db.query(query, [email]);

// ✅ Good: ORM (tự động parameterize)
const user = await User.findOne({ where: { email } });
```

#### 10.2. Principle of Least Privilege

```sql
-- Tạo user với quyền hạn chế
CREATE USER app_user WITH PASSWORD 'secure_password';

-- Chỉ cho phép SELECT, INSERT, UPDATE trên bảng cụ thể
GRANT SELECT, INSERT, UPDATE ON users TO app_user;
GRANT SELECT ON orders TO app_user;

-- Không cho DELETE
-- REVOKE DELETE ON users FROM app_user;

-- Tạo read-only user cho reporting
CREATE USER readonly_user WITH PASSWORD 'readonly_password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_user;
```

#### 10.3. Encryption

```sql
-- Encrypt sensitive columns (PostgreSQL pgcrypto)
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    password_hash BYTEA,  -- Encrypted
    ssn_encrypted BYTEA   -- Encrypted SSN
);

-- Encrypt khi insert
INSERT INTO users (email, ssn_encrypted) 
VALUES ('user@example.com', pgp_sym_encrypt('123-45-6789', 'encryption_key'));

-- Decrypt khi query
SELECT email, pgp_sym_decrypt(ssn_encrypted, 'encryption_key') as ssn
FROM users WHERE id = 1;
```

### 11. BACKUP VÀ DISASTER RECOVERY

#### 11.1. Backup Strategy

```bash
# PostgreSQL: pg_dump
pg_dump -h localhost -U user -d mydb -F c -f backup.dump

# Full backup
pg_dumpall > full_backup.sql

# Continuous archiving (WAL)
# postgresql.conf:
wal_level = replica
archive_mode = on
archive_command = 'cp %p /backup/wal/%f'
```

#### 11.2. Point-in-Time Recovery

```bash
# Restore từ backup
pg_restore -h localhost -U user -d mydb backup.dump

# Point-in-time recovery
# 1. Restore base backup
# 2. Apply WAL files đến thời điểm cụ thể
```

### 12. SCALING STRATEGIES

#### 12.1. Vertical Scaling

- Tăng CPU, RAM, Storage
- Đơn giản nhưng có giới hạn
- Phù hợp khi: Load tăng đều, Budget cho phép

#### 12.2. Horizontal Scaling

**Sharding:**

```sql
-- Shard users theo user_id
-- Shard 1: user_id % 4 = 0
-- Shard 2: user_id % 4 = 1
-- Shard 3: user_id % 4 = 2
-- Shard 4: user_id % 4 = 3

-- Application code
function getShard(userId) {
    return `shard_${userId % 4}`;
}

async function getUser(userId) {
    const shard = getShard(userId);
    const db = getShardConnection(shard);
    return await db.query('SELECT * FROM users WHERE id = $1', [userId]);
}
```

**Database per Tenant (Multi-tenancy):**

```javascript
// Mỗi tenant có database riêng
async function getTenantDB(tenantId) {
    const dbName = `tenant_${tenantId}`;
    return getConnection(dbName);
}

async function getData(tenantId, dataId) {
    const db = await getTenantDB(tenantId);
    return await db.query('SELECT * FROM data WHERE id = $1', [dataId]);
}
```

### 13. COMMON MISTAKES VÀ CÁCH TRÁNH

**Mistake 1: Không có indexes**

```sql
-- ❌ Bad: Query chậm
SELECT * FROM users WHERE email = 'user@example.com';
-- Seq Scan trên 1M rows

-- ✅ Good: Có index
CREATE INDEX idx_email ON users(email);
SELECT * FROM users WHERE email = 'user@example.com';
-- Index Scan, nhanh hơn 1000x
```

**Mistake 2: Quá nhiều indexes**

```sql
-- ❌ Bad: Index mọi column
CREATE INDEX idx_name ON users(name);
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_age ON users(age);
CREATE INDEX idx_city ON users(city);
-- Mỗi INSERT phải update 4 indexes!

-- ✅ Good: Chỉ index columns thường query
CREATE INDEX idx_email ON users(email); -- Email thường query
-- name, age, city ít query -> không cần index
```

**Mistake 3: Không monitor slow queries**

```sql
-- ✅ Good: Enable slow query log và monitor thường xuyên
-- Tìm và optimize slow queries
```

**Mistake 4: Không có connection pooling**

```javascript
// ❌ Bad: Tạo connection mới mỗi request
app.get('/users', async (req, res) => {
    const db = new Pool(); // New connection!
    const users = await db.query('SELECT * FROM users');
    // Connection không được close properly
});

// ✅ Good: Reuse connection pool
const pool = new Pool({ max: 20 });
app.get('/users', async (req, res) => {
    const users = await pool.query('SELECT * FROM users');
    // Connection được reuse
});
```

### 14. PERFORMANCE CHECKLIST

**Pre-production:**

- [ ] Tất cả queries có indexes phù hợp
- [ ] Connection pooling được config
- [ ] Slow query logging enabled
- [ ] Backup strategy đã setup
- [ ] Monitoring và alerting đã config
- [ ] Read replicas nếu cần
- [ ] Caching strategy đã implement

**Production:**

- [ ] Monitor slow queries hàng ngày
- [ ] Review index usage định kỳ
- [ ] Vacuum/Analyze định kỳ
- [ ] Review connection pool stats
- [ ] Monitor database size và growth
- [ ] Review và optimize top slow queries
- [ ] Test backup restore thường xuyên

### 5.3. Git và GitHub - Lệnh cho Mọi Tình Huống

#### 1. Git Basics - Khởi đầu

**Kiến thức:**

- **Định nghĩa:** Hệ thống quản lý phiên bản phân tán; lưu lịch sử thay đổi code, hỗ trợ branch/merge, cộng tác qua remote (GitHub/GitLab).
- git init: Khởi tạo repository
- git add: Thêm files vào staging area
- git commit: Lưu snapshot
- git status: Kiểm tra trạng thái
- git log: Xem lịch sử commits

**Commands:**

```bash
# Khởi tạo repository
git init
git init --bare  # Bare repository (cho server)

# Cấu hình Git (lần đầu)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
git config --list  # Xem tất cả config

# Thêm files vào staging
git add .                    # Thêm tất cả
git add file.txt             # Thêm file cụ thể
git add *.js                 # Thêm tất cả .js files
git add src/                 # Thêm cả thư mục
git add -A                   # Thêm tất cả (bao gồm deleted files)
git add -u                   # Chỉ thêm files đã tracked

# Commit
git commit -m "Initial commit"
git commit -m "Add feature" -m "Detailed description"
git commit --amend           # Sửa commit cuối cùng
git commit --amend --no-edit # Sửa commit nhưng giữ message

# Xem trạng thái
git status
git status -s               # Short format
git status --ignored        # Hiển thị ignored files

# Xem lịch sử
git log
git log --oneline           # Compact format
git log --graph             # Với graph
git log --all --graph --oneline  # Tất cả branches
git log -5                  # 5 commits gần nhất
git log --since="2 weeks ago"
git log --author="John"
git log --grep="bug fix"
git log file.txt            # Lịch sử của file cụ thể
```

#### 2. Undo Changes - Các Tình Huống Thường Gặp

**Tình huống 1: Chưa add, muốn undo changes trong working directory**

```bash
# Xem thay đổi
git diff

# Undo changes trong file cụ thể
git checkout -- file.txt
git restore file.txt        # Git 2.23+

# Undo tất cả changes
git checkout -- .
git restore .               # Git 2.23+

# Undo changes và xóa untracked files
git clean -fd               # -f: force, -d: directories
git clean -n                # Dry run (xem sẽ xóa gì)
```

**Tình huống 2: Đã add nhưng chưa commit, muốn unstage**

```bash
# Unstage file cụ thể
git reset HEAD file.txt
git restore --staged file.txt  # Git 2.23+

# Unstage tất cả
git reset HEAD
git restore --staged .         # Git 2.23+
```

**Tình huống 3: Đã commit, muốn sửa commit cuối**

```bash
# Sửa commit message
git commit --amend

# Thêm file vào commit cuối
git add forgotten-file.txt
git commit --amend --no-edit

# Sửa commit và thay đổi message
git commit --amend -m "New message"
```

**Tình huống 4: Muốn xóa commit cuối (giữ changes)**

```bash
# Soft reset - giữ changes trong staging
git reset --soft HEAD~1

# Mixed reset (default) - giữ changes trong working directory
git reset HEAD~1
git reset --mixed HEAD~1

# Hard reset - XÓA TẤT CẢ (cẩn thận!)
git reset --hard HEAD~1
```

**Tình huống 5: Muốn xóa nhiều commits**

```bash
# Xóa 3 commits gần nhất (giữ changes)
git reset HEAD~3

# Xóa đến commit cụ thể
git reset <commit-hash>

# Xóa tất cả và quay về commit đầu tiên
git reset --hard <initial-commit-hash>
```

**Tình huống 6: Đã push, muốn undo (cần cẩn thận!)**

```bash
# Tạo commit mới để revert (an toàn)
git revert HEAD
git revert <commit-hash>
git revert HEAD~3..HEAD     # Revert nhiều commits

# Force push (chỉ khi làm việc một mình!)
git reset --hard HEAD~1
git push --force            # ⚠️ Nguy hiểm!
git push --force-with-lease # An toàn hơn
```

#### 3. Stash - Tạm thời lưu changes

**Tình huống: Đang làm dở, cần switch branch**

```bash
# Stash changes
git stash
git stash save "WIP: working on feature"

# Xem danh sách stash
git stash list

# Apply stash (giữ stash)
git stash apply
git stash apply stash@{0}

# Apply và xóa stash
git stash pop
git stash pop stash@{0}

# Xóa stash
git stash drop stash@{0}
git stash clear              # Xóa tất cả

# Stash với untracked files
git stash -u                 # Include untracked
git stash -a                 # Include ignored files

# Tạo branch từ stash
git stash branch new-branch stash@{0}

# Xem nội dung stash
git stash show
git stash show -p            # Với diff
```

#### 4. Branching - Quản lý nhánh

**Tạo và chuyển branch:**

```bash
# Tạo branch mới
git branch feature-branch
git branch -b feature-branch  # Tạo và chuyển ngay

# Chuyển branch
git checkout feature-branch
git switch feature-branch     # Git 2.23+

# Tạo branch từ commit cụ thể
git branch new-branch <commit-hash>
git checkout -b new-branch <commit-hash>

# Tạo branch từ remote
git checkout -b local-branch origin/remote-branch
git switch -c local-branch origin/remote-branch
```

**Quản lý branches:**

```bash
# Xem tất cả branches
git branch                    # Local only
git branch -a                # Tất cả (local + remote)
git branch -r                # Remote only
git branch -v                # Với commit info

# Xóa branch
git branch -d feature-branch # Safe delete
git branch -D feature-branch # Force delete

# Xóa remote branch
git push origin --delete feature-branch
git push origin :feature-branch  # Cách cũ

# Rename branch
git branch -m old-name new-name
git branch -m new-name      # Rename current branch

# Xem branches đã merge
git branch --merged
git branch --no-merged
```

#### 5. Merge - Gộp nhánh

**Basic merge:**

```bash
# Merge branch vào current branch
git checkout main
git merge feature-branch

# Merge với no-fast-forward (tạo merge commit)
git merge --no-ff feature-branch

# Merge với message
git merge -m "Merge feature branch" feature-branch

# Abort merge (khi có conflict)
git merge --abort
```

**Merge strategies:**

```bash
# Ours strategy (giữ code của branch hiện tại)
git merge -s ours feature-branch

# Theirs strategy (giữ code của branch merge vào)
git merge -X theirs feature-branch

# Squash merge (gộp tất cả commits thành 1)
git merge --squash feature-branch
git commit -m "Squashed feature branch"
```

#### 6. Conflict Resolution - Giải quyết xung đột

**Khi có conflict:**

```bash
# Xem files có conflict
git status

# Mở file và sửa conflict
# <<<<<<< HEAD
# code từ current branch
# =======
# code từ branch merge vào
# >>>>>>> feature-branch

# Sau khi sửa xong
git add resolved-file.txt
git commit                  # Hoàn thành merge

# Sử dụng tool để resolve
git mergetool

# Chấp nhận tất cả từ một bên
git checkout --ours file.txt    # Giữ code của mình
git checkout --theirs file.txt   # Lấy code của họ
```

**Conflict trong rebase:**

```bash
# Khi rebase có conflict
git rebase --continue      # Sau khi sửa conflict
git rebase --abort         # Hủy rebase
git rebase --skip          # Bỏ qua commit này
```

#### 7. Rebase - Làm phẳng lịch sử

**Basic rebase:**

```bash
# Rebase current branch lên main
git checkout feature-branch
git rebase main

# Interactive rebase (sửa nhiều commits)
git rebase -i HEAD~3       # 3 commits gần nhất
git rebase -i <commit-hash>

# Trong interactive rebase:
# pick = giữ commit
# reword = sửa message
# edit = sửa commit
# squash = gộp với commit trước
# fixup = giống squash nhưng bỏ message
# drop = xóa commit

# Rebase onto
git rebase --onto main feature-branch~3 feature-branch
```

**Rebase với remote (cẩn thận!):**

```bash
# Rebase và force push
git rebase main
git push --force-with-lease

# Pull với rebase thay vì merge
git pull --rebase
git config pull.rebase true  # Set default
```

#### 8. Cherry-pick - Lấy commit cụ thể

**Tình huống: Cần lấy 1 commit từ branch khác**

```bash
# Cherry-pick commit
git cherry-pick <commit-hash>

# Cherry-pick nhiều commits
git cherry-pick <hash1> <hash2>
git cherry-pick <hash1>..<hash2>  # Range (không include hash1)

# Cherry-pick với edit
git cherry-pick -e <commit-hash>  # Edit message
git cherry-pick -n <commit-hash>  # Chưa commit (để sửa)
git cherry-pick --no-commit <commit-hash>

# Resolve conflict trong cherry-pick
# Sửa conflict, sau đó:
git add .
git cherry-pick --continue
# hoặc
git cherry-pick --abort
```

#### 9. Remote - Làm việc với GitHub/GitLab

**Quản lý remotes:**

```bash
# Xem remotes
git remote
git remote -v               # Với URLs

# Thêm remote
git remote add origin https://github.com/user/repo.git
git remote add upstream https://github.com/original/repo.git

# Sửa remote URL
git remote set-url origin https://github.com/user/new-repo.git

# Xóa remote
git remote remove origin

# Rename remote
git remote rename old-name new-name

# Xem thông tin remote
git remote show origin
```

**Push và Pull:**

```bash
# Push
git push origin main
git push -u origin main    # Set upstream
git push --all             # Push tất cả branches
git push --tags            # Push tags

# Force push (cẩn thận!)
git push --force
git push --force-with-lease  # An toàn hơn

# Pull
git pull origin main
git pull --rebase          # Pull với rebase

# Fetch (chỉ tải về, không merge)
git fetch origin
git fetch --all            # Fetch tất cả remotes
git fetch origin main      # Fetch branch cụ thể
```

**Sync với remote:**

```bash
# Xem khác biệt với remote
git fetch origin
git diff main origin/main

# Update local branch từ remote
git pull origin main
# hoặc
git fetch origin
git merge origin/main

# Xóa local branches đã xóa trên remote
git fetch --prune
git remote prune origin
```

#### 10. Tags - Đánh dấu version

```bash
# Tạo tag
git tag v1.0.0
git tag -a v1.0.0 -m "Release version 1.0.0"

# Xem tags
git tag
git tag -l "v1.*"          # Filter

# Xóa tag
git tag -d v1.0.0
git push origin --delete v1.0.0  # Xóa trên remote

# Push tags
git push origin v1.0.0
git push --tags            # Push tất cả tags

# Checkout tag
git checkout v1.0.0
```

#### 11. Reflog - Cứu dữ liệu

**Tình huống: Xóa nhầm commit/branch**

```bash
# Xem reflog (lịch sử tất cả thao tác)
git reflog
git reflog show main       # Reflog của branch cụ thể

# Khôi phục từ reflog
git checkout <commit-hash-from-reflog>
git branch recovered-branch <commit-hash>

# Khôi phục branch đã xóa
git reflog
git branch recovered-branch <commit-hash>
```

#### 12. Diff - Xem thay đổi

```bash
# Xem changes trong working directory
git diff

# Xem changes đã staged
git diff --staged
git diff --cached

# Xem changes giữa commits
git diff HEAD~1 HEAD
git diff <commit1> <commit2>

# Xem changes của file cụ thể
git diff file.txt
git diff HEAD~1 HEAD -- file.txt

# Xem changes giữa branches
git diff main..feature-branch
git diff main...feature-branch  # Chỉ changes trong feature-branch

# Xem stats
git diff --stat
```

#### 13. Submodules - Quản lý dependencies

```bash
# Thêm submodule
git submodule add https://github.com/user/repo.git path/to/submodule

# Clone repo với submodules
git clone --recursive https://github.com/user/repo.git
# hoặc sau khi clone
git submodule update --init --recursive

# Update submodules
git submodule update --remote

# Xóa submodule
git submodule deinit path/to/submodule
git rm path/to/submodule
```

#### 14. Worktrees - Nhiều working directories

**Tình huống: Cần làm việc trên nhiều branches cùng lúc**

```bash
# Tạo worktree
git worktree add ../project-feature feature-branch

# Xem worktrees
git worktree list

# Xóa worktree
git worktree remove ../project-feature
```

#### 15. Các Tình Huống Thực Tế Thường Gặp

**Tình huống 1: Commit nhầm vào main, cần chuyển sang branch khác**

```bash
# Tạo branch mới từ commit hiện tại
git branch feature-branch

# Reset main về commit trước
git reset --hard HEAD~1

# Chuyển sang branch mới
git checkout feature-branch
```

**Tình huống 2: Commit message sai, chưa push**

```bash
git commit --amend -m "Correct message"
```

**Tình huống 3: Quên add file vào commit cuối**

```bash
git add forgotten-file.txt
git commit --amend --no-edit
```

**Tình huống 4: Muốn tách commit lớn thành nhiều commits nhỏ**

```bash
git reset HEAD~1              # Undo commit, giữ changes
git add file1.txt
git commit -m "Add file1"
git add file2.txt
git commit -m "Add file2"
```

**Tình huống 5: Muốn gộp nhiều commits thành 1**

```bash
git reset --soft HEAD~3       # Gộp 3 commits
git commit -m "Combined commits"
```

**Tình huống 6: Cần xóa file khỏi Git nhưng giữ trong working directory**

```bash
git rm --cached file.txt
git commit -m "Remove file from tracking"
```

**Tình huống 7: Cần xóa file khỏi Git history (có sensitive data)**

```bash
# Sử dụng git filter-branch hoặc BFG Repo-Cleaner
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch sensitive-file.txt" \
  --prune-empty --tag-name-filter cat -- --all

# Force push (cẩn thận!)
git push --force --all
```

**Tình huống 8: Cần tìm commit đã xóa file**

```bash
git log --all --full-history -- file.txt
git log --diff-filter=D --summary
```

**Tình huống 9: Cần tìm commit gây ra bug**

```bash
# Binary search với git bisect
git bisect start
git bisect bad                # Current commit is bad
git bisect good <commit-hash> # Known good commit
# Test và mark good/bad
git bisect good
git bisect bad
git bisect reset              # Khi tìm thấy
```

**Tình huống 10: Cần backup trước khi làm thao tác nguy hiểm**

```bash
# Tạo backup branch
git branch backup-before-reset

# Hoặc tạo tag
git tag backup-$(date +%Y%m%d)
```

**Tình huống 11: Cần xem ai đã sửa dòng code này**

```bash
git blame file.txt
git blame -L 10,20 file.txt   # Dòng 10-20
```

**Tình huống 12: Cần tìm commit có chứa text cụ thể**

```bash
git log -S "search text"      # Tìm trong code
git log -G "regex pattern"    # Tìm với regex
git log --all --grep="text"   # Tìm trong messages
```

**Tình huống 13: Cần xem file ở commit cụ thể**

```bash
git show <commit-hash>:file.txt
git checkout <commit-hash> -- file.txt
```

**Tình huống 14: Cần xem commit sẽ được push**

```bash
git log origin/main..HEAD
git diff origin/main..HEAD
```

**Tình huống 15: Cần cleanup branches đã merge**

```bash
# Xóa local branches đã merge vào main
git branch --merged main | grep -v "main" | xargs git branch -d

# Xóa remote branches đã merge
git branch -r --merged main | grep -v "main" | sed 's/origin\///' | xargs -n 1 git push origin --delete
```

#### 16. GitHub - Pull Requests và Collaboration

**Workflow với Pull Request:**

```bash
# 1. Fork hoặc clone repo
git clone https://github.com/user/repo.git
cd repo

# 2. Tạo branch mới
git checkout -b feature-branch

# 3. Làm việc và commit
git add .
git commit -m "Add feature"

# 4. Push branch
git push -u origin feature-branch

# 5. Tạo Pull Request trên GitHub
# Sau đó có thể update PR:
git add .
git commit -m "Update feature"
git push

# 6. Sau khi PR được merge, cleanup
git checkout main
git pull origin main
git branch -d feature-branch
git push origin --delete feature-branch
```

**Sync fork với upstream:**

```bash
# Thêm upstream remote
git remote add upstream https://github.com/original/repo.git

# Fetch từ upstream
git fetch upstream

# Merge vào main
git checkout main
git merge upstream/main

# Push lên fork
git push origin main
```

**Best Practices:**

```bash
# 1. Commit messages rõ ràng
git commit -m "feat: add user authentication"
git commit -m "fix: resolve login bug"
git commit -m "docs: update README"

# 2. Branch naming
feature/user-authentication
bugfix/login-error
hotfix/security-patch

# 3. Regular commits
# Commit thường xuyên, mỗi commit là một logical change

# 4. Code review
# Luôn tạo PR và review trước khi merge

# 5. .gitignore
# Luôn ignore: node_modules, .env, build/, dist/, *.log
```

### 5.4. Project: Blog với CRUD + Database

**Yêu cầu:**

- Tạo database schema
- CRUD operations cho posts
- User authentication (cơ bản)
- Deploy lên Heroku/Vercel

**Database Schema:**

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# GIAI ĐOẠN 2: FULL STACK WEB (Tháng 4-9)

## THÁNG 4: Frontend Foundation

### 6.1. HTML5

#### Semantic Elements

**Kiến thức:**

- `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`
- Semantic HTML giúp SEO và accessibility

**Ví dụ:**

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
            </ul>
        </nav>
    </header>
  
    <main>
        <article>
            <h1>Article Title</h1>
            <p>Content...</p>
        </article>
    </main>
  
    <footer>
        <p>© 2024</p>
    </footer>
</body>
</html>
```

#### Forms

**Kiến thức:**

- Form elements: input, textarea, select, button
- Input types: text, email, password, number, date, etc.
- Validation: required, pattern, min, max

**Ví dụ:**

```html
<form action="/submit" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
  
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
  
    <label for="age">Age:</label>
    <input type="number" id="age" name="age" min="18" max="100">
  
    <button type="submit">Submit</button>
</form>
```

### 6.2. CSS3

#### Flexbox

**Kiến thức:**

- Container properties: display, flex-direction, justify-content, align-items, flex-wrap
- Item properties: flex, align-self, order

**Ví dụ:**

```css
.container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.item {
    flex: 1;
    align-self: flex-start;
}
```

#### Grid

**Kiến thức:**

- Grid container: display, grid-template-columns, grid-template-rows, gap
- Grid items: grid-column, grid-row, grid-area

**Ví dụ:**

```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: auto;
    gap: 20px;
}

.item {
    grid-column: span 2;
    grid-row: 1;
}
```

#### Responsive Design

**Kiến thức:**

- Media queries
- Mobile-first approach
- Breakpoints

**Ví dụ:**

```css
/* Mobile first */
.container {
    width: 100%;
    padding: 10px;
}

/* Tablet */
@media (min-width: 768px) {
    .container {
        max-width: 750px;
        margin: 0 auto;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .container {
        max-width: 1200px;
    }
}
```

### 6.3. JavaScript ES6+ - Học để Code

#### 1. Variables: let, const, var

**Kiến thức:**

- `var`: Function-scoped, có hoisting
- `let`: Block-scoped, có thể reassign
- `const`: Block-scoped, không thể reassign (nhưng object/array bên trong có thể thay đổi)

**Ví dụ code:**

```javascript
// var - Function scoped
function exampleVar() {
    if (true) {
        var x = 10;
    }
    console.log(x); // 10 - accessible outside block
}

// let - Block scoped
function exampleLet() {
    if (true) {
        let y = 20;
    }
    // console.log(y); // ReferenceError: y is not defined
}

// const - Block scoped, cannot reassign
const PI = 3.14159;
// PI = 3.14; // TypeError: Assignment to constant variable

// const với objects/arrays - có thể mutate
const person = { name: 'John', age: 25 };
person.age = 26; // ✅ OK
person.city = 'NYC'; // ✅ OK
// person = {}; // ❌ Error

const numbers = [1, 2, 3];
numbers.push(4); // ✅ OK
numbers[0] = 10; // ✅ OK
// numbers = []; // ❌ Error

// Hoisting
console.log(a); // undefined (not error)
var a = 5;

// console.log(b); // ReferenceError
let b = 5;

// Temporal Dead Zone
function example() {
    console.log(typeof x); // ReferenceError
    let x = 10;
}
```

#### 2. Arrow Functions

**Kiến thức:**

- Cú pháp ngắn gọn
- Không có `this` binding riêng (lexical this)
- Không có `arguments` object
- Không thể dùng làm constructor

**Ví dụ code:**

```javascript
// Basic syntax
const add = (a, b) => a + b;
const square = x => x * x;
const greet = () => console.log('Hello');

// Multiple statements
const process = (data) => {
    const result = data.map(item => item * 2);
    return result.filter(item => item > 10);
};

// this binding
class Counter {
    constructor() {
        this.count = 0;
    }
  
    // ❌ Regular function - this is lost
    incrementBad() {
        setTimeout(function() {
            this.count++; // this is undefined
        }, 1000);
    }
  
    // ✅ Arrow function - this is preserved
    incrementGood() {
        setTimeout(() => {
            this.count++; // this refers to Counter instance
        }, 1000);
    }
}

// Returning objects
const createUser = (name, age) => ({ name, age });
// Equivalent to:
const createUser2 = (name, age) => {
    return { name, age };
};

// Higher-order functions
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((acc, n) => acc + n, 0);
```

#### 3. Template Literals

**Kiến thức:**

- Multi-line strings
- String interpolation
- Tagged templates

**Ví dụ code:**

```javascript
// Basic interpolation
const name = 'John';
const age = 25;
const message = `Hello, ${name}! You are ${age} years old.`;

// Multi-line strings
const html = `
    <div>
        <h1>${name}</h1>
        <p>Age: ${age}</p>
    </div>
`;

// Expressions
const a = 10;
const b = 20;
const result = `Sum: ${a + b}`; // "Sum: 30"

// Nested templates
const users = ['John', 'Jane', 'Bob'];
const list = `
    <ul>
        ${users.map(user => `<li>${user}</li>`).join('')}
    </ul>
`;

// Tagged templates
function highlight(strings, ...values) {
    return strings.reduce((result, string, i) => {
        const value = values[i] ? `<strong>${values[i]}</strong>` : '';
        return result + string + value;
    }, '');
}

const name2 = 'John';
const age2 = 25;
const output = highlight`Hello, ${name2}! You are ${age2} years old.`;
// "Hello, <strong>John</strong>! You are <strong>25</strong> years old."
```

#### 4. Destructuring

**Kiến thức:**

- Array destructuring
- Object destructuring
- Nested destructuring
- Default values
- Rest operator trong destructuring

**Ví dụ code:**

```javascript
// Array destructuring
const numbers = [1, 2, 3, 4, 5];
const [first, second, third] = numbers;
console.log(first, second, third); // 1 2 3

// Skip elements
const [a, , c] = numbers; // Skip second element
console.log(a, c); // 1 3

// Rest operator
const [head, ...tail] = numbers;
console.log(head); // 1
console.log(tail); // [2, 3, 4, 5]

// Default values
const [x = 0, y = 0] = [1];
console.log(x, y); // 1 0

// Swap variables
let a1 = 1, b1 = 2;
[a1, b1] = [b1, a1];
console.log(a1, b1); // 2 1

// Object destructuring
const person = {
    name: 'John',
    age: 25,
    city: 'NYC',
    email: 'john@example.com'
};

const { name, age } = person;
console.log(name, age); // John 25

// Rename variables
const { name: personName, age: personAge } = person;
console.log(personName, personAge); // John 25

// Default values
const { name: userName = 'Guest', country = 'USA' } = person;
console.log(userName, country); // John USA

// Nested destructuring
const user = {
    id: 1,
    profile: {
        name: 'John',
        address: {
            city: 'NYC',
            zip: '10001'
        }
    }
};

const {
    profile: {
        name: profileName,
        address: { city, zip }
    }
} = user;
console.log(profileName, city, zip); // John NYC 10001

// Rest trong object destructuring
const { name: userName2, ...rest } = person;
console.log(userName2); // John
console.log(rest); // { age: 25, city: 'NYC', email: 'john@example.com' }

// Function parameters
function greet({ name, age = 18 }) {
    return `Hello, ${name}! You are ${age} years old.`;
}

greet({ name: 'John', age: 25 }); // "Hello, John! You are 25 years old."
greet({ name: 'Jane' }); // "Hello, Jane! You are 18 years old."

// Return multiple values
function getCoordinates() {
    return { x: 10, y: 20 };
}

const { x, y } = getCoordinates();
console.log(x, y); // 10 20
```

#### 5. Spread Operator

**Kiến thức:**

- Spread trong arrays
- Spread trong objects
- Spread trong function calls
- Copy arrays/objects

**Ví dụ code:**

```javascript
// Spread trong arrays
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];
console.log(combined); // [1, 2, 3, 4, 5, 6]

// Copy array
const original = [1, 2, 3];
const copy = [...original];
copy.push(4);
console.log(original); // [1, 2, 3]
console.log(copy); // [1, 2, 3, 4]

// Add elements
const numbers = [1, 2, 3];
const newNumbers = [0, ...numbers, 4];
console.log(newNumbers); // [0, 1, 2, 3, 4]

// Spread trong function calls
function sum(a, b, c) {
    return a + b + c;
}

const numbers2 = [1, 2, 3];
console.log(sum(...numbers2)); // 6

// Spread với Math functions
const numbers3 = [5, 10, 15, 20];
console.log(Math.max(...numbers3)); // 20
console.log(Math.min(...numbers3)); // 5

// Spread trong objects (ES2018)
const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const merged = { ...obj1, ...obj2 };
console.log(merged); // { a: 1, b: 2, c: 3, d: 4 }

// Override properties
const defaults = { theme: 'light', fontSize: 14 };
const userSettings = { fontSize: 16 };
const finalSettings = { ...defaults, ...userSettings };
console.log(finalSettings); // { theme: 'light', fontSize: 16 }

// Copy object
const originalObj = { name: 'John', age: 25 };
const copyObj = { ...originalObj };
copyObj.age = 26;
console.log(originalObj); // { name: 'John', age: 25 }
console.log(copyObj); // { name: 'John', age: 26 }

// Shallow copy - nested objects
const nested = {
    user: {
        name: 'John',
        address: { city: 'NYC' }
    }
};
const shallowCopy = { ...nested };
shallowCopy.user.name = 'Jane';
console.log(nested.user.name); // 'Jane' - changed!

// Deep copy (cần thư viện hoặc JSON)
const deepCopy = JSON.parse(JSON.stringify(nested));
deepCopy.user.name = 'Bob';
console.log(nested.user.name); // 'Jane' - unchanged
```

#### 6. Default Parameters

**Kiến thức:**

- Default values cho function parameters
- Default values có thể là expressions
- Default values được evaluate mỗi lần gọi

**Ví dụ code:**

```javascript
// Basic default parameters
function greet(name = 'Guest') {
    return `Hello, ${name}!`;
}

greet(); // "Hello, Guest!"
greet('John'); // "Hello, John!"

// Multiple defaults
function createUser(name = 'Anonymous', age = 0, isActive = true) {
    return { name, age, isActive };
}

createUser(); // { name: 'Anonymous', age: 0, isActive: true }
createUser('John', 25); // { name: 'John', age: 25, isActive: true }

// Default với expressions
function getDate(format = 'YYYY-MM-DD') {
    const now = new Date();
    if (format === 'YYYY-MM-DD') {
        return now.toISOString().split('T')[0];
    }
    return now.toString();
}

// Default với function calls
function getDefaultId() {
    return Math.random().toString(36).substr(2, 9);
}

function createItem(name, id = getDefaultId()) {
    return { id, name };
}

// Default với destructuring
function processUser({ name = 'Guest', age = 0, email = '' } = {}) {
    return { name, age, email };
}

processUser(); // { name: 'Guest', age: 0, email: '' }
processUser({ name: 'John' }); // { name: 'John', age: 0, email: '' }
```

#### 7. Rest Parameters

**Kiến thức:**

- Thu thập remaining arguments
- Phải là parameter cuối cùng
- Tạo array từ arguments

**Ví dụ code:**

```javascript
// Rest parameters
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

sum(1, 2, 3, 4, 5); // 15
sum(10, 20); // 30

// Rest với other parameters
function greet(greeting, ...names) {
    return names.map(name => `${greeting}, ${name}!`).join(' ');
}

greet('Hello', 'John', 'Jane', 'Bob');
// "Hello, John! Hello, Jane! Hello, Bob!"

// Convert arguments to array (old way)
function oldWay() {
    const args = Array.from(arguments);
    return args.reduce((a, b) => a + b, 0);
}

// New way với rest
function newWay(...args) {
    return args.reduce((a, b) => a + b, 0);
}
```

#### 8. Enhanced Object Literals

**Kiến thức:**

- Shorthand property names
- Shorthand method names
- Computed property names

**Ví dụ code:**

```javascript
// Shorthand property names
const name = 'John';
const age = 25;

// Old way
const person1 = {
    name: name,
    age: age
};

// New way
const person2 = { name, age };

// Shorthand methods
const calculator = {
    // Old way
    add: function(a, b) {
        return a + b;
    },
  
    // New way
    subtract(a, b) {
        return a - b;
    },
  
    // Arrow function (không có this)
    multiply: (a, b) => a * b
};

// Computed property names
const prop = 'name';
const obj = {
    [prop]: 'John',
    [`${prop}Upper`]: 'JOHN',
    ['age']: 25
};
console.log(obj); // { name: 'John', nameUpper: 'JOHN', age: 25 }

// Dynamic property names
function createObject(key, value) {
    return {
        [key]: value
    };
}

createObject('email', 'john@example.com'); // { email: 'john@example.com' }
```

#### 9. Classes

**Kiến thức:**

- Class syntax
- Constructor
- Methods
- Static methods
- Getters và Setters
- Inheritance
- Private fields (ES2022)

**Ví dụ code:**

```javascript
// Basic class
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
  
    greet() {
        return `Hello, I'm ${this.name}`;
    }
  
    getInfo() {
        return `${this.name} is ${this.age} years old`;
    }
}

const john = new Person('John', 25);
console.log(john.greet()); // "Hello, I'm John"

// Static methods
class MathUtils {
    static add(a, b) {
        return a + b;
    }
  
    static multiply(a, b) {
        return a * b;
    }
}

console.log(MathUtils.add(5, 3)); // 8
console.log(MathUtils.multiply(5, 3)); // 15

// Getters và Setters
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
  
    get area() {
        return this.width * this.height;
    }
  
    set area(value) {
        this.width = Math.sqrt(value);
        this.height = Math.sqrt(value);
    }
}

const rect = new Rectangle(5, 10);
console.log(rect.area); // 50
rect.area = 100;
console.log(rect.width, rect.height); // 10 10

// Inheritance
class Animal {
    constructor(name) {
        this.name = name;
    }
  
    speak() {
        return `${this.name} makes a sound`;
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name); // Call parent constructor
        this.breed = breed;
    }
  
    speak() {
        return `${this.name} barks`;
    }
  
    getInfo() {
        return `${super.speak()}. It's a ${this.breed}`;
    }
}

const dog = new Dog('Buddy', 'Golden Retriever');
console.log(dog.speak()); // "Buddy barks"
console.log(dog.getInfo()); // "Buddy makes a sound. It's a Golden Retriever"

// Private fields (ES2022)
class BankAccount {
    #balance = 0; // Private field
  
    constructor(initialBalance = 0) {
        this.#balance = initialBalance;
    }
  
    deposit(amount) {
        if (amount > 0) {
            this.#balance += amount;
        }
    }
  
    withdraw(amount) {
        if (amount > 0 && amount <= this.#balance) {
            this.#balance -= amount;
        }
    }
  
    getBalance() {
        return this.#balance;
    }
}

const account = new BankAccount(100);
account.deposit(50);
console.log(account.getBalance()); // 150
// console.log(account.#balance); // SyntaxError: Private field
```

#### 10. Promises - Chi tiết

**Kiến thức:**

- Promise states: pending, fulfilled, rejected
- then, catch, finally
- Promise.all, Promise.allSettled, Promise.race
- Promise chaining
- Error handling

**Ví dụ code:**

```javascript
// Tạo Promise
const myPromise = new Promise((resolve, reject) => {
    const success = true;
  
    if (success) {
        resolve('Operation successful');
    } else {
        reject('Operation failed');
    }
});

// Sử dụng Promise
myPromise
    .then(result => console.log(result))
    .catch(error => console.error(error));

// Promise với async operation
function fetchUser(userId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (userId > 0) {
                resolve({ id: userId, name: 'John' });
            } else {
                reject(new Error('Invalid user ID'));
            }
        }, 1000);
    });
}

// Promise chaining
fetchUser(1)
    .then(user => {
        console.log('User:', user);
        return fetchUser(user.id + 1);
    })
    .then(nextUser => {
        console.log('Next user:', nextUser);
    })
    .catch(error => {
        console.error('Error:', error);
    });

// finally - luôn chạy
fetchUser(1)
    .then(user => console.log(user))
    .catch(error => console.error(error))
    .finally(() => {
        console.log('Request completed');
    });

// Promise.all - chờ tất cả, fail nếu một cái fail
const promise1 = fetchUser(1);
const promise2 = fetchUser(2);
const promise3 = fetchUser(3);

Promise.all([promise1, promise2, promise3])
    .then(users => {
        console.log('All users:', users);
    })
    .catch(error => {
        console.error('One failed:', error);
    });

// Promise.allSettled - chờ tất cả, không fail
Promise.allSettled([promise1, promise2, promise3])
    .then(results => {
        results.forEach((result, index) => {
            if (result.status === 'fulfilled') {
                console.log(`User ${index + 1}:`, result.value);
            } else {
                console.error(`User ${index + 1} failed:`, result.reason);
            }
        });
    });

// Promise.race - trả về promise đầu tiên hoàn thành
Promise.race([
    fetchUser(1),
    fetchUser(2),
    fetchUser(3)
])
    .then(firstUser => {
        console.log('First user loaded:', firstUser);
    });

// Promise với timeout
function fetchWithTimeout(url, timeout = 5000) {
    return Promise.race([
        fetch(url),
        new Promise((_, reject) =>
            setTimeout(() => reject(new Error('Timeout')), timeout)
        )
    ]);
}

// Convert callback to Promise
function readFilePromise(filename) {
    return new Promise((resolve, reject) => {
        fs.readFile(filename, 'utf8', (err, data) => {
            if (err) reject(err);
            else resolve(data);
        });
    });
}
```

#### 11. Async/Await - Chi tiết

**Kiến thức:**

- async functions luôn return Promise
- await chỉ dùng trong async functions
- Error handling với try/catch
- Parallel execution
- Sequential execution

**Ví dụ code:**

```javascript
// Basic async/await
async function fetchUserData(userId) {
    try {
        const response = await fetch(`/api/users/${userId}`);
        const user = await response.json();
        return user;
    } catch (error) {
        console.error('Error fetching user:', error);
        throw error;
    }
}

// Sequential execution
async function processSequentially() {
    const user1 = await fetchUser(1);
    console.log('User 1:', user1);
  
    const user2 = await fetchUser(2);
    console.log('User 2:', user2);
  
    const user3 = await fetchUser(3);
    console.log('User 3:', user3);
}

// Parallel execution
async function processParallel() {
    const [user1, user2, user3] = await Promise.all([
        fetchUser(1),
        fetchUser(2),
        fetchUser(3)
    ]);
  
    console.log('All users:', user1, user2, user3);
}

// Error handling
async function safeFetch(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Fetch error:', error);
        return null; // Return default value
    }
}

// Multiple async operations với error handling
async function fetchMultipleUsers(userIds) {
    const results = await Promise.allSettled(
        userIds.map(id => fetchUser(id))
    );
  
    const users = [];
    const errors = [];
  
    results.forEach((result, index) => {
        if (result.status === 'fulfilled') {
            users.push(result.value);
        } else {
            errors.push({ userId: userIds[index], error: result.reason });
        }
    });
  
    return { users, errors };
}

// Async trong loops
async function processUsers(userIds) {
    // ❌ Sequential - chậm
    for (const id of userIds) {
        const user = await fetchUser(id);
        console.log(user);
    }
  
    // ✅ Parallel - nhanh
    const users = await Promise.all(
        userIds.map(id => fetchUser(id))
    );
    users.forEach(user => console.log(user));
}

// Async arrow functions
const fetchData = async (url) => {
    const response = await fetch(url);
    return response.json();
};

// Async trong class methods
class UserService {
    async getUser(userId) {
        const response = await fetch(`/api/users/${userId}`);
        return response.json();
    }
  
    async getUsers(userIds) {
        return Promise.all(
            userIds.map(id => this.getUser(id))
        );
    }
}

// Top-level await (ES2022)
// Chỉ dùng trong modules
const data = await fetch('/api/data').then(r => r.json());
console.log(data);
```

#### 12. Closures và Scope

**Kiến thức:**

- Lexical scoping
- Closure là function có access đến outer scope
- Module pattern
- IIFE (Immediately Invoked Function Expression)

**Ví dụ code:**

```javascript
// Basic closure
function outerFunction(x) {
    // Outer function's variable
    const outerVariable = x;
  
    // Inner function (closure)
    function innerFunction(y) {
        console.log(outerVariable + y); // Access outer variable
    }
  
    return innerFunction;
}

const addFive = outerFunction(5);
addFive(10); // 15

// Closure với private variables
function createCounter() {
    let count = 0; // Private variable
  
    return {
        increment: () => ++count,
        decrement: () => --count,
        getCount: () => count
    };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.getCount()); // 2
// console.log(counter.count); // undefined - private

// Module pattern
const UserModule = (function() {
    // Private variables
    let users = [];
  
    // Private functions
    function validateUser(user) {
        return user.name && user.email;
    }
  
    // Public API
    return {
        addUser(user) {
            if (validateUser(user)) {
                users.push(user);
                return true;
            }
            return false;
        },
      
        getUsers() {
            return [...users]; // Return copy
        },
      
        getUserCount() {
            return users.length;
        }
    };
})();

UserModule.addUser({ name: 'John', email: 'john@example.com' });
console.log(UserModule.getUsers());

// Closure trong loops - common mistake
// ❌ Wrong
for (var i = 0; i < 3; i++) {
    setTimeout(() => {
        console.log(i); // Prints 3, 3, 3
    }, 1000);
}

// ✅ Fix 1: Use let
for (let i = 0; i < 3; i++) {
    setTimeout(() => {
        console.log(i); // Prints 0, 1, 2
    }, 1000);
}

// ✅ Fix 2: IIFE
for (var i = 0; i < 3; i++) {
    (function(j) {
        setTimeout(() => {
            console.log(j); // Prints 0, 1, 2
        }, 1000);
    })(i);
}

// Closure với event handlers
function setupButtons() {
    const buttons = document.querySelectorAll('button');
  
    buttons.forEach((button, index) => {
        button.addEventListener('click', () => {
            console.log(`Button ${index} clicked`);
        });
    });
}

// Memoization với closure
function memoize(fn) {
    const cache = {};
  
    return function(...args) {
        const key = JSON.stringify(args);
      
        if (cache[key]) {
            console.log('Cache hit');
            return cache[key];
        }
      
        console.log('Cache miss');
        const result = fn(...args);
        cache[key] = result;
        return result;
    };
}

const expensiveFunction = (n) => {
    // Expensive computation
    return n * n;
};

const memoized = memoize(expensiveFunction);
console.log(memoized(5)); // Cache miss, computes
console.log(memoized(5)); // Cache hit, returns cached
```

**📚 GIẢI THÍCH CHI TIẾT - CLOSURES:**

**Closure là gì?**
Closure cho phép inner function truy cập variables của outer function ngay cả sau khi outer function đã return. Đây là một trong những tính năng mạnh mẽ nhất của JavaScript.

**Cơ chế hoạt động:**

1. Khi function được tạo, nó "nhớ" lexical environment (scope) nơi nó được định nghĩa
2. Inner function giữ reference đến outer function's variables
3. Ngay cả khi outer function đã return, inner function vẫn có thể truy cập variables đó

**Tại sao closure trong loop với var lại sai?**

```javascript
// Vấn đề: var có function scope, không phải block scope
for (var i = 0; i < 3; i++) {
    setTimeout(() => {
        console.log(i); // Tất cả in ra 3
    }, 1000);
}
// Giải thích:
// - var i được hoisted lên function scope
// - Tất cả closures share cùng một biến i
// - Khi setTimeout chạy, loop đã chạy xong, i = 3
// - Tất cả closures thấy i = 3

// Fix với let:
// - let có block scope
// - Mỗi iteration tạo scope mới
// - Mỗi closure có i riêng
```

**Memory Leak với Closures:**

```javascript
// ⚠️ Cẩn thận: Closure giữ reference, không phải value
function createHandlers() {
    const largeData = new Array(1000000).fill('data');
  
    return function() {
        // Closure giữ reference đến largeData
        // largeData không bao giờ được garbage collected!
        console.log('Handler called');
    };
}

// ✅ Fix: Chỉ giữ data cần thiết
function createHandlers() {
    const largeData = new Array(1000000).fill('data');
    const neededData = largeData[0]; // Chỉ lấy cần thiết
  
    return function() {
        console.log(neededData); // Closure chỉ giữ neededData
    };
}
```

**Use Cases thực tế:**

- **Data Privacy**: Tạo private variables (JS không có private keyword)
- **Function Factories**: Tạo functions với behavior khác nhau
- **Event Handlers**: Giữ context khi xử lý events
- **Memoization**: Cache kết quả tính toán
- **Currying**: Partial application của functions

#### 13. this Binding

**Kiến thức:**

- this trong different contexts
- call, apply, bind
- Arrow functions và this
- this trong classes

**Ví dụ code:**

```javascript
// this trong global context
console.log(this); // Window (browser) hoặc global (Node.js)

// this trong object method
const person = {
    name: 'John',
    greet: function() {
        return `Hello, I'm ${this.name}`;
    }
};

console.log(person.greet()); // "Hello, I'm John"

// this lost trong callback
const person2 = {
    name: 'John',
    hobbies: ['reading', 'coding'],
    showHobbies: function() {
        // ❌ this is lost
        this.hobbies.forEach(function(hobby) {
            console.log(`${this.name} likes ${hobby}`); // this is undefined
        });
      
        // ✅ Fix 1: Arrow function
        this.hobbies.forEach(hobby => {
            console.log(`${this.name} likes ${hobby}`); // this refers to person2
        });
      
        // ✅ Fix 2: bind
        this.hobbies.forEach(function(hobby) {
            console.log(`${this.name} likes ${hobby}`);
        }.bind(this));
      
        // ✅ Fix 3: Store this
        const self = this;
        this.hobbies.forEach(function(hobby) {
            console.log(`${self.name} likes ${hobby}`);
        });
    }
};

// call, apply, bind
function greet(greeting, punctuation) {
    return `${greeting}, ${this.name}${punctuation}`;
}

const person3 = { name: 'John' };
const person4 = { name: 'Jane' };

// call - gọi function với this và arguments riêng lẻ
console.log(greet.call(person3, 'Hello', '!')); // "Hello, John!"

// apply - gọi function với this và arguments array
console.log(greet.apply(person4, ['Hi', '?'])); // "Hi, Jane?"

// bind - tạo function mới với this cố định
const greetJohn = greet.bind(person3);
console.log(greetJohn('Hey', '!')); // "Hey, John!"

// bind với partial application
const greetWithHello = greet.bind(person3, 'Hello');
console.log(greetWithHello('!')); // "Hello, John!"

// this trong classes
class Counter {
    constructor() {
        this.count = 0;
    }
  
    increment() {
        this.count++;
        return this; // Return this for chaining
    }
  
    decrement() {
        this.count--;
        return this;
    }
  
    getValue() {
        return this.count;
    }
}

const counter = new Counter();
counter.increment().increment().decrement();
console.log(counter.getValue()); // 1
```

**📚 GIẢI THÍCH CHI TIẾT - THIS BINDING:**

**this được xác định như thế nào?**
`this` trong JavaScript được xác định bởi cách function được gọi (call site), không phải nơi nó được định nghĩa. Đây là điểm khác biệt quan trọng so với các ngôn ngữ khác.

**4 Quy tắc xác định this (theo thứ tự ưu tiên):**

**1. New Binding (Ưu tiên cao nhất):**

```javascript
function Person(name) {
    // Khi dùng 'new', this = {} (object mới)
    this.name = name;
    // return this (implicit)
}

const john = new Person('John');
// this trong Person = john object
```

**2. Explicit Binding (call/apply/bind):**

```javascript
function greet() {
    return this.name;
}

const obj = { name: 'John' };
greet.call(obj);  // this = obj
greet.apply(obj); // this = obj
const bound = greet.bind(obj);
bound();          // this = obj (luôn luôn)
```

**3. Implicit Binding (object method):**

```javascript
const obj = {
    name: 'John',
    greet() {
        // this = obj (object gọi method)
        return this.name;
    }
};
obj.greet(); // this = obj
```

**4. Default Binding (thấp nhất):**

```javascript
function greet() {
    // this = global object (window/global)
    return this.name;
}
greet(); // this = window (browser) hoặc global (Node.js)
```

**Arrow Functions và this:**

- Arrow functions KHÔNG có `this` riêng
- `this` trong arrow function = `this` của scope bên ngoài (lexical this)
- Arrow functions không thể bind `this` (call/apply/bind không work)
- Arrow functions không thể dùng làm constructor

**Ví dụ minh họa:**

```javascript
const obj = {
    name: 'John',
  
    // Regular function
    regular: function() {
        console.log(this.name); // "John"
      
        setTimeout(function() {
            // this = global (vì setTimeout gọi function)
            console.log(this.name); // undefined
        }, 100);
    },
  
    // Arrow function
    arrow: function() {
        console.log(this.name); // "John"
      
        setTimeout(() => {
            // this = obj (lexical this từ arrow function)
            console.log(this.name); // "John"
        }, 100);
    }
};
```

**Lưu ý quan trọng:**

- `this` không phải là variable, không thể assign
- `this` chỉ có giá trị khi function được gọi
- Arrow functions "lock" `this` tại thời điểm định nghĩa
- Strict mode: `this` = undefined nếu không có binding

#### 14. Array Methods - Nâng cao

**Kiến thức:**

- map, filter, reduce
- find, findIndex, some, every
- forEach, for...of
- flat, flatMap
- sort, reverse

**Ví dụ code:**

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const users = [
    { id: 1, name: 'John', age: 25, active: true },
    { id: 2, name: 'Jane', age: 30, active: false },
    { id: 3, name: 'Bob', age: 20, active: true }
];

// map - transform array
const doubled = numbers.map(n => n * 2);
const userNames = users.map(user => user.name);

// filter - select elements
const evens = numbers.filter(n => n % 2 === 0);
const activeUsers = users.filter(user => user.active);

// reduce - accumulate values
const sum = numbers.reduce((acc, n) => acc + n, 0);
const userAges = users.reduce((acc, user) => acc + user.age, 0);
const averageAge = userAges / users.length;

// Complex reduce
const groupedByActive = users.reduce((acc, user) => {
    const key = user.active ? 'active' : 'inactive';
    if (!acc[key]) acc[key] = [];
    acc[key].push(user);
    return acc;
}, {});

// find - find first match
const user = users.find(u => u.id === 2);
const firstEven = numbers.find(n => n % 2 === 0);

// findIndex
const index = users.findIndex(u => u.age > 25);

// some - check if any element matches
const hasActive = users.some(u => u.active);
const hasNegative = numbers.some(n => n < 0);

// every - check if all elements match
const allActive = users.every(u => u.active);
const allPositive = numbers.every(n => n > 0);

// forEach - iterate (không return value)
users.forEach(user => {
    console.log(`${user.name} is ${user.age} years old`);
});

// for...of - modern iteration
for (const user of users) {
    console.log(user.name);
}

// flat - flatten nested arrays
const nested = [1, [2, 3], [4, [5, 6]]];
const flat = nested.flat(); // [1, 2, 3, 4, [5, 6]]
const flatDeep = nested.flat(2); // [1, 2, 3, 4, 5, 6]

// flatMap - map then flat
const words = ['hello world', 'foo bar'];
const letters = words.flatMap(word => word.split(' '));
// ['hello', 'world', 'foo', 'bar']

// sort
const sorted = numbers.sort((a, b) => a - b);
const sortedUsers = users.sort((a, b) => a.age - b.age);

// Chaining methods
const result = users
    .filter(u => u.active)
    .map(u => u.name)
    .sort();
```

#### 15. ES6 Modules

**Kiến thức:**

- export, import
- Default exports
- Named exports
- Dynamic imports

**Ví dụ code:**

```javascript
// math.js - Named exports
export function add(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}

export const PI = 3.14159;

// Import named exports
import { add, subtract, PI } from './math.js';
import { add as sum } from './math.js'; // Rename
import * as math from './math.js'; // Import all

// user.js - Default export
export default class User {
    constructor(name) {
        this.name = name;
    }
}

// Import default
import User from './user.js';
import UserClass from './user.js'; // Can rename default

// Mixed exports
export default function greet(name) {
    return `Hello, ${name}!`;
}

export function farewell(name) {
    return `Goodbye, ${name}!`;
}

// Import both
import greet, { farewell } from './greetings.js';

// Dynamic import
async function loadModule() {
    const module = await import('./math.js');
    console.log(module.add(2, 3));
}

// Re-export
export { add, subtract } from './math.js';
export { default } from './user.js';
```

#### 16. Error Handling Patterns

**Kiến thức:**

- try/catch/finally
- Error objects
- Custom errors
- Error propagation
- Async error handling

**Ví dụ code:**

```javascript
// Basic try/catch
try {
    const result = riskyOperation();
    console.log(result);
} catch (error) {
    console.error('Error:', error.message);
} finally {
    console.log('Always executed');
}

// Custom Error classes
class ValidationError extends Error {
    constructor(message, field) {
        super(message);
        this.name = 'ValidationError';
        this.field = field;
    }
}

class NotFoundError extends Error {
    constructor(resource) {
        super(`${resource} not found`);
        this.name = 'NotFoundError';
        this.resource = resource;
    }
}

// Usage
function validateUser(user) {
    if (!user.name) {
        throw new ValidationError('Name is required', 'name');
    }
    if (!user.email) {
        throw new ValidationError('Email is required', 'email');
    }
}

try {
    validateUser({});
} catch (error) {
    if (error instanceof ValidationError) {
        console.error(`Validation error in ${error.field}: ${error.message}`);
    } else {
        console.error('Unknown error:', error);
    }
}

// Error handling trong async
async function fetchUserWithRetry(userId, retries = 3) {
    for (let i = 0; i < retries; i++) {
        try {
            const response = await fetch(`/api/users/${userId}`);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            if (i === retries - 1) throw error;
            await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
        }
    }
}

// Error propagation
async function processUser(userId) {
    try {
        const user = await fetchUser(userId);
        const profile = await fetchProfile(user.id);
        return { user, profile };
    } catch (error) {
        // Log và re-throw
        console.error('Error processing user:', error);
        throw error; // Propagate to caller
    }
}

// Error handling wrapper
function asyncHandler(fn) {
    return (req, res, next) => {
        Promise.resolve(fn(req, res, next)).catch(next);
    };
}

// Usage trong Express
app.get('/api/users/:id', asyncHandler(async (req, res) => {
    const user = await User.findById(req.params.id);
    if (!user) {
        throw new NotFoundError('User');
    }
    res.json(user);
}));
```

#### 17. Functional Programming Concepts

**Kiến thức:**

- Pure functions
- Higher-order functions
- Function composition
- Currying
- Immutability

**Ví dụ code:**

```javascript
// Pure functions - no side effects
// ✅ Pure
function add(a, b) {
    return a + b;
}

// ❌ Impure
let counter = 0;
function increment() {
    counter++; // Side effect
    return counter;
}

// Higher-order functions
function createMultiplier(multiplier) {
    return function(number) {
        return number * multiplier;
    };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

// Function composition
const compose = (...fns) => (x) => fns.reduceRight((acc, fn) => fn(acc), x);
const pipe = (...fns) => (x) => fns.reduce((acc, fn) => fn(acc), x);

const addOne = x => x + 1;
const multiplyByTwo = x => x * 2;
const square = x => x * x;

const composed = compose(square, multiplyByTwo, addOne);
console.log(composed(3)); // ((3 + 1) * 2)² = 64

const piped = pipe(addOne, multiplyByTwo, square);
console.log(piped(3)); // ((3 + 1) * 2)² = 64

// Currying
function curry(fn) {
    return function curried(...args) {
        if (args.length >= fn.length) {
            return fn(...args);
        }
        return (...nextArgs) => curried(...args, ...nextArgs);
    };
}

const addCurried = curry((a, b, c) => a + b + c);
console.log(addCurried(1)(2)(3)); // 6
console.log(addCurried(1, 2)(3)); // 6
console.log(addCurried(1)(2, 3)); // 6

// Immutability
// ❌ Mutating
const user = { name: 'John', age: 25 };
user.age = 26; // Mutation

// ✅ Immutable
const updatedUser = { ...user, age: 26 };
const users = [user1, user2, user3];
const newUsers = [...users, newUser]; // Add without mutation
const updatedUsers = users.map(u => 
    u.id === id ? { ...u, age: 26 } : u
); // Update without mutation
```

#### 18. DOM Manipulation - Nâng cao

**Kiến thức:**

- Query selectors
- Element manipulation
- Event delegation
- Event object
- Creating và manipulating DOM

**Ví dụ code:**

```javascript
// Query selectors
const element = document.querySelector('#myId');
const elements = document.querySelectorAll('.myClass');
const firstDiv = document.querySelector('div');
const allDivs = document.querySelectorAll('div');

// Element manipulation
element.textContent = "New text"; // Safe, no HTML
element.innerHTML = "<strong>Bold</strong>"; // Can inject HTML
element.setAttribute('data-id', '123');
element.getAttribute('data-id');
element.removeAttribute('data-id');

// classList methods
element.classList.add('active', 'highlight');
element.classList.remove('active');
element.classList.toggle('active');
element.classList.contains('active'); // true/false
element.classList.replace('old', 'new');

// Style manipulation
element.style.color = 'red';
element.style.backgroundColor = 'blue';
element.style.cssText = 'color: red; background: blue;';

// Creating elements
const div = document.createElement('div');
div.textContent = 'Hello';
div.className = 'container';
div.setAttribute('data-id', '1');

// Append methods
parent.appendChild(div);
parent.insertBefore(newDiv, existingDiv);
parent.replaceChild(newDiv, oldDiv);
parent.removeChild(div);
div.remove(); // Modern way

// Event listeners
element.addEventListener('click', handleClick);
element.addEventListener('click', handleClick, { once: true });
element.removeEventListener('click', handleClick);

// Event object
element.addEventListener('click', (event) => {
    console.log(event.target); // Element that triggered
    console.log(event.currentTarget); // Element with listener
    console.log(event.type); // 'click'
    event.preventDefault(); // Prevent default behavior
    event.stopPropagation(); // Stop bubbling
});

// Event delegation
document.addEventListener('click', (e) => {
    if (e.target.matches('.button')) {
        console.log('Button clicked:', e.target);
    }
});

// Form handling
const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    console.log(data);
});

// Fetch API với DOM
async function loadUsers() {
    try {
        const response = await fetch('/api/users');
        const users = await response.json();
      
        const container = document.querySelector('#users');
        container.innerHTML = users.map(user => `
            <div class="user">
                <h3>${user.name}</h3>
                <p>${user.email}</p>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error loading users:', error);
    }
}
```

#### 19. Browser APIs

**Kiến thức:**

- LocalStorage, SessionStorage
- Fetch API
- WebSocket
- Geolocation
- Intersection Observer

**Ví dụ code:**

```javascript
// LocalStorage
localStorage.setItem('key', 'value');
const value = localStorage.getItem('key');
localStorage.removeItem('key');
localStorage.clear();

// Store objects
const user = { name: 'John', age: 25 };
localStorage.setItem('user', JSON.stringify(user));
const stored = JSON.parse(localStorage.getItem('user'));

// SessionStorage (same API, but cleared on tab close)
sessionStorage.setItem('key', 'value');

// Fetch API
async function fetchData() {
    try {
        const response = await fetch('/api/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer token'
            },
            body: JSON.stringify({ key: 'value' })
        });
      
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
      
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Fetch error:', error);
    }
}

// WebSocket
const ws = new WebSocket('ws://localhost:8080');

ws.onopen = () => {
    console.log('Connected');
    ws.send(JSON.stringify({ type: 'message', data: 'Hello' }));
};

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Received:', data);
};

ws.onerror = (error) => {
    console.error('WebSocket error:', error);
};

ws.onclose = () => {
    console.log('Disconnected');
};

// Geolocation
navigator.geolocation.getCurrentPosition(
    (position) => {
        console.log('Latitude:', position.coords.latitude);
        console.log('Longitude:', position.coords.longitude);
    },
    (error) => {
        console.error('Geolocation error:', error);
    },
    { enableHighAccuracy: true, timeout: 5000 }
);

// Intersection Observer
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        } else {
            entry.target.classList.remove('visible');
        }
    });
}, {
    threshold: 0.5
});

document.querySelectorAll('.observe').forEach(el => {
    observer.observe(el);
});
```

#### 20. Node.js Specific JavaScript

**Kiến thức:**

- CommonJS modules
- File system operations
- Streams
- Events
- Buffer

**Ví dụ code:**

```javascript
// CommonJS modules
// math.js
function add(a, b) {
    return a + b;
}

module.exports = { add };
// hoặc
exports.add = add;

// main.js
const { add } = require('./math');
const math = require('./math');

// File system
const fs = require('fs').promises;

// Read file
async function readFile() {
    try {
        const data = await fs.readFile('file.txt', 'utf8');
        console.log(data);
    } catch (error) {
        console.error('Error reading file:', error);
    }
}

// Write file
async function writeFile() {
    await fs.writeFile('output.txt', 'Hello World', 'utf8');
}

// Streams
const fs2 = require('fs');
const readStream = fs2.createReadStream('large-file.txt');
const writeStream = fs2.createWriteStream('output.txt');

readStream.pipe(writeStream);

readStream.on('data', (chunk) => {
    console.log('Received chunk:', chunk.length);
});

readStream.on('end', () => {
    console.log('Finished reading');
});

// Events
const EventEmitter = require('events');

class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();

myEmitter.on('event', (data) => {
    console.log('Event received:', data);
});

myEmitter.emit('event', { message: 'Hello' });

// Buffer
const buf = Buffer.from('Hello World', 'utf8');
console.log(buf.toString('hex'));
console.log(buf.toString('base64'));
```

### 6.4. React Basics

#### Components

**Kiến thức:**

- Functional components
- JSX syntax
- Props: Truyền dữ liệu từ parent xuống child
- Component composition

**Ví dụ:**

```jsx
// Functional component
function Welcome({ name }) {
    return <h1>Hello, {name}!</h1>;
}

// Component với children
function Card({ title, children }) {
    return (
        <div className="card">
            <h2>{title}</h2>
            {children}
        </div>
    );
}

// Usage
<Welcome name="John" />
<Card title="My Card">
    <p>Content here</p>
</Card>
```

#### State với useState

**Kiến thức:**

- useState hook
- State updates
- Functional updates

**Ví dụ:**

```jsx
import { useState } from 'react';

function Counter() {
    const [count, setCount] = useState(0);
  
    const increment = () => {
        setCount(count + 1);
    };
  
    const incrementBy = (amount) => {
        setCount(prev => prev + amount);
    };
  
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={increment}>+1</button>
            <button onClick={() => incrementBy(5)}>+5</button>
        </div>
    );
}
```

#### useEffect

**Kiến thức:**

- Side effects: API calls, subscriptions, DOM manipulation
- Dependency array
- Cleanup function

**Ví dụ:**

```jsx
import { useState, useEffect } from 'react';

function UserProfile({ userId }) {
    const [user, setUser] = useState(null);
  
    useEffect(() => {
        // Fetch data
        fetch(`/api/users/${userId}`)
            .then(res => res.json())
            .then(data => setUser(data));
      
        // Cleanup (optional)
        return () => {
            // Cleanup code
        };
    }, [userId]); // Dependency array
  
    if (!user) return <div>Loading...</div>;
  
    return <div>{user.name}</div>;
}
```

#### React Router

**Kiến thức:**

- BrowserRouter, Routes, Route
- Link, NavLink
- useNavigate, useParams
- Nested routes

**Ví dụ:**

```jsx
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

function App() {
    return (
        <BrowserRouter>
            <nav>
                <Link to="/">Home</Link>
                <Link to="/about">About</Link>
            </nav>
          
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/users/:id" element={<UserProfile />} />
            </Routes>
        </BrowserRouter>
    );
}

function UserProfile() {
    const { id } = useParams();
    return <div>User ID: {id}</div>;
}
```

### 6.5. Projects

#### Project: Todo App với React

**Yêu cầu:**

- Thêm, xóa, sửa todos
- Đánh dấu hoàn thành
- Lọc todos (all, active, completed)
- Lưu vào localStorage

#### Project: Blog Frontend với React Router

**Yêu cầu:**

- Trang danh sách bài viết
- Trang chi tiết bài viết
- Trang tạo/sửa bài viết
- Navigation

---

## THÁNG 5: Backend Foundation

### 7.1. Node.js Basics

**Kiến thức:**

- Node.js runtime
- NPM: Package management
- Modules: require, module.exports, ES6 imports
- File system: fs module
- HTTP: http module

**Ví dụ:**

```javascript
// Basic server
const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello World');
});

server.listen(3000, () => {
    console.log('Server running on port 3000');
});

// File system
const fs = require('fs');

fs.readFile('file.txt', 'utf8', (err, data) => {
    if (err) throw err;
    console.log(data);
});
```

### 7.2. Express Framework

**Kiến thức:**

- Express setup
- Routes: GET, POST, PUT, DELETE
- Middleware: app.use()
- Request/Response objects
- Error handling

**Ví dụ:**

```javascript
const express = require('express');
const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', (req, res) => {
    res.json({ message: 'Hello World' });
});

app.get('/users/:id', (req, res) => {
    const { id } = req.params;
    res.json({ userId: id });
});

app.post('/users', (req, res) => {
    const { name, email } = req.body;
    // Create user
    res.status(201).json({ message: 'User created' });
});

// Error handling
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
```

### 7.3. RESTful API Design

**Kiến thức:**

- REST principles
- HTTP methods: GET, POST, PUT, PATCH, DELETE
- Status codes: 200, 201, 400, 404, 500
- Resource naming
- API versioning

**Ví dụ:**

```javascript
// RESTful routes
// GET    /api/users        - Get all users
// GET    /api/users/:id    - Get user by id
// POST   /api/users        - Create user
// PUT    /api/users/:id    - Update user
// PATCH  /api/users/:id    - Partial update
// DELETE /api/users/:id    - Delete user

app.get('/api/users', async (req, res) => {
    try {
        const users = await User.find();
        res.json(users);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/api/users', async (req, res) => {
    try {
        const user = await User.create(req.body);
        res.status(201).json(user);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});
```

### 7.4. Database Integration

#### MongoDB với Mongoose

**Kiến thức:**

- Mongoose ODM
- Schema definition
- Models
- CRUD operations
- Relationships

**Ví dụ:**

```javascript
const mongoose = require('mongoose');

// Connect
mongoose.connect('mongodb://localhost:27017/myapp');

// Schema
const userSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    age: { type: Number, min: 0 }
}, { timestamps: true });

// Model
const User = mongoose.model('User', userSchema);

// CRUD
// Create
const user = await User.create({ name: 'John', email: 'john@example.com' });

// Read
const users = await User.find();
const user = await User.findById(id);

// Update
await User.findByIdAndUpdate(id, { name: 'Jane' });

// Delete
await User.findByIdAndDelete(id);
```

#### PostgreSQL với Sequelize

**Kiến thức:**

- Sequelize ORM
- Models
- Migrations
- Associations

**Ví dụ:**

```javascript
const { Sequelize, DataTypes } = require('sequelize');

const sequelize = new Sequelize('database', 'username', 'password', {
    host: 'localhost',
    dialect: 'postgres'
});

// Model
const User = sequelize.define('User', {
    name: {
        type: DataTypes.STRING,
        allowNull: false
    },
    email: {
        type: DataTypes.STRING,
        unique: true
    }
});

// CRUD
await User.create({ name: 'John', email: 'john@example.com' });
const users = await User.findAll();
await User.update({ name: 'Jane' }, { where: { id: 1 } });
await User.destroy({ where: { id: 1 } });
```

### 7.5. Authentication với JWT

**Kiến thức:**

- JWT (JSON Web Tokens)
- Password hashing: bcrypt
- Token generation và verification
- Middleware để protect routes

**Ví dụ:**

```javascript
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

// Register
app.post('/api/register', async (req, res) => {
    const { email, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const user = await User.create({ email, password: hashedPassword });
    res.status(201).json({ message: 'User created' });
});

// Login
app.post('/api/login', async (req, res) => {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
  
    if (!user || !await bcrypt.compare(password, user.password)) {
        return res.status(401).json({ error: 'Invalid credentials' });
    }
  
    const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET, {
        expiresIn: '24h'
    });
  
    res.json({ token });
});

// Middleware
const authenticateToken = (req, res, next) => {
    const token = req.headers['authorization']?.split(' ')[1];
  
    if (!token) {
        return res.status(401).json({ error: 'No token provided' });
    }
  
    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
        if (err) return res.status(403).json({ error: 'Invalid token' });
        req.user = user;
        next();
    });
};

// Protected route
app.get('/api/profile', authenticateToken, async (req, res) => {
    const user = await User.findById(req.user.userId);
    res.json(user);
});
```

### 7.6. Project: REST API cho Blog

**Yêu cầu:**

- CRUD cho posts
- User authentication
- Comments system
- Pagination
- Error handling

---

## THÁNG 6: Full Stack Integration

### 8.1. Connect Frontend + Backend

**Kiến thức:**

- API integration với fetch/axios
- CORS configuration
- Error handling
- Loading states

**Ví dụ:**

```javascript
// Frontend - API service
const API_URL = 'http://localhost:3000/api';

export const api = {
    async get(endpoint) {
        const response = await fetch(`${API_URL}${endpoint}`);
        if (!response.ok) throw new Error('Failed to fetch');
        return response.json();
    },
  
    async post(endpoint, data) {
        const response = await fetch(`${API_URL}${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        if (!response.ok) throw new Error('Failed to create');
        return response.json();
    }
};

// React component
function PostsList() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
  
    useEffect(() => {
        api.get('/posts')
            .then(data => {
                setPosts(data);
                setLoading(false);
            })
            .catch(err => {
                setError(err.message);
                setLoading(false);
            });
    }, []);
  
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
  
    return (
        <div>
            {posts.map(post => (
                <div key={post.id}>{post.title}</div>
            ))}
        </div>
    );
}
```

### 8.2. State Management

#### Context API

**Kiến thức:**

- createContext
- useContext
- Provider pattern

**Ví dụ:**

```jsx
// Context
const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
  
    const login = async (email, password) => {
        const response = await api.post('/login', { email, password });
        setUser(response.user);
        localStorage.setItem('token', response.token);
    };
  
    const logout = () => {
        setUser(null);
        localStorage.removeItem('token');
    };
  
    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

export const useAuth = () => useContext(AuthContext);

// Usage
function App() {
    return (
        <AuthProvider>
            <Routes />
        </AuthProvider>
    );
}

function Profile() {
    const { user, logout } = useAuth();
    return (
        <div>
            <p>{user.name}</p>
            <button onClick={logout}>Logout</button>
        </div>
    );
}
```

#### Redux (Optional)

**Kiến thức:**

- Store: Nơi lưu trữ global state
- Actions: Objects mô tả điều gì đã xảy ra
- Reducers: Pure functions xác định state thay đổi như thế nào
- useSelector, useDispatch: Hooks để connect với Redux store
- Redux Toolkit: Công cụ giúp viết Redux code dễ dàng hơn

**Ví dụ Redux cơ bản:**

```jsx
// actions.js
export const increment = () => ({
    type: 'INCREMENT'
});

export const decrement = () => ({
    type: 'DECREMENT'
});

export const addTodo = (text) => ({
    type: 'ADD_TODO',
    payload: text
});

// reducers.js
const counterReducer = (state = 0, action) => {
    switch (action.type) {
        case 'INCREMENT':
            return state + 1;
        case 'DECREMENT':
            return state - 1;
        default:
            return state;
    }
};

const todosReducer = (state = [], action) => {
    switch (action.type) {
        case 'ADD_TODO':
            return [...state, { id: Date.now(), text: action.payload }];
        default:
            return state;
    }
};

// store.js
import { createStore, combineReducers } from 'redux';

const rootReducer = combineReducers({
    counter: counterReducer,
    todos: todosReducer
});

export const store = createStore(rootReducer);

// Component
import { useSelector, useDispatch } from 'react-redux';
import { increment, decrement } from './actions';

function Counter() {
    const count = useSelector(state => state.counter);
    const dispatch = useDispatch();
  
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => dispatch(increment())}>+</button>
            <button onClick={() => dispatch(decrement())}>-</button>
        </div>
    );
}
```

**Redux Toolkit (Modern approach):**

```jsx
// store.js
import { configureStore, createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
    name: 'counter',
    initialState: 0,
    reducers: {
        increment: (state) => state + 1,
        decrement: (state) => state - 1,
        incrementByAmount: (state, action) => state + action.payload
    }
});

export const { increment, decrement, incrementByAmount } = counterSlice.actions;

const todosSlice = createSlice({
    name: 'todos',
    initialState: [],
    reducers: {
        addTodo: (state, action) => {
            state.push({ id: Date.now(), text: action.payload });
        },
        removeTodo: (state, action) => {
            return state.filter(todo => todo.id !== action.payload);
        }
    }
});

export const { addTodo, removeTodo } = todosSlice.actions;

export const store = configureStore({
    reducer: {
        counter: counterSlice.reducer,
        todos: todosSlice.reducer
    }
});

// Component với Redux Toolkit
import { useSelector, useDispatch } from 'react-redux';
import { increment, decrement } from './store';

function Counter() {
    const count = useSelector(state => state.counter);
    const dispatch = useDispatch();
  
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => dispatch(increment())}>+</button>
            <button onClick={() => dispatch(decrement())}>-</button>
        </div>
    );
}
```

**Async Actions với Redux Thunk:**

```jsx
// thunk actions
import { createAsyncThunk } from '@reduxjs/toolkit';

export const fetchUser = createAsyncThunk(
    'user/fetchUser',
    async (userId) => {
        const response = await fetch(`/api/users/${userId}`);
        return response.json();
    }
);

// reducer với thunk
const userSlice = createSlice({
    name: 'user',
    initialState: { data: null, loading: false, error: null },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchUser.pending, (state) => {
                state.loading = true;
            })
            .addCase(fetchUser.fulfilled, (state, action) => {
                state.loading = false;
                state.data = action.payload;
            })
            .addCase(fetchUser.rejected, (state, action) => {
                state.loading = false;
                state.error = action.error.message;
            });
    }
});
```

### 8.3. Project: Full Stack E-commerce (MVP)

**Yêu cầu:**

- User authentication
- Product catalog
- Shopping cart
- Checkout process
- Order management

**Database Schema:**

```sql
-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INTEGER DEFAULT 0,
    image_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cart table
CREATE TABLE cart_items (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders table
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    total DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Order items table
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
```

**Backend API Structure:**

```javascript
// routes/auth.js
router.post('/register', async (req, res) => {
    const { email, password, name } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const user = await User.create({ email, password: hashedPassword, name });
    const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET);
    res.json({ token, user });
});

router.post('/login', async (req, res) => {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user || !await bcrypt.compare(password, user.password)) {
        return res.status(401).json({ error: 'Invalid credentials' });
    }
    const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET);
    res.json({ token, user });
});

// routes/products.js
router.get('/', async (req, res) => {
    const products = await Product.find();
    res.json(products);
});

router.get('/:id', async (req, res) => {
    const product = await Product.findById(req.params.id);
    res.json(product);
});

// routes/cart.js
router.get('/', authenticateToken, async (req, res) => {
    const cartItems = await CartItem.find({ user_id: req.user.userId })
        .populate('product_id');
    res.json(cartItems);
});

router.post('/', authenticateToken, async (req, res) => {
    const { product_id, quantity } = req.body;
    const cartItem = await CartItem.create({
        user_id: req.user.userId,
        product_id,
        quantity
    });
    res.json(cartItem);
});

// routes/orders.js
router.post('/', authenticateToken, async (req, res) => {
    const cartItems = await CartItem.find({ user_id: req.user.userId })
        .populate('product_id');
  
    const total = cartItems.reduce((sum, item) => {
        return sum + (item.product_id.price * item.quantity);
    }, 0);
  
    const order = await Order.create({
        user_id: req.user.userId,
        total
    });
  
    for (const item of cartItems) {
        await OrderItem.create({
            order_id: order.id,
            product_id: item.product_id.id,
            quantity: item.quantity,
            price: item.product_id.price
        });
    }
  
    await CartItem.deleteMany({ user_id: req.user.userId });
  
    res.json(order);
});
```

**Frontend Components:**

```jsx
// ProductList.jsx
function ProductList() {
    const [products, setProducts] = useState([]);
  
    useEffect(() => {
        api.get('/products').then(setProducts);
    }, []);
  
    return (
        <div className="product-grid">
            {products.map(product => (
                <ProductCard key={product.id} product={product} />
            ))}
        </div>
    );
}

// ShoppingCart.jsx
function ShoppingCart() {
    const { user } = useAuth();
    const [cartItems, setCartItems] = useState([]);
  
    useEffect(() => {
        if (user) {
            api.get('/cart').then(setCartItems);
        }
    }, [user]);
  
    const removeItem = async (itemId) => {
        await api.delete(`/cart/${itemId}`);
        setCartItems(items => items.filter(item => item.id !== itemId));
    };
  
    const checkout = async () => {
        const order = await api.post('/orders');
        navigate(`/orders/${order.id}`);
    };
  
    const total = cartItems.reduce((sum, item) => {
        return sum + (item.product_id.price * item.quantity);
    }, 0);
  
    return (
        <div>
            <h2>Shopping Cart</h2>
            {cartItems.map(item => (
                <CartItem 
                    key={item.id} 
                    item={item} 
                    onRemove={() => removeItem(item.id)}
                />
            ))}
            <div>Total: ${total.toFixed(2)}</div>
            <button onClick={checkout}>Checkout</button>
        </div>
    );
}
```

---

## THÁNG 7: Advanced Frontend

### 9.1. React Advanced

#### Custom Hooks

**Kiến thức:**

- Tạo custom hooks để tái sử dụng logic
- Naming convention: Bắt đầu với "use"
- Có thể sử dụng các hooks khác bên trong

**Ví dụ:**

```jsx
// Custom hook: useFetch
function useFetch(url) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
  
    useEffect(() => {
        fetch(url)
            .then(res => res.json())
            .then(data => {
                setData(data);
                setLoading(false);
            })
            .catch(err => {
                setError(err);
                setLoading(false);
            });
    }, [url]);
  
    return { data, loading, error };
}

// Usage
function UserProfile({ userId }) {
    const { data: user, loading, error } = useFetch(`/api/users/${userId}`);
  
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;
  
    return <div>{user.name}</div>;
}

// Custom hook: useLocalStorage
function useLocalStorage(key, initialValue) {
    const [storedValue, setStoredValue] = useState(() => {
        try {
            const item = window.localStorage.getItem(key);
            return item ? JSON.parse(item) : initialValue;
        } catch (error) {
            return initialValue;
        }
    });
  
    const setValue = (value) => {
        try {
            setStoredValue(value);
            window.localStorage.setItem(key, JSON.stringify(value));
        } catch (error) {
            console.error(error);
        }
    };
  
    return [storedValue, setValue];
}
```

#### useMemo và useCallback

**Kiến thức:**

- useMemo: Memoize giá trị tính toán
- useCallback: Memoize function
- Tránh re-render không cần thiết

**Ví dụ:**

```jsx
function ExpensiveComponent({ items, filter }) {
    // Memoize filtered items
    const filteredItems = useMemo(() => {
        return items.filter(item => item.category === filter);
    }, [items, filter]);
  
    // Memoize callback
    const handleClick = useCallback((id) => {
        console.log('Clicked:', id);
    }, []);
  
    return (
        <div>
            {filteredItems.map(item => (
                <Item key={item.id} item={item} onClick={handleClick} />
            ))}
        </div>
    );
}
```

#### Performance Optimization

**Kiến thức:**

- React.memo: Memoize components
- Code splitting: React.lazy, Suspense
- Virtual scrolling cho lists lớn
- Debounce/Throttle cho events

**Ví dụ:**

```jsx
// React.memo
const MemoizedComponent = React.memo(function Component({ name }) {
    return <div>{name}</div>;
});

// Code splitting
const LazyComponent = React.lazy(() => import('./LazyComponent'));

function App() {
    return (
        <Suspense fallback={<div>Loading...</div>}>
            <LazyComponent />
        </Suspense>
    );
}

// Debounce hook
function useDebounce(value, delay) {
    const [debouncedValue, setDebouncedValue] = useState(value);
  
    useEffect(() => {
        const handler = setTimeout(() => {
            setDebouncedValue(value);
        }, delay);
      
        return () => clearTimeout(handler);
    }, [value, delay]);
  
    return debouncedValue;
}
```

### 9.2. Testing

#### Jest + React Testing Library

**Kiến thức:**

- Unit testing
- Component testing
- Snapshot testing
- Mocking

**Ví dụ:**

```javascript
// Component test
import { render, screen, fireEvent } from '@testing-library/react';
import Counter from './Counter';

test('increments counter on button click', () => {
    render(<Counter />);
    const button = screen.getByText('+1');
    const count = screen.getByText(/count/i);
  
    expect(count).toHaveTextContent('0');
    fireEvent.click(button);
    expect(count).toHaveTextContent('1');
});

// API mock test
test('fetches and displays user data', async () => {
    global.fetch = jest.fn(() =>
        Promise.resolve({
            json: () => Promise.resolve({ name: 'John' })
        })
    );
  
    render(<UserProfile userId={1} />);
    expect(await screen.findByText('John')).toBeInTheDocument();
});
```

#### E2E Testing với Cypress

**Kiến thức:**

- Cypress setup
- Writing E2E tests
- Best practices

**Ví dụ:**

```javascript
describe('Login Flow', () => {
    it('should login successfully', () => {
        cy.visit('/login');
        cy.get('[data-testid="email"]').type('user@example.com');
        cy.get('[data-testid="password"]').type('password123');
        cy.get('[data-testid="submit"]').click();
        cy.url().should('include', '/dashboard');
    });
});
```

### 9.3. Build Tools

#### Webpack/Vite Basics

**Kiến thức:**

- Module bundling
- Loaders và plugins
- Development vs Production builds
- Code splitting

**Ví dụ Vite config:**

```javascript
// vite.config.js
export default {
    build: {
        rollupOptions: {
            output: {
                manualChunks: {
                    vendor: ['react', 'react-dom'],
                    utils: ['./src/utils']
                }
            }
        }
    }
};
```

---

## THÁNG 8: Advanced Backend

### 10.1. Advanced API Features

#### Pagination

**Kiến thức:**

- Offset-based pagination
- Cursor-based pagination
- Page size limits

**Ví dụ:**

```javascript
// Offset-based
app.get('/api/posts', async (req, res) => {
    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 10;
    const skip = (page - 1) * limit;
  
    const posts = await Post.find()
        .skip(skip)
        .limit(limit)
        .sort({ createdAt: -1 });
  
    const total = await Post.countDocuments();
  
    res.json({
        posts,
        pagination: {
            page,
            limit,
            total,
            pages: Math.ceil(total / limit)
        }
    });
});

// Cursor-based
app.get('/api/posts', async (req, res) => {
    const cursor = req.query.cursor;
    const limit = parseInt(req.query.limit) || 10;
  
    const query = cursor ? { _id: { $gt: cursor } } : {};
    const posts = await Post.find(query)
        .limit(limit + 1)
        .sort({ _id: 1 });
  
    const hasMore = posts.length > limit;
    if (hasMore) posts.pop();
  
    res.json({
        posts,
        nextCursor: hasMore ? posts[posts.length - 1]._id : null
    });
});
```

#### Filtering và Sorting

**Ví dụ:**

```javascript
app.get('/api/products', async (req, res) => {
    const { category, minPrice, maxPrice, sortBy, order } = req.query;
  
    let query = {};
    if (category) query.category = category;
    if (minPrice || maxPrice) {
        query.price = {};
        if (minPrice) query.price.$gte = parseFloat(minPrice);
        if (maxPrice) query.price.$lte = parseFloat(maxPrice);
    }
  
    let sortOptions = {};
    if (sortBy) {
        sortOptions[sortBy] = order === 'desc' ? -1 : 1;
    }
  
    const products = await Product.find(query).sort(sortOptions);
    res.json(products);
});
```

#### Search Functionality

**Ví dụ:**

```javascript
// Full-text search với MongoDB
app.get('/api/posts/search', async (req, res) => {
    const { q } = req.query;
  
    const posts = await Post.find({
        $text: { $search: q }
    }, {
        score: { $meta: 'textScore' }
    }).sort({ score: { $meta: 'textScore' } });
  
    res.json(posts);
});

// Regex search
app.get('/api/users/search', async (req, res) => {
    const { name } = req.query;
  
    const users = await User.find({
        name: { $regex: name, $options: 'i' }
    });
  
    res.json(users);
});
```

#### File Upload

**Ví dụ:**

```javascript
const multer = require('multer');
const path = require('path');

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'uploads/');
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + path.extname(file.originalname));
    }
});

const upload = multer({
    storage,
    limits: { fileSize: 5 * 1024 * 1024 }, // 5MB
    fileFilter: (req, file, cb) => {
        const allowedTypes = /jpeg|jpg|png|gif/;
        const extname = allowedTypes.test(path.extname(file.originalname).toLowerCase());
        const mimetype = allowedTypes.test(file.mimetype);
      
        if (extname && mimetype) {
            cb(null, true);
        } else {
            cb(new Error('Only image files are allowed'));
        }
    }
});

app.post('/api/upload', upload.single('image'), (req, res) => {
    res.json({ url: `/uploads/${req.file.filename}` });
});
```

#### Caching với Redis

**Kiến thức:**

- Redis basics
- Cache strategies: Cache-aside, Write-through, Write-back
- TTL (Time To Live)

**Ví dụ:**

```javascript
const redis = require('redis');
const client = redis.createClient();

async function getCachedData(key) {
    const cached = await client.get(key);
    if (cached) {
        return JSON.parse(cached);
    }
    return null;
}

async function setCachedData(key, data, ttl = 3600) {
    await client.setEx(key, ttl, JSON.stringify(data));
}

app.get('/api/posts/:id', async (req, res) => {
    const { id } = req.params;
    const cacheKey = `post:${id}`;
  
    // Try cache first
    let post = await getCachedData(cacheKey);
  
    if (!post) {
        // Cache miss - fetch from database
        post = await Post.findById(id);
        if (post) {
            await setCachedData(cacheKey, post, 3600); // Cache for 1 hour
        }
    }
  
    if (!post) {
        return res.status(404).json({ error: 'Post not found' });
    }
  
    res.json(post);
});
```

### 10.2. Microservices Basics

**Kiến thức:**

- Service separation
- API Gateway
- Service communication
- Message queues

**Ví dụ Architecture:**

```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
┌──────▼──────────┐
│  API Gateway    │
└──┬──────┬───────┘
   │      │
┌──▼──┐ ┌─▼──┐ ┌──────┐
│User │ │Prod│ │Order │
│Svc  │ │Svc │ │Svc   │
└─────┘ └────┘ └──────┘
```

**API Gateway Example:**

```javascript
// API Gateway
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

app.use('/api/users', createProxyMiddleware({
    target: 'http://user-service:3001',
    changeOrigin: true
}));

app.use('/api/products', createProxyMiddleware({
    target: 'http://product-service:3002',
    changeOrigin: true
}));

app.listen(3000);
```

**Message Queue với RabbitMQ:**

```javascript
const amqp = require('amqplib');

// Producer
async function sendMessage(queue, message) {
    const connection = await amqp.connect('amqp://localhost');
    const channel = await connection.createChannel();
  
    await channel.assertQueue(queue, { durable: true });
    channel.sendToQueue(queue, Buffer.from(JSON.stringify(message)), {
        persistent: true
    });
  
    await channel.close();
    await connection.close();
}

// Consumer
async function consumeMessages(queue) {
    const connection = await amqp.connect('amqp://localhost');
    const channel = await connection.createChannel();
  
    await channel.assertQueue(queue, { durable: true });
  
    channel.consume(queue, (msg) => {
        if (msg) {
            const message = JSON.parse(msg.content.toString());
            console.log('Received:', message);
            channel.ack(msg);
        }
    });
}
```

---

## THÁNG 9: DevOps & Deployment

### 11.1. Docker

#### Dockerfile

**Kiến thức:**

- Dockerfile syntax
- Multi-stage builds
- Best practices

**Ví dụ:**

```dockerfile
# Node.js app
FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM node:18-alpine
WORKDIR /app

COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY package*.json ./

EXPOSE 3000
CMD ["node", "dist/index.js"]
```

#### Docker Compose

**Ví dụ:**

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db
      - redis
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

### 11.2. CI/CD

#### GitHub Actions

**Ví dụ:**

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
  
    steps:
    - uses: actions/checkout@v3
  
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
  
    - name: Install dependencies
      run: npm ci
  
    - name: Run tests
      run: npm test
  
    - name: Build
      run: npm run build
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
  
    steps:
    - uses: actions/checkout@v3
  
    - name: Deploy to production
      run: |
        # Deployment commands
        echo "Deploying..."
```

#### Deployment

**Vercel (Frontend):**

```bash
npm i -g vercel
vercel
```

**Heroku (Backend):**

```bash
heroku create myapp
git push heroku main
```

**AWS (Full Stack):**

- EC2 cho servers
- RDS cho database
- S3 cho static files
- CloudFront cho CDN

---

# GIAI ĐOẠN 3: MOBILE DEVELOPMENT (Tháng 10-12)

## THÁNG 10: React Native Foundation

### 12.1. React Native Basics

#### Setup Environment

**Kiến thức:**

- Node.js, npm/yarn
- React Native CLI hoặc Expo
- Android Studio (cho Android)
- Xcode (cho iOS - macOS only)

**Commands:**

```bash
# Expo (Recommended for beginners)
npx create-expo-app MyApp
cd MyApp
npm start

# React Native CLI
npx react-native init MyApp
cd MyApp
npm run android  # hoặc npm run ios
```

#### Components

**Kiến thức:**

- View: Container component
- Text: Hiển thị text
- Button: Button component
- TextInput: Input field
- ScrollView, FlatList: Lists
- Image: Hiển thị images

**Ví dụ:**

```jsx
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

function LoginScreen() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
  
    return (
        <View style={styles.container}>
            <Text style={styles.title}>Login</Text>
            <TextInput
                style={styles.input}
                placeholder="Email"
                value={email}
                onChangeText={setEmail}
                keyboardType="email-address"
            />
            <TextInput
                style={styles.input}
                placeholder="Password"
                value={password}
                onChangeText={setPassword}
                secureTextEntry
            />
            <Button title="Login" onPress={handleLogin} />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 20,
        justifyContent: 'center'
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 20
    },
    input: {
        borderWidth: 1,
        borderColor: '#ccc',
        padding: 10,
        marginBottom: 10,
        borderRadius: 5
    }
});
```

#### Navigation

**Kiến thức:**

- React Navigation
- Stack Navigator
- Tab Navigator
- Drawer Navigator

**Ví dụ:**

```jsx
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Stack = createStackNavigator();
const Tab = createBottomTabNavigator();

function HomeTabs() {
    return (
        <Tab.Navigator>
            <Tab.Screen name="Home" component={HomeScreen} />
            <Tab.Screen name="Profile" component={ProfileScreen} />
        </Tab.Navigator>
    );
}

function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen name="Login" component={LoginScreen} />
                <Stack.Screen name="Main" component={HomeTabs} />
            </Stack.Navigator>
        </NavigationContainer>
    );
}
```

### 12.2. API Integration & State

**Ví dụ:**

```jsx
// API service
const API_URL = 'https://api.example.com';

export const api = {
    async get(endpoint) {
        const response = await fetch(`${API_URL}${endpoint}`);
        return response.json();
    },
  
    async post(endpoint, data) {
        const response = await fetch(`${API_URL}${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return response.json();
    }
};

// AsyncStorage
import AsyncStorage from '@react-native-async-storage/async-storage';

// Save
await AsyncStorage.setItem('token', token);

// Get
const token = await AsyncStorage.getItem('token');

// Remove
await AsyncStorage.removeItem('token');
```

---

## THÁNG 11: Advanced React Native

### 13.1. Native Features

#### Camera

**Ví dụ:**

```jsx
import { launchCamera, launchImageLibrary } from 'react-native-image-picker';

const options = {
    mediaType: 'photo',
    quality: 0.8
};

// Take photo
launchCamera(options, (response) => {
    if (response.assets) {
        const image = response.assets[0];
        console.log(image.uri);
    }
});

// Pick from library
launchImageLibrary(options, (response) => {
    if (response.assets) {
        const image = response.assets[0];
        console.log(image.uri);
    }
});
```

#### Geolocation

**Ví dụ:**

```jsx
import Geolocation from '@react-native-community/geolocation';

Geolocation.getCurrentPosition(
    (position) => {
        const { latitude, longitude } = position.coords;
        console.log(latitude, longitude);
    },
    (error) => console.error(error),
    { enableHighAccuracy: true, timeout: 15000 }
);
```

#### Push Notifications

**Ví dụ:**

```jsx
import messaging from '@react-native-firebase/messaging';

// Request permission
async function requestUserPermission() {
    const authStatus = await messaging().requestPermission();
    return authStatus === messaging.AuthorizationStatus.AUTHORIZED;
}

// Get FCM token
const token = await messaging().getToken();

// Listen for messages
messaging().onMessage(async remoteMessage => {
    console.log('Message:', remoteMessage);
});
```

---

## THÁNG 12: Cross-platform & Deployment

### 14.1. Flutter Basics (Tùy chọn)

#### Dart Basics

**Kiến thức:**

- Dart là ngôn ngữ lập trình của Flutter
- Strongly typed language
- Null safety
- Async/await

**Ví dụ:**

```dart
// Variables
String name = "John";
int age = 25;
bool isStudent = true;

// Null safety
String? nullableString; // Có thể null
String nonNullableString = "Hello"; // Không thể null

// Functions
int add(int a, int b) {
    return a + b;
}

// Arrow function
int multiply(int a, int b) => a * b;

// Async/await
Future<String> fetchData() async {
    final response = await http.get(Uri.parse('https://api.example.com/data'));
    return response.body;
}
```

#### Widgets

**Kiến thức:**

- Flutter sử dụng widgets cho mọi thứ
- StatelessWidget: Widget không có state
- StatefulWidget: Widget có state
- Material và Cupertino widgets

**Ví dụ:**

```dart
// StatelessWidget
class MyApp extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
        return MaterialApp(
            title: 'My App',
            home: HomePage(),
        );
    }
}

// StatefulWidget
class Counter extends StatefulWidget {
    @override
    _CounterState createState() => _CounterState();
}

class _CounterState extends State<Counter> {
    int _count = 0;
  
    void _increment() {
        setState(() {
            _count++;
        });
    }
  
    @override
    Widget build(BuildContext context) {
        return Scaffold(
            appBar: AppBar(title: Text('Counter')),
            body: Center(
                child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                        Text('Count: $_count'),
                        ElevatedButton(
                            onPressed: _increment,
                            child: Text('Increment'),
                        ),
                    ],
                ),
            ),
        );
    }
}
```

#### State Management

**Kiến thức:**

- setState cho local state
- Provider cho global state
- Bloc pattern (advanced)

**Ví dụ với Provider:**

```dart
// Provider setup
class CounterProvider extends ChangeNotifier {
    int _count = 0;
  
    int get count => _count;
  
    void increment() {
        _count++;
        notifyListeners();
    }
}

// Usage
class MyApp extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
        return ChangeNotifierProvider(
            create: (_) => CounterProvider(),
            child: MaterialApp(
                home: CounterPage(),
            ),
        );
    }
}

class CounterPage extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
        final counter = Provider.of<CounterProvider>(context);
      
        return Scaffold(
            body: Center(
                child: Column(
                    children: [
                        Text('Count: ${counter.count}'),
                        ElevatedButton(
                            onPressed: () => counter.increment(),
                            child: Text('Increment'),
                        ),
                    ],
                ),
            ),
        );
    }
}
```

#### Navigation

**Ví dụ:**

```dart
// Navigate to new screen
Navigator.push(
    context,
    MaterialPageRoute(builder: (context) => SecondScreen()),
);

// Navigate back
Navigator.pop(context);

// Named routes
MaterialApp(
    initialRoute: '/',
    routes: {
        '/': (context) => HomeScreen(),
        '/details': (context) => DetailsScreen(),
    },
);

// Navigate with named route
Navigator.pushNamed(context, '/details');
```

### 14.2. App Deployment

#### Build APK/IPA

**Android (APK):**

```bash
cd android
./gradlew assembleRelease
# APK sẽ ở: android/app/build/outputs/apk/release/app-release.apk
```

**iOS (IPA):**

- Mở project trong Xcode
- Archive
- Distribute App

#### App Store Submission

**Checklist:**

- App icons (various sizes)
- Screenshots
- App description
- Privacy policy
- Terms of service
- Version number
- Build number

---

# GIAI ĐOẠN 4: NÂNG CAO & CHUYÊN SÂU (Tháng 13-18)

## THÁNG 13-14: System Design

### 15.1. Scalability Concepts

**Kiến thức:**

- Vertical scaling vs Horizontal scaling
- Load balancing
- Database sharding
- Caching strategies
- CDN (Content Delivery Network)
- CAP Theorem

**Load Balancing:**

```
┌─────────┐
│ Client  │
└────┬────┘
     │
┌────▼──────────┐
│ Load Balancer │
└──┬──────┬─────┘
   │      │
┌──▼──┐ ┌─▼──┐
│App1 │ │App2│
└─────┘ └────┘
```

**Database Sharding:**

```
User ID 1-1000   → Shard 1
User ID 1001-2000 → Shard 2
User ID 2001-3000 → Shard 3
```

### 15.2. System Design Examples

#### URL Shortener (bit.ly)

**Requirements:**

- Shorten long URLs
- Redirect to original URL
- Analytics

**Design:**

```
┌──────┐     ┌──────────┐     ┌─────────┐
│Client│────▶│API Server│────▶│Database │
└──────┘     └──────────┘     └─────────┘
                    │
                    ▼
              ┌──────────┐
              │   Cache  │
              └──────────┘
```

**Key Components:**

- Base62 encoding cho short URL
- Distributed ID generation
- Caching popular URLs
- Database với indexes

#### Twitter Clone

**Requirements:**

- Post tweets
- Follow users
- Timeline feed
- Real-time updates

**Design:**

- Fan-out on write vs Fan-out on read
- Message queue cho real-time
- Caching cho feeds
- Database sharding by user

**Chi tiết Implementation:**

**Database Schema:**

```sql
-- Users
CREATE TABLE users (
    id BIGINT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(255),
    created_at TIMESTAMP
);

-- Tweets
CREATE TABLE tweets (
    id BIGINT PRIMARY KEY,
    user_id BIGINT REFERENCES users(id),
    content TEXT,
    created_at TIMESTAMP,
    INDEX idx_user_created (user_id, created_at DESC)
);

-- Follows
CREATE TABLE follows (
    follower_id BIGINT REFERENCES users(id),
    followee_id BIGINT REFERENCES users(id),
    PRIMARY KEY (follower_id, followee_id)
);

-- Timeline cache (Redis)
-- Key: timeline:user_id
-- Value: List of tweet IDs
```

**Fan-out on Write (Push Model):**

```javascript
// Khi user post tweet
async function postTweet(userId, content) {
    const tweet = await Tweet.create({ user_id: userId, content });
  
    // Push vào timeline của tất cả followers
    const followers = await Follow.find({ followee_id: userId });
  
    for (const follower of followers) {
        await redis.lpush(`timeline:${follower.follower_id}`, tweet.id);
        await redis.ltrim(`timeline:${follower.follower_id}`, 0, 800); // Giữ 800 tweets mới nhất
    }
  
    return tweet;
}

// Lấy timeline
async function getTimeline(userId) {
    const tweetIds = await redis.lrange(`timeline:${userId}`, 0, 20);
    const tweets = await Tweet.find({ id: { $in: tweetIds } })
        .populate('user_id')
        .sort({ created_at: -1 });
  
    return tweets;
}
```

**Fan-out on Read (Pull Model):**

```javascript
// Khi user post tweet - chỉ lưu vào database
async function postTweet(userId, content) {
    return await Tweet.create({ user_id: userId, content });
}

// Lấy timeline - query real-time
async function getTimeline(userId) {
    const following = await Follow.find({ follower_id: userId })
        .select('followee_id');
    const followingIds = following.map(f => f.followee_id);
  
    const tweets = await Tweet.find({
        user_id: { $in: followingIds }
    })
    .populate('user_id')
    .sort({ created_at: -1 })
    .limit(20);
  
    return tweets;
}
```

**Hybrid Approach (Recommended):**

```javascript
// Push cho users có nhiều followers (celebrity)
// Pull cho users có ít followers (normal users)

async function postTweet(userId, content) {
    const tweet = await Tweet.create({ user_id: userId, content });
    const followerCount = await Follow.count({ followee_id: userId });
  
    if (followerCount > 1000) {
        // Push model cho celebrity
        const followers = await Follow.find({ followee_id: userId });
        for (const follower of followers) {
            await redis.lpush(`timeline:${follower.follower_id}`, tweet.id);
        }
    }
  
    return tweet;
}

async function getTimeline(userId) {
    // Kiểm tra cache trước
    const cached = await redis.lrange(`timeline:${userId}`, 0, 20);
    if (cached.length > 0) {
        return await Tweet.find({ id: { $in: cached } })
            .populate('user_id')
            .sort({ created_at: -1 });
    }
  
    // Fallback to pull model
    return getTimelinePull(userId);
}
```

#### Uber Clone

**Requirements:**

- Match riders với drivers
- Real-time location tracking
- Payment processing
- Rating system

**Design:**

```
┌─────────┐
│  Rider  │
└────┬────┘
     │
┌────▼──────────┐
│ Matching      │
│ Service       │
└──┬──────┬─────┘
   │      │
┌──▼──┐ ┌─▼──┐
│Geo  │ │Pay │
│Svc  │ │Svc │
└─────┘ └────┘
```

**Key Components:**

- Geospatial database (MongoDB với geospatial indexes)
- Real-time matching algorithm
- WebSocket cho real-time updates
- Payment gateway integration

**Implementation:**

```javascript
// Geospatial query để tìm drivers gần nhất
async function findNearbyDrivers(latitude, longitude, radius = 5) {
    const drivers = await Driver.find({
        location: {
            $near: {
                $geometry: {
                    type: "Point",
                    coordinates: [longitude, latitude]
                },
                $maxDistance: radius * 1000 // meters
            }
        },
        status: 'available'
    }).limit(10);
  
    return drivers;
}

// Matching service
async function matchRide(riderId, pickupLocation, dropoffLocation) {
    const nearbyDrivers = await findNearbyDrivers(
        pickupLocation.latitude,
        pickupLocation.longitude
    );
  
    if (nearbyDrivers.length === 0) {
        return { error: 'No drivers available' };
    }
  
    // Chọn driver gần nhất
    const selectedDriver = nearbyDrivers[0];
  
    // Tạo ride request
    const ride = await Ride.create({
        rider_id: riderId,
        driver_id: selectedDriver.id,
        pickup_location: pickupLocation,
        dropoff_location: dropoffLocation,
        status: 'matched'
    });
  
    // Notify driver qua WebSocket
    io.to(`driver:${selectedDriver.id}`).emit('ride_request', ride);
  
    return ride;
}
```

---

## THÁNG 15: Advanced Algorithms

### 16.1. Dynamic Programming

**Kiến thức:**

- Memoization
- Tabulation
- Common patterns: Fibonacci, Knapsack, LCS

**Ví dụ:**

```python
# Fibonacci với DP
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Tabulation
def fibonacci_tab(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

### 16.2. Graph Algorithms

**BFS (Breadth-First Search):**

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
  
    while queue:
        node = queue.popleft()
        print(node)
      
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**DFS (Depth-First Search):**

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
  
    visited.add(start)
    print(start)
  
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

**Dijkstra's Algorithm:**

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
  
    while pq:
        current_dist, current = heapq.heappop(pq)
      
        if current_dist > distances[current]:
            continue
      
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
          
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
  
    return distances
```

---

## THÁNG 16: Distributed Systems

### 17.1. Microservices Architecture

**Patterns:**

- API Gateway
- Service Discovery
- Circuit Breaker
- Saga Pattern

**Chi tiết Implementation:**

#### Service Discovery

**Consul Example:**

```javascript
const consul = require('consul')();

// Register service
consul.agent.service.register({
    name: 'user-service',
    address: 'localhost',
    port: 3001,
    check: {
        http: 'http://localhost:3001/health',
        interval: '10s'
    }
}, (err) => {
    if (err) throw err;
    console.log('Service registered');
});

// Discover service
consul.health.service({
    service: 'user-service',
    passing: true
}, (err, result) => {
    if (err) throw err;
    const service = result[0];
    const url = `http://${service.Service.Address}:${service.Service.Port}`;
    console.log('Service found:', url);
});
```

#### Circuit Breaker Pattern

```javascript
class CircuitBreaker {
    constructor(service, threshold = 5, timeout = 60000) {
        this.service = service;
        this.failureCount = 0;
        this.threshold = threshold;
        this.timeout = timeout;
        this.state = 'CLOSED'; // CLOSED, OPEN, HALF_OPEN
        this.nextAttempt = Date.now();
    }
  
    async call(...args) {
        if (this.state === 'OPEN') {
            if (Date.now() < this.nextAttempt) {
                throw new Error('Circuit breaker is OPEN');
            }
            this.state = 'HALF_OPEN';
        }
      
        try {
            const result = await this.service(...args);
            this.onSuccess();
            return result;
        } catch (error) {
            this.onFailure();
            throw error;
        }
    }
  
    onSuccess() {
        this.failureCount = 0;
        this.state = 'CLOSED';
    }
  
    onFailure() {
        this.failureCount++;
        if (this.failureCount >= this.threshold) {
            this.state = 'OPEN';
            this.nextAttempt = Date.now() + this.timeout;
        }
    }
}

// Usage
const breaker = new CircuitBreaker(async (userId) => {
    const response = await fetch(`http://user-service/api/users/${userId}`);
    return response.json();
});

try {
    const user = await breaker.call(123);
    console.log(user);
} catch (error) {
    console.error('Service unavailable:', error);
}
```

#### Saga Pattern (Distributed Transactions)

```javascript
// Order Saga - Choreography pattern
class OrderSaga {
    async createOrder(orderData) {
        try {
            // Step 1: Reserve inventory
            await this.reserveInventory(orderData.items);
          
            // Step 2: Process payment
            await this.processPayment(orderData.payment);
          
            // Step 3: Create order
            const order = await this.createOrderRecord(orderData);
          
            // Step 4: Send notification
            await this.sendNotification(order.userId, order.id);
          
            return order;
        } catch (error) {
            // Compensating transactions
            await this.compensate(orderData);
            throw error;
        }
    }
  
    async compensate(orderData) {
        // Rollback inventory
        await this.releaseInventory(orderData.items);
      
        // Refund payment
        await this.refundPayment(orderData.payment);
      
        // Cancel order if created
        if (orderData.orderId) {
            await this.cancelOrder(orderData.orderId);
        }
    }
}
```

### 17.2. Event-Driven Architecture

**Concepts:**

- Event sourcing
- CQRS (Command Query Responsibility Segregation)
- Message queues
- Event streaming

**Chi tiết Implementation:**

#### Event Sourcing

```javascript
// Event Store
class EventStore {
    constructor() {
        this.events = [];
    }
  
    append(aggregateId, event) {
        this.events.push({
            aggregateId,
            event,
            timestamp: Date.now()
        });
    }
  
    getEvents(aggregateId) {
        return this.events.filter(e => e.aggregateId === aggregateId);
    }
}

// Aggregate
class Order {
    constructor(id) {
        this.id = id;
        this.status = 'pending';
        this.items = [];
    }
  
    apply(event) {
        switch (event.type) {
            case 'ORDER_CREATED':
                this.status = 'created';
                this.items = event.items;
                break;
            case 'ORDER_PAID':
                this.status = 'paid';
                break;
            case 'ORDER_SHIPPED':
                this.status = 'shipped';
                break;
        }
    }
  
    static fromEvents(events) {
        const order = new Order(events[0].aggregateId);
        events.forEach(event => order.apply(event));
        return order;
    }
}

// Usage
const eventStore = new EventStore();

// Create order
const orderId = 'order-123';
eventStore.append(orderId, {
    type: 'ORDER_CREATED',
    items: [{ productId: 'p1', quantity: 2 }]
});

eventStore.append(orderId, {
    type: 'ORDER_PAID',
    amount: 100
});

// Reconstruct order from events
const events = eventStore.getEvents(orderId);
const order = Order.fromEvents(events);
console.log(order); // { id: 'order-123', status: 'paid', items: [...] }
```

#### CQRS (Command Query Responsibility Segregation)

```javascript
// Command Side (Write)
class OrderCommandHandler {
    async createOrder(command) {
        // Write to event store
        await eventStore.append(command.orderId, {
            type: 'ORDER_CREATED',
            ...command
        });
      
        // Publish event
        await eventBus.publish('order.created', command);
    }
  
    async payOrder(command) {
        await eventStore.append(command.orderId, {
            type: 'ORDER_PAID',
            ...command
        });
      
        await eventBus.publish('order.paid', command);
    }
}

// Query Side (Read)
class OrderQueryHandler {
    constructor(readModel) {
        this.readModel = readModel; // Optimized read database
    }
  
    async getOrder(orderId) {
        return await this.readModel.findById(orderId);
    }
  
    async getOrdersByUser(userId) {
        return await this.readModel.find({ userId });
    }
}

// Projection (Update read model from events)
class OrderProjection {
    async handle(event) {
        switch (event.type) {
            case 'ORDER_CREATED':
                await this.readModel.create({
                    id: event.orderId,
                    userId: event.userId,
                    status: 'created',
                    items: event.items,
                    createdAt: new Date()
                });
                break;
            case 'ORDER_PAID':
                await this.readModel.update(
                    { id: event.orderId },
                    { status: 'paid', paidAt: new Date() }
                );
                break;
        }
    }
}
```

#### Event Streaming với Kafka

```javascript
const { Kafka } = require('kafkajs');

const kafka = new Kafka({
    clientId: 'my-app',
    brokers: ['localhost:9092']
});

// Producer
const producer = kafka.producer();
await producer.connect();

async function publishEvent(topic, event) {
    await producer.send({
        topic,
        messages: [{
            key: event.aggregateId,
            value: JSON.stringify(event)
        }]
    });
}

// Consumer
const consumer = kafka.consumer({ groupId: 'order-group' });
await consumer.connect();
await consumer.subscribe({ topic: 'order-events', fromBeginning: true });

await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
        const event = JSON.parse(message.value.toString());
        console.log('Received event:', event);
      
        // Handle event
        await handleEvent(event);
    }
});

// Event handlers
async function handleEvent(event) {
    switch (event.type) {
        case 'ORDER_CREATED':
            await updateInventory(event.items);
            await sendNotification(event.userId);
            break;
        case 'ORDER_PAID':
            await processShipping(event.orderId);
            break;
    }
}
```

---

## THÁNG 17: Security & Performance

### 18.1. Web Security

#### OWASP Top 10

1. **Injection**: SQL, NoSQL, Command injection
2. **Broken Authentication**: Weak passwords, session management
3. **Sensitive Data Exposure**: Encryption, HTTPS
4. **XML External Entities (XXE)**
5. **Broken Access Control**: Authorization
6. **Security Misconfiguration**
7. **XSS (Cross-Site Scripting)**
8. **Insecure Deserialization**
9. **Using Components with Known Vulnerabilities**
10. **Insufficient Logging & Monitoring**

**Prevention:**

```javascript
// SQL Injection prevention
// ❌ Bad
const query = `SELECT * FROM users WHERE id = ${userId}`;

// ✅ Good
const query = 'SELECT * FROM users WHERE id = $1';
await db.query(query, [userId]);

// XSS prevention
// ✅ Sanitize input
const sanitized = DOMPurify.sanitize(userInput);

// Password hashing
const bcrypt = require('bcrypt');
const hashedPassword = await bcrypt.hash(password, 10);
```

### 18.2. Performance Optimization

**Database:**

- Indexes
- Query optimization
- Connection pooling
- Read replicas

**Application:**

- Caching
- Code optimization
- Lazy loading
- Compression

**Chi tiết Implementation:**

#### Database Optimization

**Indexes:**

```sql
-- Tạo index cho queries thường dùng
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_order_user_date ON orders(user_id, created_at DESC);
CREATE INDEX idx_product_category ON products(category, price);

-- Composite index
CREATE INDEX idx_user_status_created ON users(status, created_at);

-- Partial index (chỉ index một phần data)
CREATE INDEX idx_active_users ON users(email) WHERE status = 'active';
```

**Query Optimization:**

```javascript
// ❌ Bad: N+1 query problem
const orders = await Order.find();
for (const order of orders) {
    const user = await User.findById(order.userId); // N queries
}

// ✅ Good: Use populate/join
const orders = await Order.find().populate('userId'); // 1 query

// ❌ Bad: Select all fields
const users = await User.find();

// ✅ Good: Select only needed fields
const users = await User.find().select('name email');

// ❌ Bad: No limit
const products = await Product.find();

// ✅ Good: Use pagination
const products = await Product.find()
    .limit(20)
    .skip((page - 1) * 20);
```

**Connection Pooling:**

```javascript
// PostgreSQL với pg-pool
const { Pool } = require('pg');

const pool = new Pool({
    host: 'localhost',
    database: 'mydb',
    user: 'user',
    password: 'password',
    max: 20, // Maximum pool size
    idleTimeoutMillis: 30000,
    connectionTimeoutMillis: 2000
});

// Reuse connections
async function query(text, params) {
    const client = await pool.connect();
    try {
        const result = await client.query(text, params);
        return result.rows;
    } finally {
        client.release();
    }
}
```

**Read Replicas:**

```javascript
// Write to master
const masterDB = new Sequelize('postgres://master-host/db');

// Read from replica
const replicaDB = new Sequelize('postgres://replica-host/db');

async function getUsers() {
    // Read from replica
    return await replicaDB.query('SELECT * FROM users');
}

async function createUser(userData) {
    // Write to master
    return await masterDB.query(
        'INSERT INTO users ...',
        userData
    );
}
```

#### Application Optimization

**Caching Strategies:**

```javascript
// Cache-aside pattern
async function getProduct(productId) {
    // Check cache first
    const cached = await redis.get(`product:${productId}`);
    if (cached) {
        return JSON.parse(cached);
    }
  
    // Cache miss - fetch from database
    const product = await Product.findById(productId);
  
    // Store in cache
    await redis.setEx(
        `product:${productId}`,
        3600, // TTL: 1 hour
        JSON.stringify(product)
    );
  
    return product;
}

// Write-through pattern
async function updateProduct(productId, data) {
    // Update database
    const product = await Product.update(productId, data);
  
    // Update cache immediately
    await redis.setEx(
        `product:${productId}`,
        3600,
        JSON.stringify(product)
    );
  
    return product;
}

// Cache invalidation
async function deleteProduct(productId) {
    await Product.delete(productId);
    await redis.del(`product:${productId}`);
}
```

**Code Optimization:**

```javascript
// ❌ Bad: Synchronous operations
function processData(data) {
    const result = [];
    for (const item of data) {
        result.push(expensiveOperation(item)); // Blocking
    }
    return result;
}

// ✅ Good: Async operations
async function processData(data) {
    const promises = data.map(item => expensiveOperation(item));
    return await Promise.all(promises);
}

// ❌ Bad: Unnecessary computations
function Component({ items }) {
    const sorted = items.sort((a, b) => a.price - b.price); // Re-sort on every render
    return <div>{sorted.map(...)}</div>;
}

// ✅ Good: Memoize
function Component({ items }) {
    const sorted = useMemo(
        () => items.sort((a, b) => a.price - b.price),
        [items]
    );
    return <div>{sorted.map(...)}</div>;
}
```

**Lazy Loading:**

```javascript
// React lazy loading
const HeavyComponent = React.lazy(() => import('./HeavyComponent'));

function App() {
    return (
        <Suspense fallback={<div>Loading...</div>}>
            <HeavyComponent />
        </Suspense>
    );
}

// Image lazy loading
function LazyImage({ src, alt }) {
    const [loaded, setLoaded] = useState(false);
    const imgRef = useRef();
  
    useEffect(() => {
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                setLoaded(true);
                observer.disconnect();
            }
        });
      
        if (imgRef.current) {
            observer.observe(imgRef.current);
        }
      
        return () => observer.disconnect();
    }, []);
  
    return (
        <img
            ref={imgRef}
            src={loaded ? src : 'placeholder.jpg'}
            alt={alt}
        />
    );
}
```

**Compression:**

```javascript
// Express compression middleware
const compression = require('compression');
app.use(compression());

// Gzip static files
// In nginx:
// gzip on;
// gzip_types text/plain text/css application/json application/javascript;

// Image optimization
const sharp = require('sharp');

async function optimizeImage(inputPath, outputPath) {
    await sharp(inputPath)
        .resize(800, 600, { fit: 'inside' })
        .jpeg({ quality: 80 })
        .toFile(outputPath);
}
```

#### Monitoring và Profiling

```javascript
// Performance monitoring
const performance = require('perf_hooks');

async function monitoredFunction() {
    const start = performance.now();
  
    // Your code here
    await doSomething();
  
    const end = performance.now();
    console.log(`Execution time: ${end - start}ms`);
}

// Memory profiling
const v8 = require('v8');

function getMemoryUsage() {
    const usage = process.memoryUsage();
    return {
        heapUsed: (usage.heapUsed / 1024 / 1024).toFixed(2) + ' MB',
        heapTotal: (usage.heapTotal / 1024 / 1024).toFixed(2) + ' MB',
        rss: (usage.rss / 1024 / 1024).toFixed(2) + ' MB'
    };
}

// Database query profiling
mongoose.set('debug', true); // Log all queries

// Or use custom logger
mongoose.set('debug', (collectionName, method, query, doc) => {
    console.log(`${collectionName}.${method}`, query);
});
```

---

## THÁNG 18: Best Practices & Soft Skills

### 19.1. Clean Code

**Principles:**

- Meaningful names
- Functions should do one thing
- Small functions
- No comments (code should be self-documenting)
- Error handling
- DRY (Don't Repeat Yourself)

### 19.2. Code Review

**Checklist:**

- Code quality
- Functionality
- Performance
- Security
- Tests
- Documentation

### 19.3. TDD (Test-Driven Development)

**Process:**

1. Write failing test
2. Write minimal code to pass
3. Refactor
4. Repeat

---

# GIAI ĐOẠN 5: PORTFOLIO & CHUYÊN NGHIỆP (Tháng 19-24)

## THÁNG 19-20: Portfolio Projects

### 20.1. Enterprise E-commerce Platform

**Features:**

- Full stack (React + Node.js)
- Microservices
- Payment (Stripe)
- Real-time notifications
- Admin dashboard
- Analytics
- AWS deployment

**Architecture:**

```
┌─────────────┐
│   Client     │
└──────┬───────┘
       │
┌──────▼──────────┐
│  API Gateway    │
└──┬──────┬───────┘
   │      │      │
┌──▼──┐ ┌─▼──┐ ┌─▼──┐
│User │ │Prod│ │Order│
│Svc  │ │Svc │ │Svc  │
└─────┘ └────┘ └─────┘
```

**Key Components:**

**Payment Integration (Stripe):**

```javascript
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

// Create payment intent
app.post('/api/payments/create-intent', async (req, res) => {
    const { amount, currency = 'usd' } = req.body;
  
    const paymentIntent = await stripe.paymentIntents.create({
        amount: amount * 100, // Convert to cents
        currency,
        metadata: { orderId: req.body.orderId }
    });
  
    res.json({ clientSecret: paymentIntent.client_secret });
});

// Webhook handler
app.post('/api/payments/webhook', express.raw({type: 'application/json'}), (req, res) => {
    const sig = req.headers['stripe-signature'];
    let event;
  
    try {
        event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET);
    } catch (err) {
        return res.status(400).send(`Webhook Error: ${err.message}`);
    }
  
    if (event.type === 'payment_intent.succeeded') {
        const paymentIntent = event.data.object;
        // Update order status
        await Order.update(
            { id: paymentIntent.metadata.orderId },
            { status: 'paid' }
        );
    }
  
    res.json({ received: true });
});
```

**Real-time Notifications:**

```javascript
// WebSocket server
const io = require('socket.io')(server);

io.on('connection', (socket) => {
    socket.on('join-room', (userId) => {
        socket.join(`user:${userId}`);
    });
});

// Send notification
function notifyUser(userId, notification) {
    io.to(`user:${userId}`).emit('notification', notification);
}

// Usage
notifyUser(userId, {
    type: 'order_shipped',
    message: 'Your order has been shipped',
    orderId: '123'
});
```

**Analytics:**

```javascript
// Track events
app.post('/api/analytics/track', async (req, res) => {
    const { event, properties, userId } = req.body;
  
    await Analytics.create({
        event,
        properties,
        userId,
        timestamp: new Date()
    });
  
    res.json({ success: true });
});

// Get analytics
app.get('/api/analytics/dashboard', async (req, res) => {
    const { startDate, endDate } = req.query;
  
    const stats = {
        totalOrders: await Order.count({
            createdAt: { $gte: startDate, $lte: endDate }
        }),
        totalRevenue: await Order.aggregate([
            { $match: { createdAt: { $gte: startDate, $lte: endDate } } },
            { $group: { _id: null, total: { $sum: '$total' } } }
        ]),
        topProducts: await OrderItem.aggregate([
            { $match: { createdAt: { $gte: startDate, $lte: endDate } } },
            { $group: { _id: '$productId', count: { $sum: '$quantity' } } },
            { $sort: { count: -1 } },
            { $limit: 10 }
        ])
    };
  
    res.json(stats);
});
```

### 20.2. Social Media Platform

**Features:**

- Full stack
- WebSocket cho real-time chat
- Image/video upload
- Feed algorithm
- React Native app
- Cloud deployment

**Key Components:**

**Real-time Chat:**

```javascript
// Chat service với Socket.io
io.on('connection', (socket) => {
    socket.on('join-room', (roomId) => {
        socket.join(`room:${roomId}`);
    });
  
    socket.on('send-message', async (data) => {
        const message = await Message.create({
            roomId: data.roomId,
            userId: data.userId,
            content: data.content,
            timestamp: new Date()
        });
      
        io.to(`room:${data.roomId}`).emit('new-message', message);
    });
  
    socket.on('typing', (data) => {
        socket.to(`room:${data.roomId}`).emit('user-typing', {
            userId: data.userId,
            isTyping: true
        });
    });
});
```

**Image/Video Upload:**

```javascript
const multer = require('multer');
const { S3Client, PutObjectCommand } = require('@aws-sdk/client-s3');

const s3Client = new S3Client({ region: 'us-east-1' });
const upload = multer({ storage: multer.memoryStorage() });

app.post('/api/upload', upload.single('file'), async (req, res) => {
    const file = req.file;
    const key = `uploads/${Date.now()}-${file.originalname}`;
  
    const command = new PutObjectCommand({
        Bucket: process.env.S3_BUCKET,
        Key: key,
        Body: file.buffer,
        ContentType: file.mimetype,
        ACL: 'public-read'
    });
  
    await s3Client.send(command);
  
    const url = `https://${process.env.S3_BUCKET}.s3.amazonaws.com/${key}`;
    res.json({ url });
});
```

**Feed Algorithm:**

```javascript
// Ranking algorithm
async function getFeed(userId, page = 1, limit = 20) {
    const user = await User.findById(userId);
    const following = await Follow.find({ followerId: userId })
        .select('followeeId');
    const followingIds = following.map(f => f.followeeId);
  
    // Get posts from following
    const posts = await Post.find({
        userId: { $in: followingIds }
    })
    .populate('userId')
    .sort({ createdAt: -1 })
    .limit(limit * 2);
  
    // Score posts
    const scoredPosts = posts.map(post => ({
        post,
        score: calculateScore(post, user)
    }));
  
    // Sort by score
    scoredPosts.sort((a, b) => b.score - a.score);
  
    // Return top posts
    return scoredPosts.slice(0, limit).map(item => item.post);
}

function calculateScore(post, user) {
    let score = 0;
  
    // Recency (newer posts score higher)
    const hoursAgo = (Date.now() - post.createdAt) / (1000 * 60 * 60);
    score += Math.max(0, 100 - hoursAgo);
  
    // Engagement
    score += post.likes.length * 2;
    score += post.comments.length * 3;
    score += post.shares.length * 5;
  
    // User preferences
    if (user.preferredCategories.includes(post.category)) {
        score += 20;
    }
  
    return score;
}
```

### 20.3. SaaS Application

**Features:**

- Multi-tenancy
- Subscription management
- Third-party API
- Advanced features
- Mobile app

**Multi-tenancy Implementation:**

```javascript
// Tenant isolation
class TenantAwareModel {
    static async find(tenantId, query = {}) {
        return await this.model.find({
            tenantId,
            ...query
        });
    }
  
    static async create(tenantId, data) {
        return await this.model.create({
            tenantId,
            ...data
        });
    }
}

// Middleware to extract tenant
function tenantMiddleware(req, res, next) {
    const tenantId = req.headers['x-tenant-id'] || 
                     req.subdomain || 
                     req.query.tenantId;
  
    if (!tenantId) {
        return res.status(400).json({ error: 'Tenant ID required' });
    }
  
    req.tenantId = tenantId;
    next();
}

// Usage
app.use(tenantMiddleware);

app.get('/api/data', async (req, res) => {
    const data = await DataModel.find(req.tenantId);
    res.json(data);
});
```

**Subscription Management:**

```javascript
// Subscription service
class SubscriptionService {
    async createSubscription(userId, planId) {
        const plan = await Plan.findById(planId);
        const subscription = await Subscription.create({
            userId,
            planId,
            status: 'active',
            currentPeriodStart: new Date(),
            currentPeriodEnd: new Date(Date.now() + plan.duration * 24 * 60 * 60 * 1000)
        });
      
        // Create Stripe subscription
        const stripeSubscription = await stripe.subscriptions.create({
            customer: userId,
            items: [{ price: plan.stripePriceId }]
        });
      
        subscription.stripeSubscriptionId = stripeSubscription.id;
        await subscription.save();
      
        return subscription;
    }
  
    async checkAccess(userId, feature) {
        const subscription = await Subscription.findOne({
            userId,
            status: 'active'
        }).populate('planId');
      
        if (!subscription) return false;
      
        return subscription.planId.features.includes(feature);
    }
}

// Middleware to check subscription
async function requireSubscription(feature) {
    return async (req, res, next) => {
        const hasAccess = await subscriptionService.checkAccess(
            req.user.id,
            feature
        );
      
        if (!hasAccess) {
            return res.status(403).json({
                error: 'Subscription required',
                upgradeUrl: '/pricing'
            });
        }
      
        next();
    };
}

// Usage
app.get('/api/premium-feature',
    authenticateToken,
    requireSubscription('premium_feature'),
    async (req, res) => {
        // Premium feature logic
    }
);
```

---

## THÁNG 21-22: Open Source & Community

### 21.1. Contributing to Open Source

**Steps:**

1. Find projects (GitHub, good first issues)
2. Fork repository
3. Create branch
4. Make changes
5. Write tests
6. Submit PR
7. Respond to feedback

### 21.2. Technical Blogging

**Topics:**

- Tutorials
- Problem-solving
- Architecture decisions
- Lessons learned
- Code reviews

**Platforms:**

- Medium
- Dev.to
- Personal blog
- LinkedIn

---

## THÁNG 23-24: Interview Preparation

### 22.1. System Design Interview

**Framework:**

1. Requirements clarification
2. Capacity estimation
3. System interface design
4. Data model design
5. High-level design
6. Detailed design
7. Identify bottlenecks
8. Scale the system

### 22.2. Coding Interview

**Patterns:**

- Two pointers
- Sliding window
- Hash maps
- Trees
- Graphs
- Dynamic programming
- Backtracking

**Practice:**

- LeetCode (150+ problems)
- Mock interviews
- Time management
- Communication

### 22.3. Behavioral Interview

**STAR Method:**

- Situation
- Task
- Action
- Result

**Common Questions:**

- Tell me about yourself
- Why do you want this job?
- Describe a challenging project
- How do you handle conflicts?

---

# CHECKLIST TỔNG THỂ

## Kiến thức

- [ ] Thành thạo Python/JavaScript
- [ ] Thành thạo React và một backend framework
- [ ] Thành thạo React Native
- [ ] Hiểu về System Design
- [ ] Giải được 200+ LeetCode problems
- [ ] Hiểu về Microservices
- [ ] Hiểu về Security best practices

## Projects

- [ ] 5+ Full Stack Web Applications
- [ ] 2+ Mobile Applications
- [ ] 1+ Microservices Project
- [ ] Tất cả đều deploy được và có tests

## Skills

- [ ] Code Review
- [ ] Refactoring
- [ ] Testing (Unit, Integration)
- [ ] Debugging
- [ ] Documentation
- [ ] Git workflow
- [ ] CI/CD

## Community

- [ ] Contribute to 5+ open source projects
- [ ] Write 10+ technical blog posts
- [ ] Có GitHub profile impressive
- [ ] Có thể mentor junior developers

## Interview

- [ ] Sẵn sàng System Design Interview
- [ ] Sẵn sàng Coding Interview
- [ ] Sẵn sàng Behavioral Interview
- [ ] Có portfolio projects tốt

---

# KIẾN THỨC THỰC TẾ TỪ DỰ ÁN PRODUCTION

> Phần này bao gồm những kiến thức và kỹ năng thực tế mà Senior Developers cần có khi làm việc với các dự án production. Đây là những kinh nghiệm quý giá từ thực tế.

## 1. DEBUGGING VÀ TROUBLESHOOTING TRONG PRODUCTION

### 1.1. Debugging Strategies

**Kiến thức:**

- Logging strategies
- Error tracking
- Distributed tracing
- Performance profiling
- Memory leak detection

**Logging Best Practices:**

```javascript
// Structured logging
const winston = require('winston');

const logger = winston.createLogger({
    level: process.env.LOG_LEVEL || 'info',
    format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.errors({ stack: true }),
        winston.format.json()
    ),
    defaultMeta: { service: 'user-service' },
    transports: [
        new winston.transports.File({ filename: 'error.log', level: 'error' }),
        new winston.transports.File({ filename: 'combined.log' })
    ]
});

// Log với context
logger.info('User created', {
    userId: user.id,
    email: user.email,
    timestamp: new Date().toISOString(),
    requestId: req.id,
    ip: req.ip
});

// Error logging với stack trace
try {
    await riskyOperation();
} catch (error) {
    logger.error('Operation failed', {
        error: error.message,
        stack: error.stack,
        context: { userId, operationId },
        requestId: req.id
    });
    throw error;
}
```

**Error Tracking với Sentry:**

```javascript
const Sentry = require('@sentry/node');

Sentry.init({
    dsn: process.env.SENTRY_DSN,
    environment: process.env.NODE_ENV,
    tracesSampleRate: 1.0
});

// Capture exceptions
try {
    await riskyOperation();
} catch (error) {
    Sentry.captureException(error, {
        tags: {
            section: 'payment',
            userId: user.id
        },
        extra: {
            orderId: order.id,
            amount: order.amount
        }
    });
    throw error;
}

// Capture messages
Sentry.captureMessage('Something went wrong', {
    level: 'warning',
    tags: { component: 'checkout' }
});
```

**Distributed Tracing:**

```javascript
const { trace, context } = require('@opentelemetry/api');

// Tạo span
const tracer = trace.getTracer('user-service');

async function createUser(userData) {
    const span = tracer.startSpan('createUser');
  
    try {
        span.setAttribute('user.email', userData.email);
      
        // Child span
        const dbSpan = tracer.startSpan('db.insert', {
            parent: span
        });
      
        const user = await db.insert(userData);
        dbSpan.setAttribute('db.operation', 'insert');
        dbSpan.setAttribute('db.table', 'users');
        dbSpan.end();
      
        span.setAttribute('user.id', user.id);
        span.setStatus({ code: 1 }); // OK
      
        return user;
    } catch (error) {
        span.setStatus({
            code: 2, // ERROR
            message: error.message
        });
        span.recordException(error);
        throw error;
    } finally {
        span.end();
    }
}
```

### 1.2. Common Production Issues và Solutions

**Memory Leaks:**

```javascript
// ❌ Memory leak: Event listeners không được cleanup
class UserService {
    constructor() {
        this.eventEmitter = new EventEmitter();
    }
  
    subscribe(userId, callback) {
        this.eventEmitter.on('user-updated', callback);
        // ❌ Không có cách unsubscribe
    }
}

// ✅ Fixed: Cleanup listeners
class UserService {
    constructor() {
        this.eventEmitter = new EventEmitter();
        this.listeners = new Map();
    }
  
    subscribe(userId, callback) {
        const listener = (data) => {
            if (data.userId === userId) {
                callback(data);
            }
        };
      
        this.eventEmitter.on('user-updated', listener);
        this.listeners.set(userId, listener);
    }
  
    unsubscribe(userId) {
        const listener = this.listeners.get(userId);
        if (listener) {
            this.eventEmitter.removeListener('user-updated', listener);
            this.listeners.delete(userId);
        }
    }
}

// Memory profiling
const v8 = require('v8');

setInterval(() => {
    const heapStats = v8.getHeapStatistics();
    console.log('Heap:', {
        used: (heapStats.used_heap_size / 1024 / 1024).toFixed(2) + ' MB',
        total: (heapStats.total_heap_size / 1024 / 1024).toFixed(2) + ' MB',
        limit: (heapStats.heap_size_limit / 1024 / 1024).toFixed(2) + ' MB'
    });
}, 60000);
```

**Database Connection Issues:**

```javascript
// Connection pool monitoring
const pool = new Pool({
    max: 20,
    idleTimeoutMillis: 30000
});

// Monitor pool stats
setInterval(() => {
    console.log('Pool stats:', {
        total: pool.totalCount,
        idle: pool.idleCount,
        waiting: pool.waitingCount
    });
  
    if (pool.waitingCount > 10) {
        logger.warn('High number of waiting connections', {
            waiting: pool.waitingCount,
            total: pool.totalCount
        });
    }
}, 5000);

// Handle connection errors
pool.on('error', (err) => {
    logger.error('Database pool error', {
        error: err.message,
        stack: err.stack
    });
  
    // Alert team
    sendAlert('Database connection error', err);
});
```

**Slow Queries:**

```javascript
// Query timeout
const queryWithTimeout = async (query, params, timeout = 5000) => {
    return Promise.race([
        db.query(query, params),
        new Promise((_, reject) =>
            setTimeout(() => reject(new Error('Query timeout')), timeout)
        )
    ]);
};

// Log slow queries
const originalQuery = db.query.bind(db);
db.query = async function(query, params) {
    const start = Date.now();
    try {
        const result = await originalQuery(query, params);
        const duration = Date.now() - start;
      
        if (duration > 1000) {
            logger.warn('Slow query detected', {
                query,
                duration,
                params
            });
        }
      
        return result;
    } catch (error) {
        logger.error('Query failed', {
            query,
            error: error.message,
            params
        });
        throw error;
    }
};
```

## 2. MONITORING VÀ OBSERVABILITY

### 2.1. Application Monitoring

**Metrics Collection:**

```javascript
const prometheus = require('prom-client');

// Create metrics
const httpRequestDuration = new prometheus.Histogram({
    name: 'http_request_duration_seconds',
    help: 'Duration of HTTP requests in seconds',
    labelNames: ['method', 'route', 'status_code'],
    buckets: [0.1, 0.5, 1, 2, 5]
});

const httpRequestTotal = new prometheus.Counter({
    name: 'http_requests_total',
    help: 'Total number of HTTP requests',
    labelNames: ['method', 'route', 'status_code']
});

const activeConnections = new prometheus.Gauge({
    name: 'active_connections',
    help: 'Number of active connections'
});

// Middleware để collect metrics
app.use((req, res, next) => {
    const start = Date.now();
  
    res.on('finish', () => {
        const duration = (Date.now() - start) / 1000;
        httpRequestDuration.observe(
            { method: req.method, route: req.route?.path || req.path, status_code: res.statusCode },
            duration
        );
        httpRequestTotal.inc({
            method: req.method,
            route: req.route?.path || req.path,
            status_code: res.statusCode
        });
    });
  
    next();
});

// Expose metrics endpoint
app.get('/metrics', async (req, res) => {
    res.set('Content-Type', prometheus.register.contentType);
    res.end(await prometheus.register.metrics());
});
```

**Health Checks:**

```javascript
// Health check endpoint
app.get('/health', async (req, res) => {
    const health = {
        status: 'healthy',
        timestamp: new Date().toISOString(),
        checks: {}
    };
  
    // Check database
    try {
        await db.query('SELECT 1');
        health.checks.database = 'healthy';
    } catch (error) {
        health.checks.database = 'unhealthy';
        health.status = 'unhealthy';
    }
  
    // Check Redis
    try {
        await redis.ping();
        health.checks.redis = 'healthy';
    } catch (error) {
        health.checks.redis = 'unhealthy';
        health.status = 'unhealthy';
    }
  
    // Check external API
    try {
        const response = await fetch('https://api.example.com/health');
        if (response.ok) {
            health.checks.externalApi = 'healthy';
        } else {
            health.checks.externalApi = 'unhealthy';
            health.status = 'unhealthy';
        }
    } catch (error) {
        health.checks.externalApi = 'unhealthy';
        health.status = 'unhealthy';
    }
  
    const statusCode = health.status === 'healthy' ? 200 : 503;
    res.status(statusCode).json(health);
});
```

**Alerting:**

```javascript
// Alert system
class AlertManager {
    async sendAlert(severity, message, details) {
        const alert = {
            severity, // 'critical', 'warning', 'info'
            message,
            details,
            timestamp: new Date().toISOString(),
            service: process.env.SERVICE_NAME
        };
      
        // Send to Slack
        await this.sendToSlack(alert);
      
        // Send to PagerDuty for critical alerts
        if (severity === 'critical') {
            await this.sendToPagerDuty(alert);
        }
      
        // Log
        logger.error('Alert sent', alert);
    }
  
    async sendToSlack(alert) {
        const webhook = process.env.SLACK_WEBHOOK;
        await fetch(webhook, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                text: `[${alert.severity.toUpperCase()}] ${alert.message}`,
                attachments: [{
                    color: alert.severity === 'critical' ? 'danger' : 'warning',
                    fields: [
                        { title: 'Service', value: alert.service, short: true },
                        { title: 'Time', value: alert.timestamp, short: true },
                        { title: 'Details', value: JSON.stringify(alert.details, null, 2), short: false }
                    ]
                }]
            })
        });
    }
}

// Usage
const alertManager = new AlertManager();

// Monitor error rate
let errorCount = 0;
setInterval(() => {
    if (errorCount > 100) {
        alertManager.sendAlert('critical', 'High error rate detected', {
            errorCount,
            timeWindow: '1 minute'
        });
    }
    errorCount = 0;
}, 60000);
```

### 2.2. Log Aggregation

**ELK Stack (Elasticsearch, Logstash, Kibana):**

```javascript
// Winston transport for ELK
const { ElasticsearchTransport } = require('winston-elasticsearch');

const esTransport = new ElasticsearchTransport({
    level: 'info',
    clientOpts: {
        node: process.env.ELASTICSEARCH_URL,
        auth: {
            username: process.env.ES_USERNAME,
            password: process.env.ES_PASSWORD
        }
    },
    index: 'logs-app-%{YYYY.MM.DD}'
});

logger.add(esTransport);

// Structured logs for better searchability
logger.info('User action', {
    userId: user.id,
    action: 'purchase',
    productId: product.id,
    amount: order.amount,
    timestamp: new Date().toISOString(),
    // Add business context
    sessionId: req.session.id,
    userAgent: req.headers['user-agent'],
    ip: req.ip
});
```

## 3. INCIDENT RESPONSE VÀ ON-CALL

### 3.1. Incident Response Process

**Runbook Template:**

```markdown
# Incident: High Error Rate

## Symptoms
- Error rate > 5% for last 5 minutes
- Multiple users reporting issues
- Dashboard showing red alerts

## Immediate Actions
1. Check health endpoints: `/health`
2. Check error logs in Kibana
3. Check database connection pool
4. Check external API status

## Common Causes
1. Database connection pool exhausted
2. External API timeout
3. Memory leak causing OOM
4. Recent deployment issue

## Resolution Steps
1. Check recent deployments
2. Check database metrics
3. Check external dependencies
4. Rollback if needed
5. Scale up if resource issue

## Post-Incident
1. Root cause analysis
2. Update runbook
3. Add monitoring/alerting
4. Document lessons learned
```

**Incident Response Code:**

```javascript
// Circuit breaker for external APIs
class IncidentHandler {
    async handleIncident(incident) {
        // Log incident
        logger.error('Incident detected', incident);
      
        // Auto-remediation attempts
        if (incident.type === 'high_error_rate') {
            await this.scaleUp();
            await this.clearCache();
        }
      
        if (incident.type === 'database_connection_pool_exhausted') {
            await this.restartConnectionPool();
        }
      
        // Alert on-call engineer
        await this.pageOnCall(incident);
      
        // Create incident ticket
        await this.createIncidentTicket(incident);
    }
  
    async scaleUp() {
        // Auto-scale logic
        logger.info('Auto-scaling triggered');
        // Call your orchestration API (Kubernetes, AWS Auto Scaling, etc.)
    }
  
    async pageOnCall(incident) {
        // Page on-call engineer via PagerDuty, Opsgenie, etc.
        await fetch(process.env.PAGERDUTY_WEBHOOK, {
            method: 'POST',
            body: JSON.stringify({
                routing_key: process.env.PAGERDUTY_KEY,
                event_action: 'trigger',
                payload: {
                    summary: incident.message,
                    severity: incident.severity,
                    source: process.env.SERVICE_NAME
                }
            })
        });
    }
}
```

## 4. CODE REVIEW THỰC TẾ

### 4.1. Code Review Checklist

**Security Review:**

```javascript
// ❌ Security issues to catch in review

// 1. SQL Injection
const query = `SELECT * FROM users WHERE id = ${userId}`; // ❌

// 2. XSS
res.send(`<div>${userInput}</div>`); // ❌

// 3. Hardcoded secrets
const apiKey = 'sk_live_1234567890'; // ❌

// 4. Missing authentication
app.get('/api/admin/users', async (req, res) => { // ❌
    const users = await User.find();
    res.json(users);
});

// 5. Missing rate limiting
app.post('/api/login', async (req, res) => { // ❌
    // No rate limiting - vulnerable to brute force
});

// ✅ Good practices
const query = 'SELECT * FROM users WHERE id = $1'; // ✅
await db.query(query, [userId]);

const sanitized = DOMPurify.sanitize(userInput); // ✅
res.send(`<div>${sanitized}</div>`);

const apiKey = process.env.API_KEY; // ✅

app.get('/api/admin/users', authenticateToken, requireRole('admin'), async (req, res) => { // ✅
    const users = await User.find();
    res.json(users);
});

const rateLimiter = rateLimit({ windowMs: 15 * 60 * 1000, max: 5 }); // ✅
app.post('/api/login', rateLimiter, async (req, res) => {
    // Login logic
});
```

**Performance Review:**

```javascript
// ❌ Performance issues

// 1. N+1 queries
const orders = await Order.find();
for (const order of orders) {
    const user = await User.findById(order.userId); // ❌
}

// 2. Missing indexes
await User.find({ email: email }); // ❌ No index on email

// 3. Loading too much data
const users = await User.find(); // ❌ Load all users

// 4. Synchronous operations in async context
function processData(data) {
    return data.map(item => expensiveSyncOperation(item)); // ❌
}

// ✅ Good practices
const orders = await Order.find().populate('userId'); // ✅

await User.find({ email: email }); // ✅ Index exists

const users = await User.find().limit(20).skip((page - 1) * 20); // ✅

async function processData(data) {
    return await Promise.all(
        data.map(item => expensiveAsyncOperation(item)) // ✅
    );
}
```

**Code Quality Review:**

```javascript
// ❌ Code quality issues

// 1. Magic numbers
if (user.age > 18) { // ❌ What is 18?
    // ...
}

// 2. Long functions
async function processOrder(order) {
    // 200 lines of code... // ❌
}

// 3. Duplicate code
function calculatePrice1(items) {
    let total = 0;
    for (let i = 0; i < items.length; i++) {
        total += items[i].price * items[i].quantity;
    }
    return total;
}

function calculatePrice2(items) {
    let total = 0;
    for (let i = 0; i < items.length; i++) {
        total += items[i].price * items[i].quantity; // ❌ Duplicate
    }
    return total;
}

// 4. Poor error handling
async function getUser(id) {
    const user = await User.findById(id); // ❌ No error handling
    return user;
}

// ✅ Good practices
const MINIMUM_AGE = 18; // ✅
if (user.age > MINIMUM_AGE) {
    // ...
}

async function processOrder(order) {
    await validateOrder(order);
    await reserveInventory(order);
    await processPayment(order);
    await createOrderRecord(order);
    await sendNotification(order);
} // ✅ Small, focused functions

function calculatePrice(items) {
    return items.reduce((total, item) => 
        total + item.price * item.quantity, 0
    );
} // ✅ Single source of truth

async function getUser(id) {
    try {
        const user = await User.findById(id);
        if (!user) {
            throw new NotFoundError('User not found');
        }
        return user;
    } catch (error) {
        logger.error('Failed to get user', { id, error });
        throw error;
    }
} // ✅ Proper error handling
```

## 5. TECHNICAL DEBT MANAGEMENT

### 5.1. Identifying và Managing Technical Debt

**Technical Debt Tracking:**

```javascript
// Technical debt registry
const technicalDebt = {
    'high-priority': [
        {
            id: 'TD-001',
            description: 'Refactor payment service - too many responsibilities',
            impact: 'High',
            effort: 'Large',
            created: '2024-01-15',
            due: '2024-03-01',
            owner: 'team-backend'
        },
        {
            id: 'TD-002',
            description: 'Add database indexes for slow queries',
            impact: 'High',
            effort: 'Small',
            created: '2024-01-20',
            due: '2024-02-01',
            owner: 'team-backend'
        }
    ],
    'medium-priority': [
        {
            id: 'TD-003',
            description: 'Update deprecated dependencies',
            impact: 'Medium',
            effort: 'Medium',
            created: '2024-01-10',
            due: '2024-04-01',
            owner: 'team-frontend'
        }
    ]
};

// Code metrics to track debt
const codeMetrics = {
    cyclomaticComplexity: {
        threshold: 10,
        current: 8.5
    },
    codeDuplication: {
        threshold: 5, // percentage
        current: 3.2
    },
    testCoverage: {
        threshold: 80, // percentage
        current: 75
    },
    dependencies: {
        outdated: 5,
        vulnerable: 0
    }
};
```

**Refactoring Strategy:**

```javascript
// Strangler Fig Pattern - Gradually replace old code
class LegacyPaymentService {
    async processPayment(order) {
        // Old implementation
    }
}

class NewPaymentService {
    async processPayment(order) {
        // New implementation
    }
}

// Feature flag để switch
class PaymentService {
    constructor() {
        this.useNewService = process.env.USE_NEW_PAYMENT_SERVICE === 'true';
        this.legacyService = new LegacyPaymentService();
        this.newService = new NewPaymentService();
    }
  
    async processPayment(order) {
        if (this.useNewService) {
            return await this.newService.processPayment(order);
        } else {
            return await this.legacyService.processPayment(order);
        }
    }
}

// Gradual migration
// Week 1: 10% traffic to new service
// Week 2: 50% traffic
// Week 3: 100% traffic
// Week 4: Remove legacy code
```

## 6. ARCHITECTURE DECISIONS

### 6.1. Architecture Decision Records (ADR)

**ADR Template:**

```markdown
# ADR-001: Chọn Database cho User Service

## Status
Accepted

## Context
User service hiện tại đang dùng MongoDB, nhưng cần support complex queries và transactions.

## Decision
Chuyển sang PostgreSQL với Sequelize ORM.

## Consequences

### Positive
- ACID transactions
- Complex queries với JOINs
- Better data integrity
- Mature ecosystem

### Negative
- Migration effort
- Team cần học SQL
- Less flexible schema

## Alternatives Considered
1. Stay with MongoDB - Rejected vì thiếu transaction support
2. Use MySQL - Rejected vì PostgreSQL có features tốt hơn
3. Hybrid approach - Rejected vì phức tạp

## Implementation Plan
1. Setup PostgreSQL database
2. Create migration scripts
3. Dual-write period (2 weeks)
4. Migrate read traffic
5. Remove MongoDB
```

**Decision Making Framework:**

```javascript
// Decision matrix
const decisionMatrix = {
    options: ['PostgreSQL', 'MongoDB', 'MySQL'],
    criteria: {
        performance: { weight: 0.3 },
        scalability: { weight: 0.2 },
        cost: { weight: 0.2 },
        teamExpertise: { weight: 0.15 },
        ecosystem: { weight: 0.15 }
    },
    scores: {
        PostgreSQL: {
            performance: 8,
            scalability: 9,
            cost: 7,
            teamExpertise: 6,
            ecosystem: 9
        },
        MongoDB: {
            performance: 7,
            scalability: 9,
            cost: 8,
            teamExpertise: 9,
            ecosystem: 8
        },
        MySQL: {
            performance: 7,
            scalability: 7,
            cost: 9,
            teamExpertise: 8,
            ecosystem: 8
        }
    }
};

// Calculate weighted scores
function calculateScore(option) {
    let total = 0;
    for (const [criterion, weight] of Object.entries(decisionMatrix.criteria)) {
        total += decisionMatrix.scores[option][criterion] * weight.weight;
    }
    return total;
}
```

## 7. TEAM COLLABORATION

### 7.1. Effective Communication

**Code Comments và Documentation:**

```javascript
/**
 * Calculates the total price of an order including taxes and discounts.
 * 
 * @param {Object} order - The order object
 * @param {Array<Object>} order.items - Array of order items
 * @param {string} order.couponCode - Optional coupon code
 * @param {string} order.shippingAddress - Shipping address for tax calculation
 * @returns {Promise<Object>} - Object containing subtotal, tax, discount, and total
 * 
 * @example
 * const order = {
 *   items: [{ price: 100, quantity: 2 }],
 *   couponCode: 'SAVE10',
 *   shippingAddress: 'US'
 * };
 * const result = await calculateOrderTotal(order);
 * // { subtotal: 200, tax: 20, discount: 20, total: 200 }
 * 
 * @throws {Error} If order is invalid
 */
async function calculateOrderTotal(order) {
    // Implementation
}

// PR Description Template
/*
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests pass locally
*/
```

## 8. PRODUCTION READINESS CHECKLIST

**Pre-Deployment Checklist:**

```javascript
const productionReadiness = {
    code: [
        'All tests passing',
        'Code reviewed and approved',
        'No console.logs or debug code',
        'Error handling implemented',
        'Input validation added'
    ],
    security: [
        'No hardcoded secrets',
        'Dependencies scanned for vulnerabilities',
        'Authentication/Authorization implemented',
        'Rate limiting configured',
        'CORS properly configured',
        'SQL injection prevention',
        'XSS prevention'
    ],
    performance: [
        'Database indexes created',
        'Query optimization done',
        'Caching strategy implemented',
        'Image/assets optimized',
        'CDN configured',
        'Load testing completed'
    ],
    monitoring: [
        'Health check endpoint added',
        'Metrics exposed',
        'Logging configured',
        'Error tracking setup',
        'Alerting configured',
        'Runbook created'
    ],
    infrastructure: [
        'Environment variables set',
        'Database migrations run',
        'Backup strategy in place',
        'Disaster recovery plan',
        'Scaling strategy defined',
        'CI/CD pipeline working'
    ]
};
```

---

# KẾT LUẬN

Giáo trình này cung cấp một lộ trình đầy đủ và chi tiết để trở thành Senior Full Stack Developer trong 18-24 tháng.

**Lưu ý quan trọng:**

1. **Thực hành là chìa khóa**: Code mỗi ngày, không bỏ qua
2. **Build real projects**: Đừng chỉ làm tutorials
3. **LeetCode mỗi ngày**: Ít nhất 1-2 bài
4. **Code Review**: Học từ code tốt
5. **Đừng perfectionism**: Ship fast, iterate later
6. **Network**: Kết nối với developers khác
7. **Nghỉ ngơi**: Tránh burnout

**Chúc bạn thành công trên hành trình trở thành Senior Full Stack Developer! 🚀**

---

# TÀI LIỆU THAM KHẢO

## Sách

1. "Clean Code" - Robert C. Martin
2. "System Design Interview" - Alex Xu
3. "You Don't Know JS" - Kyle Simpson
4. "Eloquent JavaScript" - Marijn Haverbeke

## Websites

1. LeetCode: https://leetcode.com
2. freeCodeCamp: https://www.freecodecamp.org
3. MDN Web Docs: https://developer.mozilla.org
4. React Documentation: https://react.dev
5. Node.js Documentation: https://nodejs.org/docs

## Video Courses

1. freeCodeCamp Full Stack courses
2. Traversy Media
3. The Net Ninja
4. NeetCode (Algorithms)

---

**Lưu ý:** Đây là phần đầu của giáo trình. Các phần còn lại (Mobile Development, Advanced Topics, Portfolio) sẽ được mở rộng tương tự với cùng mức độ chi tiết.

---

# PHẦN GIẢI THÍCH CHI TIẾT VÀ NOTES

> Phần này cung cấp giải thích sâu và chi tiết về các concepts quan trọng, giúp bạn hiểu rõ "Tại sao", "Khi nào", và "Như thế nào" của từng kiến thức.

---

## JAVASCRIPT - GIẢI THÍCH SÂU

### 1. CLOSURES - Hiểu Sâu

#### Giải thích chi tiết:

**Closure là gì?**
Closure là khả năng của một function bên trong (inner function) có thể truy cập và "nhớ" các biến của function bên ngoài (outer function) ngay cả sau khi outer function đã thực thi xong.

**Tại sao Closure quan trọng?**

- **Data Privacy**: Tạo private variables trong JavaScript (vì JS không có private như Java/C++)
- **Function Factories**: Tạo functions động với behavior khác nhau
- **Event Handlers**: Giữ context khi xử lý events
- **Module Pattern**: Tạo modules với public/private API

**Cơ chế hoạt động:**

```javascript
function outerFunction(x) {
    // Biến này thuộc về outer function's scope
    const outerVariable = x;
  
    // Inner function tạo closure
    function innerFunction(y) {
        // Inner function có thể truy cập outerVariable
        // Ngay cả khi outerFunction đã return
        console.log(outerVariable + y);
    }
  
    // Return inner function (không gọi nó)
    return innerFunction;
}

const addFive = outerFunction(5);
// Lúc này outerFunction đã thực thi xong
// Nhưng addFive vẫn "nhớ" outerVariable = 5

addFive(10); // 15
// innerFunction vẫn có thể truy cập outerVariable!
```

**Lưu ý quan trọng:**

- Closure giữ reference đến biến, không phải giá trị
- Nếu biến thay đổi, closure sẽ thấy giá trị mới
- Closure có thể gây memory leak nếu không cẩn thận

**Ví dụ thực tế - Memory Leak:**

```javascript
// ❌ Bad: Memory leak với closures
function attachHandlers() {
    const buttons = document.querySelectorAll('button');
  
    buttons.forEach((button, index) => {
        button.addEventListener('click', () => {
            // Closure giữ reference đến buttons array
            // buttons array không bao giờ được garbage collected!
            console.log(`Button ${index} clicked`);
        });
    });
}

// ✅ Good: Không giữ reference không cần thiết
function attachHandlers() {
    const buttons = document.querySelectorAll('button');
  
    buttons.forEach((button, index) => {
        // Chỉ giữ index (primitive value), không giữ buttons array
        button.addEventListener('click', function() {
            console.log(`Button ${index} clicked`);
        });
    });
  
    // Hoặc remove listeners khi không cần
    buttons.forEach(button => {
        button.removeEventListener('click', handler);
    });
}
```

**Use Cases thực tế:**

1. **Module Pattern:**

```javascript
const UserModule = (function() {
    // Private variables (không thể truy cập từ bên ngoài)
    let users = [];
    let nextId = 1;
  
    // Private function
    function validateUser(user) {
        return user.name && user.email;
    }
  
    // Public API (return object với methods)
    return {
        addUser(user) {
            if (validateUser(user)) {
                users.push({ ...user, id: nextId++ });
                return true;
            }
            return false;
        },
      
        getUsers() {
            // Return copy để không thể modify trực tiếp
            return [...users];
        },
      
        getUserCount() {
            return users.length;
        }
    };
})();

// Usage
UserModule.addUser({ name: 'John', email: 'john@example.com' });
console.log(UserModule.getUsers()); // [{ id: 1, name: 'John', ... }]
// console.log(UserModule.users); // undefined - private!
```

2. **Function Factory:**

```javascript
function createMultiplier(multiplier) {
    // Closure giữ multiplier
    return function(number) {
        return number * multiplier;
    };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15

// Mỗi function có multiplier riêng được "đóng gói" trong closure
```

3. **Debounce/Throttle:**

```javascript
function debounce(func, delay) {
    let timeoutId; // Closure giữ timeoutId
  
    return function(...args) {
        // Clear timeout cũ
        clearTimeout(timeoutId);
      
        // Set timeout mới
        timeoutId = setTimeout(() => {
            func.apply(this, args);
        }, delay);
    };
}

const debouncedSearch = debounce((query) => {
    console.log('Searching for:', query);
}, 300);

// Mỗi lần gọi, nó reset timer
// Chỉ execute sau khi user ngừng gõ 300ms
```

---

### 2. THIS BINDING - Hiểu Sâu

#### Giải thích chi tiết:

**this là gì?**
`this` là một keyword đặc biệt trong JavaScript, nó trỏ đến object đang thực thi function hiện tại. Giá trị của `this` được xác định bởi cách function được gọi, không phải nơi nó được định nghĩa.

**4 Quy tắc xác định this (theo thứ tự ưu tiên):**

1. **New Binding** (new keyword)
2. **Explicit Binding** (call, apply, bind)
3. **Implicit Binding** (object method)
4. **Default Binding** (global/window)

**Chi tiết từng quy tắc:**

**1. New Binding:**

```javascript
function Person(name) {
    // this = {} (object mới được tạo)
    this.name = name;
    // return this (implicit)
}

const john = new Person('John');
// this trong Person trỏ đến john object
console.log(john.name); // "John"
```

**2. Explicit Binding:**

```javascript
function greet() {
    return `Hello, ${this.name}`;
}

const person = { name: 'John' };

// call - gọi function với this cụ thể
greet.call(person); // "Hello, John"

// apply - giống call nhưng arguments là array
greet.apply(person); // "Hello, John"

// bind - tạo function mới với this cố định
const greetJohn = greet.bind(person);
greetJohn(); // "Hello, John"
```

**3. Implicit Binding:**

```javascript
const person = {
    name: 'John',
    greet() {
        // this trỏ đến person (object gọi method)
        return `Hello, ${this.name}`;
    }
};

person.greet(); // "Hello, John"
// this = person
```

**4. Default Binding:**

```javascript
function greet() {
    // this = global object (window trong browser, global trong Node.js)
    console.log(this); // Window object
    return `Hello, ${this.name}`;
}

greet(); // "Hello, undefined" (nếu window.name không tồn tại)
```

**Arrow Functions và this:**

```javascript
// Arrow functions KHÔNG có this riêng
// this trong arrow function = this của scope bên ngoài (lexical this)

const person = {
    name: 'John',
  
    // Regular function - this thay đổi
    greetRegular: function() {
        setTimeout(function() {
            // this = global (vì setTimeout gọi function)
            console.log(this.name); // undefined
        }, 100);
    },
  
    // Arrow function - this giữ nguyên
    greetArrow: function() {
        setTimeout(() => {
            // this = person (lexical this từ greetArrow)
            console.log(this.name); // "John"
        }, 100);
    }
};
```

**Lưu ý quan trọng:**

- Arrow functions không thể dùng làm constructor (không có this riêng)
- Arrow functions không thể bind this (call/apply/bind không work)
- Arrow functions không có arguments object

**Common Mistakes:**

**Mistake 1: Losing this trong callbacks**

```javascript
// ❌ Bad
const button = {
    text: 'Click me',
    click() {
        setTimeout(function() {
            console.log(this.text); // undefined - this = global
        }, 100);
    }
};

// ✅ Fix 1: Arrow function
const button = {
    text: 'Click me',
    click() {
        setTimeout(() => {
            console.log(this.text); // "Click me"
        }, 100);
    }
};

// ✅ Fix 2: Bind
const button = {
    text: 'Click me',
    click() {
        setTimeout(function() {
            console.log(this.text);
        }.bind(this), 100);
    }
};

// ✅ Fix 3: Store this
const button = {
    text: 'Click me',
    click() {
        const self = this;
        setTimeout(function() {
            console.log(self.text);
        }, 100);
    }
};
```

---

### 3. PROMISES VÀ ASYNC/AWAIT - Hiểu Sâu

#### Giải thích chi tiết:

**Tại sao cần Promises?**

- **Callback Hell**: Callbacks lồng nhau khó đọc và maintain
- **Error Handling**: Khó xử lý lỗi với callbacks
- **Parallel Execution**: Khó chạy nhiều async operations song song

**Promise States:**

1. **Pending**: Chưa hoàn thành
2. **Fulfilled**: Thành công (resolve)
3. **Rejected**: Thất bại (reject)

**Promise Chain:**

```javascript
fetch('/api/user')
    .then(response => {
        // Return value trở thành argument của then tiếp theo
        return response.json();
    })
    .then(user => {
        // user là kết quả của response.json()
        return fetch(`/api/posts/${user.id}`);
    })
    .then(response => response.json())
    .then(posts => {
        console.log(posts);
    })
    .catch(error => {
        // Bắt tất cả errors trong chain
        console.error(error);
    });
```

**Async/Await - Syntactic Sugar:**

```javascript
// Async/await làm code trông như synchronous
async function getUserPosts() {
    try {
        const response = await fetch('/api/user');
        const user = await response.json();
        const postsResponse = await fetch(`/api/posts/${user.id}`);
        const posts = await postsResponse.json();
        return posts;
    } catch (error) {
        // Xử lý tất cả errors
        console.error(error);
        throw error;
    }
}
```

**Lưu ý quan trọng:**

- `async function` luôn return Promise
- `await` chỉ dùng trong `async function`
- `await` pause execution cho đến khi Promise resolve
- Errors trong async function được wrap trong rejected Promise

**Parallel Execution:**

```javascript
// ❌ Sequential (chậm)
async function fetchSequential() {
    const user = await fetch('/api/user');
    const posts = await fetch('/api/posts');
    const comments = await fetch('/api/comments');
    // Tổng thời gian = sum của 3 requests
}

// ✅ Parallel (nhanh)
async function fetchParallel() {
    const [user, posts, comments] = await Promise.all([
        fetch('/api/user'),
        fetch('/api/posts'),
        fetch('/api/comments')
    ]);
    // Tổng thời gian = max của 3 requests
}
```

---

## DATABASE - GIẢI THÍCH SÂU

### 1. INDEXES - Hiểu Sâu

#### Giải thích chi tiết:

**Index là gì?**
Index là cấu trúc dữ liệu giúp database tìm kiếm nhanh hơn, tương tự như index trong sách giúp tìm trang nhanh hơn.

**Cơ chế hoạt động:**

```
Không có index:
- Database phải scan toàn bộ table (Sequential Scan)
- Với 1M rows: Phải đọc 1M rows
- Time: O(n)

Có index:
- Database dùng B-Tree để tìm kiếm
- Với 1M rows: Chỉ đọc ~20 nodes (log2(1M) ≈ 20)
- Time: O(log n)
```

**B-Tree Index Structure:**

```
        [50]
       /    \
   [25]      [75]
   /  \      /  \
[10][30]  [60][90]

- Root node: Giá trị giữa
- Left child: < root
- Right child: > root
- Tìm kiếm: O(log n)
```

**Khi nào cần Index:**

- ✅ Columns thường dùng trong WHERE
- ✅ Columns dùng trong JOIN
- ✅ Columns dùng trong ORDER BY
- ❌ Columns ít query
- ❌ Tables nhỏ (< 1000 rows)
- ❌ Columns thay đổi thường xuyên (trade-off)

**Composite Index - Order Matters:**

```sql
CREATE INDEX idx_status_created ON users(status, created_at DESC);

-- ✅ Good: Dùng được index
WHERE status = 'active' ORDER BY created_at DESC
WHERE status = 'active' AND created_at > '2024-01-01'

-- ❌ Bad: Không dùng được index hiệu quả
WHERE created_at > '2024-01-01'  -- Phải scan toàn bộ index
ORDER BY created_at DESC          -- Không dùng được index
```

**Lý do:** Index được sắp xếp theo (status, created_at). Nếu không có status, database không thể dùng index hiệu quả.

**Index Selectivity:**

```sql
-- Low selectivity (nhiều duplicate values)
CREATE INDEX idx_gender ON users(gender);
-- gender chỉ có 'M' hoặc 'F' -> Index không hiệu quả

-- High selectivity (ít duplicate)
CREATE INDEX idx_email ON users(email);
-- email unique -> Index rất hiệu quả
```

**Trade-offs:**

- ✅ **Pros**: Tăng tốc đọc (SELECT)
- ❌ **Cons**:
  - Tốn storage space
  - Chậm INSERT/UPDATE/DELETE (phải update index)
  - Tốn memory khi load index

---

### 2. QUERY OPTIMIZATION - Hiểu Sâu

#### EXPLAIN Plan - Đọc như Senior:

```sql
EXPLAIN ANALYZE
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.name;
```

**Đọc kết quả:**

```
Hash Left Join  (cost=1000.00..2000.00 rows=1000 width=64) (actual time=10.123..50.456 rows=500 loops=1)
  Hash Cond: (o.user_id = u.id)
  ->  Seq Scan on orders o  (cost=0.00..500.00 rows=10000 width=8) (actual time=0.123..5.456 rows=10000 loops=1)
  ->  Hash  (cost=800.00..800.00 rows=1000 width=64) (actual time=8.123..8.123 rows=1000 loops=1)
        ->  Index Scan using idx_users_created on users u  (cost=0.00..800.00 rows=1000 width=64) (actual time=0.123..5.456 rows=1000 loops=1)
              Index Cond: (created_at > '2024-01-01'::timestamp)
```

**Giải thích:**

- **cost**: Ước tính cost (không phải thời gian thực)
- **actual time**: Thời gian thực tế (ms)
- **rows**: Số rows được scan/return
- **loops**: Số lần operation được thực hiện

**Các loại Scan:**

- **Seq Scan**: Scan toàn bộ table (chậm) ❌
- **Index Scan**: Dùng index để tìm rows ✅
- **Index Only Scan**: Chỉ đọc index, không đọc table ✅✅
- **Bitmap Heap Scan**: Dùng bitmap index ✅

**Các loại Join:**

- **Nested Loop**: Tốt cho small datasets
- **Hash Join**: Tốt cho large datasets, cần memory
- **Merge Join**: Tốt cho sorted data

---

### 3. NORMALIZATION vs DENORMALIZATION - Khi Nào Dùng?

#### Normalization (3NF):

**Ưu điểm:**

- ✅ Data integrity cao (không duplicate)
- ✅ Tiết kiệm storage
- ✅ Dễ update (chỉ update 1 chỗ)
- ✅ Phù hợp write-heavy

**Nhược điểm:**

- ❌ Cần nhiều JOINs (chậm)
- ❌ Phức tạp queries
- ❌ Không phù hợp read-heavy

**Ví dụ:**

```sql
-- Normalized
users: id, name, email
user_profiles: user_id, bio, avatar
user_addresses: user_id, street, city

-- Query cần JOIN
SELECT u.name, p.bio, a.city
FROM users u
JOIN user_profiles p ON u.id = p.user_id
JOIN user_addresses a ON u.id = a.user_id;
```

#### Denormalization:

**Ưu điểm:**

- ✅ Queries nhanh (ít JOINs)
- ✅ Đơn giản queries
- ✅ Phù hợp read-heavy

**Nhược điểm:**

- ❌ Data duplication
- ❌ Khó maintain consistency
- ❌ Tốn storage
- ❌ Update phức tạp (phải update nhiều chỗ)

**Ví dụ:**

```sql
-- Denormalized
users: id, name, email, bio, avatar, city

-- Query đơn giản
SELECT name, bio, city FROM users WHERE id = 1;
```

**Khi nào dùng gì:**

- **Normalize**: Write > Read, Data integrity quan trọng
- **Denormalize**: Read >> Write, Performance quan trọng
- **Hybrid**: Normalize cho write, Denormalize cho read (Materialized Views)

---

### 4. CONNECTION POOLING - Tại Sao Cần?

#### Vấn đề không có Pool:

```javascript
// ❌ Bad: Tạo connection mới mỗi request
app.get('/users', async (req, res) => {
    const client = new Client(); // Tạo connection mới
    await client.connect();      // Tốn thời gian (50-100ms)
    const result = await client.query('SELECT * FROM users');
    await client.end();          // Đóng connection
    res.json(result.rows);
});

// Với 1000 requests/second:
// - 1000 connections/second
// - Mỗi connection: 50ms setup + 10ms query = 60ms
// - Tổng overhead: 60 seconds/second (không thể!)
```

#### Giải pháp: Connection Pool

```javascript
// ✅ Good: Reuse connections
const pool = new Pool({ max: 20 });

app.get('/users', async (req, res) => {
    const result = await pool.query('SELECT * FROM users');
    // Connection được reuse, không cần tạo mới
    res.json(result.rows);
});

// Với 1000 requests/second:
// - Chỉ cần 20 connections
// - Mỗi query: 10ms (không có setup overhead)
// - Tổng overhead: 10ms * 1000 = 10 seconds (có thể handle!)
```

**Pool Size Calculation:**

```
Pool size = (Number of cores * 2) + Effective spindle count

Ví dụ:
- 4 cores
- 1 database (1 spindle)
- Pool size = (4 * 2) + 1 = 9

Nhưng thực tế:
- Web app: 10-20 connections
- Heavy app: 20-50 connections
- Quá nhiều: Context switching overhead
```

---

## SYSTEM DESIGN - TƯ DUY SENIOR

### 1. CACHING STRATEGIES - Khi Nào Dùng Gì?

#### Cache-Aside (Lazy Loading):

**Cơ chế:**

1. Check cache
2. Nếu miss → Query database
3. Store vào cache
4. Return data

**Khi nào dùng:**

- ✅ Data không thay đổi thường xuyên
- ✅ Có thể chấp nhận stale data
- ✅ Read-heavy workloads

**Trade-offs:**

- ✅ Đơn giản implement
- ❌ Cache miss penalty (2 trips: cache + DB)
- ❌ Có thể có stale data

#### Write-Through:

**Cơ chế:**

1. Write to database
2. Write to cache immediately
3. Return

**Khi nào dùng:**

- ✅ Cần data consistency cao
- ✅ Write không quá nhiều

**Trade-offs:**

- ✅ Data luôn consistent
- ❌ Write chậm hơn (2 writes)
- ❌ Cache có thể chứa data không được đọc

#### Write-Behind (Write-Back):

**Cơ chế:**

1. Write to cache immediately
2. Return (fast!)
3. Write to database async (background)

**Khi nào dùng:**

- ✅ Write-heavy workloads
- ✅ Có thể mất data nếu cache crash

**Trade-offs:**

- ✅ Write rất nhanh
- ❌ Risk mất data
- ❌ Phức tạp implement

---

### 2. LOAD BALANCING - Strategies

#### Round Robin:

**Cơ chế:** Request 1 → Server 1, Request 2 → Server 2, ...

**Khi nào dùng:**

- ✅ Servers có cùng capacity
- ✅ Requests đơn giản

**Trade-offs:**

- ✅ Đơn giản
- ❌ Không tính đến server load

#### Least Connections:

**Cơ chế:** Route đến server có ít connections nhất

**Khi nào dùng:**

- ✅ Long-lived connections
- ✅ Servers có capacity khác nhau

**Trade-offs:**

- ✅ Cân bằng tốt hơn
- ❌ Cần track connections

#### IP Hash (Sticky Sessions):

**Cơ chế:** Hash client IP → Route đến server cố định

**Khi nào dùng:**

- ✅ Cần session affinity
- ✅ Stateful applications

**Trade-offs:**

- ✅ Session consistency
- ❌ Không cân bằng tốt nếu IP distribution không đều

---

## PERFORMANCE OPTIMIZATION - TƯ DUY SENIOR

### 1. PREMATURE OPTIMIZATION - Khi Nào?

**Quy tắc:**

> "Premature optimization is the root of all evil" - Donald Knuth

**Nhưng khi nào thì optimize?**

**✅ Optimize khi:**

- Có metrics chứng minh bottleneck
- Performance issue ảnh hưởng user experience
- Scalability requirements rõ ràng

**❌ Không optimize khi:**

- Chưa có data/metrics
- Code chưa hoạt động đúng
- "Có thể sẽ chậm" (speculation)

**Process:**

1. **Measure**: Profile và identify bottlenecks
2. **Optimize**: Fix bottlenecks
3. **Measure again**: Verify improvement
4. **Repeat**: Nếu cần

---

### 2. DATABASE SHARDING - Khi Nào Cần?

**Sharding là gì?**
Chia database thành nhiều shards nhỏ hơn, mỗi shard chứa subset của data.

**Khi nào cần:**

- ✅ Database quá lớn (> 100GB)
- ✅ Single server không đủ capacity
- ✅ Queries chậm dù đã optimize

**Khi nào không cần:**

- ❌ Database < 10GB
- ❌ Có thể scale vertical
- ❌ Queries cần JOIN across shards

**Sharding Strategies:**

**1. Range-based:**

```
Shard 1: user_id 1-1000
Shard 2: user_id 1001-2000
```

- ✅ Đơn giản
- ❌ Hot spots (một shard có thể quá tải)

**2. Hash-based:**

```
Shard = hash(user_id) % num_shards
```

- ✅ Cân bằng tốt
- ❌ Khó re-sharding

**3. Directory-based:**

```
Lookup table: user_id → shard
```

- ✅ Flexible
- ❌ Single point of failure

---

## PHỤ LỤC: MẪU CODE BACKEND (PYTHON) & FRONTEND (REACT/VUE)

### BACKEND (Python - FastAPI/Django)

#### 1) Auth JWT + Refresh (FastAPI)

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt, time

SECRET = "supersecret"
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
app = FastAPI()

def create_tokens(user_id: int):
    now = int(time.time())
    access = jwt.encode({"sub": user_id, "exp": now + 3600}, SECRET, algorithm="HS256")
    refresh = jwt.encode({"sub": user_id, "exp": now + 3600 * 24 * 30}, SECRET, algorithm="HS256")
    return access, refresh

def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/login")
def login():
    # TODO: verify user/password
    access, refresh = create_tokens(user_id=1)
    return {"access": access, "refresh": refresh}

@app.post("/refresh")
def refresh_token(refresh: str):
    payload = decode_token(refresh)
    access, _ = create_tokens(payload["sub"])
    return {"access": access}

@app.get("/me")
def me(token: str = Depends(oauth2)):
    payload = decode_token(token)
    return {"user_id": payload["sub"]}
```

#### 2) Pagination chuẩn REST

```python
from fastapi import Query

@app.get("/items")
async def list_items(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
):
    offset = (page - 1) * limit
    rows = await db.fetch("SELECT * FROM items ORDER BY id LIMIT $1 OFFSET $2", limit, offset)
    total = await db.fetchval("SELECT COUNT(*) FROM items")
    return {
        "data": rows,
        "pagination": {
            "page": page,
            "limit": limit,
            "total": total,
            "pages": (total + limit - 1) // limit
        }
    }
```

#### 3) Cursor-based pagination (hiệu năng cao)

```python
@app.get("/items/cursor")
async def list_items(cursor: int | None = None, limit: int = 20):
    if cursor:
        rows = await db.fetch(
            "SELECT * FROM items WHERE id > $1 ORDER BY id LIMIT $2",
            cursor, limit
        )
    else:
        rows = await db.fetch("SELECT * FROM items ORDER BY id LIMIT $1", limit)

    next_cursor = rows[-1]["id"] if rows and len(rows) == limit else None
    return {"data": rows, "next_cursor": next_cursor, "has_more": next_cursor is not None}
```

#### 4) Upload file + validate (FastAPI)

```python
from fastapi import File, UploadFile

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if file.content_type not in {"image/png", "image/jpeg"}:
        raise HTTPException(status_code=400, detail="Only images allowed")
    content = await file.read()
    if len(content) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Max 5MB")
    # Save file...
    return {"ok": True}
```

#### 5) Background task + retry (Celery)

```python
from celery import Celery

celery = Celery(__name__, broker="redis://localhost:6379/0")

@celery.task(bind=True, max_retries=3, default_retry_delay=5)
def send_email(self, to, subject, body):
    try:
        # call email service
        pass
    except Exception as exc:
        raise self.retry(exc=exc)
```

#### 6) Caching với Redis + TTL

```python
import aioredis, json

redis = aioredis.from_url("redis://localhost:6379", decode_responses=True)

async def get_user(user_id: int):
    key = f"user:{user_id}"
    cached = await redis.get(key)
    if cached:
        return json.loads(cached)

    user = await db.fetchrow("SELECT * FROM users WHERE id=$1", user_id)
    if user:
        await redis.set(key, json.dumps(dict(user)), ex=3600)
    return user
```

### FRONTEND (React)

#### 1) Data fetching + caching (react-query)

```tsx
import { useQuery } from "@tanstack/react-query";

async function fetchUsers() {
  const res = await fetch("/api/users");
  if (!res.ok) throw new Error("Failed");
  return res.json();
}

export function Users() {
  const { data, isLoading, error, refetch } = useQuery(["users"], fetchUsers, {
    staleTime: 60_000,
    retry: 2,
  });
  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error</div>;
  return (
    <div>
      <button onClick={() => refetch()}>Refresh</button>
      {data?.map((u: any) => (
        <div key={u.id}>{u.name}</div>
      ))}
    </div>
  );
}
```

#### 2) Form validation (React Hook Form + Zod)

```tsx
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
});

export function LoginForm() {
  const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm({
    resolver: zodResolver(schema),
  });

  const onSubmit = handleSubmit(async (data) => {
    await fetch("/api/login", { method: "POST", body: JSON.stringify(data) });
  });

  return (
    <form onSubmit={onSubmit}>
      <input {...register("email")} placeholder="Email" />
      {errors.email && <span>{errors.email.message}</span>}
      <input type="password" {...register("password")} placeholder="Password" />
      {errors.password && <span>{errors.password.message}</span>}
      <button disabled={isSubmitting}>Login</button>
    </form>
  );
}
```

#### 3) Infinite scroll (IntersectionObserver)

```tsx
import { useEffect, useRef } from "react";

export function InfiniteList({ loadMore, hasMore }: any) {
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (!ref.current) return;
    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting && hasMore) loadMore();
    }, { threshold: 0.5 });
    observer.observe(ref.current);
    return () => observer.disconnect();
  }, [hasMore, loadMore]);

  return <div ref={ref} style={{ height: 1 }} />;
}
```

#### 4) File upload với progress

```tsx
export async function upload(file: File, onProgress: (p: number) => void) {
  const form = new FormData();
  form.append("file", file);
  return fetch("/api/upload", {
    method: "POST",
    body: form,
  });
}
```

### FRONTEND (Vue 3 + Composition API)

#### 1) Fetch + state

```ts
import { ref, onMounted } from "vue";

export default {
  setup() {
    const users = ref([]);
    const loading = ref(true);

    const load = async () => {
      loading.value = true;
      const res = await fetch("/api/users");
      users.value = await res.json();
      loading.value = false;
    };

    onMounted(load);
    return { users, loading, load };
  },
};
```

#### 2) Form validation (VeeValidate + Yup)

```ts
import { useForm, useField } from "vee-validate";
import * as yup from "yup";

const schema = yup.object({
  email: yup.string().email().required(),
  password: yup.string().min(8).required(),
});

export default {
  setup() {
    const { handleSubmit, errors } = useForm({ validationSchema: schema });
    const { value: email } = useField("email");
    const { value: password } = useField("password");

    const onSubmit = handleSubmit(async (values) => {
      await fetch("/api/login", { method: "POST", body: JSON.stringify(values) });
    });

    return { email, password, errors, onSubmit };
  },
};
```

#### 3) Debounce search

```ts
import { ref, watch } from "vue";

const query = ref("");
const results = ref([]);
let timeout: any;

watch(query, (val) => {
  clearTimeout(timeout);
  timeout = setTimeout(async () => {
    const res = await fetch(`/api/search?q=${encodeURIComponent(val)}`);
    results.value = await res.json();
  }, 300);
});
```

#### 4) WebSocket (native)

```ts
import { ref, onMounted, onBeforeUnmount } from "vue";

export default {
  setup() {
    const messages = ref<string[]>([]);
    let ws: WebSocket;

    onMounted(() => {
      ws = new WebSocket("ws://localhost:8080");
      ws.onmessage = (e) => messages.value.push(e.data);
    });

    onBeforeUnmount(() => ws?.close());
    return { messages };
  },
};
```

---

## BẢNG SO SÁNH NHANH & GHI CHÚ TỐI ƯU (TỔNG HỢP)

### BẢNG ĐỊNH NGHĨA NGẮN (TRA CỨU NHANH)

- **Callback**: Hàm được truyền vào hàm khác và được gọi lại khi xong việc.
- **Promise**: Giá trị đại diện cho kết quả bất đồng bộ (pending → fulfilled/rejected).
- **Async/Await**: Cú pháp sugar trên Promise giúp code bất đồng bộ nhìn như đồng bộ.
- **Closure**: Hàm con nhớ và truy cập được biến của hàm cha sau khi hàm cha chạy xong.
- **this (JS)**: Tham chiếu đến object đang thực thi; xác định bởi cách gọi (new / call|apply|bind / implicit / default).
- **Hoisting**: Khai báo (var/function) được nâng lên đầu scope trước khi thực thi.
- **Debounce**: Trì hoãn thực thi cho đến khi người dùng ngừng thao tác một khoảng thời gian.
- **Throttle**: Giới hạn số lần thực thi trong một khoảng thời gian.
- **Normalization (DB)**: Tổ chức dữ liệu để giảm trùng lặp, tăng nhất quán (3NF).
- **Denormalization (DB)**: Cố ý trùng lặp để giảm JOIN, tăng tốc đọc.
- **Index (DB)**: Cấu trúc dữ liệu (thường B-Tree) giúp tìm kiếm nhanh (O(log n)).
- **Composite Index**: Index trên nhiều cột; thứ tự cột quan trọng (prefix rule).
- **Partial Index**: Index một phần dữ liệu thỏa điều kiện (WHERE).
- **Covering Index**: Index chứa đủ cột SELECT, cho phép Index Only Scan.
- **Seq Scan**: Quét toàn bảng; chậm với bảng lớn.
- **N+1 Query**: 1 query lấy danh sách + N query con cho từng phần tử → nhiều round-trip.
- **Cursor Pagination**: Phân trang dựa trên con trỏ (id/created_at) thay vì OFFSET.
- **Connection Pool**: Tái sử dụng kết nối DB, tránh overhead tạo/đóng connection mỗi request.
- **Cache-Aside**: Miss → lấy DB → ghi cache → trả về; đơn giản, dễ stale.
- **Write-Through**: Ghi DB và cache cùng lúc; consistent, chậm hơn khi write.
- **Write-Behind**: Ghi cache, trả về; ghi DB async; rất nhanh, rủi ro mất dữ liệu.
- **Materialized View**: View được lưu vật lý; cần REFRESH để cập nhật.
- **Sharding**: Chia dữ liệu thành nhiều shard để scale ngang.
- **JWT**: JSON Web Token; access/refresh token cho auth stateless.
- **CSR/SSR/SSG**: Client-side render / Server-side render / Static site generation.
- **SPA**: Single Page Application; render phía client, chuyển trang không reload toàn bộ.
- **CSR Caching (React Query/SWR)**: Lưu cache client cho API, tối ưu fetch và UX.
- **Blue/Green, Canary**: Chiến lược deploy an toàn, có rollback nhanh.

### 1. Bất đồng bộ JavaScript

- **Callback**: đơn giản nhưng dễ “callback hell”; khó bắt lỗi/chạy song song.
- **Promise**: chain `.then/.catch`, có `Promise.all`; code gọn hơn callback.
- **Async/Await**: sugar trên Promise, dễ đọc/try-catch; vẫn nên dùng `Promise.all` cho song song; tránh `await` trong loop nếu muốn song song.

### 2. Khai báo biến

- **var**: function-scope, hoisting; dễ bug → tránh.
- **let**: block-scope, dùng khi cần thay đổi.
- **const**: block-scope, mặc định dùng; chỉ đổi sang let khi cần reassign.

### 3. Normalization vs Denormalization (DB)

- **Normalize (3NF)**: integrity cao, tiết kiệm storage; phù hợp write-heavy; read nhiều JOIN → chậm.
- **Denormalize**: đọc nhanh, ít JOIN; phù hợp read-heavy; trùng lặp, dễ lệch data; update phức tạp.
- **Best practice**: thiết kế normalize, denormalize (materialized view/cache) khi có bottleneck đọc.

### 4. Pagination

- **OFFSET**: dễ nhảy tới page N; OFFSET lớn → chậm, không ổn định khi data thay đổi.
- **Cursor**: hiệu năng ổn định, phù hợp infinite scroll/big data; không nhảy page N truyền thống; cần cột cursor tăng dần/unique.

### 5. Caching Patterns

- **Cache-Aside**: đơn giản, cache chỉ chứa data đọc; miss penalty, có thể stale.
- **Write-Through**: consistent, cache luôn mới; mỗi write = 2 lần ghi.
- **Write-Behind**: write rất nhanh; rủi ro mất dữ liệu nếu cache chết; logic phức tạp.
- **Chọn**: web app thường → cache-aside; cần nhất quán → write-through; write-heavy & chấp nhận rủi ro → write-behind.

### 6. Indexing (DB)

- **Single**: cho cột hay lọc một mình.
- **Composite**: theo thứ tự prefix (a,b) → WHERE a AND b dùng tốt; WHERE b đơn lẻ không.
- **Partial**: index subset (vd. status='active') tiết kiệm space, nhanh.
- **Covering**: index chứa đủ cột SELECT → Index Only Scan.
- **Lưu ý**: quá nhiều index làm INSERT/UPDATE/DELETE chậm.

### 7. EXPLAIN / Query Plan (DB)

- Ưu tiên: Index Scan / Index Only Scan > Bitmap > Seq Scan.
- Join: small → Nested Loop; large → Hash Join; sorted data → Merge Join.
- Red flags: Seq Scan trên bảng lớn; Nested Loop với tập lớn; cost cao rows thấp.

### 8. N+1 Query Problem

- **Vấn đề**: 1 query lấy danh sách + N query cho từng phần tử.
- **Giải pháp**: JOIN một lần hoặc batch `WHERE id IN (...)`; hoặc dùng data loader/batching.

### 9. Connection Pooling (DB)

- Không pool: mỗi request mở/đóng connection → overhead lớn.
- Pool: reuse; theo dõi `waiting`, `idle=0 & total=max` để tránh cạn pool.
- Pool size thực tế: web app 10–20; heavy 20–50 (đo và điều chỉnh).

### 10. Caching Multi-level

- L1 (memory) ~0.1ms, L2 (Redis) ~1ms, DB ~10ms.
- Mục tiêu hit-rate > 80% để giảm tải DB.

### 11. Data Fetching Frontend

- **Fetch thủ công**: nhẹ, nhưng dễ lặp code, thiếu cache/retry.
- **React Query / SWR**: có cache, staleTime, retry, refetch, pagination, optimistic update → nên dùng cho app trung/lớn.

### 12. Form Validation Frontend

- **React**: React Hook Form + Zod/Yup → tối ưu re-render, schema rõ ràng.
- **Vue**: VeeValidate + Yup → dễ khai báo schema, error state rõ.

### 13. WebSocket vs Polling vs SSE

- **WebSocket**: 2 chiều, realtime chat/notification; cần giữ kết nối.
- **Polling**: đơn giản, tốn tài nguyên nếu interval ngắn.
- **SSE**: 1 chiều từ server → client, nhẹ hơn WebSocket nếu chỉ push.

### 14. Git Workflows (nhanh)

- **feature branch + PR**: chuẩn cho team; review trước merge.
- **rebase vs merge**: rebase để lịch sử phẳng; merge giữ lịch sử gốc; đã push chung → hạn chế rebase public history.
- **revert vs reset**: public branch → dùng revert; local chưa push → có thể reset.

### 15. Deployment & Rollback

- Blue/Green hoặc Canary: giảm rủi ro; luôn có kế hoạch rollback.
- Checklists: tests, migrations, env vars, monitoring, health checks.

### 16. Security Nhanh

- SQLi: luôn dùng parameterized queries/ORM.
- XSS: sanitize/escape output; CSP khi cần.
- AuthZ/AuthN: bảo vệ routes; least privilege DB users.

> Các bảng so sánh trên giúp bạn chọn nhanh “công cụ/phương án đúng” theo mục đích. Khi cần tối ưu sâu, xem lại phần “Giải thích chi tiết” và dùng EXPLAIN/metrics thực tế để quyết định.

---

## BEST PRACTICES - TỔNG HỢP

### 1. CODE REVIEW CHECKLIST

**Functionality:**

- [ ] Code hoạt động đúng requirements?
- [ ] Edge cases được handle?
- [ ] Error handling đầy đủ?

**Performance:**

- [ ] Có N+1 queries?
- [ ] Có unnecessary loops?
- [ ] Có memory leaks?

**Security:**

- [ ] SQL injection prevention?
- [ ] XSS prevention?
- [ ] Authentication/Authorization?

**Code Quality:**

- [ ] Code dễ đọc?
- [ ] Functions nhỏ và focused?
- [ ] Có comments cho complex logic?

---

### 2. DEPLOYMENT CHECKLIST

**Pre-deployment:**

- [ ] Tests pass?
- [ ] Code reviewed?
- [ ] Database migrations ready?
- [ ] Environment variables set?
- [ ] Monitoring configured?

**Post-deployment:**

- [ ] Health checks passing?
- [ ] No errors in logs?
- [ ] Performance metrics normal?
- [ ] Rollback plan ready?

---

**Lưu ý cuối:** Kiến thức này cần thực hành nhiều để thành thạo. Đọc code của senior developers, contribute to open source, và build real projects để áp dụng những concepts này!

---
