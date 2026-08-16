# 03. Lộ Trình Vấn Đề Thật: Từ Junior Đến Senior (Tính Toán Khoa Học/Kỹ Thuật)

> Tổng hợp lại các vấn đề đã nhắc ở Module 01-02, kèm tham chiếu [`Du_An_Ca_Nhan.md`](../../06-Exercises/MATLAB/Du_An_Ca_Nhan.md) (dự án kết hợp MATLAB xử lý tín hiệu + Python ML/Dashboard) — sắp xếp theo cấp độ để tự định vị.

---

## 🟢 Cấp độ Junior — "Ra kết quả đúng trên bộ dữ liệu mẫu, chưa hiểu giới hạn của công cụ"

| Vấn đề gặp phải | Vì sao xảy ra | Cách vượt qua | Đọc thêm |
|---|---|---|---|
| Script chạy nhanh với dữ liệu mẫu nhỏ, treo máy với file đo thật (hàng triệu mẫu) | Dùng vòng lặp `for` thay vì vector hóa, chưa preallocate mảng | Học phản xạ vector hóa trước, luôn preallocate mảng lớn | [`01`](../01-Numerical-Computing-Fundamentals/README.md) |
| Vòng lặp kiểm tra hội tụ chạy mãi không dừng | So sánh trực tiếp 2 số thực bằng `==` | Luôn dùng ngưỡng sai số (tolerance) khi so sánh số thực | [`01`](../01-Numerical-Computing-Fundamentals/README.md) |
| Chọn tần số lấy mẫu tùy ý khi thu thập dữ liệu cảm biến | Chưa biết định lý Nyquist, chưa hiểu hậu quả của aliasing | Luôn tính sampling rate dựa trên phổ tần số thực tế cần đo | [`02`](../02-Signal-Processing-ML-In-Practice/README.md) |
| Copy code mẫu OOP (`classdef`) mà chưa hiểu vì sao dùng `Access = private`, `properties (Constant)` | Học theo cú pháp mà chưa hỏi "tại sao đóng gói dữ liệu lại quan trọng" | Với mỗi thuộc tính, tự hỏi "nếu để public thì rủi ro gì" | `03_Nang_Cao.md` |

**Bài học junior cần khắc cốt ghi tâm:** *Công cụ tính toán khoa học (MATLAB/Python) có rất nhiều "phím tắt hiệu năng" (vectorization, preallocation) — không biết chúng thì code vẫn ra đúng kết quả nhưng chậm hơn hàng chục-hàng trăm lần khi dữ liệu thật lớn.*

---

## 🟡 Cấp độ Mid-level — "Biết công cụ mạnh, nhưng chưa cảnh giác với sai số hệ thống"

| Vấn đề gặp phải | Vì sao xảy ra | Cách vượt qua | Đọc thêm |
|---|---|---|---|
| Mô hình ML báo cáo accuracy rất cao trong thử nghiệm, thất bại khi dùng dữ liệu mới | Data leakage — chuẩn hóa/chọn feature trước khi tách train/test | Luôn tách train/test TRƯỚC MỌI bước xử lý dữ liệu | [`02`](../02-Signal-Processing-ML-In-Practice/README.md) |
| Deep learning model càng train lâu càng "tệ đi" trên tập validation dù train loss vẫn giảm | Overfitting — mô hình học thuộc nhiễu của tập train | Áp dụng Early Stopping, Regularization, ưu tiên thêm dữ liệu trước khi tăng độ phức tạp mô hình | [`02`](../02-Signal-Processing-ML-In-Practice/README.md) |
| Duyệt ma trận lớn trong MATLAB chậm bất thường khi porting thuật toán từ Python | Duyệt sai thứ tự so với cách lưu column-major/row-major | Hiểu rõ MATLAB column-major vs Python NumPy row-major, duyệt đúng thứ tự | [`01`](../01-Numerical-Computing-Fundamentals/README.md) |
| Bộ điều khiển hoạt động tốt trong Simulink, dao động khi chạy phần cứng thật | Mô phỏng bỏ qua độ trễ/nhiễu thật của cảm biến-actuator | Thêm mô hình nhiễu + độ trễ ước lượng vào mô phỏng trước khi triển khai | [`02`](../02-Signal-Processing-ML-In-Practice/README.md) |

