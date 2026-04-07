# ✂️ PYTHONIC CODE: NGHỆ THUẬT RÚT GỌN MÃ NGUỒN

Viết code ngắn gọn không chỉ để đẹp, mà còn để tăng hiệu năng và giúp bảo trì dễ dàng hơn. Dưới đây là những kỹ thuật "Senior" để biến 10 dòng code thành 1 dòng duy nhất.

---

## 📋 DANH MỤC CÁC KỸ THUẬT RÚT GỌN

### 1. 🏗️ Comprehensions (Thay thế vòng lặp for)
Thay vì dùng 4-5 dòng để tạo một danh sách mới, hãy dùng 1 dòng:
```python
# Cũ:
nums = []
for x in range(10):
    if x % 2 == 0:
        nums.append(x**2)

# Mới (Pythonic):
nums = [x**2 for x in range(10) if x % 2 == 0]
```

### 2. ⚡ Ternary Operator (Câu điều kiện 1 dòng)
```python
# Cũ:
if age >= 18:
    status = "Adult"
else:
    status = "Child"

# Mới:
status = "Adult" if age >= 18 else "Child"
```

### 3. 🧩 Lambda & Functional Programming
Dùng cho các hàm ngắn gọn nặc danh:
```python
# Sắp xếp danh sách user theo tuổi
users = [{"name": "A", "age": 20}, {"name": "B", "age": 15}]
users.sort(key=lambda u: u["age"])
```

### 4. 🐘 Walrus Operator `:=` (Gán và sử dụng ngay)
Kỹ thuật này cực kỳ hữu dụng trong các vòng lặp `while` hoặc câu lệnh `if`.
```python
# Cũ:
content = file.read()
if content:
    print(content)

# Mới (Python 3.8+):
if (content := file.read()):
    print(content)
```

### 5. 📦 Multiple Assignment (Gán nhiều biến cùng lúc)
```python
# Hoán đổi giá trị (Không cần biến trung gian)
a, b = b, a

# Unpacking list
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5
```

### 6. 🔍 any() & all() (Kiểm tra mảng cực gọn)
```python
# Kiểm tra xem có bất kỳ số nào > 10 không
nums = [1, 5, 12, 8]
if any(x > 10 for x in nums):
    print("Found!")
```

### 7. 🏷️ Chaining Comparison Operators (Ghép các so sánh)
```python
# Cũ:
if x > 10 and x < 20:
    pass

# Mới:
if 10 < x < 20:
    pass
```

### 8. 🛠️ Dùng `collections.defaultdict` (Tránh lỗi Key Error)
```python
from collections import defaultdict
# Cũ:
d = {}
for key in ['a', 'b', 'a']:
    if key not in d:
        d[key] = 0
    d[key] += 1

# Mới:
d = defaultdict(int) 
for key in ['a', 'b', 'a']:
    d[key] += 1
```

### 9. ⛓️ itertools (Xử lý vòng lặp lồng nhau)
Thay vì dùng 10 vòng lặp lồng nhau, hãy dùng `product`.
```python
import itertools
# Cũ:
for x in [1, 2]:
    for y in ['A', 'B']:
        print(x, y)

# Mới:
for x, y in itertools.product([1, 2], ['A', 'B']):
    print(x, y)
```

### 10. 🍕 Merging Dictionaries (Gộp từ điển siêu nhanh)
Sử dụng toán tử `|` (Python 3.9+).
```python
dict1 = {"a": 1}
dict2 = {"b": 2}
merged = dict1 | dict2
# Kết quả: {"a": 1, "b": 2}
```

### 11. 📊 collections.Counter (Đếm mọi thứ trong 1 dòng)
```python
from collections import Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
# Kết quả: Counter({'apple': 3, 'banana': 2, 'cherry': 1})
```

### 12. 🧵 str.join (Build chuỗi cực sạch)
Đừng bao giờ dùng toán tử `+` để nối chuỗi trong vòng lặp.
```python
# Cũ: "a" + ", " + "b" + ", " + "c"
items = ["Python", "Flask", "Django"]

# Mới: Tối ưu hiệu năng và cực ngắn
result = ", ".join(items)
```

### 13. 🎭 getattr (Thay thế chuỗi IF-ELIF dài dòng)
```python
# Cũ: 
if action == "run": app.run()
elif action == "stop": app.stop()

# Mới: Động và ngắn gọn
getattr(app, action, lambda: "Invalid Action")()
```

---
🚀 **Triết lý Master:** Code Pythonic không chỉ là viết ngắn, mà là viết **thông minh**. Một Senior sẽ biết khi nào dùng `lambda` và khi nào viết một hàm rõ ràng để giữ cho dự án luôn ở trạng thái tốt nhất!
