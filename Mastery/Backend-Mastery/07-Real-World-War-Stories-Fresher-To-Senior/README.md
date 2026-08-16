# 07. Chiến Trường Thực Tế: Sự Cố Backend Thật Từ Fresher Đến Senior

> Khác với Module 05 (bảng vấn đề ngắn gọn theo cấp độ), module này kể lại **từng sự cố như 1 câu chuyện đầy đủ**: bối cảnh → triệu chứng → quá trình điều tra sai hướng ban đầu (thường có) → nguyên nhân gốc → cách sửa → bài học. Đây chính là nguyên liệu thật để bạn kể trong phỏng vấn theo khung STAR ở [`Mastery/Career-Mastery/04`](../../Career-Mastery/04-Behavioral-And-Salary-Negotiation/README.md).

---

## 🟢 FRESHER — sự cố do chưa hình thành phản xạ an toàn cơ bản

### Sự cố 1: API key bị lộ công khai trên GitHub, bị lợi dụng trong vài giờ
- **Bối cảnh:** Fresher push code lên GitHub public repo cá nhân để làm portfolio, trong đó có file `.env` chứa API key của dịch vụ gửi email (SendGrid).
- **Triệu chứng:** Vài giờ sau, tài khoản SendGrid gửi hàng chục nghìn email spam, tài khoản bị khóa, nhận cảnh báo lạm dụng.
- **Nguyên nhân gốc:** Bot tự động quét GitHub liên tục tìm các pattern API key lộ trong repo public — đây không phải rủi ro lý thuyết, mà xảy ra trong vài phút tới vài giờ sau khi push.
- **Cách sửa:** Thu hồi (revoke) key ngay lập tức, tạo key mới, thêm `.env` vào `.gitignore` từ đầu mọi project, dùng `git filter-repo`/BFG để xóa key khỏi lịch sử Git (chỉ xóa file ở commit mới KHÔNG đủ — key vẫn còn trong lịch sử).
- **Bài học:** Không bao giờ commit secret dù chỉ 1 lần dù sẽ xóa ngay sau đó — lịch sử Git là public forever với repo public, và các bot quét gần như real-time.

### Sự cố 2: Kết nối database không đóng, service crash sau vài ngày chạy ổn định
- **Bối cảnh:** Fresher viết script xử lý batch dữ liệu định kỳ, mở connection DB thủ công trong vòng lặp mà không dùng context manager (`with`).
- **Triệu chứng:** Service chạy bình thường 3-4 ngày đầu, sau đó bắt đầu báo lỗi "too many connections", cuối cùng crash hoàn toàn.
- **Quá trình điều tra sai hướng:** Ban đầu nghi ngờ do lượng dữ liệu tăng đột biến, thử tăng RAM/CPU server — không cải thiện.
- **Nguyên nhân gốc:** Mỗi lần vòng lặp chạy tạo 1 connection mới nhưng không đóng lại, connection tích lũy dần tới khi chạm giới hạn `max_connections` của DB.
- **Cách sửa:** Dùng `with engine.connect() as conn:` (hoặc connection pool có scope rõ ràng) để đảm bảo connection luôn được trả lại dù có lỗi xảy ra giữa chừng.
- **Bài học:** Bất kỳ tài nguyên nào "mở" (file, connection, socket) đều phải có nơi "đóng" tương ứng được đảm bảo chạy kể cả khi có exception — đây là lý do `with`/`try-finally` tồn tại, không phải chi tiết cú pháp có thể bỏ qua.

### Sự cố 3: Hiển thị sai giờ cho user ở học kỳ đầu đi làm
- **Bối cảnh:** Fresher lưu timestamp bằng `datetime.now()` (giờ local server) thay vì UTC, hệ thống có user ở nhiều múi giờ.
- **Triệu chứng:** User báo cáo thời gian đơn hàng hiển thị sai lệch vài giờ so với thực tế họ đặt.
- **Nguyên nhân gốc:** Trộn lẫn giữa "giờ server" và "giờ hiển thị cho user" — khi server đổi vùng (dev local múi giờ khác server production), toàn bộ dữ liệu cũ bị lệch theo.
- **Cách sửa:** Luôn lưu timestamp dưới dạng UTC trong database, chỉ convert sang timezone của user ở tầng hiển thị (frontend hoặc lúc serialize response).
- **Bài học:** Nguyên tắc bất di bất dịch: **lưu trữ = UTC luôn, hiển thị = convert theo user** — trộn lẫn 2 việc này là nguồn lỗi timezone kinh điển nhất trong toàn bộ sự nghiệp backend.

---

## 🟡 JUNIOR — sự cố do chưa lường hết tình huống ngoài happy path

