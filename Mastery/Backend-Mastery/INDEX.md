# 🌳 Backend-Mastery — Cây Kiến Thức Backend & Database (Senior Companion)

> **Mục đích:** Lớp kiến thức bổ sung cho [`03-Python-Expert/`](../../03-Python-Expert/) và [`04-Database-Mastery/`](../../04-Database-Mastery/) — 2 thư mục đó đã rất chi tiết theo từng công nghệ (Flask/Django/FastAPI, Postgres/Mongo). Cây này **nối các công nghệ đó lại thành 1 luồng hệ thống hoàn chỉnh**, tập trung vào quyết định kiến trúc thật và sự cố production thật.

---

## 📋 MỤC LỤC

| # | Module | Chủ đề | Nguồn lý thuyết liên quan |
|---|---|---|---|
| 01 | [Request Lifecycle & Architecture](01-Request-Lifecycle-And-Architecture/README.md) | Toàn cảnh 1 request từ client tới DB, middleware, N+1 query, connection pool | `Python_Backend_Professional_Guide.md`, `PostgreSQL_Expert_Guide.md` |
| 02 | [Concurrency & Async](02-Concurrency-And-Async-In-Production/README.md) | GIL thật sự là gì, khi nào dùng asyncio/threading/multiprocessing, worker model | `Python_Core_Mastery.md` mục 3 |
| 03 | [Database Choice & Scaling Playbook](03-Database-Choice-And-Scaling-Playbook/README.md) | SQL vs NoSQL, index tradeoff, deadlock, lộ trình scale (cache → replica → shard) | `PostgreSQL_Expert_Guide.md`, `MongoDB_Expert_Guide.md` |
| 04 | [Testing, Observability & Debug Prod](04-Testing-Observability-And-Debugging-Prod/README.md) | Kim tự tháp test, logs/metrics/traces, quy trình debug endpoint chậm, alerting | `Python_Backend_Professional_Guide.md` mục 9 |
| 05 | [Junior-To-Senior Problem Playbook](05-Junior-To-Senior-Problem-Playbook/README.md) | Vấn đề thật + giải pháp, sắp xếp theo cấp độ Junior/Mid/Senior | Tổng hợp Module 01-04 |
| 06 | [Fresher-To-Senior Knowledge & Interview Map](06-Fresher-To-Senior-Knowledge-And-Interview-Map/README.md) | Kiến thức bắt buộc + cách áp dụng thực tế + câu hỏi phỏng vấn thật kèm mẫu trả lời, theo 4 cấp độ Fresher/Junior/Mid/Senior | Tổng hợp Module 01-05 + `04-Interview-Prep/` |
| 07 | [Real-World War Stories Fresher-To-Senior](07-Real-World-War-Stories-Fresher-To-Senior/README.md) | 12 sự cố production kể đầy đủ (bối cảnh → nguyên nhân gốc → cách sửa → bài học), 3 mỗi cấp độ, nguyên liệu STAR cho phỏng vấn | Tổng hợp Module 01-05 + kinh nghiệm thực chiến |

---

## 🗺️ Sơ đồ liên hệ

```
01-Request Lifecycle (bức tranh tổng thể)
        │
        ├──> 02-Concurrency & Async (tối ưu tầng xử lý request)
        │
        └──> 03-Database Scaling (tối ưu tầng lưu trữ)
                    │
                    ▼
        04-Observability & Debug (giám sát + xử lý sự cố toàn bộ luồng trên)
```

## Cách dùng
1. Đọc lý thuyết công nghệ cụ thể ở `03-Python-Expert/` và `04-Database-Mastery/` trước.
2. Đọc cây này để hiểu **cách các công nghệ đó phối hợp thành 1 hệ thống thật**, và các sự cố production kinh điển liên quan.
3. Mỗi module có mục 🎯 câu hỏi senior — dùng để tự đánh giá mức hiểu của bản thân hoặc chuẩn bị phỏng vấn/review.

## 🔗 Liên kết sang các cây khác
- Cấu trúc dữ liệu nền tảng (Hash Table, B-Tree, Queue) → [`../DSA-Mastery/`](../DSA-Mastery/INDEX.md)
- Triển khai backend lên hạ tầng thật (container, CI/CD) → [`../Cloud-DevOps-Mastery/`](../Cloud-DevOps-Mastery/INDEX.md)
- Biến kinh nghiệm sự cố (Module 07) thành bằng chứng tăng lương → [`../Career-Mastery/05`](../Career-Mastery/05-Salary-Growth-Playbook/README.md)
