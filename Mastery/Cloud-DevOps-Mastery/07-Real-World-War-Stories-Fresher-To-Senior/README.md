# 07. Chiến Trường Thực Tế: Sự Cố Cloud/DevOps Thật Từ Fresher Đến Senior

> Cùng cấu trúc với [`Mastery/Backend-Mastery/07`](../../Backend-Mastery/07-Real-World-War-Stories-Fresher-To-Senior/README.md) — mỗi sự cố kể đầy đủ: bối cảnh → triệu chứng → nguyên nhân gốc → cách sửa → bài học, dùng làm nguyên liệu kể chuyện phỏng vấn theo khung STAR ở [`Mastery/Career-Mastery/04`](../../Career-Mastery/04-Behavioral-And-Salary-Negotiation/README.md).

---

## 🟢 FRESHER — sự cố do chưa hình thành phản xạ vận hành cơ bản

### Sự cố 1: Log không xoay vòng (rotate), disk đầy làm crash toàn bộ server
- **Bối cảnh:** Fresher deploy app ghi log ra file trực tiếp trên EC2, không cấu hình log rotation.
- **Triệu chứng:** Sau vài tuần chạy ổn định, server đột nhiên không phản hồi, SSH vào cũng không thao tác được.
- **Nguyên nhân gốc:** File log tăng dần không giới hạn, chiếm hết dung lượng ổ đĩa — khi disk đầy 100%, hệ điều hành không còn chỗ ghi file tạm, kéo theo toàn bộ tiến trình (kể cả SSH daemon) hoạt động bất thường.
- **Cách sửa:** Cấu hình `logrotate` (xoay vòng + nén + xóa log cũ theo lịch), hoặc tốt hơn là đẩy log ra hệ thống tập trung (CloudWatch Logs/ELK) thay vì ghi file cục bộ; thêm alert khi disk usage vượt 80%.
- **Bài học:** Bất kỳ tài nguyên nào tăng dần theo thời gian (log, cache file, session file) đều cần cơ chế giới hạn/dọn dẹp tự động — "chạy ổn định vài tuần" không có nghĩa là cấu hình đúng, chỉ là chưa tới ngưỡng vỡ.

