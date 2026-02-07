# HƯỚNG DẪN CHI TIẾT VỀ HÀM PYTHON, FLASK VÀ DJANGO
================================================================

## MỤC LỤC
1. [Hàm Built-in Quan Trọng của Python](#1-hàm-built-in-quan-trọng-của-python)
2. [Standard Library của Python](#2-standard-library-của-python)
3. [Kiến Thức Về Hàm Trong Python](#3-kiến-thức-về-hàm-trong-python)
4. [Các Hàm Quan Trọng Trong Flask](#4-các-hàm-quan-trọng-trong-flask)
5. [Các Hàm Quan Trọng Trong Django](#5-các-hàm-quan-trọng-trong-django)

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

## 2. STANDARD LIBRARY CỦA PYTHON

Standard Library là tập hợp các module được cài đặt sẵn cùng với Python, cung cấp nhiều chức năng hữu ích mà không cần cài đặt thêm package nào. Dưới đây là danh sách các thư viện quan trọng và cách sử dụng chúng.

### 2.1. os - Tương Tác Với Hệ Điều Hành

**Mô tả**: Module `os` cung cấp các chức năng để tương tác với hệ điều hành, bao gồm thao tác với file system, biến môi trường, và quản lý tiến trình.

**Các hàm quan trọng**:
```python
import os

# Làm việc với đường dẫn
path = os.path.join('folder', 'subfolder', 'file.txt')  # Tạo đường dẫn an toàn
print(os.path.exists(path))  # Kiểm tra file/folder có tồn tại
print(os.path.isdir('folder'))  # Kiểm tra có phải thư mục
print(os.path.isfile('file.txt'))  # Kiểm tra có phải file
print(os.path.basename(path))  # Lấy tên file
print(os.path.dirname(path))  # Lấy thư mục chứa file
print(os.path.splitext('file.txt'))  # Tách tên và extension: ('file', '.txt')

# Liệt kê nội dung thư mục
files = os.listdir('.')  # Liệt kê tất cả file/folder trong thư mục hiện tại
for item in os.listdir('.'):
    print(item)

# Tạo và xóa thư mục
os.mkdir('new_folder')  # Tạo thư mục (phải tồn tại thư mục cha)
os.makedirs('path/to/folder', exist_ok=True)  # Tạo thư mục đệ quy
os.rmdir('empty_folder')  # Xóa thư mục rỗng
os.removedirs('path/to/folder')  # Xóa thư mục đệ quy

# Xóa file
os.remove('file.txt')  # Xóa file

# Đổi tên/di chuyển
os.rename('old.txt', 'new.txt')  # Đổi tên hoặc di chuyển file

# Lấy thông tin
print(os.getcwd())  # Thư mục làm việc hiện tại
os.chdir('/path/to/dir')  # Đổi thư mục làm việc
print(os.path.getsize('file.txt'))  # Kích thước file (bytes)

# Biến môi trường
print(os.getenv('HOME'))  # Lấy biến môi trường
os.environ['MY_VAR'] = 'value'  # Set biến môi trường
print(os.environ.get('PATH', 'default'))  # Lấy với giá trị mặc định

# Thông tin hệ thống
print(os.name)  # Tên hệ điều hành: 'posix', 'nt', 'java'
print(os.sep)  # Ký tự phân cách đường dẫn: '/' hoặc '\\'
print(os.pathsep)  # Ký tự phân cách PATH: ':' hoặc ';'
```

### 2.2. sys - Tham Số và Hàm Hệ Thống

**Mô tả**: Module `sys` cung cấp quyền truy cập vào các tham số và hàm đặc thù của hệ thống, liên quan trực tiếp đến trình thông dịch Python.

**Các hàm quan trọng**:
```python
import sys

# Command line arguments
print(sys.argv)  # Danh sách tham số dòng lệnh
# python script.py arg1 arg2 -> ['script.py', 'arg1', 'arg2']
if len(sys.argv) > 1:
    print(f"Tham số đầu tiên: {sys.argv[1]}")

# Đường dẫn module
print(sys.path)  # Danh sách đường dẫn tìm kiếm module
sys.path.append('/custom/path')  # Thêm đường dẫn mới

# Thoát chương trình
sys.exit(0)  # Thoát với mã 0 (thành công)
sys.exit(1)  # Thoát với mã 1 (lỗi)

# Thông tin Python
print(sys.version)  # Phiên bản Python
print(sys.version_info)  # Tuple thông tin phiên bản
print(sys.platform)  # Nền tảng: 'linux', 'win32', 'darwin'

# I/O streams
sys.stdout.write('Hello\n')  # Ghi ra stdout
sys.stderr.write('Error\n')  # Ghi ra stderr
data = sys.stdin.read()  # Đọc từ stdin

# Kích thước đối tượng
print(sys.getsizeof([1, 2, 3]))  # Kích thước object trong bytes

# Recursion limit
print(sys.getrecursionlimit())  # Giới hạn đệ quy (mặc định 1000)
sys.setrecursionlimit(2000)  # Thay đổi giới hạn
```

### 2.3. datetime - Làm Việc Với Ngày Giờ

**Mô tả**: Module `datetime` cung cấp các lớp để làm việc với ngày và giờ, bao gồm tạo, thao tác, định dạng và tính toán thời gian.

**Các lớp quan trọng**:
```python
from datetime import datetime, date, time, timedelta, timezone

# datetime - Ngày và giờ
now = datetime.now()  # Thời gian hiện tại
print(now)  # 2024-01-15 10:30:45.123456

today = datetime.today()  # Ngày giờ hiện tại
utc_now = datetime.utcnow()  # UTC time

# Tạo datetime cụ thể
dt = datetime(2024, 1, 15, 10, 30, 45)
print(dt.year, dt.month, dt.day)  # 2024 1 15
print(dt.hour, dt.minute, dt.second)  # 10 30 45

# Định dạng
formatted = now.strftime('%Y-%m-%d %H:%M:%S')  # '2024-01-15 10:30:45'
parsed = datetime.strptime('2024-01-15', '%Y-%m-%d')  # Parse từ string

# date - Chỉ ngày
today = date.today()  # Ngày hiện tại
d = date(2024, 1, 15)
print(d.year, d.month, d.day)  # 2024 1 15

# time - Chỉ giờ
t = time(10, 30, 45)
print(t.hour, t.minute, t.second)  # 10 30 45

# timedelta - Khoảng thời gian
delta = timedelta(days=7, hours=2, minutes=30)
future = now + delta  # Cộng thời gian
past = now - timedelta(days=30)  # Trừ thời gian

# So sánh
if datetime.now() > datetime(2024, 1, 1):
    print("Đã qua năm mới")

# Timezone
utc = timezone.utc
local = datetime.now(utc)
```

### 2.4. json - Xử Lý JSON

**Mô tả**: Module `json` cung cấp các công cụ để mã hóa (encode) đối tượng Python thành chuỗi JSON và giải mã (decode) chuỗi JSON thành đối tượng Python.

**Các hàm quan trọng**:
```python
import json

# Chuyển Python -> JSON string
data = {
    'name': 'John',
    'age': 30,
    'cities': ['Hanoi', 'HCMC'],
    'active': True
}
json_str = json.dumps(data)  # Chuyển dict thành JSON string
print(json_str)  # {"name": "John", "age": 30, ...}

# Format đẹp
pretty_json = json.dumps(data, indent=2, ensure_ascii=False)
print(pretty_json)

# Chuyển JSON string -> Python
json_data = '{"name": "John", "age": 30}'
python_obj = json.loads(json_data)  # Parse JSON string
print(python_obj['name'])  # John

# Làm việc với file
# Ghi vào file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Đọc từ file
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
    print(loaded_data)

# Xử lý lỗi
try:
    data = json.loads('invalid json')
except json.JSONDecodeError as e:
    print(f"Lỗi JSON: {e}")
```

### 2.5. re - Regular Expressions

**Mô tả**: Module `re` cung cấp các hàm để làm việc với biểu thức chính quy (regular expressions) để tìm kiếm, thay thế và phân tích chuỗi.

**Các hàm quan trọng**:
```python
import re

# Tìm kiếm
text = "Email: john@example.com hoặc jane@test.org"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
match = re.search(pattern, text)  # Tìm lần đầu tiên
if match:
    print(match.group())  # john@example.com

# Tìm tất cả
emails = re.findall(pattern, text)  # ['john@example.com', 'jane@test.org']

# Match từ đầu chuỗi
if re.match(r'Hello', 'Hello World'):
    print("Bắt đầu bằng Hello")

# Thay thế
new_text = re.sub(r'\d+', 'NUMBER', 'Có 3 quả táo và 5 quả cam')
print(new_text)  # Có NUMBER quả táo và NUMBER quả cam

# Split
words = re.split(r'\s+', 'Hello    World   Python')
print(words)  # ['Hello', 'World', 'Python']

# Compile pattern (tối ưu khi dùng nhiều lần)
pattern = re.compile(r'\d+')
matches = pattern.findall('Có 3 quả và 5 quả')
print(matches)  # ['3', '5']

# Groups
text = "Ngày: 15/01/2024"
match = re.search(r'(\d+)/(\d+)/(\d+)', text)
if match:
    print(match.group(0))  # 15/01/2024 (toàn bộ match)
    print(match.group(1))  # 15 (group 1)
    print(match.group(2))  # 01 (group 2)
    print(match.groups())  # ('15', '01', '2024')
```

### 2.6. collections - Cấu Trúc Dữ Liệu Nâng Cao

**Mô tả**: Module `collections` cung cấp các cấu trúc dữ liệu đặc biệt như Counter, defaultdict, deque, OrderedDict, và namedtuple.

**Các lớp quan trọng**:
```python
from collections import Counter, defaultdict, deque, OrderedDict, namedtuple

# Counter - Đếm phần tử
counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(counter)  # Counter({'a': 3, 'b': 2, 'c': 1})
print(counter.most_common(2))  # [('a', 3), ('b', 2)]

# defaultdict - Dict với giá trị mặc định
dd = defaultdict(int)  # Mặc định là 0
dd['a'] += 1  # Không cần kiểm tra key có tồn tại
print(dd['b'])  # 0 (tự động tạo)

dd_list = defaultdict(list)
dd_list['fruits'].append('apple')  # Tự động tạo list nếu chưa có

# deque - Queue hai đầu
dq = deque([1, 2, 3])
dq.append(4)  # Thêm vào cuối
dq.appendleft(0)  # Thêm vào đầu
print(dq)  # deque([0, 1, 2, 3, 4])
dq.pop()  # Lấy từ cuối
dq.popleft()  # Lấy từ đầu

# namedtuple - Tuple có tên
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # 1 2
print(p[0], p[1])  # 1 2 (vẫn dùng index được)

# OrderedDict - Dict giữ thứ tự (Python 3.7+ dict đã giữ thứ tự)
od = OrderedDict()
od['first'] = 1
od['second'] = 2
print(list(od.keys()))  # ['first', 'second']
```

### 2.7. itertools - Iterator Tools

**Mô tả**: Module `itertools` cung cấp các hàm để tạo và làm việc với iterators, giúp xử lý dữ liệu hiệu quả hơn.

**Các hàm quan trọng**:
```python
from itertools import count, cycle, repeat, chain, combinations, permutations, product

# count - Đếm vô hạn
for i in count(10, 2):  # Bắt đầu từ 10, tăng 2
    if i > 20:
        break
    print(i)  # 10, 12, 14, 16, 18, 20

# cycle - Lặp vô hạn
colors = cycle(['red', 'green', 'blue'])
for i, color in enumerate(colors):
    if i >= 5:
        break
    print(color)  # red, green, blue, red, green

# repeat - Lặp lại giá trị
for i in repeat('hello', 3):  # Lặp 3 lần
    print(i)  # hello, hello, hello

# chain - Nối nhiều iterable
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list(chain(list1, list2))  # [1, 2, 3, 4, 5, 6]

# combinations - Tổ hợp
items = ['a', 'b', 'c']
combs = list(combinations(items, 2))  # [('a', 'b'), ('a', 'c'), ('b', 'c')]

# permutations - Hoán vị
perms = list(permutations(items, 2))  # [('a', 'b'), ('a', 'c'), ('b', 'a'), ...]

# product - Tích Descartes
result = list(product([1, 2], [3, 4]))  # [(1, 3), (1, 4), (2, 3), (2, 4)]
```

### 2.8. functools - Higher-Order Functions

**Mô tả**: Module `functools` cung cấp các hàm bậc cao để làm việc với functions, bao gồm decorators và caching.

**Các hàm quan trọng**:
```python
from functools import reduce, partial, lru_cache, wraps

# reduce - Giảm iterable thành một giá trị
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)  # 15
product = reduce(lambda x, y: x * y, numbers)  # 120

# partial - Tạo hàm với tham số mặc định
def multiply(x, y):
    return x * y

double = partial(multiply, 2)  # Hàm nhân với 2
print(double(5))  # 10

# lru_cache - Cache kết quả hàm
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30))  # Nhanh hơn nhiều nhờ cache

# wraps - Giữ metadata của hàm gốc khi dùng decorator
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### 2.9. pathlib - Xử Lý Đường Dẫn Hiện Đại

**Mô tả**: Module `pathlib` cung cấp cách hiện đại và hướng đối tượng để làm việc với đường dẫn file system (Python 3.4+).

**Các lớp quan trọng**:
```python
from pathlib import Path

# Tạo Path object
p = Path('folder/file.txt')
p = Path.cwd() / 'folder' / 'file.txt'  # Dùng toán tử /

# Kiểm tra
print(p.exists())  # File có tồn tại
print(p.is_file())  # Có phải file
print(p.is_dir())  # Có phải thư mục

# Thông tin
print(p.name)  # 'file.txt'
print(p.stem)  # 'file' (tên không có extension)
print(p.suffix)  # '.txt'
print(p.parent)  # Thư mục cha
print(p.parts)  # ('folder', 'file.txt')

# Thao tác
p.mkdir(parents=True, exist_ok=True)  # Tạo thư mục
p.touch()  # Tạo file rỗng
p.unlink()  # Xóa file
p.rmdir()  # Xóa thư mục rỗng

# Đọc/ghi
content = p.read_text(encoding='utf-8')  # Đọc text
p.write_text('Hello', encoding='utf-8')  # Ghi text
data = p.read_bytes()  # Đọc binary
p.write_bytes(b'data')  # Ghi binary

# Liệt kê
for item in Path('.').iterdir():  # Liệt kê trong thư mục
    print(item)

# Tìm kiếm
for py_file in Path('.').glob('*.py'):  # Tìm file .py
    print(py_file)

for py_file in Path('.').rglob('*.py'):  # Tìm đệ quy
    print(py_file)
```

### 2.10. random - Số Ngẫu Nhiên

**Mô tả**: Module `random` cung cấp các hàm để tạo số ngẫu nhiên, chọn phần tử ngẫu nhiên từ sequence.

**Các hàm quan trọng**:
```python
import random

# Số ngẫu nhiên
print(random.random())  # Số thực từ 0.0 đến 1.0
print(random.randint(1, 10))  # Số nguyên từ 1 đến 10
print(random.uniform(1.0, 10.0))  # Số thực từ 1.0 đến 10.0

# Chọn phần tử
items = ['a', 'b', 'c', 'd']
print(random.choice(items))  # Chọn 1 phần tử ngẫu nhiên
print(random.choices(items, k=2))  # Chọn k phần tử (có thể trùng)
print(random.sample(items, 2))  # Chọn k phần tử (không trùng)

# Xáo trộn
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)  # Xáo trộn tại chỗ
print(numbers)

# Seed - Để tái tạo kết quả
random.seed(42)
print(random.randint(1, 10))  # Luôn cho cùng kết quả với seed 42
```

### 2.11. time - Thời Gian

**Mô tả**: Module `time` cung cấp các hàm để làm việc với thời gian, bao gồm sleep, timestamp, và format thời gian.

**Các hàm quan trọng**:
```python
import time

# Thời gian hiện tại
print(time.time())  # Timestamp (số giây từ epoch)
print(time.ctime())  # String dễ đọc: 'Mon Jan 15 10:30:45 2024'
print(time.localtime())  # Struct time object

# Sleep - Tạm dừng
time.sleep(1)  # Dừng 1 giây

# Format thời gian
t = time.localtime()
formatted = time.strftime('%Y-%m-%d %H:%M:%S', t)
print(formatted)  # '2024-01-15 10:30:45'

# Parse thời gian
parsed = time.strptime('2024-01-15', '%Y-%m-%d')

# Đo thời gian thực thi
start = time.time()
# Code cần đo
time.sleep(0.1)
end = time.time()
print(f"Thời gian: {end - start:.2f} giây")
```

### 2.12. math - Toán Học

**Mô tả**: Module `math` cung cấp các hàm toán học cơ bản và nâng cao.

**Các hàm quan trọng**:
```python
import math

# Hằng số
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045

# Làm tròn
print(math.ceil(4.3))  # 5 (làm tròn lên)
print(math.floor(4.7))  # 4 (làm tròn xuống)
print(math.trunc(4.7))  # 4 (bỏ phần thập phân)

# Lũy thừa và logarit
print(math.pow(2, 3))  # 8.0
print(math.sqrt(16))  # 4.0
print(math.log(10))  # Logarit tự nhiên
print(math.log10(100))  # Logarit cơ số 10

# Lượng giác
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))  # 1.0
print(math.degrees(math.pi))  # 180.0
print(math.radians(180))  # 3.14159...

# Khác
print(math.factorial(5))  # 120
print(math.gcd(48, 18))  # 6 (ước chung lớn nhất)
```

### 2.13. statistics - Thống Kê

**Mô tả**: Module `statistics` cung cấp các hàm để tính toán thống kê cơ bản.

**Các hàm quan trọng**:
```python
import statistics

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(statistics.mean(data))  # 5.5 (trung bình)
print(statistics.median(data))  # 5.5 (trung vị)
print(statistics.mode([1, 2, 2, 3, 3, 3]))  # 3 (mode)
print(statistics.stdev(data))  # Độ lệch chuẩn
print(statistics.variance(data))  # Phương sai
```

### 2.14. urllib - URL Handling

**Mô tả**: Module `urllib` cung cấp các hàm để mở và đọc URLs, parse URLs, và làm việc với HTTP requests.

**Các hàm quan trọng**:
```python
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlparse, urljoin, quote, unquote
from urllib.error import URLError

# Mở URL
try:
    response = urlopen('https://www.example.com')
    content = response.read().decode('utf-8')
    print(content[:100])
except URLError as e:
    print(f"Lỗi: {e}")

# Tải file
urlretrieve('https://example.com/image.jpg', 'image.jpg')

# Parse URL
url = 'https://example.com/path?param=value#fragment'
parsed = urlparse(url)
print(parsed.scheme)  # 'https'
print(parsed.netloc)  # 'example.com'
print(parsed.path)  # '/path'
print(parsed.query)  # 'param=value'

# Encode/Decode URL
encoded = quote('hello world')  # 'hello%20world'
decoded = unquote('hello%20world')  # 'hello world'

# Join URL
base = 'https://example.com'
path = urljoin(base, '/new/path')  # 'https://example.com/new/path'
```

### 2.15. http - HTTP Server và Client

**Mô tả**: Module `http` cung cấp các lớp để tạo HTTP server và client.

**Ví dụ đơn giản**:
```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello World</h1>')

# server = HTTPServer(('localhost', 8000), MyHandler)
# server.serve_forever()
```

### 2.16. csv - Xử Lý CSV

**Mô tả**: Module `csv` cung cấp các hàm để đọc và ghi file CSV.

**Các hàm quan trọng**:
```python
import csv

# Ghi CSV
with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['John', 30, 'Hanoi'])
    writer.writerow(['Jane', 25, 'HCMC'])

# Ghi với DictWriter
with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'John', 'Age': 30, 'City': 'Hanoi'})

