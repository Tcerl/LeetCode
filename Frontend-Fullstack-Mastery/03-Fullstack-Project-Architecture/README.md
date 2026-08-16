# 03. Kiến Trúc Dự Án Fullstack — Review Code Thật Trong `09-Example-Projects/`

> Đây là review trực tiếp code mẫu trong [`09-Example-Projects/`](../../09-Example-Projects/) bằng con mắt senior — chỉ ra pattern nào đúng, pattern nào cần bổ sung để "chuẩn production" thật sự chứ không chỉ là boilerplate demo.

---

## 1. `Flask_SaaS_Boilerplate` — Service Layer Pattern đã đúng hướng

```python
# app/services.py — điểm SÁNG của boilerplate này
class UserService:
    @staticmethod
    def create_user(username, email, password):
        if User.query.filter_by(username=username).first():
            return None, "Username already exists"
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user, None
```

**Điểm đúng:** tách logic nghiệp vụ ra khỏi route (Controller) — đây chính là **Service Layer Pattern**, giúp route "mỏng" (chỉ nhận request, gọi service, trả response) và logic nghiệp vụ **test được độc lập** mà không cần dựng cả HTTP server.

**Điểm senior sẽ bổ sung để chuẩn production:**
1. **Return type không nhất quán** (`(user, None)` hoặc `(None, "error")`) — đây là pattern "tuple kết quả kiểu Go", nhưng Python có công cụ tốt hơn: custom Exception hoặc `Result`/`Either` type rõ ràng, tránh việc caller quên check phần tử thứ 2.
2. **Race condition tiềm ẩn:** giữa `filter_by(username=...).first()` (check tồn tại) và `db.session.add()` (tạo mới) — nếu 2 request đăng ký cùng username gần như đồng thời, CẢ HAI đều có thể pass qua bước check trước khi bước commit xảy ra → tạo ra 2 user trùng username. Fix đúng: unique constraint ở DB (không chỉ check ở application) + bắt `IntegrityError` khi commit.
3. **Không có transaction rollback khi lỗi:** nếu `set_password` throw exception giữa `add()` và `commit()`, session có thể ở trạng thái không nhất quán — nên bọc trong `try/except` với `db.session.rollback()`.

```python
# Bản sửa chuẩn senior hơn
from sqlalchemy.exc import IntegrityError

class UserService:
    @staticmethod
    def create_user(username, email, password):
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise UserAlreadyExistsError(username)  # custom exception rõ ràng
        return user
```

---

## 2. `Django_Rest_Pro` — Custom Manager đúng pattern, nhưng thiếu ngữ cảnh N+1

```python
# apps/articles/managers.py
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='published')
    def by_author(self, user):
        return self.filter(author=user)
```

**Điểm đúng:** đóng gói query logic thường dùng vào Manager thay vì lặp lại `Article.objects.filter(status='published')` khắp nơi trong codebase — nếu sau này đổi logic "published" (VD: thêm điều kiện `published_at <= now()`), chỉ sửa 1 chỗ.

**Điểm senior sẽ bổ sung:** đây chính xác là nơi nên **chặn N+1 query ngay từ manager** (liên kết trực tiếp [`Backend-Mastery/01`](../../Backend-Mastery/01-Request-Lifecycle-And-Architecture/README.md)) — nếu serializer sau đó luôn cần `article.author.name`, nên thêm `select_related` ngay tại manager để MỌI nơi gọi `published()` đều tự động tối ưu, thay vì để từng view tự nhớ thêm:

```python
def published(self):
    return self.filter(status='published').select_related('author')
```

---

## 3. `Odoo_Advanced_Module` — Override `write()` đúng nhưng thiếu 1 nguyên tắc quan trọng

```python
def write(self, vals):
    if 'state' in vals and vals['state'] == 'sale':
        self._message_log(body="Order confirmed by Senior Automation System.")
    return super(SaleOrder, self).write(vals)
```

**Điểm đúng:** gọi `super().write(vals)` — không quên gọi phương thức gốc (lỗi kinh điển khi override trong Odoo/Django là quên `super()`, làm mất toàn bộ logic mặc định của framework).

**Điểm senior sẽ bổ sung:**
- `write()` trong Odoo có thể được gọi với **nhiều record cùng lúc** (`self` là recordset, không phải 1 record) — code hiện tại chỉ đúng khi `self` có 1 bản ghi. Với nhiều bản ghi, `self._message_log()` sẽ log vào TẤT CẢ record dù chỉ 1 số record thật sự đổi sang `'sale'`. Bản sửa đúng cần `for record in self:` để xử lý từng bản ghi riêng, hoặc kiểm tra state cũ/mới cho từng record.
- Business logic quan trọng (như "log khi xác nhận đơn") nên cân nhắc đặt trong hook chuyên dụng của Odoo (`action_confirm`) thay vì `write()` chung chung — `write()` bị gọi bởi RẤT NHIỀU luồng khác nhau (import dữ liệu, cron job, API bên ngoài), dễ gây side effect không mong muốn ở những luồng không ngờ tới.

---

## 4. Bài học tổng quát rút ra từ cả 3 project — nguyên tắc chung khi review code fullstack

1. **Luôn hỏi "code này chạy đúng khi có 2 request đồng thời không?"** — race condition là lớp bug khó phát hiện nhất khi test thủ công (luôn test tuần tự) nhưng phổ biến nhất trên production thật.
2. **Đừng quên đường lỗi (error path)** — code demo thường chỉ có happy path, code production phải xử lý: DB lỗi, network timeout, dữ liệu không hợp lệ.
3. **Đặt tối ưu hóa (N+1, index) ở tầng thấp nhất có thể (Manager/Repository)** — để mọi nơi gọi tới đều tự động hưởng lợi, không phải nhớ tối ưu ở từng nơi sử dụng.

---

## 🎯 Câu hỏi senior hay hỏi khi review PR fullstack

1. "Nếu 2 user bấm nút này cùng lúc, kết quả có đúng không?"
2. "Hàm này có thể được gọi với nhiều bản ghi cùng lúc không — logic có còn đúng không?"
3. "Query trong Manager/Repository này có tự động tối ưu N+1 cho MỌI nơi gọi tới không?"

## 🔗 Liên kết module khác
- N+1 query, transaction, race condition chi tiết → [`../Backend-Mastery/01`](../../Backend-Mastery/01-Request-Lifecycle-And-Architecture/README.md), [`../Backend-Mastery/03`](../../Backend-Mastery/03-Database-Choice-And-Scaling-Playbook/README.md)
- Case study dự án lớn hơn (NexusFlow) → [`04-Real-World-Project-Case-Study`](../04-Real-World-Project-Case-Study/README.md)
