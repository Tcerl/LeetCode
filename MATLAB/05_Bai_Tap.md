# 📝 Bài Tập Thực Hành MATLAB

> Bộ bài tập từ dễ đến khó, với gợi ý và đáp án mẫu.

---

## 🟢 Cấp Độ 1: Cơ Bản (Tuần 1-4)

### BT01 - Bảng Cửu Chương
**Yêu cầu**: In bảng cửu chương từ 2 đến 9 ra Command Window theo dạng đẹp.

**Gợi ý**: Dùng vòng lặp `for` lồng nhau, `fprintf`.

```matlab
% Đáp án mẫu:
fprintf('=== BẢNG CỬU CHƯƠNG ===\n\n');
for m = 2:9
    fprintf('--- Bảng %d ---\n', m);
    for n = 1:10
        fprintf('%d x %d = %2d\n', m, n, m*n);
    end
    fprintf('\n');
end
```

---

### BT02 - Thống Kê Mảng
**Yêu cầu**: Viết hàm `array_stats(arr)` nhận vào mảng số, trả về:
- Tổng, trung bình, min, max
- Số phần tử dương, âm, bằng 0
- Phần trăm phần tử dương

**Kiểm tra**:
```matlab
arr = [-3, 7, 0, -1, 5, 2, -4, 0, 8];
[s, m, mn, mx, n_pos, n_neg, n_zero, pct] = array_stats(arr);
% s=14, m=1.556, mn=-4, mx=8, n_pos=4, n_neg=3, n_zero=2, pct=44.4%
```

```matlab
% Đáp án mẫu:
function [s, m, mn, mx, n_pos, n_neg, n_zero, pct] = array_stats(arr)
    s      = sum(arr);
    m      = mean(arr);
    mn     = min(arr);
    mx     = max(arr);
    n_pos  = sum(arr > 0);
    n_neg  = sum(arr < 0);
    n_zero = sum(arr == 0);
    pct    = n_pos / numel(arr) * 100;
end
```

---

### BT03 - Ma Trận Đặc Biệt
**Yêu cầu**: Viết hàm tạo các ma trận sau:
1. Ma trận Pascal n×n: `A(i,j) = C(i+j-2, i-1)` (tổ hợp)
2. Ma trận xoắn ốc (spiral matrix) n×n
3. Ma trận với `A(i,j) = gcd(i,j)`

```matlab
% Đáp án - Ma trận Pascal
function A = pascal_matrix(n)
    A = zeros(n);
    for i = 1:n
        for j = 1:n
            A(i,j) = nchoosek(i+j-2, i-1);
        end
    end
end

% Đáp án - Ma trận xoắn ốc
function A = spiral_matrix(n)
    A = zeros(n);
    num = 1;
    top = 1; bottom = n; left = 1; right = n;
    while num <= n^2
        for i = left:right,  A(top,i)    = num; num = num+1; end; top    = top+1;
        for i = top:bottom,  A(i,right)   = num; num = num+1; end; right  = right-1;
        for i = right:-1:left, A(bottom,i)= num; num = num+1; end; bottom = bottom-1;
        for i = bottom:-1:top, A(i,left)  = num; num = num+1; end; left   = left+1;
    end
end

% Kiểm tra
disp(pascal_matrix(4))
disp(spiral_matrix(4))
```

---

### BT04 - Đồ Thị Hàm Số
**Yêu cầu**: Vẽ trên cùng 1 figure với 4 subplot:
1. `f(x) = x*sin(x)` trên [-4π, 4π]
2. `f(x) = e^(-x²)` (Gaussian) với nhiều σ khác nhau
3. Đồ thị cực (polar) của `r = sin(3θ)` (hoa 3 cánh)
4. Đồ thị logarithm của `y = n!` với n=1..20

