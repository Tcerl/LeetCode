# 03. Chiến Lược Trả Lời Phỏng Vấn Kỹ Thuật Theo Từng Mảng

> Câu hỏi cụ thể theo công nghệ đã có rất đầy đủ ở [`04-Interview-Prep/`](../../../04-Interview-Prep/) và [`interview_prep/`](../../../interview_prep/) (Python, Flask, Database, JS/Frontend, Docker/DevOps, Odoo, Vue/Laravel). File này bổ sung **cách trả lời có cấu trúc** để câu trả lời nghe "tầm senior" thay vì chỉ đúng.

---

## 1. Công thức trả lời câu hỏi lý thuyết — không chỉ định nghĩa suông

**Cấu trúc:** Định nghĩa ngắn gọn → **Ví dụ thực tế đã áp dụng** → **Tradeoff/giới hạn** → (nếu có) liên hệ sang chủ đề liên quan.

> Ví dụ câu hỏi: *"GIL trong Python là gì?"*
>
> ❌ **Trả lời junior:** "GIL là Global Interpreter Lock, nó khóa không cho nhiều thread chạy cùng lúc."
>
> ✅ **Trả lời senior:** "GIL đảm bảo chỉ 1 thread thực thi bytecode Python tại 1 thời điểm — nó KHÔNG ảnh hưởng tác vụ I/O-bound vì GIL được nhả trong lúc chờ I/O, nhưng làm threading vô dụng cho tác vụ CPU-bound. Trong dự án của em, khi cần resize hàng loạt ảnh (CPU-bound), em đã chuyển từ `ThreadPoolExecutor` sang `ProcessPoolExecutor` và thấy tốc độ tăng gần 4 lần trên máy 4 lõi — đúng như lý thuyết GIL dự đoán." *(xem chi tiết ở [`Backend-Mastery/02`](../../Backend-Mastery/02-Concurrency-And-Async-In-Production/README.md))*

**Vì sao cấu trúc này quan trọng:** người phỏng vấn senior không chỉ kiểm tra "biết định nghĩa" (dễ học thuộc) mà kiểm tra **đã thật sự áp dụng và hiểu giới hạn** của kiến thức đó chưa — đây chính là điều phân biệt trong câu trả lời.

---

## 2. Với câu hỏi "Tại sao chọn X thay vì Y" — luôn có ít nhất 2 tiêu chí so sánh

> Ví dụ: *"Tại sao chọn PostgreSQL thay vì MongoDB cho dự án này?"*
>
> Không trả lời 1 chiều "vì Postgres tốt hơn". Trả lời theo tiêu chí: *"Dự án có nhiều transaction liên bảng (đặt hàng phải trừ kho + tạo hóa đơn đồng thời) nên cần ACID mạnh — đây là điểm Postgres vượt trội. Nếu dự án là hệ thống log sự kiện ghi nhiều, ít quan hệ, em sẽ cân nhắc Mongo vì tối ưu ghi tốt hơn."* → Câu trả lời này cho thấy hiểu **cả 2 phía**, không chỉ thuộc lòng 1 đáp án — đúng khung quyết định ở [`Backend-Mastery/03`](../../Backend-Mastery/03-Database-Choice-And-Scaling-Playbook/README.md).

---

## 3. Với câu hỏi debug/troubleshooting — luôn trình bày theo QUY TRÌNH, không nhảy thẳng đáp án

> Ví dụ: *"API bị chậm đột ngột, bạn debug thế nào?"*

Trả lời theo đúng quy trình thật (đã có ở [`Backend-Mastery/04`](../../Backend-Mastery/04-Testing-Observability-And-Debugging-Prod/README.md)): "Đầu tiên em xem metrics — chậm từ lúc nào, có trùng với deploy gần nhất không. Sau đó xem có phải N+1 query hay connection pool cạn không qua slow query log. Nếu vẫn chưa rõ, em xem trace của 1 request cụ thể để biết thời gian rơi vào tầng nào..." — **trình bày tuần tự các bước** chứng minh có phương pháp thật, không phải đoán mò may rủi.

---

## 4. Bẫy thường gặp theo từng mảng (tổng hợp nhanh, chi tiết xem trong `04-Interview-Prep/`)

| Mảng | Bẫy hay gặp | Cách tránh |
|---|---|---|
| Python | Nhầm mutable default argument, nhầm `is` với `==` | Luôn giải thích được VÌ SAO xảy ra (tham chiếu bộ nhớ), không chỉ nhớ "phải tránh" |
| Database | Trả lời "index luôn tốt" mà không nhắc tới chi phí ghi | Luôn nêu tradeoff cả 2 chiều — xem [`Backend-Mastery/03`](../../Backend-Mastery/03-Database-Choice-And-Scaling-Playbook/README.md) |
| Docker/K8s | Không phân biệt được liveness vs readiness | Xem case study thật ở [`Cloud-DevOps-Mastery/03`](../../Cloud-DevOps-Mastery/03-Container-Orchestration-In-Practice/README.md) |
| Frontend/JS | Giải thích Event Loop mà không phân biệt microtask/macrotask | Luôn có ví dụ code minh họa thứ tự chạy thật |

---

## 🎯 Checklist trước khi vào phỏng vấn

1. Với mỗi công nghệ trong CV, mình có ít nhất 1 ví dụ THẬT đã áp dụng (không phải chỉ đọc tài liệu) không?
2. Mình có thể giải thích tradeoff của MỌI quyết định kỹ thuật mình từng đưa ra không?
3. Mình có chuẩn bị sẵn 2-3 câu hỏi ngược lại cho người phỏng vấn không? (dấu hiệu chủ động, quan tâm thật sự tới vai trò)

## 🔗 Liên kết module khác
- Khung trả lời cho câu hỏi system design (đề bài lớn, tổng hợp) → [`02-System-Design-Interview-Playbook`](../02-System-Design-Interview-Playbook/README.md)
- Chuẩn bị phần trả lời hành vi (behavioral) và đàm phán lương → [`04-Behavioral-And-Salary-Negotiation`](../04-Behavioral-And-Salary-Negotiation/README.md)
- Ngân hàng câu hỏi chi tiết theo công nghệ → [`04-Interview-Prep/`](../../../04-Interview-Prep/), [`interview_prep/`](../../../interview_prep/)
