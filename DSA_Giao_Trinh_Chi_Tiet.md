# 🧠 GIÁO TRÌNH CẤU TRÚC DỮ LIỆU & GIẢI THUẬT (DSA)
## Từ Cơ Bản Đến Thành Thạo – Python Focused

> **Cập nhật:** 2026-03-17  
> **Mục tiêu:** Chinh phục phỏng vấn kỹ thuật & tư duy lập trình chuyên sâu  
> **Ngôn ngữ thực hành:** Python 3  

---

## 📋 MỤC LỤC

| # | Chủ đề | Level | Tuần |
|---|--------|-------|------|
| [1](#1-big-o-notation--tư-duy-tối-ưu) | Big O Notation & Tư duy tối ưu | 🟢 Cơ bản | Tuần 1 |
| [2](#2-đệ-quy-recursion) | Đệ quy (Recursion) | 🟢 Cơ bản | Tuần 1 |
| [3](#3-mảng-array--kỹ-thuật-cốt-lõi) | Mảng (Array) & Kỹ thuật cốt lõi | 🟢 Cơ bản | Tuần 2 |
| [4](#4-danh-sách-liên-kết-linked-list) | Danh sách liên kết (Linked List) | 🟡 Trung bình | Tuần 2 |
| [5](#5-ngăn-xếp-stack) | Ngăn xếp (Stack) | 🟡 Trung bình | Tuần 3 |
| [6](#6-hàng-đợi-queue) | Hàng đợi (Queue) | 🟡 Trung bình | Tuần 3 |
| [7](#7-bảng-băm-hash-table) | Bảng băm (Hash Table) | 🟡 Trung bình | Tuần 4 |
| [8](#8-cây-nhị-phân--bst) | Cây nhị phân & BST | 🔴 Nâng cao | Tuần 5 |
| [9](#9-heap--priority-queue) | Heap & Priority Queue | 🔴 Nâng cao | Tuần 5 |
| [10](#10-đồ-thị-graph) | Đồ thị (Graph) | 🔴 Nâng cao | Tuần 6 |
| [11](#11-trie) | Trie (Cây tiền tố) | 🔴 Nâng cao | Tuần 6 |
| [12](#12-sắp-xếp-sorting-algorithms) | Các thuật toán sắp xếp | 🟡 Trung bình | Tuần 3 |
| [13](#13-tìm-kiếm-nhị-phân-binary-search) | Tìm kiếm nhị phân | 🟡 Trung bình | Tuần 3 |
| [14](#14-pattern-sliding-window) | Pattern: Sliding Window | 🔴 Nâng cao | Tuần 7 |
| [15](#15-pattern-two-pointers) | Pattern: Two Pointers | 🔴 Nâng cao | Tuần 7 |
| [16](#16-quy-hoạch-động-dynamic-programming) | Quy hoạch động (DP) | 🔴 Nâng cao | Tuần 8 |
| [17](#17-greedy-algorithms) | Greedy Algorithms | 🔴 Nâng cao | Tuần 8 |

---

## 1. Big O Notation & Tư Duy Tối Ưu

### 📚 Khái niệm
Big O là cách đánh giá **hiệu năng** (thời gian và bộ nhớ) của thuật toán khi dữ liệu đầu vào tăng lên.

| Ký hiệu | Tên | Ví dụ thực tế |
|---------|-----|---------------|
| O(1) | Constant | Truy cập phần tử mảng qua index |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Duyệt toàn bộ mảng |
| O(n log n) | Linearithmic | Merge Sort, Quick Sort |
| O(n²) | Quadratic | Bubble Sort, vòng lặp lồng nhau |
| O(2ⁿ) | Exponential | Fibonacci đệ quy không tối ưu |
| O(n!) | Factorial | Sinh tất cả hoán vị |

### 💡 Quy tắc phân tích nhanh
1. **Bỏ hằng số:** `O(2n)` → `O(n)`
2. **Bỏ số hạng nhỏ hơn:** `O(n² + n)` → `O(n²)`
3. **Hai vòng lặp nối tiếp:** `O(n + m)`
4. **Hai vòng lặp lồng nhau:** `O(n * m)`

### 🔍 Ví dụ so sánh thực tế

```python
import time

# ❌ O(n²) - Tìm cặp có tổng = target (cách ngây thơ)
def two_sum_naive(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# ✅ O(n) - Tìm cặp có tổng = target (dùng Hash Map)
def two_sum_optimal(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Demo hiệu năng
import random
nums = [random.randint(1, 1000) for _ in range(10000)]
target = 999

start = time.time()
two_sum_naive(nums, target)
print(f"O(n²): {time.time() - start:.4f}s")

start = time.time()
two_sum_optimal(nums, target)
print(f"O(n):  {time.time() - start:.6f}s")
# Kết quả: O(n²) chậm hơn O(n) hàng trăm lần!
```

### 📝 Space Complexity (Độ phức tạp không gian)
```python
# O(1) space - không dùng thêm bộ nhớ
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# O(n) space - dùng thêm mảng mới
def reverse_new_array(arr):
    return arr[::-1]
```

### 🎯 Bài tập
1. LeetCode **#1** – Two Sum → O(n) bằng HashMap
2. LeetCode **#217** – Contains Duplicate → O(n) bằng Set
3. LeetCode **#121** – Best Time to Buy and Sell Stock → O(n) một lượt duyệt

---

## 2. Đệ Quy (Recursion)

### 📚 Khái niệm
Hàm gọi chính nó để giải quyết bài toán con nhỏ hơn.

**3 thành phần bắt buộc:**
1. **Base case:** Điều kiện dừng (tránh infinite loop).
2. **Recursive case:** Gọi đệ quy với bài toán nhỏ hơn.
3. **Trust the recursion:** Tin rằng lời gọi đệ quy sẽ trả về đúng.

### 🔍 Ví dụ kinh điển

```python
# Giai thừa: n! = n × (n-1)!
def factorial(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive case: tin rằng factorial(n-1) đúng
    return n * factorial(n - 1)

# Fibonacci với Memoization (Top-Down DP)
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Fibonacci KHÔNG memoization: O(2ⁿ) → RẤT CHẬM
# Fibonacci CÓ memoization: O(n) → NHANH
```

### 🌳 Đệ quy và Call Stack

```
factorial(4)
├── 4 × factorial(3)
│   ├── 3 × factorial(2)
│   │   ├── 2 × factorial(1)
│   │   │   └── return 1        ← Base case
│   │   └── return 2 × 1 = 2
│   └── return 3 × 2 = 6
└── return 4 × 6 = 24
```

> ⚠️ **Lỗi thường gặp:** Quên Base case → Stack Overflow (đệ quy vô hạn)!

### 🎯 Bài tập
1. LeetCode **#206** – Reverse Linked List (đệ quy)
2. LeetCode **#104** – Maximum Depth of Binary Tree
3. LeetCode **#21** – Merge Two Sorted Lists (đệ quy)

---

## 3. Mảng (Array) & Kỹ Thuật Cốt Lõi

### 📚 Khái niệm
Dữ liệu lưu **liên tiếp trong bộ nhớ**, truy cập `O(1)` qua index.

```
Index:  [0]  [1]  [2]  [3]  [4]
Value:  [10] [20] [30] [40] [50]
Memory: 100  104  108  112  116   ← Địa chỉ liên tiếp
```

| Thao tác | Độ phức tạp | Ghi chú |
|----------|-------------|---------|
| Access | O(1) | Tính địa chỉ trực tiếp |
| Search | O(n) | Phải duyệt từng phần tử |
| Insert (end) | O(1) amortized | Dynamic Array |
| Insert (middle) | O(n) | Phải dịch phần tử |
| Delete | O(n) | Phải dịch phần tử |

### 🔧 Kỹ thuật Prefix Sum

```python
# Tính tổng bất kỳ đoạn [l, r] trong O(1)
class PrefixSum:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def range_sum(self, left, right):
        # Tổng từ index left đến right (inclusive)
        return self.prefix[right + 1] - self.prefix[left]

# Sử dụng
nums = [1, 2, 3, 4, 5]
ps = PrefixSum(nums)
print(ps.range_sum(1, 3))  # 2+3+4 = 9
print(ps.range_sum(0, 4))  # 1+2+3+4+5 = 15
```

### 🔧 Kỹ thuật Kadane's Algorithm (Maximum Subarray)

```python
def max_subarray(nums):
    """
    LeetCode #53 - Maximum Subarray
    Time: O(n), Space: O(1)
    """
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        # Tại mỗi vị trí: tiếp tục dãy cũ HOẶC bắt đầu dãy mới
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Ví dụ: [-2, 1, -3, 4, -1, 2, 1, -5, 4]  → 6 ([4,-1,2,1])
```

### 🎯 Bài tập
1. LeetCode **#53** – Maximum Subarray (Kadane)
2. LeetCode **#238** – Product of Array Except Self (Prefix/Suffix)
3. LeetCode **#11** – Container With Most Water (Two Pointers)
4. LeetCode **#15** – 3Sum (Sorting + Two Pointers)

---

## 4. Danh Sách Liên Kết (Linked List)

### 📚 Khái niệm
Dữ liệu lưu **rải rác trong bộ nhớ**, mỗi node chứa giá trị và con trỏ sang node tiếp theo.

```
[10|next] → [20|next] → [30|next] → [40|NULL]
  head
```

| Thao tác | Độ phức tạp | So sánh với Array |
|----------|-------------|-------------------|
| Access | O(n) | Array: O(1) ❌ |
| Search | O(n) | Array: O(n) = |
| Insert (head) | O(1) | Array: O(n) ✅ |
| Insert (middle) | O(n) | Array: O(n) = |
| Delete (head) | O(1) | Array: O(n) ✅ |

### 🔧 Implement từ đầu

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        """Thêm vào cuối: O(n)"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, val):
        """Thêm vào đầu: O(1)"""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def delete(self, val):
        """Xóa node với val đó: O(n)"""
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return
            curr = curr.next

    def reverse(self):
        """Đảo ngược Linked List: O(n), O(1) space"""
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next   # Lưu tạm node tiếp theo
            curr.next = prev        # Đảo chiều con trỏ
            prev = curr             # Tiến prev
            curr = next_node        # Tiến curr
        self.head = prev

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        return " → ".join(nodes) + " → NULL"
```

### 🔧 Kỹ thuật Fast & Slow Pointers

```python
def find_middle(head):
    """Tìm phần tử giữa – O(n), O(1) space"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # Đi 1 bước
        fast = fast.next.next    # Đi 2 bước
    return slow  # Khi fast đến cuối, slow ở giữa

def has_cycle(head):
    """Detect Cycle (Floyd's Algorithm) – O(n), O(1) space"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:      # Gặp nhau → có chu trình
            return True
    return False
```

### 🎯 Bài tập
1. LeetCode **#206** – Reverse Linked List
2. LeetCode **#141** – Linked List Cycle
3. LeetCode **#876** – Middle of the Linked List
4. LeetCode **#21** – Merge Two Sorted Lists
5. LeetCode **#19** – Remove Nth Node From End of List

---

## 5. Ngăn Xếp (Stack)

### 📚 Khái niệm
**LIFO** (Last In, First Out) – Vào sau ra trước. Giống như chồng sách.

```
Thêm:  PUSH →  [TOP: 30]   POP → Lấy 30
                     [20]
                     [10]
```

### 🔧 Implement và ứng dụng

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):     # O(1)
        self.items.append(item)

    def pop(self):            # O(1)
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):           # O(1)
        return self.items[-1] if self.items else None

    def is_empty(self):       # O(1)
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### 🔧 Ứng dụng: Monotonic Stack

```python
def next_greater_element(nums):
    """
    Với mỗi phần tử, tìm phần tử lớn hơn gần nhất bên phải.
    Time: O(n) – mỗi phần tử chỉ push/pop 1 lần
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # Lưu index

    for i in range(n):
        # Trong khi stack không rỗng và phần tử hiện tại lớn hơn phần tử stack top
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]  # nums[i] là "next greater" của result[idx]
        stack.append(i)

    return result

# [2, 1, 2, 4, 3] → [4, 2, 4, -1, -1]
```

### 🎯 Bài tập
1. LeetCode **#20** – Valid Parentheses
2. LeetCode **#155** – Min Stack
3. LeetCode **#739** – Daily Temperatures (Monotonic Stack)
4. LeetCode **#84** – Largest Rectangle in Histogram

---

## 6. Hàng Đợi (Queue)

### 📚 Khái niệm
**FIFO** (First In, First Out) – Vào trước ra trước. Giống như hàng đợi người mua vé.

```
Enqueue →  [10] [20] [30]  → Dequeue
                 FRONT          BACK
```

### 🔧 Implement và ứng dụng

```python
from collections import deque

class Queue:
    """Dùng deque để đạt O(1) cho cả enqueue và dequeue"""
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):   # O(1)
        self.items.append(item)

    def dequeue(self):         # O(1) với deque, O(n) nếu dùng list!
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def front(self):
        return self.items[0] if self.items else None

    def is_empty(self):
        return len(self.items) == 0


# Priority Queue (Heap-based)
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, priority, item):
        heapq.heappush(self.heap, (priority, item))  # O(log n)

    def pop(self):
        return heapq.heappop(self.heap)   # O(log n)

    def peek(self):
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0
```

### 🔧 Queue và BFS (Breadth First Search)

```python
from collections import deque

def bfs(graph, start):
    """
    Duyệt đồ thị theo chiều rộng.
    BFS luôn tìm đường đi ngắn nhất (số cạnh nhỏ nhất).
    """
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Đồ thị ví dụ
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
bfs(graph, 'A')  # A B C D E F
```

### 🎯 Bài tập
1. LeetCode **#232** – Implement Queue using Stacks
2. LeetCode **#102** – Binary Tree Level Order Traversal (BFS)
3. LeetCode **#200** – Number of Islands (BFS)
4. LeetCode **#994** – Rotting Oranges (Multi-source BFS)

---

## 7. Bảng Băm (Hash Table)

### 📚 Khái niệm
Ánh xạ **key → value** với thao tác trung bình O(1).

```
Hash Function:   "apple" → hash() → 3
                              ↓
Table:  [0][ ][...]  [3]["apple" → 5]  [...]
                     ↑
                     Bucket
```

### 🔧 Ứng dụng thực tế

```python
# 1. Đếm tần suất
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Tương đương với:
from collections import Counter
freq = Counter("abracadabra")
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# 2. Kiểm tra anagram – O(n)
def is_anagram(s, t):
    return Counter(s) == Counter(t)

# 3. Group Anagrams – O(n * k) với k là độ dài chuỗi trung bình
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = tuple(sorted(s))  # Sắp xếp chữ cái làm key
        groups.setdefault(key, []).append(s)
    return list(groups.values())

# ["eat","tea","tan","ate","nat","bat"]
# → [["eat","tea","ate"],["tan","nat"],["bat"]]
```

### 🎯 Bài tập
1. LeetCode **#1** – Two Sum
2. LeetCode **#242** – Valid Anagram
3. LeetCode **#49** – Group Anagrams
4. LeetCode **#128** – Longest Consecutive Sequence

---

## 8. Cây Nhị Phân & BST

### 📚 Khái niệm

```
       8
      / \
     3   10
    / \    \
   1   6    14
      / \   /
     4   7 13
```

**BST Property:** Node trái < Node hiện tại < Node phải

### 🔧 Implement & Duyệt cây

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ── 3 kiểu duyệt DFS ──────────────────────────────────────
def inorder(root):
    """Trái → Root → Phải | BST → sắp xếp tăng dần"""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    """Root → Trái → Phải | Dùng sao chép/serialize cây"""
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    """Trái → Phải → Root | Dùng xóa cây, tính kích thước"""
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# ── BFS (Level Order) ──────────────────────────────────────
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level_nodes)
    return result

# ── BST Search ─────────────────────────────────────────────
def search_bst(root, val):
    """Tìm kiếm trong BST: O(h), h = chiều cao cây"""
    if not root or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)
```

### 🎯 Bài tập
1. LeetCode **#104** – Maximum Depth of Binary Tree
2. LeetCode **#226** – Invert Binary Tree
3. LeetCode **#102** – Binary Tree Level Order Traversal
4. LeetCode **#235** – Lowest Common Ancestor of BST
5. LeetCode **#98** – Validate Binary Search Tree

---

## 9. Heap & Priority Queue

### 📚 Khái niệm
**Min Heap:** Phần tử nhỏ nhất luôn ở gốc.  
**Max Heap:** Phần tử lớn nhất luôn ở gốc.

```
Min Heap:        Max Heap:
      1                10
    /   \            /    \
   3     5          9      8
  / \   /          / \    /
 7   4  6         7   6  3
```

### 🔧 Sử dụng heapq trong Python

```python
import heapq

# Python chỉ có Min Heap
min_heap = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(min_heap)      # O(n)

heapq.heappush(min_heap, 0)  # O(log n)
smallest = heapq.heappop(min_heap)  # O(log n) → trả về 0

# Max Heap: dùng giá trị âm
max_heap = [-3, -1, -4, -1, -5]
heapq.heapify(max_heap)
largest = -heapq.heappop(max_heap)  # Lấy giá trị lớn nhất


# ── Tìm K phần tử lớn nhất ────────────────────────────────
def k_largest(nums, k):
    """O(n log k) – hiệu quả hơn sort O(n log n)"""
    return heapq.nlargest(k, nums)

# ── Top K Frequent Elements ────────────────────────────────
def top_k_frequent(nums, k):
    count = Counter(nums)
    # nlargest(k, iterable, key=...)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

### 🎯 Bài tập
1. LeetCode **#703** – Kth Largest Element in a Stream
2. LeetCode **#347** – Top K Frequent Elements
3. LeetCode **#295** – Find Median from Data Stream
4. LeetCode **#23** – Merge K Sorted Lists

---

## 10. Đồ Thị (Graph)

### 📚 Khái niệm
Tập các **đỉnh (vertices)** và **cạnh (edges)** nối chúng.

| Loại | Mô tả |
|------|-------|
| **Directed** | Cạnh có hướng (A → B, nhưng không phải B → A) |
| **Undirected** | Cạnh không hướng (A — B) |
| **Weighted** | Cạnh có trọng số (A --(5)--> B) |
| **Cyclic** | Có chu trình |
| **Acyclic (DAG)** | Không có chu trình (dùng trong Topological Sort) |

### 🔧 Biểu diễn đồ thị

```python
# Adjacency List (Danh sách kề) – phổ biến nhất
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# ── DFS (Depth First Search) ────────────────────────────────
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# ── BFS (Breadth First Search) ──────────────────────────────
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### 🔧 Thuật toán Dijkstra (Đường đi ngắn nhất)

```python
import heapq

def dijkstra(graph, start):
    """
    graph: {node: [(cost, neighbor), ...]}
    Trả về {node: shortest_distance}
    Time: O((V + E) log V)
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > distances[curr_node]:
            continue  # Đã tìm được đường ngắn hơn rồi

        for cost, neighbor in graph[curr_node]:
            distance = curr_dist + cost
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Ví dụ
graph = {
    'A': [(1, 'B'), (4, 'C')],
    'B': [(2, 'C'), (5, 'D')],
    'C': [(1, 'D')],
    'D': []
}
print(dijkstra(graph, 'A'))
# {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

### 🎯 Bài tập
1. LeetCode **#200** – Number of Islands (DFS/BFS)
2. LeetCode **#133** – Clone Graph
3. LeetCode **#207** – Course Schedule (Cycle Detection)
4. LeetCode **#743** – Network Delay Time (Dijkstra)
5. LeetCode **#127** – Word Ladder (BFS)

---

## 11. Trie

### 📚 Khái niệm
Cây đặc biệt lưu **chuỗi ký tự**, tối ưu cho tìm kiếm prefix.

```
Trie chứa: ["app", "apple", "apt", "bat"]

        root
       /    \
      a      b
      |      |
      p      a
     / \     |
    p   t    t
    |
    l
    |
    e
```

### 🔧 Implement Trie

```python
class TrieNode:
    def __init__(self):
        self.children = {}      # char → TrieNode
        self.is_end_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """O(m) – m là độ dài word"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True

    def search(self, word):
        """O(m)"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word

    def starts_with(self, prefix):
        """O(m) – Kiểm tra prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Sử dụng
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))    # True
print(trie.search("app"))      # False
print(trie.starts_with("app")) # True
```

### 🎯 Bài tập
1. LeetCode **#208** – Implement Trie (Prefix Tree)
2. LeetCode **#212** – Word Search II
3. LeetCode **#211** – Design Add and Search Words

---

## 12. Sắp Xếp (Sorting Algorithms)

### 📊 So sánh tổng quan

| Thuật toán | Time (Avg) | Time (Worst) | Space | Stable? |
|-----------|-----------|-------------|-------|---------|
| Bubble Sort | O(n²) | O(n²) | O(1) | ✅ |
| Insertion Sort | O(n²) | O(n²) | O(1) | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick Sort | O(n log n) | O(n²) | O(log n) | ❌ |
| Heap Sort | O(n log n) | O(n log n) | O(1) | ❌ |
| Python `sorted()` | O(n log n) | O(n log n) | O(n) | ✅ (Timsort) |

### 🔧 Merge Sort & Quick Sort

```python
def merge_sort(arr):
    """Stable, O(n log n) guaranteed. Tốt cho Linked List"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge hai nửa đã sắp xếp
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr, low=0, high=None):
    """In-place, O(n log n) average. Tốt cho Array"""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    return arr

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

---

## 13. Tìm Kiếm Nhị Phân (Binary Search)

### 📚 Khái niệm
Tìm kiếm trong mảng **đã sắp xếp** bằng cách chia đôi không gian tìm kiếm. O(log n).

### 🔧 Template chuẩn (3 biến thể)

```python
# ── Biến thể 1: Tìm chính xác ─────────────────────────────
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Tránh overflow
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ── Biến thể 2: Tìm vị trí đầu tiên >= target ─────────────
def lower_bound(nums, target):
    """Leftmost position"""
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


# ── Biến thể 3: BS trên khoảng giá trị ──────────────────
def min_days_to_bloom(bloomDay, m, k):
    """
    LeetCode #1482 – Minimum Number of Days to Make m Bouquets
    Không tìm trong mảng, mà tìm giá trị đáp án tối ưu!
    """
    def can_make(day):
        bouquets = flowers = 0
        for d in bloomDay:
            if d <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m

    left, right = min(bloomDay), max(bloomDay)
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if can_make(mid):
            result = mid
            right = mid - 1  # Tìm ngày nhỏ hơn khả thi
        else:
            left = mid + 1

    return result
```

### 🎯 Bài tập
1. LeetCode **#704** – Binary Search
2. LeetCode **#153** – Find Minimum in Rotated Sorted Array
3. LeetCode **#33** – Search in Rotated Sorted Array
4. LeetCode **#875** – Koko Eating Bananas (BS on value)
5. LeetCode **#410** – Split Array Largest Sum (BS on value)

---

## 14. Pattern: Sliding Window

### 📚 Khi nào dùng?
- Bài toán liên quan đến **dãy con liên tiếp** (subarray/substring).
- Tìm length, sum, hoặc property của một window.
- Có thể tối ưu từ O(n²) brute force → O(n).

### 🔧 Template chuẩn

```python
# ── Fixed Size Window ──────────────────────────────────────
def max_sum_subarray_k(nums, k):
    """Tổng lớn nhất của dãy con có k phần tử: O(n)"""
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # Thêm mới, bỏ cũ
        max_sum = max(max_sum, window_sum)

    return max_sum


# ── Variable Size Window ────────────────────────────────────
def longest_substring_k_distinct(s, k):
    """
    Chuỗi con dài nhất với tối đa k ký tự phân biệt.
    LeetCode #340
    Time: O(n)
    """
    from collections import defaultdict
    char_count = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        char_count[s[right]] += 1            # Mở rộng window

        while len(char_count) > k:           # Thu hẹp khi vi phạm
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)  # Cập nhật đáp án

    return max_len
```

### 🎯 Bài tập
1. LeetCode **#3** – Longest Substring Without Repeating Characters
2. LeetCode **#76** – Minimum Window Substring ⭐
3. LeetCode **#424** – Longest Repeating Character Replacement
4. LeetCode **#567** – Permutation in String

---

## 15. Pattern: Two Pointers

### 📚 Khi nào dùng?
- Mảng/chuỗi **đã sắp xếp**.
- Tìm cặp/bộ phần tử thỏa điều kiện.
- So sánh hai mảng.

### 🔧 Ví dụ kinh điển

```python
# ── 3Sum – O(n²) giảm từ O(n³) brute force ─────────────────
def three_sum(nums):
    """LeetCode #15"""
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Bỏ qua duplicate

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1; right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# ── Trapping Rain Water – O(n), O(1) space ─────────────────
def trap(height):
    """LeetCode #42 – Kinh điển nhất về Two Pointers"""
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water
```

### 🎯 Bài tập
1. LeetCode **#167** – Two Sum II (Sorted Array)
2. LeetCode **#15** – 3Sum
3. LeetCode **#42** – Trapping Rain Water ⭐
4. LeetCode **#11** – Container With Most Water

---

## 16. Quy Hoạch Động (Dynamic Programming)

### 📚 Khái niệm
DP giải bài toán bằng cách chia thành **bài toán con chồng lấp** và **lưu kết quả** (memoization/tabulation).

**Dấu hiệu nhận biết DP:**
- "Tối đa / tối thiểu / đếm số cách..."
- Bài toán có bài toán con trùng lặp

### 🔧 Framework giải DP

```python
# ── 1. Top-Down (Memoization + Recursion) ─────────────────
def climb_stairs_memo(n, memo={}):
    """LeetCode #70 – Climbing Stairs"""
    if n in memo: return memo[n]
    if n <= 2: return n
    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]


# ── 2. Bottom-Up (Tabulation) ─────────────────────────────
def climb_stairs_dp(n):
    """O(n) time, O(n) space"""
    if n <= 2: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# ── 3. Space Optimized ─────────────────────────────────────
def climb_stairs_optimal(n):
    """O(n) time, O(1) space"""
    if n <= 2: return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1


# ── Longest Common Subsequence – O(m*n) ────────────────────
def longest_common_subsequence(text1, text2):
    """LeetCode #1143 – Template cho nhiều bài DP 2D"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
```

### 🎯 Bài tập
1. LeetCode **#70** – Climbing Stairs
2. LeetCode **#198** – House Robber
3. LeetCode **#300** – Longest Increasing Subsequence
4. LeetCode **#1143** – Longest Common Subsequence ⭐
5. LeetCode **#322** – Coin Change ⭐

---

## 17. Greedy Algorithms

### 📚 Khái niệm
Ở mỗi bước, chọn lựa **tối ưu cục bộ** với hy vọng đạt được **tối ưu toàn cục**.

**Khác DP:** Greedy không cần xem xét lại quyết định cũ.

### 🔧 Ví dụ

```python
def can_jump(nums):
    """
    LeetCode #55 – Jump Game
    Tham lam: Luôn theo dõi vị trí xa nhất có thể nhảy đến.
    """
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False  # Không thể đến đây
        max_reach = max(max_reach, i + jump)
    return True


def merge_intervals(intervals):
    """
    LeetCode #56 – Merge Intervals
    Sắp xếp theo start, tham lam merge các interval chồng lấp.
    """
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:          # Chồng lấp
            merged[-1][1] = max(merged[-1][1], end)  # Mở rộng
        else:
            merged.append([start, end])

    return merged
```

### 🎯 Bài tập
1. LeetCode **#55** – Jump Game
2. LeetCode **#45** – Jump Game II
3. LeetCode **#56** – Merge Intervals ⭐
4. LeetCode **#435** – Non-overlapping Intervals

---

## 🗺️ LỘ TRÌNH THỰC HÀNH TỔNG HỢP

### Checklist 8 tuần
```
Tuần 1: Big O + Recursion
  ☐ Phân tích Big O của 5 đoạn code bất kỳ mỗi ngày
  ☐ LeetCode Easy: #1, #217, #121, #70, #21

Tuần 2: Array + Linked List
  ☐ Implement Array, LinkedList thủ công (không dùng built-in)
  ☐ LeetCode Easy: #206, #141, #876, #21, #238
  ☐ LeetCode Medium: #19, #148, #11

Tuần 3: Stack + Queue + Sorting + Binary Search
  ☐ Implement Stack (Monotonic), Queue (deque)
  ☐ Implement Merge Sort, Quick Sort
  ☐ LeetCode Easy: #20, #155, #704
  ☐ LeetCode Medium: #739, #153, #875

Tuần 4: Hash Table
  ☐ LeetCode Easy: #1, #242, #217
  ☐ LeetCode Medium: #49, #128, #347

Tuần 5: Trees + Heap
  ☐ Implement BST: insert, search, inorder
  ☐ Thực hành BFS (level order) và DFS (pre/in/post)
  ☐ LeetCode Medium: #102, #235, #98, #347, #295

Tuần 6: Graph + Trie
  ☐ Implement DFS, BFS, Dijkstra
  ☐ Implement Trie
  ☐ LeetCode Medium: #200, #207, #743, #208

Tuần 7: Sliding Window + Two Pointers
  ☐ Áp dụng template cho các bài toán subarray/substring
  ☐ LeetCode Medium: #3, #76, #424, #15, #42

Tuần 8: Dynamic Programming + Greedy
  ☐ Phân biệt rõ khi nào dùng DP, khi nào dùng Greedy
  ☐ LeetCode Medium: #198, #300, #1143, #322, #56, #55
```

### Mục tiêu LeetCode
| Giai đoạn | Số bài | Trọng tâm |
|-----------|--------|-----------|
| Sau 8 tuần | 80+ Easy | Hiểu patterns cơ bản |
| Sau 16 tuần | 100+ Medium | Tư duy tối ưu |
| Sẵn sàng phỏng vấn | 20+ Hard | Áp lực thực chiến |

---

*📌 Ghi chú: Mỗi bài LeetCode nên làm theo trình tự: **Brute Force → Optimal Solution → Phân tích Big O → Code sạch thủ công***

---

## 18. Backtracking (Quay Lui)

### 📚 Khái niệm
Backtracking là kỹ thuật **thử từng lựa chọn, nếu không hợp lệ thì quay lui** và thử lựa chọn khác. Đây là nền tảng của nhiều bài toán tối ưu hóa và tổ hợp.

```
                    []
          /          |          \
        [1]         [2]         [3]
       /   \       /   \       /   \
     [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
      |      |     |      |     |      |
  [1,2,3] [1,3,2] ...           ...  [3,2,1]
```

**Template chuẩn:**
```python
def backtrack(state, choices):
    # 1. Base case: nếu đã đủ điều kiện → lưu kết quả
    if is_complete(state):
        result.append(state[:])  # Copy tránh reference
        return

    for choice in choices:
        # 2. Kiểm tra ràng buộc (pruning - cắt tỉa)
        if is_valid(state, choice):
            # 3. Thực hiện lựa chọn
            state.append(choice)
            # 4. Đệ quy với state mới
            backtrack(state, remaining_choices)
            # 5. Hoàn tác lựa chọn (QUAN TRỌNG!)
            state.pop()
```

### 🔧 Ví dụ kinh điển

```python
# ── Permutations (Hoán vị) – O(n * n!) ───────────────────
def permute(nums):
    """LeetCode #46 – Tất cả hoán vị của nums"""
    result = []

    def backtrack(current, remaining):
        if not remaining:          # Base case: hết phần tử
            result.append(current[:])
            return
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()         # Hoàn tác

    backtrack([], nums)
    return result

# permute([1,2,3]) → [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# ── Subsets (Tập con) – O(2ⁿ) ────────────────────────────
def subsets(nums):
    """LeetCode #78 – Tất cả tập con"""
    result = []

    def backtrack(start, current):
        result.append(current[:])   # Mọi trạng thái đều là tập con hợp lệ
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


# ── N-Queens – O(n!) ─────────────────────────────────────
def solve_n_queens(n):
    """LeetCode #51 – Bài toán N quân Hậu (Classic Hard)"""
    result = []
    cols = set()           # Cột đã có quân hậu
    pos_diag = set()       # Đường chéo thuận (row + col)
    neg_diag = set()       # Đường chéo nghịch (row - col)

    board = [['.' for _ in range(n)] for _ in range(n)]

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return

        for col in range(n):
            # Kiểm tra ràng buộc: cùng cột, cùng đường chéo
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            # Thực hiện lựa chọn
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            board[row][col] = 'Q'

            backtrack(row + 1)

            # Hoàn tác
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
            board[row][col] = '.'

    backtrack(0)
    return result


# ── Word Search – O(4^(m*n)) ──────────────────────────────
def exist(board, word):
    """LeetCode #79 – Tìm từ trong ma trận ký tự"""
    rows, cols = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[idx]:
            return False

        # Đánh dấu đã thăm (tránh dùng lại)
        temp = board[r][c]
        board[r][c] = '#'

        # Thử 4 hướng
        found = (dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or
                 dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1))

        # Khôi phục
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```

### 💡 Kỹ thuật Pruning (Cắt tỉa)
```python
# ── Combination Sum với Pruning – O(2^(t/c)) ─────────────
def combination_sum(candidates, target):
    """LeetCode #39 – Tìm tổ hợp có tổng = target"""
    candidates.sort()   # Sắp xếp để pruning hiệu quả
    result = []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return

        for i in range(start, len(candidates)):
            # ✅ PRUNING: nếu candidates[i] > remaining → bỏ qua tất cả phía sau
            if candidates[i] > remaining:
                break

            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # i (không phải i+1) vì có thể dùng lại
            current.pop()

    backtrack(0, [], target)
    return result
```

### 🎯 Bài tập
1. LeetCode **#46** – Permutations ⭐
2. LeetCode **#78** – Subsets ⭐
3. LeetCode **#39** – Combination Sum
4. LeetCode **#79** – Word Search
5. LeetCode **#51** – N-Queens (Hard) ⭐⭐

---

## 19. Union-Find (Disjoint Set Union)

### 📚 Khái niệm
Cấu trúc dữ liệu quản lý các **tập hợp rời nhau** (disjoint sets). Hỗ trợ 2 thao tác cực nhanh:
- `find(x)`: Tìm "đại diện" (root) của tập chứa x → O(α(n)) ≈ O(1)
- `union(x, y)`: Gộp tập chứa x và tập chứa y → O(α(n)) ≈ O(1)

**Ứng dụng:** Tìm connected components, cycle detection, Kruskal's MST.

```
Ban đầu: {1} {2} {3} {4} {5}

union(1,2): {1,2} {3} {4} {5}
union(3,4): {1,2} {3,4} {5}
union(1,3): {1,2,3,4} {5}

find(2) → 1 (root của {1,2,3,4})
find(4) → 1 (cùng root → cùng tập!)
```

### 🔧 Implement với Path Compression + Union by Rank

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))   # parent[i] = i ban đầu
        self.rank = [0] * n            # Dùng để cân bằng cây
        self.components = n            # Số thành phần liên thông

    def find(self, x):
        """Path Compression: làm cây phẳng hơn"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Đệ quy + flatten
        return self.parent[x]

    def union(self, x, y):
        """Union by Rank: cây thấp hơn gắn vào cây cao hơn"""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Đã cùng tập → có cycle!

        # Gắn cây nhỏ vào cây lớn
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.components -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# ── Ứng dụng: Number of Connected Components ─────────────
def count_components(n, edges):
    """LeetCode #323"""
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.components


# ── Ứng dụng: Redundant Connection (Cycle Detection) ─────
def find_redundant_connection(edges):
    """LeetCode #684 – Tìm cạnh thừa tạo ra chu trình"""
    uf = UnionFind(len(edges) + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]   # Cạnh này tạo cycle
    return []


# ── Kruskal's Minimum Spanning Tree ──────────────────────
def kruskal_mst(n, edges):
    """
    Tìm cây khung nhỏ nhất.
    edges: [(weight, u, v), ...]
    """
    edges.sort()  # Sắp xếp theo trọng số tăng dần
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []

    for weight, u, v in edges:
        if uf.union(u, v):  # Nếu không tạo cycle
            mst_weight += weight
            mst_edges.append((u, v))
            if len(mst_edges) == n - 1:  # MST có đúng n-1 cạnh
                break

    return mst_weight, mst_edges
```

### 🎯 Bài tập
1. LeetCode **#547** – Number of Provinces
2. LeetCode **#684** – Redundant Connection
3. LeetCode **#200** – Number of Islands (có thể dùng Union-Find)
4. LeetCode **#1091** – Shortest Path in Binary Matrix

---

## 20. Segment Tree (Cây Phân Đoạn)

### 📚 Khái niệm
Segment Tree cho phép thực hiện **range queries** (tổng, min, max trên đoạn [l,r]) và **point updates** trong O(log n).

```
Mảng:  [1, 3, 5, 7, 9, 11]

Segment Tree:
              [36]           ← tổng toàn bộ
           /         \
        [9]           [27]   ← tổng nửa trái / nửa phải
       /   \         /   \
    [4]    [5]    [16]  [11]
   /  \   /  \   /   \
  [1] [3][5] [7][9] [11]
```

### 🔧 Implement

```python
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)  # Cần gấp 4 lần kích thước mảng
        self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self._build(nums, left_child, start, mid)
            self._build(nums, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, idx, val, node=0, start=0, end=None):
        """Cập nhật nums[idx] = val – O(log n)"""
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if idx <= mid:
                self.update(idx, val, left_child, start, mid)
            else:
                self.update(idx, val, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, l, r, node=0, start=0, end=None):
        """Tổng đoạn [l, r] – O(log n)"""
        if end is None:
            end = self.n - 1
        if r < start or end < l:
            return 0   # Ngoài phạm vi
        if l <= start and end <= r:
            return self.tree[node]  # Nằm hoàn toàn trong phạm vi
        mid = (start + end) // 2
        left_sum = self.query(l, r, 2*node+1, start, mid)
        right_sum = self.query(l, r, 2*node+2, mid+1, end)
        return left_sum + right_sum

# Sử dụng
nums = [1, 3, 5, 7, 9, 11]
st = SegmentTree(nums)
print(st.query(1, 3))   # 3+5+7 = 15
st.update(2, 10)        # nums[2] = 10
print(st.query(1, 3))   # 3+10+7 = 20
```

### 🎯 Bài tập
1. LeetCode **#307** – Range Sum Query - Mutable ⭐
2. LeetCode **#315** – Count of Smaller Numbers After Self
3. LeetCode **#493** – Reverse Pairs (Hard)

---

## 21. Topological Sort (Sắp Xếp Topo)

### 📚 Khái niệm
Sắp xếp các đỉnh của **DAG** (Directed Acyclic Graph) sao cho mọi cạnh (u → v) thì u đứng trước v. Ứng dụng: phụ thuộc task, build systems, course prerequisites.

```
Đồ thị:  5 → 0 ← 4
          ↓   ↓
          2 → 3 → 1

Topological order: 4 5 2 0 3 1
(Nhiều đáp án đúng có thể tồn tại)
```

### 🔧 Hai cách implement

```python
from collections import deque

# ── Cách 1: Kahn's Algorithm (BFS-based) ─────────────────
def topological_sort_bfs(n, edges):
    """
    Dùng in-degree: đỉnh nào in-degree = 0 thì xử lý trước.
    Phát hiện cycle: nếu kết quả không đủ n đỉnh → có cycle.
    """
    graph = [[] for _ in range(n)]
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Bắt đầu từ các đỉnh không có tiên quyết (in-degree = 0)
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Nếu result không có đủ n đỉnh → graph có cycle
    return result if len(result) == n else []


# ── Cách 2: DFS-based ─────────────────────────────────────
def topological_sort_dfs(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    visited = [0] * n  # 0: chưa thăm, 1: đang thăm, 2: đã xong
    result = []
    has_cycle = [False]

    def dfs(node):
        if visited[node] == 1:   # Đang trong DFS path → cycle!
            has_cycle[0] = True
            return
        if visited[node] == 2:   # Đã xử lý rồi
            return

        visited[node] = 1
        for neighbor in graph[node]:
            dfs(neighbor)
        visited[node] = 2
        result.append(node)      # Thêm vào CUỐI (reverse postorder)

    for i in range(n):
        if visited[i] == 0:
            dfs(i)

    return [] if has_cycle[0] else result[::-1]


# ── Ứng dụng: Course Schedule ─────────────────────────────
def can_finish(num_courses, prerequisites):
    """LeetCode #207 – Có thể hoàn thành tất cả môn học không?"""
    result = topological_sort_bfs(num_courses, prerequisites)
    return len(result) == num_courses
```

### 🎯 Bài tập
1. LeetCode **#207** – Course Schedule ⭐
2. LeetCode **#210** – Course Schedule II ⭐
3. LeetCode **#269** – Alien Dictionary (Hard)

---

## 22. Bit Manipulation

### 📚 Khái niệm
Thao tác trực tiếp trên **bit nhị phân** để tối ưu tốc độ và bộ nhớ. Thường xuất hiện trong phỏng vấn embedded/systems và các bài toán về tập hợp.

| Phép toán | Ký hiệu | Ví dụ (5 & 3) | Kết quả |
|-----------|---------|----------------|---------|
| AND | `&` | 101 & 011 | 001 = 1 |
| OR | `\|` | 101 \| 011 | 111 = 7 |
| XOR | `^` | 101 ^ 011 | 110 = 6 |
| NOT | `~` | ~101 | ...010 |
| Left Shift | `<<` | 1 << 3 | 8 |
| Right Shift | `>>` | 8 >> 2 | 2 |

### 🔧 Các trick quan trọng

```python
# ── Trick thường gặp trong phỏng vấn ─────────────────────

# 1. Kiểm tra bit thứ i có = 1 không
def is_bit_set(n, i):
    return (n >> i) & 1 == 1

# 2. Đếm số bit 1 (Hamming Weight)
def count_bits(n):
    count = 0
    while n:
        count += n & 1   # Kiểm tra bit cuối
        n >>= 1          # Dịch phải 1 bit
    return count

# 3. Brian Kernighan's trick – O(số bit 1)
def count_bits_fast(n):
    count = 0
    while n:
        n &= (n - 1)  # Xóa bit 1 thấp nhất
        count += 1
    return count

# 4. Kiểm tra số là lũy thừa của 2
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
# Giải thích: 8 = 1000, 7 = 0111 → 1000 & 0111 = 0000

# 5. XOR để tìm số duy nhất (các số khác xuất hiện 2 lần)
def single_number(nums):
    """LeetCode #136 – O(n) time, O(1) space"""
    result = 0
    for num in nums:
        result ^= num   # a ^ a = 0, a ^ 0 = a
    return result
# [4,1,2,1,2] → 4^1^2^1^2 = 4^(1^1)^(2^2) = 4^0^0 = 4

# 6. Swap không dùng biến tạm
def swap(a, b):
    a ^= b  # a = a^b
    b ^= a  # b = b^(a^b) = a
    a ^= b  # a = (a^b)^a = b
    return a, b

# 7. Bit Masking – đại diện tập hợp bằng số nguyên
# Tập con của {A, B, C, D} (4 phần tử) → dùng số 4-bit
# 1010 → tập {B, D} (bit 1 = có, bit 0 = không có)
mask = 0b1010  # = 10
element_b = 1  # index 1
has_b = (mask >> element_b) & 1  # = 1 → có B trong tập
```

### 🎯 Bài tập
1. LeetCode **#136** – Single Number ⭐
2. LeetCode **#191** – Number of 1 Bits
3. LeetCode **#338** – Counting Bits
4. LeetCode **#268** – Missing Number (XOR trick)
5. LeetCode **#190** – Reverse Bits

---

## 🗺️ BẢNG NHẬN DIỆN PATTERN (PATTERN RECOGNITION GUIDE)

> **Đây là bảng quan trọng nhất để chinh phục LeetCode!**  
> Khi đọc đề bài, hãy tìm **dấu hiệu** để chọn đúng pattern.

### 🔍 Dấu hiệu nhận biết

| Dấu hiệu trong đề | Pattern nên dùng | Ví dụ |
|-------------------|-----------------|-------|
| "Dãy con liên tiếp" (subarray/substring) | **Sliding Window** | Longest Substring Without Repeating |
| Mảng đã sắp xếp + tìm cặp | **Two Pointers** | Two Sum II, 3Sum |
| "Lớn nhất / nhỏ nhất" trong đoạn | **Monotonic Stack/Queue** | Largest Rectangle |
| "K phần tử lớn/nhỏ nhất" | **Heap** | Top K Frequent |
| "Đường đi ngắn nhất" (unweighted) | **BFS** | Word Ladder |
| "Đường đi ngắn nhất" (weighted) | **Dijkstra** | Network Delay Time |
| "Tất cả tổ hợp / hoán vị" | **Backtracking** | Permutations, Subsets |
| "Tối đa / tối thiểu / đếm cách" | **Dynamic Programming** | Coin Change, LCS |
| "Mua sớm nhất, tối ưu từng bước" | **Greedy** | Jump Game, Merge Intervals |
| "Tìm kiếm trong mảng sắp xếp" | **Binary Search** | Search in Rotated Array |
| "Prefix sum / Range sum" | **Prefix Sum** | Subarray Sum Equals K |
| "Connected components / Cycle" | **Union-Find hoặc DFS** | Number of Islands |
| "Thứ tự phụ thuộc" (prerequisites) | **Topological Sort** | Course Schedule |
| "Số lần xuất hiện / tần suất" | **Hash Map** | Group Anagrams |
| "Từ bắt đầu bằng... / prefix" | **Trie** | Implement Trie |

### ⏱️ Bảng Big O nhanh

```
Khi cần O(1)     → Hash Map, Array indexing
Khi cần O(log n) → Binary Search, Heap operations
Khi cần O(n)     → Two Pointers, Sliding Window, Prefix Sum
Khi cần O(n log n) → Sorting, Merge Sort, Heap sort
Khi cần O(n²)    → Nested loops (Brute Force) – cần tối ưu
Khi có O(2ⁿ)     → Backtracking (thường kết hợp pruning)
```

---

## 💼 Q&A PHỎNG VẤN THỰC CHIẾN

### Phần 1: Câu hỏi lý thuyết thường gặp

**Q1: Khi nào dùng Array, khi nào dùng Linked List?**
> **Array:** Khi cần truy cập ngẫu nhiên nhanh (O(1)), kích thước biết trước hoặc ít thay đổi.  
> **Linked List:** Khi insert/delete đầu danh sách thường xuyên (O(1)), kích thước thay đổi liên tục, không cần truy cập ngẫu nhiên.

---

**Q2: Giải thích sự khác biệt giữa Stack và Queue?**
> **Stack (LIFO):** Phần tử thêm vào sau được lấy ra trước. Dùng cho: hàm đệ quy (call stack), undo/redo, backtracking, kiểm tra ngoặc.  
> **Queue (FIFO):** Phần tử thêm vào trước được lấy ra trước. Dùng cho: BFS, xử lý tác vụ theo thứ tự, print queue.

---

**Q3: Hash Map hoạt động như thế nào? Xử lý collision ra sao?**
> Hash Map dùng **hash function** để ánh xạ key → index trong mảng.
> 
> **Xử lý collision:**
> - **Chaining:** Mỗi bucket là một linked list (Python dict dùng cách này).
> - **Open Addressing:** Nếu bucket bị chiếm, tìm bucket trống tiếp theo (linear probing, quadratic probing).
> 
> **Worst case:** O(n) khi mọi key hash ra cùng bucket. **Average case:** O(1).

---

**Q4: Tại sao Quick Sort nhanh hơn Merge Sort trong thực tế dù cùng O(n log n)?**
> - Quick Sort hoạt động **in-place** (O(log n) space cho call stack), cache-friendly.
> - Merge Sort cần O(n) space phụ để merge.
> - Tuy nhiên, Quick Sort có worst case O(n²) nếu chọn pivot tệ (mảng đã sắp xếp). Python's `sorted()` dùng **Timsort** – kết hợp Merge Sort và Insertion Sort, ổn định với O(n log n) guaranteed.

---

**Q5: DFS vs BFS – khi nào dùng loại nào?**
> **DFS (stack/đệ quy):**
> - Cần duyệt toàn bộ đồ thị/cây
> - Backtracking (tìm tất cả đường đi)
> - Phát hiện cycle
> - Topological sort
> 
> **BFS (queue):**
> - Tìm đường đi **ngắn nhất** (unweighted graph)
> - Duyệt theo tầng (level-order)
> - Multi-source problems (Rotting Oranges)

---

**Q6: Dynamic Programming khác Recursion ở điểm gì?**
> **Recursion thường:** Giải bài toán con trùng lặp nhiều lần → **O(2ⁿ)** (Fibonacci naive).
> 
> **DP = Recursion + Memoization (hoặc Tabulation):** Lưu kết quả bài toán con → mỗi bài toán con chỉ giải **1 lần** → **O(n)**.
> 
> **Key insight:** DP chỉ áp dụng được khi bài toán có **optimal substructure** (đáp án tối ưu chứa đáp án tối ưu của bài toán con).

---

### Phần 2: Coding Interview Tips

**🎯 Quy trình giải bài trong phỏng vấn (UMPIRE Method):**
```
U – Understand  : Đọc kỹ đề, hỏi lại constraints. Input/Output là gì? Edge cases?
M – Match       : Liên hệ với pattern đã biết. Dấu hiệu nào trong đề gợi ý pattern?
P – Plan        : Nêu thuật toán bằng lời (pseudo-code) trước khi code.
I – Implement   : Code sạch, đặt tên biến rõ ràng.
R – Review      : Debug trace qua ví dụ đơn giản.
E – Evaluate    : Phân tích Big O time & space complexity.
```

**⚠️ Edge cases cần kiểm tra:**
```python
# Luôn hỏi/kiểm tra:
# - Mảng rỗng: []
# - Một phần tử: [1]
# - Tất cả cùng giá trị: [3, 3, 3]
# - Số âm trong mảng
# - Overflow với số nguyên lớn
# - Chuỗi rỗng ""
# - n = 0, n = 1
# - Graph không liên thông
```

**💬 Cách giao tiếp khi bị stuck:**
```
1. "Để tôi bắt đầu với brute force O(n²) trước..."
2. "Tôi thấy đây có pattern của Sliding Window vì..."
3. "Trade-off ở đây là: nếu dùng HashMap thì tốn thêm O(n) space nhưng đổi lại O(n) time..."
4. "Cho tôi trace qua example này để verify..."
```

---

## 📊 DANH SÁCH 75 BÀI LEETCODE PHẢI BIẾT (NeetCode 75)

> Đây là danh sách bài tập được tuyển chọn, bao phủ đủ mọi pattern quan trọng.

### Arrays & Hashing (9 bài)
| # | Bài | Difficulty | Pattern |
|---|-----|-----------|---------|
| 217 | Contains Duplicate | Easy | HashSet |
| 242 | Valid Anagram | Easy | HashMap |
| 1 | Two Sum | Easy | HashMap |
| 49 | Group Anagrams | Medium | HashMap |
| 347 | Top K Frequent Elements | Medium | Heap/Bucket Sort |
| 238 | Product of Array Except Self | Medium | Prefix/Suffix |
| 36 | Valid Sudoku | Medium | HashSet |
| 128 | Longest Consecutive Sequence | Medium | HashSet |
| 271 | Encode and Decode Strings | Medium | Design |

### Two Pointers (5 bài)
| # | Bài | Difficulty | Pattern |
|---|-----|-----------|---------|
| 125 | Valid Palindrome | Easy | Two Pointers |
| 167 | Two Sum II | Medium | Two Pointers |
| 15 | 3Sum | Medium | Sort + Two Pointers |
| 11 | Container With Most Water | Medium | Two Pointers |
| 42 | Trapping Rain Water | Hard | Two Pointers |

### Sliding Window (4 bài)
| # | Bài | Difficulty | Pattern |
|---|-----|-----------|---------|
| 121 | Best Time to Buy and Sell Stock | Easy | Sliding Window |
| 3 | Longest Substring Without Repeating Chars | Medium | Sliding Window |
| 424 | Longest Repeating Character Replacement | Medium | Sliding Window |
| 76 | Minimum Window Substring | Hard | Sliding Window |

### Stack (7 bài)
| # | Bài | Difficulty | Pattern |
|---|-----|-----------|---------|
| 20 | Valid Parentheses | Easy | Stack |
| 155 | Min Stack | Medium | Stack |
| 150 | Evaluate Reverse Polish Notation | Medium | Stack |
| 22 | Generate Parentheses | Medium | Backtracking |
| 739 | Daily Temperatures | Medium | Monotonic Stack |
| 853 | Car Fleet | Medium | Monotonic Stack |
| 84 | Largest Rectangle in Histogram | Hard | Monotonic Stack |

### Binary Search (7 bài)
| # | Bài | Difficulty | Pattern |
|---|-----|-----------|---------|
| 704 | Binary Search | Easy | Binary Search |
| 74 | Search a 2D Matrix | Medium | Binary Search |
| 875 | Koko Eating Bananas | Medium | BS on Value |
| 153 | Find Minimum in Rotated Sorted Array | Medium | Binary Search |
| 33 | Search in Rotated Sorted Array | Medium | Binary Search |
| 981 | Time Based Key-Value Store | Medium | Binary Search |
| 4 | Median of Two Sorted Arrays | Hard | Binary Search |

### Linked List (6 bài)
| # | Bài | Difficulty | Pattern |
|---|-----|-----------|---------|
| 206 | Reverse Linked List | Easy | Iterative/Recursive |
| 21 | Merge Two Sorted Lists | Easy | Two Pointers |
| 143 | Reorder List | Medium | Fast & Slow |
| 19 | Remove Nth Node From End | Medium | Two Pointers |
| 141 | Linked List Cycle | Easy | Fast & Slow |
| 23 | Merge K Sorted Lists | Hard | Heap |

### Trees (11 bài)
| # | Bài | Difficulty | Pattern |
|---|-----|-----------|---------|
| 226 | Invert Binary Tree | Easy | DFS |
| 104 | Maximum Depth of Binary Tree | Easy | DFS |
| 100 | Same Tree | Easy | DFS |
| 572 | Subtree of Another Tree | Easy | DFS |
| 235 | Lowest Common Ancestor of BST | Medium | DFS |
| 102 | Binary Tree Level Order Traversal | Medium | BFS |
| 199 | Binary Tree Right Side View | Medium | BFS |
| 1448 | Count Good Nodes in Binary Tree | Medium | DFS |
| 98 | Validate Binary Search Tree | Medium | DFS |
| 230 | Kth Smallest Element in BST | Medium | DFS Inorder |
| 105 | Construct Binary Tree from Preorder+Inorder | Medium | DFS |

### Graphs (9 bài)
| # | Bài | Difficulty | Pattern |
|---|-----|-----------|---------|
| 200 | Number of Islands | Medium | DFS/BFS |
| 133 | Clone Graph | Medium | DFS/BFS |
| 695 | Max Area of Island | Medium | DFS |
| 417 | Pacific Atlantic Water Flow | Medium | DFS/BFS |
| 130 | Surrounded Regions | Medium | DFS |
| 994 | Rotting Oranges | Medium | Multi-source BFS |
| 207 | Course Schedule | Medium | Topological Sort |
| 210 | Course Schedule II | Medium | Topological Sort |
| 743 | Network Delay Time | Medium | Dijkstra |

### Dynamic Programming (15 bài)
| # | Bài | Difficulty | Pattern |
|---|-----|-----------|---------|
| 70 | Climbing Stairs | Easy | 1D DP |
| 746 | Min Cost Climbing Stairs | Easy | 1D DP |
| 198 | House Robber | Medium | 1D DP |
| 213 | House Robber II | Medium | 1D DP |
| 5 | Longest Palindromic Substring | Medium | 2D DP |
| 647 | Palindromic Substrings | Medium | 2D DP |
| 91 | Decode Ways | Medium | 1D DP |
| 322 | Coin Change | Medium | 1D DP |
| 152 | Maximum Product Subarray | Medium | 1D DP |
| 139 | Word Break | Medium | 1D DP |
| 300 | Longest Increasing Subsequence | Medium | 1D DP |
| 416 | Partition Equal Subset Sum | Medium | 0/1 Knapsack |
| 1143 | Longest Common Subsequence | Medium | 2D DP |
| 309 | Best Time Buy+Sell Stock w/ Cooldown | Medium | State Machine DP |
| 312 | Burst Balloons | Hard | Interval DP |

### Greedy & Intervals (5 bài)
| # | Bài | Difficulty | Pattern |
|---|-----|-----------|---------|
| 53 | Maximum Subarray | Medium | Kadane / Greedy |
| 55 | Jump Game | Medium | Greedy |
| 45 | Jump Game II | Medium | Greedy |
| 134 | Gas Station | Medium | Greedy |
| 56 | Merge Intervals | Medium | Sort + Greedy |

### Backtracking (7 bài)
| # | Bài | Difficulty | Pattern |
|---|-----|-----------|---------|
| 78 | Subsets | Medium | Backtracking |
| 39 | Combination Sum | Medium | Backtracking |
| 40 | Combination Sum II | Medium | Backtracking |
| 46 | Permutations | Medium | Backtracking |
| 90 | Subsets II | Medium | Backtracking |
| 79 | Word Search | Medium | DFS + Backtracking |
| 51 | N-Queens | Hard | Backtracking |

---

## 🏆 PHƯƠNG PHÁP HỌC HIỆU QUẢ NHẤT

### Chu trình học 1 chủ đề (áp dụng cho mỗi mục trong giáo trình này)

```
Ngày 1: Học lý thuyết (đọc tài liệu, xem hình ảnh minh họa)
            ↓
Ngày 2: Implement từ đầu (không nhìn đáp án)
            ↓
Ngày 3: Giải 3-5 bài Easy trên LeetCode liên quan
            ↓
Ngày 4: Giải 2-3 bài Medium (chấp nhận bị mắc kẹt)
            ↓
Ngày 5: Review lại code, so sánh với best solution, note lại pattern
            ↓
Ngày 7+: Ôn lại (spaced repetition)
```

### Hệ thống Spaced Repetition cho LeetCode
```
Lần 1: Làm lần đầu (dù nhìn đáp án cũng OK)
Lần 2: Làm lại sau 1 ngày (không nhìn đáp án)
Lần 3: Làm lại sau 1 tuần
Lần 4: Làm lại sau 2 tuần
→ Sau lần 4: Bài đã "vào não", không cần ôn nữa
```

### Template ghi chú mỗi bài LeetCode

```markdown
## #[số] - [Tên bài]

**Pattern:** Sliding Window / Two Pointers / DP / ...
**Difficulty:** Easy / Medium / Hard
**Time:** O(?)  |  **Space:** O(?)

**Ý tưởng chính:**
- Bước 1: ...
- Bước 2: ...

**Edge cases:**
- []
- [1]
- Số âm?

**Code:**
```python
def solution(...):
    ...
```

**Nhận xét:**
- Điểm khó: ...
- Lần sau nhớ: ...
```

---

*📌 Cập nhật: 2026-03-17 | Tác giả: Antigravity AI*  
*🔗 Thực hành tại: [LeetCode](https://leetcode.com) | [NeetCode](https://neetcode.io)*
