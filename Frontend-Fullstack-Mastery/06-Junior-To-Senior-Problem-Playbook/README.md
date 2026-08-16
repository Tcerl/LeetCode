# 06. Lộ Trình Vấn Đề Thật: Từ Junior Đến Senior (Frontend & Kiến Trúc Dự Án)

> Tổng hợp lại các vấn đề đã nhắc ở Module 01-05, sắp xếp theo cấp độ để tự định vị và biết bước tiếp theo cần học.

---

## 🟢 Cấp độ Junior — "UI chạy đúng, chưa hiểu cơ chế bên dưới nên debug bằng thử-sai"

| Vấn đề gặp phải | Vì sao xảy ra | Cách vượt qua | Đọc thêm |
|---|---|---|---|
| Đổi state nhưng UI không cập nhật, sau khi destructure object reactive | Chưa hiểu cơ chế Proxy, destructuring làm mất liên kết reactive | Học cơ chế reactive, dùng `toRefs` khi cần destructure | [`01`](../01-Frontend-Architecture-And-Performance/README.md) |
| Gõ vào ô tìm kiếm, mỗi ký tự gọi 1 API, UI giật/server quá tải | Chưa có phản xạ debounce/throttle cho input người dùng | Luôn debounce input gọi API, học composable `useDebounce` | `06-Exercises/CODE_EXERCISES.md` VUE-05/06 |
| Validate dữ liệu chỉ ở frontend, tưởng vậy là đủ an toàn | Chưa phân biệt "validate cho UX" và "validate cho bảo mật" | Hiểu: validate frontend chỉ là UX, backend MỚI là lớp bảo mật thật | [`05-Practice-Lab`](../05-Practice-Lab/README.md) |
| Copy nguyên code demo (`services.py`, Manager pattern...) mà không hiểu vì sao viết vậy | Học theo mẫu mà chưa hỏi "tại sao" | Với mỗi pattern copy về, tự hỏi "nó giải quyết vấn đề gì, nếu bỏ đi thì sao" | [`03-Fullstack-Project-Architecture`](../03-Fullstack-Project-Architecture/README.md) |

**Bài học junior cần khắc cốt ghi tâm:** *Framework che giấu rất nhiều cơ chế phức tạp phía sau API đơn giản — hiểu cơ chế đó giúp debug bằng LÝ LUẬN thay vì thử-sai ngẫu nhiên.*

---

## 🟡 Cấp độ Mid-level — "Biết pattern đúng, nhưng bỏ sót case biên và race condition"

| Vấn đề gặp phải | Vì sao xảy ra | Cách vượt qua | Đọc thêm |
|---|---|---|---|
| Token hết hạn đúng lúc có nhiều API call song song → gọi refresh-token nhiều lần trùng lặp | Interceptor không kiểm soát request đang refresh, mỗi request 401 tự gọi refresh riêng | Dùng pattern hàng đợi (queue) các request đang chờ refresh hoàn tất | [`02`](../02-State-Management-And-Data-Fetching/README.md) |
| Bảng dữ liệu vài trăm dòng thì mượt, vài nghìn dòng bắt đầu giật/đơ | Chưa nghĩ tới virtual scroll khi danh sách có thể lớn | Luôn hỏi "danh sách này có thể lớn tới đâu trong thực tế?" trước khi chọn cách render | [`01`](../01-Frontend-Architecture-And-Performance/README.md) |
| 2 user cùng đăng ký username trùng nhau gần như đồng thời, cả 2 đều tạo được tài khoản | Chỉ check tồn tại rồi mới tạo (race condition), không có unique constraint ở DB | Luôn có ràng buộc DB làm lớp bảo vệ cuối cùng, không chỉ check ở application | [`03-Fullstack-Project-Architecture`](../03-Fullstack-Project-Architecture/README.md) |
| Hàm override (`write()` trong Odoo, custom Manager...) chạy sai khi được gọi với nhiều bản ghi/nhiều nơi khác nhau | Chỉ test với 1 bản ghi/1 luồng gọi, quên các luồng gọi khác (cron, import, API ngoài) | Luôn tự hỏi "hàm này còn được gọi từ đâu khác không, với input như thế nào" | [`03-Fullstack-Project-Architecture`](../03-Fullstack-Project-Architecture/README.md) |

