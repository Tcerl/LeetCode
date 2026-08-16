# 05. Salary Growth Playbook — Vì Sao Lương Tăng (Hoặc Không), Và Cách Chủ Động Kiểm Soát Nó

> Module này trả lời câu hỏi kỹ thuật đứng sau việc tăng lương: **thị trường định giá bạn dựa trên tín hiệu (signal) nào ở mỗi cấp độ**, không phải dựa trên số năm kinh nghiệm. Phần hành động cụ thể (checklist theo tháng, bảng lương tham khảo VN) nằm ở [`01-Roadmaps/Roadmap_Tu_Junior_12Trieu_Len_Luong_Cao.md`](../../../01-Roadmaps/Roadmap_Tu_Junior_12Trieu_Len_Luong_Cao.md) — module này giải thích **vì sao** lộ trình đó được thiết kế như vậy.

---

## 1. Sự thật đầu tiên: lương phản ánh RỦI RO công ty gánh khi thiếu bạn, không phản ánh nỗ lực

Công ty không trả lương theo "bạn làm việc chăm chỉ thế nào" — họ trả theo **mức độ khó thay thế bạn** và **quy mô thiệt hại nếu bạn làm sai/nghỉ việc**. Đây là lý do 2 kỹ sư cùng số năm kinh nghiệm có thể chênh lệch lương gấp đôi:

- Kỹ sư A: làm đúng task được giao, code chạy đúng, nhưng bất kỳ ai trong team cũng làm được task tương tự trong thời gian gần bằng → dễ thay thế → lương neo theo mặt bằng thấp.
- Kỹ sư B: là người duy nhất hiểu tại sao hệ thống được thiết kế như vậy, tự phát hiện và ngăn được sự cố trước khi xảy ra, người khác trong team hỏi ý kiến trước khi đổi kiến trúc → khó thay thế → lương phản ánh đúng rủi ro nếu thiếu người này.

**Hệ quả trực tiếp:** muốn tăng lương, việc cần làm không phải "làm nhiều task hơn" mà là **chuyển từ "làm đúng việc được giao" sang "làm việc mà nếu thiếu bạn, hệ thống/team sẽ chịu rủi ro rõ rệt."**

---

## 2. Bảng tín hiệu theo cấp độ — thị trường "đọc" bạn qua đâu

| Cấp độ | Tín hiệu kỹ thuật nhà tuyển dụng tìm | Tín hiệu hành vi | Câu hỏi phỏng vấn điển hình để kiểm tra tín hiệu này |
|---|---|---|---|
| **Fresher** | Code chạy đúng logic được giao, hiểu cú pháp/framework cơ bản | Học nhanh, hỏi đúng câu hỏi khi bí | "Giải thích code này làm gì" |
| **Junior** | Tự debug được lỗi không rõ nguyên nhân ban đầu, viết được test cơ bản | Chủ động báo cáo tiến độ, nhận task không cần hướng dẫn từng bước | "Kể 1 lần bạn tự tìm ra nguyên nhân 1 lỗi khó" |
| **Mid** | Tự ra quyết định kỹ thuật có tradeoff (chọn công nghệ, thiết kế schema), hiểu giới hạn tài nguyên hệ thống | Review code người khác có chất lượng, không cần được nhắc về edge case | "Tại sao bạn chọn X thay vì Y trong dự án đó?" |
| **Senior** | Thiết kế được kiến trúc/quy trình ngăn CẢ LỚP vấn đề lặp lại, không chỉ vá từng lỗi | Người khác chủ động hỏi ý kiến trước khi quyết định lớn | "Kể 1 lần bạn thay đổi QUY TRÌNH của team, không chỉ fix 1 bug" |

> Đây chính xác là khung được dùng xuyên suốt [`Mastery/Backend-Mastery/05`](../../Backend-Mastery/05-Junior-To-Senior-Problem-Playbook/README.md) và [`Mastery/Cloud-DevOps-Mastery/06`](../../Cloud-DevOps-Mastery/06-Junior-To-Senior-Problem-Playbook/README.md) — mỗi "bài học khắc cốt ghi tâm" ở cuối mỗi cấp độ trong 2 module đó chính là 1 tín hiệu trong bảng trên.

---

## 3. Case study minh họa — 2 lộ trình khác nhau từ cùng 1 điểm xuất phát

