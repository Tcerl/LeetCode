# KHÁI NIỆM ÔN LUYỆN PHỎNG VẤN CHI TIẾT - FULLSTACK DEVELOPER (PYTHON + VUE.JS + ODOO)

Dựa trên yêu cầu công việc (3+ năm kinh nghiệm), tài liệu này được nâng cấp với mức độ chi tiết và chuyên sâu, tập trung vào kỹ năng vận hành thực tế, giải quyết vấn đề hệ thống và kiến thức cốt lõi.

---

## PHẦN 1: KNOWLEDGE MAP & LỘ TRÌNH PHÁT TRIỂN (FRESHER -> SENIOR)

Lộ trình này giúp bạn xác định xem mình đang ở đâu và cần học thêm gì để tiến tới trình độ Senior (3+ năm).

### 1. Python & Backend Core

| Cấp độ         | Kiến thức trọng tâm                                                                                         | Mục tiêu cần đạt                                                                    |
| :---------------- | :-------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- |
| **Fresher** | Syntax cơ bản, Data Types (List, Dict, Tuple), Functions, OOP cơ bản (Class, Inheritance).                  | Viết được code chạy đúng logic, hiểu tính đóng gói và kế thừa.            |
| **Junior**  | Decorators, Generators, List Comprehension, Pip/Virtualenv, Exception Handling, Logging.                        | Code sạch (Clean Code), biết dùng thư viện ngoài, debug tốt.                      |
| **Senior**  | Metaclasses, GIL, Memory Management, AsyncIO, Multi-processing, Design Patterns (Singleton, Factory, Observer). | Tối ưu hiệu năng, xử lý tác vụ song song, thiết kế cấu trúc code linh hoạt. |

### 2. Frontend (Vue.js 3 & JS/TS)

| Cấp độ         | Kiến thức trọng tâm                                                                                        | Mục tiêu cần đạt                                                                            |
| :---------------- | :------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **Fresher** | HTML/CSS/JS cơ bản, Vue Directives (`v-if`, `v-for`, `v-model`), Props & Events, Lifecycle Hooks.      | Xây dựng giao diện tĩnh, xử lý tương tác cơ bản giữa các component.                 |
| **Junior**  | Vue Router, Pinia (State Management), Composition API (`ref`, `reactive`), Axios, Vite.                    | Xây dựng Single Page App (SPA) hoàn chỉnh, quản lý dữ liệu tập trung.                   |
| **Senior**  | Custom Directives, Render functions, Teleport, Suspense, Performance (Lazy Loading, Memoization), SSR/Nuxt.js. | Tối ưu trải nghiệm người dùng, xây dựng hệ thống UI phức tạp, quy trình SEO/Speed. |

### 3. Odoo ERP (Framework đặc thù)

| Cấp độ         | Kiến thức trọng tâm                                                                                                        | Mục tiêu cần đạt                                                                                      |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| **Fresher** | Cấu trúc module Odoo, Kế thừa View (XPath), Field types cơ bản, XML RPC cơ bản.                                        | Tạo được module mới, thêm trường dữ liệu và sửa giao diện đơn giản.                        |
| **Junior**  | ORM Methods (`search`, `read`, `write`, `create`), Domain, Context, Onchange, Compute fields, Security (Groups/CSV).   | Xử lý logic nghiệp vụ phức tạp, phân quyền cơ bản, làm chủ Environment.                        |
| **Senior**  | Advanced ORM (`_auto=False`, `TransientModel`), Batch processing, SQL View, Performance profiling, Customizing Web Client. | Tối ưu hệ thống xử lý DB lớn, can thiệp sâu vào nhân Odoo, giải quyết bài toán hiệu năng. |

### 4. Database (PostgreSQL) & DevOps

