# 02. Cấu Trúc Tuyến Tính & Bảng Băm (Góc nhìn Senior)

> Lý thuyết nền: [`DSA_Giao_Trinh_Chi_Tiet.md`](../../../02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md) mục 3 (Array), 4 (Linked List), 5 (Stack), 6 (Queue), 7 (Hash Table).

---

## 1. Array — vì sao mọi database, mọi ngôn ngữ đều xây trên nó

**Sự thật ít ai để ý:** `list` trong Python không phải "mảng" thuần túy — nó là **mảng động (dynamic array)**: khi đầy, Python cấp phát vùng nhớ mới lớn hơn (thường ×1.125) và copy toàn bộ phần tử sang. Đây là lý do `append()` là O(1) *amortized* chứ không phải O(1) tuyệt đối — thỉnh thoảng có 1 lần copy tốn O(n).

### Ứng dụng thực tế

- **Contiguous memory → cache locality:** mảng nằm liền kề trong bộ nhớ nên CPU cache hit cao hơn linked list. Đây là lý do dù Big O giống nhau, `array`/`numpy.array` luôn nhanh hơn linked list trong thực tế đo benchmark — kiến thức này quan trọng khi tối ưu hệ thống xử lý dữ liệu lớn (data pipeline, ML feature vector).
- **Phân trang (Pagination) trong API:** mọi API `GET /orders?page=2&limit=20` thực chất là slicing mảng/array trên DB — hiểu rõ độ phức tạp `OFFSET` trong SQL (O(offset+limit), càng về sau càng chậm) là kiến thức senior bắt buộc khi thiết kế phân trang cho bảng hàng triệu dòng → giải pháp thực tế là **cursor-based pagination** (dùng ID/timestamp làm con trỏ thay vì OFFSET).

```python
# ❌ OFFSET pagination — chậm dần khi page tăng (DB phải quét qua hết offset)
"SELECT * FROM orders ORDER BY id LIMIT 20 OFFSET 100000"

# ✅ Cursor-based pagination — luôn O(log n) nhờ index, dùng ở Facebook/Twitter API thật
"SELECT * FROM orders WHERE id > :last_seen_id ORDER BY id LIMIT 20"
```

---

## 2. Linked List — ít dùng trực tiếp, nhưng là nền tảng của hạ tầng thật

Trong công việc hàng ngày, senior dev **hiếm khi tự cài linked list** — nhưng linked list là mô hình tư duy đứng sau rất nhiều hệ thống:

| Nơi Linked List xuất hiện thật | Vì sao không dùng Array |
|---|---|
| **LRU Cache** (Redis, trình duyệt, `functools.lru_cache` nội bộ) | Cần xóa/chèn node ở giữa O(1) khi cập nhật thứ tự truy cập gần nhất — Array phải dịch chuyển O(n) |
| **Undo/Redo trong editor** (VS Code, Photoshop) | Danh sách các trạng thái, con trỏ di chuyển tới/lui, chèn node mới ở giữa dễ dàng |
| **Hệ điều hành: quản lý tiến trình, bộ nhớ (free list)** | Linked list of blocks giúp cấp phát/giải phóng bộ nhớ động mà không cần dịch chuyển toàn bộ |
| **Blockchain** | Mỗi block trỏ tới hash của block trước — bản chất là linked list một chiều bất biến |

### 🔥 Case thật: LRU Cache — câu hỏi phỏng vấn senior kinh điển vì nó LÀ hệ thống thật

```python
from collections import OrderedDict

class LRUCache:
    """Chính là cơ chế Redis dùng để evict key khi hết bộ nhớ (maxmemory-policy allkeys-lru)."""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # Hash Table + Doubly Linked List kết hợp

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # O(1) nhờ doubly linked list bên trong
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # xóa phần tử least-recently-used
```

**Tại sao đây không chỉ là bài tập:** đây chính xác là cơ chế cache ở tầng CDN, database buffer pool (MySQL InnoDB Buffer Pool dùng biến thể LRU), và trình duyệt cache tài nguyên tĩnh.

---

## 3. Stack — vòng đời request, undo, và... security

- **Call stack:** mọi function call trong mọi ngôn ngữ đều dùng stack — hiểu stack giải thích tại sao có "stack trace" khi exception xảy ra, và tại sao đệ quy sâu gây Stack Overflow (liên kết Module 01).
- **Trình duyệt (Back button), Undo trong editor:** stack of history states.
- **Validate dấu ngoặc / cú pháp:** trình biên dịch, linter, formatter (Prettier, Black) dùng stack để kiểm tra cân bằng ngoặc `(){}[]` — bài "Valid Parentheses" chính là lõi của một syntax checker thật.
- **Bảo mật:** Buffer Overflow attack (tấn công cổ điển) khai thác chính cơ chế call stack — hiểu stack giúp hiểu vì sao ngôn ngữ có bounds-checking (Python, Java) an toàn hơn C ở khía cạnh này.

```python
def is_balanced(expression: str) -> bool:
    """Lõi thuật toán đứng sau mọi trình kiểm tra cú pháp JSON/code editor."""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack
```

---

## 4. Queue — xương sống của mọi hệ thống bất đồng bộ

