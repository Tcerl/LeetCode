# 06. Bản Đồ Kiến Thức & Phỏng Vấn Backend — Từ Fresher Đến Senior

> Đây là module **tổng hợp toàn diện nhất** của cây `Backend-Mastery`: với mỗi cấp độ sự nghiệp (Fresher → Junior → Mid-level → Senior), liệt kê **kiến thức bắt buộc phải biết**, **cách áp dụng vào công việc thực tế**, và **câu hỏi phỏng vấn thật kèm mẫu trả lời chuẩn**. Khác với [`05-Junior-To-Senior-Problem-Playbook`](../05-Junior-To-Senior-Problem-Playbook/README.md) (tập trung vào SỰ CỐ), module này tập trung vào **PHẠM VI KIẾN THỨC** cần có ở từng mốc sự nghiệp.

---

## 🟢 CẤP ĐỘ 1: FRESHER (Mới ra trường / 0-6 tháng kinh nghiệm)

### Kiến thức bắt buộc phải biết
- **Python nền tảng:** kiểu dữ liệu (list/tuple/dict/set), list comprehension, OOP cơ bản (class, kế thừa), xử lý exception (`try/except`), context manager (`with`).
- **SQL nền tảng:** `SELECT/WHERE/GROUP BY/ORDER BY`, các loại `JOIN` (INNER/LEFT/RIGHT), khái niệm Primary Key/Foreign Key.
- **HTTP & REST cơ bản:** các method (GET/POST/PUT/DELETE), status code phổ biến (200/201/400/401/404/500), khái niệm request/response, header là gì.
- **Git cơ bản:** commit/branch/merge/pull request, giải quyết conflict đơn giản.
- **1 framework cơ bản:** Flask hoặc Django — biết tạo route, nhận request, trả JSON.

### Áp dụng thực tế
Ở mức fresher, công việc thường là: sửa bug nhỏ có hướng dẫn rõ, viết CRUD endpoint đơn giản theo mẫu có sẵn, viết unit test cơ bản cho hàm đã có logic rõ ràng. **Trọng tâm:** viết code ĐÚNG theo yêu cầu, tuân thủ coding convention của team, biết hỏi khi không chắc thay vì đoán mò.

### 💬 Câu hỏi phỏng vấn thường gặp + mẫu trả lời

**Q: "Sự khác nhau giữa `list` và `tuple` trong Python?"**
> *Trả lời mẫu:* "List có thể thay đổi được (mutable) — thêm/xóa/sửa phần tử sau khi tạo; tuple thì bất biến (immutable) — một khi tạo xong không thay đổi được. Vì bất biến, tuple có thể dùng làm key trong dictionary còn list thì không. Em thường dùng tuple khi muốn đảm bảo dữ liệu không bị vô tình sửa đổi, ví dụ tọa độ (x, y) hoặc trả về nhiều giá trị cố định từ 1 hàm."

**Q: "`JOIN` và `LEFT JOIN` khác nhau thế nào?"**
> *Trả lời mẫu:* "INNER JOIN chỉ trả về các dòng có dữ liệu khớp ở CẢ HAI bảng. LEFT JOIN trả về TOÀN BỘ dòng của bảng bên trái, kể cả khi không có dòng khớp ở bảng bên phải (các cột bên phải sẽ là NULL). Ví dụ: lấy danh sách TẤT CẢ khách hàng kể cả những người chưa từng đặt hàng, phải dùng LEFT JOIN từ bảng customers sang orders, vì INNER JOIN sẽ loại bỏ khách hàng chưa có đơn hàng nào."

**Q: "HTTP status code 400 và 500 khác nhau ở đâu?"**
> *Trả lời mẫu:* "4xx là lỗi do phía CLIENT gửi request sai (400 Bad Request — dữ liệu gửi lên không hợp lệ, 401 — chưa xác thực, 404 — không tìm thấy tài nguyên). 5xx là lỗi do phía SERVER — server gặp exception không xử lý được, ví dụ code bị crash hoặc kết nối database thất bại. Phân biệt được 2 loại này quan trọng vì nó quyết định phía nào cần fix: 4xx nghĩa là client cần sửa cách gọi API, 5xx nghĩa là backend có bug cần fix."

---

## 🟡 CẤP ĐỘ 2: JUNIOR (6 tháng - 2 năm)