| Cấp độ         | Kiến thức trọng tâm                                                                                 | Mục tiêu cần đạt                                                                 |
| :---------------- | :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------ |
| **Fresher** | Cấu trúc bảng, SQL cơ bản (Select, Join, Where), Data types.                                       | Truy vấn lấy dữ liệu đơn giản, thiết kế bảng đúng chuẩn.                 |
| **Junior**  | Indexing, ACID, Transactions, Foreign Keys, JSONB, Migrations.                                          | Tối ưu tốc độ query bằng Index, đảm bảo tính toàn vẹn dữ liệu.          |
| **Senior**  | Query Optimization (Explain Analyze), Window Functions, Partitioning, Connection Pooling, Docker/CI-CD. | Quản trị DB quy mô triệu dòng, triển khai hệ thống tự động qua Docker/K8s. |

---

### CHI TIẾT NỘI DUNG KIẾN THỨC THEO LỘ TRÌNH

Phần này giúp bạn nắm vững bản chất (**Định nghĩa**) và vai trò thực tế (**Công dụng**) của từng từ khóa, giúp bạn tự tin giải quyết yêu cầu của nhà phỏng vấn.

#### 1. Mảng Python & Backend Core (Deep-Dive)

* **Cấp độ Fresher (Nền tảng):**
  - **Syntax cơ bản (Indentation):**
    - **Định nghĩa:** Quy tắc sử dụng khoảng trắng (thụt lề) để phân chia các khối mã thay vì dùng dấu `{}`.
    - **Công dụng:** Xác định phạm vi hoạt động của hàm, lớp, và cấu trúc điều khiển. Giúp code Python luôn sạch sẽ.
  - **Data Types (List/Tuple/Dict):**
    - **Định nghĩa:** Cách tổ chức dữ liệu trong bộ nhớ (Mảng động, Mảng bất biến, Bảng băm).
    - **Công dụng:** Tối ưu hóa bộ nhớ và tốc độ truy xuất (VD: dùng Dict để tìm kiếm dữ liệu theo khóa chỉ mất O(1)).
  - **OOP cơ bản (Class/Inheritance):**
    - **Định nghĩa:** Lập trình dựa trên các lớp và đối tượng thực tế.
    - **Công dụng:** Tái sử dụng code và đóng gói logic nghiệp vụ, làm nền tảng cho mọi framework chuyên nghiệp.
* **Cấp độ Junior (Thành thạo):**
  - **Decorators:**
    - **Định nghĩa:** Một hàm bao bọc một hàm khác để thực hiện logic bổ sung mà không làm thay đổi code gốc.
    - **Công dụng:** Áp dụng xử lý chung như Kiểm tra quyền (Auth), Logging, hoặc tính thời gian thực thi (Performance).
  - **Generators (`yield`):**
    - **Định nghĩa:** Một loại hàm đặc biệt trả về dữ liệu từng phần thay vì trả về toàn bộ danh sách một lúc.
    - **Công dụng:** Giúp xử lý các tệp dữ liệu khổng lồ (vài GB) mà không gây tràn bộ nhớ RAM.
  - **Logging:**
    - **Định nghĩa:** Hệ thống ghi lại lịch sử hoạt động và lỗi của ứng dụng.
    - **Công dụng:** Cực kỳ quan trọng để debug và theo dõi sức khỏe hệ thống trên môi trường Production.
