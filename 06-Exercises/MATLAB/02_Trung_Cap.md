# 🟡 MATLAB Trung Cấp

## Mục Lục
1. [Đồ Thị Nâng Cao](#1-đồ-thị-nâng-cao)
2. [Cell Array](#2-cell-array)
3. [Struct (Cấu Trúc Dữ Liệu)](#3-struct)
4. [Xử Lý File Nâng Cao](#4-xử-lý-file-nâng-cao)
5. [Regular Expression](#5-regular-expression)
6. [Containers.Map (Dictionary)](#6-containersmap)
7. [Error Handling](#7-error-handling)
8. [Debugging](#8-debugging)
9. [Đại Số Tuyến Tính](#9-đại-số-tuyến-tính)
10. [Số Liệu Thống Kê](#10-số-liệu-thống-kê)
11. [Số Vi Phân và Tích Phân](#11-số-vi-phân-và-tích-phân)
12. [Phương Trình](#12-phương-trình)

---

## 1. Đồ Thị Nâng Cao

### 1.1 Đồ Thị 3D
```matlab
% Surface plot
[X, Y] = meshgrid(-3:0.1:3, -3:0.1:3);
Z = sin(sqrt(X.^2 + Y.^2));

figure;
surf(X, Y, Z);
xlabel('X'); ylabel('Y'); zlabel('Z');
title('Surface: sin(sqrt(x^2+y^2))');
colorbar;        % Hiện thanh màu
colormap(jet);   % Bảng màu: jet, parula, hot, cool, gray...
shading interp;  % Làm mịn màu (không có lưới ô vuông)

% Contour (đường đồng mức)
figure;
contour(X, Y, Z, 20);   % 20 đường đồng mức
contourf(X, Y, Z, 20);  % Filled contour

% Kết hợp surface + contour
figure;
surfc(X, Y, Z);  % Surface với contour bên dưới

% Plot 3D đường
t = 0:0.01:6*pi;
x = sin(t); y = cos(t); z = t;
plot3(x, y, z, 'LineWidth', 2);
grid on;
```

### 1.2 Điều Chỉnh Trục và Hiển Thị
```matlab
ax = gca;  % Lấy current axes

% Giới hạn trục
xlim([0, 10]);
ylim([-1.5, 1.5]);
axis([0 10 -2 2]);      % [xmin xmax ymin ymax]
axis equal;              % Tỉ lệ bằng nhau
axis tight;              % Sát dữ liệu
axis off;                % Tắt trục

% Thang logarithm
semilogy(1:10, exp(1:10));  % Trục Y logarithm
semilogx(logspace(0,3,100), sin(logspace(0,3,100))); % X log
loglog(logspace(0,3,100), logspace(0,3,100).^2);  % Cả hai

% Định dạng trục
set(ax, 'XTick', 0:pi:4*pi);
set(ax, 'XTickLabel', {'0','\pi','2\pi','3\pi','4\pi'});
set(ax, 'FontSize', 14);

% Second y-axis (hai trục Y)
yyaxis left;  plot(x1, y1); ylabel('Trái');
yyaxis right; plot(x2, y2); ylabel('Phải');
```

### 1.3 Tùy Chỉnh Đồ Thị Đẹp
```matlab
figure('Color', 'white', 'Position', [100 100 900 500]);

x = linspace(0, 4*pi, 500);
h1 = plot(x, sin(x), 'Color', [0.2 0.6 1.0], 'LineWidth', 2.5);
hold on;
h2 = plot(x, cos(x), 'Color', [1.0 0.4 0.2], 'LineWidth', 2.5, 'LineStyle', '--');

% Vùng tô màu
patch([x, fliplr(x)], [sin(x), zeros(1,length(x))], ...
    'b', 'FaceAlpha', 0.1, 'EdgeColor', 'none');

% Text annotation
text(pi, 0.1, '\pi', 'FontSize', 16, 'HorizontalAlignment', 'center');
annotation('arrow', [0.3 0.5], [0.7 0.5]);

ax = gca;
ax.XGrid = 'on'; ax.YGrid = 'on';
ax.GridLineStyle = '--';
ax.GridAlpha = 0.3;
ax.Box = 'off';
ax.FontSize = 13;

legend([h1 h2], {'sin(x)', 'cos(x)'}, 'Location', 'best', 'Box', 'off');
xlabel('x (rad)', 'FontSize', 14);
ylabel('Biên độ',  'FontSize', 14);
title('So sánh Sin và Cos', 'FontSize', 16, 'FontWeight', 'bold');
```

### 1.4 Lưu Đồ Thị
```matlab
saveas(gcf, 'do_thi.png');       % PNG
saveas(gcf, 'do_thi.pdf');       % PDF (vector)
exportgraphics(gcf, 'do_thi.eps', 'Resolution', 300); % EPS 300 DPI
print(gcf, 'do_thi', '-dpng', '-r300');  % PNG 300 DPI
```

### 1.5 Animation
```matlab
figure;
h = plot(nan, nan, 'LineWidth', 2);
xlim([0 2*pi]); ylim([-1.2 1.2]);
grid on;

x_data = [];
y_data = [];
for t = 0:0.05:2*pi
    x_data = [x_data, t];
    y_data = [y_data, sin(t)];
    set(h, 'XData', x_data, 'YData', y_data);
    drawnow;  % Cập nhật đồ thị ngay
    pause(0.02);
end
```

---

## 2. Cell Array

> `Cell array` lưu trữ dữ liệu hỗn hợp (khác loại/kích thước).

### 2.1 Tạo Cell Array
```matlab
% Dùng {}
C = {1, 'hello', [1 2 3], true, pi}

% Cell array 2D
C2 = {1, 'abc'; [1;2], {1,2}}

% Tạo rỗng rồi điền
C3 = cell(3, 2);   % Cell 3x2 rỗng
C3{1,1} = 'row1';
C3{2,1} = [1 2 3];
```

### 2.2 Truy Cập Cell Array
```matlab
C = {'apple', 42, [1 2 3]};

% {} để lấy NỘI DUNG
C{1}      % 'apple'
C{3}      % [1 2 3]
C{3}(2)   % 2 - phần tử thứ 2 của mảng trong C{3}

% () để lấy cell con (vẫn là cell)
C(1)      % {'apple'} - cell 1x1 chứa 'apple'
C(1:2)    % {'apple', 42} - cell 1x2
```

### 2.3 Thao Tác Cell Array
```matlab
C = {'banana', 'apple', 'cherry'};

% Kích thước
length(C)    % 3
numel(C)     % 3
size(C)      % [1, 3]

% Chèn và xóa
C{end+1} = 'date';   % Thêm vào cuối
C(2) = [];           % Xóa phần tử 2

% Kiểm tra
iscell(C)            % 1
iscellstr(C)         % 1 (cell toàn chuỗi)

% Chuyển đổi
str_arr = strjoin(C, ', ');   % 'banana, cherry, date'
C2 = strsplit('a,b,c', ','); % {'a','b','c'}
celldisp(C);                  % Hiển thị chi tiết

% cellfun: áp dụng hàm lên từng cell
lengths = cellfun(@length, C)         % [6, 6, 4] - độ dài mỗi chuỗi
upper_C = cellfun(@upper, C, 'UniformOutput', false) % Không đồng nhất kích thước
```

---

## 3. Struct

> `struct` nhóm dữ liệu liên quan theo tên trường (field).

### 3.1 Tạo Struct
```matlab
% Cách 1: Gán trực tiếp
student.name  = 'Nguyen Van An';
student.age   = 20;
student.score = [8.5, 9.0, 7.5];
student.passed = true;

% Cách 2: Dùng struct()
student2 = struct('name', 'Tran Thi B', 'age', 22, 'score', [9,8,9]);

% Mảng struct
students(1) = struct('name', 'An',  'gpa', 3.5);
students(2) = struct('name', 'Bình', 'gpa', 3.8);
students(3) = struct('name', 'Lan', 'gpa', 3.2);
```

### 3.2 Truy Cập Struct
```matlab
s = students(1);
s.name        % 'An'
s.gpa         % 3.5

% Mảng struct
students(2).name   % 'Bình'
[students.gpa]     % [3.5, 3.8, 3.2] - lấy field từ tất cả

% Dynamic field name
field = 'name';
s.(field)          % Tương đương s.name

% Tên tất cả field
fieldnames(s)      % {'name'; 'gpa'}
isfield(s, 'gpa')  % 1
rmfield(s, 'gpa')  % Xóa field 'gpa'
```

### 3.3 Struct Lồng Nhau
```matlab
university.name = 'Đại học ABC';
university.location.city    = 'Hà Nội';
university.location.country = 'Việt Nam';
university.departments = {'CNTT', 'Điện tử', 'Cơ khí'};

% Truy cập
university.location.city          % 'Hà Nội'
university.departments{2}         % 'Điện tử'
```

### 3.4 Struct trong Vòng Lặp
```matlab
% Tạo dữ liệu
for i = 1:5
    data(i).x     = i;
    data(i).y     = i^2;
    data(i).label = sprintf('Point %d', i);
end

% Lấy tất cả giá trị y
all_y = [data.y];    % [1 4 9 16 25]

% Lọc
mask = [data.y] > 5;
subset = data(mask);  % data(3), data(4), data(5)
```

---

## 4. Xử Lý File Nâng Cao

### 4.1 Kiểm Tra File/Thư Mục
```matlab
exist('myfile.mat', 'file')    % 2 nếu tồn tại, 0 nếu không
exist('myfolder', 'dir')       % 7 nếu tồn tại
isfile('myfile.mat')           % true/false (R2017b+)
isfolder('myfolder')           % true/false

% Thông tin file
info = dir('myfile.mat');
info.bytes    % Kích thước (bytes)
info.date     % Ngày sửa đổi
```

### 4.2 Quản Lý Thư Mục
```matlab
pwd                        % Thư mục hiện tại
cd('/path/to/dir')         % Chuyển thư mục
ls                         % Liệt kê file (Unix)
dir                        % Liệt kê file chi tiết

% Tạo và xóa
mkdir('new_folder')
rmdir('empty_folder')
rmdir('folder_with_content', 's')  % Xóa đệ quy

% Liệt kê file theo pattern
files = dir('*.mat');       % Tất cả file .mat
for i = 1:length(files)
    fprintf('%s (%d bytes)\n', files(i).name, files(i).bytes);
end
```

### 4.3 Đọc/Ghi CSV Nâng Cao
```matlab
% Đọc với options
opts = detectImportOptions('data.csv');
opts.SelectedVariableNames = {'Name', 'Score'};  % Chọn cột
opts.DataRange = 'A2:C100';                       % Vùng dữ liệu
T = readtable('data.csv', opts);

% Xử lý table
T.Properties.VariableNames  % Tên cột
T.Score                      % Lấy cột Score
T(T.Score > 8, :)            % Lọc hàng
T.Grade = categorical({'A','B','C'}); % Thêm cột

% Ghi table
writetable(T, 'output.csv');
writetable(T, 'output.xlsx', 'Sheet', 'Data');
```

### 4.4 JSON
```matlab
% Đọc JSON
str = fileread('data.json');
data = jsondecode(str);    % Chuyển JSON -> struct/cell

% Ghi JSON
data.name = 'MATLAB';
data.version = 2024;
str = jsonencode(data);       % Chuyển struct -> JSON string
fid = fopen('output.json', 'w');
fprintf(fid, '%s', str);
fclose(fid);
```

---

## 5. Regular Expression

### 5.1 Cú Pháp Cơ Bản
```matlab
str = 'Điểm: 8.5, Lớp: CNTT01, Năm: 2024';

% regexp: Tìm vị trí
idx = regexp(str, '\d+');          % [7, 19, 28]

% regexp với match
[tokens, match] = regexp(str, '(\d+\.?\d*)', 'tokens', 'match');
match            % {'8.5', '01', '2024'}

% regexprep: Thay thế
result = regexprep('hello world', '\s+', '_');  % 'hello_world'

% Các ký tự đặc biệt
% \d  - chữ số [0-9]
% \w  - ký tự từ [a-zA-Z0-9_]
% \s  - khoảng trắng
% .   - bất kỳ ký tự nào
% *   - 0 hoặc nhiều lần
% +   - 1 hoặc nhiều lần
% ?   - 0 hoặc 1 lần
% ^   - đầu chuỗi
% $   - cuối chuỗi
% ()  - nhóm capture
% []  - tập ký tự
```

### 5.2 Ví Dụ Thực Tế
```matlab
% Kiểm tra email hợp lệ
email = 'user@example.com';
pattern = '^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$';
isvalid = ~isempty(regexp(email, pattern));

% Trích xuất số điện thoại
text = 'Gọi: 0901234567 hoặc 028-3456-7890';
phones = regexp(text, '[\d\-]{10,}', 'match');

% Parse log file
log = '2024-01-15 10:30:45 ERROR: Connection failed';
pattern = '(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+): (.+)';
tok = regexp(log, pattern, 'tokens'){1};
date = tok{1}; time = tok{2}; level = tok{3}; msg = tok{4};
```

---

## 6. Containers.Map

```matlab
% Tạo Map (dictionary)
m = containers.Map();
m('name')  = 'MATLAB';
m('year')  = 2024;
m('score') = 9.5;

% Tạo với keys và values
keys_list   = {'a', 'b', 'c'};
values_list = {1, 2, 3};
m2 = containers.Map(keys_list, values_list);

% Truy cập
m('name')         % 'MATLAB'
m.Count           % Số phần tử: 3
keys(m)           % {'name','score','year'}
values(m)         % {'MATLAB', 9.5, 2024}
isKey(m, 'name')  % 1

% Xóa
remove(m, 'year');
```

---

## 7. Error Handling

### 7.1 try - catch
```matlab
try
    x = 1/0;     % Không lỗi (Inf)
    y = sqrt(-1); % Không lỗi (NaN hoặc complex)
    z = [1 2] + [1 2 3];  % Lỗi! Kích thước không khớp
    
catch ME   % ME = MException object
    fprintf('Lỗi: %s\n', ME.message);
    fprintf('ID: %s\n', ME.identifier);
    disp(ME.stack);  % Stack trace
    
    % Xử lý lỗi cụ thể
    if strcmp(ME.identifier, 'MATLAB:sizeDimensionsMustMatch')
        disp('Kích thước mảng không khớp!');
    else
        rethrow(ME);  % Ném lỗi lên trên
    end
end
```

### 7.2 Phát Sinh Lỗi
```matlab
function result = safe_divide(a, b)
    if b == 0
        error('myPkg:divByZero', 'Không thể chia cho 0!');
    end
    if ~isnumeric(a) || ~isnumeric(b)
        error('myPkg:wrongType', 'Input phải là số, nhận được %s', class(a));
    end
    result = a / b;
end

% Warning (cảnh báo, không dừng chương trình)
warning('myPkg:slowCode', 'Hàm này chạy chậm với n > 1000');
warning('off', 'myPkg:slowCode');  % Tắt warning này
```

### 7.3 assert
```matlab
x = 5;
assert(x > 0)                       % Không lỗi
assert(x > 0, 'x phải dương!')      % Thêm message
assert(abs(0.1+0.2 - 0.3) < 1e-10) % So sánh float
```

---

## 8. Debugging

```matlab
% Thêm breakpoint: click vào số dòng trong Editor

% Lệnh trong debug mode:
% s (step)    - Chạy một bước (vào trong hàm)
% n (next)    - Chạy một dòng (bỏ qua hàm)
% c (continue)- Chạy đến breakpoint tiếp theo
% q (quit)    - Thoát debug mode
% up/down     - Di chuyển trong call stack

% Programmatic breakpoints
dbstop in myfunction        % Dừng khi vào hàm
dbstop in myfunction at 10  % Dừng tại dòng 10
dbstop if error             % Dừng khi có lỗi (rất hữu ích!)
dbstop if warning           % Dừng khi có warning
dbclear all                 % Xóa tất cả breakpoints
dbstatus                    % Xem breakpoints hiện tại

% Kiểm tra hiệu suất
tic;
% ... code cần đo ...
elapsed = toc;
fprintf('Chạy trong %.4f giây\n', elapsed);

% Profile chi tiết
profile on
my_function();
profile off
profile viewer  % Mở GUI xem performance
```

---

## 9. Đại Số Tuyến Tính

### 9.1 Hệ Phương Trình Tuyến Tính
```matlab
% Giải Ax = b
A = [2 1 -1; -3 -1 2; -2 1 2];
b = [8; -11; -3];

% Phương pháp 1: toán tử \  (khuyến dùng)
x = A \ b     % x = [2; 3; -1]

% Phương pháp 2: inv(A) * b (kém chính xác hơn)
x2 = inv(A) * b

% Kiểm tra: A*x phải ≈ b
norm(A*x - b)  % Rất nhỏ (sai số máy tính)

% Hệ quá định (overdetermined): ít nghiệm nhất bình phương
A_over = [1 1; 1 -1; 1 2];
b_over = [2; 0; 4];
x_ls = A_over \ b_over   % Least-squares solution
```

### 9.2 Phân Tích Ma Trận
```matlab
A = [4 2; 1 3];

% Trị riêng và vectơ riêng
[V, D] = eig(A);
% D: ma trận đường chéo chứa eigenvalues
% V: ma trận cột chứa eigenvectors

% Cholesky (cho ma trận xác định dương)
A_pos = A'*A + eye(2)*0.1;
L = chol(A_pos);   % A_pos = L'*L

% LU factorization
[L, U, P] = lu(A);  % P*A = L*U

% QR decomposition
[Q, R] = qr(A);    % A = Q*R

% SVD
[U, S, V] = svd(A);  % A = U*S*V'

% Số điều kiện (condition number)
cond(A)    % Lớn -> ma trận gần suy biến -> kém ổn định số
rank(A)    % Hạng ma trận
null(A)    % Không gian null
orth(A)    % Cơ sở trực chuẩn của không gian cột
```

---

## 10. Số Liệu Thống Kê

```matlab
data = randn(1000, 1) * 2 + 5;  % N(5, 4)

% Thống kê mô tả
mean(data)      % Trung bình
median(data)    % Trung vị
mode(data)      % Yếu vị (mode)
std(data)       % Độ lệch chuẩn (mẫu, n-1)
std(data, 1)    % Độ lệch chuẩn (tổng thể, n)
var(data)       % Phương sai
skewness(data)  % Độ lệch
kurtosis(data)  % Độ nhọn
prctile(data, [25 50 75])  % Phân vị 25, 50, 75
iqr(data)       % Interquartile range

% Kiểm định giả thuyết
[h, p, ci] = ttest(data, 5);     % One-sample t-test (mu=5?)
[h, p]     = ttest2(d1, d2);     % Two-sample t-test
[h, p]     = kstest(data);       % Kolmogorov-Smirnov (normal?)
[h, p]     = chi2gof(data);      % Chi-square goodness of fit

% Hồi quy tuyến tính
x = [1:10]';
y = 2*x + 3 + randn(10,1);
coeffs = polyfit(x, y, 1);  % [slope, intercept]
y_pred = polyval(coeffs, x);

% Hồi quy bội (Multiple regression)
X = [ones(10,1), x, x.^2];  % Thêm cột bias
b = X \ y;  % Least squares

% Correlation
[r, p] = corr(x, y);  % Pearson correlation
```

---

## 11. Số Vi Phân và Tích Phân

### 11.1 Đạo Hàm Số
```matlab
% Sai phân (numerical differentiation)
x = 0:0.01:2*pi;
y = sin(x);
dy = diff(y) ./ diff(x);  % Đạo hàm xấp xỉ

% Gradient (2D)
[X, Y] = meshgrid(-2:0.1:2);
Z = X.^2 + Y.^2;
[Gx, Gy] = gradient(Z, 0.1, 0.1);
quiver(X, Y, Gx, Gy);  % Vẽ vectơ gradient
```

### 11.2 Tích Phân Số
```matlab
% Tích phân xác định ∫ sin(x)dx từ 0 đến pi
f = @(x) sin(x);
I = integral(f, 0, pi)         % I ≈ 2.0 (chính xác cao)
I2 = quad(f, 0, pi)            % Cách cũ
I3 = trapz(0:0.001:pi, sin(0:0.001:pi))  % Phương pháp hình thang

% Tích phân 2D
f2 = @(x,y) x.^2 + y.^2;
I2d = integral2(f2, 0, 1, 0, 1)   % ∫∫ (x²+y²) dxdy

% Tích phân 3D
f3 = @(x,y,z) x + y + z;
I3d = integral3(f3, 0,1, 0,1, 0,1)
```

### 11.3 Phương Trình Vi Phân
```matlab
% Giải ODE: dy/dt = -2y, y(0) = 1
% Nghiệm chính xác: y(t) = exp(-2t)
f = @(t, y) -2*y;
[t, y] = ode45(f, [0, 5], 1);   % ode45: Runge-Kutta 4-5 (phổ biến nhất)
plot(t, y, 'b-', t, exp(-2*t), 'r--');

% Hệ ODE: Lorenz attractor
sigma = 10; rho = 28; beta = 8/3;
lorenz = @(t,s) [sigma*(s(2)-s(1)); s(1)*(rho-s(3))-s(2); s(1)*s(2)-beta*s(3)];
[t, S] = ode45(lorenz, [0 50], [1; 1; 1]);
plot3(S(:,1), S(:,2), S(:,3));

% Lựa chọn ODE solver:
% ode45  - RK45, phổ thông, bài toán không stiff
% ode23  - RK23, nhanh hơn ode45 với sai số lớn hơn
% ode113 - Adams, hiệu quả với bài toán trơn
% ode15s - BDF, bài toán STIFF (e.g. phản ứng hóa học nhanh)
% ode23s - Modified Rosenbrock, stiff
```

---

## 12. Phương Trình

### 12.1 Tìm Nghiệm Phương Trình
```matlab
% Tìm nghiệm của f(x) = 0
f = @(x) x^3 - 2*x - 5;
x0 = fzero(f, 2)         % Tìm nghiệm gần x=2
x0 = fzero(f, [1, 3])   % Tìm nghiệm trong [1,3]

% Đa thức
p = [1, 0, -2, -5];     % x^3 + 0*x^2 - 2x - 5
roots(p)                 % Tất cả nghiệm (có thể phức)
polyval(p, 2)            % Giá trị tại x=2

% Hệ phương trình phi tuyến
% x^2 + y^2 = 4
% x + y = 1
F = @(v) [v(1)^2 + v(2)^2 - 4; v(1) + v(2) - 1];
sol = fsolve(F, [1; 1])   % Cần Optimization Toolbox
```

### 12.2 Nội Suy
```matlab
x = [0, 1, 2, 3, 4];
y = [0, 1, 4, 9, 16];

% Nội suy tuyến tính
y_interp = interp1(x, y, 2.5)          % Nội suy tại x=2.5
y_interp = interp1(x, y, 2.5, 'cubic') % Cubic spline

% Nội suy 2D
[X, Y] = meshgrid(1:4, 1:4);
Z = sin(X) .* cos(Y);
z_new = interp2(X, Y, Z, 1.5, 2.5, 'cubic');

% Spline
cs = spline(x, y);             % Cubic spline object
y_fine = ppval(cs, 0:0.1:4);  % Tính giá trị
```

---

## 💡 Mẹo Trung Cấp

```matlab
% 1. Logical indexing thay for loop
data = randn(1, 1000);
positive = data(data > 0);          % Lấy phần tử dương
data(data < 0) = 0;                 % Clip về 0

% 2. Preallocate + vectorize
n = 1e6;
x = (1:n) / n;
y = sin(x) .* exp(-x);             % Vectorized ✅

% 3. Accumarray - nhóm và tổng hợp
groups = [1; 2; 1; 3; 2; 1];
values = [10; 20; 30; 40; 50; 60];
sums = accumarray(groups, values);  % [100; 70; 40]

% 4. bsxfun (broadcast) - trước R2016b
% Sau R2016b, MATLAB tự động broadcast
A = [1;2;3];
B = [10 20 30];
C = A + B;    % [11 21 31; 12 22 32; 13 23 33] - tự broadcast!

% 5. String formatting
fprintf('%-20s %8.2f %%\n', 'Accuracy:', 98.765);
% Output: Accuracy:              98.76 %
```

---

## 🏋️ Bài Tập Trung Cấp

**Bài 1**: Đọc file CSV chứa dữ liệu điểm sinh viên. Tính thống kê mô tả và vẽ histogram phân phối điểm.

**Bài 2**: Viết hàm dùng cell array để quản lý danh sách học sinh (thêm, xóa, tìm kiếm theo tên).

**Bài 3**: Tạo animation vẽ đường Lissajous: `x = sin(at+δ)`, `y = sin(bt)` với các giá trị a,b,δ khác nhau.

**Bài 4**: Giải và vẽ nghiệm hệ ODE mô hình săn mồi Lotka-Volterra:
```
dx/dt = αx - βxy
dy/dt = δxy - γy
```

**Bài 5**: Implement thuật toán interpolation tự viết (không dùng `interp1`) và so sánh kết quả với MATLAB.

---

*[⬅ 01_Co_Ban.md](01_Co_Ban.md) | [Tiếp theo: 03_Nang_Cao.md ➡](03_Nang_Cao.md)*
