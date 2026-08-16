# 01. Nền Tảng Tính Toán Số (Góc nhìn Senior/Kỹ sư thực chiến)

> Lý thuyết MATLAB chi tiết đã có ở [`06-Exercises/MATLAB/01_Co_Ban.md`](../../06-Exercises/MATLAB/01_Co_Ban.md) và [`02_Trung_Cap.md`](../../06-Exercises/MATLAB/02_Trung_Cap.md). File này bổ sung **vì sao các quy tắc đó tồn tại** — góc nhìn kỹ sư đã từng gặp sự cố tính toán thật, không chỉ cú pháp.

---

## 1. Vectorization — không phải "cho code gọn", mà là hiệu năng gấp hàng trăm lần

```matlab
% ❌ Vòng lặp for — MATLAB phải thông dịch (interpret) từng dòng lệnh cho mỗi phần tử
result = zeros(1, 1000000);
for i = 1:1000000
    result(i) = sin(i) * cos(i);
end

% ✅ Vectorized — MATLAB gọi thẳng thư viện số học tối ưu (BLAS/LAPACK) xử lý cả mảng 1 lần
i = 1:1000000;
result = sin(i) .* cos(i);
```

**Vì sao khác biệt lớn tới vậy trong thực tế:** MATLAB (giống NumPy trong Python) được xây trên các thư viện đại số tuyến tính đã tối ưu ở tầng thấp (C/Fortran, tận dụng SIMD của CPU). Vòng lặp `for` thông thường đi qua tầng thông dịch (interpreter) của MATLAB cho MỖI phần tử — chậm hơn vectorized code có thể tới **10-100 lần** với mảng lớn. Đây là bài học sống còn với kỹ sư xử lý tín hiệu/dữ liệu cảm biến thực tế: 1 file đo đạc vài triệu mẫu (sampling rate cao) mà xử lý bằng vòng lặp có thể mất hàng phút thay vì mili-giây.

---

## 2. Preallocation — lỗi hiệu năng "vô hình" khi mảng lớn dần

```matlab
% ❌ Mảng lớn dần trong vòng lặp — MỖI lần append, MATLAB phải cấp phát
% vùng nhớ MỚI lớn hơn và copy toàn bộ dữ liệu cũ sang (giống Array động ở
% DSA-Mastery/02, nhưng ở đây KHÔNG có amortized growth factor thông minh)
data = [];
for i = 1:100000
    data(end+1) = compute(i);   % Cấp phát lại + copy MỖI vòng lặp — O(n²) tổng thể
end

% ✅ Preallocate trước — cấp phát 1 lần duy nhất
data = zeros(1, 100000);
for i = 1:100000
    data(i) = compute(i);
end
```

**Liên hệ trực tiếp kiến thức Big O:** đây chính là bài học "Dynamic Array" ở [`DSA-Mastery/02`](../../DSA-Mastery/02-Linear-Structures-And-Hashing/README.md) áp dụng vào MATLAB — nhưng khác Python `list`/JS `Array` (có amortized growth), việc "grow" mảng kiểu `data(end+1) = x` trong MATLAB không được tối ưu tốt bằng, khiến vòng lặp tưởng O(n) thực chất chạy gần O(n²) với mảng lớn. Đây là lỗi hiệu năng **rất phổ biến và rất khó nhận ra** vì code vẫn chạy đúng kết quả, chỉ chậm dần một cách âm thầm.

---

## 3. Sai số dấu phẩy động (Floating Point) — bẫy so sánh kinh điển trong tính toán khoa học

```matlab
% ❌ So sánh trực tiếp 2 số thực — gần như LUÔN sai vì lỗi làm tròn nhị phân
if (0.1 + 0.2 == 0.3)
    disp('Bằng nhau')   % KHÔNG BAO GIỜ in ra dòng này!
end

% ✅ So sánh với sai số cho phép (tolerance)
tolerance = 1e-10;
if abs((0.1 + 0.2) - 0.3) < tolerance
    disp('Bằng nhau trong sai số cho phép')
end
```

**Vì sao đây là kiến thức bắt buộc với kỹ sư tính toán:** số thực (double) được lưu ở hệ nhị phân, không phải mọi số thập phân đều biểu diễn chính xác được (giống hệt lý do `0.1 + 0.2 !== 0.3` trong JavaScript/Python). Trong xử lý tín hiệu, mô phỏng vật lý, hay thuật toán tối ưu hóa lặp (iterative optimization), **so sánh trực tiếp bằng dấu `==`** để kiểm tra điều kiện dừng có thể khiến vòng lặp **chạy vô hạn** vì giá trị không bao giờ "bằng chính xác tuyệt đối" — luôn phải dùng ngưỡng sai số.

---

## 4. Ma trận: Row-major vs Column-major — nguồn gốc bug hiệu năng khi đổi ngôn ngữ

MATLAB lưu ma trận theo **column-major** (cột liền nhau trong bộ nhớ) — khác với C/Python NumPy mặc định **row-major** (hàng liền nhau). Đây không phải chi tiết vặt vãnh: duyệt ma trận SAI thứ tự so với cách lưu trong bộ nhớ làm giảm hiệu năng cache đáng kể (tương tự lý do Array nhanh hơn Linked List ở [`DSA-Mastery/02`](../../DSA-Mastery/02-Linear-Structures-And-Hashing/README.md) — cache locality).

```matlab
% ✅ Đúng cho MATLAB: duyệt theo CỘT trước (khớp cách lưu column-major)
for col = 1:size(M, 2)
    for row = 1:size(M, 1)
        process(M(row, col));
    end
end
```

**Ứng dụng thực tế:** khi kỹ sư chuyển thuật toán giữa MATLAB và Python/C (rất phổ biến khi đưa mô hình nghiên cứu MATLAB sang triển khai production bằng Python), quên đổi thứ tự duyệt ma trận là lỗi hiệu năng (và đôi khi cả lỗi logic khi reshape) rất hay gặp.

---

## 🎯 Câu hỏi kỹ sư senior hay đặt ra

1. "Đoạn code xử lý tín hiệu này có vector hóa được không, hay đang chạy vòng lặp không cần thiết?"
2. "Mảng kết quả có được preallocate trước khi lặp không?"
3. "Điều kiện dừng vòng lặp tối ưu có dùng so sánh dấu phẩy động trực tiếp không — có rủi ro chạy vô hạn không?"

## 🔗 Liên kết module khác
- Xử lý tín hiệu/ML ứng dụng thực tế → [`02-Signal-Processing-ML-In-Practice`](../02-Signal-Processing-ML-In-Practice/README.md)
- Độ phức tạp thuật toán nền tảng (Big O, Array) → [`../DSA-Mastery/`](../../DSA-Mastery/INDEX.md)
