# 📚 TỔNG HỢP LÝ THUYẾT FULLSTACK (INTERN ➔ SENIOR)

Tài liệu này hệ thống lại toàn bộ kiến thức nền tảng và nâng cao cho Frontend và Backend.

---

## 🐍 PHẦN 1: BACKEND (PYTHON, ODOO, DATABASE, SYSTEM)

### 🟢 GIAI ĐOẠN 1: INTERN / JUNIOR (BACKEND CORE)
- **Python Syntax:** Biến, kiểu dữ liệu (`Mutable` vs `Immutable`), List/Dict comprehension.
- **Functions:** Định nghĩa hàm, `*args`, `**kwargs`, Scope của biến (LGBTI rule).
- **OOP Cơ bản:** Class, Object, Method, `__init__`, `self`.
- **Database Basics:** SQL chuẩn (`SELECT`, `WHERE`, `JOIN`), quy chuẩn hóa 1NF, 2NF, 3NF.
- **Git Basics:** `Branching`, `Pull Request`, `Conflict Resolution`.

### 🟡 GIAI ĐOẠN 2: MIDDLE (ADVANCED BACKEND & ORM)
- **Advanced Python:** Decorators, Closures, Generators (`yield`), Iterators.
- **RESTful API:** Thiết kế API chuẩn (Endpoint naming, HTTP methods, Status codes).
- **Security:** SQL Injection, XSS, CSRF (Cách phòng chống trong Python/Django).
- **Odoo ORM:** `search`, `browse`, `write`, `create`, `unlink`. Hiểu về `env.context` và `env.user`.
- **Inheritance Odoo:** Phân biệt `_inherit` (Extension) và `_name` (Prototype).
- **Postgres Optimization:** Sử dụng `Indexes` (B-Tree, GIN, GiST), phân tích `Query Plan` (EXPLAIN).

### 🔴 GIAI ĐOẠN 3: SENIOR (ARCHITECTURE & PERFORMANCE)
- **Concurrency:** Asyncio (Event Loop), Global Interpreter Lock (GIL), Threading vs Multiprocessing.
- **Metaprogramming:** Cách dùng `Metaclasses` để can thiệp quá trình tạo Class (Cách lõi Odoo hoạt động).
- **System Design:** 
    - Scalability (Horizontal vs Vertical).
    - Database Replication (Master-Slave), Sharding, Caching (Redis).
    - Load Balancing (Nginx, HAProxy).
- **Odoo Internals:** `Registry`, `Signals`, `Transaction Lifecycle` (Cache -> SQL -> Postgres).
- **Infrastructure:** Docker, Kubernetes (K8s) basics, CI/CD pipeline (Jenkins, Github Actions).

---

## 🎨 PHẦN 2: FRONTEND (HTML/CSS, JS, VUE 3, ARCHITECTURE)

### 🟢 GIAI ĐOẠN 1: INTERN / JUNIOR (FRONTEND FUNDAMENTALS)
- **HTML5:** Semantic tags (Header, Footer, Section, Article).
- **CSS3:** Box Model, Flexbox, Grid, Responsive Design (Media Queries).
- **Javascript ES6+:** Let/Const, Arrow function, Template literals, Destructuring, Spread/Rest operator.
- **Vue Basics:** Data binding (`v-model`), Directives (`v-if`, `v-for`), Event handling (`v-on`).

### 🟡 GIAI ĐOẠN 2: MIDDLE (MODERN FRONTEND & STATE)
- **Vue 3 Composition API:** `ref`, `reactive`, `computed`, `watch`, `watchEffect`, `script setup`.
- **State Management:** Pinia (Cơ chế Actions, Getters, State).
- **Navigation:** Vue Router (Nested routes, Navigation guards).
- **API Integration:** Axios (Interceptors, Error handling), xử lý `Async/Await` trong Vue.
- **Optimization:** Component communication (Props, Emit), Slots, Teleport.

### 🔴 GIAI ĐOẠN 3: SENIOR (INTERNAL & OPTIMIZATION)
- **Vue Internal:** Proxy-based Reactivity (Effect, Track, Trigger), Virtual DOM, Diffing Algorithm.
- **Advanced UI:** Xây dựng Dashboard phức tạp bằng Custom Widgets, Canvas, SVG.
- **Performance:** 
    - `Lazy loading`, `Code-splitting`, `Tree-shaking`.
    - `Virtual Scrolling` cho dữ liệu vạn dòng.
    - SSR (Server-Side Rendering) vs CSR (Client-Side Rendering) vs SSG.
