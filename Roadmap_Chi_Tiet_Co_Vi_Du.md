# ROADMAP TĂNG TỐC - GIẢI THÍCH CHI TIẾT VÀ VÍ DỤ THỰC HÀNH

File này giải thích chi tiết từng giai đoạn với ví dụ cụ thể để bạn có thể thực hành ngay

---


# GIAI ĐOẠN 1: NỀN TẢNG TỐC ĐỘ (Tháng 1-3)


# TUẦN 1-2: Tư duy lập trình + Python cơ bản


GIẢI THÍCH:
Đây là tuần đầu tiên, bạn cần làm quen với Python và cách máy tính "nghĩ".
Không cần học quá sâu, chỉ cần đủ để code được.

KIẾN THỨC CẦN HỌC:

1. Variables và Data Types
   Ví dụ:
   ```python
   # String
   name = "Nguyễn Văn A"
   age = 25  # Integer
   height = 1.75  # Float
   is_student = True  # Boolean
   
   # In ra màn hình
   print(f"Tên: {name}, Tuổi: {age}")
   ```

2. If/else và Loops
   Ví dụ:
   ```python
   # If/else
   score = 85
   if score >= 90:
       grade = "A"
   elif score >= 80:
       grade = "B"
   else:
       grade = "C"
   
   # For loop
   for i in range(1, 11):
       print(i)
   
   # While loop
   count = 0
   while count < 5:
       print(count)
       count += 1
   ```

3. Functions
   Ví dụ:
   ```python
   def calculate_total(price, tax_rate=0.1):
       """Tính tổng tiền bao gồm thuế"""
       total = price * (1 + tax_rate)
       return total
   
   result = calculate_total(1000)
   print(f"Tổng: {result}")  # 1100.0
   ```

4. List và Dictionary
   Ví dụ:
   ```python
   # List
   fruits = ["apple", "banana", "orange"]
   fruits.append("grape")
   print(fruits[0])  # "apple"
   
   # Dictionary
   student = {
       "name": "Nguyễn Văn A",
       "age": 20,
       "grades": [8.5, 9.0, 7.5]
   }
   print(student["name"])
   ```

BÀI TẬP THỰC HÀNH:

## Bài 1: Calculator App

Yêu cầu: Tạo máy tính đơn giản với các phép tính cơ bản

Code mẫu:
```python
def calculator():
    print("=== MÁY TÍNH ĐƠN GIẢN ===")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    
    choice = input("Chọn phép tính (1-4): ")
    num1 = float(input("Nhập số thứ nhất: "))
    num2 = float(input("Nhập số thứ hai: "))
    
    if choice == "1":
        result = num1 + num2
        print(f"Kết quả: {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"Kết quả: {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"Kết quả: {result}")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"Kết quả: {result}")
        else:
            print("Không thể chia cho 0!")
    else:
        print("Lựa chọn không hợp lệ!")

calculator()
```

## Bài 2: Todo List

Yêu cầu: Quản lý danh sách công việc

Code mẫu:
```python
todos = []

def add_todo():
    task = input("Nhập công việc mới: ")
    todos.append({"task": task, "done": False})
    print("Đã thêm công việc!")

def show_todos():
    if not todos:
        print("Danh sách trống!")
        return
    print("\n=== DANH SÁCH CÔNG VIỆC ===")
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["done"] else "○"
        print(f"{i}. {status} {todo['task']}")

def mark_done():
    show_todos()
    index = int(input("Chọn số thứ tự để đánh dấu hoàn thành: ")) - 1
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        print("Đã đánh dấu hoàn thành!")
    else:
        print("Số thứ tự không hợp lệ!")

def main():
    while True:
        print("\n=== TODO LIST ===")
        print("1. Thêm công việc")
        print("2. Xem danh sách")
        print("3. Đánh dấu hoàn thành")
        print("4. Thoát")
        
        choice = input("Chọn (1-4): ")
        if choice == "1":
            add_todo()
        elif choice == "2":
            show_todos()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            break
        else:
            print("Lựa chọn không hợp lệ!")

main()
```

LEETCODE EASY (20 bài đầu tiên):
1. Two Sum - https://leetcode.com/problems/two-sum/
   Ví dụ giải:
   ```python
   def twoSum(nums, target):
       seen = {}
       for i, num in enumerate(nums):
           complement = target - num
           if complement in seen:
               return [seen[complement], i]
           seen[num] = i
       return []
       ```
2. Reverse Integer - https://leetcode.com/problems/reverse-integer/
3. Palindrome Number - https://leetcode.com/problems/palindrome-number/`
4. Roman to Integer - https://leetcode.com/problems/roman-to-integer/
5. Valid Parentheses - https://leetcode.com/problems/valid-parentheses/

... (tiếp tục đến bài 20)

CHECKLIST TUẦN 1-2:
- [ ] Hoàn thành Calculator App
- [ ] Hoàn thành Todo List
- [ ] Giải được 20 bài LeetCode Easy
- [ ] Hiểu được variables, functions, loops
- [ ] Có thể đọc và viết code Python cơ bản

---



# TUẦN 3-4: Cấu trúc dữ liệu cơ bản


GIẢI THÍCH:
Bạn cần hiểu cách lưu trữ và tổ chức dữ liệu. Đây là nền tảng cho mọi thuật toán.

KIẾN THỨC CẦN HỌC:

1. Array/List (Đã học, nhưng cần hiểu sâu hơn)
   Ví dụ:
   ```python
   # Tạo list
   numbers = [1, 2, 3, 4, 5]
   
   # Truy cập
   print(numbers[0])  # 1
   print(numbers[-1])  # 5 (phần tử cuối)
   
   # Slice
   print(numbers[1:3])  # [2, 3]
   
   # Thao tác
   numbers.append(6)  # Thêm vào cuối
   numbers.insert(0, 0)  # Chèn vào vị trí 0
   numbers.remove(3)  # Xóa phần tử 3
   numbers.pop()  # Xóa phần tử cuối
   ```

2. Linked List (Implement từ đầu)
   Ví dụ:
   ```python
   class Node:
       def __init__(self, data):
           self.data = data
           self.next = None
   
   class LinkedList:
       def __init__(self):
           self.head = None
       
       def append(self, data):
           new_node = Node(data)
           if not self.head:
               self.head = new_node
               return
           current = self.head
           while current.next:
               current = current.next
           current.next = new_node
       
       def display(self):
           current = self.head
           while current:
               print(current.data, end=" -> ")
               current = current.next
           print("None")
       
       def search(self, data):
           current = self.head
           while current:
               if current.data == data:
                   return True
               current = current.next
           return False
   
   # Sử dụng
   ll = LinkedList()
   ll.append(1)
   ll.append(2)
   ll.append(3)
   ll.display()  # 1 -> 2 -> 3 -> None
   print(ll.search(2))  # True
   ```

3. Stack (Ngăn xếp - LIFO)
   Ví dụ:
   ```python
   class Stack:
       def __init__(self):
           self.items = []
       
       def push(self, item):
           self.items.append(item)
       
       def pop(self):
           if not self.is_empty():
               return self.items.pop()
           return None
       
       def peek(self):
           if not self.is_empty():
               return self.items[-1]
           return None
       
       def is_empty(self):
           return len(self.items) == 0
       
       def size(self):
           return len(self.items)
   
   # Sử dụng: Kiểm tra dấu ngoặc đúng
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
   
   print(is_balanced("()"))  # True
   print(is_balanced("([)]"))  # False
   ```

4. Queue (Hàng đợi - FIFO)
   Ví dụ:
   ```python
   class Queue:
       def __init__(self):
           self.items = []
       
       def enqueue(self, item):
           self.items.append(item)
       
       def dequeue(self):
           if not self.is_empty():
               return self.items.pop(0)
           return None
       
       def is_empty(self):
           return len(self.items) == 0
       
       def size(self):
           return len(self.items)
   
   # Sử dụng: Mô phỏng hàng đợi
   queue = Queue()
   queue.enqueue("Người 1")
   queue.enqueue("Người 2")
   print(queue.dequeue())  # "Người 1"
   ```

