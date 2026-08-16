# 01. Vòng Đời Một Request — Cách Backend Thật Sự Vận Hành

> Lý thuyết framework/ORM chi tiết đã có ở [`03-Python-Expert/`](../../../03-Python-Expert/) (Flask/Django/FastAPI) và [`04-Database-Mastery/`](../../../04-Database-Mastery/). File này nối các mảnh rời rạc đó thành **một luồng dữ liệu hoàn chỉnh** — điều mà tài liệu theo từng công nghệ riêng lẻ không thể hiện được.

---

## 1. Toàn cảnh: 1 request đi qua bao nhiêu tầng trước khi tới DB?

```
Client (browser/app)
   │  HTTPS request
   ▼
Load Balancer / CDN (CloudFront, Nginx)      ← xem 07-AWS-Mastery
   │
   ▼
Web Server (Nginx/Gunicorn) ──> WSGI/ASGI    ← Python_Backend_Professional_Guide.md mục 3-4
   │
   ▼
Framework (Flask/Django/FastAPI)
   │  Middleware chain (auth, CORS, logging, rate limit)
   ▼
View/Controller → Business Logic (Service layer)
   │
   ▼
ORM (Django ORM / SQLAlchemy)                ← PostgreSQL_Expert_Guide.md
   │  Connection Pool
   ▼
Database (Postgres/Mongo)
   │
   ▼
Cache layer (Redis) — có thể chen vào TRƯỚC bước gọi DB
```

**Vì sao senior phải nắm được toàn bộ luồng này, không chỉ 1 tầng:** khi API chậm, junior thường chỉ nhìn vào code trong view function. Senior biết độ trễ có thể nằm ở **bất kỳ tầng nào** — DNS resolve chậm, load balancer health-check sai, connection pool cạn kiệt, N+1 query, hay disk I/O của DB. Kỹ năng debug hệ thống thật là kỹ năng "định vị đúng tầng gây lỗi" trước khi đào sâu.

---

## 2. Middleware — nơi 90% cross-cutting concern thật sự nằm

Middleware xử lý các việc **áp dụng cho MỌI request** mà không nên lặp lại trong từng view: xác thực (auth), CORS, logging, rate limiting, nén response (gzip).

```python
# Middleware thực tế: log thời gian xử lý mỗi request — nền tảng của mọi hệ thống APM
import time

async def timing_middleware(request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    response.headers["X-Process-Time"] = str(duration)
    if duration > 1.0:  # ngưỡng cảnh báo — pattern dùng thật trong production
        logger.warning(f"SLOW REQUEST: {request.url} took {duration:.2f}s")
    return response
```

**Bài học senior:** middleware chạy theo **thứ tự khai báo**, và lỗi phổ biến nhất là đặt sai thứ tự (VD: middleware nén response chạy trước middleware auth → có thể rò rỉ dữ liệu lỗi chưa được auth check). Luôn vẽ sơ đồ thứ tự middleware khi review kiến trúc.

---

## 3. N+1 Query — con quái vật âm thầm giết hiệu năng production

Đây là bug hiệu năng **phổ biến nhất** trong mọi hệ thống dùng ORM (Django ORM, SQLAlchemy) — và nó **không hiện ra khi test với dữ liệu ít**.

```python
# ❌ N+1: 1 query lấy orders + N query lấy customer cho MỖI order
orders = Order.objects.all()          # 1 query
for order in orders:
    print(order.customer.name)        # +1 query MỖI vòng lặp → 1 + N query!

# ✅ Senior fix: JOIN trước bằng select_related (foreign key) / prefetch_related (many-to-many)
orders = Order.objects.select_related("customer").all()   # đúng 1 query duy nhất
```

**Vì sao nguy hiểm hơn junior nghĩ:** với 20 đơn hàng demo, N+1 chỉ chậm thêm vài ms — không ai để ý. Với 50,000 đơn hàng trên production, đây là 50,001 lần round-trip tới DB → timeout, và tệ hơn: **rút cạn connection pool**, khiến các request KHÁC (không liên quan) cũng bị treo theo. Đây là lý do senior luôn bật **query logging** ở môi trường staging trước khi deploy tính năng liên quan tới danh sách dữ liệu.

---

## 4. Connection Pool — tài nguyên hữu hạn thường bị bỏ quên

Mỗi kết nối DB tốn RAM + file descriptor ở cả 2 phía (app server và DB server). DB thường giới hạn cứng số connection đồng thời (Postgres mặc định `max_connections = 100`).

**Sự cố thật hay gặp:** deploy nhiều instance app (auto-scaling) mà mỗi instance mở pool riêng (VD: pool size 20 × 10 instance = 200 connection) → vượt giới hạn DB → **"too many connections", toàn bộ hệ thống down**, kể cả khi CPU/RAM của DB vẫn còn dư thừa.

**Giải pháp senior thực tế:**
- Dùng **connection pooler ở tầng trung gian** (PgBouncer cho Postgres) để nhiều app instance dùng chung 1 pool nhỏ tới DB thật.
- Luôn tính: `số instance × pool size mỗi instance ≤ max_connections DB - buffer cho admin/migration`.
- Set `pool_timeout` hợp lý — request chờ connection quá lâu nên fail nhanh (fail-fast) thay vì xếp hàng vô hạn làm nghẽn toàn hệ thống.

---

## 🎯 Câu hỏi senior hay hỏi khi review PR/thiết kế

1. "Endpoint này trả về danh sách — bạn đã kiểm tra query log xem có N+1 không?"
2. "Nếu traffic tăng 10x đột ngột, connection pool của bạn có bảo vệ được DB không, hay sẽ sập dây chuyền?"
3. "Middleware auth có chạy TRƯỚC middleware log response body không? Có rủi ro lộ dữ liệu nhạy cảm trong log không?"

## 🔗 Liên kết module khác
- Async/concurrency ảnh hưởng thế nào tới middleware chain → [`02-Concurrency-And-Async-In-Production`](../02-Concurrency-And-Async-In-Production/README.md)
- Chọn index/transaction đúng để N+1 fix không tạo ra vấn đề mới → [`03-Database-Choice-And-Scaling-Playbook`](../03-Database-Choice-And-Scaling-Playbook/README.md)
- Cách phát hiện N+1/slow query bằng công cụ thật → [`04-Testing-Observability-And-Debugging-Prod`](../04-Testing-Observability-And-Debugging-Prod/README.md)