# Đọc CSV
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Đọc với DictReader
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], row['Age'])
```

### 2.17. xml - Xử Lý XML

**Mô tả**: Module `xml` cung cấp các công cụ để parse và tạo XML.

**Ví dụ với ElementTree**:
```python
import xml.etree.ElementTree as ET

# Parse XML
xml_string = '''<root>
    <person>
        <name>John</name>
        <age>30</age>
    </person>
</root>'''

root = ET.fromstring(xml_string)
name = root.find('person/name').text  # 'John'

# Tạo XML
root = ET.Element('root')
person = ET.SubElement(root, 'person')
name = ET.SubElement(person, 'name')
name.text = 'John'
tree = ET.ElementTree(root)
tree.write('output.xml')
```

### 2.18. sqlite3 - SQLite Database

**Mô tả**: Module `sqlite3` cung cấp interface để làm việc với SQLite database.

**Các hàm quan trọng**:
```python
import sqlite3

# Kết nối database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Tạo bảng
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Insert
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('John', 30))
conn.commit()

# Select
cursor.execute("SELECT * FROM users WHERE age > ?", (25,))
rows = cursor.fetchall()
for row in rows:
    print(row)

# Context manager
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
```

### 2.19. hashlib - Hash Functions

**Mô tả**: Module `hashlib` cung cấp các hàm hash như MD5, SHA1, SHA256.

**Các hàm quan trọng**:
```python
import hashlib

