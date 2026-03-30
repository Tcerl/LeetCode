# TÀI LIỆU ÔN LUYỆN PHỎNG VẤN CHI TIẾT - FULLSTACK DEVELOPER (PYTHON + VUE.JS + ODOO)
Dựa trên yêu cầu công việc (3+ năm kinh nghiệm), tài liệu này được nâng cấp với mức độ chi tiết và chuyên sâu, tập trung vào kỹ năng vận hành thực tế, giải quyết vấn đề hệ thống và kiến thức cốt lõi.

---

## PHẦN 1: LỘ TRÌNH ÔN LUYỆN CHUYÊN SÂU

### 1. Kiến thức cốt lõi & Ngôn ngữ (Language Core)
**A. Python (Deep Dive):**
*   **Memory Management & Garbage Collection:** Reference counting và Garbage collector (Generational GC). Tránh vòng lặp tham chiếu (Reference Cycles).
*   **Đa luồng & Đa tiến trình:** Hiểu sâu về GIL (Global Interpreter Lock). Khi nào dùng `threading`, `multiprocessing`, `concurrent.futures` hay `asyncio`.
*   **Tính năng nâng cao:** Metaclasses, Context Managers (`with` statement, `__enter__`, `__exit__`), Generators nâng cao (`yield from`), Decorators có tham số.
*   **Typing:** Type hinting trong Python (`typing` module) áp dụng cho FastAPI/Pydantic.

**B. JavaScript / TypeScript & Vue 3:**
*   **JS Engine:** V8 Engine, Call Stack, Memory Heap, Event Loop (Microtask vs Macrotask), Hoisting, Closures.
*   **Vue 3 Core:** Reactivity system dưới background (ES6 Proxy thay vì `Object.defineProperty` như Vue 2). Virtual DOM và Diffing algorithm.
*   **Vue 3 Advanced:** Custom Directives, Render functions / JSX, Teleport, Suspense. Quản lý state toàn cục với Pinia (thay thế Vuex).
*   **Micro-frontend / SSR:** Khái niệm Server-Side Rendering (Nuxt.js) vs Client-Side Rendering (Vue SPA).

### 2. Kiến thức Framework & Backend Systems
*   **Django / Flask / FastAPI:**
    *   **FastAPI:** Starlette (ASGI) vs WSGI, Pydantic validations, Dependency Injection system.
    *   **Django:** Vòng đời của 1 request (Middleware, URL Router, View, Template/Response). Custom User Model, Signals, Celery integration.
*   **Database (PostgreSQL / MySQL):**
    *   **Indexing & Performance:** Phân biệt B-Tree, Hash, GIN, GiST (trong PostgreSQL). Query Plan (`EXPLAIN ANALYZE`).
    *   **Concurrency Control:** ACID, Isolation Levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable), Locking mechanisms, Deadlocks.
*   **System Design & Architecture:**
    *   **Caching:** Redis/Memcached (Cache invalidation strategies: LRU, LFU, Write-through, Read-through).
    *   **Message Brokers:** RabbitMQ (AMQP) vs Kafka. Pub/Sub pattern, Worker queues (Celery).
    *   **RESTful API vs GraphQL:** Phân trang (Offset/Cursor-based), Rate limiting, Versioning (v1, v2).

### 3. Odoo ERP (Strong Advantage - Deep Customization)
*   **Kiến trúc:** Khác biệt giữa Models (`models.Model` - DB Table), TransientModel (`models.TransientModel` - Tự động xóa, dùng cho Wizards/Popups) và AbstractModel.
*   **ORM Advanced:** `self.env` (Environment), `self.sudo()` (Bỏ qua Security rules), `self.with_context()`. Batch operations để tối ưu performance.
*   **Security:** Access Rights (CSV) vs Record Rules (XML).
*   **UI/UX (QWeb):** Kế thừa Views bằng XPath (`expr`, `position="before|after|replace|inside"`).

---

## PHẦN 2: BỘ CÂU HỎI PHỎNG VẤN CHUYÊN SÂU & TRẢ LỜI CHI TIẾT

### NHÓM 1: PYTHON & BACKEND (MỨC ĐỘ KHÓ: KHÁ/GIỎI)

**Q1: Phân biệt `__new__` và `__init__` trong Python? Khi nào cần override `__new__`?**
* **Trả lời:**
  * `__new__` là phương thức định nghĩa việc **tạo ra (create)** một instance (đối tượng) mới. Nó được gọi TRƯỚC và trả về một instance. Đây là phương thức tĩnh (static method) của class.
  * `__init__` là phương thức **khởi tạo (initialize)** trạng thái cho instance đó (gán giá trị cho thuộc tính). Nó được gọi SAU `__new__` và không trả về gì cả (`return None`).
  * *Thực tế:* Ta hiếm khi đụng đến `__new__` trừ khi cần triển khai pattern **Singleton** (đảm bảo chỉ có 1 instance được tạo ra) hoặc kế thừa từ các immutable built-in types (như `int`, `tuple`).

**Q2: Giải thích GIL trong Python. Nếu GIL làm Python chạy chậm trên multi-core, tại sao người ta vẫn chuộng Python cho Backend và AI? Làm sao vượt qua hạn chế của GIL?**
* **Trả lời:**
  * **GIL (Global Interpreter Lock)** lock interpreter lại, đảm bảo tại 1 thời điểm chỉ 1 thread thực thi Python bytecode (ngăn chặn race conditions trong memory management của CPython).
  * **Tại sao vẫn chuộng?** Hầu hết các thư viện AI/Data (NumPy, PyTorch) và lệnh gọi hệ thống nội bộ (I/O, Network calls, Database query) đều được viết bằng C/C++. Khi các code này chạy, chúng tác động trực tiếp lên C-level và **tự giải phóng (release) GIL**, cho phép multi-threading thực sự. Hơn nữa HTTP servers như Gunicorn chạy đa tiến trình (multi-processing), mỗi tiến trình có 1 GIL riêng nên không bị nghẽn nhau.
  * **Cách khắc phục cho code ứng dụng:** Thay vì dùng `threading` cho tác vụ CPU-bound, dùng module `multiprocessing`. Sử dụng Async/await (`asyncio`) cho I/O-bound (gọi API gọi DB).

