# 02. Concurrency & Async — Sự Thật Đằng Sau "Python Chậm"

> Lý thuyết AsyncIO/GIL đã có ở [`Python_Core_Mastery.md`](../../../03-Python-Expert/Python_Core_Mastery.md) mục 3 và [`Python_Backend_Professional_Guide.md`](../../../03-Python-Expert/Python_Backend_Professional_Guide.md) mục 3, 8. File này tập trung vào **quyết định kiến trúc thật**: khi nào dùng gì, và sự cố thật khi chọn sai.

---

## 1. GIL không phải "Python chậm" — mà là "Python threading không tăng tốc CPU-bound"

**Hiểu lầm phổ biến:** "Python chậm vì có GIL". **Sự thật:** GIL (Global Interpreter Lock) chỉ chặn nhiều **thread** chạy Python bytecode **song song trên nhiều lõi CPU cùng lúc**. Nó KHÔNG ảnh hưởng tới I/O-bound work (đọc file, gọi API, query DB) — trong lúc chờ I/O, GIL được nhả ra cho thread khác chạy.

| Loại tác vụ | Công cụ đúng | Vì sao |
|---|---|---|
| **I/O-bound** (gọi API, query DB, đọc file) | `asyncio` hoặc `threading` | Thời gian chờ I/O không cần CPU — asyncio xử lý hàng nghìn kết nối đồng thời trên 1 thread |
| **CPU-bound** (xử lý ảnh, tính toán ML, nén dữ liệu) | `multiprocessing` | Mỗi process có GIL riêng, dùng được nhiều lõi CPU thật |
| **Mixed** (vừa gọi API vừa xử lý nặng) | `asyncio` + `run_in_executor`/`ProcessPoolExecutor` | Đẩy phần CPU-bound ra process pool, giữ event loop rảnh cho I/O |

### 🔥 Case thật: "Thêm `async def` mà API không nhanh hơn — thậm chí chậm hơn"

```python
# ❌ Sai lầm kinh điển: dùng async nhưng gọi hàm BLOCKING bên trong
async def get_user_data(user_id: int):
    data = requests.get(f"https://api.example.com/users/{user_id}")  # BLOCKING!
    return data.json()
    # Hàm này "trông" async nhưng thực chất chặn ĐỨNG event loop —
    # mọi request khác đang chờ trên cùng event loop bị đóng băng theo.

# ✅ Đúng: dùng client HTTP bất đồng bộ thật sự
import httpx

async def get_user_data(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.example.com/users/{user_id}")
        return response.json()
```

**Đây là sự cố production có thật và rất phổ biến khi migrate Flask (sync) sang FastAPI (async):** dev quen tay dùng `requests`, `time.sleep()`, hoặc driver DB đồng bộ (`psycopg2`) bên trong `async def` — event loop bị block, **toàn bộ server đứng hình** dù code "trông có vẻ" bất đồng bộ. Đây là lý do senior luôn kiểm tra: mọi thư viện I/O trong code async đều phải có bản async thật (`httpx`, `asyncpg`, `motor` cho Mongo).

---

## 2. Worker model — vì sao `gunicorn -w 4` lại quan trọng hơn code

Một app Python (WSGI/ASGI) chạy dưới process manager (Gunicorn, Uvicorn) với N worker process. Đây là quyết định kiến trúc ảnh hưởng trực tiếp tới khả năng chịu tải:

- **Sync worker (Flask mặc định):** mỗi worker xử lý 1 request tại 1 thời điểm — cần **nhiều worker process** để xử lý đồng thời (`workers = 2 × số_lõi_CPU + 1` là công thức kinh điển).
- **Async worker (Uvicorn/FastAPI):** 1 worker xử lý hàng nghìn kết nối I/O-bound đồng thời trên 1 event loop — nhưng vẫn cần nhiều worker process để tận dụng nhiều lõi CPU (vì 1 event loop chỉ chạy trên 1 lõi).

**Sự cố thật:** deploy FastAPI với `--workers 1` vì nghĩ "async đã nhanh rồi" → chỉ dùng được 1 lõi CPU trên máy 8 lõi, throughput giảm 8 lần so với khả năng thật của server. Senior luôn benchmark số worker tối ưu bằng load test thật (Locust, k6), không đoán mò.

---

## 3. Background Task — đừng để user chờ việc không cần chờ ngay

```python
# ✅ Pattern thật: trả response ngay, xử lý việc nặng (gửi email, resize ảnh) sau
from fastapi import BackgroundTasks

@app.post("/register")
async def register(user: UserCreate, background_tasks: BackgroundTasks):
    new_user = create_user(user)
    background_tasks.add_task(send_welcome_email, new_user.email)  # không block response
    return {"id": new_user.id}
```

**Giới hạn cần biết:** `BackgroundTasks` của FastAPI chạy **trong cùng process** — nếu server restart giữa lúc task đang chạy, task **mất luôn**, không retry. Với tác vụ quan trọng (gửi email xác nhận thanh toán), senior dùng **queue thật** (Celery + Redis/RabbitMQ, hoặc AWS SQS) có persistence + retry + dead-letter-queue — liên kết trực tiếp với kiến thức Queue ở [`DSA-Mastery/02-Linear-Structures-And-Hashing`](../../DSA-Mastery/02-Linear-Structures-And-Hashing/README.md).

---

## 🎯 Câu hỏi senior hay hỏi khi review

1. "Hàm `async def` này có gọi hàm blocking nào ẩn bên trong không (thư viện sync, `time.sleep`, driver DB đồng bộ)?"
2. "Bạn set bao nhiêu worker process — dựa trên benchmark thật hay đoán?"
3. "Nếu server crash giữa lúc xử lý background task, dữ liệu có bị mất không? Có cơ chế retry không?"

## 🔗 Liên kết module khác
- Middleware/request lifecycle nơi async ảnh hưởng trực tiếp → [`01-Request-Lifecycle-And-Architecture`](../01-Request-Lifecycle-And-Architecture/README.md)
- Queue/Worker pattern liên hệ trực tiếp DSA → [`DSA-Mastery/02`](../../DSA-Mastery/02-Linear-Structures-And-Hashing/README.md)
- Deploy nhiều worker/instance liên quan trực tiếp tới container orchestration → [`Cloud-DevOps-Mastery`](../../Cloud-DevOps-Mastery/INDEX.md) (đợt kế tiếp)