### Sự cố 4: Webhook đối tác gửi trùng lặp do retry vô hạn không idempotent
- **Bối cảnh:** Junior code endpoint nhận webhook xác nhận thanh toán từ cổng thanh toán thứ 3, mỗi lần nhận thì cộng tiền vào ví user.
- **Triệu chứng:** Một số user báo được cộng tiền nhiều lần cho cùng 1 giao dịch.
- **Quá trình điều tra sai hướng:** Ban đầu nghi ngờ lỗi ở phía cổng thanh toán.
- **Nguyên nhân gốc:** Cổng thanh toán retry webhook khi không nhận được response 200 kịp thời (do server xử lý chậm lúc cao điểm) — endpoint xử lý webhook không kiểm tra đã xử lý giao dịch này chưa trước khi cộng tiền.
- **Cách sửa:** Thêm bảng lưu `transaction_id` đã xử lý, kiểm tra tồn tại trước khi xử lý (idempotency key), luôn trả response 200 ngay khi đã ghi nhận (dù xử lý nghiệp vụ bất đồng bộ sau).
- **Bài học:** Bất kỳ endpoint nào nhận sự kiện từ bên ngoài (webhook, message queue) đều PHẢI thiết kế idempotent — hệ thống bên ngoài luôn có khả năng gửi trùng, đây không phải trường hợp hiếm.

### Sự cố 5: Phân trang (pagination) bị thiếu/trùng bản ghi khi có insert đồng thời
- **Bối cảnh:** Junior dùng offset-based pagination (`LIMIT 20 OFFSET n`) cho danh sách đơn hàng liên tục có đơn mới được tạo.
- **Triệu chứng:** User lướt qua trang 2, một số đơn hàng bị lặp lại từ trang 1 hoặc bị mất hẳn không xuất hiện ở trang nào.
- **Nguyên nhân gốc:** Giữa 2 lần gọi API lấy trang 1 và trang 2, có đơn hàng mới được chèn vào đầu danh sách (sắp xếp theo thời gian tạo giảm dần) — làm lệch toàn bộ offset của các trang sau.
- **Cách sửa:** Chuyển sang cursor-based pagination (dùng `id`/`created_at` của bản ghi cuối cùng đã thấy làm điểm neo, thay vì offset theo số thứ tự).
- **Bài học:** Offset pagination chỉ an toàn với dữ liệu tĩnh hoặc ít thay đổi — với danh sách có insert liên tục, cursor-based pagination mới đảm bảo tính nhất quán.

### Sự cố 6: Trả lỗi 500 kèm nguyên stack trace cho client production
- **Bối cảnh:** Junior để mặc định `DEBUG=True` khi deploy production vì "quên đổi lại".
- **Triệu chứng:** Khi có lỗi, client nhận về toàn bộ stack trace, đường dẫn file nội bộ, thậm chí có thể thấy 1 phần connection string DB trong traceback.
- **Nguyên nhân gốc:** Cấu hình debug mode không được tách biệt rõ ràng theo environment, không có checklist trước khi deploy.
- **Cách sửa:** Bắt buộc `DEBUG=False` ở production qua biến môi trường, có custom error handler trả về message chung an toàn cho client, log đầy đủ chi tiết ở phía server.
- **Bài học:** Đây không chỉ là bug UX mà là **lỗ hổng bảo mật thật** — rò rỉ thông tin nội bộ hệ thống là bước đầu tiên kẻ tấn công dùng để dò tìm lỗ hổng tiếp theo.

---

## 🔴 MID-LEVEL — sự cố do chưa tính toán hết tương tác giữa các thành phần hệ thống

### Sự cố 7: Cache stampede khi key phổ biến hết hạn cùng lúc giờ cao điểm
- **Bối cảnh:** Mid-level cache kết quả trang chủ (danh sách sản phẩm hot) trong Redis với TTL cố định 5 phút.
- **Triệu chứng:** Cứ đúng 5 phút, có 1 khoảng thời gian ngắn database bị spike CPU đột ngột, đôi khi timeout hàng loạt request.
- **Nguyên nhân gốc:** Khi cache hết hạn đúng lúc lượng truy cập cao, HÀNG NGHÌN request cùng lúc miss cache, tất cả cùng đánh thẳng vào database để tính lại giá trị — "cache stampede".
- **Cách sửa:** Áp dụng 1 trong các kỹ thuật: (a) khóa (lock) chỉ cho 1 request tính lại giá trị, các request khác chờ hoặc dùng giá trị cũ; (b) thêm jitter ngẫu nhiên vào TTL để các key không hết hạn đồng loạt; (c) cache "stale-while-revalidate" — trả giá trị cũ ngay trong lúc âm thầm tính lại giá trị mới.
- **Bài học:** Cache không chỉ là "lưu tạm cho nhanh" — thiết kế sai cách hết hạn có thể biến cache thành nguyên nhân gây sự cố thay vì giải pháp.