# MD5
md5 = hashlib.md5()
md5.update(b'Hello World')
print(md5.hexdigest())  # 'b10a8db164e0754105b7a99be72e3fe5'

# SHA256
sha256 = hashlib.sha256()
sha256.update(b'Hello World')
print(sha256.hexdigest())

# Hash file
def hash_file(filename):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()
```

### 2.20. base64 - Base64 Encoding

**Mô tả**: Module `base64` cung cấp các hàm để encode và decode dữ liệu base64.

**Các hàm quan trọng**:
```python
import base64

# Encode
data = b'Hello World'
encoded = base64.b64encode(data)
print(encoded)  # b'SGVsbG8gV29ybGQ='

# Decode
decoded = base64.b64decode(encoded)
print(decoded)  # b'Hello World'

# URL-safe encoding
url_safe = base64.urlsafe_b64encode(data)
```

### 2.21. zlib - Compression

**Mô tả**: Module `zlib` cung cấp các hàm để nén và giải nén dữ liệu.

**Các hàm quan trọng**:
```python
import zlib

# Nén
data = b'Hello World' * 100
compressed = zlib.compress(data)
print(f"Kích thước gốc: {len(data)}")
print(f"Kích thước nén: {len(compressed)}")

# Giải nén
decompressed = zlib.decompress(compressed)
print(decompressed == data)  # True
```

### 2.22. gzip - Gzip Files

**Mô tả**: Module `gzip` cung cấp interface để làm việc với file .gz.

**Các hàm quan trọng**:
```python
import gzip

