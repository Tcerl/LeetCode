# 💰 LỘ TRÌNH: TỪ JUNIOR FULLSTACK 12 TRIỆU → MỨC LƯƠNG CAO HƠN

> **Bối cảnh:** Tài liệu này dành riêng cho người **đã đi làm** (không phải fresher chuẩn bị xin việc lần đầu — xem [`Roadmap_Fresher_Junior_RutGon.md`](./Roadmap_Fresher_Junior_RutGon.md) cho trường hợp đó), hiện đang ở mức lương thấp so với thị trường (~12 triệu/tháng cho vị trí Fullstack Junior), muốn có lộ trình cụ thể để tăng thu nhập trong 6-12 tháng tới. Các roadmap kỹ thuật khác trong repo (`02` đến `10`, và `Mastery/`) trả lời câu hỏi "học gì" — tài liệu này trả lời câu hỏi khó hơn: **"học gì, theo thứ tự nào, và làm gì với nó để nó thực sự chuyển thành lương cao hơn."**

---

## 1. Nhìn thẳng vào thực trạng: vì sao đang ở mức 12 triệu

Đây không phải vấn đề "chưa đủ giỏi" — mà thường là 1 trong 3 nguyên nhân sau (thường là kết hợp cả 3):

| Nguyên nhân | Dấu hiệu nhận biết | Đòn bẩy tương ứng |
|---|---|---|
| **Công ty trả thấp hơn thị trường** (outsource nhỏ, công ty local ngân sách hẹp) | Đồng nghiệp cùng kinh nghiệm ở công ty khác lương cao hơn 30-50% | Mục 3.1 — Nhảy việc |
| **Kỹ năng chưa có gì "khan hiếm"** — chỉ làm CRUD theo hướng dẫn, chưa từng tự quyết định kiến trúc | Chưa từng bị hỏi "tại sao" trong công việc, chỉ nhận task và làm đúng như được giao | Mục 3.2 — Xây kỹ năng khan hiếm |
| **Không có "bằng chứng"** để định giá lại bản thân — có làm nhưng không đo lường, không kể lại được | Khi được hỏi "bạn đã đóng góp gì", chỉ trả lời chung chung ("làm nhiều feature") | Mục 3.3 — Portfolio có số liệu |

> **Sự thật khó nghe nhưng quan trọng nhất ở thị trường VN:** tăng lương bằng cách **ở lại công ty cũ chờ review lương hàng năm** thường chỉ được 5-15%/năm. **Nhảy việc đúng thời điểm với kỹ năng đã nâng cấp** thường tạo ra bước nhảy 30-70% trong 1 lần — đây là chênh lệch lớn nhất bạn cần biết trước khi lập kế hoạch. Chi tiết tư duy đứng sau điều này ở [`Mastery/Career-Mastery/01-Senior-Mindset-And-Career-Reality`](../Mastery/Career-Mastery/01-Senior-Mindset-And-Career-Reality/README.md).

---

## 2. Bức tranh mặt bằng lương thị trường VN (tham khảo, không phải số cố định)

Số liệu dưới đây là **ước lượng mặt bằng chung** (thay đổi theo thành phố, loại hình công ty, và biến động thị trường theo thời gian) — dùng để bạn tự định vị, không phải cam kết:

| Cấp độ | Kinh nghiệm | Product/Startup VN | Outsource VN | Product nước ngoài / Remote |
|---|---|---|---|---|
| Fresher | 0-6 tháng | 6-10tr | 6-9tr | — |
| **Junior** | 6th-2 năm | **10-18tr** | **9-15tr** | 15-25tr+ |
| Mid | 2-4 năm | 18-30tr | 15-25tr | 30-50tr+ |
| Senior | 4-6+ năm | 30-50tr+ | 25-40tr | 50-100tr+ |

