# 🐍 PYTHON CORE MASTERY: TỪ ZER0 ĐẾN HERO (CƠ BẢN - NÂNG CAO)

Tài liệu này tập trung vào ngôn ngữ Python thuần (Core). Hiểu sâu ngôn ngữ là điều kiện tiên quyết để trở thành một Senior sử dụng thành thạo mọi Framework.

---

## 📋 MỤC LỤC
1. [**CƠ BẢN: CÚ PHÁP VÀ KIỂU DỮ LIỆU TỐI ƯU**](#1-cơ-bản-cú-pháp-và-kiểu-dữ-liệu-tối-ưu)
2. [**TRUNG CẤP: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (OOP) VÀ DECORATORS**](#2-trung-cấp-lập-trình-hướng-đối-tượng-oop-và-decorators)
3. [**NÂNG CAO: ASYNCIO, METACLASS VÀ QUẢN LÝ BỘ NHỚ**](#3-nâng-cao-asyncio-metaclass-và-quản-lý-bộ-nhớ)
4. [**PHƯƠNG THỨC MA THUẬT: MAGIC METHODS (DUNDER)**](#4-phương-thức-ma-thuật-magic-methods-dunder)

---

## 🟢 1. CƠ BẢN: CÚ PHÁP VÀ KIỂU DỮ LIỆU TỐI ƯU

### 📦 A. List, Dict, Set Comprehension
Cách viết code "chuẩn Python" (Pythonic) để thay thế vòng lặp `for` dài dòng:
```python
# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]
```

### 🧱 B. Unpacking và *args, **kwargs
Linh hoạt trong việc truyền tham số vào hàm, giúp bạn viết các hàm có thể nhận số lượng đối số tùy biến.

---

## 🟡 2. TRUNG CẤP: OOP VÀ DECORATORS

### 🧬 A. Lập trình hướng đối tượng (OOP)
- **Inheritance (Kế thừa):** Tái sử dụng code.
- **Mixins:** Kỹ thuật Senior để thêm tính năng vào Class mà không làm rối cấu trúc kế thừa chính.
- **@property:** Biến một hàm thành một thuộc tính để truy cập trơn chu hơn.

### 🎨 B. Decorators (Cực kỳ quan trọng)
Dùng để "bọc" các hàm khác để thêm logic (vd: kiểm tra log, đo thời gian chạy, kiểm tra quyền) mà không làm thay đổi code gốc của hàm đó.

### 🚪 C. Context Managers (`with` statement)
Tự động quản lý tài nguyên (vd: mở file, kết nối DB) để đảm bảo tài nguyên luôn được đóng đúng cách, tránh rò rỉ bộ nhớ.

---

## 🔴 3. NÂNG CAO: ASYNCIO VÀ METACLASS

### 🚀 A. AsyncIO (Xử lý bất đồng bộ)
Sử dụng `async` và `await`. Đây là chìa khóa để Python có thể xử lý hàng chục nghìn kết nối cùng lúc mà không cần dùng quá nhiều CPU/RAM.

### 🧩 B. Metaclasses
"Class của các Class". Dùng để can thiệp vào cách một Class được khởi tạo. Đây là công nghệ đứng sau các ORM của Django/Flask.

### 🧹 C. Memory Management & GIL
- **GIL (Global Interpreter Lock):** Hiểu tại sao Python đa luồng (multi-threading) đôi khi lại chậm hơn đơn luồng.
- **Garbage Collection (GC):** Cách Python tự động dọn dẹp biến cũ để giải phóng RAM.

---

## 🧙 4. CÁC PHƯƠNG THỨC MA THUẬT (MAGIC METHODS)

Các hàm bắt đầu và kết thúc bằng `__`:
- `__init__`: Khởi tạo object.
- `__call__`: Làm cho object có thể gọi được như một hàm.
- `__str__` & `__repr__`: Định nghĩa cách hiển thị object dưới dạng chuỗi.
- `__getitem__`: Giúp object có thể truy cập bằng `[]` như một List/Dict.

---
🚀 **Triết lý Python:** Beautiful is better than ugly. Explicit is better than implicit. Hãy viết code sạch, bạn sẽ thành công!