**Q3: Trình bày chi tiết vấn đề N+1 query và đưa ra ví dụ bằng Django ORM hoặc SQLAlchemy.**
* **Trả lời:**
  * N+1 xảy ra khi bạn query danh sách M phần tử (1 query), sau đó vòng lặp qua M phần tử này và lấy dữ liệu liên kết tạo ra thêm N queries phụ. Làm nghẽn I/O Database nghiêm trọng.
  * **Giải pháp trong Django:**
    * **`select_related()`**: Dùng cho quan hệ ForeignKey (One-to-Many chiều ngược / One-to-One). Nó tạo ra câu SQL **JOIN** ở tầng Database và lấy toàn bộ dữ liệu chỉ với 1 query duy nhất.
    * **`prefetch_related()`**: Dùng cho quan hệ Nhiều-Nhiều (Many-to-Many) hoặc 1-Nhiều (One-to-Many chiều thuận). Nó tạo ra **2 queries độc lập**: 1 query lấy bảng A, 1 query dùng `WHERE ... IN (...)` lấy bảng B, sau đó map (ráp nối) kết quả lại bằng Python trên memory cache.

**Q4: Nêu các nguyên lý đánh Index trong CSDL. Khi bạn có 1 truy vấn `SELECT * FROM users WHERE status = 'active' AND age > 25`, bạn sẽ đánh index như thế nào?**
* **Trả lời:**
  * Ta dùng **Composite Index (Index kép)**.
  * **Quy tắc (Rule of thumb):** Đặt cột sử dụng toán tử so sánh bằng (Equality `=`) lên trước, các cột dùng toán tử khoảng (Range `>`, `<`, `BETWEEN`) xuống sau.
  * **Giải pháp:** Tạo index trên `(status, age)`.
  * Vì sao? B-Tree sẽ phân luồng theo `status` trước, nhảy thẳng đến nhánh có 'active', sau đó duyệt cây con đã được sắp xếp theo `age` để quét các node > 25. Nếu đặt `age` tạo nhánh trước, DB không thể tận dụng index cho phần `status` tiếp theo.

---

### NHÓM 2: VUE 3 & FRONTEND (MỨC ĐỘ KHÓ: KHÁ/GIỎI)

**Q5: Vue 3 quản lý tính Reactivity (phản ứng) như thế nào so với Vue 2? Lợi ích mang lại là gì?**
* **Trả lời:**
  * Vue 2 dùng kỹ thuật `Object.defineProperty` để ghi đè getter/setter từng thuộc tính sâu bên trong của object ngay lúc mới khởi tạo component. Khuyết điểm: Không thể detect được việc bạn tự thêm/xóa property mới khỏi object (phải dùng hàm `Vue.set`), và làm việc mảng có thể không chính xác khi gán qua index/length. Trình tạo Reactivity phải duyệt đệ quy làm tốn performance startup.
  * Vue 3 dùng chuẩn API hiện đại **ES6 Proxy**. Lớp Proxy này bao bọc toàn bộ Object/Array. Mọi loại hành vi đọc hay gán dữ liệu (Get, Set, Delete, Has...) đều bị chặn lại (intercepted) ở mức độ Object tổng thể chứ không phải đi bới từng Key.
  * **Lợi ích:** Nhanh hơn, bắt được mọi sự kiện thay đổi dữ liệu một cách linh hoạt, code lõi bảo trì cũng dễ hơn nhiều.

**Q6: Bạn viết Component giao tiếp bằng cách nào nếu chúng có cấu trúc phân cấp cực kì sâu (Ông nội -> Cha -> Cháu -> Chắt)?**
* **Trả lời:**
  * Nếu dùng Props drilling (chuyền qua từng cấp), code sẽ rác, phải bảo trì trung gian rất nhiều.
  * **Giải pháp 1 (Sử dụng API Local):** Dùng cặp hàm `provide(key, data)` ở Component cấp cao nhất và `inject(key)` ở bất cứ component con cháu nào cần. Nó giữ nguyên tính reactive đối với Composition API `ref/reactive`.
  * **Giải pháp 2 (Sử dụng Component Store):** Dùng State Management như **Pinia**. Rất lý tưởng nếu những thông tin đó (vd: thông tin User, Setting App, Giỏ hàng) được dùng ở rất nhiều nơi nằm rải rác.

**Q7: `Teleport` trong Vue 3 dùng để làm gì? Nêu một use-case thực tế.**
* **Trả lời:**
  * Thẻ `<Teleport>` cho phép ta xuất (render) template ảo của component vào một nút DOM (DOM node) ở ngoài cây cha của nó, dù mặt vật lý file code hai bên vẫn gắn kết.
  * **Usecase phổ thông nhất:** Làm hệ thống Popups, Modals, Tooltips, Fullscreen Overlay... Ví dụ 1 Form Nằm trong Box Card con bị dính CSS `overflow: hidden;` của Box Cha. Khi bật popup Modal nó sẽ bị cắt mất. Dùng `<Teleport to="body">` sẽ ném khung HTML modal này an toàn nằm sát trong thẻ Root Body gốc, hoàn toàn thoát khỏi ma trận CSS của Component cha mà Logic Javascript bên trong Modal vẫn sống khoẻ.

