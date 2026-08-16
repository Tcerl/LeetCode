# 07. Practice Lab — Review Code Thật Trong Repo & Lộ Trình Luyện Tập

> Nguồn tham khảo gốc: [`02-DSA-Curriculum/DSA_Lo_Trinh_On_Luyen_4_Tram.md`](../../02-DSA-Curriculum/DSA_Lo_Trinh_On_Luyen_4_Tram.md), [`DSA_Giao_Trinh_Chi_Tiet.md`](../../02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md) mục 21-25, và code thực hành tại [`06-Exercises/20_exam_exercies/`](../../06-Exercises/20_exam_exercies/).

Phần này review **code bạn đã tự viết** trong `20_exam_exercies/` bằng con mắt senior — không chỉ "đúng/sai" mà "sẽ ra sao nếu chạy trên production".

---

## 1. Code Review từng file trong `20_exam_exercies/`

### `two_sums.py` — ✅ Đã đúng chuẩn senior

Cách bạn viết dùng Hash Map O(n) — đúng pattern chuẩn (Module 02). Điểm senior sẽ hỏi thêm khi review PR thật: *"Nếu mảng có nhiều cặp thỏa mãn, hàm này trả về cặp đầu tiên tìm thấy — business logic có yêu cầu trả về TẤT CẢ các cặp không?"* → cần làm rõ requirement trước khi code, không tự suy diễn.

### `longest_string.py` — ✅ Đúng pattern Sliding Window (Module 06)

Đúng kỹ thuật. Điểm cải thiện: nên viết docstring + type hint đầy đủ như `two_sums.py` để nhất quán — trong code review thật, tính nhất quán style quan trọng không kém tính đúng.

### `container_water.py` — ✅ Đúng pattern Two Pointers

Lưu ý nhỏ: định nghĩa `def max_area(heights: list[int])` thiếu `self` nhưng nằm trong `class Solution` — gọi qua `Solution` (không tạo instance) nên chạy được, nhưng đây là **code smell**: nếu class không cần state, nên dùng `@staticmethod` để tường minh ý đồ, tránh gây nhầm lẫn cho người đọc code sau này (chính là bạn 6 tháng sau).

```python
# Senior sẽ sửa thành:
class Solution:
    @staticmethod
    def max_area(heights: list[int]) -> int:
        ...
```

### `median_two_sorted_array.py` — ⚠️ Đúng nhưng chưa tối ưu

Cách bạn viết merge 2 mảng rồi lấy median là **O(m+n)** — đúng và dễ hiểu, nhưng đề bài LeetCode #4 yêu cầu **O(log(m+n))** bằng binary search (Module 05, "Binary Search on Answer" biến thể). Đây là **bài học senior quan trọng nhất**: code chạy đúng (pass test) chưa chắc đạt yêu cầu phi chức năng (complexity). Trong phỏng vấn thật ở công ty lớn, nộp lời giải O(m+n) cho bài này thường bị hỏi tiếp "làm được O(log n) không?" — vì đây chính là câu hỏi được thiết kế để phân biệt ứng viên.

### `add_two_number.py` — ✅ Đúng, xử lý linked list + carry chuẩn

Đây là bài áp dụng thẳng Module 02 (Linked List) — logic cộng có nhớ (carry) giống hệt cách CPU cộng số nhị phân ở tầng phần cứng (full adder). Điểm mở rộng thực tế: nếu 2 số cực lớn (crypto, big number arithmetic), đây chính xác là kỹ thuật dùng trong thư viện `bignum`.

### `calculator.py` — ⚠️ Có bug thật + thiếu xử lý lỗi (không phải bài DSA nhưng đáng review)

Bug: hàm `history()` không phải constructor nhưng lại khởi tạo `self._history = []` — nếu gọi `add()` trước khi gọi `history()`, code sẽ **crash với AttributeError**. Đây là lỗi thiết kế class thật rất hay gặp ở junior. Sửa chuẩn senior:

```python
class Calculator:
    def __init__(self):
        self._history = []

    def divide(self, a, b):  # cũng sửa luôn lỗi chính tả "devide"
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")  # xử lý lỗi tường minh, không để crash ngầm
        result = a / b
        self._history.append(f"{a} / {b} = {result}")
        return result
```

**Bài học senior:** đây chính là lý do các team lớn bắt buộc code review + unit test trước khi merge — bug "gọi sai thứ tự method là crash" rất dễ lọt qua nếu chỉ tự test happy path.

### `todolist.py` — ⚠️ Thiếu xử lý lỗi khi ghi file (I/O)

