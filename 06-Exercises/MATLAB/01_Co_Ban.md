# 🟢 MATLAB Cơ Bản

## Mục Lục
1. [Làm Quen Với MATLAB](#1-làm-quen-với-matlab)
2. [Biến và Kiểu Dữ Liệu](#2-biến-và-kiểu-dữ-liệu)
3. [Ma Trận và Vectơ](#3-ma-trận-và-vectơ)
4. [Phép Toán](#4-phép-toán)
5. [Câu Lệnh Điều Kiện](#5-câu-lệnh-điều-kiện)
6. [Vòng Lặp](#6-vòng-lặp)
7. [Hàm (Function)](#7-hàm-function)
8. [Xử Lý Chuỗi](#8-xử-lý-chuỗi)
9. [Vẽ Đồ Thị Cơ Bản](#9-vẽ-đồ-thị-cơ-bản)
10. [Nhập/Xuất Dữ Liệu Cơ Bản](#10-nhậpxuất-dữ-liệu-cơ-bản)

---

## 1. Làm Quen Với MATLAB

### 1.1 Giao Diện MATLAB
```
- Command Window: Gõ lệnh và xem kết quả ngay
- Workspace:      Xem tất cả biến đang tồn tại
- Editor:         Viết script (.m file)
- Current Folder: Quản lý file
```

### 1.2 Các Lệnh Cơ Bản Nhất
```matlab
% Đây là comment (chú thích)
clc       % Xóa Command Window
clear     % Xóa tất cả biến trong Workspace
clear x   % Xóa biến x
close all % Đóng tất cả cửa sổ đồ thị
who       % Hiển thị danh sách biến
whos      % Hiển thị biến kèm chi tiết kích thước, kiểu
help sin  % Xem trợ giúp hàm sin
doc sin   % Mở tài liệu chi tiết hàm sin
```

### 1.3 Dấu Chấm Phẩy (;)
```matlab
x = 5       % KHÔNG có ; => hiển thị kết quả: x = 5
y = 10;     % Có ; => KHÔNG hiển thị kết quả (chạy âm thầm)
```

### 1.4 Script vs Function
```matlab
% Script: file .m, chạy từng dòng lệnh, dùng biến workspace
% Function: file .m, có input/output, biến nội bộ riêng

% Tạo script: lưu file myscript.m rồi gõ: myscript
% Tạo function: xem phần 7
```

---

## 2. Biến và Kiểu Dữ Liệu

### 2.1 Gán Biến
```matlab
a = 42          % Số nguyên (thực ra là double)
b = 3.14        % Số thực
c = 2 + 3i      % Số phức
d = true        % Logical (boolean)
e = 'Hello'     % Chuỗi ký tự (char array)
f = "Hello"     % String (MATLAB R2016b+)
```

### 2.2 Các Kiểu Dữ Liệu
```matlab
% Số
x_double = 3.14;         % double (mặc định)
x_int32  = int32(100);   % integer 32-bit
x_uint8  = uint8(255);   % unsigned integer 8-bit
x_single = single(3.14); % float 32-bit

% Kiểm tra kiểu dữ liệu
class(x_double)   % 'double'
class(x_int32)    % 'int32'
isa(x_int32, 'int32')  % 1 (true)

% Chuyển đổi kiểu
y = double(x_int32);
z = int32(3.7);   % z = 4 (làm tròn)
```

### 2.3 Hằng Số Đặc Biệt
```matlab
pi          % 3.14159265358979...
exp(1)      % e = 2.71828...
Inf         % Vô cực
-Inf        % Âm vô cực
NaN         % Not a Number (0/0)
eps         % Sai số máy tính: 2.2204e-16
intmax      % Số nguyên lớn nhất: 2147483647
```

### 2.4 Kiểm Tra Giá Trị
```matlab
isnan(NaN)    % 1
isinf(Inf)    % 1
isfinite(5)   % 1
isreal(3+2i)  % 0
isinteger(int32(5)) % 1
isnumeric(3.14)     % 1
ischar('abc')       % 1
islogical(true)     % 1
```

---

## 3. Ma Trận và Vectơ

> MATLAB = **MAT**rix **LAB**oratory - Ma trận là trái tim của MATLAB!

### 3.1 Tạo Vectơ
```matlab
% Vectơ hàng (row vector)
v1 = [1, 2, 3, 4, 5]    % dùng dấu phẩy
v2 = [1 2 3 4 5]         % hoặc dùng khoảng trắng

% Vectơ cột (column vector)
v3 = [1; 2; 3; 4; 5]    % dùng dấu chấm phẩy

% Dãy số đều (linspace & colon)
v4 = 1:5           % [1, 2, 3, 4, 5] - bước = 1
v5 = 1:2:10        % [1, 3, 5, 7, 9] - bước = 2
v6 = 0:0.5:2       % [0, 0.5, 1.0, 1.5, 2.0]
v7 = linspace(0, 1, 5)  % [0, 0.25, 0.5, 0.75, 1.0] - chia đều 5 điểm
v8 = logspace(0, 3, 4)  % [1, 10, 100, 1000] - chia đều logarithm
```

### 3.2 Tạo Ma Trận
```matlab
% Ma trận 3x3
A = [1 2 3; 4 5 6; 7 8 9]
% Kết quả:
% A =
%  1  2  3
%  4  5  6
%  7  8  9

% Ma trận đặc biệt
zeros(3)      % Ma trận 0 kích thước 3x3
zeros(2,4)    % Ma trận 0 kích thước 2x4
ones(3)       % Ma trận 1
eye(4)        % Ma trận đơn vị 4x4
rand(3)       % Ma trận ngẫu nhiên [0,1] uniform
randn(3)      % Ma trận ngẫu nhiên phân phối chuẩn N(0,1)
randi(10,3)   % Ma trận nguyên ngẫu nhiên [1,10] kích thước 3x3

% Tạo ma trận từ vectơ
x = 1:3;
diag(x)       % Ma trận đường chéo chính = [1,2,3]
```

### 3.3 Kích Thước Ma Trận
```matlab
A = [1 2 3; 4 5 6];  % Ma trận 2x3

size(A)       % [2, 3]
size(A, 1)    % 2 (số hàng)
size(A, 2)    % 3 (số cột)
length(A)     % 3 (chiều lớn nhất)
numel(A)      % 6 (tổng phần tử)
ndims(A)      % 2 (số chiều)
```

### 3.4 Truy Cập Phần Tử (Indexing)
```matlab
A = [10 20 30; 40 50 60; 70 80 90];

% Truy cập phần tử đơn (index bắt đầu từ 1, không phải 0!)
A(1,1)    % 10  - hàng 1, cột 1
A(2,3)    % 60  - hàng 2, cột 3
A(end,end)% 90  - phần tử cuối

% Truy cập hàng và cột
A(1,:)    % [10 20 30] - toàn bộ hàng 1
A(:,2)    % [20;50;80] - toàn bộ cột 2
A(2,:)    % [40 50 60] - hàng 2

% Truy cập vùng con (submatrix)
A(1:2, 2:3)   % [20 30; 50 60] - hàng 1-2, cột 2-3

% Index tuyến tính (linear indexing)
A(1)      % 10 - phần tử thứ 1 (theo cột)
A(4)      % 20 - phần tử thứ 4
A(:)      % Chuyển thành vectơ cột

% Thay đổi giá trị
A(1,1) = 99;
A(2,:) = [0 0 0];
```

### 3.5 Số Học Ma Trận
```matlab
A = [1 2; 3 4];
B = [5 6; 7 8];

A + B       % Cộng ma trận
A - B       % Trừ ma trận
A * B       % Nhân ma trận (matrix multiplication)
A .* B      % Nhân từng phần tử (element-wise)
A / B       % A * inv(B) - chia ma trận
A ./ B      % Chia từng phần tử
A ^ 2       % Lũy thừa ma trận (A*A)
A .^ 2      % Lũy thừa từng phần tử

% Chú ý: .* và ./ rất quan trọng!
[1 2 3] .* [4 5 6]    % [4 10 18]  ✓
[1 2 3] * [4 5 6]     % Lỗi! Không đúng kích thước
```

### 3.6 Hàm Ma Trận
```matlab
A = [1 2; 3 4];

inv(A)         % Ma trận nghịch đảo
det(A)         % Định thức
rank(A)        % Hạng
trace(A)       % Vết (tổng đường chéo)
A'             % Chuyển vị (transpose)
conj(A)        % Liên hợp phức
ctranspose(A)  % Chuyển vị liên hợp Hermitian (A')

[V, D] = eig(A)   % Trị riêng (eigenvalue) và vectơ riêng
[U, S, V] = svd(A) % Phân tích suy biến (SVD)
```

### 3.7 Thao Tác Mảng
```matlab
A = [1 2 3; 4 5 6];

% Ghép ma trận
B = [A; [7 8 9]]       % Ghép theo hàng (thêm hàng xuống dưới)
C = [A, [10;20]]       % Ghép theo cột (thêm cột bên phải)

% Sắp xếp và tìm
sort([3 1 4 1 5])       % [1 1 3 4 5] - tăng dần
sort([3 1 4 1 5], 'descend')  % [5 4 3 1 1] - giảm dần
[sorted, idx] = sort([3 1 2]) % sorted=[1 2 3], idx=[2 3 1]
max(A)           % max mỗi cột: [4 5 6]
max(max(A))      % max toàn bộ: 6
max(A(:))        % cách khác: 6
[val, idx] = max([3 1 4])  % val=4, idx=3
min(A)
sum(A)           % tổng mỗi cột: [5 7 9]
sum(A(:))        % tổng toàn bộ: 21
sum(A, 2)        % tổng mỗi hàng: [6;15]
cumsum([1 2 3 4])  % [1 3 6 10]
prod([1 2 3 4])    % 24
mean(A)          % trung bình mỗi cột
std(A)           % độ lệch chuẩn
var(A)           % phương sai

% Reshape và flatten
reshape(A, 3, 2)    % Đổi hình dạng thành 3x2 (giữ nguyên số phần tử)
reshape(A, 1, [])   % Flatten thành hàng
A(:)                % Flatten thành cột

% Loại bỏ/xóa
A(:, 2) = []        % Xóa cột 2
```

---

## 4. Phép Toán

### 4.1 Toán Học Cơ Bản
```matlab
% Phép toán số học
5 + 3     % 8
10 - 4    % 6
3 * 7     % 21
15 / 4    % 3.75
15 \ 4    % 4/15 = 0.2667 (chia ngược)
2 ^ 3     % 8
mod(10,3) % 1 (chia lấy dư)
rem(10,3) % 1 (tương tự mod, khác với số âm)
abs(-5)   % 5

% Làm tròn
floor(3.7)  % 3 (làm tròn xuống)
ceil(3.2)   % 4 (làm tròn lên)
round(3.5)  % 4 (làm tròn gần nhất)
fix(3.9)    % 3 (bỏ phần thập phân, về phía 0)
```

### 4.2 Hàm Toán Học
```matlab
% Lượng giác (đơn vị radian)
sin(pi/2)       % 1
cos(0)          % 1
tan(pi/4)       % 1
asin(1)         % pi/2
acos(0)         % pi/2
atan(1)         % pi/4
atan2(y, x)     % góc từ gốc tới (x,y), kết quả trong (-pi, pi]

% Chuyển đổi góc
deg2rad(180)    % pi
rad2deg(pi)     % 180

% Lũy thừa & logarithm
exp(1)          % e = 2.7183
log(exp(1))     % 1 (log tự nhiên ln)
log2(8)         % 3
log10(1000)     % 3
sqrt(16)        % 4
nthroot(8, 3)   % 2 (căn bậc 3)
```

### 4.3 Toán Tử So Sánh (trả về logical)
```matlab
5 > 3       % 1 (true)
5 < 3       % 0 (false)
5 >= 5      % 1
5 <= 4      % 0
5 == 5      % 1 (bằng)
5 ~= 3      % 1 (khác nhau)

% So sánh mảng
[1 2 3] > 2        % [0 0 1]
[1 2 3] == [1 3 3] % [1 0 1]
```

### 4.4 Toán Tử Logic
```matlab
true & false    % 0 (AND)
true | false    % 1 (OR)
~true           % 0 (NOT)
xor(true,false) % 1 (XOR)

% Short-circuit (chỉ tính khi cần)
true && false   % AND ngắn mạch (cho scalar)
true || false   % OR ngắn mạch (cho scalar)

% Hàm logic
any([0 0 1 0])  % 1 (có ít nhất một true)
all([1 1 1 0])  % 0 (mọi phần tử đều true?)
find([0 3 0 5]) % [2 4] (index của phần tử khác 0)
find([1 2 3 4] > 2)  % [3 4]
```

---

## 5. Câu Lệnh Điều Kiện

### 5.1 if - elseif - else
```matlab
x = 75;

if x >= 90
    disp('Xuất sắc')
elseif x >= 75
    disp('Giỏi')
elseif x >= 60
    disp('Khá')
elseif x >= 50
    disp('Trung bình')
else
    disp('Yếu')
end
```

### 5.2 switch - case
```matlab
color = 'red';

switch color
    case 'red'
        disp('Màu đỏ')
    case {'blue', 'navy'}     % Nhiều giá trị trong một case
        disp('Màu xanh dương')
    case 'green'
        disp('Màu xanh lá')
    otherwise
        disp('Màu khác')
end
```

### 5.3 Toán Tử Ba Ngôi (cách MATLAB)
```matlab
% MATLAB không có ?: nhưng có thể dùng:
x = 5;
result = x * (x > 0) + (-x) * (x <= 0);  % abs(x)

% Hoặc dùng if inline (không khuyến khích)
% Tốt hơn: viết rõ if-else
```

---

## 6. Vòng Lặp

### 6.1 Vòng Lặp for
```matlab
% Lặp qua dãy số
for i = 1:5
    fprintf('i = %d\n', i);
end

% Lặp với bước nhảy
for i = 0:0.5:2
    disp(i)
end

% Lặp ngược
for i = 5:-1:1
    disp(i)
end

% Lặp qua mảng
fruits = {'apple', 'banana', 'cherry'};
for i = 1:length(fruits)
    fprintf('Trái cây: %s\n', fruits{i});
end

% Lặp qua ma trận (theo cột)
A = [1 2 3; 4 5 6];
for col = A        % col là từng cột của A
    disp(col)
end
```

### 6.2 Vòng Lặp while
```matlab
% Đếm đến 5
n = 1;
while n <= 5
    fprintf('n = %d\n', n);
    n = n + 1;
end

% Vòng lặp với điều kiện phức tạp
x = 100;
while x > 1
    x = x / 2;
    fprintf('x = %.4f\n', x);
end
```

### 6.3 break và continue
```matlab
% break: thoát vòng lặp
for i = 1:10
    if i == 5
        break;  % Dừng tại i=5
    end
    disp(i);
end

% continue: bỏ qua lần lặp hiện tại
for i = 1:10
    if mod(i, 2) == 0
        continue;  % Bỏ qua số chẵn
    end
    disp(i);  % Chỉ hiện số lẻ
end
```

### 6.4 Vectorization (Thay Thế Vòng Lặp - QUAN TRỌNG!)
```matlab
% ❌ Chậm: dùng for loop
n = 1000000;
result = zeros(1, n);
for i = 1:n
    result(i) = sin(i * pi / 180);
end

% ✅ Nhanh: vectorized (nên dùng!)
i = 1:n;
result = sin(i * pi / 180);

% ⚡ Benchmark
tic; % Bắt đầu đếm thời gian
% ... code ...
toc; % Dừng và hiện thời gian
```

---

## 7. Hàm (Function)

### 7.1 Cú Pháp Cơ Bản
```matlab
% File: tinh_dien_tich.m
function dien_tich = tinh_dien_tich(chieu_dai, chieu_rong)
    % Tính diện tích hình chữ nhật
    % Input:
    %   chieu_dai  - chiều dài (m)
    %   chieu_rong - chiều rộng (m)
    % Output:
    %   dien_tich  - diện tích (m^2)
    
    dien_tich = chieu_dai * chieu_rong;
end

% Gọi hàm
s = tinh_dien_tich(5, 3)  % s = 15
```

### 7.2 Nhiều Output
```matlab
% File: thong_ke.m
function [tb, std_dev, min_val, max_val] = thong_ke(data)
    tb      = mean(data);
    std_dev = std(data);
    min_val = min(data);
    max_val = max(data);
end

% Gọi hàm
data = [4, 7, 13, 2, 8, 1];
[mu, sigma, lo, hi] = thong_ke(data);
fprintf('TB=%.2f, STD=%.2f, Min=%d, Max=%d\n', mu, sigma, lo, hi);

% Chỉ lấy một số output (dùng ~)
[mu, ~, lo, ~] = thong_ke(data);  % Bỏ sigma và max
```

### 7.3 Nargin / Nargout (Số Tham Số)
```matlab
function result = my_power(x, n)
    if nargin < 2
        n = 2;  % Mặc định: bình phương
    end
    result = x ^ n;
end

my_power(3)     % 9  (n mặc định = 2)
my_power(3, 3)  % 27 (n = 3)
```

### 7.4 Anonymous Function (Hàm Vô Danh)
```matlab
% Cú pháp: f = @(args) expression
square = @(x) x.^2;
add    = @(x, y) x + y;
gauss  = @(x, mu, sig) exp(-(x-mu).^2 / (2*sig^2));

square(5)       % 25
add(3, 4)       % 7
gauss(0, 0, 1)  % 1.0

% Hữu ích khi truyền hàm vào hàm khác
x = -pi:0.01:pi;
plot(x, arrayfun(@(t) sin(t)^2 + cos(t), x));
```

### 7.5 Hàm Lồng Nhau (Nested Functions)
```matlab
function result = outer(x)
    a = 10;
    result = inner(x) + a;
    
    function y = inner(x)
        y = x * 2;  % Có thể truy cập 'a' từ outer!
    end
end
```

### 7.6 Hàm Đệ Quy
```matlab
% Tính giai thừa
function n_fact = factorial_custom(n)
    if n <= 1
        n_fact = 1;
    else
        n_fact = n * factorial_custom(n - 1);
    end
end

factorial_custom(5)  % 120

% Fibonacci
function f = fib(n)
    if n <= 2
        f = 1;
    else
        f = fib(n-1) + fib(n-2);
    end
end
```

---

## 8. Xử Lý Chuỗi

### 8.1 Tạo Chuỗi
```matlab
s1 = 'Hello World';    % char array (kiểu cũ)
s2 = "Hello World";    % string (R2016b+, khuyến dùng)

% Chuyển đổi
char_arr = char(s2);   % string -> char
str_obj  = string(s1); % char -> string
```

### 8.2 Thao Tác Chuỗi
```matlab
s = 'Hello, MATLAB!';

length(s)           % 14
numel(s)            % 14
size(s)             % [1, 14]

upper(s)            % 'HELLO, MATLAB!'
lower(s)            % 'hello, matlab!'
strtrim('  abc  ')  % 'abc' (xóa khoảng trắng đầu cuối)
strtrim('  abc  ')  % 'abc'

% Ghép chuỗi
s3 = [s1, ' - ', s2]          % Ghép char array
s4 = strcat(s1, ' - ', s2)    % strcat (tự động xóa trailing spaces)
s5 = s2 + " World"            % Cộng string (R2016b+)
sprintf('Value: %d', 42)      % 'Value: 42'

% Tìm kiếm
strfind(s, 'MATLAB')  % Trả về index xuất hiện
contains(s, 'Hello')  % true/false (string obj)
startsWith(s, "Hello")% true/false
endsWith(s, "!")     % true/false

% Thay thế
strrep(s, 'MATLAB', 'Octave')  % 'Hello, Octave!'

% Tách chuỗi
strsplit('a,b,c', ',')        % {'a','b','c'}
strsplit('hello world')        % {'hello','world'}

% So sánh
strcmp('abc', 'abc')   % 1 (true)
strcmpi('ABC', 'abc')  % 1 (không phân biệt hoa/thường)
```

### 8.3 Định Dạng Chuỗi
```matlab
% fprintf: xuất ra Command Window
fprintf('x = %d\n', 42);          % x = 42
fprintf('pi = %.4f\n', pi);       % pi = 3.1416
fprintf('%s has %d items\n', 'List', 5);

% sprintf: tạo chuỗi định dạng
s = sprintf('Value: %.2f', 3.14159);  % 'Value: 3.14'

% Định dạng số
fprintf('%5d\n', 42);      % '   42' (rộng 5)
fprintf('%-5d|\n', 42);    % '42   |' (căn trái)
fprintf('%05d\n', 42);     % '00042' (đệm số 0)
fprintf('%e\n', 12345.6);  % '1.234560e+04'
fprintf('%g\n', 12345.6);  % '12345.6' (tự chọn format)
```

---

## 9. Vẽ Đồ Thị Cơ Bản

### 9.1 Plot 2D Đơn Giản
```matlab
x = 0:0.01:2*pi;
y = sin(x);

figure;          % Tạo cửa sổ đồ thị mới
plot(x, y);      % Vẽ đường
xlabel('x (rad)');
ylabel('Biên độ');
title('Đồ thị sin(x)');
grid on;         % Hiện lưới
```

### 9.2 Tùy Chỉnh Đường
```matlab
x = 0:0.01:2*pi;

% Cú pháp: plot(x, y, 'LineSpec')
plot(x, sin(x), 'r-', 'LineWidth', 2);     % Đỏ, nét liền, dày 2
hold on;  % Giữ đồ thị, vẽ thêm lên
plot(x, cos(x), 'b--', 'LineWidth', 1.5);  % Xanh, nét đứt
plot(x, sin(2*x), 'go:', 'MarkerSize', 5); % Xanh lá, chấm tròn

legend('sin(x)', 'cos(x)', 'sin(2x)');
hold off;
```

### 9.3 Vẽ Nhiều Đồ Thị (subplot)
```matlab
x = linspace(0, 2*pi, 100);

figure('Position', [100 100 800 600]);  % Kích thước cửa sổ

subplot(2, 2, 1);  % 2 hàng, 2 cột, vị trí 1
plot(x, sin(x)); title('Sin');

subplot(2, 2, 2);
plot(x, cos(x)); title('Cos');

subplot(2, 2, 3);
plot(x, sin(x).^2); title('Sin^2');

subplot(2, 2, 4);
plot(x, exp(-x).*sin(x)); title('Tắt dần');
```

### 9.4 Các Loại Đồ Thị Khác
```matlab
% Bar chart
data = [23 45 12 67 34];
bar(data); title('Bar Chart');

% Pie chart
pie([30 25 20 15 10], {'A','B','C','D','E'});

% Histogram
data = randn(1, 1000);
histogram(data, 30);  % 30 bins

% Scatter plot
x = randn(100,1); y = 2*x + randn(100,1);
scatter(x, y, 'filled');

% Stem (rời rạc)
n = 0:20;
stem(n, sin(n*pi/10));
```

---

## 10. Nhập/Xuất Dữ Liệu Cơ Bản

### 10.1 Nhập Từ Bàn Phím
```matlab
x = input('Nhập số x: ');         % Nhập số
s = input('Nhập tên: ', 's');      % Nhập chuỗi
```

### 10.2 Lưu và Tải File .mat
```matlab
x = 1:10;
A = magic(4);
name = 'MATLAB';

% Lưu tất cả workspace
save('mydata.mat');

% Lưu biến cụ thể
save('mydata.mat', 'x', 'A', 'name');

% Tải dữ liệu
load('mydata.mat');        % Tải tất cả
load('mydata.mat', 'x');   % Tải biến x

% Kiểm tra nội dung file .mat
whos('-file', 'mydata.mat');
```

### 10.3 Đọc/Ghi File Text
```matlab
% Ghi file text
fid = fopen('output.txt', 'w');  % 'w': ghi mới, 'a': nối tiếp
fprintf(fid, 'Dòng 1\n');
fprintf(fid, 'x = %d\n', 42);
fclose(fid);

% Đọc file text
fid = fopen('output.txt', 'r');
line = fgetl(fid);   % Đọc từng dòng
while ischar(line)
    disp(line);
    line = fgetl(fid);
end
fclose(fid);

% Đọc file số (nhanh hơn)
data = load('numbers.txt');  % Đọc ma trận số từ file text
```

### 10.4 Đọc CSV / Excel
```matlab
% Đọc CSV
T = readtable('data.csv');              % Đọc vào table
data = readmatrix('data.csv');          % Đọc vào ma trận số
opts = detectImportOptions('data.csv'); % Tự động phát hiện kiểu

% Ghi CSV
writematrix(A, 'output.csv');
writetable(T, 'output.csv');

% Excel
T = readtable('data.xlsx', 'Sheet', 'Sheet1');
writematrix(A, 'output.xlsx');
```

---

## 💡 Mẹo và Thủ Thuật

```matlab
% 1. Preallocation - Cấp phát trước bộ nhớ (tăng tốc vòng lặp)
n = 10000;
result = zeros(1, n);  % ✅ Tốt
for i = 1:n
    result(i) = i^2;
end

% 2. Dùng ; để tắt output
A = rand(1000);  % ✅ Không hiển thị ma trận 1000x1000

% 3. Profile code để tìm bottleneck
profile on
% ... chạy code ...
profile off
profile viewer   % Xem phân tích

% 4. Keyboard shortcuts
% Ctrl+C: Dừng lệnh đang chạy
% Tab:    Tự động hoàn thành
% ↑↓:    Lịch sử lệnh
% F5:    Chạy script
% F9:    Chạy vùng được chọn

% 5. Format số hiển thị
format long    % Hiện nhiều chữ số thập phân
format short   % Mặc định (4 chữ số thập phân)
format rat     % Hiện phân số (2/3 thay vì 0.6667)
format compact % Bỏ dòng trống thừa
```

---

## 🏋️ Bài Tập Cơ Bản

**Bài 1**: Viết script tính và in bảng cửu chương từ 1 đến 9.

**Bài 2**: Viết hàm nhận vào một mảng số, trả về 3 giá trị: tổng, trung bình, và số lượng phần tử dương.

**Bài 3**: Tạo ma trận 5x5 với phần tử `A(i,j) = i^2 + j^2`. Tìm phần tử lớn nhất và vị trí của nó.

**Bài 4**: Vẽ đồ thị so sánh 4 hàm: `sin(x)`, `sin(2x)`, `2*sin(x)`, `sin(x+pi/4)` trên cùng một figure với chú thích đầy đủ.

**Bài 5**: Viết hàm kiểm tra số nguyên tố. Dùng hàm đó tìm tất cả số nguyên tố nhỏ hơn 100.

---

*[⬅ README](README.md) | [Tiếp theo: 02_Trung_Cap.md ➡](02_Trung_Cap.md)*