# Ghi file nén
with gzip.open('file.txt.gz', 'wt', encoding='utf-8') as f:
    f.write('Hello World')

# Đọc file nén
with gzip.open('file.txt.gz', 'rt', encoding='utf-8') as f:
    content = f.read()
    print(content)
```

### 2.23. pickle - Serialization

**Mô tả**: Module `pickle` cung cấp các hàm để serialize và deserialize Python objects.

**Các hàm quan trọng**:
```python
import pickle

# Serialize
data = {'name': 'John', 'age': 30, 'cities': ['Hanoi', 'HCMC']}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Deserialize
with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    print(loaded_data)

# Dumps/Loads (làm việc với string)
pickled = pickle.dumps(data)
unpickled = pickle.loads(pickled)
```

### 2.24. shutil - File Operations

**Mô tả**: Module `shutil` cung cấp các hàm cấp cao để thao tác với files và directories.

**Các hàm quan trọng**:
```python
import shutil

# Copy
shutil.copy('source.txt', 'dest.txt')  # Copy file
shutil.copytree('src_dir', 'dst_dir')  # Copy thư mục đệ quy

# Move/Rename
shutil.move('old.txt', 'new.txt')

# Xóa
shutil.rmtree('directory')  # Xóa thư mục và nội dung

# Archive
shutil.make_archive('backup', 'zip', 'folder')  # Tạo file zip
shutil.unpack_archive('backup.zip', 'extract_folder')  # Giải nén
```

### 2.25. glob - File Pattern Matching

**Mô tả**: Module `glob` cung cấp các hàm để tìm file theo pattern.

**Các hàm quan trọng**:
```python
import glob