*(Tình huống minh họa mang tính điển hình, tổng hợp từ các mẫu hình phổ biến trên thị trường, không phải 1 cá nhân cụ thể.)*

**Kỹ sư X và Y cùng vào nghề với mức lương 10-12 triệu, vị trí Junior Fullstack outsource.**

- **X sau 2 năm vẫn ở mức ~14 triệu:** ở lại 1 công ty, nhận task đều đặn, hoàn thành đúng hạn — nhưng chưa từng chủ động đề xuất thay đổi kiến trúc, chưa viết test trừ khi được yêu cầu, chưa từng phỏng vấn công ty khác để biết mình đang được định giá bao nhiêu trên thị trường.
- **Y sau 18 tháng đạt ~28 triệu:** sau 6 tháng đầu tương tự X, Y bắt đầu tự làm 1 dự án cá nhân có CI/CD + test + deploy thật, chủ động đề xuất thêm cache khi phát hiện API chậm (dù không được giao), và **đi phỏng vấn 3 công ty khác ở tháng thứ 10** dù chưa chắc nghỉ — nhận ra mình đang bị trả dưới giá thị trường, dùng offer đó đàm phán lại, rồi nhảy việc.

**Khác biệt cốt lõi không phải "Y giỏi hơn X 2 lần"** — mà là Y liên tục tạo ra **bằng chứng đo lường được** (dự án thật, đề xuất chủ động) và **liên tục kiểm tra lại giá trị bản thân với thị trường thật** (phỏng vấn định kỳ), thay vì tự đánh giá một mình rồi chờ công ty tự nhận ra.

---

## 4. Ba bẫy tư duy khiến người có năng lực vẫn bị trả lương thấp

1. **"Chờ được ghi nhận" thay vì chủ động tạo bằng chứng** — công ty không có nghĩa vụ tự phát hiện giá trị của bạn; bạn phải chủ động kể lại nó (xem [`04-Behavioral-And-Salary-Negotiation`](../04-Behavioral-And-Salary-Negotiation/README.md) mục khung STAR).
2. **Học dàn trải nhiều công nghệ nhưng không có dự án thật chứng minh** — nhà tuyển dụng không định giá "bạn biết gì", mà định giá "bạn từng tự tay giải quyết vấn đề gì" — kiến thức không gắn với 1 vấn đề thật cụ thể sẽ không thuyết phục được ai trong phỏng vấn.
3. **Không bao giờ phỏng vấn công ty khác vì "đang ổn định"** — đây là cách chắc chắn nhất để bị trả lương dưới giá thị trường mà không hề biết, vì bạn mất đi cơ chế duy nhất để tự kiểm chứng giá trị thật của mình (chi tiết ở [`01-Senior-Mindset-And-Career-Reality`](../01-Senior-Mindset-And-Career-Reality/README.md)).

---

## 🎯 Câu hỏi tự đánh giá

1. Trong 3 tháng gần nhất, bạn có làm điều gì mà **nếu bạn nghỉ, người khác sẽ khó thay thế ngay** không? Kể cụ thể.
2. Bạn có đang giữ 1 dự án thật (không phải bài tập) làm bằng chứng năng lực, cập nhật định kỳ không?
3. Lần gần nhất bạn phỏng vấn 1 công ty khác (kể cả không có ý định nghỉ) là khi nào?

## 🔗 Liên kết module khác
- Lộ trình hành động cụ thể theo tháng, bảng lương tham khảo VN → [`Roadmap_Tu_Junior_12Trieu_Len_Luong_Cao.md`](../../../01-Roadmaps/Roadmap_Tu_Junior_12Trieu_Len_Luong_Cao.md)
- Kỹ thuật đàm phán khi đã có tín hiệu/bằng chứng → [`04-Behavioral-And-Salary-Negotiation`](../04-Behavioral-And-Salary-Negotiation/README.md)
- Tín hiệu kỹ thuật thật theo từng mảng để tạo bằng chứng → [`Mastery/Backend-Mastery/05`](../../Backend-Mastery/05-Junior-To-Senior-Problem-Playbook/README.md), [`Mastery/Cloud-DevOps-Mastery/06`](../../Cloud-DevOps-Mastery/06-Junior-To-Senior-Problem-Playbook/README.md)
