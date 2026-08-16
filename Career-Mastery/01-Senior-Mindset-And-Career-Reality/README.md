# 01. Senior Mindset — Điều Gì Thật Sự Phân Biệt Junior/Mid/Senior

> Roadmap chi tiết theo mốc thời gian đã có ở [`01-Roadmaps/`](../../01-Roadmaps/) (đặc biệt `Roadmap_Tang_Toc_Senior_FullStack.md`, `IT_Career_Path_And_Missing_Skills_VN.md`). File này bổ sung **tiêu chí đánh giá thật** mà các công ty dùng để phân biệt level — không phải số năm kinh nghiệm.

---

## 1. Sự khác biệt thật giữa các level (không phải "biết nhiều công nghệ hơn")

| Khía cạnh | Junior | Mid-level | Senior |
|---|---|---|---|
| **Phạm vi quyết định** | Làm đúng theo yêu cầu được giao | Tự quyết định cách implement 1 tính năng | Tự quyết định **có nên làm tính năng này không**, đánh đổi ra sao |
| **Xử lý sự cố** | Cần hướng dẫn từng bước | Tự debug được vấn đề trong phạm vi mình phụ trách | Điều phối xử lý sự cố xuyên nhiều team, biết khi nào cần escalate |
| **Code review** | Nhận feedback | Cho feedback về code style/bug | Cho feedback về **kiến trúc, tradeoff dài hạn**, dạy người khác qua review |
| **Giao tiếp** | Báo cáo tiến độ | Trao đổi kỹ thuật với team | **Giải thích quyết định kỹ thuật cho người không kỹ thuật** (PM, stakeholder) |
| **Tầm nhìn thời gian** | Task hôm nay | Sprint hiện tại | **Hệ quả 6-12 tháng tới** của quyết định hôm nay (technical debt, khả năng mở rộng) |

**Sự thật quan trọng nhất:** senior không phải người "biết nhiều thứ nhất" mà là người **đưa ra quyết định đúng dưới sự không chắc chắn**, và **chịu trách nhiệm về hệ quả** của quyết định đó. Đây là lý do phần lớn nội dung trong `DSA-Mastery`, `Backend-Mastery`, `Cloud-DevOps-Mastery` tập trung vào "tại sao chọn X" và "sự cố gì xảy ra khi chọn sai" — đó chính là tư duy senior thật, không phải chỉ thuộc cú pháp/API.

---

## 2. "Missing Skills" thật sự — điều CV không thể hiện nhưng phỏng vấn senior luôn kiểm tra

- **Đọc code người khác nhanh và đúng** — senior dành phần lớn thời gian đọc/review code hơn viết mới. Kỹ năng này gần như không được luyện tập chủ động ở giai đoạn junior (chỉ tập trung viết code của riêng mình).
- **Ước lượng công việc (estimation) có kèm rủi ro** — không chỉ "3 ngày" mà "3 ngày nếu API bên thứ 3 hoạt động đúng tài liệu, có thể tới 5 ngày nếu phải làm thêm retry/fallback".
- **Nói "không" hoặc "chưa nên làm bây giờ"** — với đủ lý do kỹ thuật thuyết phục, thay vì nhận mọi yêu cầu rồi cố gánh.
- **Viết tài liệu quyết định (ADR - Architecture Decision Record)** — ghi lại vì sao chọn giải pháp A thay vì B, để 1 năm sau người khác (hoặc chính mình) hiểu được bối cảnh, tránh việc "sửa đi sửa lại" cùng 1 quyết định.

---

## 3. Lộ trình thực tế: từ đọc tài liệu tới thể hiện được trong phỏng vấn/công việc

1. **Học lý thuyết công nghệ** (đã có sẵn ở `02-DSA-Curriculum`, `03-Python-Expert`, `04-Database-Mastery`, `07-AWS-Mastery`, `10-DevOps-Architect`).
2. **Hiểu ứng dụng thực tế + tradeoff** (đã bổ sung ở `DSA-Mastery`, `Backend-Mastery`, `Cloud-DevOps-Mastery`).
3. **Tự tạo case study cá nhân:** với mỗi dự án đã làm (kể cả dự án cá nhân), viết ra 3 quyết định kỹ thuật quan trọng nhất và lý do — đây chính là nguyên liệu cho câu hỏi phỏng vấn "kể về 1 vấn đề kỹ thuật khó bạn từng giải quyết" (xem [`04-Behavioral-And-Salary-Negotiation`](../04-Behavioral-And-Salary-Negotiation/README.md)).
4. **Luyện trả lời system design** bằng chính kiến thức đã có ở các cây trên → [`02-System-Design-Interview-Playbook`](../02-System-Design-Interview-Playbook/README.md).

---

## 🎯 Câu hỏi tự đánh giá bản thân

1. "Lần gần nhất mình từ chối 1 yêu cầu vì lý do kỹ thuật thuyết phục là khi nào?"
2. "Mình có thể giải thích 1 quyết định kiến trúc trong dự án gần nhất cho người không rành kỹ thuật hiểu không?"
3. "Nếu dự án hiện tại scale traffic gấp 10 lần, mình biết chính xác điểm nào sẽ vỡ trận đầu tiên không?"

## 🔗 Liên kết module khác
- Áp dụng mindset này vào trả lời phỏng vấn system design → [`02-System-Design-Interview-Playbook`](../02-System-Design-Interview-Playbook/README.md)
- Kiến thức kỹ thuật nền để chứng minh mindset này bằng hành động thật → [`../DSA-Mastery/`](../../DSA-Mastery/INDEX.md), [`../Backend-Mastery/`](../../Backend-Mastery/INDEX.md), [`../Cloud-DevOps-Mastery/`](../../Cloud-DevOps-Mastery/INDEX.md)
