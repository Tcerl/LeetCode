# 🌳 DSA-Mastery — Cây Kiến Thức Cấu Trúc Dữ Liệu & Giải Thuật (Senior Companion)

> **Mục đích:** Đây là lớp kiến thức **bổ sung** cho giáo trình gốc tại [`02-DSA-Curriculum/`](../02-DSA-Curriculum/), giúp bạn hiểu **vì sao hệ thống thật cần từng cấu trúc dữ liệu/thuật toán**, chúng đang chạy ở đâu trong các sản phẩm bạn dùng hàng ngày (Redis, Postgres, Kubernetes, Git, npm...), và senior dev xử lý các vấn đề thực tế liên quan như thế nào.
>
> **Không lặp lại** lý thuyết cơ bản đã có sẵn — mỗi file đều trỏ ngược về đúng mục tương ứng trong giáo trình gốc.
>
> **Phạm vi đợt này:** nhóm chủ đề "DSA & Thuật toán" (ưu tiên #1 trong 4 nhóm bạn chọn). Các nhóm còn lại (Backend: Database & Python | Cloud & DevOps | Phỏng vấn & Roadmap) sẽ được xây dựng tuần tự ở các đợt tiếp theo, theo đúng cấu trúc cây tương tự.

---

## 📋 MỤC LỤC

| # | Module | Chủ đề | Nguồn gốc lý thuyết |
|---|---|---|---|
| 00 | — | [Tổng quan cách dùng cây kiến thức này](#cách-sử-dụng-cây-kiến-thức-này) | — |
| 01 | [Foundations](01-Foundations/README.md) | Big O, Recursion — ngân sách hiệu năng & bẫy stack overflow thật | Giáo trình mục 1-2 |
| 02 | [Linear Structures & Hashing](02-Linear-Structures-And-Hashing/README.md) | Array, Linked List, Stack, Queue, Hash Table — LRU Cache, Rate Limiter, Consistent Hashing | Giáo trình mục 3-7 |
| 03 | [Trees, Heaps & Tries](03-Trees-Heaps-Tries/README.md) | BST/B-Tree (DB Index), Heap (Scheduler), Trie (Autocomplete) | Giáo trình mục 8-9, 11 |
| 04 | [Graphs & Union-Find](04-Graphs-And-Union-Find/README.md) | Dependency graph, Topological Sort (npm), Dijkstra, Fraud detection | Giáo trình mục 10, 19 |
| 05 | [Sorting & Searching](05-Sorting-And-Searching/README.md) | Timsort, cursor pagination, Binary Search on Answer | Giáo trình mục 12-13 |
| 06 | [Advanced Patterns](06-Advanced-Patterns/README.md) | Sliding Window (rate limiting), DP (diff/spellcheck), Greedy, Backtracking, Bit flags | Giáo trình mục 14-18, 20 |
| 07 | [Practice Lab](07-Practice-Lab/README.md) | Code review thật cho `20_exam_exercies/`, lộ trình luyện tập kiểu senior | `06-Exercises/`, Giáo trình mục 21-25 |
| 08 | [Junior-To-Senior Problem Playbook](08-Junior-To-Senior-Problem-Playbook/README.md) | Vấn đề thật + giải pháp, sắp xếp theo cấp độ Junior/Mid/Senior | Tổng hợp Module 01-07 |

---

## Cách sử dụng cây kiến thức này

1. **Học lý thuyết** ở [`02-DSA-Curriculum/`](../02-DSA-Curriculum/) trước — nắm vững cú pháp, cấu trúc, độ phức tạp cơ bản.
2. **Đọc module tương ứng** trong `DSA-Mastery/` để hiểu ứng dụng thật, bẫy production, và câu hỏi senior sẽ hỏi khi review code/thiết kế của bạn.
3. **Thực hành** theo [`07-Practice-Lab`](07-Practice-Lab/README.md) — vừa luyện đề, vừa tự review code của chính mình theo tiêu chuẩn senior.
4. Mỗi module đều có mục **🔗 Liên kết module khác** ở cuối — dùng để di chuyển giữa các chủ đề liên quan thay vì đọc tuyến tính.

---

## 🗺️ Sơ đồ liên hệ giữa các module

```
01-Foundations (Big O, Recursion)
        │  nền tảng cho toàn bộ complexity analysis
        ▼
02-Linear & Hashing ──┬──> 03-Trees/Heaps/Tries ──┬──> 04-Graphs & Union-Find
   (Array/List/Queue) │     (BST/Heap/Trie)       │     (DFS/BFS/Dijkstra/DSU)
                       │                            │
                       └────────────┬───────────────┘
                                     ▼
                    05-Sorting & Searching (Timsort/Binary Search)
                                     ▼
                    06-Advanced Patterns (Sliding Window/Two Pointers/
                                            DP/Greedy/Backtracking/Bit)
                                     ▼
                    07-Practice Lab (áp dụng tất cả vào code thật)
```

---

## 📌 Kế hoạch mở rộng tiếp theo (chưa thực hiện — chờ xác nhận theo từng đợt)

- [ ] **Backend: Database & Python** — gộp `03-Python-Expert/`, `04-Database-Mastery/`
- [ ] **Cloud & DevOps** — gộp `07-AWS-Mastery/`, `10-DevOps-Architect/`
- [ ] **Phỏng vấn & Roadmap** — gộp `01-Roadmaps/`, `04-Interview-Prep/`, `interview_prep/`
- [ ] **Frontend/Fullstack** — tái tổ chức phần Vue/Laravel hiện đang nằm lẫn trong `06-Exercises/CODE_EXERCISES.md`, `theory_mastery.md`, và `08-Frontend-Mastery/`
- [ ] Rà soát `09-Example-Projects/`, `05-Projects-Docs/` để xem có nội dung nào cần đưa vào cây kiến thức chung không

> Kiến thức mới phát sinh sẽ được thêm vào folder chung sẵn có nếu cùng chủ đề, hoặc tạo folder mới nếu là mảng kiến thức chưa có — theo đúng nguyên tắc bạn đã yêu cầu.