- **Custom UI Library:** OWL (Odoo Web Library) - Sự tương đồng và khác biệt với Vue 3.
- **Testing:** Unit Test (Vitest), End-to-End Test (Playwright, Cypress) cho Frontend.

---

## 🏗️ PHẦN 3: TƯ DUY TỔNG HỢP (SENIOR MINDSET)

1.  **Clean Code & Architecture:** SOLID, DRY, KISS, YAGNI.
2.  **Trade-offs:** Biết khi nào nên hy sinh tốc độ phát triển để đổi lấy chất lượng code, hoặc ngược lại trong dự án MVP.
3.  **Mentoring:** Khả năng giải thích các khái niệm phức tạp cho Junior một cách đơn giản nhất.
4.  **Security-First:** Luôn đặt bảo mật dữ liệu khách hàng lên hàng đầu (Encryption, Authentication, Authorization).

---

# 📖 GIẢI THÍCH CHI TIẾT CÁC KHỐI KIẾN THỨC (DEEP DIVE EXPLANATIONS)

Phần này sẽ giải thích "Tại sao" và "Bản chất" của từng công nghệ để bạn có thể nắm vững mọi ngóc ngách.

## 🐍 PHẦN 1: BACKEND (PYTHON, ODOO, SYSTEM)

### 1. Python Internals (Cơ chế bên dưới):
- **List vs tuple:** List là một mảng động (dynamic array), cho phép thay đổi dữ liệu (Mutable). Tuple là mảng cố định (Immutable), giúp tiết kiệm bộ nhớ và an toàn hơn khi dùng làm Key trong Dict.
- **Python's Event Loop:** Trái tim của `asyncio`. Nó là một vòng lặp liên tục quét các tác vụ (Tasks). Khi một task đang chờ I/O, nó sẽ tạm dừng và nhường quyền cho task khác chạy. Đây là lý do đơn luồng (Single-thread) nhưng vẫn xử lý được hàng nghìn kết nối.

### 2. Odoo Magic (ORM & Inheritance):
- **Metaclass & Registry:** Khi Odoo khởi động, nó quét qua mọi file Python. Metaclass sẽ tạo ra các Model. `Registry` là bản đồ lưu trữ các Model này. Khi bạn `_inherit`, Odoo sẽ tìm trong Registry và "trộn" các thuộc tính mới vào Class hiện tại.
- **The Environment (env):** Mỗi khi bạn gọi `self.env`, Odoo đang cung cấp một "ngữ cảnh" bao gồm: User (`env.uid`), Quyền (`env.context`), và Cache hiện tại. 

### 3. Database & Distributed Systems:
- **ACID in ERP:** Trong Kế toán, tính `Atomicity` (Nguyên tử) cực kỳ quan trọng. Hoặc là lưu cả Invoice và Payment, hoặc là không lưu cái nào (Rollback). Không bao giờ có trạng thái "nửa vời".
- **Master-Slave Replication:** Master dùng để Ghi (Write), Slave để Đọc (Read). Điều này giúp hệ thống ERP có hàng trăm báo cáo nặng chạy mà không làm nghẽn tiến trình nhập đơn hàng của Sales.

---

## 🎨 PHẦN 2: FRONTEND (JS, VUE 3, PERFORMANCE)

### 1. Javascript & Browser Internals:
- **Call Stack & Event Loop:** Javascript chạy đơn luồng. `Call Stack` xử lý các hàm đồng bộ. `Task Queue` (hoặc Microtask Queue) xử lý các hàm bất đồng bộ (`Promise`, `setTimeout`). Event loop liên tục đẩy các task từ Queue vào Stack khi Stack trống.
- **CSS Box Model:** Mọi thứ trên web là một cái hộp. Hiểu `box-sizing: border-box` giúp bạn kiểm soát kích thước chuẩn xác thay vì phải cộng dọn Padding/Border vào Width/Height.