---

### NHÓM 3: ODOO ERP NÂNG CAO (MỨC ĐỘ KHÓ: MIDDLE/SENIOR)

**Q8: Giải thích sự phân chia vai trò của `models.Model`, `models.TransientModel` và `models.AbstractModel` trong Odoo framework.**
* **Trả lời:**
  * **`models.Model`**: Dùng cho Dữ liệu cứng. Tự sinh ra DB Tables và lưu vĩnh viễn (VD: `sale.order`, `res.partner`).
  * **`models.TransientModel`**: Dữ liệu Tạm thời (Chỉ xuất hiện Wizard, Cửa sổ phụ, Popup nhập params report). Mỗi database định kỳ có Cron job Odoo dọn dẹp các dòng quá hạn, không bao giờ load nặng DB.
  * **`models.AbstractModel`**: KHÔNG tạo ra DB tables vật lý nào cả. Abstract y như một mẫu base Mixins. Vd Odoo định nghĩa abstract module là hàm gửi mail, các Models thực tế muốn thừa hưởng tính năng này chỉ việc thêm `_inherit = ['mail.thread']` là toàn bộ hàm Email nhảy sang file Database Model đó một cách gọn lẹ.

**Q9: Batch Performance: Khi code một logic update hàng vạn record dữ liệu trong Odoo, làm sao để tối ưu hóa triệt để?**
* **Trả lời:**
  * **Lỗi kinh điển (N+1 Update in Odoo):** Dùng dòng lặp for đi qua từng `rec` của Odoo Recordset và chạy `rec.write({'state': 'done'})`. Hàm gọi này sinh SQL liên tục, kích hoạt triggers, update onchange gây nghẽn RAM memory sập module Web.
  * **Cách xử lý đúng chuẩn:** Dùng Bulk API: Chạy đúng 1 lệnh write gộp `self.write({'state': 'done'})` (Bản thân biến `self` đã chứa nhiều record IDS). Odoo ORM sẽ tóm toàn bộ chạy ra duy nhất 1 SQL `UPDATE ... WHERE id IN (1,2,3...)`.
  * *Notes Thêm:* Cần thận trọng khi override `.write()` hay `.create()`, tránh vòng lặp đệ quy, nếu phải lưu khối data khủng không ràng buộc có thể drop raw SQL qua `self.env.cr.execute()`.

**Q10: Khác biệt ngầm giữa `_inherit` (Thêm s không?) và `_inherits` (Delegation Inheritance)?**
* **Trả lời:**
  * `_inherit`: Xài trên 90%. Nới rộng bản thân bảng đó ra, chèn Field mới, can thiệp lại Function sẵn có (Classical base object Mixin).
  * `_inherits` (Có đuôi chữ 's'): Kế thừa kiểu Nhúng/Ủy quyền bảng (Delegation).
    **Ví dụ cụ thể:** Khi tạo Model Users của Odoo (`res.users`), nó khai báo `_inherits = {'res.partner': 'partner_id'}`. Điều này khiến cho Users ko cần định nghĩa lặp lại các thuộc tính Address, Email... mà tự động trỏ tham chiếu sang Partner. Bất kỳ lệnh cập nhật Email nào ở bảng Users sẽ ngầm đổ dữ liệu đó về bảng vật lý Partner qua khóa link kia.

**Q11: Khái niệm Context (`self.env.context`) trong Odoo mang lại sức mạnh gì cho luồng xử lý?**
* **Trả lời:**
  * Context là bộ "Bộ Nhớ Ngữ Cảnh" truyền ngầm ẩn suốt qua mọi Request luân chuyển từ Action -> Window/Views UI -> Python Database ORM.
  * Chức năng mạnh nhất là:
    1. Đưa giá trị Default field: Cho action xml `context="{'default_is_company': True}"` khi người ta bấm Cài Mới giao diện tự đánh tích.
    2. Chế độ Language Translation: Nếu truyền `self.with_context(lang='en_US')`, hàm xuất báo cáo PDF Python sẽ query String được phiên dịch bằng tiếng Anh thay vì tiếng Việt của User.
    3. Bypass/Flag cắm cờ cho Backend phân nhánh logic nghiệp vụ (với cùng 1 logic call) hoặc bắt Odoo tắt các hàm `onchange` tự động cản trở quá trình import DB lớn.

---

### NHÓM 4: SYSTEM DESIGN, ARCHITECTURE & DEVOPS (MỨC ĐỘ KHÓ: SENIOR)

**Q12: Tương lai bạn cần thiết kế một ứng dụng REST API để cho phép người dùng Upload các tệp kích cỡ tới 2GB-5GB. Bạn giải quyết ra sao?**
* **Trả lời:**
  * Chặn đầu tiên là nếu Frontend bọc ảnh ném thẳng qua Backend (Django/Python HTTP), Data này sẽ kẹt trong Memory RAM Python lâu lắc gây sập Thread Workers Của Web Server.
  * Giải pháp đỉnh cao và an toàn: **Pre-signed Object Storage (vd API AWS S3/Minio)**:
    1. Client (trình duyệt Vue JS) bắn API nhẹ tênh hỏi Backend: "Hãy cho tao quyền upload cái file X năng 2G"
    2. Backend Generate ra một link "Pre-signed PUT Object URL" của Cloud Oject Storage với hạn dùng khóa 15 phút đưa cho Client.
    3. Trình duyệt Frontend tải file **Xuyên qua thẳng** đến Cloud Storage (AWS S3) không đi qua Backend nữa.
    4. Xong xuôi, Client báo cho Backend: File đã up xong, đường dẫn S3 này nhé. Hoặc bản thân S3 sẽ chủ động webhook bắn "Events File Upload Finished" gọi đến Node Backend Python lưu DB lại đường Path là xong tiến trình.

