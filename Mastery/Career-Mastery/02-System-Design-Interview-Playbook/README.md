# 02. System Design Interview — Khung Trả Lời Dùng Được Cho Mọi Đề Bài

> Đây là nơi **toàn bộ kiến thức trong 3 cây trước hội tụ lại**: DSA-Mastery (cấu trúc dữ liệu), Backend-Mastery (kiến trúc backend), Cloud-DevOps-Mastery (hạ tầng) — system design chính là bài toán tổng hợp cả 3.

---

## 1. Khung 5 bước — dùng cho MỌI đề bài system design

```
1. LÀM RÕ YÊU CẦU (Requirements Clarification) — 5 phút
   - Functional: hệ thống làm gì? (VD: rút gọn URL, chat real-time, feed tin tức)
   - Non-functional: bao nhiêu user? Bao nhiêu request/giây? Ưu tiên consistency hay availability?

2. ƯỚC LƯỢNG QUY MÔ (Back-of-envelope Estimation) — 5 phút
   - QPS (query per second), dung lượng lưu trữ/năm, băng thông
   - Đây là bước junior hay bỏ qua nhưng senior LUÔN làm — vì nó quyết định toàn bộ lựa chọn phía sau
     (100 user thì SQLite cũng chạy được; 100 triệu user thì kiến trúc hoàn toàn khác)

3. THIẾT KẾ TỔNG QUAN (High-level Design) — 10 phút
   - Vẽ sơ đồ: Client → LB → Service → DB/Cache — dùng đúng khối kiến thức từ Backend-Mastery Module 01

4. ĐÀO SÂU (Deep Dive) — 15-20 phút
   - Chọn 1-2 điểm khó nhất để đào sâu: database schema, cách chống race condition,
     cách scale phần bottleneck nhất (dùng Backend-Mastery Module 03, DSA-Mastery)

5. XÁC ĐỊNH ĐIỂM YẾU & CẢI THIỆN (Trade-offs & Bottlenecks) — 5 phút
   - Chủ động chỉ ra điểm yếu của thiết kế mình vừa đưa ra — đây là dấu hiệu senior thật sự,
     junior thường chỉ trình bày thiết kế mà không tự phản biện
```

**Sai lầm phổ biến nhất khi luyện tập:** nhảy thẳng vào vẽ kiến trúc phức tạp (microservices, Kafka, sharding) ngay từ đầu mà **chưa làm rõ quy mô thật của bài toán**. Đề bài "thiết kế Twitter" cho 1000 user và cho 1 tỷ user có đáp án hoàn toàn khác nhau — kỹ năng đầu tiên senior thể hiện là **hỏi đúng câu hỏi trước khi thiết kế**, không phải "biết nhiều buzzword".

---

## 2. Bộ câu hỏi làm rõ yêu cầu — dùng lại được cho hầu hết đề bài

- "Hệ thống cần đọc nhiều hơn hay ghi nhiều hơn?" → quyết định SQL vs NoSQL, có cần cache mạnh không (liên kết [`Backend-Mastery/03`](../../Backend-Mastery/03-Database-Choice-And-Scaling-Playbook/README.md)).
- "Dữ liệu cần chính xác tuyệt đối (strong consistency) hay có thể trễ vài giây (eventual consistency) chấp nhận được?" → VD: số dư tài khoản cần strong consistency; số lượt like bài viết chấp nhận eventual consistency.
- "Có cần real-time không, hay có thể xử lý theo batch (định kỳ)?" → quyết định có cần WebSocket/message queue hay chỉ cần cron job.
- "Traffic có tăng đột biến theo sự kiện không (flash sale, viral content)?" → ảnh hưởng thiết kế auto-scaling, rate limiting (liên kết [`Cloud-DevOps-Mastery/02`](../../Cloud-DevOps-Mastery/02-Compute-Choices-EC2-Lambda-Containers/README.md)).

---

## 3. Bản đồ: đề bài kinh điển → kiến thức cần dùng trong repo này

| Đề bài kinh điển | Kiến thức chính cần dùng |
|---|---|
| Thiết kế URL Shortener | Hash Table (encode/decode) → [`DSA-Mastery/02`](../../DSA-Mastery/02-Linear-Structures-And-Hashing/README.md); chọn DB đọc nhiều → [`Backend-Mastery/03`](../../Backend-Mastery/03-Database-Choice-And-Scaling-Playbook/README.md) |
| Thiết kế Rate Limiter | Sliding Window + Hash Table → [`DSA-Mastery/02`](../../DSA-Mastery/02-Linear-Structures-And-Hashing/README.md), [`06`](../../DSA-Mastery/06-Advanced-Patterns/README.md) |
| Thiết kế News Feed / Social Media | Graph (quan hệ follow) → [`DSA-Mastery/04`](../../DSA-Mastery/04-Graphs-And-Union-Find/README.md); Queue cho fan-out → [`DSA-Mastery/02`](../../DSA-Mastery/02-Linear-Structures-And-Hashing/README.md) |
| Thiết kế Autocomplete/Search | Trie → [`DSA-Mastery/03`](../../DSA-Mastery/03-Trees-Heaps-Tries/README.md) |
| Thiết kế Hệ thống đặt vé/Chống overselling | Transaction & Locking → [`Backend-Mastery/03`](../../Backend-Mastery/03-Database-Choice-And-Scaling-Playbook/README.md) |
| Thiết kế Hệ thống thông báo (Notification) | Queue, retry, idempotency → [`Backend-Mastery/02`](../../Backend-Mastery/02-Concurrency-And-Async-In-Production/README.md) |
| Thiết kế hệ thống chịu tải cao, nhiều region | Compute/Container/Auto-scaling → [`Cloud-DevOps-Mastery/02-03`](../../Cloud-DevOps-Mastery/02-Compute-Choices-EC2-Lambda-Containers/README.md) |

**Cách luyện tập hiệu quả:** chọn 1 đề bài/tuần, tự làm đủ 5 bước ở trên trong 45 phút (đúng thời gian phỏng vấn thật), sau đó tra cứu bảng trên để kiểm tra mình có bỏ sót khối kiến thức quan trọng nào không.

---

## 🎯 Checklist tự đánh giá sau mỗi lần luyện tập

1. Mình có ước lượng quy mô (QPS, dung lượng) trước khi thiết kế không, hay nhảy thẳng vào vẽ sơ đồ?
2. Mình có tự chỉ ra được điểm yếu/bottleneck của chính thiết kế mình đưa ra không?
3. Mình có giải thích được TẠI SAO chọn công nghệ này thay vì công nghệ khác (không chỉ liệt kê tên) không?

## 🔗 Liên kết module khác
- Mindset đứng sau cách trả lời → [`01-Senior-Mindset-And-Career-Reality`](../01-Senior-Mindset-And-Career-Reality/README.md)
- Câu hỏi kỹ thuật chi tiết theo từng mảng công nghệ → [`03-Technical-Interview-Strategy-By-Stack`](../03-Technical-Interview-Strategy-By-Stack/README.md)
