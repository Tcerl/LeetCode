# 📚 LEETCODE & KNOWLEDGE MANAGEMENT REPOSITORY

Chào mừng bạn đến với kho lưu trữ kiến thức đã được tối ưu hóa. Toàn bộ tài liệu đã được phân loại vào các thư mục chuyên biệt để bạn dễ dàng quản lý và theo dõi tiến trình học tập.

---

## 🌳 6 CÂY KIẾN THỨC "SENIOR COMPANION" (MỚI — ĐÃ HOÀN THIỆN TOÀN BỘ REPO)

Bên cạnh các thư mục giáo trình gốc theo công nghệ (bên dưới), repo có thêm **6 cây kiến thức tổng hợp theo chủ đề**, tập trung vào ứng dụng thực tế, quyết định kiến trúc, sự cố production thật và cách trình bày trong phỏng vấn — thay vì lặp lại lý thuyết cú pháp đã có sẵn. Mỗi cây trỏ ngược về đúng tài liệu gốc liên quan, và tất cả liên kết vòng tròn với nhau. **Mỗi cây (trừ Career-Mastery) đều có module cuối "Junior-To-Senior Problem Playbook"** — tổng hợp lại toàn bộ vấn đề thật + giải pháp trong cây đó, sắp xếp theo 3 cấp độ Junior/Mid/Senior để bạn tự định vị mình đang ở đâu và biết bước tiếp theo cần học.

| Cây kiến thức | Chủ đề | Gộp từ các folder gốc |
|---|---|---|
| 🌳 [`DSA-Mastery/`](./Mastery/DSA-Mastery/INDEX.md) | Cấu trúc dữ liệu & giải thuật — ứng dụng thật (Redis LRU, DB Index, npm dependency graph...) | `02-DSA-Curriculum/`, `06-Exercises/20_exam_exercies/` |
| 🌳 [`Backend-Mastery/`](./Mastery/Backend-Mastery/INDEX.md) | Kiến trúc backend & database — vòng đời request, concurrency, scaling DB | `03-Python-Expert/`, `04-Database-Mastery/` |
| 🌳 [`Cloud-DevOps-Mastery/`](./Mastery/Cloud-DevOps-Mastery/INDEX.md) | Cloud & vận hành hệ thống — VPC/IAM, container, CI/CD, incident response | `07-AWS-Mastery/`, `10-DevOps-Architect/` |
| 🌳 [`Career-Mastery/`](./Mastery/Career-Mastery/INDEX.md) | Sự nghiệp & phỏng vấn — system design playbook, senior mindset, đàm phán lương | `01-Roadmaps/`, `04-Interview-Prep/`, `interview_prep/` |
| 🌳 [`Frontend-Fullstack-Mastery/`](./Mastery/Frontend-Fullstack-Mastery/INDEX.md) | Frontend & kiến trúc dự án — Vue 3 internals, review code thật, phản biện kiến trúc microservices | `08-Frontend-Mastery/`, `09-Example-Projects/`, `05-Projects-Docs/`, `06-Exercises/CODE_EXERCISES.md` |
| 🌳 [`Scientific-Computing-Mastery/`](./Mastery/Scientific-Computing-Mastery/INDEX.md) | Tính toán khoa học/kỹ thuật — vectorization, sai số, data leakage, sai lệch mô phỏng-thực tế | `06-Exercises/MATLAB/` |

**Cách dùng:** học lý thuyết/cú pháp ở folder gốc theo công nghệ trước → đọc cây tương ứng để hiểu ứng dụng thật + tradeoff + sự cố production → đọc module "Junior-To-Senior Problem Playbook" cuối mỗi cây để tự đánh giá cấp độ → dùng `Career-Mastery` để tổng hợp lại thành câu trả lời phỏng vấn. Chi tiết mục lục nằm trong `INDEX.md` của từng cây.

> ✅ Toàn bộ nội dung gốc trong repo (thư mục `01` đến `10`, `06-Exercises`, `interview_prep`) hiện đã có lớp kiến thức senior companion tương ứng — không còn phần nào chưa xử lý.

