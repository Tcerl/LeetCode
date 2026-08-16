# 03. Chọn & Mở Rộng Database — Playbook Quyết Định Thật

> Lý thuyết Postgres/Mongo chi tiết đã có ở [`PostgreSQL_Expert_Guide.md`](../../04-Database-Mastery/PostgreSQL_Expert_Guide.md) và [`MongoDB_Expert_Guide.md`](../../04-Database-Mastery/MongoDB_Expert_Guide.md) (đặc biệt mục "Khi nào dùng SQL vs NoSQL" đã có sẵn). File này bổ sung **khung ra quyết định** và các sự cố thật khi hệ thống scale.

---

## 1. Khung quyết định SQL vs NoSQL — vượt ra ngoài "SQL cho dữ liệu có cấu trúc"

Câu trả lời sách vở "SQL cho dữ liệu quan hệ, NoSQL cho dữ liệu linh hoạt" không đủ cho quyết định thật. Senior hỏi thêm:

| Câu hỏi | Nếu câu trả lời nghiêng về... | Xu hướng chọn |
|---|---|---|
| Có cần transaction đa bảng (chuyển tiền, đặt hàng trừ kho) không? | Có, bắt buộc ACID | PostgreSQL |
| Schema có thay đổi liên tục theo từng khách hàng (multi-tenant SaaS linh hoạt)? | Có | MongoDB (document linh hoạt) |
| Tỷ lệ đọc/ghi thế nào? Ghi cực nhiều, ít join (log, event, IoT sensor data)? | Ghi nhiều, đơn giản | MongoDB/Cassandra (tối ưu ghi) hoặc TimescaleDB |
| Có cần full-text search phức tạp, join nhiều bảng báo cáo? | Có | PostgreSQL (hoặc thêm Elasticsearch riêng cho search) |
| Team có kinh nghiệm vận hành gì sẵn? | — | Yếu tố thực tế thường bị đánh giá thấp nhưng quyết định rất nhiều trong công ty vừa/nhỏ |

**Thực tế senior hay gặp nhất:** không phải chọn 1 trong 2 tuyệt đối, mà là **polyglot persistence** — dùng Postgres cho dữ liệu giao dịch lõi, Redis cho cache/session, Elasticsearch cho search, S3 cho file lớn — mỗi công cụ giải quyết đúng 1 bài toán nó mạnh nhất.

---

## 2. Index — con dao hai lưỡi, không phải "cứ thêm cho chắc"

Đã có lý thuyết chi tiết ở PostgreSQL_Expert_Guide mục 2. Bổ sung góc nhìn vận hành thật:

- **Mỗi index tăng tốc `SELECT` nhưng làm chậm `INSERT/UPDATE/DELETE`** (phải cập nhật lại cấu trúc B-Tree — liên kết [`DSA-Mastery/03`](../../DSA-Mastery/03-Trees-Heaps-Tries/README.md)). Bảng ghi nhiều (event log) mà thêm quá nhiều index → ghi chậm hẳn, đây là sự cố thật khi "tối ưu đọc" vô tình phá "hiệu năng ghi".
- **Index không dùng vẫn tốn dung lượng + I/O khi ghi** — senior định kỳ rà soát index không được `EXPLAIN` sử dụng (Postgres có `pg_stat_user_indexes`) để dọn dẹp.
- **Composite index đúng thứ tự cột mới có tác dụng:** index `(user_id, created_at)` dùng tốt cho `WHERE user_id = ? ORDER BY created_at`, nhưng **không** tối ưu cho query chỉ lọc theo `created_at` một mình — đây là bẫy rất hay gặp khi query pattern thay đổi mà không cập nhật lại index.

---

## 3. Transaction & Locking — sự cố "deadlock" giữa đêm

```sql
-- Kịch bản thật gây deadlock: 2 transaction khóa 2 bảng theo THỨ TỰ NGƯỢC NHAU
-- Transaction A: UPDATE accounts SET ... WHERE id=1;  rồi UPDATE orders SET ... WHERE id=5;
-- Transaction B: UPDATE orders SET ... WHERE id=5;    rồi UPDATE accounts SET ... WHERE id=1;
-- → A chờ B nhả khóa orders, B chờ A nhả khóa accounts → DEADLOCK, DB tự kill 1 transaction
```

**Nguyên tắc senior áp dụng để tránh deadlock:** luôn khóa tài nguyên theo **cùng một thứ tự cố định** (VD: luôn khóa theo `id` tăng dần) trong mọi transaction ở mọi nơi trong codebase — đây là quy tắc kỷ luật team, không phải kỹ thuật code đơn lẻ.

**Isolation Level — tradeoff thật:** `READ COMMITTED` (mặc định Postgres) đủ cho hầu hết ứng dụng CRUD thông thường. `SERIALIZABLE` an toàn tuyệt đối nhưng làm giảm throughput đáng kể vì DB phải retry nhiều transaction xung đột — chỉ dùng khi nghiệp vụ cực kỳ nhạy cảm (giao dịch tài chính, đặt vé số lượng giới hạn).

---

## 4. Scaling thật: Replication trước, Sharding là phương án cuối cùng

Thứ tự senior thường áp dụng khi hệ thống quá tải DB (theo mức độ phức tạp tăng dần):

1. **Tối ưu query + đúng index** (rẻ nhất, hiệu quả nhất, luôn làm trước).
2. **Thêm cache layer (Redis)** trước các query đọc lặp lại nhiều (giảm tải DB mà không cần đổi kiến trúc).
3. **Read Replica:** tách các query `SELECT` báo cáo/dashboard sang bản sao chỉ đọc, giữ DB chính cho ghi — giải quyết được phần lớn use case đọc nhiều.
4. **Connection pooler (PgBouncer)** — xem [`01-Request-Lifecycle-And-Architecture`](../01-Request-Lifecycle-And-Architecture/README.md).
5. **Partitioning** (chia bảng lớn theo thời gian/khu vực trong cùng 1 DB) — vẫn còn 1 DB, quản lý đơn giản hơn sharding.
6. **Sharding** (chia dữ liệu ra NHIỀU DB server vật lý) — **phương án cuối cùng**, vì làm mất khả năng JOIN/transaction xuyên shard, độ phức tạp vận hành tăng vọt. Senior luôn cân nhắc kỹ trước khi đi tới bước này — rất nhiều công ty "sharding sớm" rồi hối hận vì độ phức tạp vượt xa lợi ích thật nhận được ở quy mô của họ.

---

## 🎯 Câu hỏi senior hay hỏi khi review

1. "Bạn chọn Mongo/Postgres cho service này dựa trên tiêu chí gì — hay chỉ vì quen tay?"
2. "2 transaction này có thể deadlock không? Thứ tự khóa tài nguyên có nhất quán trong toàn bộ codebase không?"
3. "Trước khi nghĩ tới sharding, bạn đã thử cache + read replica + tối ưu index chưa?"

## 🔗 Liên kết module khác
- B-Tree index là ứng dụng trực tiếp của cấu trúc cây → [`DSA-Mastery/03`](../../DSA-Mastery/03-Trees-Heaps-Tries/README.md)
- Connection pool ảnh hưởng bởi tầng request phía trên → [`01-Request-Lifecycle-And-Architecture`](../01-Request-Lifecycle-And-Architecture/README.md)
- Giám sát query chậm bằng công cụ thật → [`04-Testing-Observability-And-Debugging-Prod`](../04-Testing-Observability-And-Debugging-Prod/README.md)