* **Cấp độ Senior (Chuyên sâu):**
  - **Memory Management (GC):**
    - **Định nghĩa:** Cơ chế của Python giúp tự động quản lý việc cấp phát và thu hồi bộ nhớ (Reference Counting + Generational Garbage Collection).
    - **Công dụng:** Loại bỏ gánh nặng quản lý RAM thủ công, bảo vệ ứng dụng khỏi hiện tượng rò rỉ bộ nhớ (Memory Leaks).
    - **Chuyên sâu:** Nắm được sự khác biệt giữa **Reference Counting** (thu hồi ngay - nhanh) và **GC** (xử lý tham chiếu vòng - chạy định kỳ). Biết dùng `__slots__` để giảm dấu chân bộ nhớ (Memory footprint) cho các class chứa hàng triệu đối tượng (Odoo dùng rất nhiều).
    
  - **GIL (Global Interpreter Lock):**
    - **Định nghĩa:** Cơ chế của Python ngăn cản nhiều luồng (thread) chạy cùng lúc trên CPU đa lõi.
    - **Công dụng:** Bảo vệ tính toàn vẹn của dữ liệu trong bộ nhớ, nhưng gây nghẽn cho các tác vụ tính toán (CPU-bound).
    - **Chuyên sâu:** 
      1. Hiểu cách vượt qua GIL bằng **`Multiprocessing`**. 
      2. Tại sao các thư viện như NumPy, PyTorch không bị ảnh hưởng bởi GIL (do viết bằng C).
  - **AsyncIO:**
    - **Định nghĩa:** Mô hình lập trình bất đồng bộ đơn luồng dựa trên Event Loop.
    - **Công dụng:** Tăng tốc độ phản hồi gấp nhiều lần cho các tác vụ I/O (Database, API, Web crawling).
    - **Chuyên sâu:** 
      1. Hiểu bản chất của **`coroutine`**, **`await`**, và **`Non-blocking I/O`**:
        - **Non-blocking I/O:** Thay vì ngồi chờ dữ liệu từ ổ cứng hay mạng về (Blocking), chương trình sẽ gửi yêu cầu đi và rảnh tay làm việc khác ngay lập tức.
        - **Coroutine:** Một loại hàm đặc biệt (định nghĩa bằng `async def`) có khả năng **tạm dừng** (Pause) và **tiếp tục** (Resume) tại điểm đã dừng mà không làm mất trạng thái (Biến, ngữ cảnh).
        - **await:** Điểm "đặt lệnh" yêu cầu dừng coroutine hiện tại để nhường quyền điều khiển cho Event Loop, chỉ tiếp tục chạy dòng tiếp theo khi kết quả I/O đã sẵn sàng.
      2. Phân biệt khi nào dùng **Multi-threading** (nhiều luồng - tốn RAM) vs **AsyncIO** (đơn luồng - cực kỳ nhẹ, tối ưu cho hàng vạn kết nối đồng thời).

#### 2. Mảng Frontend (Vue.js 3 & JS/TS) (Deep-Dive)

* **Cấp độ Fresher (Nền tảng):**
  - **Vue Directives (`v-if`, `v-for`, `v-model`):**
    - **Định nghĩa:** Các từ khóa đặc biệt gắn vào thẻ HTML để Vue điều khiển trực tiếp cấu trúc (DOM) và luồng dữ liệu.
    - **Công dụng:** Giúp lập trình viên điều khiển giao diện phản hồi linh động theo trạng thái của dữ liệu.
    - **Chuyên sâu:** 
      1. Phân biệt **`v-if`** (tháo lắp DOM - tốn phí re-render) vs **`v-show`** (chỉ ẩn bằng CSS - rẻ hơn). 
      2. Tại sao **`v-for`** luôn cần **`:key`** (để Vue định danh và tối ưu thuật toán Diffing của Virtual DOM). 
      3. Quy định mới của Vue 3: **`v-if`** có độ ưu tiên CAO HƠN **`v-for`** (tránh dùng chung trên 1 thẻ). 
      4. Bản chất **`v-model`** là cú pháp "sugar" của tổ hợp `v-bind` (truyền prop) và `v-on` (phát event cập nhật).
  - **Lifecycle Hooks:**
    - **Định nghĩa:** Các "điểm dừng" trong vòng đời của một component (từ lúc tạo ra đến khi bị hủy).
    - **Công dụng:** Cho phép chạy code đúng thời điểm (VD: Fetch data ngay khi vẽ xong màn hình).
    - **Chuyên sâu:** 
      1. Hiểu sự thay đổi từ **Vue 2 (created, mounted)** sang **Vue 3 (setup, onMounted)**. 
      2. Tại sao nên dùng **`onUnmounted`** để dọn dẹp biến toàn cục hoặc stop Timer (tránh Memory Leak).
