# ✅ Checklist & Hướng Dẫn Thực Hành Chi Tiết Bài Tập DevOps (DO-01 → DO-06)

> **Mục tiêu:** Đạt trình độ **Backend Developer tự deploy, tự vận hành và tự debug hệ thống (Production Troubleshooting)**. Nắm vững bản chất mạng Container, Persistence Storage Volume, CI/CD Pipeline Lifecycle, Kubernetes Pod Scheduling/Service Routing và Kỹ năng xử lý sự cố thực tế (Incident Response).

---

## 📌 Danh Sách Bài Tập & Sự Cố
- [ ] **DO-01 — Multi-container Orchestration với Docker Compose & Persistence Volume** (Tuần 12)
- [ ] **DO-02 — Debugging Container Startup Failures & Log Analysis** (Tuần 12)
- [ ] **DO-03 — CI Pipeline Automation với GitHub Actions** (Tuần 13)
- [ ] **DO-04 — Continuous Deployment (CD) & Infrastructure Integration** (Tuần 15)
- [ ] **DO-05 — Enterprise Secret Management & Vault Hygiene** (Tuần 16)
- [ ] **DO-06 — Kubernetes Foundations: Minikube Deployment & Service** (Tuần 17)

### 🔴 Sub-checklist: Thực Hành Tự Gây Sự Cố & Giải Quyết (Troubleshooting Labs)
- [ ] **LAB-01:** Xử lý sự cố tràn dung lượng đĩa `No space left on device`
- [ ] **LAB-02:** Xóa vết nhạy cảm (Secrets) trong lịch sử Git bằng `git filter-repo`
- [ ] **LAB-03:** Debug lỗi Mismatch Labels/Selector trên K8s Service
- [ ] **LAB-04:** Debug lỗi CI Pipeline Build Fail do Dependency Mismatch
- [ ] **LAB-05:** Debug & Fix Race Condition dữ liệu bằng Database Locks (`SELECT FOR UPDATE`)

---

## 📘 HƯỚNG DẪN THỰC HÀNH CHI TIẾT & GIẢI THÍCH CHUYÊN SÂU

### 1. DO-01 — Docker Compose Đa Dịch Vụ & Persistence Volume
#### 🔬 Giải thích chuyên sâu:
- **Docker Compose Architecture:** Docker Compose khởi tạo một custom Bridge Network riêng biệt (VD: `app_default`). Các container trong cùng network có thể giao tiếp với nhau trực tiếp thông qua **Container Name** nhờ cơ chế DNS nội bộ của Docker Daemon.
- **Named Volume vs Bind Mount:**
  - **Bind Mount:** Map trực tiếp một đường dẫn trên Host Machine vào Container (`./data:/app/data`). Phụ thuộc vào cấu trúc thư mục của OS Host.
  - **Named Volume:** Do Docker tự quản lý trong `/var/lib/docker/volumes/`. Dữ liệu độc lập với lifecycle của container. Khi chạy `docker-compose down`, container bị xóa nhưng Named Volume vẫn tồn tại nguyên vẹn. Dữ liệu chỉ mất khi cố tình chạy `docker-compose down -v`.

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Soạn thảo `docker-compose.yml` (Flask + Postgres + Redis):**
   ```yaml
   version: '3.8'

   services:
     web:
       build: .
       ports:
         - "5000:5000"
       environment:
         - DATABASE_URL=postgresql://user:password@db:5432/mydb
         - REDIS_URL=redis://redis:6379/0
       depends_on:
         - db
         - redis

     db:
       image: postgres:15-alpine
       environment:
         POSTGRES_USER: user
         POSTGRES_PASSWORD: password
         POSTGRES_DB: mydb
       volumes:
         - postgres_data:/var/lib/postgresql/data

     redis:
       image: redis:7-alpine
       ports:
         - "6379:6379"

   volumes:
     postgres_data:  # Named Volume đảm bảo persistence
   ```