**Q13: Trình bày sự thiết yếu phân chia "Stateful" và "Stateless" application trong Kubernetes Docker. Hệ Backend Microservices nên để chuẩn nào?**
* **Trả lời:**
  * **Stateful:** Lưu lại Trạng thái trên bản thân cái máy chạy nó. Lưu Session vào vùng Memory Node ảo, Lưu Media user vào ổ Data cục bộ. Khi Server Load banlance phân quyền 1 Request qua Node (Container A), nếu user bị gửi qua Node B... Bị Kick văng ra vì Node B ko có info User RAM. 
  * **Stateless:** Bản thân cái Server API chả có Trạng thái (Cache memory, DB, Disk). Nhận request, hỏi mọi trạng thái từ ngoài (SQL / Redis tập trung), logic xử lý xong trả.
  * Tất nhiên Backend Apps/Workers phải bắt buộc là Stateless để DevOps thiết lập Auto-scaling/High Availablity (Nhân lên 50 pod chạy lúc cao điểm mà k vướng bận gì Session lạc dòng cả). Phần Lưu trữ đổ hết về DB và Object Storage Servers quản lý.

**Q14: Quá trình thiết lập CI/CD Pipeline Build 1 bộ Fullstack Apps lên môi trường Server qua Github Actions chạy qua những bước nào?**
* **Trả lời:**
  * Gồm Workflow Steps bài bản:
    1. **Format/Linter / Type Checks:** (như Black, Flake8, ESLint, TypeScript Check). Sai syntax block chết pipeline từ đầu.
    2. **Run Tests:** Chạy file Docker TestDB cô lập (Pytest) / Frontend Components tests (Vitest). Yêu cầu Test Coverage đạt ngưỡng mới thông hành.
    3. **Containerize / Build Artifacts:** Run Script Backend Compile (`docker build` làm Images), Npm Bundle phần Frontend tạo file Dist tĩnh hoặc Build SSR.
    4. **Push Registry:** Upload images mới lên Private Docker Registry (Vd: Github PR, GitLab CR).
    5. **Deploy & Webhook:** Kích hoạt trigger đến Server Staging/Production để Pull image mới xuống. Tự động áp dụng `Alembic/Django Migrations` DB Schema nếu có. Push Telegram bot báo cáo DevOps tiến trình hoàn thiện màu Xanh (Xong).
---

## PHẦN 3: CÁC VÍ DỤ CODE THỰC TẾ (PRACTICAL USE-CASES)

Để chuẩn bị tốt hơn nếu người phỏng vấn yêu cầu bạn pseudo-code, hoặc review live code, dưới đây là một số ví dụ trọng điểm:

### Ví dụ 1: Custom Hook (Composable) trong Vue 3
Trong Vue 3 (Composition API), việc tách logic gọi API thành một "Composable" tái sử dụng ở mọi nơi là kỹ năng Middle/Senior bắt buộc.

```javascript
import { ref, unref, watchEffect } from 'vue'

export function useFetchData(url) {
  const data = ref(null)
  const error = ref(null)
  const isLoading = ref(true)

  async function fetchData() {
    isLoading.value = true
    error.value = null
    try {
      // unref(): Giúp hàm fetchData linh hoạt, người dùng truyền chuỗi string thẳng 
      // hoặc truyền 1 biến dạng ref() vào url đều tự động lấy được giá trị.
      const response = await fetch(unref(url))
      if (!response.ok) throw new Error('API request failed')
      data.value = await response.json()
    } catch (err) {
      error.value = err
    } finally {
      isLoading.value = false
    }
  }

  // watchEffect: Tự động đánh hơi (track) biến url nếu nó là `ref`. 
  // Ngay khi url thay đổi (vd đổi id page), function tự gọi lại API lập tức!
  watchEffect(() => fetchData())

  return { data, error, isLoading }
}
```

### Ví dụ 2: Giải quyết bài toán N+1 bằng Python (Django ORM)
Giả định bảng Bài Viết (Article) trỏ khóa ngoại (ForeignKey) về Tác Giả (Author). Khi in Bài Viết ta cần cả tên Tác Giả.

```python
# 🚫 LỖI CƠ BẢN (Gây ra N+1 Query làm sập web)
articles = Article.objects.all() # Chỉ chạy 1 SQl query lấy Articles
for art in articles:
    # Ở dòng này ORM bắn thêm 1 lệnh DB query nữa với TỪNG dòng bài viết
    # Nếu vòng lặp 500 bài viết -> Sẽ bắn thêm 500 query SQL lên database!
    print(art.title, art.author.name) 


# ✅ CÁCH ĐÚNG CỦA SENIOR DEV (Tối ưu về 1 Query)
# Dùng select_related() nó sẽ ép Database chạy luôn câu INNER JOIN giữa 2 bảng.
articles = Article.objects.select_related('author').all()
for art in articles:
    # Câu lặp này chỉ đọc trên vùng RAM Python hiện tại, Tốc độ đạt mức tức thời (O(1))
    print(art.title, art.author.name) 
```

### Ví dụ 3: Cấu hình Github Actions CI/CD Cơ Bản
Để chứng minh bạn từng đụng tới quy trình lên Server, đây là file Workflow chuẩn (`.github/workflows/deploy.yml`) cho một pipeline cơ bản để đẩy file lên staging Server.

