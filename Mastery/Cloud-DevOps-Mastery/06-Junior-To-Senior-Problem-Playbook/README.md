# 06. Lộ Trình Vấn Đề Thật: Từ Junior Đến Senior (Cloud & DevOps)

> Tổng hợp lại các vấn đề đã nhắc ở Module 01-05, sắp xếp theo cấp độ để tự định vị và biết bước tiếp theo cần học.

---

## 🟢 Cấp độ Junior — "Deploy được, chưa biết mình đang mở toang rủi ro gì"

| Vấn đề gặp phải | Vì sao xảy ra | Cách vượt qua | Đọc thêm |
|---|---|---|---|
| Mở security group `0.0.0.0/0` cho SSH/RDS "để dễ debug" | Chưa hiểu hậu quả thật của việc để data tier public | Học nguyên tắc bất di bất dịch: data tier KHÔNG BAO GIỜ có route trực tiếp ra internet | [`01`](../01-Cloud-Foundations-Real-Decisions/README.md) |
| Gán `AdministratorAccess`/Access Key tĩnh cho script CI/CD "cho tiện" | Chưa hiểu rủi ro rò rỉ credential tĩnh | Luôn dùng IAM Role thay vì Access Key khi có thể (Instance Profile, OIDC) | [`01`](../01-Cloud-Foundations-Real-Decisions/README.md) |
| Cuối tháng nhận hóa đơn AWS cao bất thường, không biết vì sao | Quên tắt NAT Gateway/snapshot cũ, chưa có thói quen review chi phí định kỳ | Tập thói quen check Cost Explorer hàng tuần, đặt budget alert | [`01`](../01-Cloud-Foundations-Real-Decisions/README.md) |
| Chạy container bằng user root vì "không nghĩ tới việc đó" | Chưa có ý thức bảo mật container | Luôn thêm `USER appuser` trong Dockerfile, học multi-stage build | [`03`](../03-Container-Orchestration-In-Practice/README.md) |

**Bài học junior cần khắc cốt ghi tâm:** *Cloud cho phép làm mọi thứ dễ dàng — kể cả những thứ nguy hiểm. "Chạy được" không có nghĩa là "an toàn" hay "đúng chi phí".*

---

## 🟡 Cấp độ Mid-level — "Biết cấu hình đúng, nhưng chưa lường hết vận hành thật"

| Vấn đề gặp phải | Vì sao xảy ra | Cách vượt qua | Đọc thêm |
|---|---|---|---|
| Pod bị restart liên tục dù app không hề treo | Nhầm liveness và readiness probe, dùng chung 1 endpoint kiểm tra cả dependency ngoài | Tách rõ: liveness chỉ tự kiểm tra process, readiness mới check dependency ngoài | [`03`](../03-Container-Orchestration-In-Practice/README.md) |
| Auto Scaling thêm instance nhưng vẫn có khoảng thời gian hệ thống quá tải/timeout | Đặt ngưỡng scale-out quá sát (90%), không đủ buffer cho thời gian khởi động instance mới | Scale ở ngưỡng 60-70%, có buffer thời gian | [`02`](../02-Compute-Choices-EC2-Lambda-Containers/README.md) |
| Deploy xong, user báo lỗi 502 thoáng qua dù pipeline báo "thành công" | Chưa cấu hình graceful shutdown (`preStop`, `terminationGracePeriodSeconds`) | Cho pod cũ thời gian hoàn thành request đang xử lý trước khi bị kill | [`03`](../03-Container-Orchestration-In-Practice/README.md) |
| Alert bắn liên tục, dần dần cả team bỏ qua alert | Alert quá nhạy, không actionable, theo chỉ số nội bộ (CPU) thay vì triệu chứng user cảm nhận (error rate) | Thiết kế lại alert theo Golden Signals, mỗi alert có runbook | [`05`](../05-Observability-Incident-Response/README.md) |

