# 🗺️ LỘ TRÌNH DEVOPS FULL 9 HỌC PHẦN — TỪ CƠ BẢN ĐẾN THỰC CHIẾN

Tài liệu này dựng lại đầy đủ lộ trình DevOps theo mô hình VTI Academy (9 học phần), chia mỗi học phần thành 3 tầng: **Cơ bản → Nâng cao → Thực chiến (Labs + Sự cố thường gặp)**. Học xong 1 học phần, làm luôn Lab của học phần đó rồi mới qua học phần tiếp theo.

---

## 📋 MỤC LỤC

1. [Học phần 1: Fundamental](#học-phần-1-fundamental)
2. [Học phần 2: Basic Linux](#học-phần-2-basic-linux)
3. [Học phần 3: AWS Basic](#học-phần-3-aws-basic)
4. [Học phần 4: Kubernetes (K8s)](#học-phần-4-kubernetes-k8s)
5. [Học phần 5: GITS (Git)](#học-phần-5-gits-git)
6. [Học phần 6: CI/CD](#học-phần-6-cicd)
7. [Học phần 7: Monitoring](#học-phần-7-monitoring)
8. [Học phần 8: IaC (Infrastructure as Code)](#học-phần-8-iac-infrastructure-as-code)
9. [Học phần 9: Mock Project (Đồ án tổng hợp)](#học-phần-9-mock-project-đồ-án-tổng-hợp)
10. [Bảng tổng hợp sự cố thực chiến hay gặp nhất](#bảng-tổng-hợp-sự-cố-thực-chiến-hay-gặp-nhất)

---

## HỌC PHẦN 1: FUNDAMENTAL

### 🟢 Cơ bản
- **DevOps là gì:** văn hóa xóa bỏ ranh giới Dev (viết code) và Ops (vận hành), mục tiêu là release nhanh, ổn định, tự động hóa.
- **Vòng đời phần mềm (SDLC):** Plan → Code → Build → Test → Release → Deploy → Operate → Monitor (vòng lặp vô hạn ∞ — chính là logo học phần 1).
- **Agile/Scrum cơ bản:** Sprint, Backlog, Stand-up, Retro — vì pipeline DevOps luôn gắn với quy trình làm việc nhóm.
- **Kiến trúc client-server, mô hình mạng OSI 7 tầng (tối thiểu nhớ tầng 3-Network, 4-Transport, 7-Application), khái niệm IP/Port/DNS/HTTP-HTTPS.**
- **Khái niệm ảo hóa (Virtualization) vs container hóa (Containerization).**

### 🟡 Nâng cao
- Mô hình **12-Factor App** (config tách biệt code, stateless process, log as stream...) — nền tảng để thiết kế app "cloud-native".
- **SRE (Site Reliability Engineering):** SLA/SLO/SLI, error budget — khái niệm đo độ tin cậy hệ thống.
- Tư duy **Infrastructure as Cattle, not Pet** — server hỏng thì thay chứ không "chữa bệnh" thủ công.

### 🔴 Thực chiến
**Lab:**
1. Vẽ sơ đồ SDLC cho một dự án thật bạn từng làm, chỉ ra bước nào đang làm tay → bước nào có thể tự động hóa.
2. Dùng `curl -v https://example.com` để soi toàn bộ request/response, giải thích từng dòng (DNS resolve, TCP handshake, TLS, HTTP headers).

**Sự cố thường gặp:**
- Nhầm lẫn giữa "DevOps là công cụ" và "DevOps là văn hóa" → công ty mua đủ tool (Jenkins, Docker, K8s) nhưng Dev/Ops vẫn cãi nhau đổ lỗi khi sập hệ thống vì không có quy trình chia sẻ trách nhiệm.
- Không hiểu OSI/TCP-IP cơ bản → debug lỗi mạng (connection refused, timeout, DNS not resolved) mất rất nhiều thời gian ở các học phần sau.

---

## HỌC PHẦN 2: BASIC LINUX

### 🟢 Cơ bản
- Cấu trúc thư mục Linux: `/etc`, `/var/log`, `/home`, `/usr`, `/opt`, `/tmp`.
- Lệnh thao tác file: `ls, cd, cp, mv, rm, mkdir, find, grep, cat, less, tail -f`.
- Quyền hạn: `chmod, chown`, ý nghĩa `rwx` và số `755/644`.
- Quản lý process: `ps aux, top, htop, kill, kill -9, systemctl status`.
- Quản lý gói: `apt/yum/dnf install`, biết phân biệt Debian-family vs RedHat-family.
- Redirect & Pipe: `>`, `>>`, `|`, `2>&1`.

### 🟡 Nâng cao
- **Shell scripting (Bash):** biến, vòng lặp, điều kiện, hàm, `cron job` (`crontab -e`) để lên lịch chạy script tự động.
- **systemd:** viết một Unit file để chạy app như một service (`systemctl enable/start/restart`).
- **Network troubleshooting trên Linux:** `netstat -tulpn` / `ss -tulpn`, `curl`, `ping`, `traceroute`, `dig/nslookup`, `iptables/ufw` cơ bản.
- **Log management:** `journalctl`, xoay vòng log với `logrotate`.
- Quản lý user/group, sudoers, SSH key-based authentication (`ssh-keygen`, `authorized_keys`).

### 🔴 Thực chiến
**Lab:**
1. Viết bash script tự động backup một thư mục `/var/www` thành file `.tar.gz` có gắn timestamp, đẩy lên S3 (dùng AWS CLI), chạy bằng cron mỗi ngày 2h sáng.
2. Một service Node.js bị "Out of Memory" và bị kill — dùng `dmesg | grep -i kill`, `journalctl -u <service>` để tìm nguyên nhân.
3. Setup SSH không cần mật khẩu (key-based) từ máy local vào 1 server test (VM hoặc EC2).

**Sự cố thường gặp:**
- **"Permission denied"** khi chạy script — quên `chmod +x`, hoặc chạy sai user (dùng `sudo` cho lệnh cần quyền root).
- **Disk full (`No space left on device`)** — nguyên nhân kinh điển: log không được xoay vòng (logrotate) chiếm hết `/var/log`, hoặc Docker image/container cũ không dọn (`docker system prune`).
- **Port đã bị chiếm (`Address already in use`)** — dùng `lsof -i :PORT` hoặc `ss -tulpn | grep PORT` để tìm và kill đúng process.
- **Cron job không chạy** — do PATH trong cron khác với shell tương tác, hoặc quên `2>&1` để redirect log lỗi ra file mà debug.
- **Zombie/Defunct process** — quy trình cha không "reap" con đúng cách, cần hiểu init process (PID 1) trong container.

---

## HỌC PHẦN 3: AWS BASIC

### 🟢 Cơ bản
- **IAM:** User, Group, Role, Policy — nguyên tắc **Least Privilege**.
- **EC2:** khởi tạo instance, chọn AMI, Security Group (như firewall), Key Pair để SSH.
- **VPC:** Subnet public/private, Internet Gateway, Route Table, NAT Gateway — mô hình mạng cơ bản của AWS.
- **S3:** Bucket, Object, quyền truy cập (Bucket Policy), Storage Class (Standard, IA, Glacier).
- **RDS:** Database managed (MySQL/PostgreSQL), Multi-AZ để failover.

### 🟡 Nâng cao
- **Load Balancer (ALB/NLB) + Auto Scaling Group** — scale instance theo tải, health check.
- **Route 53:** DNS management, routing policy (Weighted, Failover, Latency-based).
- **CloudWatch:** Metrics, Alarms, Logs — nền tảng để qua Học phần 7 (Monitoring).
- **ECR/ECS/EKS:** container registry và service chạy container trên AWS (bước đệm sang Học phần 4 K8s).
- **Cost optimization:** Reserved Instance, Spot Instance, Savings Plan.
- **Security:** KMS (mã hóa), Secrets Manager, WAF, VPC Peering.

### 🔴 Thực chiến
**Lab:**
1. Dựng 1 VPC có subnet public (chứa EC2 chạy web app) và subnet private (chứa RDS), cấu hình Security Group sao cho chỉ EC2 mới truy cập được RDS.
2. Deploy 1 static website lên S3 + CloudFront, gắn domain qua Route 53.
3. Cấu hình Auto Scaling Group cho 1 EC2 chạy Node.js/Flask, test load bằng `ab` hoặc `k6` để xem instance tự nhân bản.

**Sự cố thường gặp:**
- **EC2 không SSH được** — Security Group chưa mở port 22, hoặc file `.pem` sai quyền (`chmod 400`), hoặc đang ở subnet private không có Internet Gateway.
- **App chạy trên EC2 nhưng không truy cập được từ trình duyệt** — quên mở port ứng dụng (80/3000/8080) trong Security Group, hoặc app chỉ bind `127.0.0.1` thay vì `0.0.0.0`.
- **RDS connection timeout** — Security Group của RDS chưa cho phép inbound từ Security Group của EC2 (nên trỏ SG-to-SG thay vì IP cứng).
- **Bill AWS tăng bất thường** — quên tắt EC2/NAT Gateway sau khi test (NAT Gateway tính phí theo giờ + traffic dù không dùng), quên xóa Elastic IP không gắn instance nào.
- **IAM Access Denied** — thiếu policy hoặc gắn nhầm Role; nguyên tắc debug: dùng **IAM Policy Simulator**.

---

## HỌC PHẦN 4: KUBERNETES (K8S)

*(Xem chi tiết nền tảng tại [Docker_Kubernetes_Mastery.md](./Docker_Kubernetes_Mastery.md) — dưới đây là phần mở rộng theo đúng khung "Cơ bản → Nâng cao → Thực chiến").*

### 🟢 Cơ bản
- **Kiến trúc K8s:** Control Plane (API Server, Scheduler, Controller Manager, etcd) vs Worker Node (Kubelet, Kube-proxy, Container Runtime).
- **Object cơ bản:** Pod, Deployment, ReplicaSet, Service (ClusterIP/NodePort/LoadBalancer), Namespace.
- `kubectl` cơ bản: `get, describe, logs, exec, apply -f, delete`.
- YAML manifest: viết 1 Deployment + Service đơn giản.

### 🟡 Nâng cao
- **ConfigMap & Secret** — tách config/khóa bí mật khỏi image.
- **Ingress + Ingress Controller (NGINX)** — routing traffic theo domain/path.
- **Volume & PersistentVolumeClaim (PVC)** — lưu trữ dữ liệu bền vững.
- **Helm:** package manager cho K8s, viết Helm Chart để tái sử dụng cấu hình.
- **HPA (Horizontal Pod Autoscaler)** — tự động scale Pod theo CPU/Memory.
- **Liveness Probe / Readiness Probe** — để K8s biết khi nào restart Pod hay khi nào đưa vào traffic.
- **RBAC** — phân quyền truy cập cluster.

### 🔴 Thực chiến
**Lab:**
1. Deploy 1 app 3-tier (Frontend + Backend API + Database) lên Minikube/Kind, dùng Service để 3 tầng giao tiếp nhau.
2. Viết Helm Chart cho app trên, parameterize số replicas và image tag.
3. Cấu hình HPA để Pod tự scale từ 2 → 10 khi CPU > 70%, test bằng cách tạo tải giả (`kubectl run -it load-generator`).

**Sự cố thường gặp:**
- **`CrashLoopBackOff`** — app trong container bị lỗi ngay khi start; debug bằng `kubectl logs <pod> --previous` và `kubectl describe pod`.
- **`ImagePullBackOff`** — sai tên image/tag, hoặc thiếu `imagePullSecrets` khi kéo từ private registry.
- **Pod `Pending` mãi không chạy** — cluster không đủ tài nguyên (CPU/Memory request quá cao so với node), hoặc thiếu `nodeSelector`/taint-toleration phù hợp.
- **Service không route được traffic tới Pod** — nhãn (`labels`) trong Deployment và `selector` trong Service không khớp nhau (lỗi kinh điển nhất của người mới học K8s).
- **`OOMKilled`** — Pod bị kill do vượt `memory limit`, cần review lại `resources.requests/limits`.
- **Config thay đổi (ConfigMap) nhưng Pod không nhận** — ConfigMap mount vào Pod không tự reload, cần rolling restart Deployment.

---

## HỌC PHẦN 5: GITS (GIT)

### 🟢 Cơ bản
- Khái niệm Working Directory – Staging Area – Repository.
- Lệnh nền tảng: `init, clone, add, commit, status, log, diff`.
- Branch: `branch, checkout/switch, merge`.
- Remote: `push, pull, fetch`, `.gitignore`.

### 🟡 Nâng cao
- **Merge vs Rebase** — khi nào dùng cái nào, hiểu rõ hệ quả với lịch sử commit.
- **Git workflow:** Git Flow (feature/develop/release/hotfix/main) vs Trunk-Based Development (phổ biến hơn trong CI/CD hiện đại).
- **Conflict resolution** nâng cao: `git rebase -i` để squash/reorder commit, `cherry-pick`.
- **Git hooks** (`pre-commit`, `pre-push`) — tự động lint/test trước khi commit.
- **Semantic commit message** (Conventional Commits) để tự động generate changelog/version.
- `git bisect` để tìm commit gây lỗi (regression hunting).

### 🔴 Thực chiến
**Lab:**
1. Mô phỏng 2 người cùng sửa 1 file, tạo conflict thật, thực hành resolve bằng cả `merge` và `rebase`, so sánh lịch sử commit (`git log --graph`).
2. Setup pre-commit hook chạy `lint` + `test` tự động trước khi cho phép commit.
3. Dùng `git bisect` để tìm ra commit nào làm hỏng 1 test case trong repo demo.

**Sự cố thường gặp:**
- **`detached HEAD`** — checkout nhầm vào 1 commit thay vì branch, commit tiếp bị "mồ côi" nếu không tạo branch mới kịp thời.
- **Force push làm mất commit của đồng nghiệp** — luôn ưu tiên `git push --force-with-lease` thay vì `--force`.
- **Merge conflict lặp lại nhiều lần trên cùng 1 branch dài ngày** — dấu hiệu branch sống quá lâu, nên áp dụng Trunk-Based + feature flag thay vì giữ branch feature hàng tuần.
- **Commit nhầm secret (API key, `.env`)** — cần `git filter-repo` hoặc BFG Repo-Cleaner để xóa khỏi lịch sử, đồng thời **revoke key ngay lập tức** (xóa khỏi git chưa đủ, key đã lộ coi như "cháy").
- **`fatal: refusing to merge unrelated histories`** — khi merge 2 repo tách biệt, cần cờ `--allow-unrelated-histories` và hiểu rõ hệ quả.

---

## HỌC PHẦN 6: CI/CD

*(Nền tảng GitHub Actions xem tại [CI_CD_Automation_GithubActions.md](./CI_CD_Automation_GithubActions.md); học phần này mở rộng thêm các nền tảng khác trong ảnh: Azure DevOps, GitLab CI, CircleCI).*

### 🟢 Cơ bản
- Khái niệm Pipeline: Stage → Job → Step.
- Trigger: push, pull request, schedule, manual.
- Artifact: build ra 1 file/image để dùng ở stage sau.
- So sánh nhanh 4 nền tảng phổ biến:
  - **GitHub Actions** — tích hợp sẵn với GitHub, YAML trong `.github/workflows`.
  - **GitLab CI** — `.gitlab-ci.yml`, mạnh về self-hosted runner.
  - **Azure DevOps** — Pipeline YAML hoặc Classic UI, mạnh trong hệ sinh thái Microsoft/Enterprise.
  - **CircleCI** — SaaS, orb (package tái sử dụng step), tốc độ build nhanh nhờ caching thông minh.

### 🟡 Nâng cao
- **Multi-stage pipeline:** Build → Test (unit + integration) → Security Scan (SAST) → Deploy Staging → Manual Approval → Deploy Production.
- **Caching & Parallelization** để giảm thời gian build.
- **Blue-Green Deployment** và **Canary Release** — 2 chiến lược deploy giảm rủi ro downtime.
- **Secret management trong pipeline** (GitHub Secrets, Azure Key Vault, GitLab CI/CD Variables) — không bao giờ hardcode.
- **Self-hosted Runner/Agent** — khi cần build trong mạng nội bộ hoặc cần GPU/tài nguyên đặc thù.

### 🔴 Thực chiến
**Lab:**
1. Viết pipeline GitHub Actions: chạy test → build Docker image → push lên ECR → deploy lên EC2 qua SSH.
2. Chuyển pipeline trên sang GitLab CI (`.gitlab-ci.yml`) để so sánh cú pháp và cơ chế cache.
3. Cấu hình 1 bước "Manual Approval" trước khi deploy Production (Azure DevOps hoặc GitHub Environments).

**Sự cố thường gặp:**
- **Pipeline pass ở local nhưng fail trên CI** — khác biệt môi trường (version Node/Python, biến môi trường thiếu, timezone).
- **Build chậm dần theo thời gian** — cache bị vô hiệu do thay đổi key cache không đúng cách (VD: `package-lock.json` hash thay đổi liên tục).
- **Secret bị lộ trong log** — pipeline `echo $SECRET` để debug rồi quên xóa; luôn dùng cơ chế `mask`/`secret variable` của nền tảng.
- **Deploy production nhưng rollback thủ công cực khổ** — thiếu chiến lược Blue-Green/Canary nên khi lỗi phải downtime để fix.
- **Race condition giữa nhiều pipeline chạy song song** — 2 người push gần nhau cùng deploy 1 lúc gây conflict trên server; cần cơ chế lock deployment (concurrency group).
- **`docker push` bị "denied: requested access to the resource is denied"** — thiếu login registry hoặc sai quyền IAM/Role gắn cho CI runner.

---

## HỌC PHẦN 7: MONITORING

### 🟢 Cơ bản
- 3 trụ cột Observability: **Metrics – Logs – Traces**.
- **Prometheus:** time-series database, mô hình pull-based scrape metrics.
- **Grafana:** trực quan hóa dữ liệu từ Prometheus (dashboard, panel).
- Log cơ bản: log level (DEBUG/INFO/WARN/ERROR), tập trung log về 1 nơi thay vì rải rác trên từng server.

### 🟡 Nâng cao
- **Alertmanager** — định nghĩa rule cảnh báo (VD: CPU > 80% trong 5 phút) và route cảnh báo tới Slack/Telegram/PagerDuty.
- **ELK/EFK Stack** (Elasticsearch – Logstash/Fluentd – Kibana) hoặc **Grafana Loki** — tập trung & tìm kiếm log.
- **Distributed Tracing** (Jaeger/OpenTelemetry) — theo dõi 1 request đi qua nhiều microservice.
- **SLO-based Alerting** — cảnh báo dựa trên error budget thay vì ngưỡng CPU/Memory đơn thuần (tránh "alert fatigue").
- **Node Exporter / cAdvisor** — exporter thu thập metrics hệ thống và container cho Prometheus.

### 🔴 Thực chiến
**Lab:**
1. Dựng bộ Prometheus + Grafana + Node Exporter bằng Docker Compose, tạo dashboard theo dõi CPU/RAM/Disk của server.
2. Cấu hình Alertmanager gửi cảnh báo qua Telegram khi CPU > 80% trong 5 phút.
3. Thêm `/metrics` endpoint tùy chỉnh (custom metrics) vào 1 app Node.js/Flask để Prometheus scrape (VD: số request/giây, latency).

**Sự cố thường gặp:**
- **Alert Fatigue** — set ngưỡng cảnh báo quá nhạy khiến Slack/Telegram spam liên tục, dẫn đến team bỏ qua cả cảnh báo thật.
- **Dashboard đẹp nhưng vô dụng khi sự cố xảy ra** — thiếu dashboard theo "Golden Signals" (Latency, Traffic, Errors, Saturation) nên không biết nhìn vào đâu lúc khẩn cấp.
- **Prometheus mất data sau khi restart** — quên cấu hình persistent volume cho thư mục dữ liệu của Prometheus.
- **Log quá nhiều làm đầy ổ đĩa / tốn chi phí ELK** — thiếu retention policy (index lifecycle management), cần tự động xóa log cũ.
- **Không tương quan được log-metric-trace** khi debug — thiếu `trace_id`/`request_id` xuyên suốt các service (root cause của rất nhiều buổi "mò kim đáy bể" khi có incident).

---

## HỌC PHẦN 8: IAC (INFRASTRUCTURE AS CODE)

### 🟢 Cơ bản
- Khái niệm IaC: định nghĩa hạ tầng bằng code thay vì click tay trên Console.
- **Terraform:** HCL syntax, Provider, Resource, `plan/apply/destroy`.
- **State file** — nơi Terraform lưu trạng thái hạ tầng thực tế.
- **Ansible:** Playbook, Inventory, Module — công cụ config management (push-based, không cần agent).

### 🟡 Nâng cao
- **Terraform Module** — đóng gói tái sử dụng hạ tầng (VD: module VPC dùng lại cho nhiều môi trường).
- **Remote State + State Locking** (S3 + DynamoDB) — làm việc nhóm an toàn, tránh 2 người apply cùng lúc.
- **Terraform Workspace** để quản lý nhiều môi trường (dev/staging/prod) từ 1 codebase.
- **Ansible Role** — tổ chức playbook lớn thành các role tái sử dụng.
- So sánh Terraform (provisioning) vs Ansible (configuration) vs CloudFormation (native AWS) — khi nào phối hợp cả hai.

### 🔴 Thực chiến
**Lab:**
1. Viết Terraform tạo VPC + EC2 + Security Group (đúng những gì đã làm tay ở Học phần 3, giờ code hóa toàn bộ).
2. Cấu hình Remote State trên S3 + lock bằng DynamoDB, thử 2 terminal chạy `apply` cùng lúc để thấy cơ chế lock hoạt động.
3. Dùng Ansible Playbook để cài Docker + deploy container tự động lên EC2 vừa tạo bằng Terraform.

**Sự cố thường gặp:**
- **State file bị mất hoặc conflict** — 2 người `apply` cùng lúc không có lock → hạ tầng thực tế lệch với state, gây lỗi khó lường (nên luôn dùng Remote State + Locking ngay từ đầu).
- **`terraform apply` xóa nhầm resource production** — do đổi tên resource trong code khiến Terraform hiểu là "resource cũ bị xóa + resource mới được tạo" thay vì "rename"; luôn `terraform plan` kỹ và dùng `terraform state mv` khi cần đổi tên.
- **Secret bị commit vào state file** (state lưu plaintext) — cần mã hóa S3 bucket chứa state, hạn chế quyền truy cập, cân nhắc dùng Vault cho secret thật sự nhạy cảm.
- **Ansible chạy không idempotent** — playbook viết ẩu khiến chạy lại nhiều lần cho kết quả khác nhau; nguyên tắc vàng của config management là phải idempotent (chạy N lần vẫn ra cùng 1 trạng thái).
- **Drift hạ tầng** — ai đó sửa tay trên AWS Console, lần sau `terraform apply` sẽ cố "sửa lại" theo code gây gián đoạn ngoài ý muốn; cần dùng `terraform plan` thường xuyên để phát hiện drift sớm.

---

## HỌC PHẦN 9: MOCK PROJECT (ĐỒ ÁN TỔNG HỢP)

### 🎯 Mục tiêu
Ghép toàn bộ 8 học phần trên thành **một pipeline DevOps hoàn chỉnh, chạy thật từ A-Z**.

### 🏗️ Kiến trúc đề xuất cho Mock Project
```
Dev push code (Git - HP5)
   → CI/CD Pipeline (GitHub Actions/GitLab CI - HP6)
       → Run test + Build Docker Image
       → Push image lên AWS ECR (AWS - HP3)
   → Terraform apply hạ tầng (IaC - HP8): VPC, EKS cluster, RDS
   → Deploy lên Kubernetes (K8s - HP4) qua Helm Chart
   → Prometheus + Grafana giám sát (Monitoring - HP7)
   → Toàn bộ server nền chạy trên Linux (HP2), điều phối theo văn hóa DevOps (HP1)
```

### 📦 Checklist đồ án hoàn chỉnh
- [ ] Repo Git có branch strategy rõ ràng (Trunk-Based hoặc Git Flow) + pre-commit hook lint/test.
- [ ] Pipeline CI: test tự động, build image, scan bảo mật cơ bản (VD: `trivy image`).
- [ ] Pipeline CD: deploy tự động lên staging, có bước Manual Approval trước khi lên production.
- [ ] Hạ tầng 100% code hóa bằng Terraform, có Remote State.
- [ ] App chạy trên K8s có: Deployment, Service, Ingress, ConfigMap/Secret, HPA, health check (liveness/readiness).
- [ ] Có dashboard Grafana theo dõi Golden Signals + Alert gửi Telegram/Slack khi sự cố.
- [ ] Viết `README.md` mô tả kiến trúc + hướng dẫn chạy lại từ đầu (Runbook).
- [ ] Diễn tập 1 sự cố giả lập (VD: kill Pod ngẫu nhiên — "Chaos Engineering cơ bản") và viết post-mortem.

### 🔴 Sự cố thực chiến khi làm Mock Project (thường là tổng hợp lỗi của các học phần trước, xảy ra dồn dập)
- **Thứ tự triển khai sai:** cố `helm install` khi EKS cluster chưa apply xong bằng Terraform → luôn thiết kế pipeline theo đúng dependency (Terraform trước, K8s sau).
- **Biến môi trường/secret không đồng bộ giữa các tầng** (Terraform output → K8s Secret → App env) — nên dùng 1 nguồn sự thật duy nhất (VD: AWS Secrets Manager + External Secrets Operator) thay vì copy tay qua nhiều nơi.
- **Chi phí AWS vượt dự kiến** khi chạy EKS 24/7 cho đồ án cá nhân — nhớ `terraform destroy` sau khi demo xong, hoặc dùng Minikube/Kind để luyện tập phần K8s không tốn phí.
- **Demo trước mặt người khác bị lỗi bất ngờ** — luôn có "rollback plan" và đã test lại toàn bộ pipeline ít nhất 1 lần từ đầu trước ngày demo, không sửa code phút chót.
- **Không ai đọc được hệ thống bạn dựng ngoài chính bạn** — thiếu Runbook/README khiến đồ án "chạy được nhưng không giải thích được" — đây là điểm bị trừ nhiều nhất khi phỏng vấn hỏi sâu.

---

## BẢNG TỔNG HỢP SỰ CỐ THỰC CHIẾN HAY GẶP NHẤT

| Nhóm | Triệu chứng | Nguyên nhân gốc rễ thường gặp |
|---|---|---|
| Linux | `Permission denied` | Thiếu `chmod +x` hoặc chạy sai user |
| Linux | `No space left on device` | Log không rotate, Docker image/container rác |
| AWS | SSH timeout vào EC2 | Security Group chưa mở port 22 hoặc ở subnet private |
| AWS | RDS connection timeout | SG của RDS chưa cho phép inbound từ SG của app |
| K8s | `CrashLoopBackOff` | App lỗi ngay khi start, xem `kubectl logs --previous` |
| K8s | Service không route tới Pod | `labels` và `selector` không khớp |
| Git | Force push mất commit đồng nghiệp | Dùng `--force` thay vì `--force-with-lease` |
| Git | Lộ secret trong lịch sử commit | Thiếu `.gitignore` + chưa dùng pre-commit hook chặn secret |
| CI/CD | Pipeline pass local, fail CI | Khác biệt biến môi trường/version |
| CI/CD | Secret lộ trong log | Debug bằng `echo $SECRET` quên xóa |
| Monitoring | Alert Fatigue | Ngưỡng cảnh báo quá nhạy, không phân loại mức độ |
| Monitoring | Mất dữ liệu Prometheus khi restart | Thiếu Persistent Volume |
| IaC | State conflict/mất state | Không dùng Remote State + Locking |
| IaC | `apply` xóa nhầm resource production | Đổi tên resource mà không `terraform state mv` |
| Mock Project | Chi phí AWS vượt dự kiến | Quên `terraform destroy` sau demo |

---

## 🎓 GỢI Ý LỘ TRÌNH THỜI GIAN (tham khảo, tự điều chỉnh theo tốc độ cá nhân)

| Học phần | Thời lượng đề xuất |
|---|---|
| 1. Fundamental | 3-5 ngày |
| 2. Basic Linux | 1 tuần |
| 3. AWS Basic | 1.5 tuần |
| 4. K8s | 2 tuần |
| 5. GITS | 3-5 ngày |
| 6. CI/CD | 1.5 tuần |
| 7. Monitoring | 1 tuần |
| 8. IaC | 1.5 tuần |
| 9. Mock Project | 2-3 tuần |

**Tổng:** ~10-12 tuần nếu học full-time, ~4-5 tháng nếu học part-time song song đi làm.

---
🚀 **Nguyên tắc xuyên suốt:** Học xong lý thuyết một học phần → làm Lab thực chiến của học phần đó ngay → chủ động gây lỗi ra để tự tay fix (không chỉ học cách làm đúng, mà phải học cách *debug khi sai*). Đó là cách duy nhất để "thực chiến" thật sự chứ không chỉ là làm theo hướng dẫn.
