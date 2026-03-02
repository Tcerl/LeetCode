## I. Python core

## 1. Kiểu dữ liệu
#### 1.1 Mutable vs Immutable

# Immutable là kiểu dữ liệu không thể thay đổi sau khi tạo: (str,tuple, int, float, bool )
# Mutable là những kiểu dữ liệu thể thay đổi: (list, dict, set)

>** when use????
> - **Immutable**: Dùng làm dict key, thread-safe, bảo vệ dữ liệu không bị thay đổi ngoài ý muốn 
> - **Mutable**: Khi cần thêm/xóa/sửa dữ liệu linh hoạt trong runtime


> - **Câu hỏi hay gặp:** "Tại sao tuple nhanh hơn list?"
> Vì tuple được lưu ởbộ nhớ cố định, it overhead hơn. python cũng cache tuple nhỏ.


#### 1.2 List comprehension and Generator Expression
# List comprehension - tạo ngay toàn bộ  list trong RAM
squares = [x**2 for x in range(1000000)]

# Generator Expression - lazy evaluation, tiết kiệm RAM(chỉ tính toán khi cần)
squares_gen  = (x**2 for x in range(1000000))
next(squares_gen)  # Lấy từng phần tử

# Dictionary comprehension
d = {k: v for k, v in zip("abc", [1, 2, 3])}
# {'a': 1,'b': 2, 'c':3}

# Set comprehension
unique = {x % 3 for x in range(10)}
# {0,1,2}

> **When use???**
> - **List comprehension**: Khi cần toàn bộ kết quả ngay, dataset nhỏ/vừa
> - **Generator**: Khi xử lý file lớn, streaming data, pipeline transform


--------------------------------------------------------------------


## 2. Function and CLOSURES

### 2.1 *args & **kwargs

args -> tuple các positional arguments
kwargs -> dict các keyword arguments.

> - **Dùng khi nào???**
> - Viết hàm linh hoạt (wrapper, middleware)
> - Kế thừa, mở rộng hàm cha mà kông biết trước trước tham số

### 2.2 Closures

    clousure: hàm bên trong nhớ biến của hàm bên ngoài

> - **Dùng khi nào???**
> - Tạo factory functions
> - Encapsulate state mà không cần class
> - Dùng trong decorators

----------------------------------------------------------------------


### 2.3 Lambda Functions
Lambda là hàm ẩn danh(anonymous function), không có tên, dùng cho các biểu thức ngắn gọn
Cú pháp: ** `lambda arguments expression`


> - **Dùng trong trường hợp nào??**
> 1. ** Custom Sorting: ** làm `key` cho `sorted()`, `min()`, `max()`
> - **Ex**: sorted(data, key= lambda x: x[`age`])
> 2. **High-order Function**: ** Kết hợp với `map()`, `filter()`, `reduce()` để xử lý list nhanh
> 3. **Callbacks:** Truyền vào các nhận tham số là hàm (như `df.apply()` trong Pandas hoặc các nút bấm trong giao diện GUI)
> 4. **Hàm dùng 1 lần**: Khi logic quá đơn giản, không cần thiết phải định nghĩa bằng `def`

> **When use?**
> - Khi logic phức tạp(có nhiều câu lệnh `if/else` hoặc vòng lặp)
> - Khi cần tái sử dụng hàm ở nhiều nơi khác nhau
> - Khi việc dùng lambda làm code trở nên khó đọc(vi phạm triết lý "Readability counts" của python)

## 3. DECORATORS

#### 3.1 Decorator cơ bản
@timer

#### 3.2 Decorator có tham số

#### 3.3 Clase-based Decorator

> **When use it???** 
    - Logging/Timing: Theo dõi performance
    - Authentication: `@login_required` trong Flask
    - Caching: Cache kết quả tốn kém
    - Retry: Gọi API không ổn định
    - Rate limiting: Giới hạn tốc độ gọi hàm

--------------------------------------------------------------------

## 4. GENERATORS VÀ ITERATORS

#### 4.1 Generator Functions(yield)

Generator đọc file lớn từng dòng - không load hết vào RAM
Xử lý file log gigabyte mà không hết RAM
Generator pipeline


#### 4.2 Generator với send()

Generator 2 chiều - nhận và gửi dữ liệu

