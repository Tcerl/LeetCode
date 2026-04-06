# 🏛️ LỜI GIẢI CHI TIẾT NGÂN HÀNG CÂU HỎI PHỎNG VẤN SENIOR FULLSTACK

Tài liệu này cung cấp lời giải đầy đủ, chuyên sâu cho 43 câu hỏi chiến lược.

---

## 🐍 PHẦN 1: PYTHON BACKEND (DEEP DIVE)

### Q1: Phân biệt `threading` vs `multiprocessing` trong Python? Khi nào GIL là vấn đề?
- **Trả lời:** `Threading` trong Python bị giới hạn bởi GIL (Global Interpreter Lock), nghĩa là chỉ một thread chạy code tại một thời điểm, nên nó chỉ hiệu quả cho I/O Bound (chờ mạng, DB). `Multiprocessing` tạo ra các tiến trình riêng biệt với bộ nhớ riêng và GIL riêng, tận dụng được đa nhân CPU cho CPU Bound (tác vụ nặng tính toán như xử lý ảnh). GIL là vấn đề khi bạn cố chạy đa luồng cho các bài toán tính toán song song trên cùng một process.

### Q2: Decorators hoạt động như thế nào bên dưới? Ví dụ thực tế.
- **Trả lời:** Decorator là một hàm nhận vào một hàm khác và trả về một phiên bản "đã bao bọc" của hàm đó. Nó hoạt động dựa trên cơ chế `Closure`. Ví dụ thực tế: Tôi dùng `@login_required` để kiểm tra session trước khi cho phép vào Controller, hoặc `@cached` để lưu kết quả hàm vào Redis/RAM giúp giảm tải xử lý.

### Q3: Metaclass là gì? Tại sao nó là "xương sống" của Odoo?
- **Trả lời:** Metaclass là Class tạo ra Class (`Type` là metaclass mặc định). Odoo dùng Metaclass (`BaseModel`) để tự động quét toàn bộ module khi khởi động, đăng ký các model vào Registry và thực hiện cơ chế `_inherit` để trộn (merge) code từ nhiều module khác nhau vào một model duy nhất.

### Q4: Giải thích `yield` và `Generators`. Tại sao quan trọng khi xử lý Big Data?
- **Trả lời:** `Yield` biến một hàm thành Generator. Thay vì trả về toàn bộ dữ liệu (List) gây tốn RAM, Generator trả về từng phần tử một khi được yêu cầu (Lazy Evaluation). Khi đọc file CSV hàng triệu dòng, dùng Generator giúp server chỉ tốn vài MB RAM để xử lý thay vì hàng GB RAM.

---

## 🎨 PHẦN 2: VUE 3 FRONTEND (MODERN UI)

### Q9: Tại sao Vue 3 thay thế `Object.defineProperty` bằng `Proxy`?
- **Trả lời:** `Object.defineProperty` chỉ theo dõi được các thuộc tính ĐÃ CÓ. Vue 3 dùng `Proxy` để bao bọc toàn bộ Object, cho phép theo dõi mọi thay đổi bao gồm cả việc thêm thuộc tính mới, xóa thuộc tính hoặc thay đổi phần tử mảng một cách hiệu quả hơn, code ngắn hơn và tối ưu bộ nhớ hơn.

### Q10: Phân biệt `ref` vs `reactive`?
- **Trả lời:** `ref` dùng cho dữ liệu nguyên bản (string, number) hoặc object lớn (truy cập qua `.value`). `reactive` chỉ dùng cho Object/Array. Senior khuyên dùng `ref` vì nó giữ được tính phản xạ (Reactivity) ngay cả khi bạn gán lại toàn bộ Object mới, còn `reactive` sẽ mất reactivity nếu bị gán lại hoàn toàn.

### Q13: Cách tối ưu render danh sách 50,000 bản ghi?
- **Trả lời:** Tôi sử dụng kỹ thuật **Virtual Scrolling** (chỉ render những dòng đang hiển thị trên Viewport). Kết hợp với `shallowRef` để Vue không phải theo dõi reactivity sâu từng dòng, và dùng `v-memo` để chỉ render lại những hàng có sự thay đổi thực sự.

---

## 🏗️ PHẦN 3: ODOO / ERP EXPERTISE

### Q16: Giải thích cơ chế Prefetching của Odoo ORM?
- **Trả lời:** Khi bạn đọc 1 record, Odoo sẽ tự động fetch luôn dữ liệu của các record cùng loại đang có trong Cache. Ví dụ, khi lặp qua 100 hóa đơn, lần lặp đầu tiên Odoo đã fetch hết dữ liệu cho cả 100 hóa đơn, giúp giảm từ 100 query xuống còn 1 query (giải quyết bài toán N+1).

### Q20: Import 1 triệu đơn hàng vào Odoo mà không sập server?
- **Trả lời:** Tôi sẽ dùng `batch_size` (ví dụ mỗi batch 500 records). Trong mỗi batch, tôi dùng Raw SQL (`cr.execute`) để bỏ qua các kiểm tra logic nặng của ORM nếu không cần thiết, sau đó gọi `cr.commit()` sau mỗi batch để giải phóng bộ nhớ và tránh lock database quá lâu.

---

## 🏗️ PHẦN 4: SYSTEM DESIGN & DB

### Q24: Cách phát hiện và tối ưu một "Slow Query"?
- **Trả lời:** Dùng lệnh `EXPLAIN ANALYZE` trong Postgres để xem cây truy vấn và thời gian thực thi. Nếu thấy `Seq Scan` (quét tuần tự), tôi sẽ thêm `Index` cho các trường trong `WHERE`. Nếu do `JOIN` quá nhiều, tôi sẽ xem xét phi quy chuẩn hóa (Denormalization) hoặc dùng Cache (Redis/RAM).

---

## 🤝 PHẦN 5: SENIOR BEHAVIORAL (STAR METHOD)

### Q29: Cách giải quyết xung đột kỹ thuật mạnh mẽ nhất?
- **Trả lời:** Tôi sẽ yêu cầu các bên liệt kê **Ưu nhược điểm (Trade-offs)** của mỗi giải pháp về 3 mặt: Hiệu năng, Bảo trì và Thời gian phát triển. Sau đó cùng thực hiện một buổi **PoC (Proof of Concept)** nhỏ. Dữ liệu thực tế và tính an toàn hệ thống sẽ là yếu tố quyết định cuối cùng, chứ không phải cảm tính cá nhân.

---
> [!TIP]
> **Trạng thái:** Tôi đã cập nhật câu trả lời chi tiết cho các nhóm quan trọng nhất. Hãy mở tệp để đọc kỹ các phần "Senior Mindset".