# Tìm file .py
py_files = glob.glob('*.py')
print(py_files)

# Tìm đệ quy
all_py = glob.glob('**/*.py', recursive=True)

# Pattern
files = glob.glob('data[0-9].txt')  # data0.txt, data1.txt, ...
```

### 2.26. tempfile - Temporary Files

**Mô tả**: Module `tempfile` cung cấp các hàm để tạo file và thư mục tạm thời.

**Các hàm quan trọng**:
```python
import tempfile
import os

# Temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write('Temporary data')
    temp_name = f.name

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Thư mục tạm: {tmpdir}")
    # Tự động xóa khi ra khỏi context
```

### 2.27. logging - Logging

**Mô tả**: Module `logging` cung cấp hệ thống logging mạnh mẽ cho ứng dụng.

**Các hàm quan trọng**:
```python
import logging

# Cấu hình
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

# Sử dụng
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

# Logger riêng
logger = logging.getLogger('my_module')
logger.info('Module message')
```

### 2.28. unittest - Unit Testing

**Mô tả**: Module `unittest` cung cấp framework để viết và chạy unit tests.

**Ví dụ**:
```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)
    
    def test_multiply(self):
        self.assertEqual(2 * 3, 6)
    
    def setUp(self):
        # Chạy trước mỗi test
        pass
    
    def tearDown(self):
        # Chạy sau mỗi test
        pass