```matlab
% Đáp án mẫu:
figure('Position', [100 100 1000 800]);

% 1. x*sin(x)
ax1 = subplot(2,2,1);
x = linspace(-4*pi, 4*pi, 1000);
plot(x, x.*sin(x), 'b', 'LineWidth', 1.5);
xlabel('x'); title('x·sin(x)'); grid on;

% 2. Gaussian nhiều sigma
ax2 = subplot(2,2,2);
x2 = linspace(-5, 5, 500);
sigmas = [0.5, 1, 1.5, 2];
colors = lines(4);
for k = 1:4
    plot(x2, exp(-x2.^2/(2*sigmas(k)^2)), 'Color', colors(k,:), 'LineWidth', 1.5);
    hold on;
end
legend(arrayfun(@(s) sprintf('σ=%.1f',s), sigmas, 'UniformOutput',false));
title('Gaussian'); xlabel('x'); grid on; hold off;

% 3. Polar
ax3 = subplot(2,2,3);
theta = 0:0.01:2*pi;
r = sin(3*theta);
polarplot(theta, r, 'r', 'LineWidth', 2);
title('r = sin(3θ) - Hoa 3 cánh');

% 4. Factorial log
ax4 = subplot(2,2,4);
n = 1:20;
f = arrayfun(@factorial, n);
semilogy(n, f, 'gs-', 'LineWidth', 1.5, 'MarkerFaceColor', 'g');
xlabel('n'); ylabel('n! (log scale)'); title('Factorial (log scale)'); grid on;
```

---

### BT05 - Chuỗi Số
**Yêu cầu**: Viết hàm tính các chuỗi sau với N số hạng:
1. Chuỗi Leibniz: π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
2. Chuỗi Euler: e = 1 + 1/1! + 1/2! + 1/3! + ...
3. Chuỗi Basel: π²/6 = 1 + 1/4 + 1/9 + 1/16 + ...

Vẽ đồ thị hội tụ (sai số với giá trị thực theo N).

```matlab
% Đáp án:
function [vals, errors] = leibniz_pi(N)
    k = 0:N-1;
    terms = (-1).^k ./ (2*k+1);
    vals   = 4 * cumsum(terms);
    errors = abs(vals - pi);
end

N = 500;
[vals, errs] = leibniz_pi(N);
figure;
semilogy(1:N, errs, 'b');
xlabel('N số hạng'); ylabel('|Sai số|');
title('Hội tụ chuỗi Leibniz');
grid on;
```

---

## 🟡 Cấp Độ 2: Trung Cấp (Tuần 5-8)

### BT06 - Sắp Xếp Tự Viết
**Yêu cầu**: Implement các thuật toán sắp xếp và so sánh hiệu suất:
1. Bubble Sort
2. Merge Sort (đệ quy)
3. Quick Sort (in-place)

So sánh thời gian chạy với `sort` của MATLAB cho n = [100, 1000, 10000, 100000].

```matlab
% Merge Sort
function arr = merge_sort(arr)
    n = length(arr);
    if n <= 1, return; end
    mid   = floor(n/2);
    left  = merge_sort(arr(1:mid));
    right = merge_sort(arr(mid+1:end));
    arr   = merge(left, right);
end

function result = merge(L, R)
    result = [];
    i = 1; j = 1;
    while i <= length(L) && j <= length(R)
        if L(i) <= R(j)
            result = [result, L(i)]; i = i + 1;
        else
            result = [result, R(j)]; j = j + 1;
        end
    end
    result = [result, L(i:end), R(j:end)];
end

% Benchmark
sizes = [100, 1000, 10000, 100000];
times_merge  = zeros(size(sizes));
times_matlab = zeros(size(sizes));
for k = 1:length(sizes)
    n = sizes(k);
    arr = rand(1, n);
    tic; merge_sort(arr); times_merge(k)  = toc;
    tic; sort(arr);       times_matlab(k) = toc;
end

loglog(sizes, times_merge,  'r-o', 'DisplayName', 'Merge Sort');
hold on;
loglog(sizes, times_matlab, 'b-s', 'DisplayName', 'MATLAB sort');
legend; xlabel('n'); ylabel('Thời gian (s)'); title('So sánh sắp xếp');
```

---

### BT07 - Phân Tích Dữ Liệu CSV
**Yêu cầu**: Tạo file CSV mẫu về điểm học sinh và phân tích:

