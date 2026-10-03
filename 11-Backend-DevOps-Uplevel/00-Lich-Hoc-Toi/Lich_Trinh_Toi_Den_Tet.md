# 🌙 Lịch Học Tối 9h00 – 10h00/10h30 — Từ 25/09/2026 Đến Ra Tết (~12/02/2027)

> Khung giờ cố định: **21h00 – 22h00 (hoặc 22h30 nếu còn sức)**, sau khi đã học tiếng Anh. Mỗi tối chỉ 1 chủ đề nhỏ, KHÔNG ôm đồm — mục tiêu là đều đặn 6 tối/tuần.
>
> **💡 Nguyên tắc Học & Thực hành Xen kẽ (Interleaved Learning):** Tất cả các phần **Giải thích chuyên sâu (Lý thuyết)** và **Hướng dẫn thực hành từng bước (Hands-on Lab)** đã được **nhúng xen kẽ trực tiếp vào từng chương của cuốn sách [BOOK_Middle_Backend_Python_DevOps.md](../BOOK_Middle_Backend_Python_DevOps.md)**. Khi đọc xong phần cơ chế/lý thuyết ở Tối Thứ 2 & 4, bạn có thể thực hành ngay đoạn code & lệnh terminal ở mục `🛠️ Hướng dẫn thực hành từng bước` nằm ngay bên dưới của chính chương đó!

**Nhịp tuần cố định (lặp lại xuyên suốt 20 tuần):**

| Tối | Nội dung | Thời lượng |
|---|---|---|
| Thứ 2 | Đọc Lý thuyết & Cơ chế chuyên sâu trong `BOOK_Middle_Backend_Python_DevOps.md` | 45-60 phút |
| Thứ 3 | Thực hành theo mục `🛠️ Hướng dẫn thực hành` ngay dưới chương đó (Hands-on) | 45-60 phút |
| Thứ 4 | Đọc Lý thuyết & Cơ chế chuyên sâu tiếp theo trong `BOOK_Middle_Backend_Python_DevOps.md` | 45-60 phút |
| Thứ 5 | Thực hành theo mục `🛠️ Hướng dẫn thực hành` ngay dưới chương đó (Hands-on) | 45-60 phút |
| Thứ 6 | Làm 1 bài trong Exercise checklist (kiểm tra lại không nhìn hướng dẫn) | 60-90 phút |
| Thứ 7 | Lab lớn hơn / ghép nối kiến thức cả tuần / Debug lỗi thực tế | 60-90 phút |
| CN | Nghỉ hoặc đọc nhẹ + tick Progress Tracker + xem trước tuần sau | 15-30 phút |

---

## 🟢 CHẶNG 1 — Django Core (Tuần 1-4, 28/09 → 25/10)

> Tập trung vào **tư duy kiến trúc + cú pháp Django**, so sánh với Flask để hiểu rõ ưu/nhược điểm từng framework.

| Tuần | Thứ 2 & 4 (Lý thuyết) | Thứ 3 & 5 (Code theo) |
|---|---|---|
| 1 (28/9-4/10) | `Django_Mastery_Guide.md` — Models, Migrations, Admin | Tạo 1 Django project mới, 2 model có quan hệ ForeignKey |
| 2 (5/10-11/10) | `Django_Mastery_Guide.md` — Views, URLs, Templates cơ bản | Viết 3 view (list/detail/create) cho model tuần 1 |
| 3 (12/10-18/10) | `Python_Functions_Flask_Django_Guide.md` — so sánh cách Django vs Flask xử lý request | Refactor code tuần 2 theo Class-Based View |
| 4 (19/10-25/10) | `Mastery/Backend-Mastery/01-Request-Lifecycle-And-Architecture` — N+1 query, middleware | Bật query log, tự tạo N+1 query rồi tự fix bằng `select_related` |

**Thứ 6/Thứ 7 tuần 4:** làm Exercise DJ-01 → DJ-04 trong [01-Django-Exercises/Checklist_Bai_Tap.md](../01-Django-Exercises/Checklist_Bai_Tap.md).

---

## 🟡 CHẶNG 2 — Django REST Framework + Git nâng cao (Tuần 5-8, 26/10 → 22/11)

| Tuần | Thứ 2 & 4 (Lý thuyết) | Thứ 3 & 5 (Code theo) |
|---|---|---|
| 5 | DRF: Serializer, ViewSet, Router | Chuyển 3 view tuần 2 thành DRF API trả JSON |
| 6 | DRF: Permission, Authentication (JWT) | Thêm JWT login vào API trên |
| 7 | `DevOps_Roadmap_9_HocPhan.md` — Học phần 5 (Git nâng cao: rebase, hooks) | Setup pre-commit hook lint/test cho project Django đang làm |
| 8 | Đọc code thật `09-Example-Projects/Django_Rest_Pro` (đọc kiến trúc, không copy) | Viết unit test (mock) cho API đã làm tuần 5-6 |

