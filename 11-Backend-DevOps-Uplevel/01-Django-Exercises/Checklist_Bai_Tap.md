# ✅ Checklist & Hướng Dẫn Thực Hành Chi Tiết Bài Tập Django (DJ-01 → DJ-07)

> **Mục tiêu:** Không chỉ tích dấu hoàn thành, mà qua mỗi bài tập bạn phải nắm rõ **bản chất hoạt động sâu bên trong (Deep-dive)** và **thực hành từng bước (Hands-on step-by-step)** để tự tin làm việc cũng như trả lời phỏng vấn Middle Backend Developer.
> Đánh dấu `[x]` khi hoàn thành và ghi lại ngày làm.

---

## 📌 Danh Sách Bài Tập
- [ ] **DJ-01 — Model & Migration** (Tuần 1)
- [ ] **DJ-02 — CRUD View cơ bản: FBV vs CBV** (Tuần 2)
- [ ] **DJ-03 — Query Tối Ưu & Xử Lý N+1 Query** (Tuần 3)
- [ ] **DJ-04 — Deep Comparison: Django vs Flask** (Tuần 4)
- [ ] **DJ-05 — DRF CRUD API với ViewSet & Router** (Tuần 6)
- [ ] **DJ-06 — Authentication JWT & Security Permissions** (Tuần 7)
- [ ] **DJ-07 — Unit Testing & API Integration Tests** (Tuần 8)

---

## 📘 HƯỚNG DẪN THỰC HÀNH CHI TIẾT & GIẢI THÍCH CHUYÊN SÂU

### 1. DJ-01 — Model & Migration
#### 🔬 Giải thích chuyên sâu:
- **Cơ chế Migration của Django:** Migration là hệ thống quản lý phiên bản (Version Control) cho schema database.
  - Khi chạy `python manage.py makemigrations`, Django sẽ so sánh trạng thái hiện tại của các file `models.py` với trạng thái được ghi nhận trong các file migration trước đó, từ đó sinh ra file `.py` mới trong folder `migrations/`.
  - Khi chạy `python manage.py migrate`, Django sẽ kiểm tra bảng `django_migrations` trong database để xem những migration nào chưa được áp dụng, sau đó dịch mã Python trong file migration thành các lệnh SQL tương ứng (`CREATE TABLE`, `ALTER TABLE`, `ADD CONSTRAINT`) và thực thi trong một Database Transaction.
  - **Foreign Key Indexing:** Khi khai báo `ForeignKey`, Django mặc định tự tạo một Index trên cột đó trong Database để tối ưu hiệu năng cho các truy vấn `JOIN`.

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Khởi tạo môi trường & project:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   pip install django
   django-admin startproject myproject .
   python manage.py startapp blog
   ```
2. **Khai báo Model (`blog/models.py`):**
   ```python
   from django.db import models

   class Author(models.Model):
       name = models.CharField(max_length=100)
       email = models.EmailField(unique=True)
       created_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return self.name

   class Post(models.Model):
       title = models.CharField(max_length=200)
       content = models.TextField()
       author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
       published_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return self.title
   ```
3. **Đăng ký App & Chạy Migration:**
   - Thêm `'blog'` vào `INSTALLED_APPS` trong `myproject/settings.py`.
   - Kiểm tra câu lệnh SQL thực sự sẽ chạy bằng `sqlmigrate`:
     ```bash
     python manage.py makemigrations blog
     python manage.py sqlmigrate blog 0001
     python manage.py migrate
     ```
4. **Tạo Superuser & Kiểm tra trong Django Admin:**
   - Đăng ký model trong `blog/admin.py`: `admin.site.register(Author)`, `admin.site.register(Post)`.
   - Chạy lệnh `python manage.py createsuperuser` và truy cập `http://127.0.0.1:8000/admin` để thêm 2 Author và 5 Post.

---

