# 🌳 Cloud-DevOps-Mastery — Cây Kiến Thức Cloud & Vận Hành Hệ Thống (Senior Companion)

> **Mục đích:** Lớp kiến thức bổ sung cho [`07-AWS-Mastery/`](../../07-AWS-Mastery/) và [`10-DevOps-Architect/`](../../10-DevOps-Architect/). Hai thư mục đó đã giải thích chi tiết TỪNG dịch vụ (VPC, EC2, Docker, K8s...). Cây này tập trung vào **quyết định kiến trúc thật, sự cố production thật, và quy trình vận hành** — thứ chỉ có được từ kinh nghiệm vận hành hệ thống thật, không nằm trong tài liệu tính năng dịch vụ.

---

## 📋 MỤC LỤC

| # | Module | Chủ đề | Nguồn lý thuyết liên quan |
|---|---|---|---|
| 01 | [Cloud Foundations: Real Decisions](01-Cloud-Foundations-Real-Decisions/README.md) | VPC design an toàn, IAM least-privilege thật sự, kiểm soát chi phí | `AWS_Architecture_Deep_Dive.md`, `AWS_Knowledge_Handbook_VN.md` |
| 02 | [Compute Choices](02-Compute-Choices-EC2-Lambda-Containers/README.md) | EC2 vs Container vs Lambda, cold start, auto scaling đúng cách | `Cloud_Architecture_AWS_Expert.md` |
| 03 | [Container Orchestration In Practice](03-Container-Orchestration-In-Practice/README.md) | Image an toàn, resource limits, liveness/readiness, rolling update | `Docker_Kubernetes_Mastery.md` |
| 04 | [CI/CD Deployment Strategies](04-CICD-Deployment-Strategies/README.md) | Blue-green/canary, feature flag, migration an toàn, pipeline gates | `CI_CD_Automation_GithubActions.md` |
| 05 | [Observability & Incident Response](05-Observability-Incident-Response/README.md) | SLI/SLO/SLA, Golden Signals, quy trình xử lý sự cố, postmortem | `AWS_Knowledge_Handbook_VN.md` mục 8 |
| 06 | [Junior-To-Senior Problem Playbook](06-Junior-To-Senior-Problem-Playbook/README.md) | Vấn đề thật + giải pháp, sắp xếp theo cấp độ Junior/Mid/Senior | Tổng hợp Module 01-05 |
| 07 | [Real-World War Stories Fresher-To-Senior](07-Real-World-War-Stories-Fresher-To-Senior/README.md) | 12 sự cố production kể đầy đủ (bối cảnh → nguyên nhân gốc → cách sửa → bài học), 3 mỗi cấp độ, nguyên liệu STAR cho phỏng vấn | Tổng hợp Module 01-06 + kinh nghiệm thực chiến |

---

## 🗺️ Sơ đồ liên hệ

```
01-Cloud Foundations (nền móng bảo mật + chi phí)
        │
        ▼
02-Compute Choices ──> 03-Container Orchestration (nếu chọn container)
        │                        │
        └────────────┬───────────┘
                      ▼
        04-CI/CD Deployment Strategies (đưa thay đổi lên an toàn)
                      ▼
        05-Observability & Incident Response (giám sát + phản ứng khi có sự cố)
```

## Cách dùng
1. Đọc chi tiết dịch vụ cụ thể ở `07-AWS-Mastery/` và `10-DevOps-Architect/` trước.
2. Đọc cây này để hiểu **khi nào chọn gì, và điều gì thật sự xảy ra khi vận hành sai** — đây là nội dung phân biệt senior với người chỉ biết cú pháp/tính năng dịch vụ.
3. Mỗi module có mục 🎯 câu hỏi senior — dùng làm checklist tự review kiến trúc hoặc chuẩn bị phỏng vấn system design.

## 🔗 Liên kết sang các cây khác
- Ứng dụng backend được triển khai lên hạ tầng này → [`../Backend-Mastery/`](../Backend-Mastery/INDEX.md)
- Cấu trúc dữ liệu nền tảng cho các thuật toán scheduling/routing thật (K8s scheduler, load balancer) → [`../DSA-Mastery/`](../DSA-Mastery/INDEX.md)
- Biến kinh nghiệm sự cố (Module 07) thành bằng chứng tăng lương → [`../Career-Mastery/05`](../Career-Mastery/05-Salary-Growth-Playbook/README.md)