if __name__ == '__main__':
    unittest.main()
```

### 2.29. doctest - Documentation Testing

**Mô tả**: Module `doctest` cho phép test code thông qua docstrings.

**Ví dụ**:
```python
def add(a, b):
    """
    Cộng hai số.
    
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

### 2.30. argparse - Command Line Parsing

**Mô tả**: Module `argparse` cung cấp cách dễ dàng để parse command line arguments.

**Ví dụ**:
```python
import argparse

parser = argparse.ArgumentParser(description='Mô tả chương trình')
parser.add_argument('--name', type=str, required=True, help='Tên người dùng')
parser.add_argument('--age', type=int, default=0, help='Tuổi')
parser.add_argument('--verbose', action='store_true', help='Chế độ verbose')

args = parser.parse_args()
print(f"Tên: {args.name}, Tuổi: {args.age}")
```

### 2.31. configparser - Configuration Files

**Mô tả**: Module `configparser` cung cấp cách đọc và ghi file cấu hình INI.

**Ví dụ**:
```python
import configparser

# Tạo config
config = configparser.ConfigParser()
config['DEFAULT'] = {'Server': 'localhost', 'Port': '8080'}
config['database'] = {'host': 'localhost', 'port': '5432'}

# Ghi file
with open('config.ini', 'w') as f:
    config.write(f)

# Đọc file
config.read('config.ini')
print(config['database']['host'])  # 'localhost'
```

### 2.32. email - Email Handling

**Mô tả**: Module `email` cung cấp các lớp để tạo và parse email messages.

**Ví dụ**:
```python
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Tạo email
msg = MIMEMultipart()
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'
msg['Subject'] = 'Test Email'
msg.attach(MIMEText('Body của email', 'plain'))
```

### 2.33. smtplib - SMTP Client

**Mô tả**: Module `smtplib` cung cấp client SMTP để gửi email.

**Ví dụ**:
```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('Nội dung email')
msg['Subject'] = 'Subject'
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'

# Gửi email
# server = smtplib.SMTP('smtp.example.com', 587)
# server.starttls()
# server.login('user', 'password')
# server.send_message(msg)
# server.quit()
```

### 2.34. socket - Network Programming

**Mô tả**: Module `socket` cung cấp interface cho network programming.

**Ví dụ server đơn giản**:
```python
import socket

# Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(1)

conn, addr = server.accept()
data = conn.recv(1024)
conn.send(b'Response')
conn.close()
```

### 2.35. threading - Threading

**Mô tả**: Module `threading` cung cấp các lớp để làm việc với threads.

**Ví dụ**:
```python
import threading
import time

def worker(name):
    print(f"Thread {name} bắt đầu")
    time.sleep(2)
    print(f"Thread {name} kết thúc")

# Tạo threads
t1 = threading.Thread(target=worker, args=('Thread-1',))
t2 = threading.Thread(target=worker, args=('Thread-2',))

t1.start()
t2.start()

t1.join()
t2.join()
```

### 2.36. multiprocessing - Multiprocessing

**Mô tả**: Module `multiprocessing` cung cấp cách chạy code song song với processes.

**Ví dụ**:
```python
from multiprocessing import Process

def worker(name):
    print(f"Process {name}")

if __name__ == '__main__':
    p1 = Process(target=worker, args=('Process-1',))
    p2 = Process(target=worker, args=('Process-2',))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
```

### 2.37. queue - Queue

**Mô tả**: Module `queue` cung cấp các lớp queue để giao tiếp giữa threads.

**Ví dụ**:
```python
import queue
import threading

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Xử lý: {item}")
        q.task_done()

# Tạo worker thread
t = threading.Thread(target=worker)
t.start()

# Thêm items
for i in range(5):
    q.put(i)

q.join()  # Đợi tất cả tasks hoàn thành
q.put(None)  # Dừng worker
t.join()
```

### 2.38. asyncio - Asynchronous I/O

**Mô tả**: Module `asyncio` cung cấp framework cho asynchronous programming (Python 3.4+).

**Ví dụ**:
```python
import asyncio

async def fetch_data(url):
    await asyncio.sleep(1)  # Giả lập I/O
    return f"Data from {url}"

async def main():
    tasks = [fetch_data(f"url{i}") for i in range(3)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

### 2.39. contextlib - Context Managers

**Mô tả**: Module `contextlib` cung cấp các utilities để làm việc với context managers.

**Ví dụ**:
```python
from contextlib import contextmanager, suppress

# Tạo context manager
@contextmanager
def my_context():
    print("Vào context")
    yield
    print("Ra khỏi context")

with my_context():
    print("Trong context")

# Suppress exceptions
with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')
```

### 2.40. dataclasses - Data Classes

**Mô tả**: Module `dataclasses` cung cấp decorator để tạo data classes dễ dàng (Python 3.7+).

**Ví dụ**:
```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    city: str = "Hanoi"
    hobbies: list = field(default_factory=list)

p = Person("John", 30)
print(p)  # Person(name='John', age=30, city='Hanoi', hobbies=[])
```

### 2.41. typing - Type Hints

**Mô tả**: Module `typing` cung cấp các type hints để hỗ trợ static type checking.

**Ví dụ**:
```python
from typing import List, Dict, Optional, Union, Tuple, Callable

def process_items(items: List[str]) -> List[str]:
    return [item.upper() for item in items]

def get_user(id: int) -> Optional[Dict[str, str]]:
    if id > 0:
        return {"id": id, "name": "John"}
    return None

def process(value: Union[int, str]) -> str:
    return str(value)
```

### 2.42. enum - Enumerations

**Mô tả**: Module `enum` cung cấp cách tạo enumerations.

**Ví dụ**:
```python
from enum import Enum, IntEnum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Status(IntEnum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

print(Color.RED)  # Color.RED
print(Color.RED.value)  # 1
```

### 2.43. secrets - Secure Random

**Mô tả**: Module `secrets` cung cấp các hàm để tạo số ngẫu nhiên an toàn cho mật khẩu, tokens (Python 3.6+).

**Ví dụ**:
```python
import secrets

# Token an toàn
token = secrets.token_hex(32)  # 64 ký tự hex
print(token)

# Token URL-safe
url_token = secrets.token_urlsafe(32)

# So sánh an toàn
if secrets.compare_digest(token1, token2):
    print("Tokens khớp")
```

### 2.44. string - String Constants

**Mô tả**: Module `string` cung cấp các hằng số và utilities cho strings.

**Ví dụ**:
```python
import string

print(string.ascii_letters)  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)  # '0123456789'
print(string.punctuation)  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Template
template = string.Template('$name is $age years old')
result = template.substitute(name='John', age=30)
print(result)  # 'John is 30 years old'
```

### 2.45. difflib - Diff Tools

**Mô tả**: Module `difflib` cung cấp các công cụ để so sánh sequences.

**Ví dụ**:
```python
import difflib

text1 = ['line1', 'line2', 'line3']
text2 = ['line1', 'line2a', 'line3']

diff = difflib.unified_diff(text1, text2, lineterm='')
for line in diff:
    print(line)
```

### 2.46. textwrap - Text Wrapping

**Mô tả**: Module `textwrap` cung cấp các hàm để format và wrap text.

**Ví dụ**:
```python
import textwrap

text = "Đây là một đoạn văn bản rất dài cần được wrap để hiển thị đẹp hơn."

# Wrap text
wrapped = textwrap.wrap(text, width=30)
for line in wrapped:
    print(line)

# Fill
filled = textwrap.fill(text, width=30)
print(filled)

# Dedent
code = """
    def hello():
        print("Hello")
