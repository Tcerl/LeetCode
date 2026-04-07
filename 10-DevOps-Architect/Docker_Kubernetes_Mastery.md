# 🐳 DOCKER & KUBERNETES MASTER: TỰ ĐỘNG HÓA VÀ ĐÓNG GÓI HỆ THỐNG

Docker là chuẩn mực để chạy code của bạn ở mọi nơi mà không lo lỗi môi trường ("It works on my machine"). Kubernetes (K8s) là "nhạc trưởng" điều phối hàng nghìn Docker đó.

---

## 📋 MỤC LỤC
1. [**CƠ BẢN: DOCKERFILE VÀ IMAGE TỐI ƯU**](#1-cơ-bản-dockerfile-và-image-tối-ưu)
2. [**TRUNG CẤP: DOCKER COMPOSE (CHẠY ĐA DỊCH VỤ)**](#2-trung-cấp-docker-compose-chạy-đa-dịch-vụ)
3. [**NÂNG CAO: KUBERNETES (PODS, SERVICES, DEPLOYMENTS)**](#3-nâng-cao-kubernetes-pods-services-deployments)
4. [**⭐ SENIOR DOCKER: MULTI-STAGE BUILDS**](#-senior-docker-multi-stage-builds)

---

## 🟢 1. CƠ BẢN: DOCKERFILE VÀ IMAGE TỐI ƯU

### 📦 A. Dockerfile chuyên nghiệp
Đừng dùng các image nặng nề. Hãy dùng bản **Alpine** hoặc **Slim** của Python để giảm kích thước Image từ 1GB xuống còn 100MB.

### 🧱 B. Các lệnh quan trọng
- `FROM python:3.9-slim`: Chọn hệ điều hành nhẹ.
- `WORKDIR /app`: Đặt thư mục làm việc.
- `pip install --no-cache-dir`: Tiết kiệm dung lượng ổ cứng.

---

## 🟡 2. TRUNG CẤP: DOCKER COMPOSE

Đây là "nút bấm thần kỳ" để khởi động toàn bộ app gồm: **Flask + Postgres + Redis + Nginx** chỉ bằng 1 lệnh `docker-compose up`.

- **Volumes:** Giúp dữ liệu Database không bị mất khi Docker bị tắt.
- **Networks:** Giúp các Docker "nói chuyện" với nhau một cách bảo mật trong mạng nội bộ.

---

## 🔴 3. NÂNG CAO: KUBERNETES (K8S)

Khi hệ thống của bạn quá lớn cho một Server đơn lẻ, K8s sẽ giúp:
- **Auto-healing:** Nếu 1 Docker bị sập, K8s tự động khởi động lại cái mới thay thế.
- **Auto-scaling:** Khi có hàng triệu người vào cùng lúc, K8s tự động nhân bản thêm nhiều Docker để gánh tải.
- **Rolling Update:** Cập nhật phiên bản mới của app mà không làm gián đoạn người dùng (Zero downtime).

---

## ⭐ 4. SENIOR DOCKER: MULTI-STAGE BUILDS

Đây là kỹ thuật đỉnh cao:
1. Giai đoạn 1: Dùng Image nặng để cài đặt thư viện và build code.
2. Giai đoạn 2: Chỉ copy file đã build sang một Image siêu nhẹ để chạy.
=> Kết quả: Image của bạn sẽ cực kỳ bảo mật (vì không có mã nguồn gốc) và tải cực nhanh lên Server.

---
🚀 **Triết lý DevOps:** Hãy coi Server là gia súc (Cattle), không phải thú cưng (Pet). Nếu cái nào hỏng, hãy tự động thay thế cái mới!