**Bài học mid-level cần khắc cốt ghi tâm:** *Test thủ công LUÔN tuần tự (1 người, 1 thao tác 1 lúc) — bug đồng thời (race condition) chỉ xuất hiện ở quy mô thật, phải chủ động hình dung "nếu 2 việc xảy ra CÙNG LÚC thì sao".*

---

## 🔴 Cấp độ Senior — "Đánh giá kiến trúc tổng thể, dám phản biện thiết kế phức tạp không cần thiết"

| Vấn đề gặp phải (ở tầm hệ thống) | Senior xử lý thế nào | Đọc thêm |
|---|---|---|
| Dự án mới được thiết kế microservices ngay từ đầu dù chưa có traffic thật | Phản biện thẳng: đề xuất modular monolith trước, tách service khi có bằng chứng cần thiết (như case NexusFlow) | [`04-Real-World-Project-Case-Study`](../04-Real-World-Project-Case-Study/README.md) |
| Codebase có nhiều pattern không nhất quán (mỗi module tự chọn cách xử lý lỗi/state khác nhau) | Định ra chuẩn kiến trúc chung (coding convention, error handling pattern, state management rule), review để giữ nhất quán | [`02`](../02-State-Management-And-Data-Fetching/README.md), [`03`](../03-Fullstack-Project-Architecture/README.md) |
| Team liên tục gặp lại cùng loại bug (N+1, race condition, hydration mismatch) ở các tính năng khác nhau | Đưa vào checklist review bắt buộc + viết tài liệu nội bộ (như file playbook này) để cả team học từ 1 lần thay vì lặp lại | Toàn bộ Module 01-05 |
| Stakeholder yêu cầu tính năng phức tạp "cho tương lai" nhưng chưa có nhu cầu thật | Áp dụng nguyên tắc "thiết kế cho quy mô THẬT hiện tại, có đường mở rộng rõ ràng" — từ chối over-engineering có lý lẽ thuyết phục | [`04-Real-World-Project-Case-Study`](../04-Real-World-Project-Case-Study/README.md) |

**Bài học senior cần khắc cốt ghi tâm:** *Senior không phải người biết nhiều pattern nhất, mà là người biết KHI NÀO KHÔNG NÊN dùng 1 pattern phức tạp — dám nói "đơn giản hơn thì tốt hơn" và bảo vệ được quan điểm đó bằng lý lẽ kỹ thuật.*

---

## 🗺️ Lộ trình tổng hợp để tự đánh giá bản thân đang ở đâu

```
Junior  → UI/API chạy đúng theo happy path, debug bằng thử-sai khi có lỗi
            │ (dấu hiệu sẵn sàng lên Mid: hiểu được CƠ CHẾ bên dưới framework,
            │  debug bằng lý luận thay vì đoán)
            ▼
Mid     → Áp dụng đúng pattern, nhưng cần được nhắc mới nghĩ tới race condition/case biên
            │ (dấu hiệu sẵn sàng lên Senior: TỰ hình dung được case biên/đồng thời
            │  mà không cần ai nhắc, review code người khác phát hiện được các lỗi này)
            ▼
Senior  → Đánh giá và phản biện kiến trúc tổng thể, chủ động đơn giản hóa hệ thống,
          xây dựng chuẩn chung để cả team không lặp lại cùng 1 lớp lỗi
```

## 🔗 Liên kết
Chi tiết kỹ thuật: [`01`](../01-Frontend-Architecture-And-Performance/README.md) · [`02`](../02-State-Management-And-Data-Fetching/README.md) · [`03`](../03-Fullstack-Project-Architecture/README.md) · [`04`](../04-Real-World-Project-Case-Study/README.md) · [`05`](../05-Practice-Lab/README.md)
Ứng dụng vào phỏng vấn/kể chuyện senior: [`../Career-Mastery/`](../../Career-Mastery/INDEX.md)