---

## 📂 CẤU TRÚC THƯ MỤC (FOLDER STRUCTURE)

### 🧭 [01-Roadmaps/](./01-Roadmaps/)
*Chứa các lộ trình học tập tổng thể từ cơ bản đến chuyên gia.*
- `Expert_Mastery_Roadmap_Project.md`: Lộ trình Fullstack & AWS Expert 2026.
- `AWS_90Days_Mastery_Plan.md`: Kế hoạch 90 ngày chinh phục AWS.
- `Roadmap_Tang_Toc_Senior_FullStack.md`: Lộ trình tăng tốc lên Senior.

### 🌳 [Career-Mastery/](./Mastery/Career-Mastery/) — **(Mới)**
*Cây kiến thức "senior companion" nối `01-Roadmaps`, `04-Interview-Prep` và `interview_prep` — đây là nơi kiến thức kỹ thuật từ 3 cây trên (DSA/Backend/Cloud) được tổng hợp thành: senior mindset thật sự là gì, khung 5 bước trả lời system design (kèm bản đồ "đề bài kinh điển → kiến thức cần dùng"), chiến lược trả lời phỏng vấn kỹ thuật, và đàm phán lương. Xem [`INDEX.md`](./Mastery/Career-Mastery/INDEX.md).*

### 🧠 [02-DSA-Curriculum/](./02-DSA-Curriculum/)
*Giáo trình chi tiết về Cấu trúc dữ liệu và Giải thuật.*
- `DSA_Giao_Trinh_Chi_Tiet.md`: Tài liệu học DSA từ đầu (Python focused).
- `DSA_Lo_Trinh_On_Luyen_4_Tram.md`: Lộ trình ôn tập 4 trạm thực chiến.

### 🌳 [DSA-Mastery/](./Mastery/DSA-Mastery/) — **(Mới)**
*Cây kiến thức "senior companion" cho DSA — bổ sung lớp ứng dụng thực tế (hệ thống nào đang dùng cấu trúc dữ liệu này, bẫy production, giải pháp thật) lên trên nền `02-DSA-Curriculum`. Xem [`INDEX.md`](./Mastery/DSA-Mastery/INDEX.md) để có mục lục đầy đủ 7 module + code review thật cho bài tập trong `06-Exercises/20_exam_exercies/`.

### 🐍 [03-Python-Expert/](./03-Python-Expert/)
*Kiến thức chuyên sâu về ngôn ngữ Python.*
- `Python_Core_Mastery.md`: **(Mới)** Từ cơ bản đến nâng cao (AsyncIO, OOP, Metaclass).
- `Python_Standard_Library_Guide.md`: **(Mới)** Danh mục các Module "Batteries Included" cần biết.
- `Pythonic_Code_Shortening_Guide.md`: **(Mới)** Nghệ thuật rút gọn code (Walrus, Comprehensions, Lambda).
- `Python_Functions_Flask_Django_Guide.md`: **(Mới)** Lộ trình Flask/Django chuyên sâu.
- `Django_Mastery_Guide.md`: **(Mới)** Lộ trình Django chuyên sâu.
- `Python_Backend_Professional_Guide.md`: **(Mới)** Backend Python chuyên sâu (chưa có giáo trình Odoo riêng — xem `09-Example-Projects/Odoo_Advanced_Module`).

### 🗄️ [04-Database-Mastery/](./04-Database-Mastery/)
*Làm chủ linh hồn của hệ thống: SQL & NoSQL.*
- `PostgreSQL_Expert_Guide.md`: **(Mới)** Tối ưu hóa SQL, Indexing, Partitioning.
- `MongoDB_Expert_Guide.md`: **(Mới)** Linh hoạt với NoSQL, Sharding & Aggregation.

