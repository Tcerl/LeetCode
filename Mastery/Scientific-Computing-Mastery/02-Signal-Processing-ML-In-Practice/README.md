# 02. Xử Lý Tín Hiệu & Machine Learning Ứng Dụng (Góc nhìn Senior)

> Lý thuyết chi tiết đã có ở [`03_Nang_Cao.md`](../../06-Exercises/MATLAB/03_Nang_Cao.md) (OOP, Signal Processing, Parallel Computing) và [`04_Ung_Dung.md`](../../06-Exercises/MATLAB/04_Ung_Dung.md) (Machine Learning, Image Processing, Deep Learning, Simulink, Control System). File này bổ sung **cạm bẫy thực tế khi đưa mô hình nghiên cứu ra ứng dụng thật**.

---

## 1. Xử lý tín hiệu: Sampling Rate sai — lỗi kinh điển gây dữ liệu "ma" (Aliasing)

**Định lý Nyquist-Shannon:** để khôi phục đúng 1 tín hiệu, tần số lấy mẫu (sampling rate) phải **tối thiểu gấp đôi** tần số cao nhất có trong tín hiệu gốc. Vi phạm điều này gây ra **aliasing** — tín hiệu tần số cao "giả dạng" thành tín hiệu tần số thấp trong dữ liệu đo được, hoàn toàn sai với thực tế nhưng nhìn vẫn "hợp lý".

**Sự cố thật trong công nghiệp:** hệ thống giám sát rung động máy móc (vibration monitoring) lấy mẫu quá thấp so với tần số dao động thật của máy → dữ liệu hiển thị máy "rung nhẹ, ổn định" trong khi thực tế đang rung ở tần số nguy hiểm cao hơn nhiều — sai số này có thể dẫn tới bỏ lỡ cảnh báo hỏng hóc nghiêm trọng. Đây là lý do mọi hệ thống thu thập dữ liệu cảm biến thật (IoT, giám sát công nghiệp) đều phải tính toán sampling rate dựa trên **phổ tần số thực tế của tín hiệu cần đo**, không chọn tùy tiện.

```matlab
% Kiểm tra sampling rate có đủ trước khi triển khai hệ thống thật
fs = 1000;              % Tần số lấy mẫu (Hz)
f_signal_max = 400;     % Tần số cao nhất dự kiến trong tín hiệu (Hz)
if fs < 2 * f_signal_max
    error('Sampling rate không đủ theo Nyquist — dữ liệu sẽ bị aliasing!')
end
```

---

## 2. Machine Learning: Data Leakage — lỗi khiến mô hình "ảo tưởng" độ chính xác

**Sai lầm rất phổ biến kể cả ở người đã học ML:** chuẩn hóa dữ liệu (normalization/scaling) hoặc chọn feature **TRƯỚC KHI** tách tập train/test — khiến thông tin từ tập test "rò rỉ" vào quá trình huấn luyện, làm độ chính xác đo được cao giả tạo, nhưng mô hình thất bại thảm hại khi gặp dữ liệu thật hoàn toàn mới.

```matlab
% ❌ Data leakage: tính mean/std trên TOÀN BỘ dữ liệu trước khi tách train/test
data_normalized = (data - mean(data)) / std(data);
[trainData, testData] = splitData(data_normalized, 0.8);

% ✅ Đúng: tách train/test TRƯỚC, chỉ dùng thống kê của tập TRAIN để chuẩn hóa cả 2
[trainData, testData] = splitData(data, 0.8);
mu = mean(trainData); sigma = std(trainData);
trainData_norm = (trainData - mu) / sigma;
testData_norm = (testData - mu) / sigma;  % Dùng mu/sigma của TRAIN, không tính lại trên test
```

**Vì sao đây là lỗi nghiêm trọng trong thực tế:** mô hình báo cáo accuracy 95% trong nghiên cứu nhưng khi triển khai production chỉ đạt 60% — nguyên nhân rất thường là data leakage đã "cho mô hình nhìn trộm" thông tin tương lai trong lúc huấn luyện. Đây là câu hỏi bắt buộc trong mọi buổi review mô hình ML nghiêm túc: "pipeline xử lý dữ liệu có đảm bảo tách biệt hoàn toàn train/test ngay từ bước đầu tiên không?"

---

## 3. Deep Learning: Overfitting — mô hình "học thuộc lòng" thay vì "học hiểu"

Dấu hiệu nhận biết thật trong thực hành: loss trên tập train giảm liên tục, nhưng loss trên tập validation bắt đầu **tăng trở lại** sau một số epoch — mô hình đang "học thuộc" nhiễu của tập train thay vì học pattern tổng quát.

**Giải pháp senior áp dụng theo thứ tự ưu tiên thực tế:**
1. **Early Stopping:** dừng huấn luyện ngay khi validation loss bắt đầu tăng, không đợi hết số epoch định sẵn.
2. **Regularization (L2/Dropout):** phạt mô hình quá phức tạp, ép nó học pattern đơn giản/tổng quát hơn.
3. **Thêm dữ liệu hoặc data augmentation** (đặc biệt trong Image Processing) — thường hiệu quả hơn tinh chỉnh kiến trúc mô hình phức tạp hơn.
4. **Chỉ cuối cùng mới tăng độ phức tạp mô hình** — nguyên tắc ngược với trực giác của người mới: mô hình phức tạp hơn KHÔNG tự động tốt hơn nếu dữ liệu không đủ.

---

## 4. Simulink/Control System: Sai lệch giữa mô phỏng và hệ thống thật

**Vấn đề kinh điển trong kỹ thuật điều khiển:** bộ điều khiển (PID, tối ưu theo mô hình lý tưởng) hoạt động hoàn hảo trong Simulink nhưng dao động/mất ổn định khi chạy trên phần cứng thật. Nguyên nhân thường gặp: mô hình mô phỏng bỏ qua **độ trễ thực tế** của cảm biến/actuator, nhiễu đo lường thật, và sai số rời rạc hóa (discretization) khi chuyển từ hệ liên tục sang vi điều khiển số.

**Nguyên tắc senior khi đưa mô hình điều khiển ra thực tế:** luôn thêm mô hình nhiễu + độ trễ thật (dù ước lượng) vào mô phỏng TRƯỚC khi tự tin triển khai phần cứng, và luôn có cơ chế giới hạn an toàn (saturation limit, watchdog) độc lập với bộ điều khiển chính — phòng trường hợp mô hình lý thuyết sai lệch với thực tế.

---

## 🎯 Câu hỏi senior/kỹ sư thực chiến hay đặt ra

1. "Sampling rate của hệ thống đo này có đủ theo Nyquist cho tần số cao nhất thực tế cần đo không?"
2. "Pipeline ML này có tách train/test TRƯỚC khi chuẩn hóa dữ liệu không, hay đang bị data leakage?"
3. "Mô hình điều khiển đã tính tới độ trễ và nhiễu thật của phần cứng chưa, hay chỉ mô phỏng trong điều kiện lý tưởng?"

## 🔗 Liên kết module khác
- Nền tảng tính toán số (vectorization, sai số dấu phẩy động) → [`01-Numerical-Computing-Fundamentals`](../01-Numerical-Computing-Fundamentals/README.md)
- Lộ trình vấn đề junior→senior cho toàn mảng tính toán khoa học → [`03-Junior-To-Senior-Problem-Playbook`](../03-Junior-To-Senior-Problem-Playbook/README.md)
