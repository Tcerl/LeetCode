# HƯỚNG DẪN CHI TIẾT VỀ HÀM PYTHON, FLASK VÀ DJANGO
================================================================

## MỤC LỤC
1. [Hàm Built-in Quan Trọng của Python](#1-hàm-built-in-quan-trọng-của-python)
2. [Kiến Thức Về Hàm Trong Python](#2-kiến-thức-về-hàm-trong-python)
3. [Các Hàm Quan Trọng Trong Flask](#3-các-hàm-quan-trọng-trong-flask)
4. [Các Hàm Quan Trọng Trong Django](#4-các-hàm-quan-trọng-trong-django)

---

## 1. HÀM BUILT-IN QUAN TRỌNG CỦA PYTHON

### 1.1. Hàm Xử Lý Chuỗi (String Functions)

#### `len()`
**Mô tả**: Trả về độ dài của một đối tượng (chuỗi, list, tuple, dict, etc.)

**Cú pháp**: `len(object)`

**Ví dụ**:
```python
# Với chuỗi
text = "Hello World"
print(len(text))  # Output: 11

# Với list
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # Output: 5

# Với dict
person = {"name": "John", "age": 30}
print(len(person))  # Output: 2
```

#### `str()`
**Mô tả**: Chuyển đổi một đối tượng thành chuỗi

**Cú pháp**: `str(object)`

**Ví dụ**:
```python
number = 123
text = str(number)
print(text)  # Output: "123"
print(type(text))  # Output: <class 'str'>

# Với list
my_list = [1, 2, 3]
print(str(my_list))  # Output: "[1, 2, 3]"
```

#### `format()`
**Mô tả**: Định dạng chuỗi với các giá trị

**Cú pháp**: `str.format(*args, **kwargs)`

**Ví dụ**:
```python
# Cách 1: Vị trí
name = "John"
age = 30
text = "Tên: {}, Tuổi: {}".format(name, age)
print(text)  # Output: "Tên: John, Tuổi: 30"

# Cách 2: Tên biến
text = "Tên: {name}, Tuổi: {age}".format(name="John", age=30)

# Cách 3: f-string (Python 3.6+)
text = f"Tên: {name}, Tuổi: {age}"

# Định dạng số
pi = 3.14159
print(f"Pi = {pi:.2f}")  # Output: "Pi = 3.14"
```

#### `split()`
**Mô tả**: Chia chuỗi thành list dựa trên delimiter

**Cú pháp**: `str.split(sep=None, maxsplit=-1)`

**Ví dụ**:
```python
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']

# Với khoảng trắng
sentence = "Hello World Python"
words = sentence.split()
print(words)  # Output: ['Hello', 'World', 'Python']

# Giới hạn số lần split
text = "a,b,c,d"
result = text.split(",", maxsplit=2)
print(result)  # Output: ['a', 'b', 'c,d']
```

#### `join()`
**Mô tả**: Nối các phần tử của iterable thành một chuỗi

**Cú pháp**: `str.join(iterable)`

**Ví dụ**:
```python
words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print(sentence)  # Output: "Hello World Python"

# Với dấu phẩy
fruits = ["apple", "banana", "orange"]
text = ", ".join(fruits)
print(text)  # Output: "apple, banana, orange"
```

#### `strip()`, `lstrip()`, `rstrip()`
**Mô tả**: Loại bỏ khoảng trắng hoặc ký tự ở đầu/cuối chuỗi

**Cú pháp**: 
- `str.strip([chars])` - Loại bỏ cả đầu và cuối
- `str.lstrip([chars])` - Loại bỏ đầu
- `str.rstrip([chars])` - Loại bỏ cuối

**Ví dụ**:
```python
text = "  Hello World  "
print(text.strip())  # Output: "Hello World"
print(text.lstrip())  # Output: "Hello World  "
print(text.rstrip())  # Output: "  Hello World"

# Loại bỏ ký tự cụ thể
text = "!!!Hello!!!"
print(text.strip("!"))  # Output: "Hello"
```

#### `replace()`
**Mô tả**: Thay thế một phần của chuỗi

**Cú pháp**: `str.replace(old, new, count=-1)`

**Ví dụ**:
```python
text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text)  # Output: "Hello Python"

# Thay thế nhiều lần
text = "apple apple apple"
new_text = text.replace("apple", "orange", 2)
print(new_text)  # Output: "orange orange apple"
```

#### `find()`, `index()`
**Mô tả**: Tìm vị trí của chuỗi con trong chuỗi

**Cú pháp**: 
- `str.find(sub, start, end)` - Trả về -1 nếu không tìm thấy
- `str.index(sub, start, end)` - Ném exception nếu không tìm thấy

**Ví dụ**:
```python
text = "Hello World"
print(text.find("World"))  # Output: 6
print(text.find("Python"))  # Output: -1

print(text.index("World"))  # Output: 6
# print(text.index("Python"))  # ValueError: substring not found
```

#### `upper()`, `lower()`, `title()`, `capitalize()`
**Mô tả**: Chuyển đổi chữ hoa/chữ thường

**Ví dụ**:
```python
text = "hello world"
print(text.upper())  # Output: "HELLO WORLD"
print(text.lower())  # Output: "hello world"
print(text.title())  # Output: "Hello World"
print(text.capitalize())  # Output: "Hello world"
```

---

### 1.2. Hàm Xử Lý List/Tuple

#### `list()`, `tuple()`
**Mô tả**: Chuyển đổi iterable thành list hoặc tuple

**Ví dụ**:
```python
# Từ string
text = "hello"
char_list = list(text)
print(char_list)  # Output: ['h', 'e', 'l', 'l', 'o']

# Từ range
numbers = list(range(5))
print(numbers)  # Output: [0, 1, 2, 3, 4]

# Từ tuple
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]
```

#### `append()`, `extend()`, `insert()`
**Mô tả**: Thêm phần tử vào list

**Ví dụ**:
```python
# append() - Thêm một phần tử vào cuối
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'orange']

# extend() - Thêm nhiều phần tử
fruits.extend(["grape", "mango"])
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape', 'mango']

# insert() - Chèn phần tử tại vị trí
fruits.insert(1, "kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'orange', 'grape', 'mango']
```

#### `remove()`, `pop()`, `clear()`
**Mô tả**: Xóa phần tử khỏi list

**Ví dụ**:
```python
fruits = ["apple", "banana", "orange"]

# remove() - Xóa phần tử đầu tiên tìm thấy
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'orange']

# pop() - Xóa và trả về phần tử tại index
last = fruits.pop()
print(last)  # Output: "orange"
print(fruits)  # Output: ['apple']

first = fruits.pop(0)
print(first)  # Output: "apple"

# clear() - Xóa tất cả
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)  # Output: []
```

#### `sort()`, `sorted()`
**Mô tả**: Sắp xếp list

**Ví dụ**:
```python
# sort() - Sắp xếp tại chỗ (in-place)
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]

# sorted() - Trả về list mới đã sắp xếp
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]
print(numbers)  # Output: [3, 1, 4, 1, 5, 9, 2] (không đổi)

# Sắp xếp ngược
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 5, 4, 3, 2, 1, 1]

# Sắp xếp với key
students = [("John", 25), ("Jane", 20), ("Bob", 30)]
students.sort(key=lambda x: x[1])  # Sắp xếp theo tuổi
print(students)  # Output: [('Jane', 20), ('John', 25), ('Bob', 30)]
```

#### `reverse()`, `reversed()`
**Mô tả**: Đảo ngược thứ tự

**Ví dụ**:
```python
# reverse() - Đảo ngược tại chỗ
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]

# reversed() - Trả về iterator đảo ngược
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)  # Output: [5, 4, 3, 2, 1]
```

#### `count()`, `index()`
**Mô tả**: Đếm và tìm vị trí phần tử

**Ví dụ**:
```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# count() - Đếm số lần xuất hiện
print(numbers.count(2))  # Output: 3

# index() - Tìm vị trí đầu tiên
print(numbers.index(2))  # Output: 1
print(numbers.index(2, 2))  # Output: 3 (bắt đầu từ index 2)
```

---

### 1.3. Hàm Xử Lý Dictionary

#### `dict()`
**Mô tả**: Tạo dictionary mới

**Ví dụ**:
```python
# Từ list of tuples
person = dict([("name", "John"), ("age", 30)])
print(person)  # Output: {'name': 'John', 'age': 30}

# Từ keyword arguments
person = dict(name="John", age=30)
print(person)  # Output: {'name': 'John', 'age': 30}
```

#### `get()`
**Mô tả**: Lấy giá trị theo key, trả về default nếu không tồn tại

**Cú pháp**: `dict.get(key, default=None)`

**Ví dụ**:
```python
person = {"name": "John", "age": 30}

# Sử dụng get()
age = person.get("age")
print(age)  # Output: 30

# Key không tồn tại
city = person.get("city", "Unknown")
print(city)  # Output: "Unknown"

# So sánh với cách thông thường
# person["city"]  # KeyError
# person.get("city")  # None (an toàn hơn)
```

#### `keys()`, `values()`, `items()`
**Mô tả**: Lấy keys, values, hoặc items của dictionary

**Ví dụ**:
```python
person = {"name": "John", "age": 30, "city": "Hanoi"}

# keys()
print(list(person.keys()))  # Output: ['name', 'age', 'city']

# values()
print(list(person.values()))  # Output: ['John', 30, 'Hanoi']

# items()
print(list(person.items()))  # Output: [('name', 'John'), ('age', 30), ('city', 'Hanoi')]

# Duyệt qua items
for key, value in person.items():
    print(f"{key}: {value}")
```

#### `update()`
**Mô tả**: Cập nhật dictionary với các cặp key-value mới

**Ví dụ**:
```python
person = {"name": "John", "age": 30}
person.update({"age": 31, "city": "Hanoi"})
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'Hanoi'}

# Hoặc
person.update(age=32, country="Vietnam")
print(person)  # Output: {'name': 'John', 'age': 32, 'city': 'Hanoi', 'country': 'Vietnam'}
```

#### `pop()`, `popitem()`
**Mô tả**: Xóa và trả về phần tử

**Ví dụ**:
```python
person = {"name": "John", "age": 30, "city": "Hanoi"}

# pop() - Xóa key cụ thể
age = person.pop("age")
print(age)  # Output: 30
print(person)  # Output: {'name': 'John', 'city': 'Hanoi'}

# popitem() - Xóa và trả về phần tử cuối cùng (Python 3.7+)
item = person.popitem()
print(item)  # Output: ('city', 'Hanoi')
print(person)  # Output: {'name': 'John'}
```

#### `setdefault()`
**Mô tả**: Lấy giá trị nếu key tồn tại, nếu không thì set giá trị mặc định

**Ví dụ**:
```python
person = {"name": "John", "age": 30}

# Key đã tồn tại
name = person.setdefault("name", "Unknown")
print(name)  # Output: "John"

# Key chưa tồn tại
city = person.setdefault("city", "Hanoi")
print(city)  # Output: "Hanoi"
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'Hanoi'}
```

---

### 1.4. Hàm Xử Lý Số

#### `int()`, `float()`, `complex()`
**Mô tả**: Chuyển đổi sang số nguyên, số thực, số phức

**Ví dụ**:
```python
# int()
print(int("123"))  # Output: 123
print(int(3.14))  # Output: 3
print(int("1010", 2))  # Output: 10 (chuyển từ binary)

# float()
print(float("3.14"))  # Output: 3.14
print(float(5))  # Output: 5.0

# complex()
print(complex(1, 2))  # Output: (1+2j)
print(complex("1+2j"))  # Output: (1+2j)
```

#### `abs()`
**Mô tả**: Trả về giá trị tuyệt đối

**Ví dụ**:
```python
print(abs(-5))  # Output: 5
print(abs(3.14))  # Output: 3.14
print(abs(-3.14))  # Output: 3.14
```

#### `round()`
**Mô tả**: Làm tròn số

**Ví dụ**:
```python
print(round(3.14159))  # Output: 3
print(round(3.14159, 2))  # Output: 3.14
print(round(3.5))  # Output: 4 (làm tròn lên)
print(round(2.5))  # Output: 2 (làm tròn xuống - banker's rounding)
```

#### `min()`, `max()`, `sum()`
**Mô tả**: Tìm giá trị nhỏ nhất, lớn nhất, và tổng

**Ví dụ**:
```python
numbers = [1, 5, 3, 9, 2]

print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 9
print(sum(numbers))  # Output: 20

# Với key function
students = [("John", 25), ("Jane", 20), ("Bob", 30)]
oldest = max(students, key=lambda x: x[1])
print(oldest)  # Output: ('Bob', 30)
```

#### `pow()`
**Mô tả**: Tính lũy thừa

**Ví dụ**:
```python
print(pow(2, 3))  # Output: 8 (2^3)
print(pow(2, 3, 5))  # Output: 3 (2^3 mod 5)
print(2 ** 3)  # Output: 8 (cách viết tắt)
```

#### `divmod()`
**Mô tả**: Trả về thương và số dư

**Ví dụ**:
```python
result = divmod(10, 3)
print(result)  # Output: (3, 1) - thương là 3, dư là 1

quotient, remainder = divmod(17, 5)
print(quotient)  # Output: 3
print(remainder)  # Output: 2
```

---

### 1.5. Hàm Xử Lý Iterable

#### `range()`
**Mô tả**: Tạo một dãy số

**Cú pháp**: `range(stop)` hoặc `range(start, stop, step)`

**Ví dụ**:
```python
# range(stop)
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]

# range(start, stop)
print(list(range(2, 6)))  # Output: [2, 3, 4, 5]

# range(start, stop, step)
print(list(range(0, 10, 2)))  # Output: [0, 2, 4, 6, 8]
print(list(range(10, 0, -1)))  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

#### `enumerate()`
**Mô tả**: Thêm index vào iterable

**Ví dụ**:
```python
fruits = ["apple", "banana", "orange"]

# Không dùng enumerate
for i in range(len(fruits)):
    print(i, fruits[i])

# Dùng enumerate
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Bắt đầu từ số khác
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)  # Output: 1 apple, 2 banana, 3 orange
```

#### `zip()`
**Mô tả**: Kết hợp nhiều iterable thành tuple

**Ví dụ**:
```python
names = ["John", "Jane", "Bob"]
ages = [25, 30, 35]

# Kết hợp
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# Tạo list of tuples
pairs = list(zip(names, ages))
print(pairs)  # Output: [('John', 25), ('Jane', 30), ('Bob', 35)]

# Unzip
names2, ages2 = zip(*pairs)
print(names2)  # Output: ('John', 'Jane', 'Bob')
```

#### `map()`
**Mô tả**: Áp dụng hàm cho mỗi phần tử của iterable

**Ví dụ**:
```python
numbers = [1, 2, 3, 4, 5]

# Áp dụng hàm
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Với hàm built-in
texts = ["hello", "world", "python"]
lengths = list(map(len, texts))
print(lengths)  # Output: [5, 5, 6]

# Nhiều iterable
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(sums)  # Output: [5, 7, 9]
```

#### `filter()`
**Mô tả**: Lọc các phần tử thỏa mãn điều kiện

**Ví dụ**:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lọc số chẵn
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]

# Lọc số lớn hơn 5
large = list(filter(lambda x: x > 5, numbers))
print(large)  # Output: [6, 7, 8, 9, 10]

# Với None (loại bỏ falsy values)
values = [0, 1, "", "hello", None, [], [1, 2]]
truthy = list(filter(None, values))
print(truthy)  # Output: [1, 'hello', [1, 2]]
```

#### `reduce()`
**Mô tả**: Giảm iterable thành một giá trị duy nhất (cần import từ functools)

**Ví dụ**:
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Tính tổng
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15

# Tính tích
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Với giá trị khởi tạo
total = reduce(lambda x, y: x + y, numbers, 10)
print(total)  # Output: 25 (10 + 15)
```

#### `any()`, `all()`
**Mô tả**: Kiểm tra xem có phần tử nào True (any) hoặc tất cả đều True (all)

**Ví dụ**:
```python
# any() - Trả về True nếu có ít nhất một phần tử True
numbers = [0, 0, 1, 0]
print(any(numbers))  # Output: True

numbers = [0, 0, 0, 0]
print(any(numbers))  # Output: False

# all() - Trả về True nếu tất cả phần tử đều True
numbers = [1, 2, 3, 4]
print(all(numbers))  # Output: True

numbers = [1, 2, 0, 4]
print(all(numbers))  # Output: False
```

---

### 1.6. Hàm Kiểm Tra Loại và Chuyển Đổi

#### `type()`, `isinstance()`
**Mô tả**: Kiểm tra kiểu dữ liệu

**Ví dụ**:
```python
# type()
print(type(5))  # Output: <class 'int'>
print(type("hello"))  # Output: <class 'str'>
print(type([1, 2, 3]))  # Output: <class 'list'>

# isinstance() - Kiểm tra kiểu (nên dùng hơn type)
print(isinstance(5, int))  # Output: True
print(isinstance(5, (int, float)))  # Output: True
print(isinstance("hello", int))  # Output: False
```

#### `hasattr()`, `getattr()`, `setattr()`, `delattr()`
**Mô tả**: Làm việc với attributes của object

**Ví dụ**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

# hasattr() - Kiểm tra attribute có tồn tại
print(hasattr(person, "name"))  # Output: True
print(hasattr(person, "city"))  # Output: False

# getattr() - Lấy giá trị attribute
name = getattr(person, "name")
print(name)  # Output: "John"

# Với default value
city = getattr(person, "city", "Unknown")
print(city)  # Output: "Unknown"

# setattr() - Set giá trị attribute
setattr(person, "city", "Hanoi")
print(person.city)  # Output: "Hanoi"

# delattr() - Xóa attribute
delattr(person, "city")
# print(person.city)  # AttributeError
```

---

### 1.7. Hàm I/O và File

#### `open()`
**Mô tả**: Mở file để đọc/ghi

**Cú pháp**: `open(file, mode='r', encoding=None)`

**Modes**:
- `'r'` - Đọc (read)
- `'w'` - Ghi (write, ghi đè)
- `'a'` - Ghi thêm (append)
- `'x'` - Tạo mới (exclusive creation)
- `'b'` - Binary mode
- `'t'` - Text mode (mặc định)
- `'+'` - Update mode (đọc và ghi)

**Ví dụ**:
```python
# Đọc file
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# Ghi file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello World")

# Đọc từng dòng
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Đọc tất cả dòng
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
```

#### `print()`
**Mô tả**: In ra màn hình

**Cú pháp**: `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

**Ví dụ**:
```python
# Cơ bản
print("Hello", "World")  # Output: Hello World

# Với separator
print("Hello", "World", sep="-")  # Output: Hello-World

# Với end
print("Hello", end="")
print("World")  # Output: HelloWorld

# Với file
with open("output.txt", "w") as f:
    print("Hello World", file=f)

# Formatting
name = "John"
age = 30
print(f"Name: {name}, Age: {age}")  # Output: Name: John, Age: 30
```

#### `input()`
**Mô tả**: Đọc input từ người dùng

**Ví dụ**:
```python
name = input("Nhập tên của bạn: ")
print(f"Xin chào, {name}!")

# Chuyển đổi kiểu
age = int(input("Nhập tuổi: "))
print(f"Bạn {age} tuổi")
```

---

### 1.8. Hàm Xử Lý Exception

#### `try`, `except`, `finally`, `raise`
**Mô tả**: Xử lý lỗi và ném exception

**Ví dụ**:
```python
# try-except cơ bản
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Không thể chia cho 0!")

# Nhiều exception
try:
    value = int(input("Nhập số: "))
    result = 10 / value
except ValueError:
    print("Không phải số hợp lệ!")
except ZeroDivisionError:
    print("Không thể chia cho 0!")
except Exception as e:
    print(f"Lỗi: {e}")

# finally - Luôn chạy
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File không tồn tại!")
finally:
    file.close()  # Luôn đóng file

# raise - Ném exception
def check_age(age):
    if age < 0:
        raise ValueError("Tuổi không thể âm!")
    return age

# try-except-else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Lỗi chia cho 0")
else:
    print(f"Kết quả: {result}")  # Chạy nếu không có exception
```

---

## 2. KIẾN THỨC VỀ HÀM TRONG PYTHON

### 2.1. Định Nghĩa Hàm Cơ Bản

**Cú pháp**:
```python
def function_name(parameters):
    """Docstring - mô tả hàm"""
    # Code
    return value
```

**Ví dụ**:
```python
def greet(name):
    """Chào hỏi người dùng"""
    return f"Xin chào, {name}!"

result = greet("John")
print(result)  # Output: "Xin chào, John!"
```

### 2.2. Tham Số Mặc Định (Default Parameters)

**Ví dụ**:
```python
def greet(name, greeting="Xin chào"):
    return f"{greeting}, {name}!"

print(greet("John"))  # Output: "Xin chào, John!"
print(greet("John", "Hello"))  # Output: "Hello, John!"
```

**Lưu ý**: Không dùng mutable objects làm default value!

```python
# SAI
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

# ĐÚNG
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

### 2.3. Tham Số Tùy Ý (*args và **kwargs)

**Ví dụ**:
```python
# *args - Nhận nhiều positional arguments
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15

# **kwargs - Nhận nhiều keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="Hanoi")
# Output:
# name: John
# age: 30
# city: Hanoi

# Kết hợp
def my_function(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

my_function(1, 2, 3, 4, 5, x=10, y=20)
# Output:
# a: 1, b: 2
# args: (3, 4, 5)
# kwargs: {'x': 10, 'y': 20}
```

### 2.4. Lambda Functions (Anonymous Functions)

**Cú pháp**: `lambda arguments: expression`

**Ví dụ**:
```python
# Hàm thông thường
def square(x):
    return x ** 2

# Lambda tương đương
square = lambda x: x ** 2

print(square(5))  # Output: 25

# Dùng với map, filter, sorted
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Sắp xếp với key
students = [("John", 25), ("Jane", 20), ("Bob", 30)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # Output: [('Jane', 20), ('John', 25), ('Bob', 30)]
```

### 2.5. Decorators

**Mô tả**: Hàm bọc quanh hàm khác để mở rộng chức năng

**Ví dụ**:
```python
# Decorator đơn giản
def my_decorator(func):
    def wrapper():
        print("Trước khi gọi hàm")
        func()
        print("Sau khi gọi hàm")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Trước khi gọi hàm
# Hello!
# Sau khi gọi hàm

# Decorator với arguments
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Thời gian thực thi: {end - start:.2f} giây")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

result = slow_function()
# Output: Thời gian thực thi: 1.00 giây

# Decorator với arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi():
    print("Hi!")

say_hi()
# Output:
# Hi!
# Hi!
# Hi!
```

### 2.6. Generators và yield

**Mô tả**: Hàm trả về iterator, tiết kiệm bộ nhớ

**Ví dụ**:
```python
# Generator function
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Sử dụng
counter = count_up_to(5)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2

# Hoặc dùng trong loop
for num in count_up_to(5):
    print(num)  # Output: 1, 2, 3, 4, 5

# Generator expression
squares = (x**2 for x in range(10))
print(list(squares))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 2.7. Closures

**Mô tả**: Hàm bên trong có thể truy cập biến của hàm bên ngoài

**Ví dụ**:
```python
def outer_function(x):
    # Biến của hàm ngoài
    outer_var = x
    
    def inner_function(y):
        # Có thể truy cập outer_var
        return outer_var + y
    
    return inner_function

# Tạo closure
add_five = outer_function(5)
result = add_five(10)
print(result)  # Output: 15

# Ví dụ thực tế: Tạo hàm nhân với số cố định
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

### 2.8. Type Hints và Annotations

**Ví dụ**:
```python
# Type hints cơ bản
def add(a: int, b: int) -> int:
    return a + b

# Với list, dict
from typing import List, Dict, Optional

def process_items(items: List[str]) -> List[str]:
    return [item.upper() for item in items]

def get_user(id: int) -> Optional[Dict[str, str]]:
    if id > 0:
        return {"id": id, "name": "John"}
    return None

# Union types
from typing import Union

def process(value: Union[int, str]) -> str:
    return str(value)
```

### 2.9. Recursive Functions

**Mô tả**: Hàm gọi chính nó

**Ví dụ**:
```python
# Tính giai thừa
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Output: 55

# Tìm kiếm nhị phân
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
```

---

## 3. CÁC HÀM QUAN TRỌNG TRONG FLASK

### 3.1. Flask Application Setup

#### `Flask()`
**Mô tả**: Tạo Flask application instance

**Ví dụ**:
```python
from flask import Flask

app = Flask(__name__)

# Với config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['DEBUG'] = True
```

#### `app.run()`
**Mô tả**: Chạy development server

**Ví dụ**:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### 3.2. Routing Functions

#### `@app.route()`
**Mô tả**: Định nghĩa route cho URL

**Ví dụ**:
```python
# Route cơ bản
@app.route('/')
def index():
    return 'Hello World!'

# Route với methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Xử lý POST
        return 'Logged in'
    return 'Login page'

# Route với parameters
@app.route('/user/<username>')
def show_user(username):
    return f'User: {username}'

# Route với type converter
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'

# Multiple routes
@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return 'Home page'
```

#### `url_for()`
**Mô tả**: Tạo URL từ tên hàm

**Ví dụ**:
```python
from flask import url_for

@app.route('/user/<username>')
def profile(username):
    return f'Profile of {username}'

# Tạo URL
url = url_for('profile', username='John')
print(url)  # Output: /user/John

# Trong template
# <a href="{{ url_for('profile', username='John') }}">Profile</a>
```

#### `redirect()`
**Mô tả**: Chuyển hướng đến URL khác

**Ví dụ**:
```python
from flask import redirect, url_for

@app.route('/login')
def login():
    # Redirect đến route khác
    return redirect(url_for('dashboard'))

@app.route('/old')
def old_page():
    # Redirect đến URL tuyệt đối
    return redirect('http://example.com/new')
```

### 3.3. Request Handling

#### `request`
**Mô tả**: Object chứa thông tin request

**Ví dụ**:
```python
from flask import request

# GET parameters
@app.route('/search')
def search():
    query = request.args.get('q', '')  # Lấy parameter 'q', default ''
    return f'Searching for: {query}'

# POST data
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    return f'Name: {name}, Email: {email}'

# JSON data
@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.get_json()
    return {'received': data}

# Headers
@app.route('/headers')
def headers():
    user_agent = request.headers.get('User-Agent')
    return f'User-Agent: {user_agent}'

# Files
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save('uploads/' + file.filename)
    return 'File uploaded'
```

#### `request.method`
**Mô tả**: HTTP method của request

**Ví dụ**:
```python
@app.route('/data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_data():
    if request.method == 'GET':
        return 'Getting data'
    elif request.method == 'POST':
        return 'Creating data'
    elif request.method == 'PUT':
        return 'Updating data'
    elif request.method == 'DELETE':
        return 'Deleting data'
```

### 3.4. Response Functions

#### `render_template()`
**Mô tả**: Render template HTML

**Ví dụ**:
```python
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, age=30)

# Với context
@app.route('/dashboard')
def dashboard():
    data = {'users': ['John', 'Jane'], 'count': 2}
    return render_template('dashboard.html', **data)
```

#### `jsonify()`
**Mô tả**: Tạo JSON response

**Ví dụ**:
```python
from flask import jsonify

@app.route('/api/user')
def api_user():
    user = {'name': 'John', 'age': 30}
    return jsonify(user)

@app.route('/api/users')
def api_users():
    users = [
        {'name': 'John', 'age': 30},
        {'name': 'Jane', 'age': 25}
    ]
    return jsonify(users)

# Với status code
@app.route('/api/create', methods=['POST'])
def api_create():
    # Tạo resource
    return jsonify({'message': 'Created'}), 201
```

#### `make_response()`
**Mô tả**: Tạo response object tùy chỉnh

**Ví dụ**:
```python
from flask import make_response

@app.route('/custom')
def custom():
    response = make_response('Custom response')
    response.headers['X-Custom-Header'] = 'Value'
    response.status_code = 200
    return response

# Với cookie
@app.route('/set-cookie')
def set_cookie():
    response = make_response('Cookie set')
    response.set_cookie('username', 'John', max_age=3600)
    return response
```

### 3.5. Session và Cookies

#### `session`
**Mô tả**: Lưu trữ dữ liệu session

**Ví dụ**:
```python
from flask import session

app.secret_key = 'your-secret-key'

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    session['username'] = username
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Welcome, {session['username']}!"
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
```

#### `request.cookies`
**Mô tả**: Đọc cookies từ request

**Ví dụ**:
```python
@app.route('/get-cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f'Username from cookie: {username}'
```

### 3.6. Error Handling

#### `@app.errorhandler()`
**Mô tả**: Xử lý lỗi HTTP

**Ví dụ**:
```python
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.errorhandler(403)
def forbidden(error):
    return 'Forbidden', 403
```

### 3.7. Blueprints

#### `Blueprint()`
**Mô tả**: Tổ chức routes thành modules

**Ví dụ**:
```python
from flask import Blueprint

# Tạo blueprint
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login page'

@auth.route('/logout')
def logout():
    return 'Logout'

# Đăng ký blueprint
app.register_blueprint(auth, url_prefix='/auth')
```

### 3.8. Database với Flask-SQLAlchemy

#### `db.create_all()`, `db.drop_all()`
**Mô tả**: Tạo/xóa tất cả tables

**Ví dụ**:
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Tạo tables
db.create_all()

# Xóa tables
db.drop_all()
```

#### `db.session.add()`, `db.session.commit()`
**Mô tả**: Thêm và commit vào database

**Ví dụ**:
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

# Tạo user mới
user = User(username='John')
db.session.add(user)
db.session.commit()

# Query
users = User.query.all()
user = User.query.filter_by(username='John').first()
```

### 3.9. Jinja2 Template Functions

#### Trong Template:
```jinja2
{# Variables #}
{{ variable }}

{# Filters #}
{{ name|upper }}
{{ name|lower }}
{{ text|truncate(50) }}

{# Control structures #}
{% if condition %}
    ...
{% endif %}

{% for item in items %}
    {{ item }}
{% endfor %}

{# Includes #}
{% include 'header.html' %}

{# Macros #}
{% macro render_user(user) %}
    <div>{{ user.name }}</div>
{% endmacro %}
```

---

## 4. CÁC HÀM QUAN TRỌNG TRONG DJANGO

### 4.1. Views và URL Routing

#### `path()`, `re_path()`
**Mô tả**: Định nghĩa URL pattern

**Ví dụ**:
```python
from django.urls import path, re_path

# path() - Đơn giản
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]

# re_path() - Với regex
urlpatterns = [
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
]
```

#### Function-based Views
**Ví dụ**:
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hello World")

def about(request):
    context = {'title': 'About Us'}
    return render(request, 'about.html', context)

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_detail.html', {'user': user})

def api_data(request):
    data = {'message': 'Hello'}
    return JsonResponse(data)
```

#### Class-based Views
**Ví dụ**:
```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/posts/'
```

### 4.2. Request và Response

#### `request` Object
**Ví dụ**:
```python
def my_view(request):
    # Method
    if request.method == 'GET':
        # Xử lý GET
        pass
    elif request.method == 'POST':
        # Xử lý POST
        pass
    
    # GET parameters
    search = request.GET.get('q', '')
    
    # POST data
    name = request.POST.get('name')
    
    # Files
    file = request.FILES.get('file')
    
    # Headers
    user_agent = request.META.get('HTTP_USER_AGENT')
    
    # Session
    request.session['key'] = 'value'
    value = request.session.get('key')
    
    # User
    if request.user.is_authenticated:
        username = request.user.username
    
    return HttpResponse("OK")
```

#### `HttpResponse`, `JsonResponse`, `HttpResponseRedirect`
**Ví dụ**:
```python
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# HttpResponse
def simple_view(request):
    return HttpResponse("Hello World")

# JsonResponse
def api_view(request):
    data = {'status': 'success', 'data': [1, 2, 3]}
    return JsonResponse(data)

# HttpResponseRedirect
def redirect_view(request):
    return HttpResponseRedirect('/new-url/')
```

### 4.3. Shortcuts

#### `render()`
**Mô tả**: Render template với context

**Ví dụ**:
```python
from django.shortcuts import render

def my_view(request):
    context = {
        'title': 'Home',
        'users': User.objects.all(),
    }
    return render(request, 'template.html', context)
```

#### `redirect()`
**Mô tả**: Chuyển hướng đến URL

**Ví dụ**:
```python
from django.shortcuts import redirect

def login_view(request):
    # Redirect đến URL
    return redirect('/dashboard/')

# Redirect đến view name
def login_view(request):
    return redirect('dashboard')

# Redirect với reverse
from django.urls import reverse
def login_view(request):
    return redirect(reverse('user_detail', args=[user_id]))
```

#### `get_object_or_404()`, `get_list_or_404()`
**Mô tả**: Lấy object hoặc trả về 404

**Ví dụ**:
```python
from django.shortcuts import get_object_or_404, get_list_or_404

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_detail.html', {'user': user})

def active_users(request):
    users = get_list_or_404(User, is_active=True)
    return render(request, 'users.html', {'users': users})
```

### 4.4. Models và Database

#### Model Methods
**Ví dụ**:
```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

# QuerySet Methods
# all()
users = User.objects.all()

# filter()
active_users = User.objects.filter(is_active=True)

# get()
user = User.objects.get(id=1)

# create()
user = User.objects.create(username='John', email='john@example.com')

# update()
User.objects.filter(is_active=False).update(is_active=True)

# delete()
User.objects.filter(id=1).delete()

# exclude()
inactive_users = User.objects.exclude(is_active=True)

# order_by()
users = User.objects.order_by('-created_at')

# values()
users = User.objects.values('username', 'email')

# count()
user_count = User.objects.count()

# exists()
if User.objects.filter(username='John').exists():
    print("User exists")

# first(), last()
first_user = User.objects.first()
last_user = User.objects.last()

# aggregate()
from django.db.models import Count, Avg, Sum
user_count = User.objects.aggregate(Count('id'))
avg_age = User.objects.aggregate(Avg('age'))
```

#### Relationships
**Ví dụ**:
```python
# ForeignKey
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

# OneToOne
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# ManyToMany
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    tags = models.ManyToManyField(Tag)

# Sử dụng
post = Post.objects.get(id=1)
author = post.author  # Lấy author
posts = author.post_set.all()  # Lấy tất cả posts của author

# ManyToMany
post.tags.add(tag1, tag2)
post.tags.remove(tag1)
post.tags.clear()
```

### 4.5. Forms

#### `forms.Form`, `forms.ModelForm`
**Ví dụ**:
```python
from django import forms

# Form thông thường
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# ModelForm
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# Trong view
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Xử lý dữ liệu
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

### 4.6. Authentication

#### `authenticate()`, `login()`, `logout()`
**Ví dụ**:
```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
```

#### `@login_required`, `@permission_required`
**Ví dụ**:
```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def protected_view(request):
    return HttpResponse("Protected content")

@permission_required('app.can_view')
def special_view(request):
    return HttpResponse("Special content")
```

### 4.7. Middleware và Decorators

#### `@csrf_exempt`, `@csrf_protect`
**Ví dụ**:
```python
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
def api_view(request):
    # Bỏ qua CSRF protection
    return JsonResponse({'status': 'ok'})

@csrf_protect
def form_view(request):
    # Bắt buộc CSRF protection
    return render(request, 'form.html')
```

#### `@require_http_methods`, `@require_GET`, `@require_POST`
**Ví dụ**:
```python
from django.views.decorators.http import require_http_methods, require_GET, require_POST

@require_http_methods(["GET", "POST"])
def my_view(request):
    return HttpResponse("OK")

@require_GET
def get_view(request):
    return HttpResponse("GET only")

@require_POST
def post_view(request):
    return HttpResponse("POST only")
```

### 4.8. Template Tags và Filters

#### Trong Template:
```django
{# Variables #}
{{ variable }}

{# Filters #}
{{ name|upper }}
{{ name|lower|truncatewords:10 }}
{{ date|date:"Y-m-d" }}
{{ text|safe }}

{# Tags #}
{% if condition %}
    ...
{% endif %}

{% for item in items %}
    {{ item }}
{% empty %}
    No items
{% endfor %}

{% url 'view_name' arg1 arg2 %}
{% load static %}
{% static 'css/style.css' %}

{% extends 'base.html' %}
{% block content %}
    ...
{% endblock %}

{% include 'header.html' %}
```

### 4.9. Admin

#### `admin.site.register()`
**Ví dụ**:
```python
from django.contrib import admin
from .models import User, Post

# Đăng ký đơn giản
admin.site.register(User)

# Với ModelAdmin
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at']

admin.site.register(Post, PostAdmin)
```

### 4.10. Signals

#### `@receiver`
**Ví dụ**:
```python
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(pre_save, sender=Post)
def update_post_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
```

---

## KẾT LUẬN

Tài liệu này đã trình bày chi tiết về:
- Các hàm built-in quan trọng của Python
- Kiến thức về hàm trong Python (decorators, lambda, generators, closures)
- Các hàm quan trọng trong Flask
- Các hàm quan trọng trong Django

Mỗi hàm đều có ví dụ cụ thể để bạn có thể thực hành ngay. Hãy thử nghiệm với các ví dụ này để hiểu rõ hơn về cách sử dụng từng hàm!