* **Cấp độ Junior (Thành thạo):**
  - **Composition API & Reactivity:**
    - **Định nghĩa:** Cách tổ chức code theo tính năng (Function-based) và hệ thống theo dõi dữ liệu của Vue.
    - **Công dụng:** Tái sử dụng code cực mạnh qua **Composables** và giúp code dễ bảo trì hơn `Options API`.
    - **Chuyên sâu:** 
      1. Phân biệt **`ref`** (cho dữ liệu đơn lẻ) vs **`reactive`** (cho object). 
      2. Cơ chế **`watch`** (theo dõi thay đổi) vs **`computed`** (tự tính toán và lưu cache kết quả).
  - **Pinia:**
    - **Định nghĩa:** Kho quản lý trạng thái (State Management) chính thức cho Vue 3.
    - **Công dụng:** Giúp chia sẻ dữ liệu giữa các component ở xa nhau mà không cần truyền props.
    - **Chuyên sâu:** 
      1. Hiểu cấu trúc **State - Getters - Actions**:
        - **State:** Nơi lưu trữ dữ liệu gốc (Single Source of Truth), tương tự như `data()` trong component.
        - **Getters:** Các giá trị được tính toán từ State (Computed Properties), tự động cập nhật và cache kết quả khi State thay đổi.
        - **Actions:** Các hàm chứa logic xử lý (Methods), có thể là đồng bộ hoặc bất đồng bộ (API calls). Trong Pinia, Actions dùng để thay đổi (Mutate) trực tiếp State mà không cần qua Mutations như Vuex.
      2. Tại sao Pinia lại thay thế Vuex hoàn toàn (hỗ trợ TypeScript tốt hơn, không có mutation lằng nhằng, hỗ trợ đệ quy tốt hơn).
  - **Vue Router:**
    - **Định nghĩa:** Bộ định tuyến giúp chuyển trang mượt mà trong ứng dụng SPA.
    - **Công dụng:** Quản lý đường dẫn URL và bảo vệ các trang yêu cầu đăng nhập.
    - **Chuyên sâu:** 
      1. Kỹ thuật **Lazy Loading Routes** (chuyển đến đâu load code đến đó để tăng tốc độ trang). 
      2. Sử dụng **Navigation Guards** để kiểm tra quyền truy cập (Auth) trước khi vào trang.
* **Cấp độ Senior (Chuyên sâu):**
  - **Virtual DOM Diffing:**
    - **Định nghĩa:** Thuật toán so sánh sự thay đổi giữa cây DOM ảo và DOM thật.
    - **Công dụng:** Chỉ cập nhật những phần thực sự thay đổi trên màn hình, giúp app cực mượt.
    - **Chuyên sâu:** Nắm được cơ chế **Patching** và lý do tại sao thay đổi dữ liệu trong `ref` lại kích hoạt vẽ lại trang.
  - **SSR & Hydration:**
    - **Định nghĩa:** Kỹ thuật render trang web trên máy chủ (Server) rồi gửi về client.
    - **Công dụng:** Tăng tốc độ load trang đầu tiên và hỗ trợ SEO tốt nhất (Bots dễ đọc dữ liệu).
    - **Chuyên sâu:** Quá trình **Hydration** - nơi Vue "hồi sinh" các sự kiện Javascript trên nội dung tĩnh đã render từ server.
  - **Performance Optimizations:**
    - **Định nghĩa:** Các kỹ thuật tối ưu hóa tài nguyên trình duyệt.
    - **Công dụng:** Tiết kiệm RAM cho người dùng và tăng điểm Core Web Vitals (SEO).
    - **Chuyên sâu:** Sử dụng **`v-memo`** (bỏ qua render thừa), **`shallowRef`** (cho data lớn tĩnh), và **Asynchronous Components**.

#### 3. Mảng Odoo ERP (Framework Deep-Dive)

* **Cấp độ Fresher (Nền tảng):**
  - **Module Structure (`__manifest__.py`):**
    - **Định nghĩa:** Cách tổ chức thư mục và khai báo các file nghiệp vụ trong Odoo.
    - **Công dụng:** Giúp Odoo nhận diện module, quản lý sự phụ thuộc (Dependencies) và cài đặt dữ liệu.
    - **Chuyên sâu:** Hiểu vai trò của file `__init__.py` (khởi tạo Python) và các thư mục chuẩn như `models/`, `views/`, `security/`, `data/`.
  - **Kế thừa View (XPath):**
    - **Định nghĩa:** Sử dụng ngôn ngữ XPath để can thiệp vào các Views XML có sẵn.
    - **Công dụng:** Thay đổi giao diện gốc của Odoo (thêm trường, ẩn nút) mà không làm hỏng code của hệ thống.
    - **Chuyên sâu:** Nắm được các chế độ `position="after|before|replace|attributes|inside"`.
