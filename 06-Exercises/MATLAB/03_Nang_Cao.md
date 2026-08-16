# 🔴 MATLAB Nâng Cao

## Mục Lục
1. [Lập Trình Hướng Đối Tượng (OOP)](#1-lập-trình-hướng-đối-tượng)
2. [Handle Class và Value Class](#2-handle-class-và-value-class)
3. [Tối Ưu Hóa (Optimization)](#3-tối-ưu-hóa)
4. [Xử Lý Tín Hiệu (Signal Processing)](#4-xử-lý-tín-hiệu)
5. [Lập Trình Song Song](#5-lập-trình-song-song)
6. [MEX Files (C/C++ Integration)](#6-mex-files)
7. [MATLAB với Python](#7-matlab-với-python)
8. [Metaprogramming](#8-metaprogramming)
9. [Unit Testing](#9-unit-testing)
10. [Performance Tuning](#10-performance-tuning)

---

## 1. Lập Trình Hướng Đối Tượng

### 1.1 Classdef Cơ Bản
```matlab
% File: Animal.m
classdef Animal
    properties          % Thuộc tính public
        Name
        Species
    end
    
    properties (Access = private)  % Thuộc tính private
        energy = 100;
    end
    
    properties (Constant)  % Hằng số lớp
        WORLD = 'Earth';
    end
    
    methods
        % Constructor
        function obj = Animal(name, species)
            obj.Name    = name;
            obj.Species = species;
        end
        
        % Phương thức thông thường
        function speak(obj)
            fprintf('%s says hello!\n', obj.Name);
        end
        
        % Getter/Setter
        function e = get.energy(obj)
            e = obj.energy;
        end
        
        function obj = set.energy(obj, val)
            if val < 0 || val > 100
                error('Energy phải trong [0, 100]');
            end
            obj.energy = val;
        end
        
        % Overload toán tử
        function disp(obj)
            fprintf('Animal: %s (%s)\n', obj.Name, obj.Species);
        end
        
        function result = plus(a, b)
            % Overload toán tử +
            result = Animal([a.Name ' & ' b.Name], 'Hybrid');
        end
    end
    
    methods (Static)    % Phương thức tĩnh (không cần instance)
        function info()
            fprintf('Animal class - Học OOP MATLAB\n');
        end
    end
end
```

### 1.2 Kế Thừa (Inheritance)
```matlab
% File: Dog.m
classdef Dog < Animal    % Kế thừa từ Animal
    properties
        Breed
    end
    
    methods
        function obj = Dog(name, breed)
            obj = obj@Animal(name, 'Canis lupus'); % Gọi constructor cha
            obj.Breed = breed;
        end
        
        function speak(obj)
            fprintf('%s barks: Woof! Woof!\n', obj.Name);
        end
        
        function fetch(obj)
            fprintf('%s fetches the ball!\n', obj.Name);
        end
    end
end

% Sử dụng
d = Dog('Rex', 'Labrador');
d.speak();          % Gọi phương thức con: "Rex barks: Woof! Woof!"
d.fetch();
isa(d, 'Animal')    % 1 (true) - d IS-A Animal
isa(d, 'Dog')       % 1 (true)
```

### 1.3 Abstract Class và Interface
```matlab
% File: Shape.m
classdef Shape
    properties (Abstract)  % Subclass PHẢI định nghĩa
        Color
    end
    
    methods (Abstract)     % Subclass PHẢI implement
        area = getArea(obj)
        perimeter = getPerimeter(obj)
    end
    
    methods
        function describe(obj)
            fprintf('Shape with area = %.2f\n', obj.getArea());
        end
    end
end

% File: Circle.m
classdef Circle < Shape
    properties
        Color = 'red';
        Radius
    end
    
    methods
        function obj = Circle(r)
            obj.Radius = r;
        end
        
        function a = getArea(obj)
            a = pi * obj.Radius^2;
        end
        
        function p = getPerimeter(obj)
            p = 2 * pi * obj.Radius;
        end
    end
end
```

---

## 2. Handle Class và Value Class

```matlab
% VALUE class: mỗi assign tạo bản sao mới
% classdef MyValue ...  (mặc định)

% HANDLE class: chia sẻ tham chiếu (như pointer)
% classdef MyHandle < handle ...

% Ví dụ sự khác biệt:
classdef Counter < handle
    properties
        count = 0;
    end
    methods
        function increment(obj)
            obj.count = obj.count + 1;
        end
    end
end

c1 = Counter();
c2 = c1;      % c2 TRỎ vào cùng object (không phải bản sao!)
c1.increment();
c2.count      % 1 (bị thay đổi vì cùng object!)

% Handle class thường dùng cho:
% - Event systems
% - Objects cần modify trong phương thức
% - Linked lists, graphs
```

### 2.1 Events và Listeners
```matlab
classdef Button < handle
    events
        Clicked   % Định nghĩa event
    end
    
    methods
        function click(obj)
            notify(obj, 'Clicked');  % Phát event
        end
    end
end

classdef Logger < handle
    methods
        function onClicked(obj, src, event)
            fprintf('Button clicked at %s\n', datestr(now));
        end
    end
end

b = Button();
l = Logger();
addlistener(b, 'Clicked', @l.onClicked);  % Đăng ký listener
b.click();   % Trigger event -> Logger.onClicked được gọi
```

---

## 3. Tối Ưu Hóa (Optimization)

> Cần **Optimization Toolbox**

### 3.1 Tối Ưu Hóa Vô Ràng Buộc
```matlab
% Tìm min của f(x,y) = (x-3)^2 + (y-2)^2
f = @(v) (v(1)-3)^2 + (v(2)-2)^2;

% fminsearch: Nelder-Mead (không cần gradient)
x0 = [0, 0];
[x_opt, fval] = fminsearch(f, x0);
% x_opt ≈ [3, 2], fval ≈ 0

% fminunc: Quasi-Newton (dùng gradient)
options = optimoptions('fminunc', 'Algorithm', 'quasi-newton', ...
    'Display', 'iter', 'MaxIterations', 1000);
[x_opt, fval, exitflag, output] = fminunc(f, x0, options);
```

### 3.2 Tối Ưu Hóa Có Ràng Buộc
```matlab
% Minimize: f(x) = x1^2 + x2^2
% Subject to: x1 + x2 >= 3 (ràng buộc bất đẳng thức)
%             x1 - x2 = 1  (ràng buộc đẳng thức)
%             x1, x2 >= 0  (ràng buộc biên)

f    = @(x) x(1)^2 + x(2)^2;
Aineq = [-1, -1];  % Aineq*x <= bineq
bineq = [-3];      % -x1 - x2 <= -3  <=> x1+x2 >= 3
Aeq   = [1, -1];   % Aeq*x = beq
beq   = [1];       % x1 - x2 = 1
lb    = [0; 0];    % Giới hạn dưới
ub    = [];        % Không giới hạn trên

x0 = [1; 1];
[x_opt, fval] = fmincon(f, x0, Aineq, bineq, Aeq, beq, lb, ub);
```

### 3.3 Lập Trình Tuyến Tính (Linear Programming)
```matlab
% Maximize: 5x1 + 4x2 + 3x3
% = Minimize: -5x1 - 4x2 - 3x3
f = [-5; -4; -3];
A = [6 4 2; 3 2 5; 5 6 5];
b = [240; 270; 420];
lb = zeros(3,1);

[x, fval] = linprog(f, A, b, [], [], lb);
max_profit = -fval;   % Lợi nhuận tối đa
```

### 3.4 Tối Ưu Hóa Toàn Cục
```matlab
% Simulated Annealing
f = @(x) sin(5*x)*(x-0.3)^2 + cos(x);  % Nhiều cực tiểu địa phương
[x_opt, fval] = simulannealbnd(f, 0.5, 0, 1);

% Genetic Algorithm
[x_opt, fval] = ga(f, 1, [], [], [], [], 0, 1);

% Particle Swarm
[x_opt, fval] = particleswarm(f, 1, 0, 1);

% Surrogate Optimization
[x_opt, fval] = surrogateopt(f, 0, 1);
```

---

## 4. Xử Lý Tín Hiệu (Signal Processing)

> Cần **Signal Processing Toolbox**

### 4.1 FFT và Phổ Tần Số
```matlab
fs = 1000;          % Tần số lấy mẫu (Hz)
T  = 1/fs;          % Chu kỳ lấy mẫu
N  = 1024;          % Số mẫu
t  = (0:N-1)*T;     % Trục thời gian

% Tín hiệu tổng hợp: 50Hz + 150Hz + noise
f1 = 50; f2 = 150;
x = 0.7*sin(2*pi*f1*t) + 0.4*sin(2*pi*f2*t) + 0.1*randn(1,N);

% FFT
X  = fft(x);
X_mag = abs(X(1:N/2+1)) * 2/N;   % Biên độ một phía
freqs = fs * (0:N/2) / N;         % Trục tần số

figure;
subplot(2,1,1); plot(t(1:200), x(1:200)); xlabel('t (s)'); title('Tín hiệu');
subplot(2,1,2); plot(freqs, X_mag); xlabel('f (Hz)'); title('Phổ biên độ');
```

### 4.2 Lọc Tín Hiệu (Filtering)
```matlab
% Thiết kế bộ lọc thông thấp (Low-pass filter)
fs = 1000;
fc = 100;          % Tần số cắt (Hz)
order = 6;

% Butterworth filter
[b, a] = butter(order, fc/(fs/2));  % fc/Nyquist

% Kiểm tra đáp ứng tần số
freqz(b, a, [], fs);

% Lọc tín hiệu
x_filtered = filter(b, a, x);       % Có phase delay
x_zp       = filtfilt(b, a, x);     % Zero-phase (không delay, khuyến dùng)

% Các loại filter khác
[b, a] = butter(4, [50 200]/(fs/2), 'bandpass');  % Band-pass
[b, a] = butter(4, 100/(fs/2), 'high');            % High-pass
[b, a] = cheby1(4, 1, 100/(fs/2));  % Chebyshev type 1 (ripple in passband)
[b, a] = ellip(4, 1, 60, 100/(fs/2)); % Elliptic (steepest rolloff)

% FIR filter
b_fir = fir1(64, fc/(fs/2));        % Linear phase
x_fir = conv(x, b_fir, 'same');
```

### 4.3 STFT và Spectrogram
```matlab
% Short-time Fourier Transform
window = hamming(256);
overlap = 128;
nfft = 512;

figure;
spectrogram(x, window, overlap, nfft, fs, 'yaxis');
title('Spectrogram');
colorbar;
```

### 4.4 Xử Lý Tín Hiệu Thực Tế
```matlab
% Đọc file âm thanh
[y, fs] = audioread('audio.wav');
audioinfo('audio.wav')  % Thông tin file

% Phát âm thanh
sound(y, fs);
pause(length(y)/fs + 0.5);  % Đợi phát xong

% Tính envelope
y_abs = abs(hilbert(y));     % Hilbert envelope

% Resampling
y_new = resample(y, 22050, fs);  % Resample về 22050 Hz

% Ghi file
audiowrite('output.wav', y_new, 22050);
```

---

## 5. Lập Trình Song Song

### 5.1 Parallel Computing Toolbox
```matlab
% Mở parallel pool
p = parpool(4);   % 4 workers (CPUs)
% hoặc: parpool('local', maxNumCompThreads());

% parfor: thay for bằng parfor
tic;
n = 1000;
result = zeros(1, n);
parfor i = 1:n
    result(i) = expensive_function(i);  % Chạy song song!
end
toc;

% Lưu ý parfor:
% - Thứ tự lặp không xác định
% - Không thể dùng break/return
% - Biến phải "sliced" hoặc "broadcast" được

% Đóng pool
delete(p);
```

### 5.2 parfeval - Task Bất Đồng Bộ
```matlab
p = parpool(4);

% Gửi task bất đồng bộ
f1 = parfeval(p, @fft, 1, randn(1024,1));   % 1 output
f2 = parfeval(p, @svd, 3, rand(500));       % 3 outputs

% Làm việc khác trong khi đợi...
disp('Đang tính toán song song...');

% Lấy kết quả (block cho đến khi xong)
fft_result = fetchOutputs(f1);
[U, S, V]  = fetchOutputs(f2);
```

### 5.3 GPU Computing
```matlab
% Kiểm tra GPU
gpuDeviceCount()
gpuDevice()          % Thông tin GPU hiện tại

% Chuyển dữ liệu lên GPU
A_gpu = gpuArray(rand(1000));
B_gpu = gpuArray(rand(1000));

% Tính toán trên GPU (tự động!)
C_gpu = A_gpu * B_gpu;  % Ma trận nhân trên GPU

% Chuyển kết quả về CPU
C = gather(C_gpu);

% arrayfun trên GPU
result = arrayfun(@(x) sin(x)^2 + cos(x), gpuArray(1:1e6));
result_cpu = gather(result);
```

### 5.4 Shared Memory Arrays
```matlab
p = parpool(4);

% SharedMemory: tránh copy data
large_data = rand(1e6, 1);
shared = parallel.pool.Constant(large_data);  % Chia sẻ không copy

parfor i = 1:1000
    % Mỗi worker đọc shared.Value mà không copy
    chunk = shared.Value(i:i+100);
    process(chunk);
end
```

---

## 6. MEX Files

> MEX: MATLAB EXecutable - Gọi C/C++/Fortran từ MATLAB

### 6.1 Viết MEX File Đơn Giản
```c
// File: my_sum.c
#include "mex.h"

void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[])
{
    // Kiểm tra input
    if (nrhs != 1 || !mxIsDouble(prhs[0])) {
        mexErrMsgIdAndTxt("MyTool:invalidInput", "Cần 1 mảng double");
    }
    
    // Lấy pointer đến dữ liệu
    double *data = mxGetDoubles(prhs[0]);
    mwSize n     = mxGetNumberOfElements(prhs[0]);
    
    // Tạo output
    plhs[0] = mxCreateDoubleScalar(0);
    double *result = mxGetDoubles(plhs[0]);
    
    // Tính tổng
    for (mwSize i = 0; i < n; i++) {
        *result += data[i];
    }
}
```

```matlab
% Biên dịch MEX
mex my_sum.c

% Sử dụng
x = 1:1000000;
my_sum(x)   % Gọi như hàm MATLAB thông thường
```

### 6.2 Tối Ưu MEX với BLAS/LAPACK
```matlab
% Sử dụng thư viện tích hợp
mex -lmwblas -lmwlapack my_blas_code.c
```

---

## 7. MATLAB với Python

### 7.1 Gọi Python từ MATLAB
```matlab
% Kiểm tra Python
pyenv                   % Xem Python environment
pyenv('Version', '3.9') % Chọn phiên bản

% Gọi hàm Python
result = py.math.sqrt(16)     % 4.0
py.print('Hello from Python!')

% Import module
np = py.importlib.import_module('numpy');
arr = np.array([1, 2, 3, 4, 5]);
mean = np.mean(arr);          % 3.0

% Chuyển đổi kiểu dữ liệu
py_list = py.list({1, 2, 3});
mat_arr = double(py_list);    % Chuyển về MATLAB

% Gọi file Python
py.runfile('/path/to/script.py');
```

### 7.2 Gọi MATLAB từ Python
```python
# Cần cài: pip install matlabengine
import matlab.engine

eng = matlab.engine.start_matlab()

# Gọi hàm MATLAB
result = eng.sqrt(16.0)       # 4.0
eng.plot(eng.linspace(0, 2*eng.pi(), 100))
eng.eval("disp('Hello from Python!')")

# Truyền data
x = matlab.double([1, 2, 3, 4])
y = eng.fft(x)

eng.quit()
```

---

## 8. Metaprogramming

### 8.1 Function Handles và Closures
```matlab
% Closure: hàm "ghi nhớ" biến cục bộ
function f = make_multiplier(k)
    f = @(x) k * x;   % k được "capture" vào closure
end

double_it = make_multiplier(2);
triple_it = make_multiplier(3);
double_it(5)   % 10
triple_it(5)   % 15

% Currying
add = @(a) @(b) a + b;
add5 = add(5);
add5(3)   % 8
add5(10)  % 15
```

### 8.2 feval và Strings Làm Function Names
```matlab
func_name = 'sin';
feval(func_name, pi/2)   % 1.0 - gọi sin(pi/2)

% Tạo hàm động từ string expression
f = str2func('@(x) x.^2 + 2*x + 1');
f(3)   % 16

% eval (cẩn thận - security risk nếu từ user input)
expr = 'x = 10; y = x^2';
eval(expr);   % Thực thi code từ string
```

### 8.3 Meta-information
```matlab
% Introspection
methods('containers.Map')     % Liệt kê phương thức của class
properties('gaussian')        % Liệt kê thuộc tính
superclasses('Dog')           % Lớp cha

% Meta class
mc = ?Dog;                    % Meta-class object
mc.MethodList                 % Danh sách method
mc.PropertyList               % Danh sách property

% Kiểm tra sự tồn tại
exist('sin', 'builtin')       % 5 - built-in function
exist('interp1', 'file')      % 2 - m-file tồn tại
which('sin')                  % Đường dẫn đầy đủ
```

### 8.4 inputParser
```matlab
function result = flexible_func(varargin)
    p = inputParser();
    addRequired(p, 'x');                       % Tham số bắt buộc
    addOptional(p, 'n', 2);                    % Tùy chọn có default
    addParameter(p, 'verbose', false);         % Named parameter
    addParameter(p, 'method', 'default', ...
        @(x) ismember(x, {'default','fast','accurate'})); % Với validation
    
    parse(p, varargin{:});
    
    x       = p.Results.x;
    n       = p.Results.n;
    verbose = p.Results.verbose;
    method  = p.Results.method;
    
    if verbose
        fprintf('Computing x^%d using %s method\n', n, method);
    end
    result = x^n;
end

% Gọi
flexible_func(3)                             % 9
flexible_func(3, 3)                          % 27
flexible_func(3, 'verbose', true)            % in log + return 9
flexible_func(3, 4, 'method', 'fast')        % 81
```

---

## 9. Unit Testing

### 9.1 Script-based Tests
```matlab
% File: test_my_function.m
% Chạy: runtests('test_my_function')

function tests = test_my_function
    tests = functiontests(localfunctions);
end

function test_positive_input(testCase)
    result = my_function(5);
    verifyEqual(testCase, result, 25);
end

function test_zero_input(testCase)
    result = my_function(0);
    verifyEqual(testCase, result, 0);
end

function test_negative_input(testCase)
    verifyError(testCase, @() my_function(-1), 'MyFunc:negativeInput');
end

function test_floating_point(testCase)
    result = my_function(0.1 + 0.2);
    verifyEqual(testCase, result, 0.09, 'AbsTol', 1e-10);
end
```

### 9.2 Class-based Tests
```matlab
% File: TestMyClass.m
classdef TestMyClass < matlab.unittest.TestCase
    properties
        data
    end
    
    methods (TestMethodSetup)    % Chạy trước mỗi test
        function setup(testCase)
            testCase.data = [1 2 3 4 5];
        end
    end
    
    methods (TestMethodTeardown) % Chạy sau mỗi test
        function teardown(testCase)
            % cleanup
        end
    end
    
    methods (Test)
        function testMean(testCase)
            testCase.verifyEqual(mean(testCase.data), 3.0);
        end
        
        function testSize(testCase)
            testCase.verifySize(testCase.data, [1, 5]);
        end
        
        function testClass(testCase)
            testCase.verifyClass(testCase.data, 'double');
        end
    end
    
    methods (Test, TestTags = {'slow'})
        function testSlowOperation(testCase)
            % Tag 'slow' để có thể skip: runtests('TestMyClass', 'Tag', '~slow')
            result = svd(rand(1000));
            testCase.verifyNotEmpty(result);
        end
    end
end

% Chạy tests
results = runtests('TestMyClass');
table(results)   % Bảng kết quả đẹp
```

---

## 10. Performance Tuning

### 10.1 Profiling Chuyên Sâu
```matlab
% Profile từng dòng
profile on -detail builtin   % Bao gồm cả built-in
run_my_algorithm();
profile off

% Xuất báo cáo
profsave(profile('info'), 'profile_results');  % HTML report
p = profile('info');
p.FunctionTable(1)   % Thông tin hàm tốn nhiều thời gian nhất
```

### 10.2 Memory Optimization
```matlab
% Kiểm tra bộ nhớ
memory                           % Xem RAM hiện có
whos                             % Xem kích thước biến

% Dùng kiểu dữ liệu nhỏ hơn khi có thể
A_single = single(rand(1000));   % 4 bytes/phần tử (thay vì 8)
A_uint8  = uint8(rand(1000)*255);% 1 byte/phần tử

% Tránh copy không cần thiết (copy-on-write)
function result = no_copy(A)
    result = A(1:end, :);   % Không copy nếu không sửa A
end

% Sparse matrix cho ma trận thưa
A_dense  = rand(1000); A_dense(A_dense < 0.99) = 0;
A_sparse = sparse(A_dense);     % Tiết kiệm bộ nhớ đáng kể!
whos A_dense A_sparse

% Giải phóng bộ nhớ
clear large_variable;
pack;    % Compact memory (giảm fragmentation)
```

### 10.3 Precompile và Cache
```matlab
% Precompute thay vì tính lại nhiều lần
% ❌ Chậm
for i = 1:1000
    x = i * sin(pi/180 * 45);  % sin(pi/4) tính 1000 lần
end

% ✅ Nhanh
sin45 = sin(pi/4);
for i = 1:1000
    x = i * sin45;
end

% Persistent variable (giống static trong C)
function result = cached_fib(n)
    persistent cache;
    if isempty(cache)
        cache = containers.Map('KeyType','int32','ValueType','double');
    end
    
    if isKey(cache, int32(n))
        result = cache(int32(n));
        return;
    end
    
    if n <= 2
        result = 1;
    else
        result = cached_fib(n-1) + cached_fib(n-2);
    end
    cache(int32(n)) = result;
end
```

### 10.4 Vectorization Nâng Cao
```matlab
% Tránh dynamic resizing (quan trọng nhất!)
% ❌ Rất chậm: mảng mở rộng mỗi lần lặp
result = [];
for i = 1:10000
    result = [result, i^2];  % Cấp phát lại bộ nhớ!
end

% ✅ Prealloc + fill
result = zeros(1, 10000);
for i = 1:10000
    result(i) = i^2;
end

% ✅✅ Vectorized (tốt nhất)
result = (1:10000).^2;

% bsxfun vs implicit expansion benchmark
A = rand(1000, 1);
B = rand(1, 500);
tic; C1 = bsxfun(@plus, A, B); t1=toc;    % Cũ
tic; C2 = A + B; t2=toc;                   % Mới (R2016b+), tương đương
fprintf('bsxfun: %.4fs, implicit: %.4fs\n', t1, t2);

% cellfun vs loop
C = num2cell(rand(1, 10000));
tic; r1 = cellfun(@(x) x^2, C); t1=toc;               % cellfun
tic; r2 = cell2mat(C).^2; t2=toc;                     % convert+vectorize (nhanh hơn)
fprintf('cellfun: %.4fs, vectorized: %.4fs\n', t1, t2);
```

---

## 💡 Tips Nâng Cao

```matlab
% 1. Dùng nargout để tránh tính toán không cần thiết
function [result, details] = expensive_analysis(data)
    result = quick_compute(data);
    if nargout > 1
        details = slow_detailed_compute(data);  % Chỉ tính khi cần
    end
end
r = expensive_analysis(data);         % Nhanh, không tính details
[r, d] = expensive_analysis(data);    % Chậm hơn, tính cả details

% 2. onCleanup - đảm bảo cleanup khi hàm kết thúc
function safe_file_processing(filename)
    fid = fopen(filename);
    cleaner = onCleanup(@() fclose(fid));  % Tự đóng file dù có lỗi hay không!
    % ... xử lý file ...
end  % fid tự đóng ở đây

% 3. validateattributes - kiểm tra đầu vào chuyên nghiệp
function result = safe_sqrt(x)
    validateattributes(x, {'numeric'}, {'scalar','nonnegative','finite'}, ...
        'safe_sqrt', 'x', 1);
    result = sqrt(x);
end

% 4. Logging chuyên nghiệp
import matlab.unittest.diagnostics.Diagnostic.*
logger = matlab.io.MatFile('run_log.mat', 'Writable', true);
```

---

## 🏋️ Bài Tập Nâng Cao

**Bài 1**: Implement một lớp `Matrix` với OOP: overload `+`, `-`, `*`, `display`; thêm phương thức `inv()`, `det()`, `rank()`. Viết unit tests.

**Bài 2**: Viết hàm tối ưu `min_surface_area(V)` tìm hình hộp chữ nhật có thể tích **V** với diện tích bề mặt nhỏ nhất (dùng `fmincon`).

**Bài 3**: Thiết kế bộ lọc Butterworth lowpass 8th-order, lọc tín hiệu nhiễu EMG, phân tích STFT trước và sau lọc.

**Bài 4**: Dùng `parfor` để tính Pi bằng Monte Carlo với N = 1e8 điểm, so sánh thời gian với `for` thông thường.

**Bài 5**: Viết MEX file C tính convolution 1D nhanh hơn MATLAB built-in `conv` (dùng thuật toán overlap-add hoặc FFT).

---

*[⬅ 02_Trung_Cap.md](02_Trung_Cap.md) | [Tiếp theo: 04_Ung_Dung.md ➡](04_Ung_Dung.md)*