### Kiến thức bắt buộc phải biết
- **ORM thành thạo:** Django ORM/SQLAlchemy — query, filter, relationship (`ForeignKey`, `ManyToMany`), migration.
- **Thiết kế REST API cơ bản đúng chuẩn:** đặt tên endpoint theo resource (`/users/{id}`, không phải `/getUser`), versioning API, cấu trúc response nhất quán.
- **N+1 query problem:** nhận diện và fix bằng `select_related`/`prefetch_related` — xem chi tiết [`01-Request-Lifecycle-And-Architecture`](../01-Request-Lifecycle-And-Architecture/README.md).
- **Testing:** viết unit test với mock, phân biệt unit test và integration test.
- **Docker cơ bản:** viết Dockerfile đơn giản, `docker-compose` cho môi trường dev.
- **Authentication cơ bản:** JWT là gì, session vs token-based auth.

### Áp dụng thực tế
Tự thiết kế và implement 1 tính năng nhỏ-vừa từ đầu tới cuối (API + logic + test) với ít giám sát hơn. Bắt đầu tham gia code review — cho feedback về style/bug đơn giản. Debug được lỗi trong phạm vi module mình phụ trách.

### 💬 Câu hỏi phỏng vấn thường gặp + mẫu trả lời

**Q: "N+1 query problem là gì và làm sao phát hiện/fix nó?"**
> *Trả lời mẫu:* "N+1 xảy ra khi lấy N bản ghi rồi với MỖI bản ghi lại query thêm 1 lần để lấy dữ liệu liên quan — tổng cộng N+1 query thay vì 1. Ví dụ lấy 100 đơn hàng rồi loop qua từng đơn để lấy `order.customer.name` sẽ tạo ra 101 query. Em phát hiện bằng cách bật query logging ở môi trường dev và đếm số query mỗi request. Cách fix trong Django là dùng `select_related()` cho quan hệ ForeignKey (JOIN ngay trong 1 query) hoặc `prefetch_related()` cho quan hệ ManyToMany."

**Q: "Khi nào dùng PUT, khi nào dùng PATCH?"**
> *Trả lời mẫu:* "PUT dùng để thay thế TOÀN BỘ resource — client phải gửi đầy đủ tất cả field, field nào không gửi sẽ bị coi là xóa/reset. PATCH chỉ cập nhật MỘT PHẦN — chỉ gửi field cần đổi, các field khác giữ nguyên. Ví dụ update chỉ riêng email của user nên dùng PATCH thay vì PUT để tránh vô tình ghi đè các field khác thành rỗng."

**Q: "Bạn test 1 API endpoint như thế nào?"**
> *Trả lời mẫu:* "Em viết test theo 3 nhóm: (1) happy path — input đúng, kiểm tra response đúng định dạng và status code đúng; (2) validation error — input sai định dạng, kiểm tra trả về 400 với message rõ ràng; (3) edge case — input rỗng, giá trị biên, quyền truy cập sai (401/403). Với phần phụ thuộc external service, em mock lại để test không bị phụ thuộc vào service đó có sẵn hay không."

---

## 🔴 CẤP ĐỘ 3: MID-LEVEL (2-4 năm)

### Kiến thức bắt buộc phải biết
- **Concurrency thật sự:** GIL, khi nào dùng asyncio/threading/multiprocessing — xem [`02-Concurrency-And-Async-In-Production`](../02-Concurrency-And-Async-In-Production/README.md).
- **Database sâu:** transaction, isolation level, index strategy, phân tích `EXPLAIN` — xem [`03-Database-Choice-And-Scaling-Playbook`](../03-Database-Choice-And-Scaling-Playbook/README.md).
- **Caching strategy:** cache-aside, write-through, invalidation strategy, TTL.
- **Message Queue:** khi nào cần queue, đảm bảo idempotency, xử lý retry/dead-letter-queue.
- **Observability cơ bản:** structured logging, đọc metrics/trace để debug — xem [`04-Testing-Observability-And-Debugging-Prod`](../04-Testing-Observability-And-Debugging-Prod/README.md).
- **CI/CD cơ bản:** hiểu pipeline, viết được GitHub Actions/GitLab CI đơn giản.

