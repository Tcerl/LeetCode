# 05. Practice Lab — Cách Khai Thác Kho Bài Tập Vue/Laravel Đã Có

> Kho bài tập gốc: [`CODE_EXERCISES.md`](../../../06-Exercises/CODE_EXERCISES.md) (4000+ dòng: Vue, Pinia, Nuxt, Laravel, Axios, Testing, Mock Interview, Security Checklist đã có sẵn rất đầy đủ). File này không lặp lại nội dung — chỉ bổ sung **cách luyện tập hiệu quả** và liên kết các bài tập với đúng module senior tương ứng.

---

## 1. Bản đồ: Bài tập trong `CODE_EXERCISES.md` → Module senior liên quan

| Bài tập gốc | Kỹ năng chính | Đọc thêm senior tại |
|---|---|---|
| VUE-01, VUE-02, VUE-03 (Reactivity, Composables) | Cơ chế reactive, tái sử dụng logic | [`01-Frontend-Architecture-And-Performance`](../01-Frontend-Architecture-And-Performance/README.md) |
| PINIA-01, PINIA-02 (Cart Store, Auth Store) | Quản lý state toàn cục | [`02-State-Management-And-Data-Fetching`](../02-State-Management-And-Data-Fetching/README.md) |
| API-01 (Axios Interceptor JWT) | Xử lý auth token, race condition khi refresh | [`02-State-Management-And-Data-Fetching`](../02-State-Management-And-Data-Fetching/README.md) mục 2 |
| LARAVEL-01, 02, 03 (Eloquent, CRUD API, Queue) | ORM, REST API, xử lý bất đồng bộ | [`../Backend-Mastery/01`](../../Backend-Mastery/01-Request-Lifecycle-And-Architecture/README.md), [`../Backend-Mastery/02`](../../Backend-Mastery/02-Concurrency-And-Async-In-Production/README.md) |
| VUE-09 (Virtual List Performance) | Tối ưu render danh sách lớn | [`01-Frontend-Architecture-And-Performance`](../01-Frontend-Architecture-And-Performance/README.md) mục 3 |
| LARAVEL-04 (Testing) | Unit/Feature test | [`../Backend-Mastery/04`](../../Backend-Mastery/04-Testing-Observability-And-Debugging-Prod/README.md) mục 1 |
| Security Checklist (đã có sẵn trong file gốc) | Checklist trước khi deploy | Bổ sung góc nhìn ở mục 2 bên dưới |

---

## 2. Bổ sung: Security Checklist đã có — vì sao TỪNG mục lại quan trọng thật sự

File gốc đã liệt kê checklist bảo mật trước khi deploy. Bổ sung "tại sao" cho các mục dễ bị xem nhẹ nhất:

- **CORS cấu hình đúng domain, không dùng `*` cho production:** `Access-Control-Allow-Origin: *` kết hợp `Access-Control-Allow-Credentials: true` là cấu hình **không hợp lệ và nguy hiểm** — cho phép BẤT KỲ website nào gọi API kèm cookie/credential của user, mở đường cho tấn công CSRF quy mô lớn.
- **Rate limiting ở API Gateway/Backend:** không chỉ chống spam — còn chống **brute-force** vào endpoint đăng nhập (liên kết trực tiếp kỹ thuật Rate Limiter ở [`../DSA-Mastery/02`](../../DSA-Mastery/02-Linear-Structures-And-Hashing/README.md)).
- **Validate input ở BACKEND, không chỉ frontend:** validate frontend chỉ là UX (feedback nhanh cho user) — **không phải bảo mật**, vì attacker có thể gọi thẳng API bỏ qua UI hoàn toàn. Đây là lỗi tư duy rất phổ biến ở dev mới.

---

## 3. Cách luyện tập hiệu quả hơn — quy trình 3 bước senior áp dụng

1. **Làm bài tập gốc bình thường** (theo đúng hướng dẫn trong `CODE_EXERCISES.md`).
2. **Tự đặt câu hỏi "phá hoại":** "Nếu 100 user cùng bấm nút này 1 lúc thì sao?", "Nếu network bị mất giữa chừng thì sao?", "Nếu user cố tình gửi dữ liệu sai định dạng thì sao?" — đây chính là tư duy đã áp dụng khi review `09-Example-Projects` ở [`03-Fullstack-Project-Architecture`](../03-Fullstack-Project-Architecture/README.md).
3. **So sánh với case thật đã review** — mỗi bài tập gốc đều có 1 "phiên bản production" tương ứng đã phân tích trong các module senior liệt kê ở bảng trên; đọc lại để thấy khoảng cách giữa "bài tập chạy đúng" và "code sẵn sàng chịu tải thật".

---

## 4. Ghi chú: `MATLAB/` trong `06-Exercises/`

Thư mục `06-Exercises/MATLAB/` (giáo trình MATLAB từ cơ bản tới ML/Deep Learning/Simulink) thuộc mảng **tính toán khoa học/kỹ thuật**, không liên quan trực tiếp tới hệ sinh thái Web Fullstack hay 4 nhóm chủ đề đã ưu tiên xử lý (DSA, Backend, Cloud/DevOps, Career). Nội dung này **chưa được gộp vào cây kiến thức nào** — nếu cần, có thể tạo riêng 1 cây `Scientific-Computing-Mastery/` khi có yêu cầu cụ thể.

---

## 🎯 Câu hỏi senior hay hỏi khi review bài tập tự làm

1. "Bài tập này nếu chạy với 1000 item/1000 user cùng lúc thay vì demo vài item, còn đúng không?"
2. "Phần validate trong bài tập của bạn có ở cả frontend LẪN backend không?"
3. "Nếu tách bài tập này thành 1 API thật, response lỗi trả về có đủ thông tin để debug mà không lộ chi tiết hệ thống (stack trace, đường dẫn nội bộ) không?"

## 🔗 Liên kết module khác
Toàn bộ nền tảng: [`01`](../01-Frontend-Architecture-And-Performance/README.md) · [`02`](../02-State-Management-And-Data-Fetching/README.md) · [`03`](../03-Fullstack-Project-Architecture/README.md) · [`04`](../04-Real-World-Project-Case-Study/README.md)