> **When des it use???**
> - Xử lý file/data lớn (ETL pipeline)
> - Streaming response từ API
> - Infinite squences (ID generator, timestamp stream)
> - Khi bạn làm **eCommerce migration** - Đọc hàng nghìn records mà không OOM

-----------------------------------------------------------------------------

## 5. OOP - LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG
#### 5.1.1. ENCAPSULATION - đóng gói
#### 5.1.2. INHERITANCE - kế thừa
#### 5.1.3. POLYMORPHISM - đa hình
#### 5.1.4. ABSTRACTION - trừu tượng hóa

#### 5.2 Dunder Methods(Magic Methods)
#### 5.3 Class Methods vs Static Methods vs Propertes
> - `@property`: Computed attributes, validate khi set giá trị
> - `@classmethod`: Factory patterm, alternative constructors
> - `@staticmetod`: Utility function liên quan đến class nhưng không cần state

--------------------------------------------------------------------------------------

## 6. CONTEXT MANAGERS

# Cách 1: Dùng class
class DatabaseConnection:
    def __enter__(self):
        self.conn = connect_to_db()
        return self.conn
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close() # luôn đóng dù có lỗi hay không
        return False # không supperess exception
with DatabaseConnection()  as conn:
    conn.execute("SELECT * FORM users")

# Cách 2: Dùng contextlib
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield # code trong `width` block chạy ở đây
    print(f"Elapsed: {time.time() - start:.4f}s")
with timer():
    time.sleep(1)


> - **When does it use?**
**File I/O**: `with open(...) as f`
**Database**: Mở/đóng connection, transaction
**Locks**: Thread/process locking
**Temporary state**: Thay đổi config tạm thời



## 7. Exception Handling


## 8. CONCURRENCY
#### 8.1. Threading vs Multiprocessing vs AsyncIO


```python
import threading
import multiprocessing
import asyncio

# THREADING - I/O bound tasks
def fetch_data(url):
    import requests
    return requests.get(url).json()

threads = [threading.Thread(target=fetch_data, args=(url,)) for url in urls]
for t in threads: t.start()
for t in threads: t.join()

#MULTIPROCESSING - CPU bound tasks

def compute(n):
    return sum(i*i for i in range(n))

with multiprocessing.Pool() as pool:
    results = pool.map(compute, [10**6, 10**6, 10**6])


#ASYNCIO - Many concurrent I/O (best for APIs)
async def fetch_async(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
```
**When does it use??**
**Threading**: Gọi nhiều API cùng lúc, I/O bound( bị GIL hạn chế CPU)
**Multiprocessing**:Xử lý ảnh, ML inference, tính toán nặng
**AsyncIO**: Web server, chat app, many concurrent connections(Flask async, FastAPI)

------------------------------------------------------------------------------------


# 9. TYPE HINTS & DATACLASSES
> - **When does use it?**
**Dataclass**: Data containers, DTOs, replace simple classes
**Type hints**: Mọi hàm trong production code, IDE support, mypy checking


------------------------------------------------------------------------------------

# 10. PYTHON MEMORY MODEL

so sánh `is` và `==`:

`==` so sánh giá trị bằng cách gọi __eq()__, còn `is` so sánh địa chỉ bộ nhớ   -- dùng is chỉ khi check None, True, False




## FLASK & BACKEND - ÔN LUYỆN PHỎNG VẤN


## 1. FLASK cơ bản 
#### 1.1 App Factory Pattern

# app/__init__.py

**When does it use??**
> - Tránh circular imports khi app lớn
> - Cho phép tạo nhiều instance khác nhau(testing, prod, dev)
> - Đây là **best practice** cho Flask production apps

--------------------------------------------------------------------------------------------------------------------------

## 1.2 Blueprint Pattern

**When does it use?**
> - Chia code theo feature modules
> - Mỗi blueprint là 1 mini-app: auth, users, products, orders


--------------------------------------------------------------------------------------------------------------------------


## 2. REST API DESIGN

#### 2.1 Chuẩn RESTful

