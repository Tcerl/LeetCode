# 04. Đồ Thị & Union-Find (Góc nhìn Senior)

> Lý thuyết nền: [`DSA_Giao_Trinh_Chi_Tiet.md`](../../../02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md) mục 10 (Graph), 19 (Union-Find).

---

## 1. Đồ thị — mô hình dữ liệu phổ biến nhất mà bạn không nhận ra mình đang dùng

Bất cứ khi nào dữ liệu có dạng "A liên quan tới B", đó là đồ thị:

| Hệ thống thật | Đồ thị biểu diễn gì |
|---|---|
| **Mạng xã hội** (Facebook, LinkedIn) | User = node, Follow/Friend = edge |
| **Microservices architecture** | Service = node, gọi API lẫn nhau = edge (có hướng) — dùng để phát hiện circular dependency |
| **Trình quản lý gói (npm, pip, Maven)** | Package = node, dependency = edge có hướng — **Topological Sort** quyết định thứ tự cài đặt |
| **Google Maps / GPS** | Giao lộ = node, đường = edge có trọng số (thời gian/khoảng cách) |
| **Compiler / Build system** (Webpack, Make, Bazel) | File/module = node, import/require = edge — phát hiện circular import, tính thứ tự build |
| **Database Foreign Key** | Bảng = node, FK constraint = edge — kiểm tra được thứ tự xóa/tạo bảng an toàn |
| **Kiểm duyệt giao dịch gian lận** | Tài khoản = node, giao dịch = edge — tìm cụm tài khoản liên kết bất thường (dùng chung Union-Find) |

### DFS vs BFS — chọn sai gây lãng phí tài nguyên thật

- **BFS:** tìm đường đi **ngắn nhất về số bước** (không trọng số) — dùng khi cần kết quả gần nhất nhanh nhất (gợi ý kết nối gần, lan truyền thông báo theo cấp).
- **DFS:** khám phá toàn bộ nhánh trước khi quay lại — dùng khi cần liệt kê **tất cả** đường đi/khả năng (giải mê cung, kiểm tra tồn tại đường đi, phát hiện chu trình).

```python
from collections import deque, defaultdict

def shortest_path_bfs(graph: dict, start: str, target: str) -> int:
    """
    Mô hình thật: 'X độ kết nối' trên LinkedIn (1st, 2nd, 3rd degree connection).
    BFS đảm bảo lần đầu chạm tới target chính là đường đi NGẮN NHẤT.
    """
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        if node == target:
            return dist
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1  # không kết nối được
```

### 🔥 Case thật: Topological Sort — vì sao `npm install` không bị treo vòng lặp vô hạn

```python
def topological_sort(num_packages: int, dependencies: list[tuple[int, int]]) -> list[int]:
    """
    dependencies[i] = (a, b) nghĩa là 'a phụ thuộc b' → phải cài b trước a.
    Đây CHÍNH XÁC là thuật toán npm/pip dùng để quyết định thứ tự cài package,
    và để PHÁT HIỆN circular dependency (A cần B, B cần A → lỗi, không thể cài).
    """
    graph = defaultdict(list)
    in_degree = [0] * num_packages
    for a, b in dependencies:
        graph[b].append(a)
        in_degree[a] += 1

    queue = deque([i for i in range(num_packages) if in_degree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != num_packages:
        raise ValueError("Circular dependency detected!")  # đúng lỗi npm/pip thật sự trả về
    return order
```

**Ứng dụng senior thực tế khác của Topological Sort:** thứ tự chạy migration database (migration B phụ thuộc migration A), thứ tự build các service trong CI/CD pipeline (monorepo), thứ tự tính toán các ô công thức trong spreadsheet engine (Excel/Google Sheets — ô C = A + B phải tính A, B trước).

### Dijkstra — thuật toán đứng sau mọi hệ thống định tuyến

Kết hợp Heap (Module 03) + Graph: luôn mở rộng node có tổng khoảng cách nhỏ nhất đã biết trước. Google Maps, network routing protocol (OSPF), và bài toán "chi phí thấp nhất để chuyển tiền qua nhiều sàn giao dịch" đều dùng biến thể của Dijkstra.

**Giới hạn quan trọng senior phải biết:** Dijkstra **không hoạt động đúng với trọng số âm** (VD: một số cạnh mang "phí thưởng" âm). Khi đó phải dùng **Bellman-Ford** (chậm hơn nhưng xử lý được trọng số âm và phát hiện chu trình âm — quan trọng trong hệ thống phát hiện arbitrage tài chính).

---

## 2. Union-Find (Disjoint Set Union) — công cụ "gom nhóm" hiệu quả nhất

Union-Find trả lời nhanh 2 câu hỏi: "A và B có cùng nhóm không?" và "gộp 2 nhóm lại" — cả hai gần như O(1) (chính xác là O(α(n)), gần như hằng số) nhờ **path compression** + **union by rank**.

### Ứng dụng thực tế

| Bài toán thật | Vì sao Union-Find phù hợp hơn BFS/DFS lặp lại |
|---|---|
| **Phát hiện gian lận:** gom nhóm tài khoản liên kết qua giao dịch chung | Xử lý hàng triệu giao dịch liên tục (streaming), Union-Find cập nhật O(α(n)) mỗi lần thay vì chạy lại BFS toàn đồ thị |
| **Network connectivity monitoring:** kiểm tra 2 server có nằm cùng cụm mạng không sau khi 1 link đứt | Union-Find động, không cần build lại toàn bộ đồ thị mỗi lần |
| **Kruskal's Algorithm (Minimum Spanning Tree):** thiết kế mạng cáp quang/điện với chi phí thấp nhất kết nối toàn bộ node | Union-Find dùng để kiểm tra "thêm cạnh này có tạo chu trình không" trong O(α(n)) |
| **Redis Cluster / distributed system:** kiểm tra các node có "nhìn thấy nhau" (cùng partition) sau lỗi mạng (network partition/split-brain) | Mô hình tư duy giống Union-Find dù cài đặt thật phức tạp hơn (gossip protocol) |

```python
class UnionFind:
    """
    Dùng thật trong: hệ thống phát hiện gian lận ngân hàng, kiểm tra kết nối mạng,
    và thuật toán Kruskal cho bài toán thiết kế hạ tầng chi phí thấp nhất.
    """
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  # đã cùng nhóm — thêm cạnh này sẽ tạo chu trình
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True
```

---

## 🎯 Câu hỏi senior hay hỏi khi review kiến trúc

1. "Sơ đồ dependency giữa các microservices của bạn có chu trình không? Nếu service A gọi B, B gọi C, C gọi lại A — hệ thống có thể deadlock khi nào?"
2. "Bạn chọn BFS hay DFS cho bài toán này — và tại sao lựa chọn đó ảnh hưởng tới độ trễ phản hồi thực tế?"
3. "Nếu cạnh có trọng số âm (chiết khấu, hoàn tiền), Dijkstra của bạn còn đúng không?"

## 🔗 Liên kết module khác
- Heap là thành phần bắt buộc của Dijkstra → [`03-Trees-Heaps-Tries`](../03-Trees-Heaps-Tries/README.md)
- DFS trên đồ thị chính là nền tảng của Backtracking → [`06-Advanced-Patterns`](../06-Advanced-Patterns/README.md)
- Kiến trúc microservices/dependency thực tế sẽ khai triển sâu hơn ở nhóm `Cloud & DevOps` (đợt kế tiếp).