5. Hash Table/Dictionary (Đã học, nhưng hiểu cách hoạt động)
   Ví dụ:
   ```python
   # Dictionary trong Python là Hash Table
   # Hash function: chuyển key thành index
   
   class HashTable:
       def __init__(self, size=10):
           self.size = size
           self.table = [[] for _ in range(size)]
       
       def _hash(self, key):
           return hash(key) % self.size
       
       def insert(self, key, value):
           index = self._hash(key)
           for item in self.table[index]:
               if item[0] == key:
                   item[1] = value
                   return
           self.table[index].append([key, value])
       
       def get(self, key):
           index = self._hash(key)
           for item in self.table[index]:
               if item[0] == key:
                   return item[1]
           return None
   
   # Sử dụng
   ht = HashTable()
   ht.insert("name", "Nguyễn Văn A")
   ht.insert("age", 25)
   print(ht.get("name"))  # "Nguyễn Văn A"
   ```

6. Binary Tree cơ bản
   Ví dụ:
   ```python
   class TreeNode:
       def __init__(self, value):
           self.value = value
           self.left = None
           self.right = None
   
   class BinaryTree:
       def __init__(self):
           self.root = None
       
       def insert(self, value):
           if not self.root:
               self.root = TreeNode(value)
           else:
               self._insert(self.root, value)
       
       def _insert(self, node, value):
           if value < node.value:
               if node.left is None:
                   node.left = TreeNode(value)
               else:
                   self._insert(node.left, value)
           else:
               if node.right is None:
                   node.right = TreeNode(value)
               else:
                   self._insert(node.right, value)
       
       def inorder_traversal(self, node):
           if node:
               self.inorder_traversal(node.left)
               print(node.value, end=" ")
               self.inorder_traversal(node.right)
   
   # Sử dụng
   bt = BinaryTree()
   bt.insert(5)
   bt.insert(3)
   bt.insert(7)
   bt.insert(2)
   bt.inorder_traversal(bt.root)  # 2 3 5 7
   ```

BÀI TẬP THỰC HÀNH:

## Bài 1: Stack-based Calculator

Yêu cầu: Tính toán biểu thức hậu tố (postfix) bằng Stack

Ví dụ: "3 4 + 2 *" = (3+4)*2 = 14

Code mẫu:
```python
def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            # Pop 2 số
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    
    return stack[0]

# Test
print(evaluate_postfix("3 4 + 2 *"))  # 14
print(evaluate_postfix("5 1 2 + 4 * + 3 -"))  # 14
```

## Bài 2: Expression Parser

Yêu cầu: Chuyển biểu thức trung tố sang hậu tố

Code mẫu:
```python
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    
    for token in expression.split():
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:
            while stack and stack[-1] != '(' and \
                  precedence.get(token, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)

# Test
print(infix_to_postfix("3 + 4 * 2"))  # "3 4 2 * +"
```

LEETCODE EASY (30 bài tiếp theo):
21. Remove Duplicates from Sorted Array
22. Best Time to Buy and Sell Stock
23. Valid Anagram
24. Contains Duplicate
25. Two Sum II
... (tiếp tục đến bài 50)

CHECKLIST TUẦN 3-4:
- [ ] Implement được Linked List
- [ ] Implement được Stack và Queue
- [ ] Hiểu cách Hash Table hoạt động
- [ ] Implement được Binary Tree cơ bản
- [ ] Giải được 30 bài LeetCode Easy
- [ ] Build được Stack-based Calculator
- [ ] Build được Expression Parser

---



# TUẦN 5-6: Thuật toán cơ bản


GIẢI THÍCH:
Thuật toán là cách giải quyết vấn đề. Bạn cần hiểu các thuật toán cơ bản và khi nào dùng cái nào.

KIẾN THỨC CẦN HỌC:

1. Linear Search (Tìm kiếm tuyến tính)
   Ví dụ:
   ```python
   def linear_search(arr, target):
       for i, value in enumerate(arr):
           if value == target:
               return i
       return -1
   
   # Độ phức tạp: O(n)
   ```

2. Binary Search (Tìm kiếm nhị phân - chỉ cho mảng đã sắp xếp)
   Ví dụ:
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
   
   # Độ phức tạp: O(log n)
   # Test
   arr = [1, 3, 5, 7, 9, 11, 13]
   print(binary_search(arr, 7))  # 3
   ```

3. Bubble Sort (Sắp xếp nổi bọt)
   Ví dụ:
   ```python
   def bubble_sort(arr):
       n = len(arr)
       for i in range(n):
           for j in range(0, n - i - 1):
               if arr[j] > arr[j + 1]:
                   arr[j], arr[j + 1] = arr[j + 1], arr[j]
       return arr
   
   # Độ phức tạp: O(n²)
   # Test
   arr = [64, 34, 25, 12, 22, 11, 90]
   print(bubble_sort(arr))  # [11, 12, 22, 25, 34, 64, 90]
   ```

4. Merge Sort (Sắp xếp trộn)
   Ví dụ:
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
   
   # Độ phức tạp: O(n log n)
   ```

5. Quick Sort (Sắp xếp nhanh)
   Ví dụ:
   ```python
   def quick_sort(arr):
       if len(arr) <= 1:
           return arr
       
       pivot = arr[len(arr) // 2]
       left = [x for x in arr if x < pivot]
       middle = [x for x in arr if x == pivot]
       right = [x for x in arr if x > pivot]
       
       return quick_sort(left) + middle + quick_sort(right)
   
   # Độ phức tạp: O(n log n) average, O(n²) worst case
   ```

6. Recursion (Đệ quy)
   Ví dụ:
   ```python
   # Tính giai thừa
   def factorial(n):
       if n <= 1:
           return 1
       return n * factorial(n - 1)
   
   # Fibonacci
   def fibonacci(n):
       if n <= 1:
           return n
       return fibonacci(n - 1) + fibonacci(n - 2)
   
   # Tối ưu với memoization
   memo = {}
   def fibonacci_memo(n):
       if n in memo:
           return memo[n]
       if n <= 1:
           return n
       memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
       return memo[n]
   ```

7. Big O Notation (Hiểu cơ bản)
   - O(1): Constant - Truy cập phần tử trong array
   - O(log n): Logarithmic - Binary search
   - O(n): Linear - Linear search
   - O(n log n): Linearithmic - Merge sort, Quick sort
   - O(n²): Quadratic - Bubble sort, nested loops
   - O(2^n): Exponential - Recursive Fibonacci (không tối ưu)

BÀI TẬP THỰC HÀNH:

## Bài 1: Sorting Visualizer

Yêu cầu: Visualize các thuật toán sắp xếp (có thể dùng matplotlib)

Code mẫu (console version):
```python
import time

def visualize_sort(arr, algorithm_name):
    print(f"\n{algorithm_name}:")
    print(f"Trước: {arr}")
    
    start = time.time()
    sorted_arr = quick_sort(arr.copy())
    end = time.time()
    
    print(f"Sau: {sorted_arr}")
    print(f"Thời gian: {end - start:.6f} giây")
    print(f"Độ dài: {len(arr)} phần tử")

# Test với các kích thước khác nhau
sizes = [10, 100, 1000]
for size in sizes:
    import random
    arr = [random.randint(1, 1000) for _ in range(size)]
    visualize_sort(arr, f"Quick Sort ({size} phần tử)")
```

LEETCODE EASY (30 bài tiếp theo):
51. Climbing Stairs
52. House Robber
53. Maximum Subarray
54. Best Time to Buy and Sell Stock
55. Contains Duplicate
... (tiếp tục đến bài 80)

CHECKLIST TUẦN 5-6:
- [ ] Implement được các thuật toán tìm kiếm
- [ ] Implement được các thuật toán sắp xếp
- [ ] Hiểu được recursion
- [ ] Hiểu được Big O Notation
- [ ] Giải được 30 bài LeetCode Easy
- [ ] Build được Sorting Visualizer

