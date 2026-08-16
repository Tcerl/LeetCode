# 08. Lộ Trình Vấn Đề Thật: Từ Junior Đến Senior (DSA & Cấu Trúc Dữ Liệu)

> File này tổng hợp lại **theo cấp độ** các vấn đề đã nhắc rải rác ở Module 01-07 — giúp bạn tự định vị mình đang ở đâu và biết bước tiếp theo cần học gì. Mỗi dòng đều trỏ lại module chi tiết tương ứng.

---

## 🟢 Cấp độ Junior — "Code chạy đúng, nhưng chưa biết tại sao lại chậm/vỡ"

| Vấn đề gặp phải | Vì sao xảy ra | Cách vượt qua | Đọc thêm |
|---|---|---|---|
| Code pass test với dữ liệu nhỏ, timeout với dữ liệu lớn | Chưa có thói quen phân tích Big O trước khi code, chỉ code theo bản năng | Trước khi code, tự hỏi "n lớn nhất có thể là bao nhiêu, thuật toán này O(?)" | [`01-Foundations`](../01-Foundations/README.md) |
| `RecursionError: maximum recursion depth exceeded` khi xử lý dữ liệu người dùng nhập | Không kiểm soát độ sâu đệ quy, không nghĩ tới input độc hại/bất thường | Luôn hỏi "input này có thể sâu tới đâu?" — chuyển sang lặp nếu không kiểm soát được | [`01-Foundations`](../01-Foundations/README.md) |
| Dùng `list.pop(0)` để làm hàng đợi, không hiểu vì sao chậm dần khi queue lớn | Chưa phân biệt được độ phức tạp của từng thao tác trên từng cấu trúc dữ liệu | Học "bảng độ phức tạp thao tác" của Array/LinkedList/Deque thuộc lòng | [`02-Linear-Structures-And-Hashing`](../02-Linear-Structures-And-Hashing/README.md) |
| Không biết khi nào dùng Set/Dict thay vì List để tăng tốc | Chưa quen phản xạ "tìm kiếm lặp lại → nghĩ ngay tới Hash Table" | Luyện tập nhận diện: thấy `if x in list` trong vòng lặp → cảnh giác ngay | [`02-Linear-Structures-And-Hashing`](../02-Linear-Structures-And-Hashing/README.md) |

**Bài học junior cần khắc cốt ghi tâm:** *"Code chạy được" và "Code đúng" là 2 khái niệm khác nhau.* Code đúng còn phải đúng ở quy mô dữ liệu thật, không chỉ ở bộ test mẫu.

---

## 🟡 Cấp độ Mid-level — "Biết cấu trúc dữ liệu, nhưng chọn sai biến thể hoặc dùng sai ngữ cảnh"

| Vấn đề gặp phải | Vì sao xảy ra | Cách vượt qua | Đọc thêm |
|---|---|---|---|
| Tự cài BST thuần cho dữ liệu sắp xếp sẵn → cây lệch hẳn về 1 phía, thao tác O(n) thay vì O(log n) | Biết BST là gì nhưng chưa hiểu vấn đề mất cân bằng | Học vì sao production luôn dùng biến thể cân bằng (B-Tree/RB-Tree) | [`03-Trees-Heaps-Tries`](../03-Trees-Heaps-Tries/README.md) |
| Dùng Heap để "tìm phần tử X trong danh sách" | Nhầm lẫn heap đảm bảo thứ tự TOÀN BỘ, trong khi nó chỉ đảm bảo phần tử gốc | Nhớ rõ: Heap chỉ trả lời "cái nhỏ/lớn nhất là gì", không trả lời "X có trong đó không" | [`03-Trees-Heaps-Tries`](../03-Trees-Heaps-Tries/README.md) |
| Chọn BFS cho bài toán cần liệt kê TẤT CẢ đường đi, code chạy đúng nhưng logic rối, khó maintain | Chưa phân biệt rõ khi nào dùng BFS (đường ngắn nhất) và DFS (khám phá toàn bộ nhánh) | Luyện phản xạ: "cần đường NGẮN NHẤT" → BFS; "cần TẤT CẢ khả năng" → DFS/Backtracking | [`04-Graphs-And-Union-Find`](../04-Graphs-And-Union-Find/README.md), [`06-Advanced-Patterns`](../06-Advanced-Patterns/README.md) |
| Dùng Greedy cho bài toán chưa chứng minh được tính đúng đắn, ra kết quả sai ở 1 số test case hiếm | Nhầm "trông có vẻ đúng" với "chứng minh được đúng" | Luôn tự hỏi "mình có phản chứng được Greedy này không?" trước khi tự tin dùng, nếu không chắc thì dùng DP an toàn hơn | [`06-Advanced-Patterns`](../06-Advanced-Patterns/README.md) |