2. **Thực hành Verify Persistence Data:**
   - Run: `docker-compose up -d`
   - Gửi POST request tạo Post dữ liệu.
   - Run: `docker-compose down` (Xóa toàn bộ container).
   - Run: `docker-compose up -d` (Tạo lại container).
   - Gửi GET request verify dữ liệu vừa tạo vẫn còn nguyên vẹn!

---

### 2. DO-02 — Debugging Container Startup Failures & Log Analysis
#### 🔬 Giải thích chuyên sâu:
- **Container Lifecycle:** Container là một isolated process chạy lệnh Entrypoint/CMD. Nếu process chính này kết thúc (exit code != 0) thì container sẽ lập tức chuyển sang trạng thái `Exited` hoặc bị restart liên tục (nếu có restart policy).
- **Kỹ năng Debug Container:**
  - `docker logs <container_id>`: Đọc stdout/stderr của process chính trong container.
  - `docker inspect <container_id>`: Kiểm tra chi tiết IP, Mount points, Environment variables, Exit status.
  - `docker exec -it <container_id> /bin/sh`: Truyp cập trực tiếp vào bên trong container để debug file/mạng (chỉ dùng được khi container đang running).

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Cố tình tạo lỗi:**
   - Trong `docker-compose.yml`, sửa `POSTGRES_PASSWORD` của DB thành `wrongpassword`, giữ nguyên env trong service `web`.
2. **Quan sát & Debug:**
   - Chạy `docker-compose up -d`.
   - Quan sát container web bị crash: `docker-compose ps`.
   - Đọc log chi tiết của container crash:
     ```bash
     docker logs flask_app_web_1
     ```
   - Thấy log báo: `sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) fatal: password authentication failed for user "user"`.
3. **Khắc phục:** Sửa lại mật khẩu khớp giữa 2 service và restart.

---

### 3. DO-03 — Pipeline CI Automation với GitHub Actions
#### 🔬 Giải thích chuyên sâu:
- **Continuous Integration (CI):** Là tập hợp các bước tự động kiểm tra code (Linting, Type Checking, Unit Tests, Security Scanning, Container Build) mỗi khi dev push code mới hoặc mở Pull Request.
- **GitHub Actions Runner:** Là máy chủ giả lập (Ubuntu/Windows/macOS) do GitHub cấp. Mỗi job chạy trong một runner hoàn toàn cách ly. `steps` chạy nối tiếp nhau trong cùng 1 job, `jobs` mặc định chạy song song.

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Tạo file `.github/workflows/ci.yml`:**
   ```yaml
   name: Python Backend CI

   on:
     push:
       branches: [ "main", "develop" ]
     pull_request:
       branches: [ "main" ]

   jobs:
     test-and-build:
       runs-on: ubuntu-latest

       steps:
       - name: Checkout Code
         uses: actions/checkout@v3

       - name: Set up Python
         uses: actions/setup-python@v4
         with:
           python-version: '3.11'

       - name: Install Dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -r requirements.txt
           pip install pytest flake8

       - name: Run Code Quality Checks (Linting)
         run: flake8 . --max-line-length=100

       - name: Run Unit Tests
         run: pytest

       - name: Build Docker Image Test
         run: docker build -t my-app:${{ github.sha }} .
   ```
2. **Push code lên GitHub & Kiểm tra tab Actions:** Quan sát quy trình chạy xanh (Passed) đủ các bước.

---

