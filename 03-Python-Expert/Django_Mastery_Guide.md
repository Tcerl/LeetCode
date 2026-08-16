# 🎸 DJANGO MASTERY: GIẢI THÍCH CHI TIẾT TỪ CƠ BẢN ĐẾN CAO CẤP (FULL GUIDE)

Django là framework "pin sạc sẵn" (batteries-included). Nó cung cấp hầu hết các công cụ mạnh mẽ nhất bạn cần cho dự án Web chuyên nghiệp.

---

## 📋 MỤC LỤC
1. [**CƠ BẢN: BỘ KHUNG M-V-T VÀ ORM**](#1-cơ-bản-bộ-khung-m-v-t-và-orm)
2. [**TRUNG CẤP: RESTFUL API VÀ TỐI ƯU HÓA**](#2-trung-cấp-restful-api-và-tối-ưu-hóa)
3. [**NÂNG CAO: HỆ THỐNG LỚN VÀ PHỨC TẠP**](#3-nâng-cao-hệ-thống-lớn-và-phức-tạp)
4. [**⭐ TRƯỜNG HỢP SỬ DỤNG ĐẶC TRƯNG CỦA DJANGO**](#-trường-hợp-sử-dụng-đặc-trưng-của-django)
5. [**⚠️ THỬ THÁCH THỰC TẾ & GIẢI PHÁP**](#️-thử-thách-thực-tế--giải-pháp)
6. [**💡 SENIOR'S KNOWLEDGE: KINH NGHIỆM THỰC CHIẾN**](#-seniors-knowledge-kinh-nghiệm-thực-chiến)
7. [**🛡️ SECURITY & VULNERABILITY FIXES: BẢO MẬT HỆ THỐNG**](#️-security--vulnerability-fixes-bảo-mật-hệ-thống)
8. [**🗄️ DATABASE INTERACTION: TƯƠNG TÁC CƠ SỞ DỮ LIỆU**](#️-database-interaction-tương-tác-cơ-sở-dữ-liệu)
9. [**🚀 SQL OPTIMIZATION: TỐI ƯU HÓA TRUY VẤN**](#-sql-optimization-tối-ưu-hóa-truy-vấn)

---

## 🟢 1. CƠ BẢN: BỘ KHUNG M-V-T VÀ ORM

### 🏗️ A. MVT (Model-View-Template)
Logic tổ chức code: **Model** là dữ liệu, **View** là điều hướng/xử lý, **Template** là giao diện HTML.

### 🐘 B. Django ORM (Database Pro)
Truy vấn Database bằng Python. Hỗ trợ đầy đủ quan hệ **ForeignKey**, **OneToOne**, **ManyToMany**.

### 🛠️ C. Django Admin
Trang quản trị "thần thánh" giúp quản lý dữ liệu CMS ngay lập tức mà không tốn 1 dòng code UI nào.

---

## 🟡 2. TRUNG CẤP: RESTFUL API VÀ TỐI ƯU HÓA

### 📡 A. DRF (Django REST Framework)
Công cụ tốt nhất để làm API JSON cho Vue/React. Sử dụng **Serializers** để biến Object Python thành chuỗi JSON.

### ⚡ B. QuerySet Optimization (Senior Skill)
Khắc phục lỗi **N+1 Query** bằng cách dùng `select_related()` (cho ForeignKey) và `prefetch_related()` (cho ManyToMany).

### 🏷️ C. Custom User Model
Bí kíp sống còn: Luôn tạo User model riêng từ đầu dự án kế thừa từ `AbstractUser` để dễ mở rộng.

---

## 🔴 3. NÂNG CAO: HỆ THỐNG LỚN VÀ PHỨC TẠP

### 📡 A. Signals & Middleware
**Signals** (Lắng nghe sự kiện) và **Middleware** (Bộ lọc cổng vào) giúp quản lý logic toàn hệ thống tập trung.

### 💬 B. WebSocket & Django Channels
Xử lý Chat, Thông báo đẩy thời gian thực (Real-time) cho hàng ngàn người dùng cùng lúc.

### 🏢 C. Multi-tenancy & Scalability
Cấu hình SaaS một ứng dụng nhiều công ty. Tối ưu hiệu năng bằng **Redis Caching** và **Celery Backend Workers**.

---

## ⭐ 4. TRƯỜNG HỢP SỬ DỤNG ĐẶC TRƯNG CỦA DJANGO
1.  **Hệ thống Content Management (CMS):** Xử lý hàng triệu bài viết cho các trang báo lớn.
2.  **E-commerce:** Quản lý đơn hàng và thanh toán an toàn tuyệt đối.
3.  **Hệ thống SaaS phức tạp:** Khi có quan hệ hàng trăm bảng dữ liệu chằng chịt.

---

## ⚠️ 5. THỬ THÁCH THỰC TẾ & GIẢI PHÁP
- **Xung đột Migration:** Khắc phục bằng `--merge` hoặc quản lý tập trung trong team.
- **Admin bị chậm:** Tắt bộ đếm bản ghi (`show_full_result_count = False`) khi database quá lớn.
- **CORS Errors:** Cấu hình `django-cors-headers` cho frontend.

---

## 💡 SENIOR'S KNOWLEDGE: KINH NGHIỆM THỰC CHIẾN
- **Squash Migrations:** Nén hàng trăm file cũ để dọn dẹp hệ thống.
- **Fat Models vs Thin Views:** Đẩy logic nghiệp vụ vào Model hoặc Manager để tái sử dụng tối đa.
- **Tùy biến Admin:** Dùng Inlines, Actions, Custom Forms thay vì viết Dashboard mới từ đầu.

---

## 🛡️ 7. SECURITY & VULNERABILITY FIXES
- **Raw SQL Injection:** Không cộng chuỗi SQL, luôn truyền tham số `params=[...]`.
- **Debug on Prod:** Luôn đặt `DEBUG = False` và dùng lệnh `check --deploy`.
- **Phân quyền IDOR:** Luôn lọc dữ liệu theo `request.user` để chống người dùng xem trộm dữ liệu nhau.

---

## 🗄️ 8. DATABASE INTERACTION: TƯƠNG TÁC DB
- **Lazy Evaluation:** Hệ thống chỉ truy vấn SQL khi bạn thực sự "chạm" vào dữ liệu (tiết kiệm tài nguyên).
- **Transactions:** Dùng `ATOMIC_REQUESTS` để đảm bảo lỗi ở đâu, phục hồi (rollback) ở đó.
- **Database Routers:** Chia tải (Read/Write splitting) cho server Database.

---

## 🚀 9. SQL OPTIMIZATION: TỐI ƯU HÓA TRUY VẤN

Django ORM rất tiện lợi nhưng dễ làm phát sinh các truy vấn kém hiệu quả nếu không biết cách tối ưu:

1.  **Dùng `only()` và `defer()`:** 
    - `only('name', 'email')`: Chỉ lấy 2 cột này từ DB.
    - `defer('content')`: Lấy tất cả trừ cột 'content' (thường dùng cho các cột text/blob siêu nặng).
2.  **Sử dụng `iterator()`:** Khi cần xử lý hàng triệu bản ghi (vd: Export CSV), dùng `.iterator()` để Django không tải toàn bộ dữ liệu vào RAM một lúc, giúp tránh lỗi `MemoryError`.
3.  **Kiểm tra SQL bằng `explain()`:** Django hỗ trợ phương thức `.explain()` trên QuerySet. Nó sẽ trả về kế hoạch thực thi của Database (Execution Plan), giúp bạn biết câu lệnh có đang dùng Index hay không.
4.  **Database Indexing cấp cao:** Sử dụng `Meta.indexes` để tạo các composite index (index kết hợp nhiều cột) cho các yêu cầu lọc phức tạp.
5.  **Tránh đếm dữ liệu thừa:** Thay vì `len(queryset)`, hãy dùng `queryset.count()`. Thay vì `if queryset:`, hãy dùng `queryset.exists()`. Các phương thức này chạy lệnh `COUNT` hoặc `EXISTS` tối ưu trên Database thay vì tải dữ liệu về Python.