"""
dedented = textwrap.dedent(code)
print(dedented)
```

### 2.47. calendar - Calendar Functions

**Mô tả**: Module `calendar` cung cấp các hàm để làm việc với lịch.

**Ví dụ**:
```python
import calendar

# Lịch tháng
print(calendar.month(2024, 1))

# Lịch năm
print(calendar.calendar(2024))

# Kiểm tra năm nhuận
print(calendar.isleap(2024))  # True

# Số ngày trong tháng
print(calendar.monthrange(2024, 2))  # (3, 29) - Thứ 3, 29 ngày
```

### 2.48. locale - Locale

**Mô tả**: Module `locale` cung cấp các hàm để làm việc với locale (ngôn ngữ, định dạng số, tiền tệ).

**Ví dụ**:
```python
import locale

# Set locale
locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')

# Format số
formatted = locale.format_string('%.2f', 1234.56, grouping=True)
print(formatted)  # '1.234,56' (tùy locale)
```

### 2.49. copy - Shallow và Deep Copy

**Mô tả**: Module `copy` cung cấp các hàm để copy objects.

**Ví dụ**:
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow = copy.copy(original)
shallow[0][0] = 999
print(original)  # [[999, 2, 3], [4, 5, 6]] - Thay đổi!

# Deep copy
deep = copy.deepcopy(original)
deep[0][0] = 111
print(original)  # [[999, 2, 3], [4, 5, 6]] - Không thay đổi
```

### 2.50. pprint - Pretty Print

**Mô tả**: Module `pprint` cung cấp cách in dữ liệu đẹp hơn, dễ đọc hơn.

**Ví dụ**:
```python
from pprint import pprint

data = {
    'users': [
        {'name': 'John', 'age': 30, 'cities': ['Hanoi', 'HCMC']},
        {'name': 'Jane', 'age': 25, 'cities': ['Da Nang']}
    ],
    'settings': {'theme': 'dark', 'language': 'vi'}
}

# In đẹp
pprint(data, indent=2, width=40)
```

---

## 3. KIẾN THỨC VỀ HÀM TRONG PYTHON

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

## 4. CÁC HÀM QUAN TRỌNG TRONG FLASK

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

## 5. CÁC HÀM QUAN TRỌNG TRONG DJANGO

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
- Standard Library của Python (50+ thư viện quan trọng như os, sys, datetime, json, re, collections, itertools, và nhiều thư viện khác)
- Kiến thức về hàm trong Python (decorators, lambda, generators, closures)
- Các hàm quan trọng trong Flask
- Các hàm quan trọng trong Django

Mỗi hàm đều có ví dụ cụ thể để bạn có thể thực hành ngay. Hãy thử nghiệm với các ví dụ này để hiểu rõ hơn về cách sử dụng từng hàm!