* **Cấp độ Junior (Thành thạo):**
  - **Environment (`self.env`):**
    - **Định nghĩa:** Đối tượng lưu đầy đủ thông tin về User, Database, và các Recordsets.
    - **Công dụng:** Là cầu nối để thực hiện mọi thao tác ORM (Search, Create, Write).
    - **Chuyên sâu:** Phân biệt được khi nào dùng **`with_user`**, **`with_context`**, và **`sudo`** (để vượt quyền bảo mật).
  - **Compute & Onchange:**
    - **Định nghĩa:** Các decorators `@api.depends` và `@api.onchange` để tính toán dữ liệu tự động.
    - **Công dụng:** Tăng trải nghiệm người dùng bằng cách tự điền thông tin và đảm bảo logic nghiệp vụ chính xác.
    - **Chuyên sâu:** Phân biệt được **`store=True`** (lưu vào database) vs không lưu, và lý do tại sao nên ưu tiên Compute hơn Onchange trong các phiên bản Odoo mới.
* **Cấp độ Senior (Chuyên sâu):**
  - **Batch Processing:**
    - **Định nghĩa:** Kỹ thuật gom nhiều bản ghi để xử lý trong một lệnh SQL duy nhất.
    - **Công dụng:** Tối ưu hóa hiệu năng, tránh tình trạng "treo" server khi xử lý hàng nghìn đơn hàng.
    - **Chuyên sâu:** Nắm được quy tắc "Don't browse in a loop" - Tuyệt đối không query lẻ tẻ trong vòng lặp `for`.
  - **Owl Framework:**
    - **Định nghĩa:** Framework Frontend hiện đại dựa trên Class/Component của chính Odoo.
    - **Công dụng:** Cho phép bạn viết các Widget và Dashboard linh động như Vue/React.
    - **Chuyên sâu:** Hiểu về **Hooks (useState, onWillStart)** và cơ chế **Reactivity** trong Owl để can thiệp sâu vào Web Client.
  - **Registry & Pool:**
    - **Định nghĩa:** Hệ thống quản lý các Models tập trung trong bộ nhớ RAM của Odoo.
    - **Công dụng:** Giúp Odoo duy trì sự kế thừa chồng chéo giữa hàng trăm module.
    - **Chuyên sâu:** Hiểu cách Odoo khởi tạo (setup) các lớp Models và cơ chế nạp chồng (Override) function.

#### 4. Mảng Database & DevOps (Deep-Dive)

* **Cấp độ Fresher (Nền tảng):**
  - **SQL JOINs & GROUP BY:**
    - **Định nghĩa:** Các kỹ thuật kết nối bảng (Inner, Left, Right) và nhóm dữ liệu.
    - **Công dụng:** Tái cấu trúc dữ liệu theo yêu cầu báo cáo thực tế.
    - **Chuyên sâu:** Nắm vững sự khác biệt giữa **JOIN** và **Subquery**; biết dùng **HAVING** để lọc sau khi Aggregate.
  - **Database Normalization:**
    - **Định nghĩa:** Quy chuẩn thiết kế bảng để tránh dư thừa (1NF, 2NF, 3NF).
    - **Công dụng:** Đảm bảo tính toàn vẹn và dễ dàng bảo trì dữ liệu.
    - **Chuyên sâu:** Khi nào nên **Denormalize** (Phản chuẩn hóa) để đánh đổi dung lượng lấy tốc độ truy vấn trong hệ thống lớn.