### 2. DJ-02 — CRUD View cơ bản (FBV vs CBV)
#### 🔬 Giải thích chuyên sâu:
- **Function-Based Views (FBV):** Đơn giản, rõ ràng, luồng xử lý (Control flow) hiển thị trực tiếp. Tuy nhiên dễ bị lặp code (boilerplate) khi xử lý form validation hoặc HTTP method checks (`if request.method == 'POST'`).
- **Class-Based Views (CBV):** Sử dụng tính đóng gói và kế thừa của OOP. 
  - `View.as_view()` chuyển đổi class thành một callable function có thể dùng trong `urls.py`.
  - CBV chia nhỏ luồng xử lý request thành các method (`get()`, `post()`, `form_valid()`, `get_queryset()`), giúp tái sử dụng mã nguồn bằng Mixins nhưng làm tăng độ phức tạp khi cần tùy biến logic sâu (Implicit flow).

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Viết FBV (`blog/views.py`):**
   ```python
   from django.shortcuts import render, get_object_or_404, redirect
   from .models import Post

   def post_list_fbv(request):
       posts = Post.objects.all()
       return render(request, 'blog/post_list.html', {'posts': posts})

   def post_detail_fbv(request, pk):
       post = get_object_or_404(Post, pk=pk)
       return render(request, 'blog/post_detail.html', {'post': post})
   ```
2. **Chuyển sang CBV kế thừa Generic Views (`blog/views.py`):**
   ```python
   from django.views.generic import ListView, DetailView, CreateView
   from django.urls import reverse_lazy

   class PostListView(ListView):
       model = Post
       template_name = 'blog/post_list.html'
       context_object_name = 'posts'

   class PostDetailView(DetailView):
       model = Post
       template_name = 'blog/post_detail.html'

   class PostCreateView(CreateView):
       model = Post
       fields = ['title', 'content', 'author']
       template_name = 'blog/post_form.html'
       success_url = reverse_lazy('post-list')
   ```
3. **Cấu hình `urls.py` & So sánh:**
   - Map đường dẫn trong `blog/urls.py`: `path('', PostListView.as_view(), name='post-list')`.
   - Đánh giá: Đếm số dòng code của FBV vs CBV và ghi chú trường hợp nên chọn từng loại.

---

### 3. DJ-03 — Query Tối Ưu & Xử Lý N+1 Query
#### 🔬 Giải thích chuyên sâu:
- **Hiện tượng N+1 Query:** Xảy ra khi lấy ra N bản ghi ở bảng chính (VD: 20 bài `Post`), sau đó trong vòng lặp (hoặc template) lại truy cập vào thuộc tính của quan hệ (VD: `post.author.name`). Khi đó Django ORM thực thi 1 query ban đầu để lấy danh sách Post + N query riêng lẻ để lấy Author cho từng Post -> Tổng cộng N+1 queries.
- **`select_related` vs `prefetch_related`:**
  - `select_related`: Dùng cho quan hệ **1-1** hoặc **N-1** (ForeignKey). Django sẽ tự động thực hiện SQL `INNER JOIN` hoặc `LEFT OUTER JOIN` để nạp toàn bộ dữ liệu liên quan trong **đúng 1 query duy nhất**.
  - `prefetch_related`: Dùng cho quan hệ **N-N** hoặc **1-N** reverse. Django chạy **2 query riêng biệt** (query 1 lấy danh sách chính, query 2 dùng `WHERE id IN (...)`) rồi thực hiện join bằng Python memory.

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Cài đặt Django Debug Toolbar:**
   ```bash
   pip install django-debug-toolbar
   ```
   - Thêm `'debug_toolbar'` vào `INSTALLED_APPS` và Middleware trong `settings.py`.
2. **Tạo View bị lỗi N+1:**
   ```python
   def unoptimized_posts(request):
       posts = Post.objects.all()[:20]  # Chưa nạp author
       return render(request, 'blog/posts_with_author.html', {'posts': posts})
   ```
   - Trong Template render: `{% for post in posts %}{{ post.title }} - {{ post.author.name }}{% endfor %}`.
   - Mở trình duyệt, kiểm tra Debug Toolbar: Thấy hiển thị **21 queries**!
3. **Tối ưu bằng `select_related`:**
   ```python
   def optimized_posts(request):
       posts = Post.objects.select_related('author').all()[:20]
       return render(request, 'blog/posts_with_author.html', {'posts': posts})
   ```
   - Mở lại trình duyệt: Số query giảm xuống chỉ còn **1 query JOIN duy nhất**!

---

### 4. DJ-04 — Deep Comparison: Django vs Flask
#### 🔬 Giải thích chuyên sâu:
- **Tư duy Kiến trúc (Architecture Philosophy):**
  - **Django (Batteries-included):** Cung cấp sẵn ORM, Admin Panel, Auth System, Migration Engine, Form Validation. Phù hợp cho ứng dụng lớn, monolithic hoặc CMS/Dashboard cần ra mắt nhanh.
  - **Flask (Micro-framework / Minimalist):** Chỉ cung cấp WSGI Router (Werkzeug) & Jinja2 Template Engine. Mọi thành phần khác (ORM, Auth, Migration) do developer tự lựa chọn thư viện độc lập ghép lại. Phù hợp cho Microservices, API chuyên biệt hoặc dự án yêu cầu linh hoạt tối đa.