**Đọc bảng này thế nào:** ở mức 12tr, bạn đang ở vùng Junior thấp/outsource. Có 2 trục để di chuyển lên: (a) **trục dọc** — lên cấp độ kinh nghiệm/kỹ năng, (b) **trục ngang** — chuyển loại hình công ty (outsource → product, hoặc product VN → remote nước ngoài). Trục ngang thường tạo bước nhảy lương lớn hơn và nhanh hơn trục dọc đơn thuần — đây là lý do mục 3.1 và 3.4 dưới đây quan trọng ngang với việc học kỹ thuật.

---

## 3. Bốn đòn bẩy — làm theo đúng thứ tự ưu tiên

### 3.1. Nhảy việc đúng thời điểm (đòn bẩy nhanh nhất)

- **Không đợi "giỏi hẳn rồi mới apply".** Apply khi đã hoàn thành ~70% checklist mục 4 bên dưới — thị trường luôn định giá theo *tiềm năng thể hiện được trong phỏng vấn*, không phải điểm số tuyệt đối.
- **Luôn phỏng vấn kể cả khi chưa quyết định nghỉ** — mỗi buổi phỏng vấn là 1 lần định giá lại bản thân theo thị trường thật, và tạo ra offer để đàm phán ngược lại với công ty hiện tại nếu muốn ở lại.
- Chi tiết kỹ thuật đàm phán, cách trả lời không tiết lộ số trước, cách dùng offer làm đòn bẩy → [`Mastery/Career-Mastery/04-Behavioral-And-Salary-Negotiation`](../Mastery/Career-Mastery/04-Behavioral-And-Salary-Negotiation/README.md).

### 3.2. Xây kỹ năng khan hiếm — không phải kỹ năng "biết dùng", mà kỹ năng "biết quyết định"

Sự khác biệt giữa Junior 12tr và Mid/Senior không nằm ở việc *biết công cụ gì*, mà ở việc *có tự quyết định được kiến trúc, tự debug được sự cố lạ, tự đánh giá được tradeoff không*. Thứ tự ưu tiên học (dựa trên nội dung đã có sẵn trong repo):