### 🌳 [Backend-Mastery/](./Mastery/Backend-Mastery/) — **(Mới, cập nhật)**
*Cây kiến thức "senior companion" nối `03-Python-Expert` và `04-Database-Mastery` thành 1 luồng hệ thống hoàn chỉnh: vòng đời request, N+1 query, connection pool, async/GIL thật sự, playbook chọn & scale database, observability. **Mới bổ sung Module 06** — bản đồ kiến thức đầy đủ Fresher→Junior→Mid→Senior kèm câu hỏi phỏng vấn backend thật + mẫu trả lời cho từng cấp độ. Xem [`INDEX.md`](./Mastery/Backend-Mastery/INDEX.md).*

### 💼 [04-Interview-Prep/](./04-Interview-Prep/)
*Tài liệu ôn luyện phỏng vấn thực chiến.*
- `ON_LUYEN_PHONG_VAN.md`: Tổng hợp câu hỏi và kỹ năng phỏng vấn.
- `Fullstack_Python_Vue_Interview_Prep.md`: Ôn luyện Fullstack (Python/Vue).
- `Interview_Prep_Odoo_Developer.md`: Chuyên biệt cho Odoo Developer.

### 🏗️ [05-Projects-Docs/](./05-Projects-Docs/)
*Hướng dẫn và tài liệu thiết kế dự án.*
- `Huong_Dan_Du_An_Chi_Tiet_Va_Mo_Rong.md`: Tài liệu hướng dẫn dự án NexusFlow.

### 🏠 [07-AWS-Mastery/](./07-AWS-Mastery/)
*Chuyên đề xây dựng kiến trúc hệ thống đám mây.*
- `AWS_Architecture_Deep_Dive.md`: **(Mới)** Kiến thức chuyên sâu về VPC, IAM, Compute, Storage kèm ví dụ thực tế.
- `AWS_90Days_Mastery_Plan.md`: Kế hoạch 90 ngày chinh phục AWS.

### 🌳 [Cloud-DevOps-Mastery/](./Mastery/Cloud-DevOps-Mastery/) — **(Mới)**
*Cây kiến thức "senior companion" nối `07-AWS-Mastery` và `10-DevOps-Architect` — quyết định kiến trúc thật (VPC an toàn, IAM least-privilege, EC2 vs Lambda vs Container), vận hành container thật (resource limits, liveness/readiness), chiến lược deploy (canary, feature flag, migration an toàn), và incident response (SLI/SLO, golden signals, postmortem). Xem [`INDEX.md`](./Mastery/Cloud-DevOps-Mastery/INDEX.md).*

### 🎨 [08-Frontend-Mastery/](./08-Frontend-Mastery/)
*Chuyên sâu kiến trúc giao diện hiện đại.*
- `VueJS_Professional_Guide.md`: **(Mới)** Composition API, Pinia, Composables & Performance.

### 🌳 [Frontend-Fullstack-Mastery/](./Mastery/Frontend-Fullstack-Mastery/) — **(Mới)**
*Cây kiến thức "senior companion" nối `08-Frontend-Mastery`, `09-Example-Projects`, `05-Projects-Docs` và phần Vue/Laravel trong `06-Exercises` — Vue 3 Proxy/Event Loop internals, khi nào cần global state, **code review thật** cho từng project mẫu (Flask/Django/Odoo, có chỉ ra bug thật), và phản biện kiến trúc microservices của dự án NexusFlow ("premature microservices"). Xem [`INDEX.md`](./Mastery/Frontend-Fullstack-Mastery/INDEX.md).*

### 🚀 [09-Example-Projects/](./09-Example-Projects/)
*Kho dự án mẫu Boilerplate "chuẩn Senior".*
- `Flask_SaaS_Boilerplate`: Dự án mẫu Flask SaaS.
- `Django_Rest_Pro`: Dự án mẫu Django REST.
- `Odoo_Advanced_Module`: Dự án mẫu Odoo.