* **Cấp độ Junior (Thành thạo):**
  - **Indexing (B-Tree):**
    - **Định nghĩa:** Cấu trúc dữ liệu phụ giúp tìm kiếm nhanh hơn.
    - **Công dụng:** Tăng tốc độ Query từ vài giây xuống mili-giây.
    - **Chuyên sâu:** Hiểu về **Composite Index** và **Lefmost Prefix Rule** (Quy tắc tiền tố trái nhất) - cực kỳ quan trọng để đánh index đúng.
  - **ACID Transaction:**
    - **Định nghĩa:** 4 đặc tính của một giao dịch an toàn (Atomicity, Consistency, Isolation, Durability).
    - **Công dụng:** Đảm bảo tiền trong tài khoản không bị "mất" nếu hệ thống mạng sập khi đang chuyển khoản.
    - **Chuyên sâu:** Các cấp độ **Isolation Levels** (Read Committed, Serializable) và ảnh hưởng của chúng đến hiệu năng đồng thời (Concurrency).
* **Cấp độ Senior (Chuyên sâu):**
  - **Explain Analyze:**
    - **Định nghĩa:** Công cụ phân tích kế hoạch thực thi (Execution Plan) của SQL.
    - **Công dụng:** "Bắt bệnh" những câu SQL chạy chậm trong môi trường Production.
    - **Chuyên sâu:** Đọc hiểu các thông số như **Sequential Scan** (quét toàn bộ bảng - tệ) vs **Index Scan** (tốt).
  - **Saga Pattern:**
    - **Định nghĩa:** Một mẫu kiến trúc để quản lý giao dịch phân tán (Distributed Transactions).
    - **Công dụng:** Đảm bảo tính nhất quán dữ liệu giữa các Microservices (VD: Trừ kho odoo -> Thanh toán ngân hàng).
    - **Chuyên sâu:** Hiểu cơ chế **Compensating Transaction** (Giao dịch bù) để "Undo" lại khi có một bước trong chuỗi bị lỗi.
  - **CI/CD Pipeline:**
    - **Định nghĩa:** Quy trình tự động hóa việc Kiểm thử, Đóng gói và Triển khai code.
    - **Công dụng:** Giảm thiểu lỗi do con người và giúp product ra mắt nhanh hơn.
    - **Chuyên sâu:** Nắm vững quy trình **Blue-Green Deployment** hoặc **Canary Release** để cập nhật app mà không gây gián đoạn hệ thống.

---

## PHẦN 2: BỘ CÂU HỎI PHỎNG VẤN THEO CẤP ĐỘ

### NHÓM 0: CÂU HỎI NỀN TẢNG (LEVEL: FRESHER)

**Q0.1: Phân biệt List và Tuple trong Python? Khi nào nên dùng loại nào?**

* **Trả lời:**
  - `List` là *Mutable* (có thể thay đổi nội dung sau khi tạo). Dùng khi danh sách cần thêm/xóa/sửa phần tử.
  - `Tuple` là *Immutable* (không thể thay đổi). Dùng khi danh sách cố định (như tọa độ màu, cấu hình hệ thống), giúp tối ưu bộ nhớ và bảo mật dữ liệu.

**Q0.2: `v-if` và `v-show` trong Vue khác nhau điểm nào?**

* **Trả lời:**
  - `v-if`: Thêm hoặc xóa hoàn toàn thẻ HTML khỏi DOM. Tiết kiệm tài nguyên nếu ban đầu điều kiện là false, nhưng tốn phí re-render nếu bật tắt liên tục.
  - `v-show`: Luôn giữ thẻ trong DOM nhưng dùng CSS `display: none` để ẩn/hiện. Thích hợp cho các phần tử cần bật tắt thường xuyên (như toggle menu).

**Q0.3: Domain trong Odoo dùng để làm gì? Ví dụ?**

* **Trả lời:**
  - Dùng để lọc dữ liệu hiển thị (trên View) hoặc lọc bản ghi (trong mã Python).
  - Ví dụ: `[('state', '=', 'posted')]` để chỉ lấy các hóa đơn đã vào sổ.

**Q0.4: `Composition API` khác gì `Options API` trong Vue 3?**