---



# TUẦN 7-8: OOP và Design Patterns cơ bản


GIẢI THÍCH:
OOP giúp code dễ quản lý và tái sử dụng. Design Patterns là các giải pháp cho các vấn đề thường gặp.

KIẾN THỨC CẦN HỌC:

1. OOP - Class và Object
   Ví dụ:
   ```python
   class BankAccount:
       def __init__(self, account_number, balance=0):
           self.account_number = account_number
           self._balance = balance  # Protected
       
       def deposit(self, amount):
           if amount > 0:
               self._balance += amount
               return f"Đã gửi {amount}. Số dư: {self._balance}"
           return "Số tiền không hợp lệ"
       
       def withdraw(self, amount):
           if 0 < amount <= self._balance:
               self._balance -= amount
               return f"Đã rút {amount}. Số dư: {self._balance}"
           return "Số dư không đủ"
       
       def get_balance(self):
           return self._balance
   
   # Sử dụng
   account = BankAccount("123456", 1000)
   print(account.deposit(500))
   print(account.withdraw(200))
   ```

2. Inheritance (Kế thừa)
   Ví dụ:
   ```python
   class Animal:
       def __init__(self, name):
           self.name = name
       
       def speak(self):
           return "Some sound"
   
   class Dog(Animal):
       def speak(self):
           return f"{self.name} says Woof!"
   
   class Cat(Animal):
       def speak(self):
           return f"{self.name} says Meow!"
   
   # Sử dụng
   dog = Dog("Buddy")
   cat = Cat("Whiskers")
   print(dog.speak())  # "Buddy says Woof!"
   print(cat.speak())  # "Whiskers says Meow!"
   ```

3. Design Pattern: Singleton
   Ví dụ:
   ```python
   class Database:
       _instance = None
       
       def __new__(cls):
           if cls._instance is None:
               cls._instance = super().__new__(cls)
           return cls._instance
       
       def connect(self):
           print("Connected to database")
   
   # Sử dụng - chỉ có 1 instance
   db1 = Database()
   db2 = Database()
   print(db1 is db2)  # True
   ```

4. Design Pattern: Factory
   Ví dụ:
   ```python
   class AnimalFactory:
       @staticmethod
       def create_animal(animal_type, name):
           if animal_type == "dog":
               return Dog(name)
           elif animal_type == "cat":
               return Cat(name)
           else:
               raise ValueError("Unknown animal type")
   
   # Sử dụng
   dog = AnimalFactory.create_animal("dog", "Buddy")
   cat = AnimalFactory.create_animal("cat", "Whiskers")
   ```

5. Design Pattern: Observer
   Ví dụ:
   ```python
   class Subject:
       def __init__(self):
           self._observers = []
       
       def attach(self, observer):
           self._observers.append(observer)
       
       def notify(self, message):
           for observer in self._observers:
               observer.update(message)
   
   class EmailObserver:
       def update(self, message):
           print(f"Email: {message}")
   
   class SMSObserver:
       def update(self, message):
           print(f"SMS: {message}")
   
   # Sử dụng
   news = Subject()
   news.attach(EmailObserver())
   news.attach(SMSObserver())
   news.notify("Breaking news!")
   ```

BÀI TẬP THỰC HÀNH:

## Bài 1: Library Management System với OOP

Yêu cầu: Quản lý thư viện với OOP

Code mẫu:
```python
class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def return_book(self):
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}
    
    def add_book(self, book):
        self.books[book.isbn] = book
    
    def borrow_book(self, isbn, borrower_id):
        if isbn in self.books:
            book = self.books[isbn]
            if book.borrow():
                if borrower_id not in self.borrowers:
                    self.borrowers[borrower_id] = []
                self.borrowers[borrower_id].append(isbn)
                return f"Đã mượn: {book.title}"
            return "Sách đã được mượn"
        return "Không tìm thấy sách"
    
    def return_book(self, isbn, borrower_id):
        if isbn in self.books and borrower_id in self.borrowers:
            if isbn in self.borrowers[borrower_id]:
                self.books[isbn].return_book()
                self.borrowers[borrower_id].remove(isbn)
                return "Đã trả sách"
        return "Không tìm thấy"

# Sử dụng
library = Library()
book1 = Book("123", "Python Guide", "Author A")
book2 = Book("456", "JavaScript Guide", "Author B")
library.add_book(book1)
library.add_book(book2)

print(library.borrow_book("123", "user1"))
print(library.borrow_book("123", "user2"))  # Đã được mượn
```

CHECKLIST TUẦN 7-8:
- [ ] Hiểu và áp dụng được OOP
- [ ] Implement được 3 Design Patterns
- [ ] Refactor được projects cũ với OOP
- [ ] Build được Library Management System
- [ ] Code có cấu trúc tốt hơn

---



# TUẦN 9-12: Database và Git


GIẢI THÍCH:
Database để lưu trữ dữ liệu. Git để quản lý code. Cả hai đều cực kỳ quan trọng.

KIẾN THỨC CẦN HỌC:

1. SQL cơ bản
   Ví dụ:
   ```sql
   -- Tạo bảng
   CREATE TABLE users (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       email VARCHAR(100) UNIQUE,
       age INTEGER
   );
   
   -- INSERT
   INSERT INTO users (name, email, age) 
   VALUES ('Nguyễn Văn A', 'a@email.com', 25);
   
   -- SELECT
   SELECT * FROM users;
   SELECT name, email FROM users WHERE age > 20;
   
   -- UPDATE
   UPDATE users SET age = 26 WHERE id = 1;
   
   -- DELETE
   DELETE FROM users WHERE id = 1;
   
   -- JOIN
   SELECT u.name, o.total 
   FROM users u
   INNER JOIN orders o ON u.id = o.user_id;
   
   -- Aggregate
   SELECT COUNT(*) as total_users, AVG(age) as avg_age
   FROM users;
   ```

2. Git Commands
   Ví dụ:
   ```bash
   # Khởi tạo
   git init
   
   # Thêm file
   git add .
   git add file.py
   
   # Commit
   git commit -m "Add calculator app"
   
   # Xem lịch sử
   git log
   git log --oneline
   
   # Branch
   git branch feature/new-feature
   git checkout feature/new-feature
   git checkout -b feature/new-feature  # Tạo và chuyển
   
   # Merge
   git merge feature/new-feature
   
   # Remote
   git remote add origin https://github.com/user/repo.git
   git push origin main
   git pull origin main
   ```

BÀI TẬP THỰC HÀNH:

## Bài 1: Blog với CRUD + Database

Yêu cầu: Blog đơn giản với PostgreSQL

Code mẫu (Python với psycopg2):
```python
import psycopg2
from psycopg2 import sql

class BlogDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="blog",
            user="postgres",
            password="password"
        )
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                content TEXT,
                author VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()
    
    def create_post(self, title, content, author):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO posts (title, content, author)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (title, content, author))
        post_id = cursor.fetchone()[0]
        self.conn.commit()
        return post_id
    
    def get_all_posts(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
        return cursor.fetchall()
    
    def get_post(self, post_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = %s", (post_id,))
        return cursor.fetchone()
    
    def update_post(self, post_id, title, content):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE posts 
            SET title = %s, content = %s
            WHERE id = %s
        """, (title, content, post_id))
        self.conn.commit()
    
    def delete_post(self, post_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM posts WHERE id = %s", (post_id,))
        self.conn.commit()

# Sử dụng
blog = BlogDB()
post_id = blog.create_post("Hello World", "My first post", "Author")
posts = blog.get_all_posts()
print(posts)
```

CHECKLIST TUẦN 9-12:
- [ ] Viết được SQL queries cơ bản
- [ ] Setup được PostgreSQL/MySQL
- [ ] Thành thạo Git commands
- [ ] Tạo được GitHub account
- [ ] Build được Blog với Database
- [ ] Deploy được lên Heroku/Vercel
- [ ] Giải được 80+ bài LeetCode Easy

---


