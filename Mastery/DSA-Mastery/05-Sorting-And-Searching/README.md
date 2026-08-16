# 05. Sắp Xếp & Tìm Kiếm (Góc nhìn Senior)

> Lý thuyết nền: [`DSA_Giao_Trinh_Chi_Tiet.md`](../../../02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md) mục 12 (Sorting), 13 (Binary Search).

---

## 1. Sorting — bạn hiếm khi tự viết, nhưng phải biết cái nào đang chạy dưới hood

Senior dev gần như **không bao giờ tự cài quicksort/mergesort trong production** — luôn dùng hàm built-in (`sorted()`, `Array.sort()`, `ORDER BY`). Nhưng **phải hiểu** thuật toán nào đang chạy bên dưới để dự đoán hiệu năng và tránh bẫy.

| Thuật toán | Ai đang dùng nó thật | Vì sao được chọn |
|---|---|---|
| **Timsort** | Python `sorted()`/`list.sort()`, Java `Arrays.sort()` cho object | Hybrid Merge Sort + Insertion Sort, tận dụng các đoạn đã sắp xếp sẵn trong dữ liệu thật (real-world data hiếm khi random hoàn toàn) — best case O(n) |
| **Introsort** | C++ `std::sort`, .NET | Hybrid Quicksort + Heapsort, tránh worst-case O(n²) của quicksort thuần |
| **External Merge Sort** | Sắp xếp file/bảng DB lớn hơn RAM (`ORDER BY` trên bảng hàng chục GB) | Merge Sort chia nhỏ ra đĩa, xử lý từng phần rồi merge — không thể load hết vào RAM |
| **Radix/Counting Sort** | Sắp xếp số nguyên trong khoảng giới hạn (VD: sort điểm số 0-100 của hàng triệu học sinh) | O(n) khi biết trước phạm vi giá trị — nhanh hơn hẳn O(n log n) tổng quát |

### 🔥 Case thật: `ORDER BY` chậm bất thường — vì sao?

```sql
-- Nếu cột không có index: DB phải load toàn bộ dữ liệu vào bộ nhớ/đĩa tạm rồi sort (filesort)
SELECT * FROM orders ORDER BY created_at DESC LIMIT 20;
```

Nếu bảng có index B-Tree trên `created_at`, DB **không cần sort** — chỉ cần duyệt index theo đúng thứ tự đã lưu sẵn (liên kết Module 03: B-Tree luôn giữ thứ tự). Đây là lý do senior luôn kiểm tra `EXPLAIN` để xem query có bị "Using filesort" không — dấu hiệu thiếu index cho cột `ORDER BY`.

### ⚠️ Pitfall thực tế: So sánh không ổn định (unstable sort) làm vỡ UI

Khi sort danh sách sản phẩm theo "giá", nếu 2 sản phẩm giá bằng nhau mà thuật toán không ổn định (unstable), thứ tự tương đối giữa chúng có thể đảo lộn ngẫu nhiên mỗi lần load lại trang → trải nghiệm người dùng khó chịu ("sao list cứ nhảy lung tung"). Senior luôn chọn **stable sort** (Timsort là stable) khi có yêu cầu giữ thứ tự phụ (secondary order), hoặc thêm tiêu chí phụ rõ ràng (VD: `ORDER BY price, id`).

```python
# Sort đa tiêu chí — pattern dùng thật trong mọi hệ thống filter/sort sản phẩm
products = [
    {"name": "A", "price": 100, "rating": 4.5},
    {"name": "B", "price": 100, "rating": 4.8},
]
# Sắp theo giá tăng dần, nếu bằng giá thì rating giảm dần
products.sort(key=lambda p: (p["price"], -p["rating"]))
```

---

## 2. Binary Search — không chỉ tìm số trong mảng đã sort

### Ứng dụng thực tế vượt xa "tìm số trong mảng"

- **Git bisect:** tìm commit nào gây ra bug bằng cách nhị phân qua lịch sử commit — chính xác là binary search trên "trục thời gian đã sắp xếp".
- **Rate limiter/Load testing:** tìm ngưỡng tải tối đa hệ thống chịu được trước khi crash (binary search trên số lượng request/giây).
- **Database:** B-Tree index về bản chất thực hiện tìm kiếm theo tư duy binary search (chia nhánh) chỉ với độ phân nhánh (fan-out) lớn hơn 2.
- **"Binary Search on Answer"** — kỹ thuật senior hay dùng để tối ưu bài toán tối ưu hóa: thay vì tính trực tiếp đáp án, đoán đáp án rồi kiểm tra "đáp án X có khả thi không", thu hẹp phạm vi bằng binary search.

```python
def min_capacity_to_ship(weights: list[int], days: int) -> int:
    """
    Bài toán thật: 'Kho cần thuê xe tải trọng tải tối thiểu bao nhiêu để giao hết
    hàng trong N ngày?' — pattern Binary Search on Answer áp dụng thẳng vào
    bài toán vận hành logistics thật (capacity planning).
    """
    def can_ship_within_days(capacity: int) -> bool:
        days_needed, current_load = 1, 0
        for w in weights:
            if current_load + w > capacity:
                days_needed += 1
                current_load = 0
            current_load += w
        return days_needed <= days

    low, high = max(weights), sum(weights)
    while low < high:
        mid = (low + high) // 2
        if can_ship_within_days(mid):
            high = mid
        else:
            low = mid + 1
    return low
```

### ⚠️ Pitfall kinh điển: Integer Overflow khi tính `mid`

```python
# ❌ Ở ngôn ngữ có kiểu int giới hạn (Java, C++): left + right có thể tràn số
mid = (left + right) // 2

# ✅ An toàn tuyệt đối, thói quen senior dù Python không bị overflow
mid = left + (right - left) // 2
```

Python không có vấn đề này (int không giới hạn), nhưng **đây là kiến thức bắt buộc** khi làm việc với Java/C++/Go trong hệ thống thật — bug tràn số từng gây lỗi nổi tiếng trong `Arrays.binarySearch` của Java (bug có thật, được fix năm 2006).

---

## 🎯 Câu hỏi senior hay hỏi khi review

1. "Query `ORDER BY` này có dùng index không, hay đang filesort trên hàng triệu dòng?"
2. "Sort này có ổn định (stable) không? Nếu 2 phần tử bằng nhau, thứ tự UI có nhất quán giữa các lần load không?"
3. "Thay vì tính trực tiếp, bài toán này có thể chuyển thành 'binary search trên đáp án' để giảm từ O(n²) xuống O(n log n) không?"

## 🔗 Liên kết module khác
- Binary Search là nền tảng cho nhiều pattern tối ưu → [`06-Advanced-Patterns`](../06-Advanced-Patterns/README.md)
- B-Tree index (ứng dụng Binary Search ở tầng DB) sẽ khai triển sâu ở nhóm `Backend: Database & Python` (đợt kế tiếp).