Đây là chủ đề mà **senior backend/devops dùng hàng ngày**, không phải lý thuyết suông:

| Khái niệm Queue trong DSA | Hệ thống thật tương ứng |
|---|---|
| FIFO Queue | RabbitMQ, AWS SQS, Kafka (partition), Laravel Queue (đã có trong repo bạn — `06-Exercises`) |
| Circular Queue (buffer giới hạn) | Ring buffer trong xử lý audio/video streaming, log buffer |
| Priority Queue | Xem Module 03 (Heap) — task scheduler, Kubernetes pod scheduling |
| Double-ended Queue (deque) | `collections.deque` — dùng cho Sliding Window (Module 06), work-stealing giữa các thread |

### 🔥 Case thật: Vì sao hệ thống cần Message Queue thay vì gọi API trực tiếp?

Khi user bấm "Đặt hàng", nếu xử lý đồng bộ (gửi email, trừ kho, gọi payment gateway) trong 1 request → nếu payment gateway chậm 5s, user phải đợi 5s, và nếu server crash giữa chừng → mất dữ liệu. Giải pháp senior: đẩy các tác vụ phụ vào **Queue** (SQS/RabbitMQ), worker xử lý bất đồng bộ, có retry + dead-letter-queue khi lỗi.

```python
from collections import deque

class TaskQueue:
    """Mô hình đơn giản hóa của một worker queue thật (Celery, BullMQ...)."""
    def __init__(self):
        self.queue = deque()

    def enqueue(self, task):
        self.queue.append(task)          # O(1) — deque tối ưu hơn list.pop(0) vốn là O(n)!

    def dequeue(self):
        return self.queue.popleft() if self.queue else None  # O(1)
```

**Pitfall kinh điển:** dùng `list.pop(0)` để làm queue trong Python — đây là O(n) vì phải dịch chuyển toàn bộ phần tử còn lại. Senior luôn dùng `collections.deque` cho queue thật.

---

## 5. Hash Table — cấu trúc dữ liệu quan trọng nhất trong công việc hàng ngày

Không ngoa khi nói: **90% tối ưu hiệu năng ở tầng ứng dụng (không phải DB) đến từ việc thay O(n) tìm kiếm tuyến tính bằng O(1) tra cứu hash**.

### Ứng dụng thực tế

- **Index database:** Hash Index (Postgres `USING HASH`) dùng cho tra cứu bằng (`=`), khác với B-Tree index dùng cho range query (`<`, `>`, `BETWEEN`).
- **Caching layer:** Redis/Memcached về bản chất là **hash table phân tán** — key-value store.
- **Deduplicate dữ liệu:** loại email trùng, phát hiện request trùng (idempotency key trong thanh toán) — dùng `set()`/hash để check tồn tại O(1).
- **Rate limiting:** đếm số request theo `user_id` trong khung thời gian — hash map `{user_id: count}`.
- **Load Balancing — Consistent Hashing:** đây là kỹ thuật senior-level thật sự dùng trong production (CDN, Cassandra, Memcached cluster) để phân phối request/dữ liệu đều lên nhiều server mà khi thêm/bớt server chỉ phải re-map tối thiểu dữ liệu (khác hash `mod n` thông thường sẽ re-map gần như toàn bộ khi n đổi).

### ⚠️ Vấn đề thực tế: Hash Collision & DoS

Nếu hàm hash yếu và kẻ tấn công cố tình gửi nhiều key gây collision hàng loạt → hash table suy biến thành linked list O(n) cho mỗi thao tác → **Hash DoS attack**. Đây là lý do Python (từ 3.3+) có **hash randomization** (`PYTHONHASHSEED`) để attacker không đoán trước được giá trị hash và tạo collision cố ý.

```python
# Rate limiter thực tế dùng Hash Table + sliding window timestamp
from collections import defaultdict
import time

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = defaultdict(list)  # {user_id: [timestamp, ...]}

    def is_allowed(self, user_id: str) -> bool:
        now = time.time()
        self.requests[user_id] = [t for t in self.requests[user_id] if now - t < self.window]
        if len(self.requests[user_id]) >= self.max_requests:
            return False
        self.requests[user_id].append(now)
        return True
```

---

## 🎯 Câu hỏi senior hay hỏi khi review thiết kế hệ thống

1. "Bạn dùng OFFSET pagination hay cursor-based? Với bảng 10 triệu dòng, cái nào sẽ chậm dần?"
2. "Queue giữa 2 service của bạn có đảm bảo at-least-once hay exactly-once delivery? Xử lý message trùng (idempotency) thế nào?"
3. "Hash key của bạn có thể bị đoán trước để tấn công collision không?"

## 🔗 Liên kết module khác
- Priority Queue (biến thể nâng cao của Queue) → [`03-Trees-Heaps-Tries`](../03-Trees-Heaps-Tries/README.md)
- Sliding Window dùng Deque → [`06-Advanced-Patterns`](../06-Advanced-Patterns/README.md)
- Union-Find giải quyết bài toán "gom nhóm" mà Hash Table không làm được hiệu quả → [`04-Graphs-And-Union-Find`](../04-Graphs-And-Union-Find/README.md)