### Sự cố 8: Gọi API bên thứ 3 không có timeout/circuit breaker, kéo sập cả hệ thống
- **Bối cảnh:** Mid-level tích hợp gọi API địa chỉ/vận chuyển của bên thứ 3 trong luồng tạo đơn hàng, không set timeout.
- **Triệu chứng:** Một hôm bên thứ 3 bị sự cố, phản hồi rất chậm (không phải lỗi hẳn) — toàn bộ hệ thống tạo đơn hàng bị treo theo, dù bản thân hệ thống không có lỗi gì.
- **Nguyên nhân gốc:** Không set timeout cho HTTP client → mỗi request chờ vô thời hạn → toàn bộ worker/thread xử lý request bị chiếm giữ chờ API bên ngoài → hệ thống hết worker khả dụng cho cả các request KHÔNG liên quan tới bên thứ 3 đó.
- **Cách sửa:** Luôn set timeout hợp lý cho MỌI lời gọi ra bên ngoài, thêm circuit breaker (ngừng gọi tạm thời khi tỷ lệ lỗi/timeout vượt ngưỡng, tự thử lại sau), tách các luồng phụ thuộc bên ngoài ra queue/worker riêng thay vì dùng chung pool với luồng chính.
- **Bài học:** Một dependency bên ngoài chậm/lỗi không nên có khả năng làm sập TOÀN BỘ hệ thống — đây là nguyên tắc "graceful degradation", ranh giới rõ ràng giữa mid-level và senior nằm ở việc có chủ động thiết kế cho trường hợp phụ thuộc thất bại hay không.

### Sự cố 9: Migration `ALTER TABLE` khóa bảng production, gây downtime ngoài kế hoạch
- **Bối cảnh:** Mid-level thêm 1 cột `NOT NULL` có giá trị mặc định vào bảng có hàng chục triệu bản ghi, chạy migration trực tiếp lúc deploy giờ hành chính.
- **Triệu chứng:** Toàn bộ request liên quan tới bảng đó bị treo trong vài phút, một số bị timeout, alert dồn dập.
- **Nguyên nhân gốc:** Một số engine database khóa toàn bảng khi thêm cột có giá trị mặc định trên bảng lớn (tùy phiên bản/engine cụ thể) — bảng càng lớn, thời gian khóa càng lâu.
- **Cách sửa:** Áp dụng expand-contract pattern: thêm cột cho phép NULL trước (không khóa bảng lâu), backfill dữ liệu theo batch nhỏ ở background, sau đó mới thêm ràng buộc NOT NULL khi dữ liệu đã đầy đủ; luôn chạy migration lớn ngoài giờ cao điểm và test trên bản sao dữ liệu thật (staging) trước.
- **Bài học:** Không phải câu lệnh SQL nào "đúng cú pháp" cũng an toàn để chạy trực tiếp trên bảng lớn ở production — cần hiểu cơ chế khóa của engine database đang dùng trước khi chạy migration.

---

## 🔵 SENIOR — sự cố ở tầm kiến trúc, ảnh hưởng nhiều service/team

### Sự cố 10: Thiếu isolation multi-tenant, dữ liệu khách hàng A hiển thị cho khách hàng B
- **Bối cảnh:** Hệ thống SaaS multi-tenant, mỗi bảng có cột `tenant_id`, nhưng 1 endpoint báo cáo mới được thêm bởi 1 dev khác trong team quên thêm điều kiện lọc `tenant_id` trong 1 câu query join phức tạp.
- **Triệu chứng:** 1 khách hàng báo cáo nhìn thấy vài dòng dữ liệu không phải của mình trong 1 báo cáo tổng hợp — sự cố bảo mật dữ liệu nghiêm trọng, không phải lỗi UI thông thường.
- **Nguyên nhân gốc:** Việc lọc theo tenant phụ thuộc hoàn toàn vào việc từng dev nhớ thêm điều kiện ở từng query — không có cơ chế bắt buộc ở tầng hệ thống.
- **Cách sửa (senior xử lý ở tầm kiến trúc, không chỉ vá query lỗi):** Chuyển sang cơ chế enforce tenant isolation tự động ở tầng thấp hơn (row-level security của database, hoặc base query class/ORM middleware tự động thêm điều kiện tenant cho MỌI query, không cho phép query "trần" bỏ qua lớp này); thêm test tự động kiểm tra cross-tenant leakage cho mọi endpoint mới.
- **Bài học senior:** Vấn đề bảo mật nghiêm trọng do "con người quên" không nên được xử lý bằng cách "nhắc nhở cẩn thận hơn" — phải thiết kế lại hệ thống để lớp bảo vệ không phụ thuộc vào việc từng cá nhân nhớ đúng mỗi lần.

