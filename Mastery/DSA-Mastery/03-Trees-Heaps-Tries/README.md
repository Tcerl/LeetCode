# 03. Cây, Heap & Trie (Góc nhìn Senior)

> Lý thuyết nền: [`DSA_Giao_Trinh_Chi_Tiet.md`](../../02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md) mục 8 (Binary Tree/BST), 9 (Heap), 11 (Trie).

---

## 1. Cây nhị phân & BST — trái tim của mọi hệ quản trị cơ sở dữ liệu

**Sự thật quan trọng nhất mà nhiều dev bỏ qua:** BST thuần (`left < root < right`) **gần như không được dùng trực tiếp** trong hệ thống thật vì nó dễ mất cân bằng (worst-case O(n) khi insert dữ liệu đã sắp xếp sẵn). Cái thật sự chạy dưới các hệ thống bạn dùng hàng ngày là các **biến thể cân bằng**:

| Cấu trúc | Nơi dùng thật |
|---|---|
| **B-Tree / B+Tree** | Index của MySQL (InnoDB), PostgreSQL, hầu hết RDBMS. Tối ưu cho đọc từ đĩa (mỗi node chứa nhiều key để giảm số lần I/O). |
| **Red-Black Tree** | `TreeMap`/`TreeSet` trong Java, `std::map` trong C++, Linux kernel scheduler (CFS - Completely Fair Scheduler dùng RB-Tree để chọn tiến trình chạy tiếp theo). |
| **AVL Tree** | Cân bằng chặt hơn RB-Tree, dùng khi đọc nhiều hơn ghi (ít dùng trực tiếp trong production ngày nay nhưng vẫn là câu hỏi lý thuyết senior). |
| **LSM Tree** (không phải cây nhị phân nhưng cùng họ "cây lưu trữ") | Cassandra, RocksDB, LevelDB — tối ưu cho ghi (write-heavy workload), khác hẳn B-Tree tối ưu đọc. |

### 🔥 Case thật: Vì sao "chọn đúng index" là kỹ năng senior quan trọng nhất về DB

```sql
-- Không có index: full table scan O(n) trên 10 triệu dòng
SELECT * FROM users WHERE email = 'a@b.com';

-- Có B-Tree index trên cột email: O(log n)
CREATE INDEX idx_users_email ON users(email);
```

Hiểu cây B-Tree giải thích được **vì sao** index tăng tốc `WHERE`/`ORDER BY` nhưng làm chậm `INSERT`/`UPDATE` (phải cập nhật lại cấu trúc cây) — đây là lý do senior không bao giờ "cứ thêm index cho chắc" mà cân nhắc read/write ratio của từng bảng.

### Traversal — không chỉ là bài tập, mà là mô hình xử lý cây thật

- **DFS (pre/in/post-order):** duyệt cây thư mục (`os.walk`), duyệt AST (Abstract Syntax Tree) khi trình biên dịch/parser phân tích code, duyệt DOM tree trong trình duyệt.
- **BFS (level-order):** tìm đường đi ngắn nhất theo số bước (không theo trọng số) — tổ chức công ty (tìm cấp quản lý gần nhất), gợi ý bạn bè "friend of friend".

```python
# In-order traversal của BST luôn cho ra dãy đã SẮP XẾP — đây là tính chất
# mà DB tận dụng để trả kết quả ORDER BY gần như miễn phí khi có index B-Tree.
def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.val)
        inorder(node.right, result)
    return result
```

---

## 2. Heap & Priority Queue — bộ não của mọi scheduler

Heap trả lời câu hỏi: **"Trong hàng ngàn việc đang chờ, việc nào quan trọng nhất cần làm NGAY?"** — đây là bài toán xuất hiện khắp nơi trong hệ thống thật:

