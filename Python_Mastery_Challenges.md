# 🐍 PYTHON MASTERY CHALLENGES: FROM ZERO TO EXPERT

Bản danh sách này được thiết kế để giúp bạn nâng cấp trình độ Python từ mức độ cơ bản (Fundamentals) lên chuyên gia (Expert/Architect), bám sát lộ trình **Expert Mastery Roadmap** của bạn.

---

## 🟢 TIER 1: THE FOUNDATION (CƠ BẢN)
*Mục tiêu: Thành thạo cú pháp, kiểu dữ liệu và tư duy thuật toán cơ bản.*

1.  **Palindrome Checker:** Viết hàm kiểm tra một chuỗi có phải đối xứng không (bỏ qua khoảng trắng và ký tự đặc biệt).
    - *Kỹ năng:* String slicing, Regex, Two-pointers.
2.  **Frequency Dictionary:** Cho một danh sách từ, trả về dictionary chứa số lần xuất hiện của mỗi từ.
    - *Kỹ năng:* Dictionary manipulation, `collections.Counter`.
3.  **Basic CRUD with JSON:** Xây dựng một ứng dụng quản lý danh sách công việc (Todo List) lưu trữ dữ liệu vào file `.json`.
    - *Kỹ năng:* File I/O, Error handling (try-except), JSON module.
4.  **Prime Number Generator:** Viết hàm generator trả về các số nguyên tố từ 2 đến N.
    - *Kỹ năng:* Loops, Booleans, basic math logic.
5.  **LeetCode Recommendations:**
    - [Two Sum (1)](https://leetcode.com/problems/two-sum/)
    - [Valid Parentheses (20)](https://leetcode.com/problems/valid-parentheses/)

---

## 🟡 TIER 2: ADVANCED LOGIC & DS (TRUNG CẤP)
*Mục tiêu: Hiểu sâu về cấu trúc dữ liệu, độ phức tạp thuật toán và Clean Code.*

1.  **Custom Decorator for Logging:** Viết một decorator `@audit_log` để ghi lại thời gian thực thi và tham số đầu vào của bất kỳ hàm nào.
    - *Kỹ năng:* First-class functions, Decorators, `functools.wraps`.
2.  **LRU Cache Implementation:** Tự xây dựng một Least Recently Used (LRU) Cache mà không dùng `functools.lru_cache`.
    - *Kỹ năng:* Linked List + Dictionary, OOP.
3.  **Directory Tree Walker:** Viết script đệ quy để quét một thư mục và in ra cấu trúc cây của nó, hiển thị kích thước file.
    - *Kỹ năng:* Recursion, `os` or `pathlib` module.
4.  **Sudoku Solver:** Sử dụng thuật toán Backtracking để giải một bảng Sudoku 9x9.
    - *Kỹ năng:* Backtracking, Recursion.
5.  **LeetCode Recommendations:**
    - [Longest Substring Without Repeating Characters (3)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
    - [Merge Intervals (56)](https://leetcode.com/problems/merge-intervals/)

---

## 🔴 TIER 3: CONCURRENCY & OPTIMIZATION (CAO CẤP)
*Mục tiêu: Làm chủ AsyncIO, Multiprocessing và tối ưu hiệu suất thực tế.*

1.  **Async Web Scraper:** Viết script sử dụng `httpx` hoặc `aiohttp` để cào dữ liệu từ 50 trang web cùng một lúc.
    - *Kỹ năng:* `asyncio`, `await`, event loops, handling timeouts.
2.  **IMAGE Processor (Multiprocessing):** Viết chương trình resize 1000 ảnh trong một thư mục bằng cách tận dụng tất cả các nhân của CPU.
    - *Kỹ năng:* `multiprocessing.Pool`, GIL bypassing.
3.  **Memory-Efficient Scanner:** Đọc một file log cực lớn (vài GB) và đếm số lỗi mà không làm tràn RAM.
    - *Kỹ năng:* Generators (`yield`), Lazy evaluation, Context Managers.
4.  **Trie for Autocomplete:** Xây dựng cấu trúc dữ liệu Trie để hỗ trợ tính năng gợi ý từ khóa (autocomplete) với hiệu năng cao.
    - *Kỹ năng:* Advanced Trees, Memory usage optimization.
5.  **LeetCode Recommendations:**
    - [Trapping Rain Water (42)](https://leetcode.com/problems/trapping-rain-water/)
    - [Course Schedule (207)](https://leetcode.com/problems/course-schedule/)

---

## 👑 TIER 4: EXPERT & ARCHITECT (CHUYÊN GIA)
*Mục tiêu: Xây dựng hệ thống ổn định, bảo mật và có khả năng mở rộng.*

1.  **Distributed Rate Limiter:** Thiết kế một class xử lý Rate Limiting (ví dụ: tối đa 5 requests/giây) sử dụng Redis làm backend để dùng được cho nhiều instance ứng dụng.
    - *Kỹ năng:* Redis integration, Distributed systems, Sliding window algorithm.
2.  **Custom ORM Mockup:** Xây dựng một ORM đơn giản sử dụng Meta-programming để map các class Python vào các bảng SQL.
    - *Kỹ năng:* Metaclasses, `__getattr__`, `__setattr__`, introspection.
3.  **Message Queue Worker:** Xây dựng hệ thống Producer-Consumer đơn giản sử dụng RabbitMQ hoặc Redis Streams để xử lý các task background.
    - *Kỹ năng:* Message queues, Robustness (retry logic), Decoupling architecture.
4.  **Plugin System:** Thiết kế một ứng dụng có khả năng "hot-reload" các module plugin mà không cần restart server.
    - *Kỹ năng:* Dynamic imports (`importlib`), Registry patterns, Interface design.
5.  **LeetCode Recommendations (Hard/System Oriented):**
    - [Median of Two Sorted Arrays (4)](https://leetcode.com/problems/median-of-two-sorted-arrays/)
    - [Shortest Path in a Grid with Obstacles Elimination (1293)](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

---

## 💡 LỜI KHUYÊN ĐỂ TIẾN BỘ NHANH
1.  **Đừng chỉ giải bài tập:** Hãy viết Unit Test cho mọi hàm bạn viết (sử dụng `pytest`).
2.  **Code Review:** Sau khi giải xong, hãy lên mạng tìm giải pháp của người khác và so sánh về độ phức tạp (Time/Space Complexity).
3.  **Documentation:** Viết Docstring chuẩn (`reST` hoặc `Google style`) cho các bài toán từ Tier 2 trở lên.
4.  **Project Integration:** Hãy thử áp dụng bài toán Tier 4 (Rate Limiter) vào dự án **NexusFlow** trong roadmap của bạn.