### 2. Vue 3 Reactivity (Proxy):
- **Track & Trigger:** Vue dùng `Proxy` để "bắt" (Track) lúc ta truy cập biến và "kích hoạt" (Trigger) lúc ta thay đổi biến đó. Khác với Vue 2, nó không cần phải lặp qua từng thuộc tính của Object lúc khởi tạo, giúp giảm dung lượng RAM và tăng tốc độ.
- **Composition API Mindset:** Không chỉ là code sạch hơn, nó cho phép **Logic Localization** (đưa logic vào gần nơi nó được dùng nhất).

### 3. Frontend Performance at Scale:
- **Virtual DOM Diffing:** Vue không so sánh từng pixel. Nó so sánh các "Node" theo dạng cây. Sử dụng `:key` duy nhất giúp Vue biết chính xác Node nào bị di chuyển, Node nào bị xóa, từ đó chỉ cập nhật đúng 1 Node đó lên màn hình.
- **Hydration (trong SSR):** Là quá trình trình duyệt nhận HTML tĩnh từ Server, sau đó Javascript "đổ" sự tương tác (Click, Hover) vào HTML đó để biến nó thành một ứng dụng web động.

---

# 🧠 TƯ DUY KIẾN TRÚC & GIẢI QUYẾT VẤN ĐỀ

1.  **Principle of Least Privilege (Quyền hạn tối thiểu):** Luôn bắt đầu với quyền truy cập thấp nhất và chỉ mở rộng khi cần thiết (Áp dụng cho Odoo Record Rules).
2.  **KISS (Keep It Simple, Stupid):** Đừng cố chọn kiến trúc Microservices khi dự án Monolith (Odoo Monolith) vẫn hoạt động tốt và dễ bảo trì.
3.  **Performance vs Readability:** Ở mức Senior, ưu tiên **Readability** (Code dễ đọc) trước, chỉ tối ưu hiệu năng (Performance) khi có dữ liệu chứng minh nó thực sự chậm.

---

# 💡 LOGIC THỰC THI & TƯ DUY KIẾN TRÚC (EXECUTION LOGIC)

Phần này giúp bạn hiểu "Luồng tư duy" để giải quyết các bài toán phức tạp trên thực tế.

## 🐍 1. LOGIC BACKEND: TỪ NGHIỆP VỤ ĐẾN DỮ LIỆU

### **A. Logic Kế thừa (Inheritance Logic) trong Odoo:**
- **Vấn đề:** Làm sao để thêm tính năng cho một module có sẵn mà không chạm vào code gốc?
- **Logic giải quyết:** Odoo sử dụng `Monkey Patching` thông qua `Metaclasses`. Khi bạn khai báo `_inherit`, Odoo sẽ tìm Class cũ trong Registry, sau đó "trộn" các phương thức mới vào. Nếu có trùng tên hàm, nó sẽ dùng hàm mới nhất (trừ khi bạn gọi `super()`).
- **Tư duy:** Luôn gọi `super()` trừ khi bạn muốn thay thế hoàn toàn logic cũ. Điều này giúp hệ thống giữ được tính tương thích (Compatibility).

### **B. Logic Luồng dữ liệu (Data Flow Logic):**
- **Quy trình:** Frontend gửi Request -> Backend Middleware (check Auth) -> Controller -> Service Layer (Xử lý logic nghiệp vụ) -> ORM/Repository (Truy xuất DB) -> Trả về JSON.
- **Tư duy:** Tách biệt logic nghiệp vụ khỏi Controller. Controller chỉ nên làm nhiệm vụ "điều hướng", Logic thực sự phải nằm ở Service hoặc Model. Điều này giúp dễ Unit Test.

### **C. Logic Xử lý Bất đồng bộ (Async logic):**
- **Vấn đề:** Gửi email hoặc tạo báo cáo nặng làm treo trình duyệt người dùng.
- **Logic giải quyết:** Backend nhận yêu cầu -> Đẩy một "Job" vào hàng đợi (Queue - như Redis/Celery) -> Trả về mã 202 (Accepted) ngay lập tức cho người dùng -> Công nhân (Worker) sẽ lấy job ra xử lý dưới nền.

---

## 🎨 2. LOGIC FRONTEND: TỪ THAO TÁC ĐẾN GIAO DIỆN

### **A. Logic Phản xạ (Reactivity Logic) của Vue 3:**
- **Quy trình:** Gán giá trị mới cho biến `ref` -> Proxy "bẫy" hành động này (Setter) -> Proxy báo cho "Dependency Tracker" (Người theo dõi) -> Dependency Tracker tìm xem những Component nào đang dùng biến này -> Component đó sẽ "re-render".
- **Tư duy:** Không phải hiệu ứng nào cũng cần Reactivity. Dùng `shallowRef` cho các dữ liệu lớn chỉ cần hiển thị để giảm tải cho hệ thống theo dõi của Vue.