# GIAI ĐOẠN 2: FULL STACK WEB (Tháng 4-9)


# THÁNG 4: Frontend Foundation


# TUẦN 1-2: HTML5, CSS3, JavaScript ES6+


GIẢI THÍCH:
Đây là nền tảng của web. Bạn cần thành thạo để build giao diện đẹp và responsive.

KIẾN THỨC CẦN HỌC:

1. HTML5 Semantic Elements
   Ví dụ:
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
                   <li><a href="#home">Home</a></li>
                   <li><a href="#about">About</a></li>
               </ul>
           </nav>
       </header>
       
       <main>
           <article>
               <h1>Article Title</h1>
               <p>Content here...</p>
           </article>
           
           <aside>
               <h2>Sidebar</h2>
           </aside>
       </main>
       
       <footer>
           <p>&copy; 2025</p>
       </footer>
   </body>
   </html>
   ```

2. CSS3 Flexbox
   Ví dụ:
   ```css
   .container {
       display: flex;
       flex-direction: row;  /* hoặc column */
       justify-content: center;  /* main axis */
       align-items: center;  /* cross axis */
       flex-wrap: wrap;
       gap: 20px;
   }
   
   .item {
       flex: 1;  /* grow, shrink, basis */
       min-width: 200px;
   }
   ```

3. CSS3 Grid
   Ví dụ:
   ```css
   .grid-container {
       display: grid;
       grid-template-columns: repeat(3, 1fr);
       grid-template-rows: auto;
       gap: 20px;
   }
   
   .item-1 {
       grid-column: span 2;
       grid-row: span 2;
   }
   ```

4. Responsive Design
   Ví dụ:
   ```css
   /* Mobile first */
   .container {
       padding: 10px;
   }
   
   /* Tablet */
   @media (min-width: 768px) {
       .container {
           padding: 20px;
       }
   }
   
   /* Desktop */
   @media (min-width: 1024px) {
       .container {
           padding: 40px;
           max-width: 1200px;
           margin: 0 auto;
       }
   }
   ```

5. JavaScript ES6+
   Ví dụ:
   ```javascript
   // Arrow functions
   const add = (a, b) => a + b;
   
   // Destructuring
   const {name, age} = user;
   const [first, second] = array;
   
   // Spread operator
   const newArray = [...oldArray, newItem];
   const newObj = {...oldObj, newProp: value};
   
   // Template literals
   const message = `Hello, ${name}!`;
   
   // Promises
   fetch('/api/data')
       .then(response => response.json())
       .then(data => console.log(data))
       .catch(error => console.error(error));
   
   // Async/Await
   async function fetchData() {
       try {
           const response = await fetch('/api/data');
           const data = await response.json();
           return data;
       } catch (error) {
           console.error(error);
       }
   }
   ```

BÀI TẬP THỰC HÀNH:

## Bài 1: Responsive Landing Page

Yêu cầu: Tạo landing page responsive với HTML/CSS/JS

File: index.html
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Landing Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="logo">MyBrand</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section id="home" class="hero">
            <h1>Welcome to My Website</h1>
            <p>Building amazing web experiences</p>
            <button class="cta-button">Get Started</button>
        </section>
        
        <section id="about" class="about">
            <h2>About Us</h2>
            <p>We are a team of passionate developers...</p>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2025 MyBrand. All rights reserved.</p>
    </footer>
    
    <script src="script.js"></script>
</body>
</html>
```

File: styles.css
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background: #333;
    color: white;
}

