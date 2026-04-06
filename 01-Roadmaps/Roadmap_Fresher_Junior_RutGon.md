# ROADMAP RÚT GỌN CHO FRESHER/JUNIOR (6-12 THÁNG)

Mục tiêu: Nắm vững nền tảng, build 2-3 dự án Full Stack, sẵn sàng vị trí Junior/Fresher.
Định hướng: Tập trung vào web (React + Node.js/Express + DB). Bỏ qua phần quá nâng cao.

NGUYÊN TẮC
- 70% thời gian thực hành, 30% đọc/ghi chú
- Mỗi ngày 3-5h code; cuối tuần 6-8h hoàn thiện dự án
- Ưu tiên hoàn thành dự án và code sạch hơn là học dàn trải

PHÂN KỲ THỜI GIAN
- Tháng 1-2: Nền tảng + JS/TS + Git
- Tháng 3: Frontend (React)
- Tháng 4: Backend (Node.js/Express) + DB
- Tháng 5: Full Stack dự án 1
- Tháng 6-7: Nâng giao diện + Testing + Deploy
- Tháng 8-9: Full Stack dự án 2 (có auth + upload + search + paginate)
- Tháng 10-12: Luyện thuật toán (vừa phải), tối ưu CV/Portfolio, phỏng vấn

## CHI TIẾT TỪNG THÁNG

THÁNG 1-2: NỀN TẢNG + JS/TS + GIT
- Học nhanh Python hoặc JavaScript cơ bản (chọn JS nếu muốn frontend mạnh)
- JS/TS: cú pháp ES6+, async/await, fetch, array methods (map/filter/reduce)
- Git: clone, branch, commit, push, pull, PR, resolve conflict
- HTML/CSS cơ bản: Flexbox, Grid, responsive
- Bài tập: Calculator, Todo CLI, 20-30 LeetCode Easy (Two Sum, Valid Parentheses, Merge Two Sorted Lists, Best Time to Buy/Sell Stock, etc.)

THÁNG 3: FRONTEND (REACT)
- React: component, props, state, hooks (useState/useEffect), list & forms
- React Router: routing cơ bản, params
- Fetch API + loading/error state
- Styling: CSS module hoặc Tailwind (chọn 1)
- Bài tập: Todo App React, Blog FE (list + detail), Form validation

THÁNG 4: BACKEND (NODE.JS/EXPRESS) + DATABASE
- Express: routes, middleware, error handling
- RESTful API: CRUD chuẩn, status code, pagination cơ bản
- Auth: JWT, password hashing (bcrypt)
- DB: MongoDB (Mongoose) hoặc PostgreSQL (Sequelize/knex) – chọn 1
- Bài tập: Blog API (posts/users), Auth (register/login), Upload file (multer hoặc S3 stub)

THÁNG 5: FULL STACK DỰ ÁN 1 (MVP)
- Đề xuất: Blog/E-commerce mini/Todo nâng cao
- Yêu cầu tối thiểu: Auth (JWT), CRUD chính, upload, search, paginate, UI responsive, deploy (Render/Vercel)
- Testing cơ bản: viết 3-5 test cho BE (supertest/jest) hoặc FE (RTL)

THÁNG 6-7: NÂNG GIAO DIỆN + TEST + DEPLOY
- UI/UX: responsive, loading skeleton, toast error/success
- State management: Context hoặc Redux Toolkit (chọn 1)
- Testing: Jest + React Testing Library; BE: supertest
- CI đơn giản: GitHub Actions (lint/test)
- Deploy: FE (Vercel/Netlify), BE (Render/Fly), DB managed (Mongo Atlas/Neon)

THÁNG 8-9: FULL STACK DỰ ÁN 2 (ĐẦY ĐỦ HƠN)
- Đề xuất: Task Manager/Booking System/Job Board nhỏ
- Bổ sung: role-based authorization, filter/sort nâng cao, cache đơn giản (Redis tùy chọn), gửi email (SendGrid/Mailgun sandbox)
- Viết README chuẩn, môi trường .env, script seed data

THÁNG 10-12: HOÀN THIỆN + PHỎNG VẤN
- Thuật toán: duy trì 100-150 LeetCode Easy/Medium (2-3 bài/ngày) – tập trung patterns (two pointers, sliding window, stack/queue, binary search)
- System design mức basic: REST, auth, scale đơn giản (cache + paginate + index DB), upload file
- Portfolio: 2 dự án chính + 1 dự án nhỏ, demo deploy, ảnh chụp màn hình, video ngắn
- CV: nêu rõ stack, link GitHub, link demo, mô tả tính năng, vai trò
- Mock interview: 3-5 buổi (coding + dự án + behavior)

CẮT GIẢM/BỎ QUA (CHƯA CẦN CHO JUNIOR)
- Advanced DS: AVL/Red-Black Tree, Trie, Segment Tree
- Advanced Algorithms: A*, Network Flow, KMP (chỉ biết khái niệm)
- Distributed systems, Microservices sâu: chỉ cần hiểu khái niệm; deploy monolith trước
- DevOps nặng (K8s, Terraform): chưa cần; dùng Docker + simple CI/CD đủ
- ML/AI, Low-level, Advanced OS, Cryptography sâu

ƯU TIÊN THỰC HÀNH (CHECKLIST NGẮN)
- Mỗi tuần: 1-2 feature hoàn chỉnh + 5-10 bài LeetCode
- Mỗi tháng: 1 bản release dự án (tag v1, v1.1…) với changelog
- Code review: tự review + nhờ bạn/senior review 1-2 PR/tháng
- Viết README và hướng dẫn setup cho mọi dự án

