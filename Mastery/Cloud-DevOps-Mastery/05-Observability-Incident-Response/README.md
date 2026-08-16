# 05. Giám Sát Hạ Tầng & Xử Lý Sự Cố (Incident Response)

> CloudWatch/CloudTrail đã có ở [`AWS_Knowledge_Handbook_VN.md`](../../07-AWS-Mastery/AWS_Knowledge_Handbook_VN.md) mục 8. File này bổ sung **quy trình vận hành khi có sự cố thật** — mảng kiến thức thực chiến nhất của một senior/on-call engineer.

---

## 1. SLI / SLO / SLA — ngôn ngữ chung để nói về "đủ tốt"

| Khái niệm | Ý nghĩa | Ví dụ thật |
|---|---|---|
| **SLI** (Service Level Indicator) | Chỉ số đo lường thực tế | "99.95% request trả về < 200ms trong 30 ngày qua" |
| **SLO** (Objective) | Mục tiêu nội bộ team đặt ra | "SLO: p99 latency < 300ms, uptime > 99.9%" |
| **SLA** (Agreement) | Cam kết với khách hàng, có ràng buộc (thường kèm bồi thường) | "SLA: uptime 99.9%, nếu vi phạm hoàn tiền X%" |

**Vì sao senior cần hiểu khác biệt này:** SLO luôn phải **chặt hơn** SLA (có buffer an toàn), vì SLA là cam kết pháp lý còn SLO là mục tiêu nội bộ để chủ động cảnh báo TRƯỚC khi vi phạm SLA. Đây cũng là nền tảng của khái niệm **Error Budget** — nếu hệ thống đang chạy tốt hơn SLO nhiều, team có "ngân sách rủi ro" để deploy nhanh hơn, thử nghiệm nhiều hơn; nếu đang sát ngưỡng SLO, team nên ưu tiên ổn định hơn tính năng mới.

---

## 2. Golden Signals — 4 chỉ số senior luôn theo dõi đầu tiên

1. **Latency** — thời gian phản hồi (tách riêng request thành công vs lỗi, vì request lỗi thường nhanh bất thường và làm méo số liệu trung bình).
2. **Traffic** — số lượng request/giây.
3. **Errors** — tỷ lệ request lỗi (4xx do client, 5xx do server — phải tách riêng để biết lỗi ở đâu).
4. **Saturation** — hệ thống đang "đầy" tới mức nào (CPU, RAM, connection pool, queue depth).

**Nguyên tắc thực chiến:** khi có sự cố, luôn nhìn 4 chỉ số này TRƯỚC khi đọc code — chúng cho biết ngay **loại vấn đề** (traffic tăng đột biến? saturation ở tầng nào? lỗi tập trung ở endpoint nào?) để định hướng điều tra đúng chỗ thay vì đoán mò.

---

## 3. Quy trình xử lý sự cố (Incident Response) — các bước senior thực hiện theo thứ tự

```
1. PHÁT HIỆN (alert bắn / user báo cáo)
2. ĐÁNH GIÁ MỨC ĐỘ (Severity) — ảnh hưởng bao nhiêu % user? Có mất dữ liệu không?
3. GIẢM THIỂU NGAY (Mitigate) — ƯU TIÊN SỐ 1, KHÔNG PHẢI tìm nguyên nhân gốc trước
   → rollback deploy gần nhất? tắt feature flag? scale thêm instance? failover sang region khác?
4. THÔNG BÁO (Communicate) — cập nhật status page, thông báo nội bộ/khách hàng
5. XÁC NHẬN ĐÃ ỔN (Verify) — theo dõi golden signals trở lại bình thường
6. ĐIỀU TRA NGUYÊN NHÂN GỐC (Root Cause Analysis) — SAU KHI đã ổn định, không vội trong lúc đang cháy
7. POSTMORTEM — viết báo cáo blameless, hành động phòng ngừa cụ thể
```

**Sai lầm senior luôn cảnh báo junior:** cố gắng tìm và fix "nguyên nhân gốc" NGAY trong lúc sự cố đang diễn ra thay vì **giảm thiểu tác động trước**. Rollback về bản deploy trước đó thường nhanh hơn và an toàn hơn nhiều so với "vá nóng" (hotfix) ngay giữa sự cố — vá nóng dễ tạo ra bug thứ hai chồng lên bug thứ nhất.

---

## 4. Postmortem — văn hóa quan trọng nhất phân biệt team trưởng thành

**Blameless postmortem** (không quy trách nhiệm cá nhân) là nguyên tắc bắt buộc trong ngành: mục tiêu là hiểu **hệ thống/quy trình** đã cho phép lỗi xảy ra, không phải "ai đã bấm nút sai". Một postmortem tốt bao gồm:

- **Timeline chi tiết:** lúc nào phát hiện, lúc nào mitigate, lúc nào giải quyết xong.
- **Impact:** ảnh hưởng bao nhiêu user, bao lâu, thiệt hại gì.
- **5 Whys** hoặc kỹ thuật tương tự để đào tới nguyên nhân gốc thật sự (thường là vấn đề quy trình: thiếu test, thiếu alert, thiếu review — không phải "dev đó code dở").
- **Action items cụ thể, có người phụ trách, có deadline** — postmortem không tạo ra hành động cụ thể thì chỉ là kể chuyện, không cải thiện được gì.

**Vì sao đây là kỹ năng senior thật sự:** hệ thống lớn nào cũng sẽ có sự cố — điều phân biệt team giỏi không phải "không bao giờ có sự cố" mà là **học được gì và không lặp lại cùng 1 loại sự cố 2 lần**.

---

## 🎯 Câu hỏi senior hay hỏi khi review runbook/quy trình

1. "Khi alert này bắn lúc 3h sáng, người trực có đủ thông tin để mitigate trong 5 phút đầu không, hay phải đoán?"
2. "Postmortem gần nhất của team có action item nào đã thực sự được làm chưa, hay chỉ nằm trong document?"
3. "SLO của service này là gì — team có đang track error budget để cân bằng giữa tốc độ ra tính năng mới và độ ổn định không?"

## 🔗 Liên kết module khác
- Nguồn gốc phần lớn sự cố nằm ở tầng compute/container → [`02`](../02-Compute-Choices-EC2-Lambda-Containers/README.md), [`03`](../03-Container-Orchestration-In-Practice/README.md)
- Rollback là công cụ giảm thiểu chính khi deploy gây sự cố → [`04-CICD-Deployment-Strategies`](../04-CICD-Deployment-Strategies/README.md)
- Kỹ năng debug endpoint chậm ở tầng ứng dụng → [`Backend-Mastery/04`](../../Backend-Mastery/04-Testing-Observability-And-Debugging-Prod/README.md)