- **Bảng so sánh chuyên sâu:**
  1. **Schema & ORM:** Django dùng Django ORM (Active Record Pattern - Object tự gọi `.save()`); Flask thường tích hợp Flask-SQLAlchemy (Data Mapper & Unit of Work Pattern - quản lý qua `db.session.commit()`).
  2. **Routing & Dispatch:** Django dùng `urls.py` với URL patterns phân tách rõ ràng + Class-Based Views (CBV); Flask dùng `@app.route()` decorators trực tiếp trên view functions + Blueprints.
  3. **Event & Extensions:** Django tích hợp sẵn hệ thống `Signals` (`post_save`, `pre_delete`); Flask dựa vào extensions độc lập (VD: `Blinker` hoặc gọi direct service functions).
  4. **Admin Dashboard:** Django có sẵn Django Admin sinh tự động từ Model; Flask yêu cầu cài `Flask-Admin` hoặc tự thiết kế API/Frontend.
  5. **Migration Management:** Django dùng hệ thống `makemigrations`/`migrate` built-in; Flask dùng `Flask-Migrate` (bọc quanh Alembic).

---

### 5. DJ-05 — DRF CRUD API với ViewSet & Router
#### 🔬 Giải thích chuyên sâu:
- **Django REST Framework (DRF) Architecture:**
  - **Serializer:** Đảm nhận vai trò 2 chiều: **Serialization** (chuyển đổi QuerySet/Model instance thành Python dict/JSON) và **Deserialization** (parse JSON đầu vào, validate dữ liệu via `is_valid()` và chuyển thành Model object via `save()`).
  - **ViewSet:** Gom toàn bộ logic CRUD (`list`, `create`, `retrieve`, `update`, `destroy`) vào một class duy nhất thay vì viết từng APIView riêng biệt.
  - **Router:** Tự động phân tích ViewSet và sinh ra các URL pattern chuẩn RESTful (`GET /api/posts/`, `POST /api/posts/`, `GET /api/posts/{id}/`).

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Cài đặt DRF & Khai báo Serializer (`blog/serializers.py`):**
   ```python
   from rest_framework import serializers
   from .models import Post, Author

   class AuthorSerializer(serializers.ModelSerializer):
       class Meta:
           model = Author
           fields = ['id', 'name', 'email']

   class PostSerializer(serializers.ModelSerializer):
       author_detail = AuthorSerializer(source='author', read_only=True)

       class Meta:
           model = Post
           fields = ['id', 'title', 'content', 'author', 'author_detail', 'published_at']
   ```
2. **Tạo ViewSet (`blog/views.py`):**
   ```python
   from rest_framework import viewsets
   from .models import Post
   from .serializers import PostSerializer

   class PostViewSet(viewsets.ModelViewSet):
       queryset = Post.objects.select_related('author').all()
       serializer_class = PostSerializer
   ```
3. **Cấu hình Router (`blog/urls.py`):**
   ```python
   from rest_framework.routers import DefaultRouter
   from .views import PostViewSet

   router = DefaultRouter()
   router.register(r'posts', PostViewSet, basename='post')

   urlpatterns = router.urls
   ```
4. **Kiểm tra API:** Dùng Postman hoặc cURL kiểm tra đủ 5 thao tác HTTP methods: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.

---

### 6. DJ-06 — Authentication JWT & Security Permissions
#### 🔬 Giải thích chuyên sâu:
- **Stateless Authentication với JWT (JSON Web Token):**
  - Khác với Session-based authentication (lưu session_id trên Server RAM/Redis), JWT lưu trữ thông tin identity của User trực tiếp trong chuỗi mã hóa Token (payload).
  - Cấu trúc JWT gồm 3 phần phân tách bởi dấu chấm: `Header.Payload.Signature`.
  - **Access Token:** Có thời gian sống ngắn (VD: 5-15 phút) dùng để xác thực request gửi kèm trong Header `Authorization: Bearer <token>`.
  - **Refresh Token:** Có thời gian sống dài hơn (VD: 1-7 ngày) dùng để lấy Access Token mới mà không bắt User đăng nhập lại.
  - **DRF Permission Classes:** Hoạt động trước khi View logic được gọi. DRF kiểm tra `request.user` và chạy qua danh sách permission (`IsAuthenticated`, `IsAdminUser`, hoặc Custom Permission).

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Cài đặt djangorestframework-simplejwt:**
   ```bash
   pip install djangorestframework-simplejwt
   ```
