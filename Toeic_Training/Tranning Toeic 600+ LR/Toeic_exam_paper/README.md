# 📝 TOEIC EXAM PAPER — Hệ thống đề

> Đã dọn (07/09/2026): bỏ 190 thư mục rỗng, chuyển 10 set AI cũ vào `_legacy/`.

---

## Cấu trúc

```
Toeic_exam_paper/
├── Set_001/ … Set_020/    ← ĐỀ FULL CHUẨN ETS: Listening 100 câu + Reading 100 câu = 200 câu
│   ├── listening.md       ← Part 1–4 (P1×6, P2×25, P3×39, P4×30), 100 câu + full script (KHÔNG có audio)
│   ├── reading.md         ← Part 5–7, 100 câu (101–200)
│   ├── answer_key.md      ← 200 đáp án + giải thích
│   └── notes.md           ← ghi chú sau khi làm
│
├── RC_Sets/RC_01 … RC_20/ ← Đề READING NGẮN: 40 câu (~30′), cày nhanh mỗi ngày
│
├── LC_Sets/               ← Buổi nghe: link nguồn thật + quy trình 3 lần chạm
│   ├── README.md          ← giao thức + tracker 20 buổi
│   └── LC_01/guide.md
│
├── html/                  ← BẢN HTML dễ đọc của cả 20 set (mở index.html) + build_html.py
└── _legacy/               ← 10 set AI cũ — LỆCH ĐÁP ÁN, chỉ tham khảo
```

> 📱 **Đọc trên điện thoại / máy tính:** mở `html/index.html`. Mỗi set 4 tab (Listening · Reading · Đáp án che sẵn · Ghi chú), chỉnh cỡ chữ, nền tối, in giấy. Sửa `.md` xong chạy lại `python3 Toeic_exam_paper/build_html.py`.

**Dùng cái nào khi nào:**
| Nhu cầu | Dùng |
|---|---|
| Thi thử đầy đủ chuẩn ETS (200 câu) cuối tuần | `Set_001`–`Set_020` (`reading.md` bấm giờ 75′; `listening.md` đọc script luyện P3/4) |
| Cày 30–40 phút mỗi ngày phần đọc | `RC_Sets/RC_01`–`RC_20` |
| Luyện NGHE thật (có audio) | `LC_Sets/` + `../Brain/audio_playlist.md` + Study4 |
| Full test LC+RC chấm điểm chuẩn | **Study4** (đề ETS thật) |

> ⚠️ Repo không chứa file audio (bản quyền ETS). Phần `listening.md` là **script + câu hỏi** để luyện đọc-hiểu Part 3/4 và logic Part 2; nghe thật thì theo link.

---

## Cách làm `Set_XXX`

1. **Reading:** bấm giờ **75 phút** cho `reading.md` (100 câu). Câu bí > 1 phút → chọn đại, đánh dấu `?`.
2. **Listening:** che script, đọc câu hỏi Part 3/4 trước, chọn đáp án `listening.md` (100 câu). Sau đó đọc lại script + đọc to (shadowing).
3. Chấm bằng `answer_key.md` → ghi `notes.md` + `../Brain/progress_log.md`.
4. Chép câu sai → `../Review/Error_Analysis/`.

---

## Bảng theo dõi — Set đầy đủ

| Set | Chủ đề | Ngày làm | L /100 | R /100 | Trạng thái |
|---|---|---|---|---|---|
| Set_001 | Office hỗn hợp | | | | ✅ có nội dung |
| Set_002 | Travel & Hospitality | | | | ✅ có nội dung |
| Set_003 | Finance & Banking | | | | ✅ có nội dung |
| Set_004 | Manufacturing & Logistics | | | | ✅ có nội dung |
| Set_005 | HR, Recruitment & Training | | | | ✅ có nội dung |
| Set_006 | Marketing & Advertising | | | | ✅ có nội dung |
| Set_007 | Technology & IT | | | | ✅ có nội dung |
| Set_008 | Retail & Customer Service | | | | ✅ có nội dung |
| Set_009 | Real Estate & Facilities | | | | ✅ có nội dung |
| Set_010 | Health & Medicine | | | | ✅ có nội dung |
| Set_011 | Environment & Science | | | | ✅ có nội dung |
| Set_012 | Media & Publishing | | | | ✅ có nội dung |
| Set_013 | Legal & Contracts | | | | ✅ có nội dung |
| Set_014 | Education & Training | | | | ✅ có nội dung |
| Set_015 | Food Service & Restaurants | | | | ✅ có nội dung |
| Set_016 | Construction & Development | | | | ✅ có nội dung |
| Set_017 | Energy & Utilities | | | | ✅ có nội dung |
| Set_018 | Nonprofit & NGO | | | | ✅ có nội dung |
| Set_019 | Government & Public Services | | | | ✅ có nội dung |
| Set_020 | Ôn tổng (mixed) | | | | ✅ có nội dung |

## Bảng theo dõi — RC_Sets (đề đọc ngắn)

| Đề | Chủ đề | Đúng /40 | TT |
|---|---|---|---|
| RC_01 | Office | | ⬜ |
| RC_02 | Travel | | ⬜ |
| RC_03 | Finance | | ⬜ |
| RC_04 | Manufacturing | | ⬜ |
| RC_05 | HR | | ⬜ |
