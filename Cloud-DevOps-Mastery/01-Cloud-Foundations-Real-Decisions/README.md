# 01. Nền Tảng Cloud — Quyết Định Thật, Không Chỉ Định Nghĩa Dịch Vụ

> Lý thuyết VPC/IAM/S3/RDS chi tiết đã có ở [`AWS_Architecture_Deep_Dive.md`](../../07-AWS-Mastery/AWS_Architecture_Deep_Dive.md) và [`AWS_Knowledge_Handbook_VN.md`](../../07-AWS-Mastery/AWS_Knowledge_Handbook_VN.md). File này bổ sung **tại sao chọn cấu hình này chứ không phải cấu hình khác**, và các sự cố thật khi cấu hình sai.

---

## 1. VPC Design — không phải "tạo cho có", mà là ranh giới bảo mật thật

Senior thiết kế VPC theo nguyên tắc **defense in depth** (nhiều lớp phòng thủ), không chỉ 1 lớp security group:

```
Internet
   │
   ▼
Public Subnet (ALB/NAT Gateway)         ← chỉ đặt thứ BẮT BUỘC phải public
   │
   ▼
Private Subnet — App tier (EC2/ECS)     ← không có địa chỉ IP public, ra internet qua NAT
   │
   ▼
Private Subnet — Data tier (RDS)        ← chỉ App tier được phép kết nối vào, security group hẹp nhất
```

**Sự cố thật kinh điển:** đặt RDS ở **public subnet** để "dễ debug từ máy cá nhân" rồi quên đổi lại — đây là nguyên nhân của rất nhiều vụ rò rỉ dữ liệu có thật trên thế giới (database bị scan tự động bởi bot, brute-force password). Nguyên tắc bất di bất dịch: **data tier không bao giờ có route trực tiếp ra internet**, muốn truy cập từ xa phải qua Bastion Host/VPN/Session Manager.

---

## 2. IAM — nguyên tắc Least Privilege áp dụng thế nào trong thực tế

Lý thuyết ai cũng biết "cấp quyền tối thiểu cần thiết" — vấn đề thật là **làm sao biết "tối thiểu" là bao nhiêu** khi mới bắt đầu:

1. Bắt đầu với **AWS Managed Policy** phù hợp gần nhất (VD: `AmazonS3ReadOnlyAccess`) để không chặn tiến độ ban đầu.
2. Bật **CloudTrail**, theo dõi thực tế service/user đó gọi những API nào trong 2-4 tuần.
3. Dùng **IAM Access Analyzer** để tự động sinh ra policy chỉ chứa đúng các quyền đã thực sự dùng.
4. Thay Managed Policy bằng **Custom Policy hẹp** dựa trên dữ liệu thật đó — đây mới là "least privilege" đúng nghĩa, không phải đoán.

**Sự cố thật:** gán `AdministratorAccess` cho access key của 1 script tự động (CI/CD, Lambda) "cho tiện, sửa sau" — access key đó rò rỉ (commit nhầm lên GitHub public, log bị lộ) đồng nghĩa **toàn bộ tài khoản AWS bị chiếm quyền**. Đây là lý do senior luôn dùng **IAM Role** (tự động xoay vòng credential tạm thời) thay vì Access Key tĩnh bất cứ khi nào có thể (EC2 Instance Profile, Lambda Execution Role, GitHub OIDC cho CI/CD).

---

## 3. Chi phí (Cost) — kỹ năng senior thường bị đánh giá thấp

Cloud tính phí theo usage — thiết kế sai kiến trúc không chỉ chậm mà còn **đốt tiền thật mỗi tháng**:

| Sai lầm chi phí thường gặp | Hậu quả | Cách senior phòng tránh |
|---|---|---|
| Quên tắt NAT Gateway không dùng | Phí theo giờ + theo GB data transfer dù không có traffic | Review định kỳ tài nguyên "zombie" bằng AWS Cost Explorer |
| Data transfer **giữa các Availability Zone** | Tính phí dù cùng 1 VPC | Ưu tiên đặt các service hay giao tiếp nhau trong cùng AZ khi latency không phải yếu tố sống còn |
| Snapshot EBS/RDS tích lũy vô hạn | Phí lưu trữ tăng dần âm thầm mỗi tháng | Lifecycle policy tự động xóa snapshot cũ |
| Over-provisioned EC2 (chọn instance to hơn nhu cầu thật "cho chắc") | Trả tiền cho tài nguyên không dùng tới | Auto Scaling + benchmark tải thật trước khi chọn instance type |

---

## 🎯 Câu hỏi senior hay hỏi khi review kiến trúc

1. "Database của bạn có route trực tiếp ra internet không? Ai có thể SSH/kết nối trực tiếp vào nó?"
2. "IAM Role này có quyền gì — bạn dựa vào managed policy mặc định hay đã audit theo usage thật?"
3. "Kiến trúc này chi phí bao nhiêu/tháng ở quy mô hiện tại, và ở quy mô gấp 10 lần?"

## 🔗 Liên kết module khác
- Chọn compute phù hợp (EC2 vs Lambda vs Container) → [`02-Compute-Choices-EC2-Lambda-Containers`](../02-Compute-Choices-EC2-Lambda-Containers/README.md)
- Giám sát chi phí & bảo mật liên tục → [`05-Observability-Incident-Response`](../05-Observability-Incident-Response/README.md)