# RESTful Resource: /api/v1/users
``` python
GET      /users                        -> list users
GET      /users/{id}                   -> get user by id
POST     /users/                       -> create user
PUT      /users/{id}                   -> update (full replace)
PATCH    /users/{id}                   -> update (partial)
DELETE   /users/{id}                   -> delete


# Status codes quan trọng

200 OK
201 Created
204 No Content
400 Bad request
401 Unauthorized
403 Forbindden
404 Not Found
409 Conflict
422 Unprocessable
429 Too Many Requests
500 Internal Server
```

## DATABASE

### 1.SQL cơ bản và nâng cao

#### 1.1 JOINS - Loại và khi dùng
> - INNER JOIN: Chỉ lấy record có match ở cả 2 bảng

> - LEFT JOIN: Lấy tất cả từ bảng trái, NULL nếu k có match

> - RIGHT JOIN: Ngược lại LEFT JOIN
> - FULL OUTER JOIN: Tất cả từ cả 2 bảng 
> - CROSS JOIN: Tích Descartes(mọi cặp kết hợp)




##### II. MATLAB & MCR INTERGRATION - ÔN THI PHỎNG VẤN

**Tổng quan**: MATLAB(Matrix Laboratory) là ngôn ngữ lập trình và môi trường tính toán cho toán học, khoa học kĩ thuật , và xử lý dữ liệu.
Ưu điểm:
- Tối ưu hóa matrix/vector operations
- Built-in toolboxes: Signal Processing, Statistics, Machine Learning
- Tính toán số học chính xác cao
- Visualization mạnh mẽ

Trong dự án MBW:
- thuật toán scoring phức tạp phân tích candidate-job compatibility
-Ma trận dữ liệu ứng viên x yêu cầu công việc
- Hệ số phân tích đa biến(multivariate analysis)

**Kiến thức matlab cần nắm**

### Kiểu dữ liệu cơ bản

%Scalar

%Vector(hàng ngang)

%Matrix

%String

%Cell array(giống list trong python)

% Struct(giống dict trong python)

### Matrix Operations
A = [1, 2; 3, 4]
B = [4, 5; 6, 7]
%phép toán ma trận 
C = A + B;   % Cộng element-wise
D = A * B;   % Matrix multiplication (nhân ma trận thực sự)
E = A .* B;  % Element-wise multiplication( NOT matrix mult)
F = A ^ 2;   % Ma trận bình phương (A*A)
G = A .^ 2;  % Element-wise square

% Transpose
A_T = A';     % Transpose

% Inverse & Determinant
inv_A = inv(A);    % Ma trận nghịch đảo
det_A = det(A);    % Định thức

% Eigen values

[V, D] = eig(A);   %V:eigenvectors, D: eigenvalues(diagonal)

% Giải hệ phương trình Ax = b
b = [1; 2];
x = A \ b; Hiệu quả hơn inv(A)*b

% Kích thước
[rows, cols] = = size(A);
n = length(A);      % max(rows, cols)
total = numel(A);   %total element

**When does it use??**
> - `.`trước operator = element-wise (từng phần tử)
> - Không có `.` = matrix operation
> - `A \ b`: thay vì `inv(A)*b` -> nhanh hơn và chính xác hơn


### 2.3 Indexing và Slicing

Note:
A = [10, 20, 30; 40, 50, 60; 70, 80, 90];

- MATLAB  index bắt đầu từ 1 (khác Python bắt đầu từ 0)
A(1, 1) %= 10 (hàng 1 cột 1)
A(2, 3) *= 60 (hàng 2 cột 3)
A(end, end) = 90

- Slicing
A(1, :) % Hàng 1 toàn bộ: [10, 20, 30]
A(:, 2) % Cột 2 toàn bộ [20, 50, 80]
A(1:2,2:3) %sub-matrix [20, 30; 50,60]

- Linear indexing(column-major!)
A(1) %= 10 (cột 1 hàng 1)
A(4) %= 20 (cột 2 hàng 1) - khác Python
% Python: row-major(C-style)
% MATLAB: column-major (Fortran-style)

- logical indexing
v = [1, 5, 3, 8, 2];
v(v > 3)   $[5,8] - phần tử  > 3
v(logical([1,0,1,0,1]))  %[1, 3, 2]

Note:
tính điềm phù hợp của ứng viên với công việc


validate input 

tính trung bình của tất cả những tham số với từng vị trí trong matrix

