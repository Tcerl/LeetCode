# 🍃 MONGODB EXPERT: LÀM CHỦ NOSQL VÀ CƠ SỞ DỮ LIỆU DẠNG TÀI LIỆU (DOCUMENT-BASED)

MongoDB là "Vua" của thế giới NoSQL. Nó linh hoạt, mở rộng cực nhanh và cực kỳ phù hợp cho các dữ liệu không có cấu trúc cố định hoặc thay đổi liên tục.

---

## 📋 MỤC LỤC
1. [**CƠ BẢN: JSON, BSON VÀ SCHEMA-LESS**](#1-cơ-bản-json-bson-và-schema-less)
2. [**TRUNG CẤP: AGGREGATION PIPELINE (BÍ KÍP XỬ LÝ DỮ LIỆU)**](#2-trung-cấp-aggregation-pipeline-bí-kíp-xử-lý-dữ-liệu)
3. [**NÂNG CAO: INDEXING VÀ CHIẾN LƯỢC LƯU TRỮ (TTL, COMPOUND)**](#3-nâng-cao-indexing-và-chiến-lược-lưu-trữ-ttl-compound)
4. [**KIẾN TRÚC LỚN: REPLICA SETS VÀ SHARDING**](#4-kiến-trúc-lớn-replica-sets-và-sharding)
5. [**⭐ KHI NÀO DÙNG SQL (POSTGRES) VS NOSQL (MONGO)?**](#-khi-nào-dùng-sql-postgres-vs-nosql-mongo)

---

## 🟢 1. CƠ BẢN: JSON, BSON VÀ SCHEMA-LESS

### 📄 A. Document vs Table
- **Document (Tài liệu):** Một bản ghi trong Mongo là một đối tượng JSON (thực tế lưu dưới dạng BSON - Binary JSON).
- **Schema-less:** Bạn có thể thêm bất kỳ trường nào vào một tài liệu mà không cần phải chạy `migration` như SQL. Cực kỳ tiện lợi cho các dự án phát triển nhanh (MVP).

### 🛠️ B. CRUD Cơ bản
- `db.collection.insertOne({name: "mbw25", role: "Expert"})`
- `db.collection.find({name: "mbw25"})`
- `db.collection.updateOne({name: "mbw25"}, {$set: {level: 10}})`

---

## 🟡 2. TRUNG CẤP: AGGREGATION PIPELINE

Đây là "vũ khí tối tân" của Mongo để thay thế các câu lệnh `GROUP BY` và `JOIN` phức tạp trong SQL.

- **$match:** Lọc dữ liệu (giống `WHERE`).
- **$group:** Nhóm dữ liệu và tính toán (Tổng, Trung bình, Đếm).
- **$lookup:** "Fake" một lệnh **JOIN** để kết nối dữ liệu từ 2 Collection khác nhau (vd: Lấy thông tin đơn hàng kèm thông tin khách hàng).
- **$project:** Chỉ lấy các trường cần thiết để giảm tải RAM.

---

## 🔴 3. NÂNG CAO: INDEXING VÀ CHIẾN LƯỢC LƯU TRỮ

### 📚 A. Các loại Index
- **Compound Index:** Index trên nhiều trường để tăng tốc các câu query phức tạp.
- **TTL Index (Time-To-Live):** Tự động xóa tài liệu sau một khoảng thời gian (vd: Xóa mã OTP sau 5 phút). Cực kỳ hữu ích cho Cache/Session.
- **Multikey Index:** Index trên một mảng (Array). Mongo cực mạnh ở điểm này so với SQL.

### 🧩 B. Embedding vs Referencing
- **Embedding:** Lưu dữ liệu con nằm trong dữ liệu cha (vd: Lưu Comment nằm trong Bài viết). Tăng tốc độ đọc 1 lần lấy được tất cả.
- **Referencing:** Lưu ID liên kết (giống Foreign Key). Dùng khi dữ liệu con quá lớn hoặc dùng chung nhiều nơi.

---

## 🚀 4. KIẾN TRÚC LỚN: REPLICA SETS VÀ SHARDING

### 🏘️ A. Replica Sets (Sao chép)
Đảm bảo hệ thống không bao giờ "chết". Nếu Server Primary hỏng, các Server Secondary sẽ tự động bầu ra một Primary mới trong vài giây (**High Availability**).

### 🔪 B. Sharding (Chia nhỏ dữ liệu)
Khi dữ liệu quá lớn (vd: Hàng chục Terabyte), Mongo tự động chia nhỏ dữ liệu ra nhiều server khác nhau. Đây là lý do Mongo đứng vững trước "Big Data".

---

## ⭐ 5. KHI NÀO DÙNG SQL (POSTGRES) VS NOSQL (MONGO)?

| Đặc điểm | PostgreSQL (SQL) | MongoDB (NoSQL) |
| :--- | :--- | :--- |
| **Cấu trúc** | Cố định, chặt chẽ (Schema) | Linh hoạt, tự do (Dynamic) |
| **Giao dịch** | Cực mạnh (ACID hoàn hảo) | Đã hỗ trợ nhưng không phải thế mạnh |
| **Search** | Tốt, ổn định | Cực nhanh trên dữ liệu lớn/Array |
| **Mở rộng** | Theo chiều dọc (Vertical - Tăng RAM/CPU) | Theo chiều ngang (Horizontal - Thêm Server) |
| **Dự án phù hợp** | Tài chính, Kế toán, E-commerce | Logging, Real-time Chat, Dữ liệu mạng xã hội |

---
🚀 **Triết lý MongoDB:** Move fast, Break things. Hãy dùng Mongo khi bạn cần tốc độ và sự linh hoạt tuyệt đối!
