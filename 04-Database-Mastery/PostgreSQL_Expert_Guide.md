# 🐘 POSTGRESQL & SQL EXPERT: LÀM CHỦ LINH HỒN CỦA HỆ THỐNG BACKEND

Database là nơi lưu giữ tài sản quý giá nhất của doanh nghiệp: **Dữ liệu**. Một Senior Backend giỏi phải là một Master SQL.

---

## 📋 MỤC LỤC
1. [**CƠ BẢN: CẤU TRÚC VÀ RÀNG BUỘC (CONSTRAINTS)**](#1-cơ-bản-cấu-trúc-và-ràng-buộc-constraints)
2. [**TRUNG CẤP: INDEXING VÀ SEARCH TỐI ƯU**](#2-trung-cấp-indexing-và-search-tối-ưu)
3. [**NÂNG CAO: TRANSACTION, LOCKING VÀ CONCURRENCY**](#3-nâng-cao-transaction-locking-và-concurrency)
4. [**TỐI ƯU HÓA: EXPLAIN ANALYZE VÀ QUERY TUNING**](#4-tối-ưu-hóa-explain-analyze-và-query-tuning)
5. [**KIẾN TRÚC LỚN: PARTITIONING VÀ REPLICATION**](#5-kiến-trúc-lớn-partitioning-và-replication)

---

## 🟢 1. CƠ BẢN: CẤU TRÚC VÀ RÀNG BUỘC (CONSTRAINTS)

### 🧱 A. Chuẩn hóa dữ liệu (Normalization)
- **1NF, 2NF, 3NF:** Đảm bảo không có dữ liệu dư thừa.
- **Problem:** Khi nào nên "Phi chuẩn hóa" (Denormalization)? Senior chấp nhận dư thừa dữ liệu ở một số bảng để tăng tốc độ Đọc (Read) cho các báo cáo khổng lồ.

### ⛓️ B. Ràng buộc (Constraints)
- **Primary Key / Foreign Key:** Xương sống của quan hệ dữ liệu.
- **Check Constraint:** Ví dụ: `CHECK (age > 18)`. Giúp Logic nghiệp vụ được bảo vệ ngay từ tầng Database, cực kỳ an toàn.
- **Unique Constraint:** Đảm bảo không trùng lặp (vd: Email người dùng).

---

## 🟡 2. TRUNG CẤP: INDEXING VÀ SEARCH TỐI ƯU

### 📚 A. Các loại Index trong PostgreSQL
- **B-Tree:** Mặc định và phổ biến nhất, dùng cho `=` và `>`, `<`.
- **GIN (Generalized Inverted Index):** Chìa khóa để tìm kiếm **Full Text Search** và dữ liệu JSONB cực nhanh.
- **BRIN:** Dùng cho các bảng khổng lồ (hàng tỷ dòng) được sắp xếp theo thời gian.

### 🔍 B. Full Text Search (FTS)
Thay vì dùng `LIKE '%keyword%'` (rất chậm), Senior dùng `tsvector` và `tsquery` của Postgres để tìm kiếm từ khóa trong tích tắc.

---

## 🔴 3. NÂNG CAO: TRANSACTION, LOCKING VÀ CONCURRENCY

### 🔄 A. ACID Properties
- **Atomicity, Consistency, Isolation, Durability:** 4 cột trụ đảm bảo giao dịch (Transaction) không bao giờ bị sai lệch.

### 🔒 B. Locking (Khóa dữ liệu)
- **Row-level Lock:** Khóa 1 dòng.
- **Table-level Lock:** Khóa cả bảng (rất nguy hiểm, dễ gây treo hệ thống).
- **Deadlock:** Khi 2 tiến trình đợi nhau mở khóa. Senior luôn thiết kế để truy cập dữ liệu theo một thứ tự nhất định nhằm tránh Deadlock.

---

## 🚀 4. TỐI ƯU HÓA: EXPLAIN ANALYZE VÀ QUERY TUNING

### 🔬 A. Đọc kế hoạch thực thi (Execution Plan)
Dùng lệnh `EXPLAIN (ANALYZE, BUFFERS) select ...`.
- **Seq Scan:** Quét toàn bảng (Chậm - Cần thêm Index).
- **Index Scan:** Tìm qua Index (Nhanh).
- **Bitmap Index Scan:** Kết hợp nhiều Index.

### ⚙️ B. Query Tuning
- Sử dụng **Common Table Expressions (CTE)** bằng từ khóa `WITH` để code SQL sạch và dễ đọc hơn.
- Tránh dùng `IN` với danh sách quá lớn, hãy dùng `EXISTS` hoặc `JOIN`.

---

## 🏢 5. KIẾN TRÚC LỚN: PARTITIONING VÀ REPLICATION

### 📦 A. Table Partitioning (Chia nhỏ bảng)
Chia một bảng 1 tỷ dòng thành 12 bảng nhỏ theo tháng (vd: `orders_2023_01`, `orders_2023_02`). Giúp việc truy vấn tháng hiện tại cực nhanh vì Postgres không cần quét 11 tháng còn lại.

### 👯 B. Replication (Sao chép)
- **Master-Slave:** Server Master để Ghi, các server Slave để Đọc. Đây là bí quyết giúp các hệ thống lớn chịu tải hàng triệu người dùng cùng lúc.

---
🚀 **Triết lý Database:** SQL không chỉ là ngôn ngữ, nó là nghệ thuật sắp xếp dữ liệu. Hãy hiểu cách Database "nghĩ", bạn sẽ làm chủ nó!