```csv
Name,Math,Physics,Chemistry,English,Biology
An,8.5,7.0,9.0,8.0,7.5
Binh,6.5,8.5,7.0,9.0,8.5
...
```

Yêu cầu:
1. Đọc dữ liệu
2. Tính GPA cho mỗi học sinh
3. Xếp hạng và phân loại (Xuất sắc/Giỏi/Khá/TB)
4. Vẽ biểu đồ phân phối điểm từng môn (boxplot)
5. Tính ma trận tương quan giữa các môn

```matlab
% Đáp án:
% Tạo dữ liệu mẫu trước
names = {'An','Binh','Cam','Dung','Em','Phuong','Giang','Hung','Mai','Nam'};
scores = max(0, min(10, randn(10,5)*1.5 + 7.5));
subjects = {'Math','Physics','Chemistry','English','Biology'};

T = array2table(scores, 'VariableNames', subjects);
T.Name = names';
T = [T(:,end), T(:,1:end-1)];
writetable(T, 'students.csv');

% Phân tích
T2 = readtable('students.csv');
score_mat = T2{:, 2:end};

% GPA
T2.GPA = mean(score_mat, 2);

% Xếp loại
T2.Grade = repmat("TB", height(T2), 1);
T2.Grade(T2.GPA >= 8.5) = "Xuất sắc";
T2.Grade(T2.GPA >= 7.0 & T2.GPA < 8.5) = "Giỏi";
T2.Grade(T2.GPA >= 6.5 & T2.GPA < 7.0) = "Khá";

% Boxplot phân phối điểm
figure;
boxplot(score_mat, subjects);
ylabel('Điểm'); title('Phân phối điểm từng môn');
grid on;

% Ma trận tương quan
figure;
C = corr(score_mat);
heatmap(subjects, subjects, C);
title('Ma trận tương quan'); colormap(parula);
```

---

### BT08 - Mô Phỏng Vật Lý
**Yêu cầu**: Mô phỏng chuyển động ném xiên:
- Nhập góc θ và vận tốc đầu v₀
- Tính và vẽ quỹ đạo, có tính đến lực cản không khí: `F_drag = -k*v`
- Tìm góc cho tầm bay xa nhất (có và không có cản)
- Animation quỹ đạo

```matlab
% Đáp án:
function [x, y, t] = throw_sim(v0, theta_deg, k, dt)
    % k: hệ số lực cản (0 = không có cản)
    g = 9.81;
    theta = theta_deg * pi/180;
    
    % ODE system: [x, y, vx, vy]
    state0 = [0; 0; v0*cos(theta); v0*sin(theta)];
    
    ode_func = @(t, s) [
        s(3);
        s(4);
        -k * s(3) * sqrt(s(3)^2 + s(4)^2);    % ax
        -g - k * s(4) * sqrt(s(3)^2 + s(4)^2)  % ay
    ];
    
    tspan = [0, 20];
    opts = odeset('Events', @(t,s) ground_event(t,s));
    [t, S] = ode45(ode_func, tspan, state0, opts);
    x = S(:,1); y = S(:,2);
end

function [value, isterminal, direction] = ground_event(t, s)
    value      = s(2);    % Dừng khi y = 0
    isterminal = 1;
    direction  = -1;      % Đang đi xuống
end

% Vẽ so sánh
figure;
angles = [30 45 60 75];
for a = angles
    [x1,y1] = throw_sim(50, a, 0,    0.01);
    [x2,y2] = throw_sim(50, a, 0.01, 0.01);
    plot(x1, y1, '-', x2, y2, '--');
    hold on;
end
legend(arrayfun(@(a) sprintf('%d° (no drag)', a), angles, 'UniformOutput',false));
xlabel('x (m)'); ylabel('y (m)'); title('Ném xiên: có/không lực cản');
grid on; ylim([0, inf]);
```

---

### BT09 - Xử Lý Tín Hiệu Audio
**Yêu cầu**: Tạo, xử lý và phân tích tín hiệu âm thanh:
1. Tổng hợp âm gồm nhiều tần số: `440Hz + 880Hz + 1320Hz`
2. Thêm nhiễu
3. Lọc để giữ lại 440Hz
4. Vẽ dạng sóng và phổ tần số trước/sau lọc