**Bài học mid-level cần khắc cốt ghi tâm:** *Cấu hình "đúng theo tài liệu" chưa chắc "đúng khi vận hành thật" — luôn tự hỏi "điều gì xảy ra ở BIÊN của cấu hình này" (lúc scale, lúc deploy, lúc lỗi mạng tạm thời).*

---

## 🔴 Cấp độ Senior — "Thiết kế chiến lược vận hành cho cả tổ chức, không chỉ 1 service"

| Vấn đề gặp phải (ở tầm hệ thống) | Senior xử lý thế nào | Đọc thêm |
|---|---|---|
| Mỗi lần deploy đều hồi hộp, rollback thủ công mất nhiều phút gây downtime thật | Thiết kế lại chiến lược deploy (canary + feature flag + auto-rollback theo metric), không phụ thuộc con người phản ứng kịp | [`04`](../04-CICD-Deployment-Strategies/README.md) |
| Sự cố xảy ra, team hoảng loạn cố fix ngay nguyên nhân gốc thay vì ổn định trước | Xây dựng quy trình Incident Response chuẩn (mitigate trước, điều tra sau), đào tạo on-call | [`05`](../05-Observability-Incident-Response/README.md) |
| Cùng 1 loại sự cố lặp lại nhiều lần dù đã "fix" trước đó | Áp dụng văn hóa blameless postmortem có action item cụ thể, theo dõi tới khi thật sự triển khai | [`05`](../05-Observability-Incident-Response/README.md) |
| Team chọn kiến trúc phức tạp (nhiều service, nhiều DB) vượt quá năng lực vận hành thật của team | Đánh giá lại kiến trúc theo năng lực vận hành thật ("ai trực lúc 2h sáng"), không chỉ theo lý thuyết scale | [`../Frontend-Fullstack-Mastery/04`](../../Frontend-Fullstack-Mastery/04-Real-World-Project-Case-Study/README.md) |
| Chi phí cloud tăng không kiểm soát khi công ty scale | Thiết kế cost governance ở tầm tổ chức (tagging chuẩn, budget alert tự động, review kiến trúc định kỳ theo chi phí) | [`01`](../01-Cloud-Foundations-Real-Decisions/README.md) |

**Bài học senior cần khắc cốt ghi tâm:** *Senior chịu trách nhiệm về ĐỘ TIN CẬY và CHI PHÍ ở quy mô tổ chức — không chỉ "service của tôi chạy được" mà "cả hệ thống có thể vận hành bền vững bởi cả team, không chỉ 1 người".*

---

## 🗺️ Lộ trình tổng hợp để tự đánh giá bản thân đang ở đâu

```
Junior  → Deploy/cấu hình được theo hướng dẫn, CHƯA lường hết rủi ro bảo mật/chi phí
            │ (dấu hiệu sẵn sàng lên Mid: tự đọc kỹ tài liệu trước khi cấu hình,
            │  chủ động hỏi "còn rủi ro gì mình chưa thấy?")
            ▼
Mid     → Cấu hình đúng, hiểu vận hành thật (probe, scaling, alert) nhưng vẫn theo
          từng service riêng lẻ
            │ (dấu hiệu sẵn sàng lên Senior: nhận diện được vấn đề LẶP LẠI ở nhiều
            │  service, đề xuất giải pháp/quy trình chung cho cả team)
            ▼
Senior  → Thiết kế chiến lược vận hành (deploy, incident response, cost) ở tầm
          tổ chức, chịu trách nhiệm về độ tin cậy bền vững
```

## 🔗 Liên kết
Chi tiết kỹ thuật: [`01`](../01-Cloud-Foundations-Real-Decisions/README.md) · [`02`](../02-Compute-Choices-EC2-Lambda-Containers/README.md) · [`03`](../03-Container-Orchestration-In-Practice/README.md) · [`04`](../04-CICD-Deployment-Strategies/README.md) · [`05`](../05-Observability-Incident-Response/README.md)
Ứng dụng backend chạy trên hạ tầng này: [`../Backend-Mastery/`](../../Backend-Mastery/INDEX.md)