.nav-links {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-links a {
    color: white;
    text-decoration: none;
}

.hero {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    text-align: center;
}

.cta-button {
    padding: 1rem 2rem;
    font-size: 1.2rem;
    background: #ff6b6b;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 1rem;
}

.cta-button:hover {
    background: #ff5252;
}

/* Responsive */
@media (max-width: 768px) {
    .nav-links {
        flex-direction: column;
        gap: 1rem;
    }
    
    .hero h1 {
        font-size: 2rem;
    }
}
```

File: script.js
```javascript
// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// CTA Button click
document.querySelector('.cta-button').addEventListener('click', () => {
    alert('Thank you for your interest!');
});
```

# TUẦN 3-4: React Basics


GIẢI THÍCH:
React là framework phổ biến nhất cho frontend. Học React sẽ giúp bạn build ứng dụng web hiện đại.

KIẾN THỨC CẦN HỌC:

1. Components
   Ví dụ:
   ```jsx
   // Functional Component
   function Welcome(props) {
       return <h1>Hello, {props.name}!</h1>;
   }
   
   // Arrow function
   const Welcome = (props) => {
       return <h1>Hello, {props.name}!</h1>;
   }
   
   // Sử dụng
   <Welcome name="Nguyễn Văn A" />
   ```

2. Props
   Ví dụ:
   ```jsx
   function UserCard({ name, email, age }) {
       return (
           <div className="user-card">
               <h2>{name}</h2>
               <p>Email: {email}</p>
               <p>Age: {age}</p>
           </div>
       );
   }
   
   // Sử dụng
   <UserCard name="Nguyễn Văn A" email="a@email.com" age={25} />
   ```

3. State với useState
   Ví dụ:
   ```jsx
   import { useState } from 'react';
   
   function Counter() {
       const [count, setCount] = useState(0);
       
       return (
           <div>
               <p>Count: {count}</p>
               <button onClick={() => setCount(count + 1)}>
                   Increment
               </button>
               <button onClick={() => setCount(count - 1)}>
                   Decrement
               </button>
           </div>
       );
   }
   ```

4. useEffect
   Ví dụ:
   ```jsx
   import { useState, useEffect } from 'react';
   
   function UserProfile({ userId }) {
       const [user, setUser] = useState(null);
       const [loading, setLoading] = useState(true);
       
       useEffect(() => {
           fetch(`/api/users/${userId}`)
               .then(res => res.json())
               .then(data => {
                   setUser(data);
                   setLoading(false);
               });
       }, [userId]);  // Chạy lại khi userId thay đổi
       
       if (loading) return <div>Loading...</div>;
       if (!user) return <div>User not found</div>;
       
       return <div>{user.name}</div>;
   }
   ```

5. React Router
   Ví dụ:
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
               </Routes>
           </BrowserRouter>
       );
   }
   ```

BÀI TẬP THỰC HÀNH:

## Bài 1: Todo App với React

File: src/App.js
```jsx
import { useState } from 'react';
import './App.css';

function App() {
    const [todos, setTodos] = useState([]);
    const [input, setInput] = useState('');
    
    const addTodo = () => {
        if (input.trim()) {
            setTodos([...todos, {
                id: Date.now(),
                text: input,
                completed: false
            }]);
            setInput('');
        }
    };
    
    const toggleTodo = (id) => {
        setTodos(todos.map(todo =>
            todo.id === id ? { ...todo, completed: !todo.completed } : todo
        ));
    };
    
    const deleteTodo = (id) => {
        setTodos(todos.filter(todo => todo.id !== id));
    };
    
    return (
        <div className="App">
            <h1>Todo App</h1>
            <div className="todo-input">
                <input
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && addTodo()}
                    placeholder="Add a todo..."
                />
                <button onClick={addTodo}>Add</button>
            </div>
            <ul className="todo-list">
                {todos.map(todo => (
                    <li key={todo.id} className={todo.completed ? 'completed' : ''}>
                        <span onClick={() => toggleTodo(todo.id)}>
                            {todo.text}
                        </span>
                        <button onClick={() => deleteTodo(todo.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
```

File: src/App.css
```css
.App {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
}

.todo-input {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
}

.todo-input input {
    flex: 1;
    padding: 10px;
    font-size: 16px;
}

.todo-input button {
    padding: 10px 20px;
    background: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
}

.todo-list {
    list-style: none;
    padding: 0;
}

.todo-list li {
    display: flex;
    justify-content: space-between;
    padding: 10px;
    margin-bottom: 10px;
    background: #f5f5f5;
    border-radius: 5px;
}

.todo-list li.completed span {
    text-decoration: line-through;
    color: #999;
}

.todo-list button {
    background: #f44336;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
}
```

CHECKLIST THÁNG 4:
- [ ] Tạo được responsive landing page
- [ ] Hiểu được React components
- [ ] Sử dụng được useState và useEffect
- [ ] Build được Todo App với React
- [ ] Build được Blog Frontend với React Router

---



# THÁNG 5: Backend Foundation


# TUẦN 1-2: Node.js + Express


GIẢI THÍCH:
Backend là phần xử lý logic và dữ liệu. Express là framework phổ biến nhất cho Node.js.

KIẾN THỨC CẦN HỌC:

1. Node.js Basics
   Ví dụ:
   ```javascript
   // File: server.js
   const http = require('http');
   
   const server = http.createServer((req, res) => {
       res.writeHead(200, { 'Content-Type': 'text/plain' });
       res.end('Hello World');
   });
   
   server.listen(3000, () => {
       console.log('Server running on port 3000');
   });
   ```

2. Express Framework
   Ví dụ:
   ```javascript
   // File: app.js
   const express = require('express');
   const app = express();
   
   // Middleware để parse JSON
   app.use(express.json());
   
   // Routes
   app.get('/', (req, res) => {
       res.json({ message: 'Hello World' });
   });
   
   app.get('/api/users', (req, res) => {
       res.json([
           { id: 1, name: 'Nguyễn Văn A' },
           { id: 2, name: 'Trần Thị B' }
       ]);
   });
   
   app.post('/api/users', (req, res) => {
       const { name, email } = req.body;
       // Lưu vào database
       res.status(201).json({ id: 3, name, email });
   });
   
   app.listen(3000, () => {
       console.log('Server running on port 3000');
   });
   ```

3. RESTful API Design
   Ví dụ:
   ```javascript
   // GET /api/users - Lấy danh sách
   app.get('/api/users', async (req, res) => {
       try {
           const users = await User.find();
           res.json(users);
       } catch (error) {
           res.status(500).json({ error: error.message });
       }
   });
   
   // GET /api/users/:id - Lấy một user
   app.get('/api/users/:id', async (req, res) => {
       try {
           const user = await User.findById(req.params.id);
           if (!user) {
               return res.status(404).json({ error: 'User not found' });
           }
           res.json(user);
       } catch (error) {
           res.status(500).json({ error: error.message });
       }
   });
   
   // POST /api/users - Tạo user mới
   app.post('/api/users', async (req, res) => {
       try {
           const user = new User(req.body);
           await user.save();
           res.status(201).json(user);
       } catch (error) {
           res.status(400).json({ error: error.message });
       }
   });
   
   // PUT /api/users/:id - Cập nhật user
   app.put('/api/users/:id', async (req, res) => {
       try {
           const user = await User.findByIdAndUpdate(
               req.params.id,
               req.body,
               { new: true }
           );
           if (!user) {
               return res.status(404).json({ error: 'User not found' });
           }
           res.json(user);
       } catch (error) {
           res.status(400).json({ error: error.message });
       }
   });
   
   // DELETE /api/users/:id - Xóa user
   app.delete('/api/users/:id', async (req, res) => {
       try {
           const user = await User.findByIdAndDelete(req.params.id);
           if (!user) {
               return res.status(404).json({ error: 'User not found' });
           }
           res.json({ message: 'User deleted' });
       } catch (error) {
           res.status(500).json({ error: error.message });
       }
   });
   ```

4. Middleware
   Ví dụ:
   ```javascript
   // Logger middleware
   const logger = (req, res, next) => {
       console.log(`${req.method} ${req.path} - ${new Date()}`);
       next();
   };
   app.use(logger);
   
   // Error handling middleware
   app.use((err, req, res, next) => {
       console.error(err.stack);
       res.status(500).json({ error: 'Something went wrong!' });
   });
   
   // Authentication middleware
   const authenticate = (req, res, next) => {
       const token = req.headers.authorization?.split(' ')[1];
       if (!token) {
           return res.status(401).json({ error: 'Unauthorized' });
       }
       // Verify token
       req.user = decodedToken;
       next();
   };
   ```

BÀI TẬP THỰC HÀNH:

## Bài 1: REST API cho Blog

File: server.js
```javascript
const express = require('express');
const app = express();
app.use(express.json());

// In-memory database (sẽ thay bằng MongoDB sau)
let posts = [];
let nextId = 1;

// GET /api/posts
app.get('/api/posts', (req, res) => {
    res.json(posts);
});

// GET /api/posts/:id
app.get('/api/posts/:id', (req, res) => {
    const post = posts.find(p => p.id === parseInt(req.params.id));
    if (!post) {
        return res.status(404).json({ error: 'Post not found' });
    }
    res.json(post);
});

// POST /api/posts
app.post('/api/posts', (req, res) => {
    const { title, content, author } = req.body;
    if (!title || !content) {
        return res.status(400).json({ error: 'Title and content required' });
    }
    const post = {
        id: nextId++,
        title,
        content,
        author: author || 'Anonymous',
        createdAt: new Date()
    };
    posts.push(post);
    res.status(201).json(post);
});

// PUT /api/posts/:id
app.put('/api/posts/:id', (req, res) => {
    const post = posts.find(p => p.id === parseInt(req.params.id));
    if (!post) {
        return res.status(404).json({ error: 'Post not found' });
    }
    post.title = req.body.title || post.title;
    post.content = req.body.content || post.content;
    res.json(post);
});

// DELETE /api/posts/:id
app.delete('/api/posts/:id', (req, res) => {
    const index = posts.findIndex(p => p.id === parseInt(req.params.id));
    if (index === -1) {
        return res.status(404).json({ error: 'Post not found' });
    }
    posts.splice(index, 1);
    res.json({ message: 'Post deleted' });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
```

Test với Postman hoặc curl:
```bash
# Tạo post
curl -X POST http://localhost:3000/api/posts \
  -H "Content-Type: application/json" \
  -d '{"title":"Hello","content":"World","author":"Author"}'

# Lấy tất cả posts
curl http://localhost:3000/api/posts
```

# TUẦN 3-4: Database Integration


GIẢI THÍCH:
Cần lưu trữ dữ liệu vào database thật. Chọn MongoDB (NoSQL) hoặc PostgreSQL (SQL).

KIẾN THỨC CẦN HỌC:

1. MongoDB với Mongoose
   Ví dụ:
   ```javascript
   // File: models/Post.js
   const mongoose = require('mongoose');
   
   const postSchema = new mongoose.Schema({
       title: { type: String, required: true },
       content: { type: String, required: true },
       author: { type: String, default: 'Anonymous' },
       createdAt: { type: Date, default: Date.now }
   });
   
   module.exports = mongoose.model('Post', postSchema);
   ```

   ```javascript
   // File: server.js
   const mongoose = require('mongoose');
   const Post = require('./models/Post');
   
   // Kết nối MongoDB
   mongoose.connect('mongodb://localhost:27017/blog', {
       useNewUrlParser: true,
       useUnifiedTopology: true
   });
   
   // Sử dụng trong routes
   app.get('/api/posts', async (req, res) => {
       try {
           const posts = await Post.find();
           res.json(posts);
       } catch (error) {
           res.status(500).json({ error: error.message });
       }
   });
   
   app.post('/api/posts', async (req, res) => {
       try {
           const post = new Post(req.body);
           await post.save();
           res.status(201).json(post);
       } catch (error) {
           res.status(400).json({ error: error.message });
       }
   });
   ```

2. PostgreSQL với Sequelize
   Ví dụ:
   ```javascript
   // File: models/Post.js
   const { Sequelize, DataTypes } = require('sequelize');
   const sequelize = new Sequelize('blog', 'user', 'password', {
       host: 'localhost',
       dialect: 'postgres'
   });
   
   const Post = sequelize.define('Post', {
       title: { type: DataTypes.STRING, allowNull: false },
       content: { type: DataTypes.TEXT, allowNull: false },
       author: { type: DataTypes.STRING, defaultValue: 'Anonymous' }
   });
   
   module.exports = Post;
   ```

3. Authentication với JWT
   Ví dụ:
   ```javascript
   const jwt = require('jsonwebtoken');
   const bcrypt = require('bcrypt');
   
   // Register
   app.post('/api/auth/register', async (req, res) => {
       const { email, password } = req.body;
       const hashedPassword = await bcrypt.hash(password, 10);
       
       const user = new User({ email, password: hashedPassword });
       await user.save();
       
       const token = jwt.sign({ userId: user._id }, 'secret', { expiresIn: '1h' });
       res.json({ token, user: { id: user._id, email } });
   });
   
   // Login
   app.post('/api/auth/login', async (req, res) => {
       const { email, password } = req.body;
       const user = await User.findOne({ email });
       
       if (!user || !await bcrypt.compare(password, user.password)) {
           return res.status(401).json({ error: 'Invalid credentials' });
       }
       
       const token = jwt.sign({ userId: user._id }, 'secret', { expiresIn: '1h' });
       res.json({ token, user: { id: user._id, email } });
   });
   
   // Middleware để verify token
   const authenticate = (req, res, next) => {
       const token = req.headers.authorization?.split(' ')[1];
       if (!token) {
           return res.status(401).json({ error: 'No token provided' });
       }
       
       try {
           const decoded = jwt.verify(token, 'secret');
           req.userId = decoded.userId;
           next();
       } catch (error) {
           res.status(401).json({ error: 'Invalid token' });
       }
   };
   
   // Protected route
   app.post('/api/posts', authenticate, async (req, res) => {
       const post = new Post({ ...req.body, author: req.userId });
       await post.save();
       res.status(201).json(post);
   });
   ```

BÀI TẬP THỰC HÀNH:

## Bài 1: Hoàn thiện Blog API với MongoDB

File: package.json
```json
{
  "name": "blog-api",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.18.0",
    "mongoose": "^7.0.0",
    "jsonwebtoken": "^9.0.0",
    "bcrypt": "^5.1.0"
  }
}
```

File: server.js (hoàn chỉnh)
```javascript
const express = require('express');
const mongoose = require('mongoose');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const app = express();
app.use(express.json());

// Kết nối MongoDB
mongoose.connect('mongodb://localhost:27017/blog');

// Models
const User = mongoose.model('User', new mongoose.Schema({
    email: String,
    password: String
}));

const Post = mongoose.model('Post', new mongoose.Schema({
    title: String,
    content: String,
    author: String,
    createdAt: { type: Date, default: Date.now }
}));

// Auth routes
app.post('/api/auth/register', async (req, res) => {
    const { email, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const user = new User({ email, password: hashedPassword });
    await user.save();
    const token = jwt.sign({ userId: user._id }, 'secret');
    res.json({ token });
});

app.post('/api/auth/login', async (req, res) => {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user || !await bcrypt.compare(password, user.password)) {
        return res.status(401).json({ error: 'Invalid credentials' });
    }
    const token = jwt.sign({ userId: user._id }, 'secret');
    res.json({ token });
});

// Middleware
const authenticate = (req, res, next) => {
    const token = req.headers.authorization?.split(' ')[1];
    if (!token) return res.status(401).json({ error: 'Unauthorized' });
    try {
        req.userId = jwt.verify(token, 'secret').userId;
        next();
    } catch (error) {
        res.status(401).json({ error: 'Invalid token' });
    }
};

// Post routes
app.get('/api/posts', async (req, res) => {
    const posts = await Post.find();
    res.json(posts);
});

app.post('/api/posts', authenticate, async (req, res) => {
    const post = new Post({ ...req.body, author: req.userId });
    await post.save();
    res.status(201).json(post);
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

CHECKLIST THÁNG 5:
- [ ] Setup được Express server
- [ ] Tạo được RESTful API
- [ ] Kết nối được với MongoDB/PostgreSQL
- [ ] Implement được JWT authentication
- [ ] Build được Blog API hoàn chỉnh

---



# THÁNG 6: Full Stack Integration


GIẢI THÍCH:
Kết nối Frontend (React) với Backend (Node.js) để tạo ứng dụng hoàn chỉnh.

KIẾN THỨC CẦN HỌC:

1. API Integration trong React
   Ví dụ:
   ```jsx
   // File: src/services/api.js
   const API_URL = 'http://localhost:3000/api';
   
   export const fetchPosts = async () => {
       const response = await fetch(`${API_URL}/posts`);
       if (!response.ok) throw new Error('Failed to fetch posts');
       return response.json();
   };
   
   export const createPost = async (post, token) => {
       const response = await fetch(`${API_URL}/posts`, {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
               'Authorization': `Bearer ${token}`
           },
           body: JSON.stringify(post)
       });
       if (!response.ok) throw new Error('Failed to create post');
       return response.json();
   };
   ```

2. State Management với Context API
   Ví dụ:
   ```jsx
   // File: src/context/AuthContext.js
   import { createContext, useState, useContext } from 'react';
   
   const AuthContext = createContext();
   
   export function AuthProvider({ children }) {
       const [user, setUser] = useState(null);
       const [token, setToken] = useState(localStorage.getItem('token'));
       
       const login = async (email, password) => {
           const response = await fetch('http://localhost:3000/api/auth/login', {
               method: 'POST',
               headers: { 'Content-Type': 'application/json' },
               body: JSON.stringify({ email, password })
           });
           const data = await response.json();
           setToken(data.token);
           setUser(data.user);
           localStorage.setItem('token', data.token);
       };
       
       const logout = () => {
           setToken(null);
           setUser(null);
           localStorage.removeItem('token');
       };
       
       return (
           <AuthContext.Provider value={{ user, token, login, logout }}>
               {children}
           </AuthContext.Provider>
       );
   }
   
   export const useAuth = () => useContext(AuthContext);
   ```

3. Protected Routes
   Ví dụ:
   ```jsx
   // File: src/components/ProtectedRoute.js
   import { Navigate } from 'react-router-dom';
   import { useAuth } from '../context/AuthContext';
   
   function ProtectedRoute({ children }) {
       const { token } = useAuth();
       return token ? children : <Navigate to="/login" />;
   }
   
   // Sử dụng
   <Route path="/dashboard" element={
       <ProtectedRoute>
           <Dashboard />
       </ProtectedRoute>
   } />
   ```

BÀI TẬP THỰC HÀNH:

## Bài 1: Full Stack E-commerce MVP

Cấu trúc project:
```
ecommerce/
├── backend/
│   ├── server.js
│   ├── models/
│   │   ├── User.js
│   │   ├── Product.js
│   │   └── Order.js
│   └── routes/
│       ├── auth.js
│       ├── products.js
│       └── orders.js
└── frontend/
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   ├── context/
    │   └── services/
    └── package.json