```matlab
% Đáp án:
fs = 44100;          % Sampling rate
duration = 2;        % 2 giây
t = 0:1/fs:duration-1/fs;

% Tổng hợp tín hiệu
f1 = 440;   A1 = 1.0;
f2 = 880;   A2 = 0.5;
f3 = 1320;  A3 = 0.3;
signal = A1*sin(2*pi*f1*t) + A2*sin(2*pi*f2*t) + A3*sin(2*pi*f3*t);

% Thêm nhiễu
noise  = 0.3 * randn(size(t));
noisy  = signal + noise;

% Thiết kế bộ lọc thông dải cho 440Hz
bw     = 100;   % Bandwidth
[b, a] = butter(8, [(f1-bw/2)/(fs/2), (f1+bw/2)/(fs/2)], 'bandpass');
filtered = filtfilt(b, a, noisy);

% Phổ tần số
N      = length(t);
freqs  = (0:N/2) * fs/N;

fft_noisy    = abs(fft(noisy))*2/N;
fft_filtered = abs(fft(filtered))*2/N;

% Vẽ kết quả
figure('Position', [100 100 1200 600]);

subplot(2,2,1);
plot(t(1:500), noisy(1:500));
title('Tín hiệu có nhiễu'); xlabel('t (s)'); ylabel('Biên độ');

subplot(2,2,2);
plot(freqs, fft_noisy(1:N/2+1));
title('Phổ tần số (có nhiễu)'); xlabel('f (Hz)');
xlim([0 2000]);

subplot(2,2,3);
plot(t(1:500), filtered(1:500));
title('Tín hiệu sau lọc (440Hz)'); xlabel('t (s)');

subplot(2,2,4);
plot(freqs, fft_filtered(1:N/2+1), 'r');
title('Phổ tần số (sau lọc)'); xlabel('f (Hz)');
xlim([0 2000]);

% Phát âm thanh (normalize)
% sound(filtered/max(abs(filtered)), fs);
```

---

## 🔴 Cấp Độ 3: Nâng Cao (Tuần 9-12)

### BT10 - OOP: Thư Viện Số Phức
**Yêu cầu**: Tự implement lớp `ComplexNum` mà không dùng kiểu complex built-in của MATLAB. Phải có:
- Properties: `real`, `imag`
- Overload: `+`, `-`, `*`, `/`, `abs`, `angle`, `conj`, `display`
- Phương thức: `toPolar()`, `fromPolar()`, `toStr()`
- Unit Tests

```matlab
% File: ComplexNum.m
classdef ComplexNum
    properties
        real_part
        imag_part
    end
    
    methods
        function obj = ComplexNum(r, i)
            if nargin < 2, i = 0; end
            obj.real_part = r;
            obj.imag_part = i;
        end
        
        function r = plus(a, b)
            r = ComplexNum(a.real_part + b.real_part, ...
                           a.imag_part + b.imag_part);
        end
        
        function r = mtimes(a, b)
            r = ComplexNum(a.real_part*b.real_part - a.imag_part*b.imag_part, ...
                           a.real_part*b.imag_part + a.imag_part*b.real_part);
        end
        
        function r = mrdivide(a, b)
            denom = b.real_part^2 + b.imag_part^2;
            r = ComplexNum((a.real_part*b.real_part + a.imag_part*b.imag_part)/denom, ...
                           (a.imag_part*b.real_part - a.real_part*b.imag_part)/denom);
        end
        
        function m = abs(obj)
            m = sqrt(obj.real_part^2 + obj.imag_part^2);
        end
        
        function a = angle(obj)
            a = atan2(obj.imag_part, obj.real_part);
        end
        
        function c = conj(obj)
            c = ComplexNum(obj.real_part, -obj.imag_part);
        end
        
        function s = toStr(obj)
            if obj.imag_part >= 0
                s = sprintf('%.4f + %.4fi', obj.real_part, obj.imag_part);
            else
                s = sprintf('%.4f - %.4fi', obj.real_part, abs(obj.imag_part));
            end
        end
        
        function disp(obj)
            fprintf('%s\n', obj.toStr());
        end
    end
    
    methods (Static)
        function obj = fromPolar(r, theta)
            obj = ComplexNum(r*cos(theta), r*sin(theta));
        end
    end
end

% Test
a = ComplexNum(3, 4);
b = ComplexNum(1, -2);
c = a * b;
fprintf('a = %s\n', a.toStr());
fprintf('|a| = %f\n', abs(a));
fprintf('a*b = %s\n', c.toStr());
```

