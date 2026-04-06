# 🚀 GIÁO TRÌNH ÔN LUYỆN DSA ĐỈNH CAO: MÔ HÌNH 4 TRẠM THỰC CHIẾN

> **Mục tiêu:** Nâng cấp tư duy thuật toán từ mức độ giải bài tập (Junior/Mid) lên kiến trúc phân tích, phản biện mã nguồn và thiết kế hệ thống nền tảng (Senior).
> **Cách sử dụng:** Đối với mỗi chủ đề, hãy tự suy nghĩ nháp ra giấy trước. Sau đó, bạn có thể copy yêu cầu của từng trạm và gửi cho mình (AI) để mình kiểm tra, review đáp án hoặc đóng vai trò người phỏng vấn.

---

## 📌 CHỦ ĐỀ 1: MẢNG (ARRAY) & HAI CON TRỎ / CỬA SỔ TRƯỢT
**Trạm 1 (Code Review):** Đoạn code Python xóa phần tử trùng lặp trong mảng đã sắp xếp: `for i in nums: while nums.count(i)>1: nums.remove(i)`. Tại sao đoạn code này lại là thảm họa hiệu năng $O(N^2)$? Hãy viết lại nó đạt mốc $O(N)$ Time và $O(1)$ Space.
**Trạm 2 (Problem Solving):** Subarray Sum Equals K. Hãy viết thuật toán Prefix Sum kết hợp Hash Map để tìm số lượng mảng con liên tiếp có tổng bằng `K` trong danh sách có số âm. Tại sao Sliding Window thông thường lại thất bại ở bài toán này?
**Trạm 3 (Deep Dive):** Giải phẫu `Dynamic Array` (`list` trong Python, `ArrayList` trong Java/C++). Nó thu xếp bộ nhớ dưới nền gốc RAM như thế nào? "Amortized $O(1)$ Time" (thời gian O(1) khấu hao) khi append/thêm dữ liệu nghĩa là sao?
**Trạm 4 (Mock Interview):** Bạn cần xây dựng bộ API xử lý dữ liệu biểu đồ nến (Stock Candlestick). Làm sao để truy vấn "Giá lớn nhất trong 3 ngày liên tiếp bất kì trong 10 năm qua" với độ phức tạp $O(N)$ thời gian? (Hint: Sliding Window Maximum).

---

## 📌 CHỦ ĐỀ 2: BẢNG BĂM (HASH TABLE)
**Trạm 1 (Code Review):** Junior dev viết code kiểm tra Anagram bằng cách: `return sorted(s) == sorted(t)`. Điều này chạy hết $O(N \log N)$. Bạn hãy tái cấu trúc thành $O(N)$ sử dụng mảng phụ hoặc Hash Table.
**Trạm 2 (Problem Solving):** (Biến thể Two Sum) Cho mảng số và `Target`. Hãy trả ra **tất cả các cặp giá trị** phân biệt (không bị trùng bộ số) có tổng bằng Target.
**Trạm 3 (Deep Dive):** "Đụng độ băm" (Hash Collision) là nỗi ám ảnh. Chuyện gì xảy ra ở mức bộ nhớ khi 2 keys khác nhau đẻ ra cùng 1 Hash Code? Phân tích ưu nhược điểm giữa *Separate Chaining (Danh sách liên kết nối đuôi)* và *Open Addressing (Dò tìm địa chỉ mở)*.
**Trạm 4 (Mock Interview):** Thiết kế cấu trúc dữ liệu `LRU Cache` (Least Recently Used) nổi tiếng. Yêu cầu `get` và `put` đều thao tác dưới ngưỡng $O(1)$. Bạn sẽ mix Hash Map với Cấu trúc dữ liệu nào? Tại sao?

---

