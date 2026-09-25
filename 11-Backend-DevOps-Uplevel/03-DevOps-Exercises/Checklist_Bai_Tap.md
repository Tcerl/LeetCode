# ✅ Checklist Bài Tập DevOps (DO-01 → DO-06)

> Mục tiêu: đạt mức "backend dev tự deploy/debug được hệ thống của mình" — không kỳ vọng thạo hết mọi công cụ, chỉ cần chạy được đầu-cuối 1 lần thật sự hiểu.

- [ ] **DO-01 — Docker Compose đa dịch vụ** (Tuần 12): Compose app Flask (FL-04) + Postgres + (tùy chọn) Redis, dữ liệu không mất khi `docker-compose down` rồi `up` lại (dùng volume).
- [ ] **DO-02 — Gây lỗi & tự sửa Docker** (Tuần 12): Cố tình để app crash ngay khi container start (VD: sai biến môi trường DB), thực hành đọc `docker logs` để tìm nguyên nhân.
- [ ] **DO-03 — Pipeline CI/CD cơ bản** (Tuần 13): Viết `.github/workflows` chạy test → build Docker image cho app Flask/Django mỗi khi push.
- [ ] **DO-04 — Deploy qua pipeline** (Tuần 15): Nối thêm bước deploy (lên EC2 thật hoặc localstack) vào pipeline trên.
- [ ] **DO-05 — Secret Management** (Tuần 16): Chuyển toàn bộ biến nhạy cảm (DB password, JWT secret) đang hardcode trong các bài tập trước sang GitHub Secrets / `.env` không commit vào Git — kiểm tra lại `.gitignore`.
- [ ] **DO-06 — K8s cơ bản** (Tuần 17): Deploy app Flask (image ở DO-01) lên Minikube bằng 1 Deployment + 1 Service, verify truy cập được qua `kubectl port-forward`.

## 🎯 Bài tập nâng cao
- [ ] Thêm health check endpoint (`/health`) vào app, cấu hình Liveness Probe trong K8s Deployment.
- [ ] Dùng `git bisect` để tìm 1 commit tự tạo lỗi trong project bài tập.

## 🔴 Checklist "tự gây sự cố để tự sửa" (làm ít nhất 3/5 trước Tết — đây là thứ tạo ra khác biệt thật với người chỉ đọc lý thuyết)
- [ ] Cố tình để container hết dung lượng ổ đĩa ảo, thực hành debug `No space left on device`.
- [ ] Cố tình push nhầm secret lên Git, thực hành xóa khỏi lịch sử bằng `git filter-repo` (hoặc BFG) + đổi lại secret.
- [ ] Cố tình deploy sai `labels`/`selector` trong K8s Service, quan sát Service không route được và tự sửa.
- [ ] Cố tình để pipeline CI fail (sai version dependency), thực hành đọc log CI để tìm nguyên nhân.
- [ ] Cố tình để 2 request ghi đè dữ liệu nhau (race condition đơn giản), quan sát hậu quả rồi tìm cách khóa (lock/transaction).
