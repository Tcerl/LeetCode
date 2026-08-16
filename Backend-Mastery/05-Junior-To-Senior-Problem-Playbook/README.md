# 05. Lộ Trình Vấn Đề Thật: Từ Junior Đến Senior (Backend & Database)

> Tổng hợp lại các vấn đề đã nhắc ở Module 01-04, sắp xếp theo cấp độ để tự định vị và biết bước tiếp theo cần học.

---

## 🟢 Cấp độ Junior — "API chạy đúng lúc demo, không hiểu vì sao production khác"

| Vấn đề gặp phải | Vì sao xảy ra | Cách vượt qua | Đọc thêm |
|---|---|---|---|
| API danh sách chạy nhanh lúc test (20 bản ghi), rùa bò trên production (50,000 bản ghi) | Chưa có thói quen bật query log để soi N+1 | Luôn bật SQL query log ở môi trường dev, đếm số query mỗi request | [`01`](../01-Request-Lifecycle-And-Architecture/README.md) |
| `async def` viết ra nhưng API không nhanh hơn | Gọi nhầm thư viện đồng bộ (`requests`, `time.sleep`) bên trong hàm async | Luôn kiểm tra: MỌI I/O trong hàm async phải có bản async thật (`httpx`, `asyncpg`) | [`02`](../02-Concurrency-And-Async-In-Production/README.md) |
| Copy nguyên field từ Exception ra response trả cho client (lộ stack trace, đường dẫn nội bộ) | Chưa có ý thức phân biệt lỗi "cho dev xem" (log) và lỗi "cho user xem" (response) | Luôn catch exception, log đầy đủ nội bộ, trả về message chung an toàn cho client | [`04`](../04-Testing-Observability-And-Debugging-Prod/README.md) |
| Test chỉ chạy happy path, không test input rỗng/None/sai kiểu | Chưa hình thành thói quen nghĩ tới edge case trước khi coi task "xong" | Luyện tập: trước khi đóng task, tự hỏi "input rỗng thì sao, input cực lớn thì sao" | [`04`](../04-Testing-Observability-And-Debugging-Prod/README.md) |

**Bài học junior cần khắc cốt ghi tâm:** *Môi trường demo và production KHÔNG giống nhau về quy mô dữ liệu, số lượng người dùng đồng thời, và độ tin cậy mạng — code "chạy được lúc demo" chưa phải code hoàn thành.*

---

## 🟡 Cấp độ Mid-level — "Biết framework/ORM, nhưng chưa quản lý được tài nguyên hữu hạn"

| Vấn đề gặp phải | Vì sao xảy ra | Cách vượt qua | Đọc thêm |
|---|---|---|---|
| Deploy nhiều instance app, DB báo lỗi "too many connections" dù CPU/RAM DB vẫn dư | Chưa tính toán `số instance × pool size ≤ max_connections DB` | Luôn tính giới hạn connection TRƯỚC khi scale ngang, cân nhắc PgBouncer | [`01`](../01-Request-Lifecycle-And-Architecture/README.md) |
| Chọn Mongo/Postgres theo thói quen cá nhân, không theo yêu cầu nghiệp vụ | Chưa có khung tiêu chí ra quyết định rõ ràng | Luôn tự trả lời: cần transaction đa bảng không? tỉ lệ đọc/ghi thế nào? | [`03`](../03-Database-Choice-And-Scaling-Playbook/README.md) |
| 2 transaction thỉnh thoảng bị deadlock ngẫu nhiên, khó tái hiện | Khóa tài nguyên không theo thứ tự nhất quán trong codebase | Áp dụng kỷ luật: luôn khóa theo thứ tự cố định (VD: theo id tăng dần) toàn team | [`03`](../03-Database-Choice-And-Scaling-Playbook/README.md) |
| Viết `BackgroundTasks` cho việc quan trọng (gửi email xác nhận thanh toán), thỉnh thoảng mất task khi server restart | Chưa phân biệt background task trong-process (không persistent) và queue thật (Celery/SQS, có retry) | Việc quan trọng luôn đẩy qua queue có persistence + dead-letter-queue | [`02`](../02-Concurrency-And-Async-In-Production/README.md) |