### 🚀 [10-DevOps-Architect/](./10-DevOps-Architect/)
*Chuyên sâu về hạ tầng và tự động hóa.*
- `Docker_Kubernetes_Mastery.md`, `CI_CD_Automation_GithubActions.md`: Docker, K8s, và CI/CD Automation.

### 🛠️ [06-Exercises/](./06-Exercises/)
*Kho bài tập và thực hành.*
- `CODE_EXERCISES.md`: Tổng hợp các bài tập code.
- `20_exam_exercies/`: Các bài tập kiểm tra.
- `MATLAB/`: Tài liệu về MATLAB.

### 🌳 [Scientific-Computing-Mastery/](./Mastery/Scientific-Computing-Mastery/) — **(Mới)**
*Cây kiến thức "senior companion" cho `06-Exercises/MATLAB/` — vectorization/preallocation (hiệu năng tính toán số), sai số dấu phẩy động, định lý Nyquist/aliasing trong xử lý tín hiệu, data leakage & overfitting trong ML, sai lệch mô phỏng Simulink vs phần cứng thật. Xem [`INDEX.md`](./Mastery/Scientific-Computing-Mastery/INDEX.md).*

---

## 🗺️ LỘ TRÌNH HỌC TẬP ZERO TO HERO (CHINH PHỤC FULLSTACK & CLOUD)

Dưới đây là kế hoạch học tập được tối ưu hóa dựa trên kho tài liệu hiện có:

| Giai đoạn | Mục tiêu chính | Tài liệu trọng tâm | Thời gian dự kiến |
| :--- | :--- | :--- | :--- |
| **01. Khởi động** | Python Cơ bản & DSA | [Python_Core_Mastery.md](./03-Python-Expert/Python_Core_Mastery.md), [DSA_Giao_Trinh_Chi_Tiet.md](./02-DSA-Curriculum/DSA_Giao_Trinh_Chi_Tiet.md) | 2 tháng |
| **02. Backend** | Frameworks & SQL Expert | [Python_Functions_Flask_Django_Guide.md](./03-Python-Expert/Python_Functions_Flask_Django_Guide.md), [PostgreSQL_Expert_Guide.md](./04-Database-Mastery/PostgreSQL_Expert_Guide.md) | 2 tháng |
| **03. Frontend** | VueJS Modern Development | [VueJS_Professional_Guide.md](./08-Frontend-Mastery/VueJS_Professional_Guide.md) | 1.5 tháng |
| **04. Cloud/Ops** | AWS Architect & DevOps | [AWS_Architecture_Deep_Dive.md](./07-AWS-Mastery/AWS_Architecture_Deep_Dive.md), [Docker_Kubernetes_Mastery.md](./10-DevOps-Architect/Docker_Kubernetes_Mastery.md) | 2.5 tháng |
| **05. Pro Project** | Fullstack SaaS/Odoo | [09-Example-Projects/](./09-Example-Projects/), [09-Example-Projects/Odoo_Advanced_Module](./09-Example-Projects/Odoo_Advanced_Module/) | 2 tháng |
| **06. Interview** | Sẵn sàng cho Senior | [ON_LUYEN_PHONG_VAN.md](./04-Interview-Prep/ON_LUYEN_PHONG_VAN.md) | Liên tục |

---

## 🎯 CÁCH SỬ DỤNG HIỆU QUẢ
1. **Bắt đầu từ Roadmaps:** Luôn bám sát lộ trình trong `01-Roadmaps` để không bị lạc hướng.
2. **Học DSA/Python:** Sử dụng giáo trình tại `02` và `03` để nắm vững tư duy backend.
3. **Làm chủ Cloud:** Đào sâu kiến trúc tại `07` để hiểu cách hệ thống vận hành.
4. **Trình diễn Frontend:** Dùng tài liệu tại `08` để xây dựng UI đẳng cấp cho NexusFlow.
5. **Mock Interview:** Sử dụng tài liệu trong `04` để chuẩn bị cho kỳ phỏng vấn.

---
*Hệ thống được cấu trúc và quản lý bởi Antigravity AI Assistant.*