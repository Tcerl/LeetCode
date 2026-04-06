# 🔵 MATLAB Ứng Dụng

## Mục Lục
1. [Machine Learning với Statistics & ML Toolbox](#1-machine-learning)
2. [Xử Lý Ảnh (Image Processing)](#2-xử-lý-ảnh)
3. [Deep Learning Toolbox](#3-deep-learning)
4. [Simulink Cơ Bản](#4-simulink)
5. [Control System Toolbox](#5-control-system)
6. [Communications Toolbox](#6-communications)
7. [Data Analytics & Visualization](#7-data-analytics)

---

## 1. Machine Learning

> Cần **Statistics and Machine Learning Toolbox**

### 1.1 Phân Loại (Classification)

```matlab
% Load dữ liệu mẫu
load fisheriris
X = meas;        % 150x4: Sepal/Petal length/width
y = species;     % 150x1: setosa/versicolor/virginica

% Chia train/test (80/20)
cv = cvpartition(y, 'HoldOut', 0.2);
X_train = X(cv.training, :);
y_train = y(cv.training);
X_test  = X(cv.test, :);
y_test  = y(cv.test);

%% 1. K-Nearest Neighbors
knn = fitcknn(X_train, y_train, 'NumNeighbors', 5, ...
    'Standardize', true, 'Distance', 'euclidean');
y_pred = predict(knn, X_test);
accuracy_knn = mean(strcmp(y_pred, y_test)) * 100;
fprintf('KNN Accuracy: %.1f%%\n', accuracy_knn);

%% 2. SVM
svm = fitcecoc(X_train, y_train);  % One-vs-One SVM
y_pred_svm = predict(svm, X_test);

%% 3. Decision Tree
tree = fitctree(X_train, y_train, 'MaxNumSplits', 10);
view(tree, 'Mode', 'graph');  % Visualize tree

%% 4. Random Forest
rf = TreeBagger(100, X_train, y_train, 'Method', 'classification', ...
    'OOBPrediction', 'on');
figure; oobError(rf);  % Out-of-bag error

%% Confusion Matrix
c = confusionchart(y_test, y_pred);
c.Title = 'KNN Confusion Matrix';

%% Cross Validation
cv_model = crossval(knn, 'KFold', 5);
loss = kfoldLoss(cv_model);
fprintf('CV Loss: %.4f\n', loss);
```

### 1.2 Hồi Quy (Regression)

```matlab
% Dữ liệu mẫu
rng(42);
n = 200;
x = linspace(0, 10, n)';
y = 2*x + sin(x) + randn(n,1)*0.5;

%% 1. Linear Regression
mdl = fitlm(x, y);
disp(mdl)         % Thống kê chi tiết
figure;
plot(mdl)         % Scatter + fit line + CI

%% 2. Polynomial Regression
mdl_poly = fitlm(x, y, 'poly3');  % Degree 3

%% 3. Gaussian Process Regression (GPR)
gpr = fitrgp(x, y, 'KernelFunction', 'squaredexponential');
[y_pred, y_std] = predict(gpr, x);
figure;
plot(x, y, 'k.');
hold on;
plot(x, y_pred, 'b-', 'LineWidth', 2);
patch([x; flipud(x)], [y_pred-2*y_std; flipud(y_pred+2*y_std)], ...
    'b', 'FaceAlpha', 0.2, 'EdgeColor', 'none');
legend('Dữ liệu', 'Dự đoán', '95% CI');

%% 4. SVM Regression
svm_r = fitrsvm(x, y, 'Standardize', true, 'KernelFunction', 'rbf');

%% Metrics
y_hat = predict(mdl, x);
mse  = mean((y - y_hat).^2);
rmse = sqrt(mse);
mae  = mean(abs(y - y_hat));
r2   = mdl.Rsquared.Adjusted;
fprintf('RMSE=%.4f, MAE=%.4f, R²=%.4f\n', rmse, mae, r2);
```

### 1.3 Clustering

```matlab
X = [randn(50,2); randn(50,2)+5; randn(50,2)+[0,8]];

%% 1. K-Means
k = 3;
[idx, C, sumd] = kmeans(X, k, 'Replicates', 10);
figure;
gscatter(X(:,1), X(:,2), idx);
hold on; scatter(C(:,1), C(:,2), 200, 'k*'); title('K-Means');

%% 2. Hierarchical Clustering
Z = linkage(X, 'ward');
figure; dendrogram(Z, 0);
idx_h = cluster(Z, 'Maxclust', 3);

%% 3. DBSCAN
idx_db = dbscan(X, 1.5, 5);
% -1 = noise, 0 = unassigned, 1,2,... = cluster

%% 4. Gaussian Mixture Model
gm = fitgmdist(X, 3, 'Replicates', 5);
idx_gm = cluster(gm, X);
[~, ~, P] = cluster(gm, X);  % P: membership probabilities

%% Evaluation
eva = evalclusters(X, 'kmeans', 'silhouette', 'KList', 2:6);
plot(eva); title('Silhouette Score vs K');
```

### 1.4 Dimensionality Reduction

```matlab
load fisheriris;
X = meas;

%% PCA
[coeff, score, latent, ~, explained] = pca(X);
% coeff:    principal component directions
% score:    projected data
% latent:   eigenvalues
% explained:% variance explained

figure;
pareto(explained);  % Scree plot
title('Variance explained by each PC');

figure;
biplot(coeff(:,1:2), 'Scores', score(:,1:2), 'Labels', {'SL','SW','PL','PW'});

%% t-SNE (2D visualization)
Y = tsne(X, 'Perplexity', 30, 'NumDimensions', 2);
figure;
gscatter(Y(:,1), Y(:,2), species);
title('t-SNE Visualization');
```

---

## 2. Xử Lý Ảnh (Image Processing)

> Cần **Image Processing Toolbox**

### 2.1 Đọc, Hiển Thị, Lưu Ảnh
```matlab
% Đọc ảnh
img = imread('peppers.png');   % RGB image
gray = rgb2gray(img);          % Chuyển sang grayscale
info = imfinfo('peppers.png'); % Thông tin file

% Hiển thị
figure;
imshow(img);title('Ảnh gốc');

figure;
subplot(1,2,1); imshow(img);   title('RGB');
subplot(1,2,2); imshow(gray);  title('Grayscale');

% Lưu ảnh
imwrite(gray, 'gray_peppers.jpg', 'Quality', 90);
imwrite(img,  'output.png');
```

### 2.2 Xử Lý Ảnh Cơ Bản
```matlab
img = imread('cameraman.tif');

%% Điều chỉnh brightness/contrast
bright = imadjust(img, [0.3 0.7], [0 1]);  % Stretch contrast
gamma = imadjust(img, [], [], 0.5);         % Gamma correction
histeq_img = histeq(img);                   % Histogram equalization

% Xem histogram
figure;
subplot(1,2,1); imhist(img); title('Original');
subplot(1,2,2); imhist(histeq_img); title('After HE');

%% Cắt, Resize, Rotate
crop   = imcrop(img, [50 50 200 200]);  % [x y width height]
resized = imresize(img, 0.5);           % Scale 50%
resized2= imresize(img, [256 256]);     % Về 256x256
rotated = imrotate(img, 45);            % Xoay 45 độ
flipped = flip(img, 2);                 % Lật ngang
```

### 2.3 Lọc Ảnh
```matlab
img = imread('cameraman.tif');

%% Linear filters
h_avg = fspecial('average', 5);        % Averaging (blur)
h_gauss = fspecial('gaussian', 9, 2); % Gaussian blur σ=2
h_sharp = fspecial('unsharp', 0.5);   % Unsharp masking (sharpen)
h_laplace = fspecial('laplacian', 0.5);% Laplacian (edge)

img_blur   = imfilter(img, h_gauss, 'replicate');
img_sharp  = imfilter(img, h_sharp, 'replicate');

%% Nonlinear filters
img_med = medfilt2(img, [5 5]);        % Median (remove salt & pepper)

%% Thêm noise rồi lọc
noisy = imnoise(img, 'salt & pepper', 0.05);
denoised = medfilt2(noisy, [3 3]);
wiener_denoised = wiener2(noisy, [5 5]);

%% Frequency domain filtering
F = fft2(double(img));
F_shift = fftshift(F);
% ... apply frequency domain filter ...
img_filtered = real(ifft2(ifftshift(F_modified)));
```

### 2.4 Phát Hiện Biên (Edge Detection)
```matlab
img = imread('coins.png');
if size(img, 3) == 3
    gray = rgb2gray(img);
else
    gray = img;
end

%% Các phương pháp phát hiện biên
edge_sobel   = edge(gray, 'Sobel');
edge_canny   = edge(gray, 'Canny');         % Phổ biến nhất
edge_prewitt = edge(gray, 'Prewitt');
edge_log     = edge(gray, 'log');           % Laplacian of Gaussian

% Canny với tham số tùy chỉnh
edge_canny2  = edge(gray, 'Canny', [0.1 0.3], 2.0);  % threshold, sigma

figure;
subplot(2,3,1); imshow(gray);         title('Original');
subplot(2,3,2); imshow(edge_sobel);   title('Sobel');
subplot(2,3,3); imshow(edge_canny);   title('Canny');
subplot(2,3,4); imshow(edge_prewitt); title('Prewitt');
subplot(2,3,5); imshow(edge_log);     title('LoG');
```

### 2.5 Morphological Operations
```matlab
bw = edge_canny;
se = strel('disk', 3);   % Structuring element: disk radius 3
% Loại khác: 'square', 'line', 'rectangle', 'diamond'

dil  = imdilate(bw, se);   % Nở (dilation)
ero  = imerode(bw, se);    % Ăn mòn (erosion)
open = imopen(bw, se);     % Opening = erode then dilate (remove small objects)
clos = imclose(bw, se);    % Closing = dilate then erode (fill gaps)

%% Phân tích vùng liên thông
[labeled, n] = bwlabel(bw);         % Đánh nhãn vùng
props = regionprops(labeled, 'Area', 'Centroid', 'BoundingBox', 'Eccentricity');
areas = [props.Area];
large = labeled;
large(ismember(labeled, find(areas < 100))) = 0;  % Xóa vùng nhỏ
```

### 2.6 Phát Hiện Đối Tượng
```matlab
%% Phát hiện mặt người (Viola-Jones)
detector = vision.CascadeObjectDetector();  % Cần Computer Vision Toolbox
img = imread('visionteam.jpg');
bbox = step(detector, img);
img_ann = insertObjectAnnotation(img, 'rectangle', bbox, 'Face');
imshow(img_ann);

%% Phát hiện đường tròn
[centers, radii] = imfindcircles(gray, [20 100], ...
    'Sensitivity', 0.9, 'EdgeThreshold', 0.1);
imshow(gray); hold on;
viscircles(centers, radii, 'EdgeColor', 'r');
```

---

## 3. Deep Learning

> Cần **Deep Learning Toolbox**

### 3.1 Image Classification với CNN
```matlab
%% Tải pretrained model
net = resnet50;                    % ResNet-50 pretrained trên ImageNet
analyzeNetwork(net);               % Xem kiến trúc

%% Phân loại ảnh
img = imread('peppers.png');
img_resized = imresize(img, [224 224]);
label = classify(net, img_resized);  % Trả về categorical label
score = predict(net, img_resized);

%% Transfer Learning
imageFolder = 'my_dataset/';   % Thư mục ảnh phân loại theo subfolder
imds = imageDatastore(imageFolder, 'IncludeSubfolders', true, ...
    'LabelSource', 'foldernames');

% Chia train/val
[imds_train, imds_val] = splitEachLabel(imds, 0.8, 'randomize');

% Sửa lớp cuối
numClasses = numel(categories(imds.Labels));
layers = net.Layers;
layers(end-2) = fullyConnectedLayer(numClasses, 'Name', 'fc_new');
layers(end)   = classificationLayer('Name', 'output_new');

% Fine-tune
options = trainingOptions('adam', ...
    'InitialLearnRate', 1e-4, ...
    'MaxEpochs', 10, ...
    'MiniBatchSize', 32, ...
    'ValidationData', imds_val, ...
    'ValidationFrequency', 10, ...
    'Plots', 'training-progress', ...
    'ExecutionEnvironment', 'auto');

net_finetuned = trainNetwork(imds_train, layers, options);
```

### 3.2 Custom Neural Network
```matlab
% LSTM cho Time Series Classification
input_size  = 1;
hidden_size = 100;
num_classes = 3;

layers = [
    sequenceInputLayer(input_size)
    lstmLayer(hidden_size, 'OutputMode', 'last')
    dropoutLayer(0.3)
    fullyConnectedLayer(num_classes)
    softmaxLayer
    classificationLayer
];

% Hoặc dùng layerGraph cho skip connections
lg = layerGraph();
lg = addLayers(lg, inputLayer);
lg = addLayers(lg, hiddenLayer);
lg = connectLayers(lg, 'input', 'hidden');
```

### 3.3 Generative AI
```matlab
% Autoencoder
hiddenSize = 32;
autoenc = trainAutoencoder(X_train', hiddenSize, ...
    'MaxEpochs', 400, ...
    'L2WeightRegularization', 0.001, ...
    'SparsityRegularization', 4, ...
    'SparsityProportion', 0.05);

encoded   = encode(autoenc, X_test');
decoded   = decode(autoenc, encoded);
mse_recon = mean((X_test' - decoded).^2, 'all');
```

---

## 4. Simulink

### 4.1 Giới Thiệu Simulink
```
Simulink là môi trường mô phỏng dạng block diagram cho hệ thống động.

Mở Simulink:
1. Gõ: simulink  trong Command Window
2. Hoặc: Ctrl+Shift+N để tạo model mới

Các thành phần chính:
- Sources:  tín hiệu vào (Sine Wave, Step, Constant...)
- Math:     phép toán (Gain, Sum, Product...)
- Sinks:    quan sát kết quả (Scope, To Workspace, Display...)
- Continuous: khối liên tục (Integrator, Derivative, Transfer Fcn...)
- Discrete: khối rời rạc (Unit Delay, Zero-Order Hold...)
```

### 4.2 Tạo Model Từ MATLAB Code
```matlab
% Tạo Simulink model từ code (không cần GUI)
model = 'my_model';
new_system(model);
open_system(model);

% Thêm blocks
add_block('simulink/Sources/Sine Wave', [model '/Sine']);
add_block('simulink/Math Operations/Gain', [model '/Gain']);
add_block('simulink/Sinks/Scope', [model '/Scope']);

% Cấu hình parameters
set_param([model '/Sine'], 'Amplitude', '1', 'Frequency', '2*pi');
set_param([model '/Gain'], 'Gain', '2');

% Kết nối blocks
add_line(model, 'Sine/1', 'Gain/1');
add_line(model, 'Gain/1', 'Scope/1');

% Tự động sắp xếp
Simulink.BlockDiagram.arrangeSystem(model);

% Chạy mô phỏng
set_param(model, 'StopTime', '10');
sim(model);

% Lưu model
save_system(model, 'my_model.slx');
```

### 4.3 Chạy Mô Phỏng và Lấy Dữ Liệu
```matlab
% Cấu hình simulation
simIn = Simulink.SimulationInput('my_model');
simIn = setModelParameter(simIn, 'StopTime', '20', 'Solver', 'ode45');
simIn = setVariable(simIn, 'Kp', 1.5);  % Set workspace variables

% Chạy
simOut = sim(simIn);

% Lấy kết quả
t  = simOut.tout;           % Vector thời gian
x  = simOut.yout{1}.Values; % Signal đầu tiên
y  = simOut.logsout.get('output_signal').Values.Data;
```

---

## 5. Control System

> Cần **Control System Toolbox**

### 5.1 Transfer Function và State Space
```matlab
%% Transfer function: G(s) = (s+1) / (s^2 + 3s + 2)
num = [1 1];         % Tử số
den = [1 3 2];       % Mẫu số
G = tf(num, den);    % Tạo transfer function object
G2 = zpk([-1], [-1 -2], 1);  % Zeros-Poles-Gain form

%% State space
A = [-3 -2; 1 0]; B = [1;0]; C = [0 1]; D = 0;
sys_ss = ss(A, B, C, D);

%% Chuyển đổi
G_ss   = tf(sys_ss);        % ss -> tf
sys_ss2 = ss(G);             % tf -> ss
[z, p, k] = tf2zpk(num, den);% tf -> zpk

%% Phân tích
pole(G)              % Cực: [-1, -2]
zero(G)              % Không: [-1]
dcgain(G)            % DC gain: G(0) = 0.5
bandwidth(G)         % Bandwidth
```

### 5.2 Phân Tích Hệ Thống
```matlab
G = tf([1], [1 2 1]);     % G(s) = 1/(s+1)^2

%% Đáp ứng thời gian
step(G);           % Step response
impulse(G);        % Impulse response
lsim(G, u, t);     % Với input tùy ý

%% Thông số hiệu suất
info = stepinfo(G);
fprintf('Rise Time: %.3f s\n', info.RiseTime);
fprintf('Settling Time: %.3f s\n', info.SettlingTime);
fprintf('Overshoot: %.1f%%\n', info.Overshoot);
fprintf('Peak: %.3f\n', info.Peak);

%% Phân tích tần số
bode(G);           % Bode plot: magnitude + phase
nyquist(G);        % Nyquist plot
nichols(G);        % Nichols chart
margin(G);         % Gain & phase margin
[Gm, Pm, Wgm, Wpm] = margin(G);
fprintf('GM=%.2f dB, PM=%.2f deg\n', 20*log10(Gm), Pm);

%% Ổn định
isstable(G)           % 1 nếu ổn định
rlocus(G);            % Root locus
[r, k] = rlocus(G);   % Roots và gain
```

### 5.3 Thiết Kế Bộ Điều Khiển
```matlab
G = tf([1], [1 2 1]);

%% PID tuning
C_pid = pidtune(G, 'PID');         % Auto PID tuning
pidTuner(G, C_pid);                % GUI PID Tuner (interactive!)

%% Pole placement (state feedback)
sys = ss([-2 -1; 1 0], [1;0], [0 1], 0);
desired_poles = [-3+2i, -3-2i];   % Nơi đặt cực mong muốn
K = place(sys.A, sys.B, desired_poles);  % State feedback gain

%% LQR (Linear Quadratic Regulator)
Q = eye(2);       % State cost matrix
R = 0.1;          % Control cost
K_lqr = lqr(sys, Q, R);

%% Closed-loop analysis
T_pid = feedback(G * C_pid, 1);   % Closed-loop với PID
step(T_pid, G);                   % So sánh
legend('Với PID', 'Vòng hở');
```

---

## 6. Communications Toolbox

```matlab
%% Modulation/Demodulation
M = 16;           % 16-QAM
data = randi([0 M-1], 1000, 1);

% QAM modulation
tx = qammod(data, M, 'UnitAveragePower', true);

% AWGN channel
SNR_dB = 20;
rx = awgn(tx, SNR_dB, 'measured');

% Demodulation
rx_data = qamdemod(rx, M, 'UnitAveragePower', true);

% Bit error rate
[errors, BER] = biterr(data, rx_data);
fprintf('BER = %.6f\n', BER);

%% Constellation diagram
cd = comm.ConstellationDiagram;
cd(rx);

%% BER vs SNR curve
snr_range = 0:2:30;
ber_theory = berawgn(snr_range, 'qam', M);
plot(snr_range, log10(ber_theory), 'b-o');
xlabel('SNR (dB)'); ylabel('log10(BER)');
grid on;
```

---

## 7. Data Analytics & Visualization

### 7.1 Table Operations
```matlab
% Tạo table
T = table({'Alice';'Bob';'Cathy'}, [25;30;22], [85.5;92.0;78.3], ...
    'VariableNames', {'Name','Age','Score'});

%% Basic operations
T.Score                          % Lấy cột
T(T.Score > 80, :)               % Filter
T.Grade = categorical({'A';'A';'B'});  % Thêm cột
T = sortrows(T, 'Score', 'descend');   % Sắp xếp

%% Tổng hợp
groupsummary(T, 'Grade', 'mean', 'Score')  % Nhóm theo Grade

%% Join tables
T2 = table({'Alice';'Bob'}, {'CS';'Math'}, 'VariableNames', {'Name','Dept'});
T_joined = innerjoin(T, T2, 'Key', 'Name');  % SQL-style join

%% Writetable
writetable(T, 'output.xlsx');
```

### 7.2 Advanced Visualization
```matlab
%% Heatmap
data = magic(8);
h = heatmap(data);
h.Title = 'Magic Square';
h.Colormap = parula;

%% Bubble chart
x = randn(50,1)*2 + 3;
y = 0.5*x + randn(50,1);
sz = abs(randn(50,1))*20 + 5;   % Kích thước bong bóng
c = 1:50;

bubblechart(x, y, sz, c);
colorbar;
xlabel('X'); ylabel('Y');
title('Bubble Chart');

%% Violin plot (thống kê phân phối)
% Cần violinplot từ MATLAB File Exchange hoặc
% Dùng boxplot thay thế
data1 = randn(100,1);
data2 = randn(100,1) + 1;
boxplot([data1, data2], {'Nhóm A', 'Nhóm B'});

%% Radar chart
categories = {'Speed','Strength','Agility','Endurance','IQ'};
values = [85 70 90 60 95];
spider_plot(values, categories);  % Cần spider_plot từ FEX

%% 3D scatter với colormap
figure;
x = randn(200,1); y = randn(200,1); z = randn(200,1);
c = x.^2 + y.^2 + z.^2;  % Màu = khoảng cách từ gốc
scatter3(x, y, z, 50, c, 'filled');
colorbar; colormap(jet);
xlabel('X'); ylabel('Y'); zlabel('Z');
title('3D Scatter');
```

### 7.3 Dashboard với Figures
```matlab
figure('Name', 'Data Dashboard', 'NumberTitle', 'off', ...
    'Position', [50 50 1200 700], 'Color', [0.1 0.1 0.15]);

% Tiled layout (MATLAB R2019b+)
t = tiledlayout(2, 3, 'TileSpacing', 'compact', 'Padding', 'compact');
t.Title.String = 'Sales Dashboard 2024';
t.Title.Color  = 'white';
t.Title.FontSize = 16;

% Tile 1: Line chart
ax1 = nexttile;
months = 1:12;
sales  = [120 135 148 162 155 178 192 185 200 215 198 230];
plot(ax1, months, sales, 'c-o', 'LineWidth', 2);
set(ax1, 'Color', [0.15 0.15 0.2], 'XColor', 'w', 'YColor', 'w');
title(ax1, 'Monthly Sales', 'Color', 'w');
xlabel(ax1, 'Month'); ylabel(ax1, 'Units');

% Tile 2: Bar chart
ax2 = nexttile;
categories = {'Q1','Q2','Q3','Q4'};
quarterly  = [403 495 577 643];
b = bar(ax2, quarterly, 'FaceColor', 'flat');
b.CData = [0.2 0.6 1; 0.2 0.8 0.5; 1 0.7 0.2; 0.9 0.3 0.3];
set(ax2, 'Color', [0.15 0.15 0.2], 'XColor', 'w', 'YColor', 'w', ...
    'XTickLabel', categories);
title(ax2, 'Quarterly Revenue', 'Color', 'w');

% Tile 3: Pie chart
ax3 = nexttile;
products = [35 25 20 15 5];
labels = {'Product A','B','C','D','Others'};
pie(ax3, products, labels);
title(ax3, 'Product Mix', 'Color', 'w');
set(ax3, 'Color', [0.15 0.15 0.2]);

% Tile 4-6: thêm charts...
```

---

## 🏋️ Bài Tập Ứng Dụng

**Bài 1**: Xây dựng pipeline phân loại ảnh chó/mèo: Thu thập dữ liệu → Augmentation → Train CNN → Evaluate.

**Bài 2**: Implement hệ thống nhận diện chữ số (MNIST) với MLP tự viết từ scratch (không dùng Deep Learning Toolbox).

**Bài 3**: Thiết kế bộ điều khiển PID cho hệ con lắc ngược (inverted pendulum) trong Simulink, tune để đáp ứng tốt.

**Bài 4**: Phân tích chuỗi thời gian giá chứng khoán: Load data → Preprocessing → Dự đoán với ARIMA và LSTM → So sánh kết quả.

**Bài 5**: Tạo một ứng dụng MATLAB App (App Designer) đơn giản: Dashboard hiển thị dữ liệu thống kê với interactive controls.

---

*[⬅ 03_Nang_Cao.md](03_Nang_Cao.md) | [Tiếp theo: 05_Bai_Tap.md ➡](05_Bai_Tap.md)*
