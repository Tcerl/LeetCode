# CÁC HÀM ĐẶC BIỆT TRONG PYTHON
========================================

## MỤC LỤC
1. [Magic Methods (Dunder Methods)](#1-magic-methods-dunder-methods)
2. [Các Hàm Built-in Đặc Biệt](#2-các-hàm-built-in-đặc-biệt)
3. [Các Hàm Ít Được Biết Nhưng Hữu Ích](#3-các-hàm-ít-được-biết-nhưng-hữu-ích)
4. [Context Managers](#4-context-managers)
5. [Property và Descriptors](#5-property-và-descriptors)
6. [Metaclasses](#6-metaclasses)

---

## 1. MAGIC METHODS (DUNDER METHODS)

Magic methods là các phương thức đặc biệt bắt đầu và kết thúc bằng dấu gạch dưới kép (`__method__`). Chúng cho phép bạn định nghĩa cách các object của bạn tương tác với các toán tử và built-in functions.

### 1.1. Object Creation và Destruction

#### `__new__()`
**Mô tả**: Được gọi trước `__init__()`, tạo instance mới

**Ví dụ**:
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Test
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True (cùng một instance)
```

#### `__init__()`
**Mô tả**: Khởi tạo object (constructor)

**Ví dụ**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)
```

#### `__del__()`
**Mô tả**: Destructor, được gọi khi object bị xóa

**Ví dụ**:
```python
class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        print(f"File {filename} opened")
    
    def __del__(self):
        if hasattr(self, 'file'):
            self.file.close()
            print("File closed")

# Khi object bị garbage collected, __del__ được gọi

> [!IMPORTANT]
> **Góc nhìn Framework & So sánh:**
> - **Object Lifecycle (Python)**: `__init__` là constructor phổ biến. `__del__` ít được dùng hơn do cơ chế Garbage Collection của Python không đảm bảo thời điểm gọi chính xác.
> - **Django/SQLAlchemy**: Sử dụng `__init__` để "hydrating" objects (đổ dữ liệu từ DB vào instance).
> - **Spring Boot (Java)**: Sử dụng **Annotation-based Lifecycle**. Thay vì `__init__`, bạn dùng `@PostConstruct`. Việc khởi tạo được quản lý bởi IoC Container (Inversion of Control), giúp tách biệt logic khởi tạo và business logic.
> - **React (Frontend)**: `useEffect(() => ..., [])` đóng vai trò gần giống `__init__` và `__del__` (thông qua cleanup function) cho vòng đời của component.
```

### 1.2. String Representation

#### `__str__()`
**Mô tả**: Trả về string representation (cho người dùng)

**Ví dụ**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person = Person("John", 30)
print(person)  # Output: Person(name=John, age=30)
print(str(person))  # Output: Person(name=John, age=30)
```

#### `__repr__()`
**Mô tả**: Trả về "official" string representation (cho developers)

**Ví dụ**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("John", 30)
print(str(person))  # Output: John, 30 years old
print(repr(person))  # Output: Person('John', 30)
```

#### `__format__()`
**Mô tả**: Định dạng object với format specifier

**Ví dụ**:
```python
class Money:
    def __init__(self, amount):
        self.amount = amount
    
    def __format__(self, format_spec):
        if format_spec == 'USD':
            return f"${self.amount:,.2f}"
        elif format_spec == 'VND':
            return f"{self.amount:,.0f} VND"
        else:
            return str(self.amount)

money = Money(1000000)
print(f"{money:USD}")  # Output: $1,000,000.00
print(f"{money:VND}")  # Output: 1,000,000 VND

> [!TIP]
> **Góc nhìn Framework & So sánh:**
> - **Django Admin**: Tự động gọi `__str__` để hiển thị tên bản ghi trong bảng quản trị. Nếu bạn quên định nghĩa, admin sẽ hiện `MyModel object (1)`.
> - **Ruby on Rails**: Sử dụng `to_s`. Trong Ruby, mọi thứ đều là object và việc ghi đè `to_s` là văn hóa bắt buộc để debug hiệu quả.
> - **Java**: Hàm `toString()` của class `Object` thường được override trong mọi POJO (Plain Old Java Object).
```

### 1.3. Comparison Operators

#### `__eq__()`, `__ne__()`, `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`
**Mô tả**: So sánh objects

**Ví dụ**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age
    
    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age
    
    def __le__(self, other):
        return self.age <= other.age
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __ge__(self, other):
        return self.age >= other.age

p1 = Person("John", 30)
p2 = Person("Jane", 25)
print(p1 > p2)  # Output: True
print(p1 == p2)  # Output: False
```

#### `__hash__()`
**Mô tả**: Trả về hash value (cần thiết cho set và dict keys)

**Ví dụ**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    def __hash__(self):
        return hash((self.name, self.age))

# Bây giờ có thể dùng trong set và dict
p2 = Person("John", 30)
people = {p1, p2}  # Chỉ có 1 phần tử vì p1 == p2
print(len(people))  # Output: 1

> [!NOTE]
> **Góc nhìn Framework & So sánh:**
> - **SQLAlchemy/Django ORM**: `__eq__` được thiết kế để so sánh dựa trên Primary Key của DB. Hai object khác instance nhưng nếu cùng ID thì được coi là bằng nhau.
> - **Java**: Việc override cặp bài trùng `equals()` và `hashCode()` là bắt buộc nếu muốn object hoạt động đúng trong `HashMap` (tương đương `__eq__` và `__hash__`).
```

### 1.4. Arithmetic Operators

#### `__add__()`, `__sub__()`, `__mul__()`, `__truediv__()`, `__mod__()`, `__pow__()`
**Mô tả**: Các phép toán số học

**Ví dụ**:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Output: Vector(4, 6)
print(v1 * 2)   # Output: Vector(2, 4)
```

#### `__iadd__()`, `__isub__()`, `__imul__()`, etc.
**Mô tả**: In-place operators (`+=`, `-=`, `*=`, etc.)

**Ví dụ**:
```python
class Counter:
    def __init__(self, value=0):
        self.value = value
    
    def __iadd__(self, other):
        self.value += other
        return self
    
    def __repr__(self):
        return f"Counter({self.value})"

c = Counter(5)
c += 3
print(c)  # Output: Counter(8)
```

#### `__radd__()`, `__rsub__()`, etc.
**Mô tả**: Right-hand side operators (khi object ở bên phải)

**Ví dụ**:
```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Number(self.value + other)
    
    def __radd__(self, other):
        return Number(other + self.value)
    
    def __repr__(self):
        return f"Number({self.value})"

n = Number(5)
result1 = n + 3      # Gọi __add__
result2 = 3 + n      # Gọi __radd__
print(result1)  # Output: Number(8)
print(result2)  # Output: Number(8)
```

### 1.5. Container Methods

#### `__len__()`
**Mô tả**: Trả về độ dài (dùng với `len()`)

**Ví dụ**:
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def __len__(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
print(len(stack))  # Output: 2
```

#### `__getitem__()`, `__setitem__()`, `__delitem__()`
**Mô tả**: Truy cập items bằng index/key

**Ví dụ**:
```python
class MyList:
    def __init__(self, items):
        self.items = list(items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __delitem__(self, index):
        del self.items[index]
    
    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4, 5])
print(my_list[0])      # Output: 1
my_list[0] = 10        # Gọi __setitem__
print(my_list[0])      # Output: 10
del my_list[0]         # Gọi __delitem__
print(len(my_list))    # Output: 4
```

#### `__contains__()`
**Mô tả**: Kiểm tra membership (dùng với `in`)

**Ví dụ**:
```python
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __contains__(self, item):
        return self.start <= item < self.end

r = Range(0, 10)
print(5 in r)   # Output: True
print(15 in r)  # Output: False
```

#### `__iter__()`, `__next__()`
**Mô tả**: Làm cho object có thể iterate

**Ví dụ**:
```python
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

for num in CountDown(5):
    print(num)  # Output: 5, 4, 3, 2, 1

> [!TIP]
> **Góc nhìn Framework & So sánh:**
> - **Pandas/NumPy**: Ứng dụng cực mạnh `__getitem__` và `__setitem__` để thực hiện *Slicing* (`df[0:10]`) và *Masking* (`df[df['age'] > 20]`).
> - **Javascript (ES6+)**: Sử dụng `Proxy` để "bẫy" các thao tác truy cập item, tương đương với việc tùy biến Container methods trong Python.
```

### 1.6. Callable Objects

#### `__call__()`
**Mô tả**: Làm cho object có thể gọi như function

**Ví dụ**:
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
print(double(5))  # Output: 10

# Có thể dùng như decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Function called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))  # Output: Function called 1 times\nHello, John!

> [!IMPORTANT]
> **Góc nhìn Framework & So sánh:**
> - **FastAPI**: Cơ chế *Dependency Injection* của FastAPI dựa trên "Callables". Bạn có thể truyền một Class có hàm `__call__` vào `Depends()`, giúp class đó vừa lưu được state vừa có thể thực thi như một hàm.
> - **React (Hooks)**: Các hàm như `useMemo`, `useCallback` trong React cũng có tư tưởng tương tự: biến một logic phức tạp thành một thứ có thể "gọi" được đơn giản vào lần sau.
```

### 1.7. Context Managers

#### `__enter__()`, `__exit__()`
**Mô tả**: Làm cho object có thể dùng với `with` statement

**Ví dụ**:
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False  # Không suppress exceptions

# Sử dụng
with FileManager('test.txt', 'w') as f:
    f.write('Hello World')
# File tự động đóng khi ra khỏi with block

> [!TIP]
> **Góc nhìn Framework & So sánh:**
> - **Flask/FastAPI**: Sử dụng Context Managers để quản lý Database Session (ví dụ: `with get_db() as db:`). Điều này đảm bảo connection luôn được đóng/trả về pool kể cả khi code gặp lỗi.
> - **Go (Golang)**: Dùng từ khóa `defer`. Thay vì bọc trong block, Go gọi `defer file.Close()` ngay sau khi mở. Cách này trực quan nhưng Python's `with` an toàn hơn vì nó ép buộc phạm vi (scope).
```

### 1.8. Attribute Access

#### `__getattr__()`, `__setattr__()`, `__delattr__()`
**Mô tả**: Kiểm soát truy cập attributes

**Ví dụ**:
```python
class DynamicAttributes:
    def __init__(self):
        self._data = {}
    
    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
    
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            self._data[name] = value
    
    def __delattr__(self, name):
        if name in self._data:
            del self._data[name]
        else:
            super().__delattr__(name)

obj = DynamicAttributes()
obj.name = "John"  # Gọi __setattr__
print(obj.name)    # Gọi __getattr__, Output: John
del obj.name       # Gọi __delattr__
```

#### `__getattribute__()`
**Mô tả**: Được gọi cho MỌI attribute access

**Ví dụ**:
```python
class LoggedAccess:
    def __init__(self):
        self.value = 0
    
    def __getattribute__(self, name):
        print(f"Accessing attribute: {name}")
        return super().__getattribute__(name)

obj = LoggedAccess()
print(obj.value)  # Output: Accessing attribute: value\n0
```

### 1.9. Descriptors

#### `__get__()`, `__set__()`, `__delete__()`
**Mô tả**: Descriptor protocol

**Ví dụ**:
```python
class PositiveNumber:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name, 0)
    
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Value must be positive")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        del obj.__dict__[self.name]

class Person:
    age = PositiveNumber('age')
    height = PositiveNumber('height')

p = Person()
p.age = 30      # OK
p.height = -5   # ValueError: Value must be positive

> [!IMPORTANT]
> **Góc nhìn Framework & So sánh:**
> - **SQLAlchemy**: Sử dụng Descriptors để thực hiện **Lazy Loading**. Khi bạn gọi `user.posts`, một Descriptor sẽ chặn lại, thực hiện câu lệnh SQL để lấy posts, rồi mới trả về dữ liệu.
> - **Vue 3**: Hệ thống *Reactivity* sử dụng `Proxy` hoàn toàn thay thế cho `Object.defineProperty` (tương đương Descriptor), giúp theo dõi sự thay đổi của data một cách tự động.
```

---

## 2. CÁC HÀM BUILT-IN ĐẶC BIỆT

### 2.1. `eval()`, `exec()`
**Mô tả**: Thực thi code Python từ string

**Ví dụ**:
```python
# eval() - Đánh giá expression và trả về giá trị
result = eval("2 + 3 * 4")
print(result)  # Output: 14

x = 10
result = eval("x * 2")
print(result)  # Output: 20

# exec() - Thực thi statement
exec("x = 5")
exec("print('Hello from exec')")  # Output: Hello from exec

# Lưu ý: Cẩn thận với security! Không dùng với user input không tin cậy
```

### 2.2. `compile()`
**Mô tả**: Biên dịch source code thành code object

**Ví dụ**:
```python
code = compile("print('Hello')", '<string>', 'exec')
exec(code)  # Output: Hello

# Expression
code = compile("2 + 3", '<string>', 'eval')
result = eval(code)
print(result)  # Output: 5
```

### 2.3. `globals()`, `locals()`
**Mô tả**: Trả về dictionary của global/local variables

**Ví dụ**:
```python
x = 10
y = 20

def my_function():
    a = 1
    b = 2
    print("Locals:", locals())
    print("Globals:", globals())

my_function()
# Output:
# Locals: {'a': 1, 'b': 2}
# Globals: {... (tất cả global variables)}
```

### 2.4. `vars()`, `dir()`
**Mô tả**: Lấy attributes/variables của object

**Ví dụ**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)

# vars() - Trả về __dict__
print(vars(p))  # Output: {'name': 'John', 'age': 30}

# dir() - Trả về list tất cả attributes và methods
print(dir(p))  # Output: ['__class__', '__dict__', ..., 'age', 'name']
```

### 2.5. `super()`
**Mô tả**: Truy cập methods của parent class

**Ví dụ**:
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Gọi __init__ của Animal
        self.breed = breed
    
    def speak(self):
        return f"{super().speak()} - Woof!"

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)      # Output: Buddy
print(dog.speak())   # Output: Some sound - Woof!
```

### 2.6. `isinstance()`, `issubclass()`
**Mô tả**: Kiểm tra type và inheritance

**Ví dụ**:
```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))      # Output: True
print(isinstance(dog, Animal))   # Output: True
print(isinstance(dog, (Dog, Animal)))  # Output: True

print(issubclass(Dog, Animal))   # Output: True
print(issubclass(Dog, Dog))      # Output: True
```

### 2.7. `callable()`
**Mô tả**: Kiểm tra xem object có thể gọi được không

**Ví dụ**:
```python
def my_function():
    pass

class CallableClass:
    def __call__(self):
        pass

print(callable(my_function))        # Output: True
print(callable(CallableClass()))    # Output: True
print(callable("string"))           # Output: False
print(callable(5))                  # Output: False
```

### 2.8. `iter()`, `next()`
**Mô tả**: Tạo iterator và lấy phần tử tiếp theo

**Ví dụ**:
```python
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator, None))  # Output: 3 (với default value)
```

### 2.9. `property()`
**Mô tả**: Tạo property descriptor

**Ví dụ**:
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    def get_radius(self):
        return self._radius
    
    def set_radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    radius = property(get_radius, set_radius)

circle = Circle(5)
print(circle.radius)  # Output: 5
circle.radius = 10
# circle.radius = -5  # ValueError
```

### 2.10. `staticmethod()`, `classmethod()`
**Mô tả**: Tạo static method và class method

**Ví dụ**:
```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def create_from_string(cls, value_str):
        return cls(int(value_str))

# Static method - không cần instance
result = Math.add(5, 3)
print(result)  # Output: 8

# Class method - nhận class làm tham số đầu tiên
obj = Math.create_from_string("10")

> [!NOTE]
> **Góc nhìn Framework & So sánh:**
> - **FastAPI (Pydantic)**: Sử dụng `isinstance` và `issubclass` cực kỳ nhiều để thực hiện *Type Validation*. Dựa vào kiểu dữ liệu bạn khai báo, nó quyết định cách parse dữ liệu từ Request.
> - **Java**: Sử dụng **Reflection API** để kiểm tra type tại runtime, mạnh mẽ hơn nhưng chậm hơn so với cách check trực tiếp của Python.
```

---

## 3. CÁC HÀM ÍT ĐƯỢC BIẾT NHƯNG HỮU ÍCH

### 3.1. `functools` Module

#### `@lru_cache`
**Mô tả**: Cache kết quả của function

**Ví dụ**:
```python
from functools import lru_cache
import time

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Lần đầu chạy chậm
start = time.time()
result = fibonacci(30)
print(f"Time: {time.time() - start:.4f}s")

# Lần sau nhanh hơn nhiều (từ cache)
start = time.time()
result = fibonacci(30)
print(f"Time: {time.time() - start:.4f}s")
```

#### `partial()`
**Mô tả**: Tạo function mới với một số arguments đã được fix

**Ví dụ**:
```python
from functools import partial

def multiply(x, y):
    return x * y

# Tạo function mới với x=2 đã được fix
double = partial(multiply, 2)
print(double(5))  # Output: 10

# Với keyword arguments
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # Output: 25
```

#### `wraps()`
**Mô tả**: Giữ nguyên metadata của function gốc khi dùng decorator

**Ví dụ**:
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Giữ nguyên __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greet someone"""
    return f"Hello, {name}!"

print(greet.__name__)  # Output: greet (không phải wrapper)
print(greet.__doc__)   # Output: Greet someone
```

### 3.2. `itertools` Module

#### `itertools.chain()`
**Mô tả**: Kết hợp nhiều iterables

**Ví dụ**:
```python
from itertools import chain

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

combined = list(chain(list1, list2, list3))
print(combined)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### `itertools.combinations()`, `itertools.permutations()`
**Mô tả**: Tạo combinations và permutations

**Ví dụ**:
```python
from itertools import combinations, permutations

items = ['a', 'b', 'c']

# Combinations (không có thứ tự)
combs = list(combinations(items, 2))
print(combs)  # Output: [('a', 'b'), ('a', 'c'), ('b', 'c')]

# Permutations (có thứ tự)
perms = list(permutations(items, 2))
print(perms)  # Output: [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
```

#### `itertools.cycle()`
**Mô tả**: Lặp lại iterable vô hạn

**Ví dụ**:
```python
from itertools import cycle

colors = cycle(['red', 'green', 'blue'])
for i, color in enumerate(colors):
    if i >= 10:
        break
    print(color)  # Output: red, green, blue, red, green, blue, ...
```

#### `itertools.groupby()`
**Mô tả**: Nhóm các phần tử liên tiếp có cùng key

**Ví dụ**:
```python
from itertools import groupby

data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]

for key, group in groupby(data):
    print(f"{key}: {list(group)}")
# Output:
# 1: [1, 1, 1]
# 2: [2, 2]
# 3: [3, 3, 3, 3]
# 4: [4]
```

### 3.3. `operator` Module

**Mô tả**: Các hàm toán tử dùng được với `map()`, `filter()`, etc.

**Ví dụ**:
```python
from operator import add, mul, itemgetter, attrgetter

# Toán tử
numbers = [1, 2, 3, 4, 5]
result = list(map(add, numbers, numbers))
print(result)  # Output: [2, 4, 6, 8, 10]

# itemgetter - Lấy items từ list/tuple
get_second = itemgetter(1)
data = [(1, 'a'), (2, 'b'), (3, 'c')]
seconds = list(map(get_second, data))
print(seconds)  # Output: ['a', 'b', 'c']

# attrgetter - Lấy attributes từ objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("John", 30), Person("Jane", 25)]
get_age = attrgetter('age')
ages = list(map(get_age, people))
print(ages)  # Output: [30, 25]
```

### 3.4. `collections` Module

#### `defaultdict`
**Mô tả**: Dictionary với default value

**Ví dụ**:
```python
from collections import defaultdict

# Default value là list
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
print(dd['fruits'])  # Output: ['apple', 'banana']
print(dd['vegetables'])  # Output: [] (tự động tạo list rỗng)

# Default value là int
counter = defaultdict(int)
words = ['apple', 'banana', 'apple', 'orange']
for word in words:
    counter[word] += 1
print(dict(counter))  # Output: {'apple': 2, 'banana': 1, 'orange': 1}
```

#### `Counter`
**Mô tả**: Đếm số lần xuất hiện

**Ví dụ**:
```python
from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(words)
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Most common
print(counter.most_common(2))  # Output: [('apple', 3), ('banana', 2)]
```

#### `namedtuple`
**Mô tả**: Tạo tuple với named fields

**Ví dụ**:
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)  # Output: 1
print(p.y)  # Output: 2
print(p[0])  # Output: 1 (vẫn có thể dùng index)
```

#### `deque`
**Mô tả**: Double-ended queue

**Ví dụ**:
```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)  # Thêm vào đầu
d.append(4)      # Thêm vào cuối
print(d)  # Output: deque([0, 1, 2, 3, 4])

d.popleft()      # Lấy từ đầu
d.pop()          # Lấy từ cuối
print(d)  # Output: deque([1, 2, 3])
```

### 3.5. `contextlib` Module

#### `@contextmanager`
**Mô tả**: Tạo context manager dễ dàng hơn

**Ví dụ**:
```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Elapsed time: {end - start:.2f}s")

with timer():
    time.sleep(1)  # Output: Elapsed time: 1.00s
```

#### `contextlib.suppress()`
**Mô tả**: Suppress exceptions

**Ví dụ**:
```python
from contextlib import suppress

with suppress(FileNotFoundError):
    with open('nonexistent.txt') as f:
        content = f.read()
# Không ném exception nếu file không tồn tại
```

---

## 4. CONTEXT MANAGERS

### 4.1. Custom Context Manager

**Ví dụ**:
```python
class DatabaseConnection:
    def __enter__(self):
        print("Connecting to database...")
        self.connection = "database_connection"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection...")
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False  # Không suppress exception

with DatabaseConnection() as db:
    print("Using database...")
    # raise Exception("Error!")  # Nếu có exception, __exit__ vẫn được gọi
```

### 4.2. Multiple Context Managers

**Ví dụ**:
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, *args):
        self.file.close()

# Nhiều context managers
with FileManager('file1.txt', 'r') as f1, FileManager('file2.txt', 'w') as f2:
    content = f1.read()
    f2.write(content)
```

---

## 5. PROPERTY VÀ DESCRIPTORS

### 5.1. `@property` Decorator

**Ví dụ**:
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @radius.deleter
    def radius(self):
        del self._radius
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.radius)  # Output: 5
print(circle.area)    # Output: 78.53975
circle.radius = 10
# circle.radius = -5  # ValueError
```

### 5.2. Descriptors

**Ví dụ**:
```python
class TypedProperty:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be {self.expected_type.__name__}")
        obj.__dict__[self.name] = value

class Person:
    name = TypedProperty('name', str)
    age = TypedProperty('age', int)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
# p.name = 123  # TypeError: name must be str
# p.age = "30"  # TypeError: age must be int
```

---

## 6. METACLASSES

### 6.1. Basic Metaclass

**Mô tả**: Class của class (tạo class)

**Ví dụ**:
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        # Thêm attribute mới vào class
        dct['created_by'] = 'Meta'
        return super().__new__(cls, name, bases, dct)
    
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        print(f"Class {name} created")

class MyClass(metaclass=Meta):
    pass

print(MyClass.created_by)  # Output: Meta
```

### 6.2. Singleton với Metaclass

**Ví dụ**:
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

s1 = Singleton(1)
s2 = Singleton(2)
print(s1 is s2)  # Output: True
print(s1.value)  # Output: 1 (vì s2 không tạo instance mới)

> [!IMPORTANT]
> **Góc nhìn Framework & So sánh:**
> - **Django**: Toàn bộ hệ thống Model của Django dựa trên Metaclasses. `ModelBase` (metaclass của `models.Model`) quét toàn bộ các attributes của bạn (như `CharField`) và đăng ký chúng vào schema của database khi server khởi động.
> - **Ruby**: Có khái niệm "Eigenclasses" tương tự, cho phép thay đổi định nghĩa class ngay khi đang chạy (Monkey patching).
```

---

## KẾT LUẬN

Các hàm đặc biệt trong Python bao gồm:

1. **Magic Methods (Dunder Methods)**: Cho phép customize behavior của objects
2. **Built-in Functions Đặc Biệt**: `eval()`, `exec()`, `super()`, `property()`, etc.
3. **Functions Ít Được Biết**: Từ `functools`, `itertools`, `operator`, `collections`
4. **Context Managers**: Quản lý resources
5. **Property và Descriptors**: Kiểm soát attribute access
6. **Metaclasses**: Tạo và customize classes

Những hàm này giúp code Python linh hoạt và mạnh mẽ hơn!