TÀI NGUYÊN RÚT GỌN
- FE: React docs, React Router docs, Tailwind/Chakra docs
- BE: Express docs, Mongoose/Sequelize docs, JWT, bcrypt
- DB: MongoDB manual hoặc PostgreSQL basics (CREATE TABLE, SELECT, JOIN, INDEX)
- Tools: Postman/Insomnia, GitHub Actions (template CI), Vercel/Render
- LeetCode patterns: Two Sum, Valid Parentheses, Merge Two Lists, Binary Search, Sliding Window (Longest Substring Without Repeating), Two Pointers (3Sum), Prefix Sum

BỘ BÀI TẬP MẪU
- FE: Todo App, Blog FE, Dashboard nhỏ (table + filter + pagination)
- BE: Blog API (auth + CRUD + paginate), Upload API (multer), Email stub
- FULL STACK: E-commerce mini, Task Manager, Booking mini

KẾT QUẢ MONG ĐỢI SAU 6-12 THÁNG
- 2-3 dự án Full Stack deploy được, có auth + CRUD + upload + search + paginate
- 100-150 bài LeetCode Easy/Medium (nắm patterns)
- Thành thạo Git/GitHub, quy trình PR cơ bản
- Biết viết test cơ bản (FE/BE), biết deploy
- CV/Portfolio rõ ràng, sẵn sàng phỏng vấn Junior/Fresher

HƯỚNG DẪN ÁP DỤNG FILE CHI TIẾT CŨ
- Dùng `Roadmap_Tang_Toc_Senior_FullStack.txt` làm tham khảo dài hạn
- Dùng `Roadmap_Chi_Tiet_Co_Vi_Du.txt` để xem code mẫu
- Lọc theo timeline rút gọn này, bỏ qua phần nâng cao (microservices sâu, system design nâng cao, mobile nếu chưa cần)

BẮT ĐẦU NGAY (TUẦN 1 - NGÀY 1)
- Setup Node.js + VS Code + Git
- Làm Calculator + Todo CLI
- Giải 3 bài LeetCode Easy
- Tạo GitHub, push code đầu tiên

---


# PHỤ LỤC: FRAMEWORK THỰC HÀNH (THEO NGÀY/TUẦN)


THÓI QUEN HẰNG NGÀY (TỐI THIỂU)
- 30–60 phút: 2 Easy hoặc 1 Medium LeetCode, ghi chú pattern.
- 2–4 giờ: Code features cho dự án (FE/BE/Full stack).
- 15 phút: Nhật ký ngắn (hôm nay làm gì, lỗi gì, mai làm gì).
- 15 phút: Dọn code, xem test/CI (nếu có).

LỊCH TUẦN MẪU (FRESHER/JUNIOR)
- Thứ 2–6:
  - Sáng: 1–2 LeetCode.
  - Chiều: 2–3h làm 1–2 feature nhỏ (Todo/Blog/E-com mini).
  - Tối: 30’ đọc docs (React/Express/Mongo/PG).
- Thứ 7: 4–6h hoàn thiện tính năng lớn hoặc refactor + test; cập nhật README/changelog.
- Chủ nhật: Nghỉ nhẹ, dọn repo, lập kế hoạch tuần tới.

LỘ TRÌNH DỰ ÁN (THỰC HÀNH THEO CẤP ĐỘ)
- Dự án 0 (Tuần 1–2): CLI nhỏ (Calculator, Todo CLI).
- Dự án 1 (Tháng 3): Todo/Blog FE (React + Router + fetch API mock).
- Dự án 2 (Tháng 4–5): Blog API (Express + Mongo/PG) + Auth JWT → Full Stack Blog.
- Dự án 3 (Tháng 6): E-commerce mini (Auth, CRUD, upload, search, paginate) + deploy.
- Dự án 4 (Tháng 8–9): Task/Booking/Job Board (role, filter/sort, email, cache nhẹ).
- Dự án 5 (Năm 2): Microservice/Performance/Design (khi đã vững monolith).

THANG KỸ NĂNG (ĐIỂM ĐẾN)
- Fresher (1–2 tháng): JS/TS cơ bản, Git, 20–30 LeetCode Easy, 1–2 mini app.
- Junior (3–9 tháng): 2 dự án Full Stack deploy được (auth/CRUD/upload/search/paginate), 80–150 LeetCode Easy/Medium.
- Mid (10–18 tháng): UI/UX tốt hơn, state management, testing, Docker/CI, dự án “production-ready”.
- Senior (18–24+ tháng): System Design cơ bản–TB, performance, security, review/mentoring, 200+ LeetCode patterns.

CHECKLIST MỖI THÁNG
- 1 bản release (tag v1.x) cho dự án chính.
- README rõ, .env.example, hướng dẫn run + deploy.
- 5–10 test FE + 5–10 test BE cho luồng quan trọng.
- 20–30 bài LeetCode/tháng.
- Ít nhất 1 tính năng “đủ xài” mỗi tuần (merge main).

KANBAN CỰC GỌN
- Backlog: auth, CRUD, upload, search, paginate, role…
- In Progress: tối đa 2–3 task.
- Review/Test: tự test hoặc nhờ bạn; viết test nhanh.
- Done: merge main, update README, changelog, deploy.

MODE TĂNG TỐC (nếu có thể)
- Ngày thường 6–8h: 2h thuật toán + 4–5h dự án + 30’ docs.
- Cuối tuần 6–8h: hoàn thiện tính năng + refactor + test + deploy.
- Mục tiêu 1 tháng: 1 release ổn, 20–30 LeetCode.

KẾT NỐI VỚI FILE CHI TIẾT
- Khi đến mốc (Todo React, Blog API, E-com…), mở `Roadmap_Chi_Tiet_Co_Vi_Du.txt`, tìm đúng section và làm theo code mẫu + bài tập.
- Không cần học hết một lượt; hãy học đến đâu, tra cứu đến đó.