```yaml
name: Fullstack CI/CD Pipeline

# Kích hoạt ống nước này chỉ khi có ông nào PUSH code mới vào nhánh MAIN
on:
  push:
    branches:
      - main

jobs:
  build_test_deploy:
    runs-on: ubuntu-latest
    steps:
      - name: 1. Checkout repository
        uses: actions/checkout@v3

      - name: 2. Setup Python environment
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: 3. Linter - Check vi phạm cấu trúc Code (Flake8)
        run: |
          pip install flake8
          flake8 .
      
      # Giả thiết pass mọi unit test, nhảy qua Deploy
      - name: 4. Deploy lên Server Production qua SSH
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          # Thực thi kịch bản CLI khi vào sâu bên trong máy Server thật
          script: |
             cd /var/www/my_fullstack_app
             git pull origin main
             
             # Rebuild docker images nếu có gì thay đổi và đè ngầm -d (detach mode)
             docker-compose build
             docker-compose up -d
```

---

## PHẦN 4: TỔNG HỢP KIẾN THỨC BỔ TRỢ & NÂNG CAO TỪ CÁC TÀI LIỆU HỆ THỐNG

Phần này tổng hợp các "vàng ròng" kiến thức từ các tài liệu khác trong máy (`ODOO_INTERVIEW_ADVANCED.md`, `Python_Special_Functions.md`, v.v.) để bạn có cái nhìn toàn diện nhất.

### 1. Python Deep Dive - Bổ sung các khái niệm "thường bị hỏi"
*   **`__slots__`**: Giúp tiết kiệm bộ nhớ bằng cách ngăn Python tạo ra `__dict__` cho mỗi instance. Odoo sử dụng rất nhiều trong các Class lõi để tối ưu RAM khi load hàng ngàn bản ghi.
*   **Shallow Copy vs Deep Copy**:
    *   `Shallow Copy (copy.copy)`: Tạo object mới nhưng bên trong vẫn tham chiếu đến các list/dict của object cũ. Thay đổi con này sẽ ảnh hưởng con kia.
    *   `Deep Copy (copy.deepcopy)`: Sao chép toàn bộ, tạo ra một bản thể độc lập hoàn toàn.
*   **Closures**: Là hàm "nhớ" môi trường (Scope) nơi nó được sinh ra kể cả khi hàm cha đã chạy xong. Dùng để tạo ra các hàm có trạng thái riêng mà không cần dùng Class.
*   **Mutable Default Arguments**: Tuyệt đối không dùng `def func(a=[])`. List này được khởi tạo 1 lần duy nhất lúc load code. Mọi lần gọi hàm sau sẽ dùng chung cái List đó -> Gây lỗi logic dữ liệu chồng chéo. Cách đúng: `a=None` rồi `a = [] if a is None else a`.

### 2. Odoo Framework - Chuyên sâu vận hành (Advanced ORM)
*   **SQL View Model (`_auto = False`)**: Khi bạn cần làm các Dashboard báo cáo phức tạp (Pivot/Graph) mà ORM query quá chậm, bạn gán `_auto = False` và viết code SQL thô tạo View. Odoo sẽ coi View đó như một Table bình thường để bạn kéo thả giao diện.
*   **Cơ chế Flush & Invalidate Cache**:
    *   `self.env.flush_all()`: Ép ORM đẩy toàn bộ dữ liệu đang chờ trong RAM xuống Database ngay lập tức (Cần thiết trước khi chạy SQL thô `cr.execute`).
    *   `self.env.invalidate_all()`: Xóa sạch cache trong RAM của Odoo để buộc các hàm sau phải query lấy dữ liệu mới nhất từ database.
*   **`exists()` vs `filtered()`**:
    *   `exists()`: Kiểm tra xem record có thực sự tồn tại trong DB không (loại bỏ record ảo hoặc đã bị user khác xóa).
    *   `filtered()`: Lọc recordset dựa trên logic Python (chạy trên RAM, cực nhanh nếu data đã được load).
*   **Lưu trữ Binary (Ảnh/File)**: Odoo mặc định lưu trong **Filestore** (thư mục ngoài DB). Database chỉ lưu checksum (đường dẫn). Điều này giúp Database nhẹ và dễ backup hơn.

### 3. Database Performance & Admin (PostgreSQL)
*   **PostgreSQL VACUUM**: Khi bạn Update/Delete, Postgres không xóa ngay mà đánh dấu "dead tuple". Nếu không chạy `VACUUM` định kỳ, Database sẽ bị phình to (Bloat) làm hệ thống chạy chậm như rùa.
*   **Explain Analyze**: Công cụ tối thượng để debug SQL. Nếu thấy "Seq Scan" trên bảng lớn -> Thiếu Index. Nếu thấy "Index Scan" -> Tốt.
*   **Connection Pooling**: Odoo dùng `Psycopg2` pool để duy trì kết nối. Tránh việc mỗi request khách hàng lại mở 1 connect mới gây quá tải CPU của Database Server.

### 4. Git Workflow cho đội nhóm (Collaborative Dev)
*   **Git Merge vs Rebase**:
    *   `Merge`: Tạo 1 commit gộp, giữ nguyên lịch sử rẽ nhánh (An toàn, dùng cho các nhánh Master/Staging).
    *   `Rebase`: "Gọt" lại lịch sử cho thẳng hàng (Dùng cho nhánh Feature cá nhân trước khi đẩy lên để tránh các commit "Merge branch...").
*   **Git Stash**: Cất code đang viết dở vào "kho tạm" để chuyển nhánh fix bug gấp mà không muốn commit rác.
*   **Git Cherry-pick**: Bốc duy nhất 1 commit sửa lỗi từ nhánh A sang nhánh B mà không muốn lấy cả đống code khác của nhánh A.
*   **Git Commit --amend**: Sửa tên commit hoặc thêm file vào commit vừa mới bấm nhầm (chỉ dùng khi chưa Push lên Server).