## 📌 CHỦ ĐỀ 3: NGĂN XẾP (STACK) & HÀNG ĐỢI (QUEUE)
**Trạm 1 (Code Review):** Dev mới dùng danh sách `[]` của Python làm Queue. Hàm enqueue họ dùng `.append()`, hàm dequeue gọi `.pop(0)`. Bạn hãy chỉ ra sự tổn hao bộ nhớ và cách dùng thư viện chuẩn để xử lý tác vụ này với $O(1)$.
**Trạm 2 (Problem Solving):** (Monotonic Stack). Cho mảng `[73, 74, 75, 71, 69, 72, 76, 73]`. Tính xem sau bao nhiêu ngày (sự chênh lệch index) thì nhiệt độ mới cao hơn ngày hôm qua. Làm bài này trong $O(N)$.
**Trạm 3 (Deep Dive):** Stack lưu trữ ở đâu trên RAM của hệ điều hành? Lỗi kinh điển `StackOverflow` là gì và điều kiện vật lý nào nảy sinh ra nó?
**Trạm 4 (Mock Interview):** Hệ thống web Chat của bạn phải xử lý dấu ngoặc, thẻ HTML lồng nhau. Hãy xây dựng bộ Parser bằng Stack để phát hiện xem một đoạn văn bản HTML có hợp lệ hay bị thiếu thẻ đóng không?

---