```

Backend: server.js
```javascript
const express = require('express');
const mongoose = require('mongoose');
const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/ecommerce');

// Models
const Product = mongoose.model('Product', new mongoose.Schema({
    name: String,
    price: Number,
    description: String,
    image: String,
    stock: Number
}));

const Order = mongoose.model('Order', new mongoose.Schema({
    userId: String,
    products: [{ productId: String, quantity: Number }],
    total: Number,
    status: { type: String, default: 'pending' },
    createdAt: { type: Date, default: Date.now }
}));

// Routes
app.get('/api/products', async (req, res) => {
    const products = await Product.find();
    res.json(products);
});

app.post('/api/orders', async (req, res) => {
    const order = new Order(req.body);
    await order.save();
    res.status(201).json(order);
});

app.listen(3000, () => console.log('Backend running on port 3000'));
```

Frontend: src/App.js
```jsx
import { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ProductList from './components/ProductList';
import Cart from './components/Cart';
import Checkout from './components/Checkout';

function App() {
    const [cart, setCart] = useState([]);
    
    const addToCart = (product) => {
        setCart([...cart, product]);
    };
    
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<ProductList addToCart={addToCart} />} />
                <Route path="/cart" element={<Cart cart={cart} />} />
                <Route path="/checkout" element={<Checkout cart={cart} />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
```

CHECKLIST THÁNG 6:
- [ ] Kết nối được Frontend với Backend
- [ ] Implement được authentication flow
- [ ] Tạo được protected routes
- [ ] Build được E-commerce MVP hoàn chỉnh
- [ ] Có thể deploy được ứng dụng

---


# GIAI ĐOẠN 3: NÂNG CẤP FULL STACK (Tháng 7-12)


Mục tiêu:
- Từ mức Junior vững nền tảng → tiến gần Mid/Senior về Web.
- Nâng cấp UI/UX, testing, performance, DevOps cơ bản.
- Hoàn thiện 1–2 dự án Full Stack ở mức “production-ready” (đủ để cho vào CV).

---

## THÁNG 7-8: UI/UX, STATE MANAGEMENT, TESTING


1. UI/UX NÂNG CAO
---

Ý tưởng:
- Làm cho ứng dụng “cảm giác chuyên nghiệp”:
  - Loading state (spinner, skeleton).
  - Thông báo (toast) khi thành công/thất bại.
  - Form validation thân thiện (highlight field lỗi, message rõ ràng).

Ví dụ: sử dụng thư viện như `react-toastify`:
```jsx
import { toast } from 'react-toastify';

async function handleSubmit() {
    try {
        await api.createPost(form);
        toast.success('Tạo bài viết thành công!');
    } catch (error) {
        toast.error('Có lỗi xảy ra, vui lòng thử lại!');
    }
}
```

2. STATE MANAGEMENT (Context hoặc Redux Toolkit)
---

Không cần học tất cả, chỉ cần **một trong hai**:
- Nếu app nhỏ/vừa: Context API + custom hooks.
- Nếu app trung bình/lớn: Redux Toolkit.

Ví dụ với Redux Toolkit (store user, token và cart):
```javascript
// store.js
import { configureStore, createSlice } from '@reduxjs/toolkit';

const authSlice = createSlice({
    name: 'auth',
    initialState: { user: null, token: null },
    reducers: {
        loginSuccess(state, action) {
            state.user = action.payload.user;
            state.token = action.payload.token;
        },
        logout(state) {
            state.user = null;
            state.token = null;
        }
    }
});

export const { loginSuccess, logout } = authSlice.actions;

export const store = configureStore({
    reducer: {
        auth: authSlice.reducer
    }
});
```

3. TESTING CƠ BẢN
---

- Frontend:
  - Jest + React Testing Library.
  - Test component render, sự kiện click, submit.
- Backend:
  - Jest + supertest.
  - Test một vài endpoint quan trọng (login, tạo đơn hàng, tạo bài viết…).

Ví dụ test React component:
```jsx
import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

test('thêm todo mới', () => {
    render(<App />);
    const input = screen.getByPlaceholderText('Add a todo...');
    fireEvent.change(input, { target: { value: 'Learn Testing' } });
    fireEvent.keyPress(input, { key: 'Enter', code: 'Enter' });
    expect(screen.getByText('Learn Testing')).toBeInTheDocument();
});
```

CHECKLIST THÁNG 7-8:
- [ ] Có loading & error UI rõ ràng.
- [ ] Có toast/thông báo cho các hành động quan trọng.
- [ ] Dùng Context hoặc Redux Toolkit cho auth/state chính.
- [ ] Có tối thiểu 5–10 test FE + 5–10 test BE cho các luồng quan trọng.

---

## THÁNG 9-10: DEVOPS CƠ BẢN & TRIỂN KHAI THỰC TẾ


1. DOCKER CƠ BẢN
---

Mục tiêu:
- Đóng gói BE (và nếu cần FE) vào container.
- Chạy dev/test nhanh hơn, chuẩn bị tư duy production.

Ví dụ Dockerfile cho backend Node.js:
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --only=production
COPY . .
EXPOSE 3000
CMD [\"node\", \"server.js\"]
```

2. CI ĐƠN GIẢN VỚI GITHUB ACTIONS
---

Pipeline tối thiểu:
- Chạy `npm install`.
- Chạy `npm test`.

Ví dụ workflow:
```yaml
name: CI
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      - run: npm install
      - run: npm test
```

3. DEPLOY
---

- FE: Vercel/Netlify.
- BE: Render/Fly.io/Railway.
- DB: Mongo Atlas hoặc Postgres managed (Neon, Supabase).

Checklist deploy:
- `.env.example` mô tả các biến môi trường.
- Script `npm run start` rõ ràng.
- Health check endpoint `/health`.

CHECKLIST THÁNG 9-10:
- [ ] Backend chạy được trong Docker (local).
- [ ] Có workflow CI cơ bản chạy mỗi lần push/PR.
- [ ] FE + BE + DB đều deploy, chạy được online.
- [ ] README ghi rõ cách run local + deploy.

---

## THÁNG 11-12: DỰ ÁN FULL STACK #2 (HOÀN THIỆN HƠN)


Đề xuất: Task Manager / Booking / Job Board nhỏ.

YÊU CẦU:
- Auth đầy đủ (đăng ký, đăng nhập, reset password đơn giản qua link fake).
- Role-based authorization (`user`, `admin`).
- Filter & sort nâng cao.
- Search (theo tên, tag).
- Pagination chuẩn (page, limit, total, lastPage…).
- Gửi email (dùng SendGrid/Mailgun sandbox hoặc log ra console).

Ví dụ cấu trúc API filter/paginate:
```http
GET /api/tasks?status=done&priority=high&page=2&limit=20&sort=-createdAt
```

Response:
```json
{
  \"data\": [ /* danh sách tasks */ ],
  \"meta\": {
    \"page\": 2,
    \"limit\": 20,
    \"total\": 134,
    \"totalPages\": 7
  }
}
```

CHECKLIST GIAI ĐOẠN 3:
- [ ] 2 dự án Full Stack (Blog/E-commerce + 1 hệ thống khác) ở mức production-ready.
- [ ] FE/BE có test cơ bản, CI, deploy.
- [ ] UI/UX nhìn “đủ xài” cho người dùng thật.

---


# GIAI ĐOẠN 4: TỪ JUNIOR → SENIOR (NÂNG CAO) (Năm 2-3)


Mục tiêu:
- Không chỉ “biết làm” mà còn “biết thiết kế, tối ưu, bảo trì, dẫn dắt”.
- Hiểu System Design cơ bản–trung bình, nắm patterns chính.
- Có kinh nghiệm với performance, security, codebase lớn, review/mentoring.

---

4.1 SYSTEM DESIGN CƠ BẢN
---


Khái niệm phải nắm:
- Scalability: scale ngang/dọc, stateless, sticky session.
- Load Balancer: Nginx/ALB concept.
- Caching: Redis, CDN, cache invalidation cơ bản.
- Database: index, read-replica, partition/sharding (ở mức high-level).
- File storage: S3/GCS.

Bài tập design (dùng giấy/bảng vẽ, không cần code hết):
- Thiết kế hệ thống:
  - URL shortener (bit.ly).
  - News feed đơn giản (giống Facebook/Twitter bản nhẹ).
  - File upload service (giống Google Drive bản đơn giản).

Khi design, luôn trả lời:
- Traffic bao nhiêu?
- Đọc/ghi chủ yếu?
- Data có cần strong consistency không?
- Cache ở đâu? (frontend, backend, DB, CDN)
- Log/monitor thế nào?

---

4.2 THUẬT TOÁN & LEETCODE CHO SENIOR
---


Mục tiêu:
- 200+ bài Easy/Medium (không cần quá nhiều Hard).
- Nắm **pattern** chứ không phải thuộc lời giải.

Nhóm pattern quan trọng:
- Two Pointers, Sliding Window.
- Stack/Queue (monotonic stack).
- Binary Search nâng cao.
- BFS/DFS trên graph.
- Basic Dynamic Programming (1D, 2D).

Lịch gợi ý:
- Mỗi ngày: 2 bài Easy / 1 bài Medium.
- Mỗi tuần: review lại 5 bài đã làm, giải lại không nhìn giải.

---

4.3 CLEAN CODE, REVIEW, MENTORING
---


Để lên Senior, ngoài code, bạn cần:
- Viết code dễ đọc, dễ test, dễ refactor:
  - Tên biến/hàm rõ nghĩa.
  - Hàm ngắn, 1 trách nhiệm.
  - Tách layer (controller/service/repository).
- Code review:
  - Biết nhận feedback, biết cho feedback.
  - Comment tập trung vào correctness, readability, maintainability.
- Mentoring:
  - Hướng dẫn fresher/junior trong team.
  - Viết docs nội bộ, guideline coding.

CHECKLIST GIAI ĐOẠN 4:
- [ ] Design được 3–5 hệ thống cơ bản trên giấy/miro.
- [ ] 200+ bài LeetCode (nắm patterns).
- [ ] Biết phân tích performance & tối ưu chỗ bottleneck.
- [ ] Đã từng review code và hướng dẫn người khác (trong team hoặc open source).

---


# TỔNG KẾT: CÁCH DÙNG FILE NÀY TỪ FRESHER → SENIOR


1. Nếu bạn đang là **Fresher/Junior**:
   - Tập trung GIAI ĐOẠN 1 + 2 + 3.
   - Giai đoạn 4 đọc để định hướng, không cần “ăn hết” ngay.

2. Nếu bạn đang lên **Mid/Senior**:
   - Hoàn thiện dự án ở mức production.
   - Tập trung System Design, Performance, Security, Review/Mentoring.

3. Luôn nhớ:
   - **Thực hành > Lý thuyết**: code và ship sản phẩm thật.
   - **Patterns > Thuộc bài**: hiểu mẫu, không học vẹt.
   - **Đều đặn > Bùng nổ**: mỗi ngày một chút, không cần “đốt sức” rồi nghỉ.

Bạn có thể dùng `Roadmap_Fresher_Junior_RutGon.txt` như “bản timeline rút gọn”,  
và dùng file `Roadmap_Chi_Tiet_Co_Vi_Du.txt` này như “sách hướng dẫn + ví dụ code” để tra cứu khi triển khai từng giai đoạn.

---


# PHỤ LỤC: CÁCH HỌC, LỊCH MẪU, TÀI NGUYÊN


1) CÁCH DÙNG FILE NÀY (TÓM TẮT)
---

- Bạn là Fresher/Junior: đi tuần tự Giai đoạn 1 → 2 → 3. Giai đoạn 4 đọc để định hướng.
- Bạn đã có kinh nghiệm (Mid): có thể nhảy vào Giai đoạn 3 (UI/UX, testing, DevOps) và 4 (System Design, mentoring).
- Khi tới mốc nào, tìm đúng section trong file để lấy ví dụ code/bài tập.
- Khi bí: thử tối đa 30–45 phút, sau đó xem gợi ý/solution, đóng lại và tự code lại.

2) THÓI QUEN HẰNG NGÀY (MINIMAL)
---