`save_tasks()` ghi thẳng vào file, nếu chương trình bị kill giữa lúc ghi (mất điện, container bị restart) → **file JSON bị hỏng (corrupt), mất toàn bộ dữ liệu cũ**. Đây là vấn đề có thật trong hệ thống production. Giải pháp senior dùng — **atomic write** (ghi ra file tạm rồi rename, rename là thao tác atomic ở cấp hệ điều hành):

```python
import json, os, tempfile

def save_tasks(self):
    dir_name = os.path.dirname(os.path.abspath(self.filename)) or "."
    fd, tmp_path = tempfile.mkstemp(dir=dir_name)
    with os.fdopen(fd, "w") as f:
        json.dump(self.tasks, f, indent=4)
    os.replace(tmp_path, self.filename)  # atomic trên hầu hết hệ điều hành
```

### `learn.py` — ghi chú kiến thức `*args`/`**kwargs`

Đây là kiến thức nền tảng đúng, ứng dụng thực tế: mọi decorator generic (`@lru_cache`, middleware trong Flask/Django, `*args, **kwargs` trong hàm wrapper) đều dựa trên cơ chế này để "chuyển tiếp" tham số mà không cần biết trước signature.

---

## 2. Lộ trình luyện tập — không lặp lại, chỉ dẫn hướng dùng

- **Roadmap chi tiết theo tuần:** xem [`DSA_Giao_Trinh_Chi_Tiet.md`](../../02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md#-lộ-trình-thực-hành-tổng-hợp) và [`DSA_Lo_Trinh_On_Luyen_4_Tram.md`](../../02-DSA-Curriculum/DSA_Lo_Trinh_On_Luyen_4_Tram.md) — 4 trạm thực chiến theo pattern.
- **Pattern Recognition Guide** (cách nhìn đề bài đoán ngay kỹ thuật cần dùng): [`DSA_Giao_Trinh_Chi_Tiet.md` mục 21](../../02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md#21-pattern-recognition-guide).
- **NeetCode 75 (list bài chọn lọc):** [`DSA_Giao_Trinh_Chi_Tiet.md` mục 22](../../02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md#22-neetcode-75-curated-list).

### 🧭 Cách senior luyện tập khác junior thế nào

1. **Sau khi giải xong 1 bài, luôn tự hỏi: "Bài này là mô hình thu nhỏ của hệ thống thật nào?"** (VD: Two Sum → dedup detection; LRU → cache eviction). Đây là kỹ năng biến bài tập thành trực giác thiết kế hệ thống — chính là nội dung các Module 01-06 vừa trình bày.
2. **Review lại complexity SAU KHI đã pass**, không chỉ dừng ở "test xanh hết". Câu hỏi luôn là: "còn cách nào giảm thêm 1 bậc complexity không?" (giống case `median_two_sorted_array.py` ở trên).
3. **Viết test case biên (edge case) trước khi cho là xong:** mảng rỗng, 1 phần tử, input cực lớn, input trùng lặp toàn bộ, input đã sort ngược. Đây là thói quen bắt buộc trước khi merge code thật vào production.

---

## 3. Ghi chú về các file khác trong `06-Exercises/`

Thư mục `06-Exercises/` hiện đang **trộn lẫn nhiều chủ đề** không thuần DSA:
- `CODE_EXERCISES.md`, `theory_mastery.md` → nội dung Vue.js/Laravel/Fullstack — sẽ được tổ chức vào cây kiến thức **Frontend/Backend** ở đợt cập nhật tiếp theo (không thuộc phạm vi DSA).
- `MATLAB/` → thuộc mảng tính toán khoa học, sẽ được xem xét gộp vào nhóm phù hợp khi làm tới đó, hoặc giữ độc lập nếu không liên quan tới các nhóm còn lại.

*(Theo đúng yêu cầu: nội dung liên quan sẽ được gộp vào folder chung phù hợp khi xử lý tới nhóm chủ đề tương ứng, không tạo trùng lặp ngay từ bây giờ.)*

## 🔗 Liên kết module khác
Toàn bộ nền tảng lý thuyết cho các pattern nhắc ở trên: [`01`](../01-Foundations/README.md) · [`02`](../02-Linear-Structures-And-Hashing/README.md) · [`03`](../03-Trees-Heaps-Tries/README.md) · [`04`](../04-Graphs-And-Union-Find/README.md) · [`05`](../05-Sorting-And-Searching/README.md) · [`06`](../06-Advanced-Patterns/README.md)
