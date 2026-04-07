# 📚 PYTHON STANDARD LIBRARY: DANH MỤC "VŨ KHÍ" CÓ SẴN (BUILT-IN)

Python nổi tiếng với triết lý "Batteries Included". Đây là danh sách những Module và Hàm quan trọng nhất mà một Senior phải thuộc lòng để không phải "phát minh lại cái bánh xe".

---

## 📋 MỤC LỤC
1. [**CÁC HÀM CƠ BẢN (BUILT-IN FUNCTIONS)**](#1-các-hàm-cơ-bản-built-in-functions)
2. [**XỬ LÝ DỮ LIỆU (DATA PROCESSING)**](#2-xử-lý-dữ-liệu-data-processing)
3. [**HỆ THỐNG VÀ FILE (OS & FILESYSTEM)**](#3-hệ-thống-và-file-os--filesystem)
4. [**ĐA NHIỆM VÀ HIỆU NĂNG (CONCURRENCY & PERFORMANCE)**](#4-đa-nhiệm-và-hiệu-năng-concurrency--performance)
5. [**DEBUGGING VÀ KIỂM THỬ (DEBUG & TEST)**](#5-debugging-và-kiểm-thử-debug--test)

---

## 🟢 1. CÁC HÀM CƠ BẢN (BUILT-IN FUNCTIONS)

Đây là những hàm bạn gọi trực tiếp mà không cần `import`:

- **`len()`**: Độ dài chuỗi/danh sách.
- **`any()` & `all()`**: Kiểm tra xem có bất kỳ (any) hoặc tất cả (all) phần tử nào thỏa mãn điều kiện không.
- **`map()` & `filter()`**: Áp dụng hàm lên danh sách hoặc lọc danh sách theo điều kiện.
- **`sorted()`**: Sắp xếp dữ liệu (Hỗ trợ tham số `key` cực kỳ mạnh mẽ).
- **`zip()`**: Kết hợp nhiều danh sách lại thành các cặp.
- **`enumerate()`**: Duyệt danh sách kèm theo số thứ tự (Index).
- **`isinstance(obj, type)`**: Kiểm tra đối tượng có thuộc kiểu dữ liệu nào đó không (Tốt hơn dùng `type()`).
- **`id(obj)`**: Trả về địa chỉ bộ nhớ của đối tượng (Dùng để debug rò rỉ bộ nhớ).
- **`getattr()`, `setattr()`, `hasattr()`**: Thao tác với thuộc tính của đối tượng một cách linh hoạt (Dynamic attributes).
- **`max()`, `min()`, `sum()`, `round()`**: Các hàm toán học cơ bản cực kỳ nhanh.
- **`dir(obj)`**: Liệt kê mọi thuộc tính và phương thức mà một đối tượng sở hữu.
- **`help(obj)`**: Xem tài liệu hướng dẫn trực tiếp trong terminal cho bất kỳ hàm/class nào.

---

## 🟡 2. XỬ LÝ DỮ LIỆU (DATA PROCESSING)

- **`json`**: Chuyển đổi giữa Dictionary Python và chuỗi JSON (Cực quan trọng cho API).
- **`collections`**: Cung cấp các kiểu dữ liệu nâng cao như `deque`, `namedtuple`, `Counter`.
- **`itertools`**: Các công cụ lặp cực nhanh (vd: `product`, `permutations`, `cycle`).
- **`datetime`**: Xử lý ngày tháng, múi giờ.
- **`re`**: Làm chủ biểu thức chính quy (Regular Expressions) để tìm kiếm chuỗi phức tạp.
- **`uuid`**: Tạo định danh duy nhất (UUID) không bao giờ trùng lặp (Dùng làm ID cho Database).
- **`random` & `secrets`**: Tạo số ngẫu nhiên. `secrets` dùng cho bảo mật (mật khẩu, token).
- **`hashlib` & `hmac`**: Mã hóa dữ liệu (MD5, SHA256) và xác thực chữ ký số.
- **`base64`**: Mã hóa dữ liệu nhị phân (ảnh, file) sang dạng chuỗi để truyền qua API.
- **`math` & `statistics`**: Các hàm toán học và thống kê chuyên sâu.

---

## 🔴 3. HỆ THỐNG VÀ FILE (OS & FILESYSTEM)

- **`os`**: Tương tác với hệ điều hành (đọc biến môi trường, tạo thư mục).
- **`sys`**: Truy cập tham số dòng lệnh (`sys.argv`) và quản lý hệ thống Python.
- **`pathlib`**: (Khuyên dùng thay `os.path`) Cung cấp cách thức xử lý đường dẫn file theo hướng đối tượng cực kỳ sạch sẽ.
- **`shutil`**: Copy, di chuyển, xóa toàn bộ thư mục một cách dễ dàng.
- **`glob`**: Tìm kiếm file theo mẫu (vd: Tìm tất cả file `.jpg` trong thư mục).
- **`tempfile`**: Tạo các tệp tin và thư mục tạm thời, tự động xóa sau khi dùng xong.
- **`configparser`**: Đọc các tệp cấu hình `.ini` cho ứng dụng.

---

## 🚀 4. ĐA NHIỆM VÀ HIỆU NĂNG (CONCURRENCY)

- **`threading`**: Đa luồng cho các tác vụ tốn thời gian chờ (I/O Bound).
- **`multiprocessing`**: Đa tiến trình cho các tác vụ tốn CPU (CPU Bound).
- **`asyncio`**: Xử lý bất đồng bộ quy mô lớn (Single-threaded Concurrency).
- **`concurrent.futures`**: Cung cấp `ThreadPoolExecutor` và `ProcessPoolExecutor` để quản lý các luồng dễ dàng.

---

## 🛠️ 5. DEBUGGING VÀ KIỂM THỬ (DEBUG & TEST)

- **`logging`**: Tiêu chuẩn để ghi lại nhật ký hoạt động của ứng dụng (Senior không dùng `print`).
- **`unittest`**: Bộ công cụ viết Unit Test có sẵn.
- **`pdb`**: Công cụ Debug dòng lệnh (Cực hữu dụng khi không dùng được IDE).
- **`cProfile`**: Đo lường hiệu năng của từng dòng code để tìm chỗ gây chậm hệ thống.
- **`typing`**: Bộ công cụ định nghĩa kiểu dữ liệu (Type Hints) giúp code sạch và tránh lỗi (vd: `List`, `Dict`, `Optional`).
- **`inspect`**: Giúp bạn xem mã nguồn của bất kỳ hàm nào đang chạy, lấy các tham số của hàm (Cực hữu dụng khi viết Decorator).
- **`enum`**: Tạo các tập hằng số (Enum) chuyên nghiệp, dễ quản lý hơn là dùng chuỗi văn bản.
- **`abc`**: (Abstract Base Classes) Định nghĩa các lớp trừu tượng, buộc các lớp con phải triển khai các hàm nhất định.
- **`bisect` & `heapq`**: Các thuật toán và cấu trúc dữ liệu tối ưu (Binary search, Heap queue) cho hiệu năng siêu cao.

---

## ⚡ 6. TỔNG KẾT SỐ LƯỢNG HÀM & MODULE QUAN TRỌNG

| Nhóm chức năng | Số lượng module then chốt | Mục đích tối thượng |
| :--- | :---: | :--- |
| **Cơ bản (Built-in)** | ~15 hàm | Thao tác dữ liệu nhanh, kiểm tra đối tượng. |
| **Xử lý dữ liệu** | ~10 module | JSON, Datetime, Regex, Collections. |
| **Hệ thống & File** | ~8 module | OS, Pathlib, Shutil, Glob. |
| **Hiệu năng & Luồng** | ~5 module | AsyncIO, Threading, Multiprocessing. |
| **Bảo mật & Mã hóa** | ~5 module | Secrets, Hashlib, UUID, Base64. |
| **Kiểm thử & Debug** | ~6 module | Unittest, Logging, PDB, CProfile, Typing. |

---
🚀 **Triết lý Master:** Có khoảng 50+ hàm và module trong Standard Library mà bạn nên sử dụng thành thạo. Khi đã làm chủ chúng, bạn sẽ thấy mình code nhanh hơn và chuyên nghiệp hơn 80% các lập trình viên khác!