### Áp dụng thực tế
Tự thiết kế kiến trúc cho module vừa-lớn, đưa ra quyết định công nghệ (chọn cache ở đâu, có cần queue không) có giải thích được lý do. Review code không chỉ bug mà cả performance/kiến trúc. Debug được sự cố production với sự hỗ trợ observability.

### 💬 Câu hỏi phỏng vấn thường gặp + mẫu trả lời

**Q: "Giải thích ACID trong database?"**
> *Trả lời mẫu:* "ACID là 4 tính chất đảm bảo transaction đáng tin cậy: **Atomicity** — transaction hoặc thực hiện HOÀN TOÀN hoặc không thực hiện gì cả (all-or-nothing), nếu giữa chừng lỗi thì rollback hết. **Consistency** — transaction luôn đưa DB từ trạng thái hợp lệ này sang trạng thái hợp lệ khác, không vi phạm constraint. **Isolation** — nhiều transaction chạy đồng thời không ảnh hưởng lẫn nhau như thể chạy tuần tự (mức độ isolation có thể điều chỉnh, đánh đổi với hiệu năng). **Durability** — sau khi commit thành công, dữ liệu tồn tại vĩnh viễn kể cả khi mất điện/crash ngay sau đó."

**Q: "Cache của bạn stale (dữ liệu cũ) thì xử lý sao?"**
> *Trả lời mẫu:* "Trước tiên phải xác định chiến lược invalidation ngay từ khi thiết kế, không phải vá sau: TTL ngắn cho dữ liệu ít quan trọng độ tươi tuyệt đối, hoặc invalidate chủ động (xóa/update cache) ngay khi dữ liệu gốc thay đổi thông qua event/hook. Với dữ liệu quan trọng cần chính xác tuyệt đối (số dư tài khoản), em sẽ cân nhắc không cache hoặc cache với TTL cực ngắn kết hợp double-check ở nguồn khi thao tác quan trọng."

**Q: "Kể về 1 lần bạn gặp race condition và cách fix."**
> *Trả lời mẫu (dùng khung STAR — xem [`../Career-Mastery/04`](../../Career-Mastery/04-Behavioral-And-Salary-Negotiation/README.md)):* "2 request đăng ký cùng username gần như đồng thời đều pass qua bước check tồn tại trước khi transaction nào commit — tạo ra 2 user trùng username. Em fix bằng cách thêm unique constraint ở DB làm lớp bảo vệ cuối cùng, bắt `IntegrityError` khi commit thay vì chỉ dựa vào check ở application logic."

---

## ⭐ CẤP ĐỘ 4: SENIOR (4+ năm)

### Kiến thức bắt buộc phải biết
- **System Design toàn diện:** trade-off SQL/NoSQL, chiến lược scale (cache → replica → shard), thiết kế API cho hệ thống lớn — xem [`../Career-Mastery/02`](../../Career-Mastery/02-System-Design-Interview-Playbook/README.md).
- **Kiến trúc microservices vs monolith:** biết khi nào KHÔNG nên tách service — xem case study [`../Frontend-Fullstack-Mastery/04`](../../Frontend-Fullstack-Mastery/04-Real-World-Project-Case-Study/README.md).
- **Vận hành production:** SLI/SLO, incident response, postmortem — xem [`../Cloud-DevOps-Mastery/05`](../../Cloud-DevOps-Mastery/05-Observability-Incident-Response/README.md).
- **Kỹ năng lãnh đạo kỹ thuật:** mentoring, đưa ra quyết định kiến trúc có thể giải thích cho người không chuyên, cân bằng technical debt và tốc độ ra tính năng.

### Áp dụng thực tế
Chịu trách nhiệm về độ tin cậy và khả năng mở rộng của cả hệ thống, không chỉ 1 tính năng. Đưa ra quyết định kiến trúc có ảnh hưởng dài hạn (6-12 tháng). Mentoring junior/mid, review kiến trúc thay vì chỉ review code từng dòng. Giao tiếp được với stakeholder không chuyên kỹ thuật.

### 💬 Câu hỏi phỏng vấn thường gặp + mẫu trả lời