---

### BT11 - Tối Ưu Hóa: Bài Toán Lập Lịch
**Yêu cầu**: Bài toán Knapsack (Cái túi):
- Có N vật phẩm với `weight[i]` và `value[i]`
- Túi chứa W kg tối đa
- Chọn vật nào để tối đa giá trị?

Implement: Dynamic Programming + Genetic Algorithm (Optimization Toolbox), so sánh kết quả.

```matlab
% DP solution  
function [max_val, selected] = knapsack_dp(weights, values, W)
    n = length(weights);
    dp = zeros(n+1, W+1);
    
    for i = 1:n
        for w = 0:W
            if weights(i) <= w
                dp(i+1,w+1) = max(dp(i,w+1), dp(i, w-weights(i)+1) + values(i));
            else
                dp(i+1,w+1) = dp(i,w+1);
            end
        end
    end
    
    max_val = dp(n+1, W+1);
    
    % Backtrack để tìm vật được chọn
    selected = false(1, n);
    w = W;
    for i = n:-1:1
        if dp(i+1,w+1) ~= dp(i,w+1)
            selected(i) = true;
            w = w - weights(i);
        end
    end
end

% GA solution
function [max_val, selected] = knapsack_ga(weights, values, W)
    n = length(weights);
    
    % Fitness function (penalty for exceeding capacity)
    fitness = @(x) -(x * values') + 1000 * max(0, x * weights' - W);
    
    opts = optimoptions('ga', 'PopulationSize', 100, 'MaxGenerations', 500, ...
        'Display', 'off');
    
    x_opt = ga(fitness, n, [], [], [], [], zeros(1,n), ones(1,n), ...
        [], 1:n, opts);  % Integer constraints
    
    selected = logical(x_opt);
    max_val  = selected * values';
end

% Test
rng(42);
n = 20;
weights = randi([1 10], 1, n);
values  = randi([1 20], 1, n);
W = 50;

[val_dp, sel_dp] = knapsack_dp(weights, values, W);
[val_ga, sel_ga] = knapsack_ga(weights, values, W);
fprintf('DP:  Value = %d, Weight = %d\n', val_dp, sum(weights(sel_dp)));
fprintf('GA:  Value = %d, Weight = %d\n', val_ga, sum(weights(sel_ga)));
```

---

### BT12 - Phân Tích Tín Hiệu EEG
**Yêu cầu**: Phân tích tín hiệu não EEG (mô phỏng):
1. Tạo tín hiệu EEG nhiều kênh (tổng hợp từ delta/theta/alpha/beta/gamma bands)
2. Lọc từng band
3. Tính power spectral density (PSD)
4. Phân tích tương quan giữa các kênh
5. Detect "spike" artifact bằng ngưỡng