## 📌 CHỦ ĐỀ 4: DANH SÁCH LIÊN KẾT (LINKED LIST)
**Trạm 1 (Code Review):** Đoạn code đảo ngược Linked List bị rơi vào vòng lặp vô hạn do đan chéo con trỏ `next`. Bạn phải chỉ ra lý do tại sao phải dùng 3 con trỏ `prev`, `curr`, `next` để dời lịch sử.
**Trạm 2 (Problem Solving):** Thuật toán [Rùa và Thỏ - Floyd's Cycle Detection]. Hãy chứng minh bằng toán/logic tại sao con trỏ đi 2 bước và con trỏ đi 1 bước **chắc chắn sẽ gặp nhau** nếu Linked List có vòng lặp (Cycle).
**Trạm 3 (Deep Dive):** Arrays vs Linked Lists ở cấp độ CPU Caching. Tại sao dù duyệt tuần tự $O(N)$, Arrays lại chạy thực tế phi mã so với Linked List nhờ vào cơ chế "Spatial Locality" của Cache L1/L2?
**Trạm 4 (Mock Interview):** Bài toán Browser History. Làm sao chỉ với thao tác $O(1)$ dung lượng và $O(1)$ thời gian, thiết kế được hệ thống bấm Back/Forward/Go-To-URL y hệt Google Chrome? (Gợi ý: Doubly Linked List).

---

## 📌 CHỦ ĐỀ 5: CÂY TRỊ QUY (TREES) & CÂY TÌM KIẾM NHỊ PHÂN (BST)
**Trạm 1 (Code Review):** Đoạn code tìm kiếm phần tử trên BST không có base case (điều kiện dừng) sinh lỗi `RecursionError`. Khắc phục và thiết lập ranh giới an toàn.
**Trạm 2 (Problem Solving):** Đảo ngược Cây Nhị Phân (Invert Binary Tree) - Câu hỏi nổi tiếng đã đánh trượt creator của Homebrew tại Google. Viết code DFS để làm trong 3 dòng.
**Trạm 3 (Deep Dive):** Nếu ta chèn dữ liệu tăng dần `[1, 2, 3, 4, 5]` vào BST, cây sẽ bị "Thoái hóa" thành Linked List dẫn tới $O(N)$. Nhắc đến khái niệm Cây cân bằng (AVL / Red-Black Tree) và cách chúng tự động xoay (rotate).
**Trạm 4 (Mock Interview):** Thiết kế Autocomplete cho thanh Search Bar. Bạn sẽ sử dụng cấu trúc Tree gì? (Trie). Tối ưu việc gợi ý 10 từ khóa tìm kiếm chung nhất nhanh nhất có thể.

---

## 📌 CHỦ ĐỀ 6: ĐỒ THỊ (GRAPHS) - DFS / BFS
**Trạm 1 (Code Review):** Code duyệt DFS trên Đồ thị bị Infinite Loop vì quên đánh dấu `visited`. Sửa nó bằng cấu trúc chuẩn của Set trong Python.
**Trạm 2 (Problem Solving):** Phát hiện chu trình (Cycle) trong đồ thị CÓ HƯỚNG. Tại sao mảng `visited` thông thường là không đủ kiện? (Phải dùng mảng trạng thái `visited` 3 biến: chưa thăm, đang thăm, đã duyệt xong).
**Trạm 3 (Deep Dive):** Khi nào dùng BFS (Theo chiều rộng)? Khi nào DFS (Theo chiều sâu)? Liên hệ với bài toán tìm đường ngắn nhất trong không gian mê cung đồng nhất (weight = 1).
**Trạm 4 (Mock Interview):** Hệ thống Build Tool (như npm, maven, docker engine) cần cài đặt một danh sách hàng nghìn package bị ràng buộc (Dependencies) lẫn nhau. Sử dụng Graph và thuật toán **Topological Sorting** để lập luồng xử lý (Cái nào cài trước, cái nào cài sau).

---

## 📌 CHỦ ĐỀ 7: HÀNG ĐỢI ƯU TIÊN (HEAP / PRIORITY QUEUE)
**Trạm 1 (Code Review):** Việc dùng `.sort()` mỗi khi thêm 1 phần tử mới vào mảng để lấy Top K. Chỉ ra tại sao nó là $O(N \log N)$ và cách Heap giảm thiểu nó xuống $O(\log N)$.
**Trạm 2 (Problem Solving):** Tìm trung vị (Median) trên luồng dữ liệu thời gian thực (Data Stream) dài vô hạn. Việc duy trì 1 Min-Heap và 1 Max-Heap song song giải quyết bài toán này ra sao? 
**Trạm 3 (Deep Dive):** Bản chất của một Binary Heap là một hoàn hảo biểu diễn dưới cấu trúc mảng 1 chiều (Array). Giải nghĩa công thức con Trái/Phải nằm ở `2*i + 1` và `2*i + 2`.
**Trạm 4 (Mock Interview):** Thuật toán dẫn đường Navigation. Bạn được bản đồ thành phố dạng Graph với chiều dài các đường thẳng, thiết kế **Thuật toán Dijkstra** với Min-Heap để tìm đường đi mất ít chặng / khoảng cách nhất.

---

## 📌 CHỦ ĐỀ 8: QUY HOẠCH ĐỘNG (DYNAMIC PROGRAMMING)
**Trạm 1 (Code Review):** Hàm đệ quy tính số Fibonacci siêu cồng kềnh với độ phức tạp $O(2^N)$. Bằng cách nào chỉ thêm đúng 2 dòng dùng Hash Map (Memoization) ta cứu được chương trình về $O(N)$?
**Trạm 2 (Problem Solving):** Longest Common Subsequence (Chuỗi con chung dài nhất) hoặc bài toán Knapsack (Cái ba lô). Xây dựng bảng quy hoạch động 2D (Tabulation).
**Trạm 3 (Deep Dive):** Bắt mạch "Khi nào thì dùng DP?". Định hình 2 chỉ dấu bắt buộc: Overlapping Subproblems (bài toán con trùng lặp) + Optimal Substructure (Cấu trúc tối ưu nội bộ).
**Trạm 4 (Mock Interview):** Phỏng vấn System Design: Viết thuật toán Text Justification giống Microsoft Word (chia dòng cho chữ để căn lề hai bên sao cho chi phí - số lượng khoảng trắng dư thừa tính theo hàm bình phương - là MIN nhất).

---
*Lộ trình được tạo tùy chỉnh, lưu tại `~repo/DSA_Lo_Trinh_On_Luyen_4_Tram.md`*
