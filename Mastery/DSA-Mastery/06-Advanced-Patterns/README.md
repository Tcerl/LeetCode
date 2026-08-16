# 06. Pattern Nâng Cao (Góc nhìn Senior)

> Lý thuyết nền: [`DSA_Giao_Trinh_Chi_Tiet.md`](../../../02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md) mục 14 (Sliding Window), 15 (Two Pointers), 16 (DP), 17 (Greedy), 18 (Backtracking), 20 (Bit Manipulation).

---

## 1. Sliding Window & Two Pointers — kỹ thuật xử lý stream dữ liệu thật

Đây là 2 pattern **dùng trực tiếp hàng ngày** trong xử lý dữ liệu luồng (streaming) và tối ưu bộ nhớ:

| Ứng dụng thực tế | Pattern áp dụng |
|---|---|
| **Network throttling / TCP congestion control** | Sliding window đúng nghĩa đen — TCP dùng "window size" để kiểm soát bao nhiêu packet gửi đi trước khi cần ACK |
| **Giám sát hệ thống (metrics/monitoring):** "CPU trung bình 5 phút gần nhất" | Sliding window trên time-series data, không cần lưu lại toàn bộ lịch sử |
| **Phát hiện gian lận real-time:** "user có quá 5 giao dịch trong 1 phút không?" | Sliding window trên timestamp (giống RateLimiter ở Module 02) |
| **Xử lý file lớn không load hết vào RAM** | Two pointers đọc theo khối (chunk), xử lý tuần tự |