```matlab
% Tạo EEG mô phỏng
fs = 256;  % 256 Hz
duration = 30;  % 30 giây
t = 0:1/fs:duration-1/fs;
n_channels = 8;

channels = {'FP1','FP2','F3','F4','C3','C4','P3','P4'};
EEG = zeros(n_channels, length(t));

for ch = 1:n_channels
    % Thêm các sóng não
    delta = 20 * sin(2*pi*2*t   + rand*pi);   % 2 Hz
    theta = 10 * sin(2*pi*6*t   + rand*pi);   % 6 Hz
    alpha = 30 * sin(2*pi*10*t  + rand*pi);   % 10 Hz
    beta  =  5 * sin(2*pi*20*t  + rand*pi);   % 20 Hz
    noise =  3 * randn(size(t));               % White noise
    EEG(ch,:) = delta + theta + alpha + beta + noise;
end

% Phân tích PSD
figure;
for ch = 1:n_channels
    [psd, f] = pwelch(EEG(ch,:), hamming(512), 256, 1024, fs);
    subplot(2,4,ch);
    plot(f, 10*log10(psd));
    xlim([0 50]); xlabel('f (Hz)'); ylabel('PSD (dB/Hz)');
    title(channels{ch}); grid on;
    % Vẽ đường phân chia bands
    xline([4 8 13 30], '--r');
end

% Tính Power theo bands
bands = struct('delta',[0.5 4],'theta',[4 8],'alpha',[8 13],...
               'beta',[13 30],'gamma',[30 80]);
band_names = fieldnames(bands);
power_table = zeros(n_channels, length(band_names));

for ch = 1:n_channels
    [psd, f] = pwelch(EEG(ch,:), hamming(512), 256, 1024, fs);
    for b = 1:length(band_names)
        range = bands.(band_names{b});
        idx   = f >= range(1) & f <= range(2);
        power_table(ch, b) = mean(psd(idx));
    end
end

T = array2table(power_table, 'VariableNames', band_names, 'RowNames', channels);
disp(T)
```

---

## 🔵 Cấp Độ 4: Dự Án (Tuần 13-16)

### BT13 - Dự Án: Nhận Diện Chữ Số
**Mô tả**: Xây dựng classifier nhận diện chữ số viết tay (MNIST dataset).

**Các bước**:
1. Load MNIST data (available từ MATLAB, hoặc download)
2. Visualize mẫu dữ liệu
3. Feature extraction: raw pixels + HOG features
4. Train classifier: KNN, SVM, Neural Network
5. Evaluate: accuracy, confusion matrix, per-class precision/recall
6. Visualize misclassifications

```matlab
% Step 1: Load data
% MATLAB có sample data: digitDatasetPath
digitDatasetPath = fullfile(toolboxdir('nnet'),'nndemos','nndatasets','DigitDataset');
imds = imageDatastore(digitDatasetPath, 'IncludeSubfolders', true, 'LabelSource', 'foldernames');

% Step 2: Visualize
figure;
perm  = randperm(numel(imds.Files), 20);
for i = 1:20
    subplot(4,5,i);
    imshow(imds.Files{perm(i)});
end

% Step 3: Train/Test split
[imdsTrain, imdsTest] = splitEachLabel(imds, 0.8, 'randomize');

% Step 4: Train CNN
layers = [
    imageInputLayer([28 28 1])
    convolution2dLayer(3, 32, 'Padding', 'same')
    batchNormalizationLayer
    reluLayer
    maxPooling2dLayer(2, 'Stride', 2)
    convolution2dLayer(3, 64, 'Padding', 'same')
    batchNormalizationLayer
    reluLayer
    maxPooling2dLayer(2, 'Stride', 2)
    flattenLayer
    fullyConnectedLayer(128)
    reluLayer
    dropoutLayer(0.5)
    fullyConnectedLayer(10)
    softmaxLayer
    classificationLayer
];

options = trainingOptions('adam', ...
    'MaxEpochs', 10, ...
    'MiniBatchSize', 64, ...
    'ValidationData', imdsTest, ...
    'ValidationFrequency', 30, ...
    'Verbose', false, ...
    'Plots', 'training-progress');

net = trainNetwork(imdsTrain, layers, options);

% Step 5: Evaluate
YPred = classify(net, imdsTest);
YTest = imdsTest.Labels;
accuracy = mean(YPred == YTest) * 100;
fprintf('Accuracy: %.2f%%\n', accuracy);

figure;
confusionchart(YTest, YPred);
```

---

### BT14 - Dự Án: Hệ Thống Điều Khiển PID
**Mô tả**: Mô phỏng xe tự lái đơn giản với điều khiển tốc độ PID.

