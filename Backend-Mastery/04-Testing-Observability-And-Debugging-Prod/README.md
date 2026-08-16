# 04. Testing, Observability & Debug Trên Production

> Lý thuyết testing đã có ở [`Python_Backend_Professional_Guide.md`](../../03-Python-Expert/Python_Backend_Professional_Guide.md) mục 9. File này bổ sung phần **quan sát hệ thống khi nó đã chạy thật** — mảng kiến thức mà tài liệu theo công nghệ đơn lẻ thường thiếu.

---

## 1. Kim tự tháp kiểm thử — vì sao không nên viết toàn E2E test

```
        ▲  E2E Tests (ít, chậm, tốn kém — test cả hệ thống qua UI/API thật)
       ╱ ╲
      ╱   ╲  Integration Tests (vừa phải — test tương tác giữa các module, có DB thật/test container)
     ╱     ╲
    ╱───────╲ Unit Tests (nhiều, nhanh, rẻ — test 1 hàm/1 class độc lập, mock dependency ngoài)
```

**Sai lầm thường gặp ở team thiếu kinh nghiệm:** viết quá nhiều E2E test vì "trông giống thật nhất" → suite test chạy 45 phút, dev sợ chạy test nên bỏ qua, bug lọt vào production. Senior luôn giữ tỷ lệ: unit test nhiều nhất (chạy được trong giây), integration test vừa phải, E2E test chỉ cho các luồng nghiệp vụ quan trọng nhất (checkout, thanh toán, đăng ký).

```python
# Unit test tốt: mock hoàn toàn dependency ngoài (DB, API bên thứ 3)
def test_calculate_discount_for_vip_customer(mocker):
    mocker.patch("app.services.get_customer_tier", return_value="VIP")
    result = calculate_discount(order_total=1000)
    assert result == 150  # VIP giảm 15% — test chỉ tập trung vào LOGIC, không phụ thuộc DB thật
```

---

## 2. Observability — 3 trụ cột senior phải phân biệt rõ

| Trụ cột | Trả lời câu hỏi | Công cụ thật |
|---|---|---|
| **Logs** | "Chuyện gì đã xảy ra tại thời điểm này?" | ELK Stack, CloudWatch Logs, structured JSON logging |
| **Metrics** | "Hệ thống đang khỏe không, theo số liệu tổng quát?" | Prometheus + Grafana, CloudWatch Metrics |
| **Traces** | "Request này đi qua bao nhiêu service, tốn bao lâu ở mỗi bước?" | Jaeger, AWS X-Ray, OpenTelemetry |

**Bẫy junior hay gặp:** chỉ có logs, không có metrics/traces → khi hệ thống chậm, phải "mò" từng dòng log thủ công, không biết bottleneck nằm ở service nào trong kiến trúc microservices. Senior luôn thiết kế **structured logging** (JSON, có `request_id` xuyên suốt các service) ngay từ đầu — cực khó bổ sung sau khi hệ thống đã lớn.

```python
import logging, json, uuid

def log_request(request_id: str, event: str, **kwargs):
    """
    Structured logging — mỗi dòng log là JSON có thể query được (khác print() vô dụng
    khi cần tìm 1 request cụ thể giữa hàng triệu dòng log/ngày trên production).
    """
    logging.info(json.dumps({"request_id": request_id, "event": event, **kwargs}))
```

---

## 3. Debug một endpoint chậm trên production — quy trình senior thật sự làm

Đây là kỹ năng khác hẳn debug local (không có debugger đính kèm, không được restart tùy ý vì ảnh hưởng user thật):

1. **Xem metrics trước:** endpoint này chậm từ khi nào? Có tương quan với deploy gần nhất, hay traffic tăng đột biến, hay 1 dependency ngoài (API bên thứ 3, DB) đang chậm?
2. **Xem trace của 1 request cụ thể chậm:** thời gian tốn ở tầng nào — network, DB query, xử lý logic, gọi service khác?
3. **Xem slow query log của DB** (`pg_stat_statements` trong Postgres) — có query mới nào xuất hiện trong top slow query không?
4. **Kiểm tra tài nguyên hệ thống:** CPU/RAM/connection pool có đang bão hòa không (liên kết [`01-Request-Lifecycle-And-Architecture`](../01-Request-Lifecycle-And-Architecture/README.md))?
5. **Chỉ khi cần thiết** mới cân nhắc reproduce ở staging với debugger/profiler thật (`cProfile`, `py-spy` — có thể attach vào process Python đang chạy MÀ KHÔNG cần restart, cực hữu ích trên production).

```bash
# py-spy: profile 1 process Python đang chạy trên production mà không cần dừng nó
py-spy top --pid 12345
```

---

## 4. Alerting đúng cách — tránh "alert fatigue"

**Sự cố văn hóa thường gặp:** alert quá nhạy (CPU > 50% cũng bắn cảnh báo) → team nhận hàng trăm alert/ngày → dần dần **bỏ qua tất cả**, kể cả alert quan trọng thật (đây gọi là "alert fatigue", nguyên nhân gốc rễ của rất nhiều outage nghiêm trọng trong thực tế ngành). Nguyên tắc senior:

- Alert phải **actionable** — mỗi alert bắn ra phải có hành động rõ ràng cần làm ngay, không phải "chỉ để biết".
- Alert theo **triệu chứng người dùng cảm nhận được** (error rate, latency p99) thay vì chỉ theo chỉ số nội bộ (CPU) — CPU cao chưa chắc ảnh hưởng user, nhưng error rate tăng thì chắc chắn có.
- Có **runbook** đính kèm mỗi alert quan trọng: khi alert này bắn, việc đầu tiên cần làm là gì.

---

## 🎯 Câu hỏi senior hay hỏi khi review

1. "Suite test của bạn chạy mất bao lâu? Có bao nhiêu % là E2E — có cần thiết không?"
2. "Nếu endpoint này chậm lúc 2h sáng, bạn có đủ log/metric/trace để debug mà không cần SSH vào server không?"
3. "Alert này có actionable không, hay chỉ làm ồn thêm cho on-call?"

## 🔗 Liên kết module khác
- N+1 query, connection pool là nguyên nhân phổ biến nhất của endpoint chậm → [`01-Request-Lifecycle-And-Architecture`](../01-Request-Lifecycle-And-Architecture/README.md)
- Slow query log & index → [`03-Database-Choice-And-Scaling-Playbook`](../03-Database-Choice-And-Scaling-Playbook/README.md)
- Observability ở tầng hạ tầng/container → [`Cloud-DevOps-Mastery`](../../Cloud-DevOps-Mastery/INDEX.md)