```python
def longest_substring_without_repeat(s: str) -> int:
    """
    Pattern này áp dụng thẳng vào bài toán thật: 'phiên làm việc dài nhất mà
    user không lặp lại hành động nào' trong phân tích hành vi người dùng (analytics).
    """
    seen = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

**Vì sao senior thích pattern này:** chuyển bài toán từ O(n²) (2 vòng lặp lồng) xuống O(n) bằng cách **không tính lại từ đầu** mỗi lần dịch chuyển cửa sổ — chỉ cộng/trừ phần thay đổi. Đây là tư duy "incremental computation" áp dụng khắp nơi trong hệ thống thật (cache invalidation, streaming aggregation trong Kafka Streams/Flink).

---

## 2. Dynamic Programming — không phải "học thuộc công thức", mà là tư duy tối ưu hóa quyết định

DP giải bài toán: "quyết định ở bước hiện tại phụ thuộc vào kết quả tối ưu của các bước trước". Đây là mô hình xuất hiện trong:

| Hệ thống thật | DP giải quyết gì |
|---|---|
| **Trình so sánh diff** (Git diff, `diff` command) | Longest Common Subsequence — tìm phần thay đổi tối thiểu giữa 2 phiên bản file |
| **Spell checker/Autocorrect** | Edit Distance (Levenshtein) — tính "gần đúng" giữa từ gõ sai và từ đúng |
| **Compiler optimization** | Dynamic programming trong register allocation, instruction scheduling |
| **Tài chính:** tối ưu danh mục đầu tư với ngân sách giới hạn | 0/1 Knapsack — chọn tập tài sản tối đa lợi nhuận trong ngân sách |
| **Định tuyến mạng CDN** | Chọn đường truyền tối ưu chi phí qua nhiều chặng (tương tự DP trên đồ thị) |

```python
def edit_distance(word1: str, word2: str) -> int:
    """
    Đây CHÍNH LÀ thuật toán đứng sau gợi ý 'Bạn có phải muốn tìm...' của
    Google Search, và đứng sau `git diff --word-diff`.
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]
```

### Cách senior tiếp cận DP khi phỏng vấn/thiết kế thật (không học thuộc)

1. Định nghĩa **trạng thái** (state): "dp[i] đại diện cho cái gì?"
2. Tìm **công thức chuyển trạng thái** (transition): "dp[i] liên hệ thế nào với dp[i-1], dp[i-2]...?"
3. Xác định **trạng thái cơ sở** (base case).
4. Tối ưu bộ nhớ: hầu hết DP 2D có thể giảm xuống 1D (rolling array) khi `dp[i]` chỉ phụ thuộc `dp[i-1]` — quan trọng khi n lớn và bộ nhớ hạn chế trên production.

---

## 3. Greedy — nhanh, nhưng phải chứng minh được mới dám dùng trên production

Greedy chọn lựa tối ưu cục bộ ở mỗi bước, hy vọng ra tối ưu toàn cục — **không phải lúc nào cũng đúng**, đây là điểm khác biệt lớn nhất so với DP mà senior phải phân biệt được.

| Hệ thống thật | Vì sao Greedy đúng ở đây |
|---|---|
| **Huffman Coding** (nén file ZIP, JPEG) | Luôn ghép 2 node tần suất thấp nhất — chứng minh được tối ưu toàn cục |
| **Task scheduling đơn giản** (chọn tối đa số cuộc họp không trùng giờ) | Sắp theo thời gian kết thúc sớm nhất — kinh điển trong lập lịch phòng họp |
| **Dijkstra** (Module 04) | Về bản chất là Greedy + Heap, đúng vì trọng số không âm |

**Bẫy thực tế:** bài toán "đổi tiền tối thiểu số tờ" chỉ đúng với Greedy khi hệ mệnh giá là "canonical" (như tiền VNĐ: 500k, 200k, 100k...). Với mệnh giá tùy ý (VD: [1, 3, 4] để đổi 6), Greedy cho kết quả sai (chọn 4+1+1=3 tờ) trong khi DP cho đáp án đúng (3+3=2 tờ). **Đây là lý do senior luôn tự hỏi "Greedy có chứng minh được không, hay phải dùng DP an toàn hơn?"** trước khi đưa vào hệ thống tính tiền thật.

---

## 4. Backtracking — sinh mọi khả năng có kiểm soát (pruning)

Ứng dụng thực tế: **trình giải Sudoku, tạo lịch thi đấu tự động, cấu hình mạng (network configuration solver), trình biên dịch regex engine** (thử các nhánh match rồi quay lui khi thất bại).

```python
def generate_valid_combinations(open_slots: int) -> list[str]:
    """
    Mô hình rút gọn của: 'sinh tất cả cấu hình hợp lệ thỏa ràng buộc' —
    dùng trong trình sinh test case tự động (property-based testing) và
    trình giải constraint (CSP solver).
    """
    result = []
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * open_slots:
            result.append(current)
            return
        if open_count < open_slots:
            backtrack(current + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    backtrack("", 0, 0)
    return result
```

**Kỹ năng senior quan trọng nhất ở Backtracking:** cắt tỉa (pruning) sớm — kiểm tra điều kiện bất khả thi trước khi đệ quy tiếp, tránh khám phá cả nhánh vô nghĩa. Đây trực tiếp quyết định hệ thống chạy trong 10ms hay treo 10 giây.

---

## 5. Bit Manipulation — tối ưu tầng thấp, dùng trong hệ thống hiệu năng cao

| Ứng dụng thực tế | Kỹ thuật bit |
|---|---|
| **Feature flags** (bật/tắt tính năng cho từng user) | Mỗi bit đại diện 1 flag, dùng `&`, `\|`, `^` để kiểm tra/set — tiết kiệm bộ nhớ khi có hàng trăm flag |
| **Bitmap index trong DB** (PostgreSQL Bitmap Scan) | Kết hợp nhiều điều kiện WHERE bằng phép AND/OR trên bitmap — nhanh hơn quét tuần tự |
| **Bloom Filter** (kiểm tra "phần tử CÓ THỂ tồn tại" với xác suất sai thấp) | Dùng trong CDN/cache để tránh query DB không cần thiết (Chrome dùng Bloom Filter để check URL độc hại) |
| **Permission system** (RBAC đơn giản) | Mỗi quyền là 1 bit trong 1 số nguyên, kiểm tra quyền bằng `permission & FLAG` |

```python
class FeatureFlags:
    """Dùng thật trong hệ thống A/B testing và feature rollout (LaunchDarkly-style)."""
    DARK_MODE = 1 << 0
    NEW_CHECKOUT = 1 << 1
    BETA_SEARCH = 1 << 2

    def __init__(self):
        self.flags = 0

    def enable(self, flag: int) -> None:
        self.flags |= flag

    def is_enabled(self, flag: int) -> bool:
        return bool(self.flags & flag)
```

---

## 🎯 Câu hỏi senior hay hỏi khi review thiết kế

1. "Bạn dùng Greedy ở đây — có chứng minh được đây là bài toán mà lựa chọn cục bộ luôn dẫn tới tối ưu toàn cục không?"
2. "DP này có thể giảm từ O(n²) bộ nhớ xuống O(n) hay O(1) bằng rolling array không?"
3. "Backtracking này có pruning đủ mạnh chưa, hay đang khám phá cả nhánh chắc chắn thất bại?"

## 🔗 Liên kết module khác
- Memoization trong DP kế thừa từ đệ quy → [`01-Foundations`](../01-Foundations/README.md)
- Backtracking là DFS có kiểm soát trên cây quyết định → [`03-Trees-Heaps-Tries`](../03-Trees-Heaps-Tries/README.md), [`04-Graphs-And-Union-Find`](../04-Graphs-And-Union-Find/README.md)
