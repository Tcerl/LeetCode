# ☁️ AWS CLOUD ARCHITECT: XÂY DỰNG HỆ THỐNG TRÊN MÂY ĐẲNG CẤP THẾ GIỚI

Làm chủ đám mây (Cloud) giúp bạn mở rộng hệ thống không giới hạn. Amazon Web Services (AWS) là nền tảng dẫn đầu thế giới.

---

## 📋 MỤC LỤC
1. [**CƠ BẢN: EC2, S3 VÀ RDS (BỘ BA QUYỀN LỰC)**](#1-cơ-bản-ec2-s3-và-rds-bộ-ba-quyền-lực)
2. [**TRUNG CẤP: VPC VÀ NETWORKING (AN NINH MẠNG)**](#2-trung-cấp-vpc-và-networking-an-ninh-mạng)
3. [**NÂNG CAO: LAMBDA VÀ SERVERLESS (TIẾT KIỆM CHI PHÍ)**](#3-nâng-cao-lambda-và-serverless-tiết-kiệm-chi-phí)
4. [**KIẾN TRÚC: AWS WELL-ARCHITECTED FRAMEWORK**](#4-kiến-trúc-aws-well-architected-framework)

---

## 🟢 1. CƠ BẢN: BỘ KHUNG CỨNG
- **EC2 (Elastic Compute Cloud):** Thuê máy chủ ảo để chạy app Python.
- **S3 (Simple Storage Service):** Lưu trữ hàng tỷ ảnh, video của người dùng với giá siêu rẻ.
- **RDS (Relational Database Service):** Postgres/MySQL được AWS quản lý hoàn toàn (Tự động backup, tự động mở rộng).

---

## 🟡 2. TRUNG CẤP: AN NINH MẠNG (VPC)
Senior không bao giờ mở cổng Database ra internet. Họ tạo một **VPC (Virtual Private Cloud)**:
- **Public Subnet:** Chạy Load Balancer (Cổng đón khách).
- **Private Subnet:** Chạy App và Database (Khu vực nội bộ an toàn tuyệt đối).

---

## 🔴 3. NÂNG CAO: SERVERLESS (BAO NHIÊU DÙNG BẤY NHIÊU)
- **AWS Lambda:** Bạn chỉ viết code, AWS lo phần chạy. Bạn không cần thuê server, chỉ trả tiền cho mỗi mili giây code chạy.
- **API Gateway:** Cửa ngõ quản lý hàng triệu API của bạn một cách tập trung.

---

## 🚀 4. AWS WELL-ARCHITECTED FRAMEWORK
Để xây dựng một hệ thống "không bao giờ sập", Senior tuân theo 5 cột trụ:
1. **Operational Excellence:** Tự động hóa mọi thứ.
2. **Security:** Bảo mật đa lớp (IAM, Security Groups).
3. **Reliability:** Khả năng phục hồi dữ liệu tức thì.
4. **Performance Efficiency:** Không lãng phí tài nguyên.
5. **Cost Optimization:** Chỉ trả tiền cho những gì thực sự mang lại giá trị.

---
🚀 **Triết lý Cloud:** Đừng quản lý máy móc, hãy quản lý dịch vụ. Hãy tập trung vào giá trị kinh doanh!