### 4. DO-04 — Continuous Deployment (CD) & Infrastructure Integration
#### 🔬 Giải thích chuyên sâu:
- **Continuous Deployment (CD):** Tự động đóng gói artifact (VD: push Docker Image lên Docker Hub / AWS ECR) và kích hoạt lệnh deploy lên môi trường Staging/Production mà không cần can thiệp thủ công.
- **SSH Deploy Pattern:** GitHub Action mở kết nối SSH an toàn tới máy chủ EC2/VPS từ xa thông qua Private Key lưu trong GitHub Secrets và thực thi lệnh `docker-compose pull && docker-compose up -d`.

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Tạo GitHub Secrets:**
   - Vào Repo Settings -> Secrets and variables -> Actions.
   - Thêm `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `HOST_IP`, `SSH_PRIVATE_KEY`.
2. **Bổ sung CD step vào Workflow (`.github/workflows/ci-cd.yml`):**
   ```yaml
       - name: Log in to Docker Hub
         uses: docker/login-action@v2
         with:
           username: ${{ secrets.DOCKER_USERNAME }}
           password: ${{ secrets.DOCKER_PASSWORD }}

       - name: Build & Push Docker Image
         uses: docker/build-push-action@v4
         with:
           push: true
           tags: ${{ secrets.DOCKER_USERNAME }}/my-flask-app:latest

       - name: Deploy to Remote Server via SSH
         uses: appleboy/ssh-action@v0.1.10
         with:
           host: ${{ secrets.HOST_IP }}
           username: ubuntu
           key: ${{ secrets.SSH_PRIVATE_KEY }}
           script: |
             docker pull ${{ secrets.DOCKER_USERNAME }}/my-flask-app:latest
             docker stop flask_app || true
             docker rm flask_app || true
             docker run -d -p 5000:5000 --name flask_app ${{ secrets.DOCKER_USERNAME }}/my-flask-app:latest
   ```

---

### 5. DO-05 — Enterprise Secret Management & Vault Hygiene
#### 🔬 Giải thích chuyên sâu:
- **Nguyên tắc "Zero Secret in Git":** Không bao giờ commit credentials, API keys, JWT Secret Key, DB Passwords vào mã nguồn Git. Khi nhỡ commit secret vào Git history, kể cả khi tạo commit mới để xóa file thì secret vẫn nằm trong lịch sử commit cũ và có thể bị hacker scan tự động (dùng công cụ như GitGuardian/TruffleHog).
- **Environment Variables Injection:** Ứng dụng đọc cấu hình qua `os.getenv()` lúc runtime. Cấu hình được nạp từ file `.env` local (được add vào `.gitignore`) hoặc truyền từ Docker/Kubernetes ConfigMap & Secrets.

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Cấu hình `.gitignore` chuẩn:**
   ```text
   .env
   *.pem
   __pycache__/
   *.sqlite3
   ```
2. **Thực hành dùng `python-dotenv` trong code Python:**
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()  # Nạp từ file .env

   SECRET_KEY = os.getenv("SECRET_KEY", "fallback-dev-key")
   DB_PASS = os.getenv("DATABASE_PASSWORD")
   ```

---

### 6. DO-06 — Kubernetes Foundations: Minikube Deployment & Service
#### 🔬 Giải thích chuyên sâu:
- **Cấu trúc Kubernetes (K8s):**
  - **Pod:** Đơn vị tính toán nhỏ nhất trong K8s, chứa một hoặc một nhóm container chia sẻ chung Network Namespace (IP) và Storage.
  - **Deployment:** Quản lý khai báo danh sách Pods (Desired State), tự động xử lý Rolling Update, Self-healing (tạo lại Pod mới khi Pod cũ die) và Scaling số lượng replica.
  - **Service:** Đóng vai trò là một Layer 4 Load Balancer nội bộ. Cung cấp IP tĩnh và DNS name ổn định cho nhóm Pods phía sau dựa trên `selector` matching với `labels` của Pod.

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Khởi động Minikube:** `minikube start`
2. **Khai báo `deployment.yaml` & `service.yaml`:**
   ```yaml
   # deployment.yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: flask-deployment
   spec:
     replicas: 2
     selector:
       matchLabels:
         app: flask-web
     template:
       metadata:
         labels:
           app: flask-web
       spec:
         containers:
         - name: flask-container
           image: nginx:alpine  # Dùng nginx làm ví dụ test
           ports:
           - containerPort: 80
   ---
   # service.yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: flask-service
   spec:
     type: ClusterIP
     selector:
       app: flask-web
     ports:
     - port: 80
       targetPort: 80
   ```
