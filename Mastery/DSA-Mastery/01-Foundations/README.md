# 01. Foundations — Big O & Đệ Quy (Góc nhìn Senior)

> Lớp kiến thức nền — lý thuyết cơ bản đã có đầy đủ tại [`02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md`](../../02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md#1-big-o-notation--tư-duy-tối-ưu) (mục 1-2). File này **không lặp lại** phần đó mà bổ sung lớp "vì sao hệ thống thật cần cái này" và "sai ở đâu thì hệ thống sập".

---

## 1. Big O — không phải bài tập hàn lâm, mà là ngân sách hiệu năng

### Senior nghĩ gì khác với junior?

Junior học Big O để pass phỏng vấn. Senior dùng Big O để **trả lời câu hỏi kinh doanh**: "Tính năng này có sống được khi data tăng 100x không?" Trước khi viết dòng code đầu tiên, senior dev luôn ước lượng:

- **n hiện tại là bao nhiêu, và sẽ là bao nhiêu sau 1-2 năm?** (10K user khác 10M user).
- **Request này chạy bao nhiêu lần/giây?** O(n²) chạy 1 lần/ngày (batch job ban đêm) là chấp nhận được; O(n²) chạy trên mỗi HTTP request là thảm họa.
- **Độ trễ (latency) hay thông lượng (throughput) quan trọng hơn?** Đôi khi chấp nhận O(n log n) chậm hơn để giữ bộ nhớ thấp trên container giới hạn RAM.

### Ứng dụng thực tế — nơi Big O quyết định kiến trúc

| Tình huống thực tế | Vấn đề Big O | Giải pháp senior áp dụng |
|---|---|---|
| API tìm kiếm user theo email trong bảng 50 triệu dòng | `WHERE email = ?` không có index → **O(n) full table scan** | Thêm B-Tree index (O(log n)) — đây chính là lý do DBA luôn hỏi "cột này có index chưa?" |
| Endpoint `/friends/mutual` so 2 danh sách bạn bè | So sánh lồng nhau O(n·m) | Đổi 1 danh sách thành `set()` → O(n+m). Đây là pattern "Two Sum" áp dụng thẳng vào production. |
| Autocomplete search box gõ mỗi ký tự gọi API | Mỗi lần gõ trigger 1 query O(n) trên DB | Debounce (giảm số lần gọi) + Trie/Elasticsearch ở phía server (xem Module 03) |
| Dashboard admin tính tổng doanh thu real-time mỗi lần load trang | O(n) quét lại toàn bộ đơn hàng mỗi request | Pre-aggregate (materialized view / cache Redis), cập nhật dần thay vì tính lại từ đầu |

### 🔥 Case thật: "Tính năng chạy mượt lúc demo, sập khi lên production"

Kịch bản kinh điển: dev viết tính năng gợi ý sản phẩm liên quan bằng cách duyệt toàn bộ catalog để so sánh từng sản phẩm — O(n²) với 500 sản phẩm demo thì mượt (250,000 phép tính, <1s). Lên production với 2 triệu sản phẩm → 4×10¹² phép tính → server treo, CPU 100%, autoscaler bật hết instance mà vẫn timeout.

**Bài học senior:** luôn hỏi "n trong môi trường thật lớn cỡ nào" TRƯỚC khi chọn thuật toán, không phải sau khi incident xảy ra. Đây là lý do các buổi *system design review* luôn có câu hỏi bắt buộc: "Complexity của thao tác này theo n là gì?"

### Space Complexity trong thực tế — vấn đề bị đánh giá thấp

RAM trên container (Kubernetes pod, Lambda) luôn bị giới hạn cứng (VD: 512MB). Một thuật toán O(n) *thời gian* nhưng O(n) *bộ nhớ thêm* (tạo mảng mới, load hết vào RAM) có thể làm pod bị **OOMKilled** dù CPU vẫn rảnh. Senior luôn cân nhắc:

- Xử lý **streaming/generator** thay vì load hết vào list khi n lớn (VD: đọc file log hàng GB bằng generator thay vì `readlines()`).
- Thuật toán in-place (`reverse_in_place`) khi bộ nhớ là tài nguyên khan hiếm (mobile, edge devices, embedded).

---

## 2. Đệ quy (Recursion) — sức mạnh và cái bẫy chết người: Stack Overflow

### Vì sao hệ thống thật ngại đệ quy?

Python mặc định giới hạn độ sâu đệ quy ~1000 (`sys.getrecursionlimit()`). Một hàm đệ quy xử lý cây thư mục, cây tổ chức công ty, hoặc cây bình luận lồng nhau (nested comments) có thể **crash thật** nếu dữ liệu người dùng tạo ra một cấu trúc quá sâu (VD: JSON lồng 10,000 cấp — có thể là tấn công DoS cố ý).

```python
import sys

# ❌ Nguy hiểm trên production: không kiểm soát độ sâu
def count_nested(data):
    if isinstance(data, dict):
        return 1 + sum(count_nested(v) for v in data.values())
    return 0

# ✅ Senior fix: chuyển sang lặp (iterative) dùng stack tường minh
def count_nested_safe(data):
    stack = [data]
    count = 0
    while stack:
        item = stack.pop()
        if isinstance(item, dict):
            count += 1
            stack.extend(item.values())
    return count
```

**Nguyên tắc thực chiến:** mọi đệ quy xử lý dữ liệu **do người dùng cung cấp** (JSON, cây thư mục upload, cấu trúc XML) phải được đánh giá: có thể chuyển sang lặp bằng stack tường minh không? Nếu không, phải giới hạn độ sâu tối đa và trả lỗi có kiểm soát thay vì để crash.

### Tail Call & vì sao Python không tối ưu được

Nhiều ngôn ngữ (Scheme, Erlang, một phần JS engine) tối ưu hóa *tail call* để đệ quy không phình stack. **Python thì không** — đây là kiến thức senior bắt buộc biết để không áp dụng nhầm mindset từ ngôn ngữ khác. Hệ quả thực tế: khi porting logic từ Elixir/Erlang (hay dùng đệ quy đuôi cho vòng lặp) sang Python, phải chuyển toàn bộ về vòng lặp `while`/`for`.

### Memoization — từ bài tập Fibonacci đến hệ thống thật

```python
from functools import lru_cache

# Dùng trong production: cache kết quả API call tính toán nặng theo tham số
@lru_cache(maxsize=1024)
def compute_shipping_cost(origin: str, destination: str, weight: int) -> float:
    ...  # gọi API bên thứ 3 tốn tiền mỗi lần gọi
```

`@lru_cache` chính là kỹ thuật memoization của bài toán Fibonacci/DP, được đóng gói sẵn trong thư viện chuẩn Python và dùng trực tiếp trong code production để giảm số lần gọi API trả phí hoặc query DB lặp lại.

### ⚠️ Pitfall thực tế: Mutable default argument trong hàm đệ quy

```python
# ❌ Bug kinh điển — list "path" bị chia sẻ giữa các lần gọi
def find_paths(node, path=[]):
    path.append(node)
    ...

# ✅ Đúng
def find_paths(node, path=None):
    if path is None:
        path = []
    path = path + [node]  # tạo list mới, không mutate list cũ
```

---

## 🎯 Câu hỏi senior hay hỏi khi phỏng vấn/review code

1. "Complexity này là worst-case hay average-case? Có amortized cost nào không?" (VD: `list.append()` là O(1) amortized nhờ dynamic resizing, không phải O(1) tuyệt đối).
2. "Nếu input tăng 1000 lần, hệ thống của bạn phản ứng thế nào — bạn có SLA/benchmark nào chứng minh không?"
3. "Đệ quy này có thể bị stack overflow với input độc hại (adversarial input) không?"

## 🔗 Liên kết module khác
- Kỹ thuật giảm complexity bằng Hash Table → [`02-Linear-Structures-And-Hashing`](../02-Linear-Structures-And-Hashing/README.md)
- Đệ quy áp dụng trong duyệt cây/đồ thị → [`03-Trees-Heaps-Tries`](../03-Trees-Heaps-Tries/README.md), [`04-Graphs-And-Union-Find`](../04-Graphs-And-Union-Find/README.md)
- Memoization là nền tảng của Dynamic Programming → [`06-Advanced-Patterns`](../06-Advanced-Patterns/README.md)