2. **Cấu hình Authentication trong `settings.py`:**
   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       )
   }
   ```
3. **Cấu hình JWT Endpoints (`myproject/urls.py`):**
   ```python
   from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

   urlpatterns += [
       path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
       path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   ]
   ```
4. **Áp dụng Permission cho ViewSet (`blog/views.py`):**
   ```python
   from rest_framework.permissions import IsAuthenticatedOrReadOnly

   class PostViewSet(viewsets.ModelViewSet):
       queryset = Post.objects.select_related('author').all()
       serializer_class = PostSerializer
       permission_classes = [IsAuthenticatedOrReadOnly]
   ```
5. **Verify:** Thử gửi `POST /api/posts/` không có Header token -> Trả về `401 Unauthorized`. Thử lấy token qua `POST /api/token/`, sau đó đính kèm Header -> Tạo Post thành công (`201 Created`).

---

### 7. DJ-07 — Unit Testing & API Integration Tests
#### 🔬 Giải thích chuyên sâu:
- **Triết lý Testing cho Backend:**
  - **Unit Test:** Kiểm tra một đơn vị code nhỏ nhất độc lập (VD: 1 function, 1 serializer validation rule).
  - **Integration Test:** Kiểm tra sự phối hợp giữa nhiều thành phần (URL + Middleware + View + Serializer + Database).
  - **Database Isolation:** Trong Django, khi chạy test (`python manage.py test` hoặc `pytest`), Django tự tạo một database giả lập hoàn toàn rỗng trong RAM/DB (`test_myproject`). Mỗi test case được bọc trong một Database Transaction và tự động `ROLLBACK` khi test kết thúc để đảm bảo dữ liệu không bị ảnh hưởng chéo giữa các bài test.

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Viết Integration Test cho API (`blog/tests.py`):**
   ```python
   from django.contrib.auth.models import User
   from rest_framework.test import APITestCase
   from rest_framework import status
   from .models import Author, Post

   class PostAPITestCase(APITestCase):
       def setUp(self):
           self.user = User.objects.create_user(username='testuser', password='password123')
           self.author = Author.objects.create(name='Nguyen Van A', email='a@example.com')
           self.post = Post.objects.create(title='Test Title', content='Test Content', author=self.author)

       def test_get_posts_list_unauthenticated(self):
           response = self.client.get('/api/posts/')
           self.assertEqual(response.status_code, status.HTTP_200_OK)
           self.assertEqual(len(response.data), 1)

       def test_create_post_unauthenticated_fails(self):
           data = {'title': 'New Post', 'content': 'Content', 'author': self.author.id}
           response = self.client.post('/api/posts/', data)
           self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

       def test_create_post_authenticated_success(self):
           self.client.force_authenticate(user=self.user)
           data = {'title': 'New Post', 'content': 'Content', 'author': self.author.id}
           response = self.client.post('/api/posts/', data)
           self.assertEqual(response.status_code, status.HTTP_201_CREATED)
           self.assertEqual(Post.objects.count(), 2)
   ```
2. **Chạy Test Suite & Xem Coverage:**
   ```bash
   python manage.py test blog
   # Hoặc dùng pytest
   pip install pytest pytest-django
   pytest
   ```

---

## 🎯 Bài Tập Nâng Cao & Management Command
1. **Phân trang (Pagination) & Filtering:**
   - Cấu hình `PageNumberPagination` và `DjangoFilterBackend` trong `PostViewSet` để hỗ trợ `GET /api/posts/?page=2&author=1`.
2. **Custom Management Command (`blog/management/commands/seed_data.py`):**
   ```python
   from django.core.management.base import BaseCommand
   from blog.models import Author, Post

   class Command(BaseCommand):
       help = 'Tự động tạo dữ liệu mẫu cho Author và Post'

       def handle(self, *args, **kwargs):
           author, _ = Author.objects.get_or_create(name='Seed Author', email='seed@example.com')
           for i in range(10):
               Post.objects.create(title=f'Seeded Post {i}', content='Auto generated', author=author)
           self.stdout.write(self.style.SUCCESS('Đã seed thành công 10 bài viết!'))
   ```
   - Chạy lệnh: `python manage.py seed_data`.