1. **Testing** — lỗ hổng phổ biến nhất ở Junior. Không có test = không được tin tưởng giao việc lớn. Xem gap được liệt kê ở [`IT_Career_Path_And_Missing_Skills_VN.md`](./IT_Career_Path_And_Missing_Skills_VN.md#phần-3-những-mảng-kiến-thức-còn-thiếu-cần-bổ-sung-để-bứt-phá-update-mới) mục 3 (Pytest, Jest/Cypress).
2. **System Design cơ bản** — không cần thiết kế hệ thống triệu user ngay, nhưng phải giải thích được *tại sao* chọn kiến trúc này chứ không phải kiến trúc khác. Bắt đầu từ [`Mastery/Career-Mastery/02-System-Design-Interview-Playbook`](../Mastery/Career-Mastery/02-System-Design-Interview-Playbook/README.md), áp dụng thật vào [`Mastery/Backend-Mastery/`](../Mastery/Backend-Mastery/INDEX.md).
3. **Cloud/DevOps thực chiến (không chỉ lý thuyết)** — tự deploy, tự cấu hình CI/CD 1 dự án thật. Đây là kỹ năng khan hiếm nhất theo `IT_Career_Path_And_Missing_Skills_VN.md`, dùng [`Mastery/Cloud-DevOps-Mastery/`](../Mastery/Cloud-DevOps-Mastery/INDEX.md).
4. **Tích hợp AI/LLM vào sản phẩm thật** (RAG, gọi API OpenAI/Claude/Gemini) — trend trả lương cao nhất hiện tại cho Fullstack, vì rất ít Junior VN thực chiến được phần này, không chỉ "nghe nói tới".

> Đừng học dàn trải cả 4 mục cùng lúc trong 1-2 tháng — chọn **1 dự án thật** (mục 3.3) và học đúng phần cần dùng cho dự án đó trước.

### 3.3. Portfolio có số liệu — biến việc học thành bằng chứng định giá được

Kiến thức không tự chuyển thành lương — **bằng chứng thể hiện được trong phỏng vấn** mới chuyển thành lương. Mỗi tháng học xong 1 kỹ năng ở mục 3.2, bắt buộc áp dụng vào **1 dự án thật của riêng bạn** (không phải bài tập), có deploy thật, có số liệu thật (bao nhiêu request/s xử lý được, giảm bao nhiêu % thời gian load, test coverage bao nhiêu %). Đây chính là nguyên liệu cho khung STAR ở mục đàm phán lương (mục 3.1).

### 3.4. Tiếng Anh — đòn bẩy bị đánh giá thấp nhất nhưng ảnh hưởng trực tiếp tới trục ngang (mục 2)

Bạn đang có sẵn [`Toeic_Training/`](../Toeic_Training/) trong repo này — đừng tách rời nó khỏi lộ trình sự nghiệp. Tiếng Anh tốt (giao tiếp + đọc tài liệu kỹ thuật) là điều kiện **bắt buộc** để tiếp cận nhóm "Product nước ngoài/Remote" ở bảng lương mục 2 — nhóm trả cao gấp 2-3 lần cùng cấp độ so với thị trường trong nước. Ưu tiên luyện theo hướng giao tiếp kỹ thuật (mô tả bug, trao đổi trong code review, phỏng vấn tiếng Anh) hơn là ngữ pháp thuần túy thi cử.

---

## 4. Checklist 6 tháng — theo dõi tiến độ

**Tháng 1-2:**
- [ ] Chọn 1 dự án thật để làm nền cho portfolio (không phải bài tập có sẵn)
- [ ] Viết ≥5 test có ý nghĩa cho 1 tính năng đang làm ở công việc hiện tại (Pytest/Jest)
- [ ] Đọc xong [`Mastery/Career-Mastery/01-Senior-Mindset-And-Career-Reality`](../Mastery/Career-Mastery/01-Senior-Mindset-And-Career-Reality/README.md)

**Tháng 3-4:**
- [ ] Dự án thật có CI/CD tự động (GitHub Actions) + deploy thật (không phải chạy local)
- [ ] Giải thích được bằng lời 1 quyết định kiến trúc trong dự án đó — tại sao chọn cách này, tradeoff là gì
- [ ] Bắt đầu tích hợp 1 tính năng dùng LLM API thật vào dự án (dù nhỏ)

**Tháng 5-6:**
- [ ] CV + portfolio có số liệu cụ thể (không dùng câu chung chung "xây dựng nhiều tính năng")
- [ ] Chuẩn bị 4-5 câu chuyện STAR theo [`Mastery/Career-Mastery/04-Behavioral-And-Salary-Negotiation`](../Mastery/Career-Mastery/04-Behavioral-And-Salary-Negotiation/README.md)
- [ ] Bắt đầu apply + phỏng vấn thật (kể cả chưa chắc nhận offer) — mục tiêu là hiệu chỉnh lại bằng thị trường thật, không phải tự đánh giá

---

## 🔗 Liên kết module khác
- Kỹ năng còn thiếu chi tiết theo từng mảng → [`IT_Career_Path_And_Missing_Skills_VN.md`](./IT_Career_Path_And_Missing_Skills_VN.md)
- Tư duy senior + system design + đàm phán lương → [`Mastery/Career-Mastery/`](../Mastery/Career-Mastery/INDEX.md)
- Nền tảng kỹ thuật theo từng mảng → [`Mastery/Backend-Mastery/`](../Mastery/Backend-Mastery/INDEX.md), [`Mastery/Cloud-DevOps-Mastery/`](../Mastery/Cloud-DevOps-Mastery/INDEX.md), [`Mastery/Frontend-Fullstack-Mastery/`](../Mastery/Frontend-Fullstack-Mastery/INDEX.md)
- Luyện tiếng Anh song song → [`Toeic_Training/`](../Toeic_Training/)