### 5. Security & Phân quyền (Internal Systems)
*   **`sudo()` vs `with_user()`**:
    *   `sudo()`: Nhảy thẳng lên quyền Admin (vượt qua mọi Record Rules). Dùng cho các logic hệ thống tự động (Vd: Tự tạo Invoice khi khách bấm nút).
    *   `with_user(user)`: Giả danh một User cụ thể để kiểm tra xem với quyền của người đó thì code có chạy được không (Dùng để test bảo mật).
*   **Access Rights (CSV) vs Record Rules (XML)**:
    *   `Access Rights`: Quyền "Cửa" (Bạn có được vào xem bảng Sản phẩm không?).
    *   `Record Rules`: Quyền "Hàng" (Bạn vào được bảng Sản phẩm rồi, nhưng chỉ được xem Sản phẩm do chính bạn tạo ra thôi).

---

## PHẦN 5: TƯ DUY KIẾN TRÚC & PHÁT TRIỂN HỆ THỐNG (VUE 3 NÂNG CAO & NUXT.JS)

Dành cho trình độ Senior, nhà tuyển dụng sẽ không chỉ hỏi "làm thế nào" mà sẽ hỏi "làm sao cho tối ưu nhất".

### 1. Vue 3 Reactivity - Làm chủ hiệu năng
*   **`shallowRef` & `markRaw`**: 
    *   Mặc định `ref` sẽ track đệ quy toàn bộ object con. Với các object cực lớn (như instance của Chart.js, Google Maps, hoặc dữ liệu raw hàng vạn dòng), việc này gây lag. 
    *   Giải pháp: Dùng `shallowRef` để chỉ track ở cấp độ 1 (khi gán lại biến). Dùng `markRaw` để nói với Vue "đừng làm biến này thành reactive", giúp tiết kiệm 80% RAM cho các thư viện bên thứ 3.
*   **`watch` vs `watchEffect`**:
    *   `watch`: Phải chỉ định rõ biến cần theo dõi (Lazy). Biết được giá trị Cũ và Mới. Dùng khi bạn muốn làm gì đó dựa trên "sự thay đổi cụ thể".
    *   `watchEffect`: Tự động nhận diện mọi biến reactive bên trong nó (Eager - chạy ngay lập tức). Rất hữu ích khi viết Fetch API: `watchEffect(() => fetch('/api/' + id.value))`.
*   **`onCleanup` trong watchEffect**: Dùng `AbortController` để hủy các request cũ nếu User bấm chuyển trang/chuyển ID liên tục, tránh việc dữ liệu cũ đè lên dữ liệu mới (Race conditions).

### 2. Pinia - State Management Chuẩn "Sạch"
*   **Composition Stores**: Viết Store giống hệt Setup function (dùng `ref`, `computed`, `function`). Cách này dễ đọc và linh hoạt hơn Option Store truyền thống.
*   **`storeToRefs`**: Quan trọng! Khi bạn phá cấu trúc (destructuring) một store: `const { name } = cartStore`, biến `name` sẽ bị mất tính phản ứng. Phải dùng `const { name } = storeToRefs(cartStore)`.

### 3. Nuxt.js & Rendering Strategies (SEO & Speed)
*   **SSR (Server Side Rendering)**: Server render ra HTML rồi gửi về. Tốt cho SEO, nhanh ở lần load đầu.
*   **ISR / SWR (Incremental Static Regeneration)**: Nuxt sẽ cache HTML trên máy chủ. Ví dụ: Trang chi tiết sản phẩm. Cứ mỗi 1 tiếng nó mới re-render lại 1 lần. Cực kỳ nhanh vì browser chỉ việc hốt cache về.
*   **`useFetch` vs `useAsyncData`**:
    *   `useFetch`: Shortcut nhanh để gọi API.
    *   `useAsyncData`: Dùng khi bạn cần xử lý logic phức tạp (Vd: Gọi 3 API cùng lúc rồi mới gộp data trả về).

### 4. Tối ưu Giao diện lớn
*   **`v-memo`**: Tính năng mới của Vue 3.4+. Dùng để ra lệnh cho Vue "chỉ re-render cái list này nếu ID hoặc trạng thái selected thay đổi". Tiết kiệm hàng ngàn lần tính toán DOM ảo.

---

## PHẦN 6: CÂU HỎI TÌNH HUỐNG & KỸ NĂNG MỀM (SOFT SKILLS)

Đứng ở góc độ Senior Fullstack 3+ năm, bạn cần thể hiện tư duy quản lý và giải quyết vấn đề.

**Q1: Bạn sẽ làm gì nếu nhận lại một Source code "rác", không có tài liệu và deadline đang đến gần?**
* **Trả lời:** 
    1. **Khảo sát:** Đọc file `package.json/requirements.txt` để hiểu stack. Chạy thử dự án, record lại các luồng chính bằng công cụ Network/Logs.
    2. **Cô lập:** Không đập đi xây lại toàn bộ. Chỉ refactor những phần logic bạn chuẩn bị sửa/thêm tính năng.
    3. **Tài liệu hóa:** Viết file `README.md` mới mô tả cách chạy và các "điểm nóng" (pain points) bạn phát hiện.
    4. **Giao tiếp:** Báo cáo Leader về tình trạng code để điều chỉnh deadline hoặc phạm vi tính năng (Scope) phù hợp.

**Q2: Làm sao để bạn đảm bảo chất lượng code trong một team có nhiều thành viên trình độ khác nhau?**
* **Trả lời:**
    1. **Code Review:** Thiết lập văn hóa review chéo. Pull Request (PR) phải có ít nhất 2 người duyệt mới được merge.
    2. **Linting & Formatter:** Ép dùng chung bộ rule (ESLint cho Vue, Black/Flake8 cho Python) để tránh tranh cãi về format.
    3. **Unit Tests:** Viết test cho các hàm logic cốt lõi (Xử lý tiền tệ, phân quyền).
    4. **Tài liệu Wiki:** Viết các hướng dẫn (Guidelines) về cách đặt tên, cấu trúc thư mục chuẩn của công ty.