### Sự cố 2: Chứng chỉ TLS hết hạn lúc nửa đêm, toàn bộ dịch vụ báo lỗi bảo mật
- **Bối cảnh:** Fresher cấu hình chứng chỉ SSL thủ công 1 lần lúc setup ban đầu, không có cơ chế gia hạn tự động.
- **Triệu chứng:** Đúng ngày hết hạn, mọi request HTTPS bị trình duyệt/client chặn với cảnh báo "certificate expired", toàn bộ hệ thống coi như sập với người dùng.
- **Nguyên nhân gốc:** Không có lịch nhắc hoặc tự động hóa gia hạn chứng chỉ, không ai theo dõi ngày hết hạn.
- **Cách sửa:** Dùng chứng chỉ tự động gia hạn (Let's Encrypt với certbot cron job, hoặc AWS Certificate Manager tự động gia hạn khi gắn với ALB/CloudFront); thêm cảnh báo khi chứng chỉ còn dưới 14 ngày.
- **Bài học:** Bất kỳ thứ gì "hết hạn theo thời gian" (cert, API key, domain) phải có cơ chế tự động gia hạn hoặc cảnh báo sớm — không được phép phụ thuộc vào trí nhớ con người.

### Sự cố 3: Rò rỉ AWS Access Key trên GitHub, tài khoản bị dùng để đào coin, hóa đơn hàng nghìn đô
- **Bối cảnh:** Fresher hardcode AWS Access Key/Secret Key trực tiếp trong code để test nhanh, commit nhầm lên GitHub public.
- **Triệu chứng:** Vài giờ sau nhận email cảnh báo từ AWS về "unusual activity", vào Billing thấy hàng trăm EC2 instance loại GPU mạnh được khởi tạo ở nhiều vùng lạ, hóa đơn ước tính lên tới hàng nghìn đô.
- **Nguyên nhân gốc:** Bot tự động quét GitHub tìm AWS key lộ, dùng ngay để khởi tạo instance đào tiền điện tử — quy trình này diễn ra tự động và cực nhanh, thường trong vòng vài phút tới vài giờ.
- **Cách sửa:** Revoke key ngay lập tức, liên hệ AWS Support trình bày (nhiều trường hợp được miễn/giảm phí do lỗi lộ key lần đầu), bật AWS GuardDuty và Billing Alert; **không bao giờ dùng Access Key tĩnh trong code** — dùng IAM Role (Instance Profile cho EC2, OIDC cho CI/CD).
- **Bài học:** Đây là sự cố phổ biến nhất và tốn kém nhất với người mới học cloud — chi phí không giới hạn ở mức "xóa key là xong", cần coi secret rò rỉ là sự cố bảo mật nghiêm trọng cần xử lý toàn diện.

---

## 🟡 JUNIOR — sự cố do cấu hình đúng theo hướng dẫn nhưng chưa hiểu hệ quả vận hành

### Sự cố 4: Docker image build kèm secret trong layer, dù đã "xóa" ở bước sau
- **Bối cảnh:** Junior copy file `.env` vào image ở 1 bước `COPY`, dùng xong rồi `RUN rm .env` ở bước sau trong cùng Dockerfile.
- **Triệu chứng:** Security scan phát hiện secret vẫn tồn tại trong image dù file đã bị xóa ở bước cuối.
- **Nguyên nhân gốc:** Mỗi lệnh trong Dockerfile tạo ra 1 layer riêng, layer cũ (chứa `.env`) vẫn được lưu lại trong image dù layer sau đó xóa file — Docker image là lịch sử các layer chồng lên nhau, không phải trạng thái cuối cùng duy nhất.
- **Cách sửa:** Không bao giờ copy secret vào image ở bất kỳ bước nào — dùng build secrets (`--secret` với BuildKit) hoặc truyền secret qua biến môi trường lúc container khởi chạy (runtime), không phải lúc build image.
- **Bài học:** Hiểu đúng cơ chế layer của Docker quan trọng hơn việc "biết viết Dockerfile chạy được" — nhiều lỗi bảo mật container xuất phát từ hiểu sai mô hình layer này.

### Sự cố 5: SSH trực tiếp vào server sửa lỗi khẩn, quên đồng bộ lại vào Infrastructure as Code
- **Bối cảnh:** Junior SSH vào EC2 sửa nhanh 1 dòng config lúc nửa đêm để hết lỗi ngay, không cập nhật lại Terraform/Ansible tương ứng.
- **Triệu chứng:** Vài ngày sau, lần deploy tiếp theo (chạy lại pipeline IaC) vô tình ghi đè lại cấu hình cũ, lỗi tái xuất hiện y hệt, mất công điều tra lại từ đầu.
- **Nguyên nhân gốc:** Thay đổi thủ công ngoài quy trình IaC tạo ra "configuration drift" — trạng thái thật của server không còn khớp với trạng thái được khai báo trong code hạ tầng.
- **Cách sửa:** Với sự cố khẩn cấp có thể sửa tay để dừng chảy máu ngay, nhưng BẮT BUỘC cập nhật lại IaC ngay sau đó trong cùng ca trực (hoặc ticket theo dõi rõ ràng nếu chưa kịp), coi server là "cattle not pet" — luôn có thể tái tạo lại y hệt từ code.
- **Bài học:** Sự tiện lợi của SSH sửa tay là cái bẫy — nó tạo cảm giác "đã xong" trong khi thực chất tạo ra nợ kỹ thuật vô hình sẽ gây sự cố lặp lại.

### Sự cố 6: Deploy nhầm config staging lên production do thiếu tách biệt environment
- **Bối cảnh:** Junior chạy nhầm pipeline deploy với biến môi trường trỏ tới database staging thay vì production (do đặt tên biến dễ nhầm lẫn, không có bước xác nhận).
- **Triệu chứng:** Dữ liệu test/rác từ staging xuất hiện trên production, hoặc ngược lại — mất niềm tin nghiêm trọng từ phía business.
- **Nguyên nhân gốc:** Không có sự tách biệt rõ ràng và xác nhận bắt buộc giữa các environment trong pipeline CI/CD (cùng 1 pipeline, chỉ khác biến môi trường, dễ chọn nhầm).
- **Cách sửa:** Tách pipeline/approval flow rõ ràng theo environment (production luôn cần approval thủ công từ người có quyền, hiển thị rõ đang deploy vào đâu), đặt tên tài nguyên/biến môi trường có tiền tố rõ ràng (`prod-`, `staging-`) khó nhầm lẫn.
- **Bài học:** An toàn vận hành không nên phụ thuộc vào "cẩn thận hơn" của từng cá nhân — phải thiết kế pipeline sao cho thao tác sai khó xảy ra hơn (safety by design), liên hệ [`04`](../04-CICD-Deployment-Strategies/README.md).

---

## 🔴 MID-LEVEL — sự cố do chưa lường hết tương tác giữa các thành phần hạ tầng

### Sự cố 7: Pod bị OOMKilled liên tục dù traffic không tăng
- **Bối cảnh:** Mid-level set `memory limit` cho pod dựa trên mức sử dụng RAM đo được lúc test, không có buffer.
- **Triệu chứng:** Pod bị Kubernetes kill (OOMKilled) và restart liên tục vào những thời điểm không có traffic bất thường, gây gián đoạn ngắt quãng khó tái hiện.
- **Nguyên nhân gốc:** Ứng dụng có garbage collector (VD: JVM, hoặc Python với 1 số thư viện) có xu hướng dùng RAM tiệm cận giới hạn được cấp trước khi dọn dẹp — memory limit đặt quá sát mức sử dụng bình thường khiến những đợt tăng RAM tạm thời bình thường (không phải rò rỉ) cũng bị kill.
- **Cách sửa:** Đặt memory limit có buffer hợp lý dựa trên theo dõi thực tế qua thời gian dài (không chỉ 1 lần test ngắn), tách biệt rõ `requests` (đảm bảo scheduler cấp đủ) và `limits` (giới hạn cứng), theo dõi biểu đồ memory usage theo thời gian trước khi chốt số.
- **Bài học:** Con số cấu hình resource không nên lấy từ 1 lần đo — phải quan sát pattern sử dụng thực tế theo thời gian, đặc biệt với ứng dụng có garbage collector.

### Sự cố 8: TTL DNS quá dài, chuyển server mới bị delay lan truyền nhiều giờ
- **Bối cảnh:** Mid-level lên kế hoạch migrate sang server mới, đổi DNS record trỏ sang IP mới, TTL cũ đang để 24 giờ.
- **Triệu chứng:** Sau khi đổi DNS, một bộ phận user vẫn kết nối vào server cũ (đã dừng) trong nhiều giờ, báo lỗi không truy cập được, dù DNS mới đã "cập nhật đúng".
- **Nguyên nhân gốc:** DNS resolver ở phía client/ISP cache bản ghi cũ theo đúng TTL đã khai báo trước đó — TTL càng dài, thời gian lan truyền thay đổi càng lâu, không có cách nào "ép" client cập nhật ngay.
- **Cách sửa:** Trước migration có kế hoạch, hạ TTL xuống thấp (VD: 60-300s) từ TRƯỚC đó vài ngày, đợi TTL cũ hết hạn lan truyền hoàn toàn rồi mới thực hiện đổi IP, giữ server cũ chạy song song 1 thời gian đệm sau khi đổi.
- **Bài học:** DNS thay đổi không "tức thời" — bất kỳ kế hoạch migrate/failover nào phụ thuộc vào đổi DNS đều phải tính trước thời gian lan truyền vào kế hoạch, không phải xử lý sau khi sự cố xảy ra.

### Sự cố 9: Tự khóa quyền của chính CI/CD pipeline khi siết IAM
- **Bối cảnh:** Mid-level áp dụng nguyên tắc least-privilege, thu hẹp IAM policy của role dùng cho CI/CD deploy.
- **Triệu chứng:** Pipeline deploy tiếp theo fail với lỗi "access denied" ngay ở bước cơ bản, không ai deploy được gì nữa, kể cả bản thân người vừa sửa policy.
- **Nguyên nhân gốc:** Thu hẹp quyền dựa trên đoán những action nào "cần thiết" thay vì kiểm tra thực tế đầy đủ các action pipeline thực sự dùng (bao gồm cả các action phụ như đọc metadata, describe resource trước khi update).
- **Cách sửa:** Dùng AWS IAM Access Analyzer / CloudTrail để xem chính xác các action đã thực sự được gọi trong 1 khoảng thời gian đủ dài trước khi viết policy thu hẹp, luôn test thay đổi IAM ở môi trường staging/role riêng trước khi áp cho pipeline chính, có "break-glass" account/role dự phòng không bị ảnh hưởng để khôi phục khi tự khóa nhầm.
- **Bài học:** Least-privilege là mục tiêu đúng nhưng phải làm dựa trên dữ liệu thực tế (observed actions), không dựa trên phỏng đoán — và luôn có kế hoạch dự phòng trước khi siết quyền của chính hệ thống vận hành.

---

## 🔵 SENIOR — sự cố ở tầm tổ chức, ảnh hưởng nhiều team/toàn bộ nền tảng

### Sự cố 10: Failover đa vùng chưa từng được test thật, khi cần dùng thì không hoạt động
- **Bối cảnh:** Hệ thống được thiết kế multi-region để chịu lỗi (disaster recovery), nhưng kế hoạch failover chỉ tồn tại trên tài liệu, chưa từng diễn tập thật.
- **Triệu chứng:** Khi vùng chính thật sự gặp sự cố (AWS region outage), quy trình failover thủ công mất nhiều giờ thay vì vài phút như tài liệu mô tả, do 1 bước phụ thuộc (DNS, quyền IAM ở vùng phụ, dữ liệu chưa đồng bộ đầy đủ) không hoạt động như kỳ vọng.
- **Nguyên nhân gốc:** "Có kế hoạch trên giấy" khác hoàn toàn với "đã kiểm chứng bằng thực hành" — các giả định trong kế hoạch (quyền truy cập, độ trễ đồng bộ dữ liệu, DNS TTL) chưa từng bị thử thách thật.
- **Cách sửa:** Thiết lập lịch diễn tập failover định kỳ (game day/chaos engineering) trong môi trường kiểm soát được, coi mỗi lần diễn tập là cơ hội tìm ra giả định sai trước khi sự cố thật xảy ra, tự động hóa càng nhiều bước trong quy trình failover càng tốt để giảm phụ thuộc vào thao tác thủ công lúc căng thẳng.
- **Bài học senior:** Độ tin cậy không nằm ở việc "có tài liệu kế hoạch" mà nằm ở việc **kế hoạch đó đã được kiểm chứng bằng thực hành thật** — đây là khác biệt giữa disaster recovery trên giấy và disaster recovery thật sự hoạt động.

### Sự cố 11: Chi phí cloud tăng không kiểm soát do thiếu cost governance ở tầm tổ chức
- **Bối cảnh:** Công ty scale nhanh, nhiều team tự tạo tài nguyên AWS riêng (NAT Gateway, EBS volume, Load Balancer) không theo chuẩn chung, không ai chịu trách nhiệm dọn dẹp tài nguyên không dùng nữa.
- **Triệu chứng:** Hóa đơn AWS tăng dần đều mỗi tháng dù lượng traffic/khách hàng không tăng tương ứng, không ai trong tổ chức biết chính xác khoản nào đang gây tốn kém.
- **Nguyên nhân gốc:** Thiếu tagging chuẩn (không biết tài nguyên nào thuộc team/dự án nào), thiếu quy trình review định kỳ, thiếu budget alert ở tầm account/tổ chức — mỗi team tối ưu chi phí cục bộ của mình (nếu có) nhưng không ai nhìn tổng thể.
- **Cách sửa:** Áp dụng chuẩn tagging bắt buộc (team, môi trường, dự án) qua policy tự động (AWS Organizations SCP), thiết lập budget alert theo từng team/tài khoản, review chi phí định kỳ hàng tháng ở cấp lãnh đạo kỹ thuật, tự động hóa việc phát hiện và dọn tài nguyên "mồ côi" (unattached EBS, idle load balancer).
- **Bài học senior:** Kiểm soát chi phí ở quy mô tổ chức là vấn đề QUY TRÌNH VÀ CƠ CHẾ (tagging, alert, review), không phải vấn đề "từng kỹ sư cẩn thận hơn" — liên hệ [`01`](../01-Cloud-Foundations-Real-Decisions/README.md).

### Sự cố 12: 1 database dùng chung cho 10 service, 1 migration lỗi làm sập toàn bộ nền tảng
- **Bối cảnh:** Nền tảng phát triển dần theo thời gian, nhiều microservice được thêm vào nhưng tất cả vẫn dùng chung 1 RDS instance "cho tiện quản lý".
- **Triệu chứng:** 1 migration của riêng 1 service (thêm index trên bảng lớn) chiếm dụng toàn bộ tài nguyên I/O của RDS instance trong migration, khiến CẢ 10 service khác cũng bị timeout hàng loạt dù không liên quan gì tới migration đó.
- **Nguyên nhân gốc:** Chia sẻ chung 1 điểm lỗi (single point of failure) giữa các service về mặt lý thuyết độc lập — kiến trúc "trông như microservices" nhưng thực chất có 1 tầng hạ tầng dùng chung tạo ra blast radius rất lớn.
- **Cách sửa:** Đây là quyết định kiến trúc lớn cần lộ trình: tách database theo service (ít nhất là instance riêng, không nhất thiết phải tách ngay ở mức schema), thiết lập giới hạn tài nguyên/connection pool riêng cho từng service dùng chung instance trong lúc chờ tách, review MỌI migration lớn có khả năng ảnh hưởng I/O trước khi chạy trên instance dùng chung.
- **Bài học senior:** Ranh giới "service độc lập" phải được đánh giá ở TẤT CẢ các tầng (code, database, hạ tầng) — độc lập ở tầng code nhưng chia sẻ chung tầng hạ tầng quan trọng vẫn tạo ra 1 điểm lỗi chung có thể sập cả nền tảng, đúng như bài học ở [`../Backend-Mastery/07`](../../Backend-Mastery/07-Real-World-War-Stories-Fresher-To-Senior/README.md) sự cố 12 về distributed monolith.

---

## 🎯 Cách dùng module này
Giống [`../Backend-Mastery/07`](../../Backend-Mastery/07-Real-World-War-Stories-Fresher-To-Senior/README.md) — dùng làm nguyên liệu kể chuyện phỏng vấn theo khung STAR, hoặc làm checklist rủi ro cần chủ động phòng tránh khi tự vận hành dự án cá nhân.

## 🔗 Liên kết
Chi tiết kỹ thuật liên quan: [`01`](../01-Cloud-Foundations-Real-Decisions/README.md) · [`02`](../02-Compute-Choices-EC2-Lambda-Containers/README.md) · [`03`](../03-Container-Orchestration-In-Practice/README.md) · [`04`](../04-CICD-Deployment-Strategies/README.md) · [`05`](../05-Observability-Incident-Response/README.md) · [`06`](../06-Junior-To-Senior-Problem-Playbook/README.md)
Sự cố tầng ứng dụng tương tự: [`../Backend-Mastery/07`](../../Backend-Mastery/07-Real-World-War-Stories-Fresher-To-Senior/README.md)