### **B. Logic Quản lý Trạng thái (State Management Logic):**
- **Vấn đề:** Khi nào dùng Props/Emit, khi nào dùng Provide/Inject, khi nào dùng Pinia?
- **Logic giải quyết:** 
    - Cha-Con gần: Dùng Props/Emit (Đơn giản nhất).
    - Cây Component sâu (nhưng cùng một module): Dùng Provide/Inject.
    - Toàn dự án (User Auth, Giỏ hàng): Dùng Pinia.
- **Tư duy:** Luôn giữ cho State càng gần nơi sử dụng càng tốt (Local State first). Chỉ "nâng" lên Global State khi thật sự cần chia sẻ dữ liệu giữa các trang khác nhau.

### **C. Logic Cấu trúc Module (Modular Logic):**
- **Tư duy:** Thay vì xếp theo loại file (Folder: Controllers, Folder: Views), hãy xếp theo **Tính năng (Feature-based)**. Ví dụ: Folder: `Sales`, Folder: `Inventory`. Trong mỗi folder đó mới chứa Controllers/Views riêng. Điều này giúp Scale dự án lên hàng trăm nghìn dòng code mà không bị lạc lối.

---

# 🏭 CHI TIẾT CƠ CHẾ VẬN HÀNH NỘI TẠI (UNDER THE HOOD)

Phần này giúp bạn trả lời các câu hỏi "Làm sao nó làm được như vậy?"

## 🐍 1. PYTHON: CƠ CHẾ CLOSURES & DECORATORS
- **Logic:** Khi bạn định nghĩa một hàm lồng trong một hàm khác, hàm bên trong có quyền truy cập vào các biến của hàm bên ngoài kể cả khi hàm bên ngoài đã chạy xong. Đây chính là **Closure**.
- **Execution:** `Decorator` thực chất là một Closure nhận hàm gốc làm tham số. Khi bạn gọi `@my_decorator`, Python thực thi `func = my_decorator(func)`.

## 🎨 2. VUE 3: CƠ CHẾ EFFECT & TRACK TRONG PROXY
- **Logic:** Vue 3 sử dụng `Reactive Effect`. 
    - **Track:** Khi bạn render một biến trong template, Vue sẽ "theo dấu" (track) để biết rằng UI này phụ thuộc vào biến đó. 
    - **Trigger:** Khi bạn thay đổi giá trị biến, Vue sẽ "kích hoạt" (trigger) tất cả các hiệu ứng đã được theo dấu để cập nhật UI ngay lập tức.
- **Tư duy:** Hiểu điều này giúp bạn tránh được lỗi "Mất Reactivity" khi gán lại toàn bộ đối tượng hoặc khi tương tác với các thư viện không phải của Vue.

## 🏗️ 3. ODOO: CHI TIẾT LUỒNG DỮ LIỆU TỪ UI ĐẾN DB
- **Luồn chạy:** User nhấn Save -> Odoo Web (Javascript/OWL) gửi JSON-RPC lên Server -> Server nhận data và khởi tạo `Environment` (env) -> Gọi phương thức `create` hoặc `write` của Model -> **ORM Cache** cập nhật -> **SQL Manager** sinh câu lệnh INSERT/UPDATE -> **PostgreSQL** thực thi -> **Registry** thông báo cho các module khác (Bus/Signals) có thay đổi.
- **Tư duy Senior:** Luôn ý thức rằng việc gọi `self.env` quá nhiều lần sẽ gây tốn tài nguyên vì mỗi lần gọi nó sẽ kiểm tra Context và Quyền hạn.

---
> [!IMPORTANT]
> **Ghi nhớ cuối:** Lý thuyết giúp bạn trả lời câu hỏi, nhưng **Trải nghiệm thực tế** giúp bạn thuyết phục nhà tuyển dụng. Hãy luôn kèm theo ví dụ: "Vấn đề này tôi đã gặp ở dự án X và tôi đã áp dụng lý thuyết Y để xử lý nó..."

Chúc bạn có một buổi phỏng vấn bùng nổ vào Thứ 2 tới! 🤘🚀