**Bài học mid-level cần khắc cốt ghi tâm:** *Mọi tài nguyên (connection, memory, thread) đều HỮU HẠN — code đúng logic vẫn có thể làm sập hệ thống nếu không tính toán giới hạn tài nguyên khi scale.*

---

## 🔴 Cấp độ Senior — "Thiết kế hệ thống chịu tải, không chỉ viết feature"

| Vấn đề gặp phải (ở tầm hệ thống) | Senior xử lý thế nào | Đọc thêm |
|---|---|---|
| Team liên tục "vá" từng N+1 query riêng lẻ khi bị phát hiện, không có giải pháp gốc rễ | Đưa quy tắc vào code review checklist + tự động hóa cảnh báo (query counter middleware) thay vì chờ phát hiện thủ công | [`01`](../01-Request-Lifecycle-And-Architecture/README.md) |
| Hệ thống bắt đầu chậm dần khi data tăng, team đòi sharding ngay | Đánh giá đã thử hết cache → read replica → partitioning chưa trước khi chấp nhận độ phức tạp của sharding | [`03`](../03-Database-Choice-And-Scaling-Playbook/README.md) |
| Migration schema gây downtime/lỗi khi rollback | Thiết kế lại quy trình migration theo expand-contract pattern, review MỌI migration trước khi merge | [`../Cloud-DevOps-Mastery/04`](../../Cloud-DevOps-Mastery/04-CICD-Deployment-Strategies/README.md) |
| Team có logs nhưng vẫn mất hàng giờ để tìm nguyên nhân khi có sự cố | Thiết kế lại observability: structured logging + metrics + tracing, không chỉ dựa vào `print()`/log rời rạc | [`04`](../04-Testing-Observability-And-Debugging-Prod/README.md) |
| Junior/mid thiết kế API không nhất quán giữa các service | Định ra chuẩn kiến trúc chung (API contract, error format, versioning), review kiến trúc trước khi cho code | [`../Career-Mastery/01`](../../Career-Mastery/01-Senior-Mindset-And-Career-Reality/README.md) |

**Bài học senior cần khắc cốt ghi tâm:** *Senior giải quyết vấn đề ở tầng QUY TRÌNH/KIẾN TRÚC để nó không lặp lại — không chỉ fix từng triệu chứng riêng lẻ mỗi khi bị báo cáo.*

---

## 🗺️ Lộ trình tổng hợp để tự đánh giá bản thân đang ở đâu

```
Junior  → Code chạy đúng logic nghiệp vụ, CHƯA để ý resource limit/edge case
            │ (dấu hiệu sẵn sàng lên Mid: chủ động bật query log, viết test edge case
            │  mà không cần nhắc)
            ▼
Mid     → Hiểu và quản lý được tài nguyên hữu hạn (connection, memory), chọn đúng
          công nghệ theo tiêu chí rõ ràng
            │ (dấu hiệu sẵn sàng lên Senior: tự nhận diện được vấn đề LẶP LẠI nhiều lần
            │  và đề xuất giải pháp ở tầng quy trình thay vì vá từng chỗ)
            ▼
Senior  → Thiết kế kiến trúc/quy trình để loại bỏ CẢ LỚP vấn đề, không chỉ fix từng case
```

## 🔗 Liên kết
Chi tiết kỹ thuật: [`01`](../01-Request-Lifecycle-And-Architecture/README.md) · [`02`](../02-Concurrency-And-Async-In-Production/README.md) · [`03`](../03-Database-Choice-And-Scaling-Playbook/README.md) · [`04`](../04-Testing-Observability-And-Debugging-Prod/README.md)
Tầng hạ tầng triển khai các giải pháp trên: [`../Cloud-DevOps-Mastery/`](../../Cloud-DevOps-Mastery/INDEX.md)