**Q3: Kể về một lỗi Production nghiêm trọng bạn từng gặp và cách bạn xử lý?**
* **Gợi ý trả lời:** Hãy kể về một lần "Down server" hoặc "Lỗi dữ liệu". 
    - Tập trung vào: **Bình tĩnh cô lập lỗi** -> **Rollback (Quay lại bản cũ)** để cứu hệ thống trước -> **Tìm lỗi (Root Cause Analysis)** ở máy local -> **Viết Test case** để lỗi đó không bao giờ lặp lại.

---

## PHẦN 7: NGHIỆP VỤ ERP & QUY TRÌNH DOANH NGHIỆP (BUSINESS WORKFLOWS)

Vị trí này đòi hỏi kiến thức về ERP/CRM (Sale, Real Estate). Dưới đây là các Case-study nghiệp vụ bạn nên biết.

### 1. Luồng Bán hàng (Sales Workflow)
*   **Quy trình chuẩn:** 
    1.  **Lead (Cơ hội):** Khách hàng tiềm năng hỏi giá.
    2.  **Quotation (Báo giá):** Nhân viên Sales gửi báo giá (Trạng thái Draft).
    3.  **Sale Order (Xác nhận):** Khách đồng ý, trừ kho ảo (Trạng thái Confirmed).
    4.  **Delivery (Giao hàng):** Kho đóng gói, xuất kho thực tế.
    5.  **Invoicing (Hóa đơn):** Kế toán xuất hóa đơn và ghi nhận công nợ.
*   **Điểm Senior cần lưu ý:** Làm sao để **Ràng buộc dữ liệu?** Ví dụ: Không được xác nhận đơn hàng nếu khách còn nợ quá hạn, hoặc không được xuất kho nếu số lượng tồn kho không đủ (Double checking).

### 2. Nghiệp vụ Bất động sản (Real Estate)
*   **Quản lý bảng hàng:** Trạng thái căn hộ (Available -> Reserved -> Sold).
*   **Tiến độ thanh toán:** Chia nhỏ tiền trả theo đợt (30%, 20%, ...). Senior cần thiết kế CSDL sao cho linh hoạt: Cho phép thay đổi tiến độ thanh toán cho từng khách hàng riêng biệt mà không làm hỏng cấu trúc chuẩn.

### 3. Tích hợp thanh toán & Bank Sync
*   Xử lý bài toán **Đối soát tự động**: Làm sao khi ngân hàng báo có (Webhook), hệ thống tự tìm được đúng Hóa đơn (Invoice) để gạch nợ? 
*   Giải pháp: Sử dụng mã "Mô tả chuyển khoản" duy nhất (Unique Reference) và thuật toán khớp chuỗi để tự động hóa 90% công việc cho kế toán.

---

## PHẦN 8: KIẾN TRÚC HỆ THỐNG PHÂN TÁN (SYSTEM DESIGN & DISTRIBUTED SYSTEMS)

Khi hệ thống lớn lên, Senior Dev phải đối mặt với các bài toán về khả năng mở rộng (Scalability) và tính sẵn sàng cao (High Availability).

### 1. Chiến lược mở rộng Database (Scaling)
*   **Vertical Scaling (Mở rộng dọc):** Nâng cấp CPU, RAM cho Server. Ưu điểm: Đơn giản. Nhược điểm: Có giới hạn vật lý và cực kỳ đắt đỏ.
*   **Horizontal Scaling (Mở rộng ngang - Sharding):** Chia nhỏ Database thành nhiều mảng (Shards). 
    *   *Ví dụ:* User ID 1-1tr ở Server A, 1tr-2tr ở Server B.
    *   *Thử thách:* Truy vấn liên quan đến nhiều Shard sẽ rất chậm và khó duy trì tính toàn vẹn dữ liệu.

### 2. Các Pattern Microservices quan trọng
*   **Circuit Breaker (Cầu dao điện):** Nếu Service A gọi Service B mà B đang lỗi, Circuit Breaker sẽ "ngắt" ngay lập tức để A không phải đợi lâu (timeout), giúp hệ thống không bị "sập dây chuyền". Thường dùng thư viện như `Hystrix` hoặc tự viết logic check lỗi liên tục.
*   **Saga Pattern (Giao dịch phân tán):** Khi một thao tác cần gọi qua 3-4 service (Vd: Đặt hàng -> Trừ kho -> Trừ tiền). 
    *   Nếu bước Trừ tiền lỗi, Saga sẽ chạy các **"Hàm bù đắp" (Compensating Transactions)** để hoàn lại kho (Rollback logic).
*   **API Gateway:** Một "cánh cổng" duy nhất tiếp nhận mọi request từ Client, sau đó điều phối (Routing), xác thực (Auth) và giới hạn tốc độ (Rate Limiting) trước khi đẩy vào các Microservices bên trong.

### 3. Event-Driven Architecture (Kiến trúc hướng sự kiện)
*   **Message Queues (RabbitMQ, Kafka):** Service A đẩy tin nhắn vào Queue, Service B rảnh thì lấy ra xử lý. Giúp hệ thống "bất đồng bộ", giảm tải cho các request live.
*   **CQRS (Command Query Responsibility Segregation):** Tách biệt đường **Ghi** (Insert/Update) và đường **Đọc** (Search/Select). 
    *   Đường Ghi dùng DB quan hệ (Postgres) để đảm bảo dữ liệu chuẩn. 
    *   Đường Đọc dùng Elasticsearch hoặc Redis để tìm kiếm cực nhanh. Đồng bộ dữ liệu qua Event.