**Thứ 6/Thứ 7 tuần 8:** Exercise DJ-05 → DJ-07.

---

## 🟠 CHẶNG 3 — Flask + Docker (Tuần 9-12, 23/11 → 20/12)

| Tuần | Thứ 2 & 4 (Lý thuyết) | Thứ 3 & 5 (Code theo) |
|---|---|---|
| 9 | Đọc `09-Example-Projects/Flask_RealWorld` — so sánh cấu trúc với Django vừa học | Viết lại 1 API đơn giản (đã làm ở Django) bằng Flask thuần |
| 10 | Flask blueprint, extension (Flask-SQLAlchemy, Flask-Migrate) | Thêm DB vào Flask app trên |
| 11 | `Docker_Kubernetes_Mastery.md` — Dockerfile, multi-stage build | Viết Dockerfile cho app Flask, build image, chạy container |
| 12 | `Docker_Kubernetes_Mastery.md` — Docker Compose | Compose Flask + Postgres, `docker-compose up` chạy được |

**Thứ 6/Thứ 7 tuần 12:** Exercise FL-01 → FL-04 + DO-01 → DO-02.

---

## 🔵 CHẶNG 4 — CI/CD + AWS Basic (Tuần 13-16, 21/12 → 17/01)

> Tuần 15-16 sát Tết, công việc/nhà cửa dễ bận — cho phép giảm còn 4 tối/tuần nếu cần, ưu tiên đừng bỏ hẳn.

| Tuần | Thứ 2 & 4 (Lý thuyết) | Thứ 3 & 5 (Code theo) |
|---|---|---|
| 13 | `CI_CD_Automation_GithubActions.md` | Viết pipeline GitHub Actions: test → build Docker image |
| 14 | `AWS_90Days_Mastery_Plan.md` (chỉ phần EC2/S3/VPC cơ bản) | Setup `localstack/`, thử tạo S3 bucket + EC2 giả lập bằng AWS CLI |
| 15 | `AWS_Knowledge_Handbook_VN.md` — Security Group, RDS | Nối pipeline CI/CD ở tuần 13 để deploy thử lên localstack/EC2 |
| 16 | Ôn lại + đọc `Mastery/Cloud-DevOps-Mastery/04-CICD-Deployment-Strategies` | Fix lỗi pipeline nếu có (thực tế luôn có lỗi ở bước này) |

**Thứ 6/Thứ 7 tuần 16:** Exercise DO-03 → DO-05.

---

## 🔴 CHẶNG 5 — K8s cơ bản + Mock Project nhỏ + Ôn phỏng vấn (Tuần 17-20, 18/01 → 12/02)

> Đây là chặng chốt trước Tết — ưu tiên **ghép nối** những gì đã học thành 1 project chạy được đầu-cuối, hơn là học thêm kiến thức mới.

| Tuần | Thứ 2 & 4 (Lý thuyết) | Thứ 3 & 5 (Code theo) |
|---|---|---|
| 17 | `Docker_Kubernetes_Mastery.md` — Pod, Deployment, Service cơ bản | Deploy app Flask (Docker image tuần 11) lên Minikube |
| 18 | Đọc `Mastery/Backend-Mastery/07-Real-World-War-Stories` (2-3 story/tối) | Ghép API Django (chặng 2) + Flask (chặng 3) thành 1 mini mock project |
| 19 | Đọc `Mastery/Cloud-DevOps-Mastery/07-Real-World-War-Stories` | Viết README/Runbook cho mock project, chuẩn bị câu chuyện STAR |
| 20 (tới ~12/02) | Ôn tập tổng hợp, mock phỏng vấn với chính mình (tự hỏi-tự trả lời câu hỏi Junior→Mid trong `06-Fresher-To-Senior-Knowledge-And-Interview-Map`) | Nghỉ ngơi, không nhồi thêm — dọn dẹp code cho gọn để show khi phỏng vấn |

**Tuần cận Tết (thường rơi vào cuối tuần 20):** dừng học, không nhồi kiến thức mới — não cần nghỉ trước khi vào guồng phỏng vấn sau Tết.

---

## 📌 Quy tắc khi lệch lịch
- Lệch 1-2 tối do bận việc: bỏ qua, học tiếp buổi tiếp theo đúng lịch — **không cố học bù dồn 2 chủ đề trong 1 tối**.
- Lệch quá 1 tuần: quay lại tối Thứ 2 của tuần đang dang dở, bỏ luôn phần đã lỡ thay vì cố đuổi kịp toàn bộ lịch — mục tiêu là duy trì thói quen, không phải phủ hết 100% nội dung.
