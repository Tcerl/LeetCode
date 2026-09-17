# 📱 Phiên bản HTML — 20 bộ đề

Bản HTML dễ đọc của toàn bộ `Set_001`–`Set_020`, sinh tự động từ các file `.md`.

## Dùng thế nào

- Mở `index.html` → chọn bộ đề.
- Mỗi bộ có 4 tab: **Listening · Reading · Đáp án · Ghi chú**.
- Tab **Đáp án** bị che, phải bấm nút mới hiện (tránh lỡ nhìn khi đang làm).
- Nút `A- / A+` chỉnh cỡ chữ, nút `◐` đổi nền sáng/tối — thiết lập được nhớ lại (localStorage).
- Mỗi file tự chứa (CSS/JS nhúng sẵn) → copy 1 file lẻ sang điện thoại vẫn chạy, không cần mạng.
- In ra giấy: Ctrl/Cmd + P — bản in tự bung hết 4 phần, ẩn thanh điều hướng.

> Xem trên GitHub: GitHub hiển thị *mã nguồn* HTML chứ không render. Muốn đọc đẹp thì tải repo về mở bằng trình duyệt, hoặc bật GitHub Pages trỏ vào thư mục này.

## Sinh lại sau khi sửa nội dung `.md`

```bash
python3 "Toeic_exam_paper/build_html.py"
```

Cần `pip install markdown` (một lần).