### 4. Xử lý Feed/Timeline (Bài toán Twitter/Facebook)
*   **Fan-out on Write (Push model):** Khi bạn đăng bài, hệ thống đẩy bài đó vào "tường" của tất cả bạn bè ngay lập tức. (Nhanh cho người xem, nhưng chậm cho người đăng nếu có triệu followers).
*   **Fan-out on Read (Pull model):** Khi bạn mở App, hệ thống mới đi gom bài của bạn bè lại. (Nhanh cho người đăng, nhưng chậm cho người xem).
*   **Senior Solution:** Dùng **Hybrid**. Celebrity (người nổi tiếng) dùng Pull, người dùng thường dùng Push.

### 5. Bảo mật nâng cao (OWASP)
*   **SQL Injection:** Tuyệt đối dùng *Parameterized Queries* (Odoo/Django đã làm sẵn, nhưng nếu viết SQL thô `cr.execute` thì phải dùng `%s` thay vì f-string).
*   **XSS (Cross-Site Scripting):** Hacker chèn script mã độc vào input. Giải pháp: Sanitize (lọc sạch) HTML ở backend và dùng framework có auto-escape như Vue/Django.
*   **Broken Access Control:** Luôn kiểm tra quyền ở cấp **Record (Dòng)** chứ không chỉ cấp Menu. Trong Odoo là dùng `Record Rules`.

---
*Ghi chú: Nắm vững các khái niệm System Design này sẽ giúp bạn vượt qua vòng phỏng vấn kỹ thuật với CTO hoặc Solution Architect một cách thuyết phục.*

---

## PHẦN 9: PYTHON INTERNALS & METAPROGRAMMING (ĐÀO SÂU LÕI NGÔN NGỮ)

Để đạt mức Senior/Lead, bạn không chỉ dùng Python mà phải hiểu cách nó vận hành "dưới nắp capo".

### 1. Singleton Pattern với `__new__`
*   Thông thường ta dùng `__init__` để khởi tạo giá trị. Nhưng `__new__` mới là hàm thực sự tạo ra Instance (ô nhớ).
*   **Ứng dụng:** Tạo **Singleton** (đảm bảo cả hệ thống chỉ có đúng 1 object duy nhất cho các tác vụ như Kết nối Database, Log, Cấu hình).
    ```python
    class DatabaseConnection:
        _instance = None
        def __new__(cls):
            if not cls._instance:
                cls._instance = super().__new__(cls)
            return cls._instance
    ```

### 2. Metaprogramming với `__getattr__` & `__setattr__`
*   Đây là kỹ thuật "code sinh ra code". Odoo dùng cái này cực nhiều để tạo ra các trường (fields) động.
*   **`__getattr__`**: Chỉ được gọi khi một attribute **không tồn tại**. Giúp bạn tạo ra các thuộc tính "ảo" lúc runtime.
*   **`__getattribute__`**: Được gọi cho **mọi** truy cập thuộc tính (cực kỳ mạnh mẽ nhưng nguy hiểm, dễ gây loop vô tận).

### 3. Callable Objects (`__call__`)
*   Giúp một Object có thể được gọi như một hàm `obj()`. 
*   **Ứng dụng:** Tạo các Decorator dạng Class để lưu trạng thái giữa các lần gọi (Stateful Decorators).

---

## PHẦN 10: TỐI ƯU HÓA POSTGRESQL & TRUY VẤN NÂNG CAO (DATABASE MASTER)

PostgreSQL là trái tim của Odoo/Django. Hiểu sâu nó giúp bạn cứu hệ thống khi data lên tới hàng triệu dòng.

### 1. B-Tree Index vs GIN Index
*   **B-Tree:** Mặc định cho `=`, `<`, `>`, `BETWEEN`. Phù hợp cho số, ngày tháng, chuỗi ngắn.
*   **GIN Index (Generalized Inverted Index):** Chuyên dụng cho kiểu dữ liệu **JSONB** hoặc mảng (`Array`). Nếu Odoo của bạn dùng nhiều trường `Json`, thiếu GIN index sẽ khiến query chậm đi 100 lần.

### 2. Window Functions - Tuyệt chiêu báo cáo
*   Dùng để tính toán trên một tập con dữ liệu mà không cần `GROUP BY`.
    *   *Ví dụ:* Tính tổng doanh số tích lũy của từng nhân viên qua từng tháng (Rolling Sum).
    ```sql
    SELECT name, month, amount, 
           SUM(amount) OVER (PARTITION BY name ORDER BY month) as running_total
    FROM sales_report;
    ```

### 3. Database Locks - Chống "Tranh chấp" (Race Condition)
*   **Row-level Lock (`SELECT FOR UPDATE`):** Khi bạn đang xử lý một đơn hàng, hãy khóa dòng đó lại để User khác không thể vào sửa cùng lúc gây sai lệch tồn kho. Odoo làm việc này qua `self.with_context(active_test=False).search(..., limit=1).write(...)` hoặc SQL thô.

### 4. Partitioning (Phân mảnh bảng)
*   Khi bảng `log` hoặc `audit` lên tới 100 triệu dòng, query sẽ rất nặng.
*   Giải pháp: Chia bảng theo thời gian (Ví dụ: Mỗi tháng 1 bảng riêng). Khi query, Postgres chỉ cần quét bảng của tháng đó thay vì 100 triệu dòng.

---
*Tài liệu này hiện đã bao phủ toàn bộ các tầng: Từ Ngôn ngữ (Python/JS) -> Framework (Odoo/Vue/Nuxt) -> Kiến trúc (System Design) -> Cơ sở dữ liệu (Postgres) -> Kỹ năng mềm. Chúc bạn tỏa sáng trong buổi phỏng vấn!*


