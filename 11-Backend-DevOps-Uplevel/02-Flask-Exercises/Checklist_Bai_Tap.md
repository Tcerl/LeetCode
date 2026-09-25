# ✅ Checklist Bài Tập Flask (FL-01 → FL-04)

> Mục tiêu chính của phần Flask không phải học lại backend, mà là **cảm nhận sự khác biệt "minimalist" của Flask so với Django "batteries-included"** — đây là câu hỏi phỏng vấn senior rất hay gặp ("khi nào chọn Flask, khi nào chọn Django").

- [ ] **FL-01 — Viết lại API Django bằng Flask thuần** (Tuần 9): Lấy đúng API `Post` đã làm ở DJ-05, viết lại bằng Flask (không dùng ORM) chỉ với `flask.Flask` + route thuần — ghi note bạn phải tự viết thêm những gì mà Django có sẵn.
- [ ] **FL-02 — Thêm Flask-SQLAlchemy** (Tuần 10): Thêm ORM vào app trên bằng Flask-SQLAlchemy, so sánh cú pháp query với Django ORM.
- [ ] **FL-03 — Blueprint hóa** (Tuần 10): Tách app thành nhiều Blueprint (`auth`, `posts`) thay vì để hết trong 1 file — tập thói quen tổ chức code Flask ở quy mô lớn hơn "hello world".
- [ ] **FL-04 — Dockerize** (Tuần 11): Viết Dockerfile cho app Flask trên, build & chạy container, verify API vẫn hoạt động qua `curl`.

## 🎯 Bài tập nâng cao
- [ ] Thêm Flask-Migrate để quản lý migration giống Django.
- [ ] Viết 1 bảng so sánh cá nhân: Frappe vs Django vs Flask — cột "khi nào dùng", dùng chính bảng này để trả lời phỏng vấn.
