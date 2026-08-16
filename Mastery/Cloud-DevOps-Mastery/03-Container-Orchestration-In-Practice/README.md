# 03. Docker & Kubernetes — Vận Hành Thật, Không Chỉ Cú Pháp

> Cú pháp Dockerfile/K8s manifest đã có ở [`Docker_Kubernetes_Mastery.md`](../../../10-DevOps-Architect/Docker_Kubernetes_Mastery.md). File này tập trung vào **cách container vỡ trận trên production và cách senior phòng tránh**.

---

## 1. Image nhẹ không chỉ để build nhanh — mà là bề mặt tấn công nhỏ hơn

```dockerfile
# ❌ Image nặng, chứa cả build tool không cần lúc runtime, chạy bằng root
FROM python:3.12
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

# ✅ Multi-stage build: tách môi trường build và runtime, chạy bằng user thường
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
RUN useradd -m appuser && chown -R appuser /app
USER appuser                                    # KHÔNG chạy container bằng root
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
```

**Vì sao quan trọng thật:** image nặng (chứa compiler, dev tool, cache pip) không chỉ chậm deploy — nó **mở rộng bề mặt tấn công** (nhiều package = nhiều lỗ hổng CVE tiềm ẩn cần vá) và tốn băng thông kéo image mỗi lần scale. Chạy container bằng root là sai lầm bảo mật kinh điển: nếu attacker khai thác được lỗ hổng trong app, họ có ngay quyền root **bên trong container** — kết hợp với cấu hình sai khác có thể leo thang ra ngoài host.

---

## 2. Resource Requests & Limits — thiếu cái này là tự tạo sự cố

```yaml
# Thiếu resources → 1 pod bug (memory leak) có thể ăn hết RAM của CẢ NODE,
# làm crash luôn các pod KHÁC không liên quan đang chạy chung node đó ("noisy neighbor").
resources:
  requests:              # đảm bảo tối thiểu — Scheduler dùng để quyết định đặt pod vào node nào
    memory: "256Mi"
    cpu: "250m"
  limits:                # giới hạn tối đa — vượt quá sẽ bị kill (OOMKilled) hoặc throttle CPU
    memory: "512Mi"
    cpu: "500m"
```

**Sự cố thật:** `requests` quá thấp so với nhu cầu thật → Scheduler nhồi quá nhiều pod vào 1 node → node quá tải thật sự dù theo config "vẫn còn chỗ". `limits` quá thấp → app bị **OOMKilled** liên tục dù logic không có bug, chỉ vì traffic tăng nhẹ. Senior luôn xác định requests/limits dựa trên **load test thật**, không đoán theo cảm tính, và theo dõi lại sau khi lên production để tinh chỉnh.

---

## 3. Liveness vs Readiness Probe — nhầm lẫn gây outage dây chuyền

| Probe | Trả lời câu hỏi | Nếu fail |
|---|---|---|
| **Liveness** | "Process này có bị deadlock/treo không?" | K8s **restart pod** |
| **Readiness** | "Pod này đã sẵn sàng nhận traffic chưa?" | K8s **rút pod khỏi danh sách nhận traffic** (không restart) |

**Sự cố thật kinh điển:** dùng chung 1 endpoint `/health` cho cả liveness và readiness, và endpoint đó kiểm tra luôn kết nối tới DB. Khi DB chậm tạm thời (không phải lỗi app) → readiness fail là đúng (không nên nhận traffic mới) — nhưng nếu **liveness cũng dùng chung endpoint đó**, K8s sẽ **restart toàn bộ pod** dù app không hề bị treo, làm tình hình tệ hơn (mất luôn cả các request đang xử lý dở, và pod mới khởi động lại vẫn gặp DB chậm → vòng lặp restart liên tục = outage tự gây ra bởi chính cơ chế tự phục hồi).

**Nguyên tắc:** Liveness chỉ kiểm tra "process này còn phản hồi không" (không phụ thuộc dependency ngoài). Readiness mới kiểm tra dependency ngoài (DB, cache, service khác).

---

## 4. Rolling Update — vì sao deploy "thành công" mà user vẫn thấy lỗi 502 thoáng qua

Khi rolling update, pod cũ bị terminate trong khi vẫn còn request đang xử lý dở, và pod mới chưa kịp sẵn sàng. Senior cấu hình:

- **`preStop` hook + `terminationGracePeriodSeconds`:** cho pod cũ thời gian hoàn thành request đang xử lý và tự rút khỏi Load Balancer trước khi bị kill hẳn, thay vì bị ngắt đột ngột.
- **`maxUnavailable` / `maxSurge`** hợp lý trong Deployment strategy — không hạ hết pod cũ trước khi pod mới sẵn sàng (liên kết trực tiếp tới chiến lược deploy ở Module 04).

---

## 🎯 Câu hỏi senior hay hỏi khi review

1. "Container này chạy bằng user nào? Có set resource limits chưa?"
2. "Liveness và readiness probe của bạn có dùng chung endpoint không — nếu DB chậm, pod có bị restart oan không?"
3. "Khi rolling update, request đang xử lý dở trên pod cũ có bị cắt ngang không?"

## 🔗 Liên kết module khác
- Chọn container thay vì EC2/Lambda dựa trên tiêu chí gì → [`02-Compute-Choices-EC2-Lambda-Containers`](../02-Compute-Choices-EC2-Lambda-Containers/README.md)
- Chiến lược deploy an toàn (blue-green, canary) → [`04-CICD-Deployment-Strategies`](../04-CICD-Deployment-Strategies/README.md)
- Giám sát pod/node để phát hiện sự cố sớm → [`05-Observability-Incident-Response`](../05-Observability-Incident-Response/README.md)
