# 🏛️ ODOO MASTERY: GIẢI THÍCH CHI TIẾT TỪ FRAMEWORK ĐẾN HỆ SINH THÁI ERP (FULL GUIDE)

Odoo không chỉ là một web framework, nó là một "Hệ điều hành doanh nghiệp" mạnh mẽ. Tài liệu này giúp bạn làm chủ nó từ A-Z.

---

## 📋 MỤC LỤC
1. [**CƠ BẢN: KIẾN TRÚC VÀ CÁC THÀNH PHẦN (THE ODOO WAY)**](#1-cơ-bản-kiến-trúc-và-các-thành-phần-the-odoo-way)
2. [**TRUNG CẤP: TÙY BIẾN VÀ LOGIC NGHIỆP VỤ (INHERITANCE & API)**](#2-trung-cấp-tùy-biến-và-logic-nghiệp-vụ-inheritance--api)
3. [**NÂNG CAO: HIỆU NĂNG VÀ TÍCH HỢP HỆ THỐNG PHỨC TẠP**](#3-nâng-cao-hiệu-năng-và-tích-hợp-hệ-thống-phức-tạp)
4. [**⭐ TRƯỜNG HỢP SỬ DỤNG ĐẶC TRƯNG CỦA ODOO**](#-trường-hợp-sử-dụng-đặc-trưng-của-odoo)
5. [**⚠️ THỬ THÁCH THỰC TẾ & GIẢI PHÁP**](#️-thử-thách-thực-tế--giải-pháp)
6. [**💡 SENIOR'S KNOWLEDGE: KINH NGHIỆM THỰC CHIẾN**](#-seniors-knowledge-kinh-nghiệm-thực-chiến)
7. [**🛡️ SECURITY & VULNERABILITY FIXES: BẢO MẬT HỆ THỐNG**](#️-security--vulnerability-fixes-bảo-mật-hệ-thống)
8. [**🗄️ DATABASE INTERACTION: TƯƠER-TÁC CƠ SỞ DỮ LIỆU**](#️-database-interaction-tương-tác-cơ-sở-dữ-liệu)
9. [**🚀 SQL OPTIMIZATION: TỐI ƯU HÓA TRUY VẤN**](#-sql-optimization-tối-ưu-hóa-truy-vấn)

---

## 🟢 1. CƠ BẢN: KIẾN TRÚC CÁC THÀNH PHẦN

### 🧱 A. Model & Records
Mọi dữ liệu (Sản phẩm, Khách hàng) đều là **Model**. Sử dụng `_name` để định danh và các fields quan hệ `Many2one`, `One2many`, `Many2many`.

### 🖼️ B. XML Views
Vẽ giao diện (Tree, Form, Search) bằng XML. Odoo tự động chuyển đổi chúng sang web app hiện đại.

### 🔐 C. Security (Phân quyền)
Kiểm soát hành động CRUD qua `ir.model.access.csv` và quyền chi tiết theo dòng dữ liệu qua **Record Rules**.

---

## 🟡 2. TRUNG CẤP: TÙY BIẾN VÀ LOGIC NGHIỆP VỤ

### 🧬 A. Inheritance (Kế thừa)
Dùng `_inherit` để mở rộng module Sales/Inventory có sẵn mà không làm hỏng code gốc.

### 🧠 B. Odoo API Decorators
- `@api.depends`: Tính toán trường dữ liệu (vd: Tổng tiền).
- `@api.onchange`: Tự gợi ý dữ liệu khách hàng ngay trên UI.
- `@api.constrains`: Ràng buộc tính hợp lệ của dữ liệu.

### 🧙 C. Wizards & QWeb Reports
Tạo các bảng pop-up tạm thời và thiết kế báo cáo hóa đơn, phiếu kho PDF đẳng cấp.

---

## 🔴 3. NÂNG CAO: HIỆU NĂNG VÀ TÍCH HỢP

### ⛵ A. OWL (Open Wood Library) Framework
Framework JS hiện đại của Odoo (giống React) giúp tùy biến sâu giao diện và dashboards.

### ⚡ B. Performance & SQL Logging
Tối ưu hóa bảng triệu dòng bằng **Indexing** và dùng `self.env.cr.execute()` khi ORM quá chậm.

### 🌐 C. Controllers & External API
Tích hợp web bên ngoài và app mobile qua XML-RPC/JSON-RPC một cách bảo mật.

---

## ⭐ 4. TRƯỜNG HỢP SỬ DỤNG ĐẶC TRƯNG CỦA ODOO
1.  **Quản trị tổng thể ERP:** Kết nối Kế toán, Kho, Nhân sự vào một luồng dữ liệu duy nhất.
2.  **Tùy biến quy trình kinh doanh:** Chế biến module có sẵn cho phù hợp với bệnh viện, trường học.
3.  **Thay thế phần mềm rời rạc:** Thống nhất dữ liệu từ nhiều nguồn về một nơi.

---

## ⚠️ 5. THỬ THÁCH THỰC TẾ & GIẢI PHÁP
- **Xung đột Module:** Sử dụng `super()` để bảo tồn logic gốc.
- **Dependency Hell:** Quản lý file `__manifest__.py` chặt chẽ.
- **Tre hệ thống:** Tối ưu các hàm `@api.depends` tránh tính toán thừa.

---

## 💡 SENIOR'S KNOWLEDGE: KINH NGHIỆM THỰC CHIẾN
- **Độc lập hóa Module:** Thiết kế sao cho module có thể tháo lắp mà không làm sập hệ thống.
- **No-Code First:** Giải quyết bài toán bằng Configuration trước khi mở IDE ra code.
- **Database Maintenance:** Thực hiện `VACUUM` thường xuyên cho Postgres để duy trì tốc độ.

---

## 🛡️ 7. SECURITY & VULNERABILITY FIXES
- **Raw SQL Injection:** Luôn dùng tham số ở đối số thứ 2 của hàm `execute(query, (params,))`.
- **Lách luật sudo():** Hạn chế tối đa dùng `sudo()`, ưu tiên giải quyết qua phân quyền chuẩn.
- **XSS in QWeb:** Luôn dùng `t-esc` cho báo cáo in ấn.

---

## 🗄️ 8. DATABASE INTERACTION: TƯƠNG TÁC DB
- **Recordsets:** Hiểu cách Odoo xử lý dữ liệu theo bộ (List of records).
- **Environment:** Sử dụng `self.env` và `self.env.cr` chuyên nghiệp.
- **Registry & Cache:** Cơ chế lưu đệm dữ liệu trong RAM giúp hệ thống ERP chạy mượt.

---

## 🚀 9. SQL OPTIMIZATION: TỐI ƯU HÓA TRUY VẤN

Odoo làm việc với cơ sở dữ liệu khổng lồ của doanh nghiệp, nên tối ưu hóa là sống còn:

1.  **Tránh gọi ORM trong vòng lặp:** Đây là lỗi phổ biến nhất. Thay vì gọi `record.name` trong vòng lặp `for`, hãy dùng `mapped('name')` hoặc `read(['name'])` để Odoo thực hiện truy vấn hàng loạt (Batch read).
2.  **Tối ưu hóa `search_count()`:** Khi chỉ cần kiểm tra xem có dữ liệu không, hãy dùng `search([], limit=1)` thay vì đếm toàn bộ bảng.
3.  **Sử dụng `flush()` và `invalidate_cache()`:** Khi bạn dùng SQL thuần (`cr.execute`), hãy nhớ gọi `self.flush()` để đẩy dữ liệu từ RAM xuống DB trước khi truy vấn, và `self.invalidate_cache()` sau khi sửa dữ liệu bằng SQL để Odoo cập nhật lại giao diện.
4.  **PostgreSQL partial indexes:** Trong Odoo, bạn có thể định nghĩa index có điều kiện (vd: Chỉ index những đơn hàng có trạng thái 'đang xử lý'). Điều này giúp file index nhỏ gọn và cực kỳ nhanh.
5.  **Bớt dùng Computed Fields không có store:** Các fields `@api.depends` mà không có `store=True` sẽ bị tính toán lại MỖI KHI hiển thị. Senior luôn cân nhắc dùng `store=True` cho các logic phức tạp để tránh làm treo DB.
