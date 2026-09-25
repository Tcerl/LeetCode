# ✅ Checklist Bài Tập Django (DJ-01 → DJ-07)

> Làm đúng thứ tự, không xem code mẫu trước khi tự thử ít nhất 15 phút. Đánh dấu `[x]` khi xong, ghi ngày hoàn thành.

- [ ] **DJ-01 — Model & Migration** (Tuần 1): Tạo app `blog` với 2 model `Author` và `Post` (quan hệ ForeignKey), chạy migration, tạo vài bản ghi qua Django Admin.
- [ ] **DJ-02 — CRUD View cơ bản** (Tuần 2): Viết view list/detail/create cho `Post` bằng Function-Based View trước, sau đó viết lại bằng Class-Based View (`ListView`, `DetailView`, `CreateView`) — so sánh lượng code.
- [ ] **DJ-03 — Query tối ưu** (Tuần 3): Viết 1 trang hiển thị 20 bài Post kèm tên Author — cố tình để N+1 query xảy ra, đếm số query bằng Django Debug Toolbar, sau đó fix bằng `select_related`.
- [ ] **DJ-04 — So sánh Frappe vs Django** (Tuần 4, viết ngắn 1 trang note): Liệt kê 5 điểm khác biệt giữa cách Frappe xử lý model/hook và cách Django xử lý model/signal — việc này giúp bạn trả lời tốt câu phỏng vấn "vì sao chuyển sang Django".
- [ ] **DJ-05 — DRF CRUD API** (Tuần 6): Biến app `blog` thành REST API đầy đủ (list/create/update/delete) bằng DRF ViewSet + Router.
- [ ] **DJ-06 — Auth JWT** (Tuần 7): Thêm đăng ký/đăng nhập trả JWT, bảo vệ endpoint tạo Post chỉ cho user đã login.
- [ ] **DJ-07 — Unit Test** (Tuần 8): Viết test cho API trên — tối thiểu 1 test happy path, 1 test validation lỗi (401 khi chưa login, 400 khi thiếu field).

## 🎯 Bài tập nâng cao (làm nếu còn dư thời gian, không bắt buộc)
- [ ] Thêm phân trang (pagination) + filter theo Author cho API list Post.
- [ ] Viết custom Django management command (`python manage.py seed_data`) để tự sinh dữ liệu giả.