**Q: "Thiết kế 1 hệ thống rate limiter cho API."**
> *Trả lời mẫu (khung 5 bước — xem [`../Career-Mastery/02`](../../Career-Mastery/02-System-Design-Interview-Playbook/README.md)):* "Đầu tiên em làm rõ yêu cầu: giới hạn theo user hay theo IP? Chính xác tuyệt đối hay có thể chấp nhận sai số nhỏ để đổi lấy hiệu năng? Sau đó ước lượng quy mô — bao nhiêu request/giây cần xử lý. Với hệ thống phân tán nhiều instance, em sẽ dùng Redis để lưu counter dùng chung thay vì lưu local ở từng instance (nếu không, mỗi instance đếm riêng sẽ vượt quá giới hạn tổng thật). Thuật toán em chọn là sliding window log hoặc token bucket tùy yêu cầu độ chính xác — đánh đổi giữa độ chính xác và bộ nhớ cần lưu."

**Q: "Bạn cân bằng giữa technical debt và deadline ra sao?"**
> *Trả lời mẫu:* "Em phân loại technical debt theo mức độ rủi ro: debt nào có thể gây sự cố production (thiếu test cho luồng thanh toán, thiếu index cho bảng đang phình to) được ưu tiên xử lý ngay dù ảnh hưởng deadline; debt chỉ ảnh hưởng tốc độ phát triển sau này (code chưa đẹp nhưng chạy đúng, không rủi ro) có thể defer, nhưng em luôn ghi lại rõ ràng (ticket cụ thể) để không bị quên vĩnh viễn. Em cũng trao đổi rõ với PM/stakeholder về đánh đổi này bằng ngôn ngữ không kỹ thuật: 'nếu làm nhanh theo cách A, rủi ro X có thể xảy ra trong Y tháng tới'."

**Q: "Nếu phát hiện 1 quyết định kiến trúc của chính mình trước đây là sai, bạn xử lý thế nào?"**
> *Trả lời mẫu:* "Em thừa nhận thẳng thắn thay vì cố bảo vệ quyết định cũ — đây là văn hóa blameless mà em luôn áp dụng cho cả bản thân (xem [`../Cloud-DevOps-Mastery/05`](../../Cloud-DevOps-Mastery/05-Observability-Incident-Response/README.md) về postmortem). Em đánh giá chi phí sửa NGAY so với sống chung có kiểm soát, đề xuất lộ trình migrate dần (nếu hệ thống đã lớn, thường không thể đổi 1 phát) và ghi lại bài học trong tài liệu quyết định kiến trúc (ADR) để team không lặp lại."

---

## 🗺️ Tổng kết: bản đồ điều hướng theo mục tiêu của bạn

```
Đang là Fresher, chuẩn bị phỏng vấn Junior?
   → Học chắc SQL/Python/REST cơ bản ở mục 1, luyện trả lời câu hỏi mẫu mục 1

Đang là Junior, muốn lên Mid-level?
   → Đọc kỹ Module 01-04 (Request Lifecycle, Concurrency, Database, Observability)
     để có ĐỦ chiều sâu trả lời câu hỏi mục 3, không chỉ học thuộc câu trả lời mẫu

Đang là Mid-level, chuẩn bị phỏng vấn Senior?
   → Luyện System Design theo khung ở Career-Mastery/02, chuẩn bị câu chuyện
     STAR thật từ chính kinh nghiệm cá nhân (không dùng câu trả lời mẫu nguyên văn)
```

**Lưu ý quan trọng:** các câu trả lời mẫu ở trên là KHUNG để tham khảo cách trình bày có cấu trúc — khi phỏng vấn thật, luôn thay bằng ví dụ THẬT từ kinh nghiệm cá nhân bạn, vì người phỏng vấn senior luôn hỏi xoáy sâu thêm ("vậy lúc đó bạn đo bằng công cụ gì?", "con số cụ thể là bao nhiêu?") — trả lời học thuộc không có chi tiết thật sẽ lộ ngay.

## 🔗 Liên kết module khác
Chi tiết kỹ thuật từng chủ đề: [`01`](../01-Request-Lifecycle-And-Architecture/README.md) · [`02`](../02-Concurrency-And-Async-In-Production/README.md) · [`03`](../03-Database-Choice-And-Scaling-Playbook/README.md) · [`04`](../04-Testing-Observability-And-Debugging-Prod/README.md) · [`05`](../05-Junior-To-Senior-Problem-Playbook/README.md)
Chiến lược trả lời phỏng vấn tổng quát (không riêng backend): [`../Career-Mastery/`](../../Career-Mastery/INDEX.md)
