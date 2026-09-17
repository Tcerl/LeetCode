# 🧠 BRAIN — Hệ thống tư duy & chiến lược ôn luyện TOEIC

> **Mục tiêu dự án:** Đạt 600+ điểm TOEIC (Listening & Reading) thông qua luyện tập có hệ thống, đánh giá liên tục và mở rộng vốn từ vựng theo từng chủ đề.

---

## 📌 Mindset cốt lõi

| Nguyên tắc | Mô tả |
|---|---|
| **Consistency over Intensity** | Luyện tập đều đặn mỗi ngày quan trọng hơn học dồn |
| **Active Recall** | Không chỉ đọc đáp án — phân tích tại sao đúng / tại sao sai |
| **Spaced Repetition** | Ôn lại vocab và lỗi sai theo chu kỳ tăng dần |
| **Error-Driven Learning** | Mỗi lỗi sai là cơ hội học — review kỹ hơn luyện mới |
| **Progress Tracking** | Ghi lại điểm số và tiến độ theo tuần |

---

## 🗂️ Cấu trúc dự án

```
Tranning Toeic 600+ LR/
├── CONTENT_MANIFEST.md       ← Trạng thái nội dung: file nào có / đang chờ + "bắt đầu ở đâu"
├── Brain/                    ← Mindset, chiến lược, kế hoạch học tập
│   ├── README.md             ← File này
│   ├── study_plan.md         ← Kế hoạch sprint 8 tuần (chi tiết theo buổi)
│   ├── kickstart_14_days.md  ← Lịch TỪNG NGÀY cho 2 tuần đầu — bắt đầu ở đây
│   ├── materials.md          ← Nguồn đề + sách nên dùng
│   ├── audio_playlist.md     ← Link audio giọng thật, chia theo tuần
│   ├── diagnostic.md         ← Hướng dẫn làm đề chẩn đoán (tuần 1)
│   ├── vocab_system.md       ← Hệ thống học từ vựng theo chủ đề
│   └── progress_log.md       ← Nhật ký tiến độ, điểm số, full test
│
├── Drills/                   ← Ngân hàng câu theo Part — cày điện thoại, offline
│   ├── Part5_Grammar/        ← 01–06 xong (150 câu): từ loại, thì, hòa hợp, giới từ, liên từ, collocation
│   ├── Part2_QR/             ← 01 xong (WH-questions)
│   ├── Part6_TextCompletion/
│   └── Part7_Reading/        ← single / double / triple passage
│
├── Toeic_exam_paper/         ← Đề (đã dọn — xem README trong đó)
│   ├── RC_Sets/              ← Đề Reading (RC_01 = 40 câu, đáp án cân bằng)
│   ├── LC_Sets/              ← Guide nghe (link + quy trình 3 lần chạm)
│   └── _legacy/              ← 10 set AI cũ — lệch đáp án, chỉ tham khảo
│
└── Review/                   ← Chữa bài chi tiết, mở rộng vocab
    ├── README.md
    ├── Daily_Review/         ← Chữa bài ngày hôm đó
    ├── Vocab_Bank/           ← Ngân hàng từ vựng tích lũy
    └── Error_Analysis/       ← Phân tích lỗi sai theo dạng bài
```

---

## 📅 Lộ trình — SPRINT 8 TUẦN (07/09/2026 → cuối tháng 10/2026)

> Chi tiết: `study_plan.md` · Nguồn tài liệu: `materials.md` · Đề chẩn đoán: `diagnostic.md`

### Giai đoạn 1 — Nền tảng (Tuần 1–2)
- Đề chẩn đoán + vá gốc ngữ pháp (Part 5–6) + phản xạ nghe câu ngắn (Part 1–2)
- **Mục tiêu:** đề thử ~430–480

### Giai đoạn 2 — Tăng tốc từng phần (Tuần 3–5)
- Part 3–4 (dự đoán câu hỏi) + Part 7 (skim/scan) + vocab theo chủ đề
- 1 full test/tuần · **Mục tiêu:** đề thử ~520–570

### Giai đoạn 3 — Luyện đề & pacing (Tuần 6–8)
- 2–3 full test/tuần + review 100% câu sai + luyện nhịp Reading khít 75′
- **Mục tiêu:** 2 đề liên tiếp ≥ 620 → đăng ký thi

---

## 🎯 Chiến lược theo từng Part

### 🎧 Listening (Parts 1–4)
| Part | Tên | Chiến lược |
|---|---|---|
| Part 1 | Photographs | Quan sát kỹ chủ ngữ, trạng thái, vị trí đồ vật |
| Part 2 | Question-Response | Nhận dạng dạng câu (Wh-, Yes/No, Tag), cảnh giác bẫy |
| Part 3 | Conversations | Đọc câu hỏi TRƯỚC khi nghe, dự đoán context |
| Part 4 | Short Talks | Identify loại bài nói (announcement, report, ad...) |

### 📖 Reading (Parts 5–7)
| Part | Tên | Chiến lược |
|---|---|---|
| Part 5 | Incomplete Sentences | Phân tích từ loại, thì, cấu trúc ngữ pháp |
| Part 6 | Text Completion | Đọc toàn đoạn để hiểu context trước khi chọn |
| Part 7 | Reading Comprehension | Skim → locate keywords → scan chi tiết |

---

## 🔄 Quy trình luyện tập chuẩn (mỗi ngày)

```
BƯỚC 1 → Chọn bộ đề trong Toeic_exam_paper/
BƯỚC 2 → Làm bài trong điều kiện thi thật (thời gian chuẩn)
            Listening: 45 phút | Reading: 75 phút
BƯỚC 3 → Tự chấm điểm
BƯỚC 4 → Ghi điểm vào Brain/progress_log.md
BƯỚC 5 → Chữa bài chi tiết trong Review/Daily_Review/
BƯỚC 6 → Cập nhật Review/Vocab_Bank/ với từ mới
BƯỚC 7 → Phân tích lỗi sai vào Review/Error_Analysis/
```

---

## 📊 KPI theo dõi tiến độ

| Chỉ số | Cách theo dõi |
|---|---|
| Điểm tổng Listening + Reading | Ghi vào progress_log.md sau mỗi bài |
| Số từ vựng tích lũy | Đếm entries trong Vocab_Bank/ |
| Tỉ lệ lỗi sai theo Part | Xem Error_Analysis/ mỗi tuần |
| Chuỗi ngày luyện liên tiếp | Đánh dấu trong progress_log.md |
