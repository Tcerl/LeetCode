# 🌳 Scientific-Computing-Mastery — Cây Kiến Thức Tính Toán Khoa Học/Kỹ Thuật (Senior Companion)

> **Mục đích:** Lớp kiến thức bổ sung cho [`06-Exercises/MATLAB/`](../06-Exercises/MATLAB/) — giáo trình MATLAB đầy đủ từ cơ bản tới Machine Learning/Deep Learning/Simulink. Cây này bổ sung góc nhìn **kỹ sư đã gặp sự cố thật** (hiệu năng tính toán, sai số, data leakage, sai lệch mô phỏng-thực tế) — đây là cây thứ 6, hoàn thiện toàn bộ phạm vi kiến thức còn lại trong repo.

---

## 📋 MỤC LỤC

| # | Module | Chủ đề | Nguồn liên quan |
|---|---|---|---|
| 01 | [Numerical Computing Fundamentals](01-Numerical-Computing-Fundamentals/README.md) | Vectorization, preallocation, sai số dấu phẩy động, row/column-major | `01_Co_Ban.md`, `02_Trung_Cap.md` |
| 02 | [Signal Processing & ML In Practice](02-Signal-Processing-ML-In-Practice/README.md) | Nyquist/aliasing, data leakage, overfitting, sai lệch mô phỏng Simulink-thực tế | `03_Nang_Cao.md`, `04_Ung_Dung.md` |
| 03 | [Junior-To-Senior Problem Playbook](03-Junior-To-Senior-Problem-Playbook/README.md) | Vấn đề thật + giải pháp theo cấp độ, tham chiếu dự án MATLAB+Python thật | `Du_An_Ca_Nhan.md`, `05_Bai_Tap.md` |

---

## 🗺️ Sơ đồ liên hệ

```
01-Numerical Computing Fundamentals (nền tảng hiệu năng & sai số)
        ▼
02-Signal Processing & ML In Practice (ứng dụng thật: đo lường, mô hình, điều khiển)
        ▼
03-Junior-To-Senior Problem Playbook (tổng hợp lộ trình vấn đề theo cấp độ)
```

## Cách dùng
1. Học lý thuyết/cú pháp MATLAB đầy đủ ở `06-Exercises/MATLAB/` trước (đã có lộ trình 4 cấp độ + bài tập trong `05_Bai_Tap.md`).
2. Đọc cây này để hiểu **vì sao các quy tắc tồn tại** — hiệu năng thật, sai số thật, và cách tránh các lỗi kinh điển khi đưa mô hình nghiên cứu ra ứng dụng thật (công nghiệp, IoT, ML production).
3. Dùng [`03-Junior-To-Senior-Problem-Playbook`](03-Junior-To-Senior-Problem-Playbook/README.md) để tự đánh giá cấp độ hiện tại.

## 🔗 Liên kết sang các cây khác
- Vectorization/preallocation liên hệ trực tiếp Big O và Dynamic Array → [`../DSA-Mastery/`](../DSA-Mastery/INDEX.md)
- Data leakage/model drift liên hệ nguyên tắc Observability trong vận hành hệ thống → [`../Cloud-DevOps-Mastery/`](../Cloud-DevOps-Mastery/INDEX.md)

---

## ✅ Tổng kết: 6 cây kiến thức đã hoàn thiện toàn bộ repo

| Cây | Phạm vi |
|---|---|
| [`DSA-Mastery/`](../DSA-Mastery/INDEX.md) | Cấu trúc dữ liệu & giải thuật |
| [`Backend-Mastery/`](../Backend-Mastery/INDEX.md) | Backend & Database |
| [`Cloud-DevOps-Mastery/`](../Cloud-DevOps-Mastery/INDEX.md) | Cloud & vận hành hệ thống |
| [`Career-Mastery/`](../Career-Mastery/INDEX.md) | Sự nghiệp & phỏng vấn |
| [`Frontend-Fullstack-Mastery/`](../Frontend-Fullstack-Mastery/INDEX.md) | Frontend & kiến trúc dự án |
| `Scientific-Computing-Mastery/` (cây này) | Tính toán khoa học/kỹ thuật (MATLAB) |

Toàn bộ nội dung gốc trong repo (`01` đến `10` + `06-Exercises` + `interview_prep`) giờ đã có lớp kiến thức senior companion tương ứng.