| Hệ thống thật | Heap dùng để làm gì |
|---|---|
| **Kubernetes Scheduler** | Chọn pod nào được lên lịch chạy trước dựa trên priority class |
| **OS Process Scheduler** | Chọn tiến trình có priority cao nhất chạy tiếp theo |
| **Dijkstra's Algorithm** (tìm đường đi ngắn nhất — Google Maps, network routing) | Luôn lấy ra node có khoảng cách nhỏ nhất đã biết — chính là `heappop` |
| **Task Queue có độ ưu tiên** (đơn hàng VIP xử lý trước) | `heapq` trong Python, `PriorityQueue` trong Java |
| **Top-K problem** (top 10 sản phẩm bán chạy nhất trong 1 triệu sản phẩm) | Min-heap kích thước K — không cần sort toàn bộ O(n log n), chỉ cần O(n log k) |

```python
import heapq

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Bài toán thật: 'Top K sản phẩm được xem nhiều nhất hôm nay' trên trang chủ e-commerce.
    Dùng min-heap kích thước k thay vì sort toàn bộ — tiết kiệm đáng kể khi n rất lớn (hàng triệu SKU).
    """
    from collections import Counter
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

### ⚠️ Pitfall thực tế: Heap không phải cấu trúc để tìm kiếm

Heap chỉ đảm bảo phần tử **gốc** (root) là min/max — không đảm bảo thứ tự các phần tử còn lại. Junior hay nhầm dùng heap để "tìm phần tử X trong danh sách" — đó là sai chỗ, phải dùng Hash Table (Module 02) hoặc BST.

---

## 3. Trie (Cây tiền tố) — engine đứng sau autocomplete và spam filter

Trie giải quyết đúng 1 bài toán mà Hash Table không làm tốt: **tìm kiếm theo tiền tố (prefix)**.

### Ứng dụng thực tế

- **Autocomplete/Search suggestion:** Google Search, thanh tìm kiếm e-commerce — gõ "iph" gợi ý ngay "iphone 15", "iphone case"...
- **IP Routing (Longest Prefix Matching):** router mạng dùng biến thể Trie (Patricia Trie/Radix Tree) để quyết định gói tin đi đường nào dựa trên địa chỉ IP đích.
- **Spell checker / Từ điển:** kiểm tra từ có tồn tại + gợi ý từ gần đúng.
- **Content filter/Spam detection:** kiểm tra một đoạn text có chứa từ khóa cấm trong danh sách hàng chục nghìn từ — Trie/Aho-Corasick nhanh hơn nhiều so với so khớp từng từ.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    Lõi của mọi ô tìm kiếm autocomplete. Độ phức tạp tra cứu chỉ phụ thuộc
    độ dài từ khóa (O(L)), KHÔNG phụ thuộc số lượng từ trong từ điển (n) —
    đây là lợi thế quyết định so với duyệt tuyến tính khi từ điển có hàng triệu entry.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

**Trade-off senior cần biết:** Trie tốn bộ nhớ hơn Hash Table đáng kể (mỗi node giữ 1 dict con trỏ). Trong thực tế, hệ thống search quy mô lớn (Elasticsearch, Solr) dùng cấu trúc phức tạp hơn (FST - Finite State Transducer) để cân bằng giữa tốc độ và bộ nhớ — Trie là bước đệm tư duy để hiểu các cấu trúc đó.

---

## 🎯 Câu hỏi senior hay hỏi khi review

1. "Bảng này đọc nhiều hay ghi nhiều? Bạn chọn loại index nào và vì sao?"
2. "Nếu cần top 100 trong 50 triệu bản ghi cập nhật liên tục, bạn sort lại toàn bộ mỗi lần hay duy trì heap?"
3. "Autocomplete của bạn xử lý được bao nhiêu ký tự gõ mỗi giây? Bottleneck nằm ở DB, cache, hay thuật toán?"

## 🔗 Liên kết module khác
- Cây cân bằng liên quan mật thiết tới thiết kế Database Index → xem thêm khi làm folder `04-Database-Mastery` (đợt sau).
- Dijkstra dùng Heap là cầu nối sang → [`04-Graphs-And-Union-Find`](../04-Graphs-And-Union-Find/README.md)
- Backtracking trên cây/trie (sinh tất cả từ hợp lệ) → [`06-Advanced-Patterns`](../06-Advanced-Patterns/README.md)