- 30–60 phút: LeetCode (2 Easy hoặc 1 Medium), ghi chú pattern.
- 2–4 giờ: Code features cho dự án (frontend hoặc backend).
- 15 phút: Viết nhật ký ngắn (hôm nay làm gì, gặp lỗi gì, mai làm gì).
- 15 phút: Đọc lại/clean code, xem log CI/CD (nếu có).

3) LỊCH MẪU 1 TUẦN (CHO GIAI ĐOẠN 1–2)
---

- Thứ 2–6:
  - Sáng: 1–2 bài LeetCode.
  - Chiều: 2–3h code/feature nhỏ (Todo/Blog/E-commerce mini).
  - Tối: 30 phút đọc docs (React/Express/Mongo/PG).
- Thứ 7:
  - 4–6h hoàn thiện một tính năng lớn hoặc refactor + test.
  - Viết README, viết log thay đổi (changelog).
- Chủ nhật:
  - Nghỉ nhẹ, xem lại code, dọn repo, viết kế hoạch tuần tới.

4) TEMPLATE TIẾN ĐỘ DỰ ÁN (KANBAN RẤT GỌN)
---

- Backlog: liệt kê tính năng (auth, CRUD chính, upload, search, paginate, role…).
- In Progress: tối đa 2–3 task một lúc.
- Review/Test: tự test hoặc nhờ bạn review, viết 1–2 test nhanh (FE/BE).
- Done: merge vào main, tạo tag v1.0, update README, deploy.

