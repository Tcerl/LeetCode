# 🧠 Odoo & Python Advanced Interview Q&A (Categorized)

Tài liệu này đã được phân loại chi tiết theo từng mảng kiến thức để phục vụ ôn tập chuyên sâu.

---

## 🗂 MỤC LỤC
1. [Phần 1: Python Core & Deep Dive](#phần-1-python-core--deep-dive)
2. [Phần 2: Odoo Core & Architecture](#phần-2-odoo-core--architecture)
3. [Phần 3: Odoo ORM & Data Handling](#phần-3-odoo-orm--data-handling)
4. [Phần 4: Hiệu năng & Cơ sở dữ liệu](#phần-4-hiệu-năng--cơ-sở-dữ-liệu)
5. [Phần 5: Bảo mật & Phân quyền](#phần-5-bảo-mật--phân-quyền)
6. [Phần 6: Giao diện, Frontend & Reports](#phần-6-giao-diện-frontend--reports)
7. [Phần 7: Tích hợp hệ thống & Flask](#phần-7-tích-hợp-hệ-thống--flask)
8. [Phần 8: Git & Quy trình làm việc](#phần-8-git--quy-trình-làm-việc)
9. [Phần 9: Tình huống thực tế & Debugging](#phần-9-tình-huống-thực-tế--debugging)
10. [Phần 10: Testing & Automation](#phần-10-testing--automation)
11. [Phần 11: Odoo 17/18 Specifics](#phần-11-odoo-1718-specifics)

---

## 🐍 PHẦN 1: PYTHON CORE & DEEP DIVE

### Q1: Tại sao không nên dùng đối tượng có thể thay đổi (list, dict) làm tham số mặc định?
- **Vấn đề:** Tham số mặc định được khởi tạo 1 lần duy nhất khi load module. Nếu sửa giá trị đó bên trong hàm, nó sẽ bị thay đổi cho mọi lần gọi sau.
- **Cách sửa:** Dùng `vals=None`, sau đó gán `vals = {}` bên trong hàm.

### Q2: Phân biệt `Generators (yield)` và `List Comprehension`?
- **List Comprehension:** Tạo toàn bộ dữ liệu vào RAM ngay lập tức. Nhanh nhưng tốn bộ nhớ.
- **Generator:** Chỉ sinh dữ liệu khi cần (Lazy evaluation). Cực kỳ tiết kiệm RAM khi xử lý hàng triệu bản ghi.

### Q3: `__slots__` dùng để làm gì?
- Ngăn việc tạo `__dict__` cho mỗi instance, giúp tiết kiệm bộ nhớ khi có hàng nghìn đối tượng (Odoo dùng rất nhiều trong BaseModel).

### Q4: Decorators hoạt động ra sao?
- Là hàm bọc hàm khác để thay đổi hành vi. Trong Odoo: `@api.model`, `@api.depends`, `@api.onchange`.

### Q5: Phân biệt `is` và `==`?
- `==`: So sánh giá trị.
- `is`: So sánh địa chỉ ô nhớ (identity).

### Q6: Phân biệt `*args` và `**kwargs` và khi nào sử dụng?
- **Sự khác biệt:**
    - `*args`: Nhận các tham số không định danh (positional arguments) dưới dạng một **Tuple**.
    - `**kwargs`: Nhận các tham số có định danh (keyword arguments) dưới dạng một **Dictionary**.
- **Khi nào sử dụng:**
    - **Khi override method (Odoo):** Bắt buộc dùng cả hai để chuyển tiếp toàn bộ tham số cho hàm `super()`, đảm bảo không làm mất dữ liệu của các module kế thừa khác trong chuỗi.
    - **Khi viết Decorators:** Dùng để bọc các hàm có số lượng tham số bất kỳ.
    - **Khi viết hàm linh hoạt:** Cho phép truyền vào nhiều giá trị mà không cần định nghĩa trước số lượng tham số (VD: Hàm tính tổng nhiều số, hàm format message).

### Q7: Hàm `__call__` của một Class?
- Cho phép gọi một instance của class như thể nó là một hàm.

### Q8: Sự khác biệt giữa List và Tuple về hiệu năng và bộ nhớ?
- **Tuple:** Bất biến (immutable), kích thước cố định nên chiếm ít bộ nhớ hơn và tốc độ truy cập nhanh hơn một chút.
- **List:** Có thể thay đổi, cần bộ nhớ dự phòng để append phần tử nên nặng hơn.

### Q9: Context Managers (`with` statement) hoạt động như thế nào?
- Dùng để quản lý tài nguyên (mở file, database connection). Nó gọi `__enter__` khi bắt đầu và `__exit__` khi kết thúc (kể cả khi có lỗi) để cleanup.

### Q63: Sự khác biệt giữa `shallow copy` và `deep copy` trong Python?
- **Shallow copy:** Tạo đối tượng mới nhưng vẫn tham chiếu đến các đối tượng con bên trong cái cũ.
- **Deep copy:** Sao chép toàn bộ, tạo ra một bản thể độc lập hoàn toàn kể cả các đối tượng lồng nhau.

### Q64: LAMBDA function là gì? Khi nào nên dùng?
- Là hàm ẩn danh (anonymous function) viết trên 1 dòng. Dùng cho các logic cực ngắn gọn, thường kết hợp với `map()`, `filter()`, `sorted()`.

### Q65: Global Interpreter Lock (GIL) trong Python là gì?
- Là cơ chế ngăn cản nhiều thread cùng thực thi bytecode Python một lúc. Điều này khiến Python không tận dụng được đa nhân (Multi-core) cho các tác vụ tính toán nặng (CPU bound), nhưng vẫn tốt cho các tác vụ I/O bound.

### Q84: Cách viết một Decorator có tham số?
- Bạn cần thêm một lớp hàm bọc bên ngoài cùng để nhận tham số. Cấu trúc thường là 3 tầng: `def decorator_with_args(arg): def actual_decorator(func): def wrapper(*args, **kwargs): ... return wrapper return actual_decorator`.

### Q85: Closures trong Python là gì?
- Là một hàm "nhớ" các biến từ môi trường (scope) mà nó được tạo ra, ngay cả khi môi trường đó đã thực thi xong. Dùng để tạo ra các hàm có trạng thái riêng mà không cần dùng Class.

---
## 🦁 PHẦN 2: ODOO CORE & ARCHITECTURE

### Q10: Phân biệt `models.Model`, `models.TransientModel` và `models.AbstractModel`?
- **Model:** Lưu bền vững trong DB.
- **TransientModel:** Dùng cho Wizard, Odoo tự dọn dẹp sau 1 giờ.
- **AbstractModel:** Mixin, không tạo bảng trong DB (VD: `mail.thread`).

### Q11: 3 kiểu Kế thừa trong Odoo?
- **Classical:** `_inherit` (không có `_name`). Sửa trực tiếp bảng cũ.
- **Prototype:** `_inherit` + `_name`. Tạo bảng mới dựa trên bảng cũ.
- **Delegation:** `_inherits`. Dùng FK kết nối 2 bảng (Composition).

### Q12: External ID (XML ID) là gì?
- Định danh string (VD: `base.main_company`) để tham chiếu record mà không cần biết số ID trong DB. Giúp đồng bộ giữa file XML và Database.

### Q13: `super()` trong Đa kế thừa Odoo?
- Đảm bảo chuỗi MRO không bị đứt. Nếu không gọi `super()`, logic của các module khác sẽ không được chạy.

### Q14: Phân biệt `_name` và `_inherit` khi dùng cùng lúc?
- Nếu dùng cả hai, bạn đang tạo một bảng mới copy tính năng bảng cũ (Prototype).

### Q15: Migration scripts (`pre-migrate`, `post-migrate`) là gì?
- Là các file Python trong thư mục `migrations/` dùng để xử lý chuyển đổi dữ liệu khi nâng cấp module (ví dụ: đổi tên field, gộp data) mà ORM không tự làm được.

### Q16: Manifest `data` vs `demo` vs `assets`?
- **data:** Chứa file cấu hình, view, quyền luôn được nạp.
- **demo:** Chỉ nạp khi khởi tạo database có check "Load demo data".
- **assets:** Khai báo JS/CSS/XML cho giao diện Web.

### Q66: Thuộc tính `_auto = False` dùng khi nào?
- Khi bạn muốn tự tạo bảng bằng SQL (SQL View) thay vì để Odoo tự sinh bảng từ khai báo Python.

### Q67: Ý nghĩa của `_order` trong Model?
- Quy định thứ tự sắp xếp mặc định khi lấy dữ liệu (VD: `_order = "date_order desc, id desc"`).

### Q68: Vòng đời (Life Cycle) của một module Odoo?
- **Install:** Chạy file XML/Data -> Chạy `post_init_hook`.
- **Upgrade:** So sánh version -> Chạy migration scripts -> Cập nhật các thay đổi XML.
- **Uninstall:** Xóa dữ liệu (nếu không có ràng buộc) -> Chạy `uninstall_hook`.

### Q86: Thuộc tính `_log_access` trong Model?
- Mặc định là `True`. Nó tự động tạo 4 trường: `create_uid`, `create_date`, `write_uid`, `write_date`. Nếu set `False`, Odoo sẽ không theo dõi ai sửa gì, giúp giảm dung lượng database cho các bảng log/tạm.

### Q87: `_inherit_children` dùng để làm gì?
- Dùng trong kế thừa để biết model nào đang kế thừa từ model này. Thường dùng trong các xử lý logic cấp thấp của hệ thống.

### Q106: Giải thích vòng đời của một HTTP Request trong Odoo (Request Lifecycle)?
1. **Client Request**: Browser gửi request tới Odoo (thường qua Nginx).
2. **Werkzeug Layer**: Thư viện Werkzeug nhận request, phân tích URL.
3. **Root Dispatching**: `Root.dispatch` thiết lập session, chọn database.
4. **IR HTTP Routing**: Model `ir.http` tìm kiếm route phù hợp (Controller hoặc Action).
5. **Security & Context**: Kiểm tra quyền truy cập, thiết lập context (`self.env`).
6. **Execution**: Chạy code xử lý (Controller method hoặc ORM).
7. **Response**: Trả về dữ liệu (JSON cho RPC hoặc QWeb/HTML cho Website).

### Q108: Phân biệt chi tiết `_inherit` và `_inherits`?
*   **`_inherit` (Classical/Prototype Inheritance):**
    *   **Mục đích:** Mở rộng tính năng của một model có sẵn hoặc tạo model mới dựa trên template cũ.
    *   **Cơ chế DB:** Thêm cột trực tiếp vào bảng cũ (nếu không có `_name`) hoặc tạo bảng mới hoàn toàn (nếu có `_name`).
    *   **Sử dụng:** `_inherit = 'res.partner'`.
*   **`_inherits` (Delegation Inheritance):**
    *   **Mục đích:** Kết nối hai model khác nhau theo dạng "kế thừa thuộc tính" (giống Composition trong OOP).
    *   **Cơ chế DB:** Không thêm cột của model cha vào model con. Thay vào đó, nó tạo một trường Many2one (Foreign Key) kết nối 2 bảng. Khi truy cập field của cha từ con, Odoo sẽ tự động "proxy" qua.
    *   **Sử dụng:** `_inherits = {'res.partner': 'partner_id'}` (Ví dụ: Model `res.users` kế thừa delegation từ `res.partner`).

---
## 🏗 PHẦN 3: ODOO ORM & DATA HANDLING

### Q17: `self.env` là gì?
- Chứa con trỏ DB (`cr`), User hiện tại (`uid`), và Ngữ cảnh (`context`).

### Q18: Phân biệt `browse()` và `search()`?
- **search:** Chạy SELECT tìm ID khớp điều kiện.
- **browse:** Chỉ tạo recordset từ ID có sẵn (Lazy load dữ liệu khi cần).

### Q19: `mapped()`, `filtered()`, `sorted()`?
- Duyệt và xử lý recordset mà không cần gọi lại Database (nếu dữ liệu đã cached).

### Q20: `new()` vs `create()`?
- **create:** Lưu thật vào DB (có ID).
- **new:** Bản ghi ảo trong bộ nhớ, dùng khi `onchange`.

### Q21: Biến `self` trong Odoo khác gì Python thường?
- `self` trong Odoo là một **Recordset** (chứa 0, 1 hoặc nhiều bản ghi). Luôn dùng vòng lặp `for`.

### Q22: `_rec_name` vs `display_name`?
- `_rec_name`: Chỉ định trường làm tên chính.
- `display_name`: Kết quả từ hàm `name_get()`.

### Q23: `name_get()` và `name_search()`?
- `name_get`: Chọn tên hiển thị. `name_search`: Chọn cách tìm kiếm bản ghi.

### Q24: `default_get()`?
- Gán giá trị mặc định động khi mở Form mới dựa trên context.

### Q25: `invalidate_cache()` và `flush()` dùng khi nào?
- **invalidate_cache:** Xóa cache của ORM để buộc load lại dữ liệu mới từ DB.
- **flush:** Đẩy dữ liệu đang chờ trong cache xuống DB ngay lập tức (thường dùng trước khi chạy SQL thô).

### Q26: `with_context` để làm gì?
- Tạo một bản sao recordset với context mới (ví dụ: `self.with_context(active_test=False).search([])` để search cả các bản ghi đã bị lưu trữ).

### Q69: Phân biệt `exists()` và `filtered()`?
- **exists():** Trả về những bản ghi thực sự còn tồn tại trong Database (loại bỏ recordset ảo hoặc đã bị xóa).
- **filtered():** Lọc dữ liệu trong bộ nhớ dựa trên 1 điều kiện logic.

### Q70: Tác dụng của tham số `limit` và `offset` trong `search()`?
- **limit:** Giới hạn số lượng bản ghi trả về (VD: Lấy 10 dòng đầu).
- **offset:** Bỏ qua n bản ghi đầu tiên (Dùng để làm phân trang).

### Q71: Trường `Binary` (File/Ảnh) lưu trữ ở đâu trong Odoo?
- Mặc định lưu trong **Filestore** (thư mục ngoài database). Database chỉ lưu đường dẫn hoặc metadata để đảm bảo DB không bị phình to quá nhanh.

### Q88: Phân biệt `read()` và `export_data()`?
- **read():** Trả về giá trị của các trường theo đúng kiểu dữ liệu Python (list, dict).
- **export_data():** Trả về dữ liệu dạng list of lists, đã được định dạng chuỗi sẵn sàng để xuất ra CSV/Excel.

### Q94: `compute_sudo=True` là gì và khi nào nên dùng?
- **Ý nghĩa:** Cho phép Odoo tính toán một computed field với quyền Admin (root), bỏ qua các kiểm tra phân quyền (Record Rules).
- **Khi nào dùng:** Khi field đó cần lấy dữ liệu từ các model mà user hiện tại không có quyền truy cập (VD: Tổng doanh thu công ty hiển thị cho nhân viên bán hàng).

### Q95: Phương thức `inverse` trong computed field dùng để làm gì?
- **Tác dụng:** Cho phép người dùng chỉnh sửa trực tiếp trên computed field. Khi field bị sửa, hàm `inverse` sẽ chạy để cập nhật giá trị ngược lại cho các trường phụ thuộc.
- **Ví dụ:** Computed field `total` = `price` * `qty`. Nếu sửa `total`, hàm `inverse` có thể tính lại `price = total / qty`.

### Q96: Phân biệt `search_read()` và `search_fetch()` trong Odoo 17+?
- **search_read():** Trình ORM sẽ thực hiện search và trả về một list các dict chứa data của fields được yêu cầu.
- **search_fetch():** (Mới từ Odoo 17) Trả về một Recordset đã được pre-fetch dữ liệu. Nó tối ưu hơn về bộ nhớ và hiệu năng khi xử lý tập dữ liệu lớn vì không cần chuyển toàn bộ thành list/dict ngay lập tức.

---
## ⚡ PHẦN 4: HIỆU NĂNG & CƠ SỞ DỮ LIỆU

### Q27: Vấn đề N+1 Query là gì và cách xử lý?
- **Vấn đề**: Xảy ra khi bạn duyệt một recordset (N bản ghi) và bên trong vòng lặp thực hiện truy cập vào một trường relational (Many2one/One2many). ORM sẽ bắn ra N câu query SELECT riêng lẻ xuống DB, gây chậm hệ thống trầm trọng.
- **Cách xử lý**: Dùng cơ chế **Prefetching** của Odoo (thường tự động nếu dùng recordset đúng cách). Hoặc dùng hàm `mapped()` để đọc giá trị hàng loạt trước khi vào loop, hoặc sử dụng `read()`/`search_read()` với danh sách fields cụ thể.

### Q28: `store=True` trong Computed Field?
- Lưu giá trị vào DB. Giúp search/sort nhanh nhưng làm chậm tốc độ ghi (`write`).

### Q29: Cơ chế "Lazy Update" (Lazy Flush) của Odoo?
- **Cơ chế**: Khi gọi `write()`, Odoo không lập tức bắn UPDATE xuống Postgres. Nó lưu thay đổi vào **ORM Cache**. 
- **Khi nào Flush**: Dữ liệu chỉ được đẩy xuống DB khi: Giao dịch kết thúc (Commit), khi có lệnh `search()`/`read()` liên quan đến trường đó, hoặc khi gọi `self.env.flush_all()` (Odoo 16+) để đảm bảo tính nhất quán dữ liệu trước khi chạy SQL thô.

### Q30: Giải thích hiện tượng Gap ID (Mất số) sau khi Rollback?
- **Hiện tượng**: Bạn gọi `create()`, Odoo lấy ID = 15 từ Sequence. Sau đó gặp lỗi `ValidationError`. Lần lưu sau, bản ghi nhận ID = 16 (mất số 15).
- **Lý do**: PostgreSQL Sequence hoạt động **độc lập** với Transaction. Một khi ID đã được lấy ra ("consumed"), nó sẽ không bao giờ được trả lại dù giao dịch có bị Rollback. Điều này giúp tránh hiện tượng "Lock" hàng đợi khi nhiều người cùng tạo bản ghi đồng thời, đảm bảo hiệu năng cao.

### Q31: Many2many ở tầng Database?
- Tạo một bảng trung gian kết nối 2 ID. Cần đánh INDEX bảng này khi dữ liệu lớn.

### Q32: SQL View Model?
- Gán `_auto = False` và tạo View bằng SQL trực tiếp để xử lý báo cáo phức tạp nhanh hơn.

### Q33: `search().count()` vs `search_count()`?
- `search_count` dùng SQL `COUNT(*)` nên nhanh hơn nhiều.

### Q34: Làm sao để kiểm tra index có thực sự được dùng trong Postgres?
- Dùng `EXPLAIN ANALYZE <query>`. Tìm dòng "Index Scan" (tốt) vs "Seq Scan" (quét toàn bảng - chậm).

### Q35: Phân biệt trường `Float` và `Monetary`?
- **Monetary:** Đi kèm với `currency_id`, tự động định dạng tiền tệ và làm tròn chính xác theo cấu hình của loại tiền đó. Tránh sai số kế toán.

### Q72: Tại sao nên tránh dùng `fields.Text` cho các trường cần tìm kiếm thường xuyên?
- `fields.Text` lưu dữ liệu lớn không giới hạn. Việc tìm kiếm (`like`) trên text dung lượng lớn cực kỳ chậm so với `Char` (có giới hạn và dễ index hơn).

### Q73: Connection Pooling trong Odoo là gì?
- Odoo duy trì một tập hợp các kết nối sẵn có tới PostgreSQL để dùng lại, thay vì mỗi request lại mở mới 1 kết nối (gây chậm và tốn tài nguyên hệ thống).

### Q89: PostgreSQL VACUUM là gì và tại sao Odoo cần nó?
- Khi bạn xóa hoặc update bản ghi, Postgres không thực sự xóa ngay mà đánh dấu "dead tuple". `VACUUM` giúp thu hồi không gian trống đó. Nếu không chạy, database sẽ bị phình to khủng khiếp (Bloat) và làm chậm hệ thống.

---
## 🔐 PHẦN 5: BẢO MẬT & PHÂN QUYỀN

### Q36: Bảo mật 2 lớp trong Odoo?
- **Access Rights:** Quyền CRUD trên Model.
- **Record Rules:** Quyền trên từng bản ghi cụ thể.

### Q37: `sudo()` vs `with_user()`?
- `sudo`: Quyền quản trị tối cao, bỏ qua kiểm tra Rule.
- `with_user`: Đóng vai một User cụ thể để áp dụng đúng quyền của họ.

### Q38: Multi-company hoạt động ra sao?
- Odoo tự chèn `WHERE company_id IN (...)` vào mọi câu SQL nhờ Record Rules mặc định.

### Q39: Debug lỗi "Access Error"?
- Kiểm tra Record Rules và chạy với `--log-level=debug_sql` để xem câu lệnh WHERE bị chặn.

### Q40: Phân quyền cá nhân (Personal) vs Toàn cầu (Global) trong Record Rules?
- **Global:** Áp dụng cho mọi user, không quan trọng thuộc nhóm nào.
- **Personal:** Gán cho từng nhóm cụ thể, thường dùng để giới hạn nhân viên chỉ xem được data của chính mình.

### Q74: Cách tạo một Security Group mới qua file XML?
- Tạo bản ghi trong model `res.groups`, định nghĩa tên và các quyền (implied_ids) kế thừa từ group khác.

### Q75: Phân biệt `base.group_system` và `base.group_erp_manager`?
- **ERP Manager:** Quản lý toàn bộ dữ liệu nghiệp vụ.
- **System:** Là Admin kỹ thuật, có quyền can thiệp vào cấu hình hệ thống, debug.

---
## 🎨 PHẦN 6: GIAO DIỆN, FRONTEND & REPORTS

### Q41: XPath trong View kế thừa?
- Dùng `position="after/before/replace/attributes"` để sửa UI không đụng code gốc.

### Q42: OWL (Odoo Web Library) là gì?
- Framework JS hiện đại (Virtual DOM) từ Odoo 14+. Dùng Component, Hooks.

### Q43: Assets Bundle?
- Khai báo JS/CSS trong `__manifest__.py` để Odoo nén và gộp file chung.

### Q44: QWeb Reports (PDF)?
- Kết hợp XML và công cụ `wkhtmltopdf`. Nên chuẩn bị data ở Python trước khi render.

### Q45: Thuộc tính `groups` trên field hoặc menuitem có tác dụng gì?
- Ẩn/hiện element đó ở mức **UI**. User không thuộc nhóm sẽ không thấy nhưng vẫn có thể truy cập qua API nếu không có Access Rights chặn ở model.

### Q76: Cách sử dụng `attrs` (invisible, readonly, required) trong XML?
- Cho phép thay đổi trạng thái của field một cách năng động dựa trên giá trị của trường khác (VD: `attrs="{'invisible': [('state', '=', 'draft')]}"`).

### Q77: Widget trong Odoo là gì? Cho ví dụ.
- Là cách hiển thị dữ liệu khác đi trên UI. Ví dụ: `widget="status_bars"` (thanh trạng thái), `widget="many2many_tags"` (hiển thị tag màu).

### Q90: `search_panel` là gì?
- Là thanh lọc phía bên trái màn hình (thường thấy trong model Nhân viên hoặc Sản phẩm), giúp user lọc nhanh theo danh mục mà không cần gõ search. Khai báo bên trong thẻ `<search>`.

### Q97: Giải thích vòng đời (Lifecycle) của một component OWL?
- **setup():** Khởi tạo state, hooks. Chạy trước khi render.
- **willStart():** Chạy trước khi component được mount, dùng để load data từ server (async).
- **mounted():** Chạy sau khi DOM đã được tạo. Dùng để tương tác với thư viện bên ngoài.
- **willUpdateProps():** Chạy khi component nhận props mới từ cha.
- **willUnmount():** Chạy trước khi bị hủy để cleanup.

### Q98: Phân biệt `useState` và `reactive` trong OWL?
- **useState:** Dùng để theo dõi sự thay đổi của một object/array đơn giản trong component. Khi state đổi, component sẽ re-render.
- **reactive:** Cấp thấp hơn, dùng cho các object phức tạp hoặc chia sẻ state giữa nhiều component. Nó không tự động buộc render nếu không được bọc bởi `useState` hoặc dùng trong template.

### Q99: Cách thay đổi hành vi của một Class JS hoặc Object có sẵn trong Odoo?
- Dùng **Patching** (hàm `patch` từ `@web/core/utils/patch`). Nó cho phép thêm mới hoặc override method của một Object/Class mà không làm hỏng logic gốc (tương tự `_inherit` ở Python).

---
## 🌐 PHẦN 7: TÍCH HỢP HỆ THỐNG & FLASK

### Q46: Odoo Controller vs Flask?
- Cả hai cùng dùng `Werkzeug`. Odoo Controller tích hợp sẵn ORM/Session. Flask linh hoạt hơn cho Microservices.

### Q47: Blueprint (Flask) vs Addon Module (Odoo)?
- Cả hai đều dùng để chia nhỏ cấu trúc logic ứng dụng.

### Q48: Tích hợp với bên thứ 3?
- Dùng **XML-RPC** hoặc **JSON-RPC**. Quy trình: Login -> Call ORM methods.

### Q49: Webhook là gì và triển khai thế nào trong Odoo?
- Là một Controller lắng nghe POST request từ bên ngoài. Odoo nhận dữ liệu, xác thực hash/key và xử lý logic.

### Q78: Odoo Shell là gì?
- Là môi trường dòng lệnh (CLI) cho phép bạn truy cập vào toàn bộ bộ máy Odoo để debug, viết script chạy dữ liệu nhanh mà không cần mở giao diện Web.

### Q79: Cách gán API key cho User?
- Vào Profile của User -> tab Account Security -> New API Key. Điều này an toàn hơn việc dùng mật khẩu chính để tích hợp hệ thống.

---
## 🛠 PHẦN 8: GIT & QUY TRÌNH LÀM VIỆC

### Q50: `git merge` vs `git rebase`?
- **Merge:** Giữ lịch sử nhánh, an toàn cho nhánh chung.
- **Rebase:** Làm lịch sử thẳng hàng, chỉ dùng cho nhánh Local feature.

### Q51: `git stash`?
- Cất code đang làm dở để switch nhánh gấp.

### Q52: `git cherry-pick`?
- Lấy duy nhất 1 commit từ nhánh khác áp dụng vào nhánh hiện tại.

### Q53: `git reset --soft` vs `--hard`?
- `--soft`: Quay lại commit cũ nhưng giữ code ở Staging.
- `--hard`: Xóa sạch code đã viết, quay về quá khứ.

### Q54: `git commit --amend` dùng khi nào?
- Khi bạn vừa commit xong nhưng phát hiện sai sót nhỏ hoặc quên thêm file, dùng lệnh này để gộp thay đổi vào commit cũ.

### Q55: Git Tags là gì?
- Dùng để đánh dấu các mốc quan trọng (ví dụ: `v1.0.0`). Giúp dễ dàng quay lại đúng phiên bản đã release.

### Q80: Cách dùng `git blame`?
- Dùng để kiểm tra xem ai là người cuối cùng sửa đổi từng dòng code cụ thể trong một file. Rất hữu ích khi cần tìm người để hỏi về logic cũ.

### Q81: Phân biệt `git pull` và `git fetch`?
- **fetch:** Chỉ cập nhật thông tin về các thay đổi từ server về máy bạn, chưa gộp vào code.
- **pull:** Là tổ hợp của `fetch` + `merge`. Nó lấy code về và gộp ngay vào nhánh hiện tại.

### Q91: Mô hình Git Flow cơ bản gồm những nhánh nào?
- **Master/Main:** Chứa code sạch nhất, đã release.
- **Develop:** Nhánh chính để code.
- **Feature/Fix:** Nhánh phụ cho từng tính năng riêng.
- **Hotfix:** Nhánh sửa lỗi khẩn cấp trực tiếp từ Master.

---
## 🐞 PHẦN 9: TÌNH HUỐNG THỰC TẾ & DEBUGGING

### Q56: Cách xử lý Cron Job cập nhật 1 triệu bản ghi tránh Timeout?
- **Chiến lược**:
    1. **Chia batch nhỏ**: Sử dụng `limit` (ví dụ 1000 bản ghi mỗi lần).
    2. **Commit từng phần**: Dùng `self.env.cr.commit()` sau mỗi batch để lưu ngay vào DB, giải phóng bộ nhớ và tránh mất dữ liệu nếu crash giữa chừng.
    3. **Tự động gọi lại**: Set Cron chạy lặp lại liên tục, hoặc dùng cơ chế `re-enqueue` (check xem còn data không để set `nextcall` ngay lập tức).
    4. **Duyệt ID**: Tránh dùng `offset` (chậm khi data lớn), hãy dùng điều kiện `WHERE id > last_seen_id`.

### Q107: Cách thiết lập một Scheduled Action (Cron) qua file XML?
- Khai báo record trong model `ir.cron`. Các thuộc tính quan trọng:
    - `model_id`: Model chứa hàm xử lý.
    - `state`: Luôn là `code`.
    - `code`: Đoạn mã gọi hàm, ví dụ `model._cron_my_task()`.
    - `interval_number` & `interval_type`: Tần suất chạy (phút, giờ, ngày).
    - `numbercall`: Số lần chạy (-1 là vô hạn).
    - `doall`: Nếu Server tắt lúc đến lịch, khi bật lại có chạy bù không.

### Q57: `active=False` vs `unlink()`?
- `active=False`: Ẩn dữ liệu (Soft delete). `unlink`: Xóa vĩnh viễn (Hard delete).

### Q58: Ngăn xóa bản ghi quan trọng?
- Ghi đè `unlink()` bắn lỗi hoặc dùng `ondelete='restrict'`.

### Q59: `@api.constrains` vs `_sql_constraints`?
- `_sql`: Ở tầng DB, cực nhanh. `@api`: Ở tầng Python, cho logic phức tạp.

### Q60: Tìm câu SQL chạy chậm?
- Dùng `--log-sql`, Odoo Profiler hoặc `EXPLAIN ANALYZE` trong Postgres.

### Q61: Xử lý `MemoryError` khi import dữ liệu cực lớn?
- Dùng `Odoo shell` để chạy script Python, đọc file theo từng dòng (chunk) và `cr.commit()` sau mỗi 500-1000 bản ghi để giải phóng bộ nhớ.

### Q62: Phân biệt `UserError` và `ValidationError`?
- **UserError:** Thông báo lỗi nghiệp vụ chung cho người dùng (thường dùng bất cứ đâu).
- **ValidationError:** Kích hoạt khi quy tắc dữ liệu bị vi phạm (thường dùng trong `@api.constrains`).

### Q82: User báo lỗi "504 Gateway Timeout" khi in hóa đơn, bạn điều tra từ đâu?
1. Kiểm tra log của Nginx/Apache.
2. Kiểm tra log Odoo có báo Long Query không.
3. Kiểm tra xem file PDF có chứa ảnh quá nặng không.

### Q83: Làm thế nào để thay đổi Logo công ty hàng loạt?
- Truy cập vào model `res.company`, dùng `write()` để cập nhật trường `logo` cho tất cả các bản ghi thông qua Odoo Shell hoặc script Python.

### Q92: Nginx đóng vai trò gì khi triển khai Odoo?
- **Reverse Proxy:** Chặn các request từ internet và chuyển vào Odoo.
- **Load Balancing:** Chia tải cho nhiều Worker.
- **SSL Termination:** Xử lý chứng chỉ HTTPS.
- **Static Assets:** Phục vụ các file ảnh/JS/CSS trực tiếp mà không cần làm phiền tới Odoo server, giúp tăng tốc vượt trội.

### Q93: Tại sao nên dùng Docker khi phát triển Odoo?
- Đảm bảo môi trường (Python version, thư viện, Postgres) giống hệt nhau giữa máy Developer và máy Server, tránh lỗi "máy em chạy được nhưng máy kia không chạy".

---
## 🧪 PHẦN 10: TESTING & AUTOMATION

### Q100: Phân biệt `TransactionCase`, `SavepointCase` và `HttpCase`?
- **TransactionCase:** Mỗi test method chạy trong một transaction riêng và bị rollback sau khi xong. Chậm hơn SavepointCase.
- **SavepointCase:** (Odoo 12-16, 17+ dùng subtests) Dùng savepoint để rollback từng test. Toàn bộ class chung 1 trang thái DB trước khi test.
- **HttpCase:** Dùng để test các logic liên quan đến Controller, Website, Tours (JS). Nó mở một server HTTP thật để chạy test.

### Q101: Odoo Tour (JS Test) là gì và tại sao nó quan trọng?
- Là kịch bản test tự động mô phỏng click/type của người dùng trên trình duyệt. Rất quan trọng để đảm bảo logic frontend (OWL, JS) và UI không bị break sau khi update code.

### Q102: Cách dùng `unittest.mock` để giả lập (Mocking) trong kiểm thử Odoo?
- Dùng `@patch` hoặc `MagicMock` để thay thế các hàm gọi bên thứ 3 (Gửi mail, gọi API ngân hàng) bằng các hàm giả. Giúp test chạy nhanh và không phụ thuộc vào internet hay hệ thống bên ngoài.

---
## 🚀 PHẦN 11: ODOO 17/18 SPECIFICS

### Q103: Những thay đổi kỹ thuật lớn nhất trong Odoo 17 là gì?
- **New Registry:** Cải thiện tốc độ load module.
- **UI/UX:** Thiết kế lại hoàn toàn icons, dark mode mặc định, thanh tìm kiếm (Search bar) cải tiến.
- **Performance:** Tối ưu hóa prefetching ORM và giảm kích thước assets bundle.

### Q104: Cơ chế "Direct Print" mới trong Odoo 17 hoạt động như thế nào?
- Cho phép in hóa đơn/phiếu kho thẳng ra máy in mà không cần tải file PDF về trình duyệt rồi mới bấm in, giúp đẩy nhanh tốc độ tại quầy POS hoặc kho hàng.

### Q105: Cách bật và tùy chỉnh chế độ Dark Mode trong Odoo 17+?
- Odoo 17 hỗ trợ Dark Mode "out-of-the-box". User có thể switch trong menu User Profile. Developer có thể tùy chỉnh màu sắc qua các biến CSS variables trong hệ thống assets.