### Sự cố 11: Poison message làm nghẽn toàn bộ hàng đợi xử lý
- **Bối cảnh:** Hệ thống dùng queue (RabbitMQ/SQS) xử lý tác vụ nền, 1 message có dữ liệu dị dạng khiến consumer luôn crash khi xử lý.
- **Triệu chứng:** Consumer crash → message tự động được đưa lại vào queue (do chưa ack) → consumer khởi động lại, lại crash ngay lập tức với đúng message đó → vòng lặp vô hạn, toàn bộ message phía sau bị nghẽn không được xử lý dù bản thân chúng hợp lệ.
- **Nguyên nhân gốc:** Không có Dead Letter Queue (DLQ) và giới hạn số lần retry — hệ thống coi mọi lỗi là tạm thời và đáng retry vô hạn.
- **Cách sửa:** Cấu hình giới hạn số lần retry, chuyển message sau N lần thất bại sang DLQ để xử lý/điều tra riêng thay vì chặn toàn bộ hàng đợi chính; alert riêng khi có message vào DLQ.
- **Bài học senior:** Thiết kế hệ thống bất đồng bộ phải tính tới cả trường hợp "1 đơn vị công việc không bao giờ xử lý thành công được" — không phải mọi lỗi đều nên retry vô hạn.

### Sự cố 12: Tách service quá sớm, tạo ra "distributed monolith" khó vận hành hơn cả cũ
- **Bối cảnh:** Team tách 1 module thành microservice riêng vì "để dễ scale sau này", nhưng service mới vẫn gọi đồng bộ (synchronous) trực tiếp và chia sẻ chung 1 database với service gốc.
- **Triệu chứng:** Độ phức tạp vận hành tăng vọt (2 service để deploy/monitor thay vì 1) nhưng KHÔNG có lợi ích thực sự nào về khả năng scale hay độ tin cậy — ngược lại, latency tăng do thêm 1 lần gọi mạng, và lỗi ở service phụ giờ có thể làm service chính fail theo.
- **Nguyên nhân gốc:** Quyết định tách service dựa trên "thực hành tốt nên làm" thay vì nhu cầu thật (team/tải/độ phức tạp nghiệp vụ chưa tới ngưỡng cần tách), và tách sai ranh giới (vẫn chia sẻ database, vẫn gọi đồng bộ) nên chỉ nhân đôi độ phức tạp mà không có tính độc lập thật.
- **Cách sửa:** Đánh giá lại quyết định — hoặc merge lại thành 1 service nếu chưa có lý do vận hành thật để tách, hoặc nếu giữ tách thì phải tách đúng (database riêng, giao tiếp bất đồng bộ qua event, có API contract rõ ràng, có thể deploy độc lập thật sự).
- **Bài học senior:** Microservices là công cụ giải quyết vấn đề TỔ CHỨC (nhiều team làm việc độc lập) và vấn đề SCALE cụ thể — áp dụng nó khi chưa có vấn đề đó chỉ tạo thêm chi phí vận hành mà không có lợi ích tương xứng. Đọc thêm góc nhìn tương tự ở [`Mastery/Frontend-Fullstack-Mastery/03`](../../Frontend-Fullstack-Mastery/03-Fullstack-Project-Architecture/README.md).

---

## 🎯 Cách dùng module này trong phỏng vấn
Mỗi sự cố ở trên đều theo đúng cấu trúc STAR (Bối cảnh=S, việc cần làm=T ẩn trong "triệu chứng", Hành động=Cách sửa, Kết quả=Bài học) — nếu bạn từng gặp sự cố tương tự trong công việc thật, hãy dùng đúng cấu trúc này để kể lại theo [`Mastery/Career-Mastery/04`](../../Career-Mastery/04-Behavioral-And-Salary-Negotiation/README.md). Nếu chưa từng gặp, đây cũng là danh sách "rủi ro cần chủ động phòng tránh" cho dự án cá nhân bạn đang xây (xem [`Mastery/Career-Mastery/05`](../../Career-Mastery/05-Salary-Growth-Playbook/README.md)).

## 🔗 Liên kết
Chi tiết kỹ thuật liên quan: [`01`](../01-Request-Lifecycle-And-Architecture/README.md) · [`02`](../02-Concurrency-And-Async-In-Production/README.md) · [`03`](../03-Database-Choice-And-Scaling-Playbook/README.md) · [`04`](../04-Testing-Observability-And-Debugging-Prod/README.md) · [`05`](../05-Junior-To-Senior-Problem-Playbook/README.md)
Sự cố tầng hạ tầng tương tự: [`../Cloud-DevOps-Mastery/07`](../../Cloud-DevOps-Mastery/07-Real-World-War-Stories-Fresher-To-Senior/README.md)