5) LEETCODE PATTERNS & BỘ ĐỀ GỢI Ý
---

- Hash Map / Two Sum / Anagram:
  - Two Sum, Valid Anagram, Group Anagrams.
- Stack/Queue:
  - Valid Parentheses, Min Stack, Daily Temperatures (stack đơn điệu).
- Two Pointers / Sliding Window:
  - 3Sum, Container With Most Water, Longest Substring Without Repeating Characters, Longest Repeating Character Replacement.
- Binary Search:
  - Binary Search, Search in Rotated Sorted Array, Koko Eating Bananas.
- Prefix Sum / Interval:
  - Subarray Sum Equals K, Range Sum Query, Merge Intervals.
- Trees/Graphs (mức cơ bản–trung bình):
  - BFS/DFS traversal, Level Order, Number of Islands, Clone Graph.
- DP cơ bản:
  - Climbing Stairs, House Robber, Coin Change (chỉ cần 1–2 dạng để hiểu memo/tab).

6) TÀI NGUYÊN TIN CẬY (NGẮN GỌN)
---

- FE: React docs, React Router docs, Tailwind/Chakra docs.
- BE: Express docs, Mongoose/Sequelize docs, JWT, bcrypt.
- DB: MongoDB manual, PostgreSQL docs (CREATE TABLE, SELECT, JOIN, INDEX).
- DevOps: Docker docs (getting started), GitHub Actions starter templates.
- Luyện giải: LeetCode + NeetCode patterns (YouTube).
- UI/UX: Dribbble/Behance để tham khảo, không cần copy y nguyên; chú ý responsive, UX rõ ràng.

7) CHECKLIST KHI RELEASE MỘT PHIÊN BẢN
---

- Chạy test (ít nhất những test hiện có) và lint.
- Update `.env.example`.
- Update README (cách chạy, tài khoản demo, link deploy).
- Kiểm tra 5 flow quan trọng (đăng nhập, tạo/sửa/xóa dữ liệu chính, upload, thanh toán nếu có).
- Tạo tag phiên bản (v1.0.0, v1.1.0…).

8) FAQ NGẮN (THƯỜNG GẶP)
---

- Học gì trước? → Theo thứ tự timeline rút gọn. FE cơ bản → BE cơ bản → dự án full stack → nâng cấp UI/UX, testing, deploy → hệ thống thứ 2 → design cơ bản.
- Có phải học mọi thứ trong file? → Không. File là “sách tra cứu”. Ở giai đoạn Junior, chỉ cần làm xong Giai đoạn 1–3 và vài phần của 4; phần còn lại đọc định hướng.
- Làm bao nhiêu bài LeetCode? → 100–150 (Easy/Medium) là đủ cho Junior/Mid; Senior cần thêm kinh nghiệm design/codebase lớn và review/mentoring.
- Microservices có cần ngay không? → Không. Làm monolith ổn trước; khi nào app phức tạp mới tách.
- K8s/Terraform có cần không? → Không bắt buộc cho Junior/Mid web; biết Docker + CI + deploy là đủ.

---


# LỜI KẾT

Cuốn “sách” này nhằm mục tiêu thực dụng:
- Học để làm được, ship được, và có dự án tốt trong CV.
- Đi từ Fresher → Junior vững vàng → Mid/Senior bằng thực hành, không học vẹt.
- Mỗi ngày một chút, release đều đặn, ghi lại tiến trình và cải thiện.

Chúc bạn học nhanh, code sạch, ship đều và lên trình vững chắc!