**Bài học mid-level cần khắc cốt ghi tâm:** *"Biết tên cấu trúc dữ liệu" khác với "biết khi nào KHÔNG nên dùng nó."* Đây là giai đoạn học cách nhận diện đúng bối cảnh, không chỉ học thuộc cách cài đặt.

---

## 🔴 Cấp độ Senior — "Không tự tay cài đặt nữa, mà quyết định KIẾN TRÚC dùng gì và tại sao"

| Vấn đề gặp phải (ở tầm hệ thống) | Senior xử lý thế nào | Đọc thêm |
|---|---|---|
| Team junior đề xuất cài custom cache tự viết (không giới hạn kích thước) | Review PR, chỉ ra rủi ro memory leak, hướng dẫn dùng LRU Cache đúng chuẩn (`OrderedDict`/Redis) | [`02`](../02-Linear-Structures-And-Hashing/README.md) |
| Hệ thống cần chọn giữa "sort lại toàn bộ mỗi lần" và "duy trì cấu trúc luôn sắp xếp" khi dữ liệu cập nhật liên tục | Nhận diện đây là bài toán Heap/Top-K, đưa ra quyết định kiến trúc thay vì để junior tự mò | [`03`](../03-Trees-Heaps-Tries/README.md) |
| Circular dependency giữa các microservices gây deadlock khó chẩn đoán | Dùng tư duy Topological Sort để thiết kế lại ranh giới service, không chỉ fix triệu chứng | [`04`](../04-Graphs-And-Union-Find/README.md) |
| Junior/mid nộp code đúng nhưng chưa tối ưu (như case `median_two_sorted_array.py` đã review ở Module 07) | Review không chỉ "đúng/sai" mà đặt câu hỏi "còn tối ưu được không, có đáng đánh đổi thời gian không ở giai đoạn này" | [`07-Practice-Lab`](../07-Practice-Lab/README.md) |
| Toàn đội chỉ quen thuộc thuật toán nhưng không liên hệ được với hệ thống thật khi phỏng vấn/thiết kế | Chủ động dạy lại: mỗi cấu trúc dữ liệu tương ứng hệ thống thật nào (đã tổng hợp toàn bộ ở Module 01-06) | Dùng chính tài liệu này làm buổi chia sẻ nội bộ team |

**Bài học senior cần khắc cốt ghi tâm:** *Senior không được đánh giá bằng việc "code thuật toán nhanh nhất phòng" mà bằng khả năng nhìn ra bài toán thật đằng sau 1 yêu cầu nghiệp vụ, chọn đúng cấu trúc dữ liệu/thuật toán, và giải thích được tradeoff cho cả team lẫn stakeholder không chuyên.*

---

## 🗺️ Lộ trình tổng hợp để tự đánh giá bản thân đang ở đâu

```
Junior  → Giải được bài LeetCode Easy/Medium, pass test, CHƯA chắc về Big O thật
            │ (dấu hiệu sẵn sàng lên Mid: tự phân tích được complexity TRƯỚC khi code)
            ▼
Mid     → Chọn đúng cấu trúc dữ liệu cho từng bài, hiểu tradeoff cơ bản
            │ (dấu hiệu sẵn sàng lên Senior: tự liên hệ được bài toán với hệ thống thật,
            │  review code người khác phát hiện được lỗi chọn sai cấu trúc dữ liệu)
            ▼
Senior  → Quyết định kiến trúc dùng cấu trúc dữ liệu/thuật toán nào ở tầm hệ thống,
          dạy lại được người khác, giải thích tradeoff cho người không chuyên
```

## 🔗 Liên kết
Toàn bộ chi tiết kỹ thuật: [`01`](../01-Foundations/README.md) · [`02`](../02-Linear-Structures-And-Hashing/README.md) · [`03`](../03-Trees-Heaps-Tries/README.md) · [`04`](../04-Graphs-And-Union-Find/README.md) · [`05`](../05-Sorting-And-Searching/README.md) · [`06`](../06-Advanced-Patterns/README.md) · [`07`](../07-Practice-Lab/README.md)
Áp dụng vào trả lời phỏng vấn: [`../Career-Mastery/02`](../../Career-Mastery/02-System-Design-Interview-Playbook/README.md)
