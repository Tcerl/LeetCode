# 04. Câu Hỏi Hành Vi (Behavioral) & Đàm Phán Lương

> Câu hỏi HR cụ thể đã có ở [`CODE_EXERCISES.md`](../../../06-Exercises/CODE_EXERCISES.md) (mục "Câu Hỏi HR Thường Gặp"). File này bổ sung **khung trả lời** và **chiến lược đàm phán** — phần thường bị xem nhẹ nhưng ảnh hưởng trực tiếp tới thu nhập thật.

---

## 1. Khung STAR — công thức kể chuyện chuyên nghiệp

**S**ituation (Bối cảnh) → **T**ask (Nhiệm vụ) → **A**ction (Hành động CỤ THỂ bạn làm) → **R**esult (Kết quả, có số liệu nếu có thể).

> Câu hỏi: *"Kể về 1 lần bạn gặp bug khó và cách giải quyết."*
>
> - **S:** "Hệ thống thanh toán bị lỗi double-charge cho khoảng 0.1% giao dịch, chỉ xảy ra khi user bấm nút submit nhanh liên tiếp."
> - **T:** "Em được giao điều tra và fix trong vòng 2 ngày vì ảnh hưởng trực tiếp tới tiền của khách hàng."
> - **A:** "Em xác định đây là race condition — 2 request gần như đồng thời cùng đọc trạng thái đơn hàng là 'chưa thanh toán' trước khi cái nào kịp cập nhật. Em fix bằng cách thêm unique constraint ở DB kết hợp idempotency key gửi từ client, thay vì chỉ dựa vào check ở tầng application."
> - **R:** "Sau khi deploy, tỷ lệ lỗi giảm về 0 trong 3 tháng theo dõi tiếp theo, và em viết thêm postmortem để team áp dụng idempotency key cho toàn bộ API thanh toán khác."

**Vì sao khung này hiệu quả:** nó buộc bạn kể chuyện có **hành động cụ thể của chính bạn** (không phải "team em đã...") và **kết quả đo lường được** — đây chính xác là điều nhà tuyển dụng senior muốn nghe, khác hẳn kể lể chung chung.

---

## 2. Chuẩn bị sẵn 4-5 câu chuyện "lõi" — dùng linh hoạt cho nhiều câu hỏi khác nhau

Không cần chuẩn bị câu trả lời riêng cho từng câu hỏi HR có thể hỏi (quá nhiều, không nhớ hết). Thay vào đó chuẩn bị sẵn **4-5 tình huống thật đã trải qua**, mỗi tình huống có thể "biến hóa" trả lời cho nhiều loại câu hỏi:

| Câu chuyện lõi | Dùng trả lời cho câu hỏi dạng |
|---|---|
| 1 lần bug khó đã giải quyết | "Thử thách kỹ thuật khó nhất", "Cách bạn debug vấn đề phức tạp" |
| 1 lần bất đồng quan điểm kỹ thuật với đồng nghiệp | "Xử lý xung đột", "Thuyết phục người khác theo ý kiến của bạn" |
| 1 lần deadline gấp / ưu tiên công việc | "Quản lý thời gian", "Áp lực công việc" |
| 1 lần mắc lỗi và cách khắc phục | "Điểm yếu của bạn", "Bài học từ thất bại" |
| 1 lần chủ động đề xuất cải tiến ngoài phạm vi được giao | "Chủ động trong công việc", "Đóng góp ngoài JD" |

---

## 3. Đàm phán lương — nguyên tắc thực tế, không phải mẹo vặt

- **Không nói con số trước nếu có thể tránh:** nếu được hỏi "mức lương mong muốn", có thể trả lời "Em muốn tìm hiểu thêm về phạm vi công việc trước, nhưng em tin công ty có mức lương cạnh tranh cho vị trí này theo thị trường — anh/chị có thể chia sẻ range cho vị trí này không?" — người hỏi trước ở thế bất lợi hơn trong đàm phán.
- **Luôn có khoảng (range), không phải 1 con số cố định**, và neo mức thấp nhất trong range = mức bạn *thật sự chấp nhận được*, không phải mức bạn mong muốn tối đa.
- **Tổng thu nhập (Total Compensation), không chỉ lương gross:** thưởng, bảo hiểm, số ngày nghỉ phép, chính sách làm việc từ xa, ngân sách học tập — tất cả đều có giá trị quy đổi.
- **Có offer khác là đòn bẩy mạnh nhất** — nhưng phải trung thực, không bịa offer giả (rủi ro uy tín rất lớn nếu bị phát hiện, và ngành công nghệ khá "nhỏ", tin đồn lan nhanh).
- **Im lặng là công cụ:** sau khi nêu con số mong muốn, đừng vội nói thêm để "giải thích/xin lỗi" — để khoảng lặng cho phía tuyển dụng phản hồi.

---

## 4. Câu hỏi ngược lại nhà tuyển dụng — thể hiện tư duy senior

Thay vì hỏi chung chung ("Văn hóa công ty thế nào?"), hỏi câu cho thấy bạn đã tư duy như người sẽ làm việc thật:

- "Đâu là thử thách kỹ thuật lớn nhất team đang đối mặt trong 6 tháng tới?"
- "Quy trình xử lý sự cố (incident response) của team hiện tại ra sao — có postmortem văn hóa không?" *(liên kết trực tiếp [`Cloud-DevOps-Mastery/05`](../../Cloud-DevOps-Mastery/05-Observability-Incident-Response/README.md) — hỏi câu này còn cho thấy bạn hiểu vận hành thật)*
- "Technical debt lớn nhất hiện tại của hệ thống là gì, và có kế hoạch giải quyết không?"

---

## 🎯 Checklist chuẩn bị

1. Đã viết ra 4-5 câu chuyện lõi theo khung STAR, có số liệu kết quả cụ thể chưa?
2. Đã xác định rõ range lương chấp nhận được (dựa trên nghiên cứu thị trường thật, không đoán) chưa?
3. Đã chuẩn bị 3 câu hỏi ngược lại thể hiện tư duy chủ động chưa?

## 🔗 Liên kết module khác
- Nguồn nguyên liệu cho các câu chuyện kỹ thuật thật → toàn bộ [`../DSA-Mastery/`](../../DSA-Mastery/INDEX.md), [`../Backend-Mastery/`](../../Backend-Mastery/INDEX.md), [`../Cloud-DevOps-Mastery/`](../../Cloud-DevOps-Mastery/INDEX.md)
- Tư duy senior đứng sau cách kể chuyện này → [`01-Senior-Mindset-And-Career-Reality`](../01-Senior-Mindset-And-Career-Reality/README.md)