3. **Deploy & Forward Port:**
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   kubectl get pods
   kubectl get svc
   # Test truy cập bằng port-forward
   kubectl port-forward service/flask-service 8080:80
   ```
   - Mở trình duyệt truy cập `http://localhost:8080`.

---

## 🔴 HƯỚNG DẪN THỰC HÀNH 5 BÀI LAB TỰ GÂY SỰ CỐ & SỬA LỖI (TROUBLESHOOTING)

### LAB-01: Tràn Dung Lượng Ổ Đĩa Container `No space left on device`
- **Tạo sự cố:** Chạy lệnh sinh file rác ngốn bộ nhớ: `dd if=/dev/zero of=hugefile.img bs=1M count=2000`.
- **Triệu chứng:** App không thể ghi log, SQLite báo lỗi `database or disk is full`.
- **Cách debug & sửa lỗi:**
  - Kiểm tra dung lượng ổ đĩa: `df -h`.
  - Tìm folder/file ngốn dung lượng nhất: `du -sh /* | sort -rh | head -n 5`.
  - Dọn dẹp tài nguyên rác của Docker: `docker system prune -a --volumes`.

---

### LAB-02: Xóa Vết Secret Bị Commit Nhầm Trong Git History
- **Tạo sự cố:** Tạo commit chứa file `passwords.txt` có mật khẩu thật, sau đó lỡ `git push`.
- **Cách sửa lỗi chuẩn Enterprise (Dùng `git filter-repo`):**
  ```bash
  pip install git-filter-repo
  # Xóa sạch file passwords.txt khỏi toàn bộ lịch sử commit
  git filter-repo --path passwords.txt --invert-paths
  # Force push đè lịch sử đã dọn sạch
  git push origin --force --all
  ```
- **Hành động bắt buộc:** Lập tức thu hồi và cấp lại (Rotate) secret vừa bị rò rỉ!

---

### LAB-03: Debug Lỗi Service K8s Không Route Được Tới Pod (Mismatch Selector)
- **Tạo sự cố:** Trong `service.yaml`, cố tình sửa `selector: app: flask-web` thành `selector: app: wrong-tag`.
- **Triệu chứng:** Lệnh `kubectl port-forward service/flask-service 8080:80` bị timeout hoặc báo lỗi `503 Service Unavailable`.
- **Cách debug:**
  - Kiểm tra Endpoints của Service xem có gán đúng Pod IP không: `kubectl get endpoints flask-service`.
  - Thấy danh sách Endpoints hiển thị `<none>` -> Chứng tỏ Selector không khớp với Label của Pod!
  - Fix: Sửa lại `selector` trong `service.yaml` khớp với `template.metadata.labels` của Deployment.

---

### LAB-04: Debug Pipeline CI Fail Do Mismatch Dependency
- **Tạo sự cố:** Sửa file `requirements.txt` thêm package không tồn tại hoặc sai version: `django==99.0.0`.
- **Triệu chứng:** Pipeline GitHub Actions báo màu đỏ tại bước `Install Dependencies`.
- **Cách debug:** Mở tab Actions -> Bấm vào job bị lỗi -> Đọc chi tiết log pip error -> Sửa lại version đúng trong `requirements.txt` và push lại.

---

### LAB-05: Debug & Fix Race Condition Ghi Đè Dữ Liệu
- **Tạo sự cố:** Hai request đồng thời cập nhật số lượng tồn kho `inventory = inventory - 1` mà không dùng Transaction Lock.
- **Giải thích chuyên sâu:** Khi 2 thread/process cùng đọc `inventory = 10` tại cùng một thời điểm, cả 2 cùng tính `10 - 1 = 9` và cùng ghi `9` xuống DB -> Tồn kho giảm 1 thay vì giảm 2!
- **Cách fix bằng Pessimistic Locking trong SQL/Django:**
  ```python
  from django.db import transaction

  with transaction.atomic():
      # Khóa row trong Database cho tới khi transaction kết thúc (FOR UPDATE)
      product = Product.objects.select_for_update().get(id=1)
      product.inventory -= 1
      product.save()
  ```

