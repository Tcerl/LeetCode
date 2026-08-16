# 02. EC2 vs Lambda vs Container — Khung Ra Quyết Định Thật

> Chi tiết dịch vụ đã có ở [`AWS_Architecture_Deep_Dive.md`](../../../07-AWS-Mastery/AWS_Architecture_Deep_Dive.md) mục 3 và [`Cloud_Architecture_AWS_Expert.md`](../../../10-DevOps-Architect/Cloud_Architecture_AWS_Expert.md) mục 3. File này tập trung vào **tiêu chí chọn** thay vì liệt kê tính năng.

---

## 1. Bảng quyết định nhanh

| Tiêu chí | EC2 (VM truyền thống) | Container (ECS/EKS) | Lambda (Serverless) |
|---|---|---|---|
| Traffic pattern | Ổn định, dự đoán được | Ổn định-biến động vừa phải | Rất biến động, có lúc = 0 |
| Thời gian xử lý mỗi request | Không giới hạn | Không giới hạn | **Giới hạn cứng 15 phút** |
| Cold start | Không (luôn chạy) | Thấp (image đã pull sẵn) | **Có** — ảnh hưởng latency lần gọi đầu |
| Chi phí khi traffic = 0 | Vẫn trả tiền (server luôn bật) | Vẫn trả tiền (trừ khi scale-to-zero) | **$0** — chỉ trả theo lượt gọi thật |
| Kiểm soát hạ tầng (OS, network tuning) | Toàn quyền | Vừa phải | Gần như không |
| Phù hợp | Legacy app, cần custom OS/kernel | Microservices, cần đóng gói nhất quán dev↔prod | Xử lý sự kiện ngắn (webhook, xử lý ảnh upload, cron nhỏ) |

**Nguyên tắc senior:** không có lựa chọn "tốt nhất tuyệt đối" — chỉ có lựa chọn **đúng với traffic pattern và ràng buộc nghiệp vụ**. Một hệ thống thật thường **kết hợp cả 3**: API chính chạy trên container (ECS/EKS) vì cần chạy liên tục và kiểm soát tốt, xử lý ảnh/video upload chạy Lambda (event-driven, tiết kiệm chi phí khi ít traffic), và 1-2 service legacy đặc thù vẫn giữ trên EC2.

---

## 2. Cold Start — vấn đề thật của Lambda mà tài liệu marketing ít nhắc

Khi Lambda không được gọi trong 1 khoảng thời gian, container chạy nó bị thu hồi. Lần gọi tiếp theo phải khởi tạo lại từ đầu (tải code, khởi động runtime) — có thể mất **vài trăm ms tới vài giây**, đặc biệt với runtime nặng (Java, .NET) hoặc package lớn.

**Ảnh hưởng thật:** API dùng Lambda cho luồng người dùng tương tác trực tiếp (không phải background job) có thể gây trải nghiệm giật cục ngẫu nhiên — request đôi khi nhanh (50ms), đôi khi chậm bất thường (2s) tùy có đang "nguội" hay không.

**Giải pháp senior thực tế:**
- **Provisioned Concurrency:** trả thêm phí để giữ sẵn N instance "nóng" — dùng cho API quan trọng, traffic có thể dự đoán theo giờ cao điểm.
- Chọn runtime nhẹ (Python/Node) thay vì Java/.NET nếu cold start là yếu tố quan trọng.
- Với luồng cực kỳ nhạy cảm về latency, cân nhắc container thay vì Lambda ngay từ đầu.

---

## 3. Auto Scaling — cấu hình sai gây sự cố thật (thundering herd)

```
Traffic tăng đột biến → CloudWatch alarm trigger → Auto Scaling thêm instance mới
      → Instance mới CẦN THỜI GIAN khởi động (health check pass)
      → Trong lúc chờ, instance CŨ vẫn quá tải → có thể timeout/crash trước khi instance mới kịp gánh tải
```

**Nguyên tắc senior áp dụng:**
- **Scale trước khi cần, không phải sau khi quá tải:** đặt ngưỡng scale-out ở 60-70% tải (không đợi tới 90%) để có buffer thời gian cho instance mới khởi động.
- **Health check phải phản ánh đúng "sẵn sàng phục vụ"**, không chỉ "process đang chạy" — nếu app cần warm-up cache/kết nối DB trước khi nhận traffic, health check phải đợi đúng bước đó, nếu không Load Balancer sẽ đẩy traffic vào instance chưa sẵn sàng.
- **Scale-in (giảm instance) phải chậm hơn scale-out** — tránh dao động liên tục (flapping) khi traffic dao động nhẹ quanh ngưỡng.

---

## 🎯 Câu hỏi senior hay hỏi khi review

1. "Tác vụ này có khả năng chạy quá 15 phút không? Nếu có, Lambda không phải lựa chọn phù hợp."
2. "Cold start của Lambda này có ảnh hưởng tới trải nghiệm người dùng thật không, hay chỉ dùng cho background job?"
3. "Auto Scaling của bạn scale ở ngưỡng nào — có đủ buffer thời gian cho instance mới khởi động trước khi hệ thống quá tải không?"

## 🔗 Liên kết module khác
- Container thật sự vận hành thế nào (Docker/K8s) → [`03-Container-Orchestration-In-Practice`](../03-Container-Orchestration-In-Practice/README.md)
- Nền tảng VPC/IAM cho compute → [`01-Cloud-Foundations-Real-Decisions`](../01-Cloud-Foundations-Real-Decisions/README.md)