```matlab
% Mô hình xe: m*dv/dt = F - b*v (quán tính + ma sát)
m = 1500;     % Khối lượng xe (kg)
b = 50;       % Hệ số ma sát
G = tf(1, [m b]);  % Transfer function: V(s)/F(s)

% PID controller
Kp = 800; Ki = 400; Kd = 10;
C = pid(Kp, Ki, Kd);

% Closed-loop
T = feedback(C*G, 1);

% Mô phỏng theo dõi tốc độ
t    = 0:0.01:30;
v_ref = 30 * (t >= 0) + 20 * (t >= 10) - 20 * (t >= 20);  % Reference speed

% Dùng lsim
[v_actual, t_out] = lsim(T, v_ref, t);

% Vẽ kết quả
figure;
subplot(2,1,1);
plot(t, v_ref, 'r--', t_out, v_actual, 'b', 'LineWidth', 2);
legend('Tốc độ mục tiêu', 'Tốc độ thực');
xlabel('t (s)'); ylabel('v (m/s)'); title('Điều khiển tốc độ xe');
grid on;

subplot(2,1,2);
error = v_ref - v_actual';
plot(t, error, 'g', 'LineWidth', 1.5);
xlabel('t (s)'); ylabel('Sai số (m/s)'); title('Sai số');
grid on;

% Thống kê
fprintf('Sai số RMS: %.4f m/s\n', rms(error));
fprintf('Sai số Max: %.4f m/s\n', max(abs(error)));
```

---

### BT15 - Dự Án: Dashboard Phân Tích Dữ Liệu
**Mô tả**: Tạo ứng dụng MATLAB App (App Designer) với:
- Load CSV data
- Visualize với nhiều loại đồ thị
- Thống kê mô tả tự động
- Export báo cáo PDF/PNG

```
Gợi ý từng bước:
1. Mở App Designer: appdesigner
2. Tạo UIFigure với các components:
   - UIButton: Load File
   - UIAxes: Vùng vẽ đồ thị
   - UITable: Hiển thị dữ liệu
   - UIDropDown: Chọn loại đồ thị
   - UIListBox: Chọn cột
3. Implement callbacks cho từng button/dropdown
4. Thêm export functionality
```

---

## 💡 Gợi Ý Chung

```matlab
% 1. Khi bắt đầu một project mới:
clc; clear; close all;
rng(42);  % Đặt seed ngẫu nhiên để kết quả reproducible

% 2. Luôn document hàm của bạn
function result = my_func(x, n)
    % MY_FUNC - Mô tả ngắn gọn
    %
    % Syntax: result = my_func(x, n)
    %
    % Input arguments:
    %   x - mô tả input x (kiểu dữ liệu, ràng buộc)
    %   n - mô tả input n
    %
    % Output arguments:
    %   result - mô tả kết quả trả về
    %
    % Example:
    %   r = my_func(5, 2);  % r = 25
    %
    % See also: related_function, another_func
    
    validateattributes(x, {'numeric'}, {'scalar'}, 'my_func', 'x', 1);
    result = x^n;
end

% 3. Test ngay sau khi viết
assert(my_func(5, 2) == 25);
assert(abs(my_func(3, 0.5) - sqrt(3)) < 1e-10);

% 4. Sử dụng diary để ghi log
diary('session_log.txt');
% ... run code ...
diary off;
```

---

## 📊 Bảng Tiến Độ Học Tập

| Bài tập | Kỹ năng luyện | Thời gian ước tính |
|---------|---------------|---------------------|
| BT01-02 | For loop, function, output nhiều | 1-2 giờ |
| BT03    | Ma trận, indexing | 2-3 giờ |
| BT04    | Đồ thị, subplot | 1-2 giờ |
| BT05    | Vectorization, plot | 2 giờ |
| BT06    | Đệ quy, benchmark | 3-4 giờ |
| BT07    | Table, file I/O, visualization | 3-4 giờ |
| BT08    | ODE, simulation | 4-5 giờ |
| BT09    | Signal processing | 4-5 giờ |
| BT10    | OOP, unit testing | 5-6 giờ |
| BT11    | Optimization | 4-5 giờ |
| BT12    | Spectral analysis | 5-6 giờ |
| BT13    | ML, CNN | 8-12 giờ |
| BT14    | Control systems | 6-8 giờ |
| BT15    | App Designer | 8-12 giờ |

---

*[⬅ 04_Ung_Dung.md](04_Ung_Dung.md) | [⬆ Về README](README.md)*