* **Trả lời:**
  - `Options API`: Chia code theo các option (`data`, `methods`, `computed`). Dễ học cho người mới nhưng khó tái sử dụng khi component lớn.
  - `Composition API`: Sử dụng hàm `setup()`. Giúp gom nhóm logic theo tính năng (Feature), dễ dàng tái sử dụng qua "Composables" và hỗ trợ TypeScript tốt hơn.

**Q0.5: Middleware trong Web Framework (Django/FastAPI) dùng để làm gì?**

* **Trả lời:**
  - Là một lớp phần mềm nằm giữa Request và Response.
  - Công dụng: Kiểm tra quyền truy cập (Authentication), Ghi log, nén dữ liệu, xử lý lỗi tập trung trước khi request đến được View.

**Q0.6: Phân biệt `_inherit` và `_inherits` trong Odoo?**

* **Trả lời:**
  - `_inherit`: Kế thừa theo kiểu mở rộng (Extension). Thêm trường/hàm mới vào bảng đã có sẵn.
  - `_inherits`: Kế thừa theo kiểu ủy quyền (Delegation). Tạo bảng mới liên kết với bảng cũ qua một ID (Composition).

---

### NHÓM 1: PYTHON & BACKEND (LEVEL: SENIOR)

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

**Q2.1: Python quản lý bộ nhớ như thế nào? Làm sao để tối ưu hóa bộ nhớ cho một ứng dụng xử lý hàng triệu bản ghi?**

* **Trả lời:**
  * **Cơ chế chính:** Python sử dụng kết hợp **Reference Counting** (đếm số lượng tham chiếu tới một đối tượng) và **Generational Garbage Collection** (để giải quyết các Circular References).
  * **Tối ưu hóa (Senior level):**
    1.  Sử dụng `__slots__` trong class để giảm bớt bộ nhớ của `__dict__` (Odoo/ORM dùng rất nhiều).
    2.  Sử dụng **Generators** thay vì **Lists** để tránh việc load toàn bộ dữ liệu vào RAM (Lazy loading).
    3.  Tận dụng cơ chế **Interning** (đối với các chuỗi ngắn hoặc số nhỏ).
    4.  Sử dụng các thư viện như `tracemalloc` hoặc `objgraph` để tìm các đối tượng bị "rò rỉ" (leaks) nhưng vẫn còn tham chiếu ngầm.

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

### Ví dụ 1: Custom Hook (Composable) trong Vue 3

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
      const response = await fetch(unref(url))
      if (!response.ok) throw new Error('API request failed')
      data.value = await response.json()
    } catch (err) {
      error.value = err
    } finally {
      isLoading.value = false
    }
  }

  watchEffect(() => fetchData())

  return { data, error, isLoading }
}
```

### Ví dụ 2: Giải quyết bài toán N+1 bằng Python

```python
# ✅ CÁCH ĐÚNG CỦA SENIOR DEV (Tối ưu về 1 Query)
# Dùng select_related() nó sẽ ép Database chạy luôn câu INNER JOIN giữa 2 bảng.
articles = Article.objects.select_related('author').all()
for art in articles:
    # Câu lặp này chỉ đọc trên vùng RAM Python hiện tại
    print(art.title, art.author.name) 
```

---

## PHẦN 4: TỐNG HỢP KIẾN THỨC BỔ TRỢ & NÂNG CAO

* **`__slots__`**: Tiết kiệm bộ nhớ RAM bằng cách ngăn Python tạo ra từ điển thuộc tính (`__dict__`) cho mỗi đối tượng.
* **Shallow vs Deep Copy**: Sao chép nông (chỉ chép tham chiếu) và sao chép sâu (chép toàn bộ giá trị độc lập).
* **PostgreSQL VACUUM**: Lệnh dọn rác bộ nhớ cho Database để duy trì tốc độ truy xuất.
* **Git Rebase**: Làm sạch lịch sử commit trước khi merge code vào nhánh chính.
* **OWASP Security**: Parameterized Queries chống SQL Injection, XSS protection bằng cách Sanitize HTML.

---

*Ghi chú: Nắm vững các khái niệm này sẽ giúp bạn vượt qua vòng phỏng vấn kỹ thuật một cách thuyết phục. Chúc bạn tỏa sáng!*