**Bài học mid-level cần khắc cốt ghi tâm:** *Kết quả "đẹp" trên dữ liệu/mô phỏng lý tưởng luôn cần bị hoài nghi — luôn tự hỏi "điều gì trong dữ liệu thật hoặc phần cứng thật có thể phá vỡ giả định lý tưởng này?"*

---

## 🔴 Cấp độ Senior/Chuyên gia — "Thiết kế toàn bộ pipeline đo lường-xử lý-triển khai đáng tin cậy"

| Vấn đề gặp phải (ở tầm hệ thống) | Senior/Chuyên gia xử lý thế nào | Đọc thêm |
|---|---|---|
| Dự án kết hợp MATLAB (xử lý tín hiệu) + Python (ML/Dashboard) như `Du_An_Ca_Nhan.md` — cần đảm bảo dữ liệu nhất quán giữa 2 hệ thống khác ngôn ngữ | Thiết kế format trao đổi dữ liệu chuẩn (CSV/HDF5/JSON có schema rõ ràng), kiểm tra kỹ thứ tự lưu ma trận (row/column-major) khi truyền qua lại | [`01`](../01-Numerical-Computing-Fundamentals/README.md) |
| Hệ thống giám sát công nghiệp thật cần vừa chính xác vừa chạy real-time | Cân bằng giữa độ chính xác thuật toán và tốc độ xử lý — chọn thuật toán/tần số lấy mẫu phù hợp với ràng buộc phần cứng thật, không chỉ tối ưu độ chính xác lý thuyết | [`02`](../02-Signal-Processing-ML-In-Practice/README.md) |
| Mô hình ML được huấn luyện tốt nhưng không ai kiểm tra lại khi dữ liệu thực tế thay đổi theo thời gian (model drift) | Thiết kế quy trình giám sát mô hình liên tục (theo dõi độ chính xác thực tế theo thời gian), không coi việc huấn luyện là "làm 1 lần xong" | [`../Cloud-DevOps-Mastery/05`](../../Cloud-DevOps-Mastery/05-Observability-Incident-Response/README.md) |
| Junior/mid liên tục mắc lỗi data leakage hoặc sai sampling rate ở nhiều dự án khác nhau | Đưa checklist bắt buộc vào quy trình review (giống playbook này), đào tạo lại nguyên lý gốc thay vì chỉ sửa từng lỗi | Áp dụng đúng tinh thần đã làm ở các cây kiến thức khác trong repo này |

**Bài học senior/chuyên gia cần khắc cốt ghi tâm:** *Trong tính toán khoa học/kỹ thuật, sai số không biến mất — nó chỉ chuyển từ "biết trước và kiểm soát được" sang "phát hiện muộn khi hệ thống thật đã hỏng". Vai trò cao nhất là thiết kế hệ thống đo lường/kiểm tra để phát hiện sai số SỚM, không phải cố loại bỏ sai số tuyệt đối (điều không thể).*

---

## 🗺️ Lộ trình tổng hợp để tự đánh giá bản thân đang ở đâu

```
Junior  → Chạy được thuật toán/mô hình ra kết quả đúng trên dữ liệu mẫu nhỏ,
          CHƯA để ý hiệu năng và giới hạn vật lý (Nyquist, sai số dấu phẩy động)
            ▼
Mid     → Biết tối ưu hiệu năng, nhưng cần được nhắc mới cảnh giác với
          data leakage/overfitting/sai lệch mô phỏng-thực tế
            ▼
Senior  → Thiết kế cả pipeline đo lường-xử lý-triển khai đáng tin cậy,
          chủ động xây cơ chế phát hiện sai số sớm ở tầm hệ thống
```

## 🔗 Liên kết
Chi tiết kỹ thuật: [`01`](../01-Numerical-Computing-Fundamentals/README.md) · [`02`](../02-Signal-Processing-ML-In-Practice/README.md)
Nguyên tắc chung áp dụng từ các cây kiến thức khác: [`../DSA-Mastery/`](../../DSA-Mastery/INDEX.md), [`../Cloud-DevOps-Mastery/`](../../Cloud-DevOps-Mastery/INDEX.md)
