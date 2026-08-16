# 🔧 MATLAB & MCR INTEGRATION - ÔN THI PHỎNG VẤN

> **Điểm đặc biệt trong CV của bạn:** Tích hợp MATLAB Compiler Runtime (MCR) vào production Python server  
> Đây là kỹ năng rất hiếm và sẽ là điểm nổi bật trong phỏng vấn!

---

## 1. MATLAB LÀ GÌ VÀ DÙNG KHI NÀO?

### 1.1 Tổng quan MATLAB
```
MATLAB (Matrix Laboratory) là ngôn ngữ lập trình và môi trường tính toán 
cho toán học, khoa học kỹ thuật, và xử lý dữ liệu.

Ưu điểm:
- Tối ưu hóa matrix/vector operations
- Built-in toolboxes: Signal Processing, Statistics, Machine Learning
- Tính toán số học chính xác cao
- Visualization mạnh mẽ

Trong dự án MBW của bạn:
- Thuật toán scoring phức tạp phân tích candidate-job compatibility
- Ma trận dữ liệu ứng viên × yêu cầu công việc
- Hệ số phân tích đa biến (multivariate analysis)
```

---

## 2. KIẾN THỨC MATLAB CẦN NẮM

### 2.1 Kiểu dữ liệu cơ bản
```matlab
% Scalar
x = 5;
y = 3.14;
z = true;

% Vector (hàng ngang)
row_vec = [1, 2, 3, 4, 5];
% Vector (cột dọc)
col_vec = [1; 2; 3; 4; 5];

% Ma trận
A = [1, 2, 3; 4, 5, 6; 7, 8, 9];  % 3×3 matrix

% String
name = "Phạm Duy Tín";
name_char = 'Hello';  % char array

% Cell array (giống list trong Python)
cell_data = {1, "hello", [1,2,3], true};

% Struct (giống dict trong Python)
person.name = "Tin";
person.age = 22;
person.skills = {"Python", "MATLAB"};
```

**📋 Output thực tế (bỏ dấu `;` để thấy):**
```
>> row_vec = [1, 2, 3, 4, 5]
row_vec =
   1   2   3   4   5

>> col_vec = [1; 2; 3; 4; 5]
col_vec =
   1
   2
   3
   4
   5

>> A = [1, 2, 3; 4, 5, 6; 7, 8, 9]
A =
   1   2   3
   4   5   6
   7   8   9

>> person
person =
  struct with fields:
    name: 'Tin'
     age: 22
  skills: {'Python', 'MATLAB'}
```

> **🎯 Tại sao MATLAB dùng ma trận làm kiểu dữ liệu cơ bản?**
> - Mọi scalar thực ra là ma trận 1×1
> - Operations được tối ưu hóa cấp phần cứng (BLAS/LAPACK)
> - Phù hợp cho tính toán khoa học kỹ thuật

---

### 2.2 Matrix Operations
```matlab
A = [1, 2; 3, 4];
B = [5, 6; 7, 8];

% Phép toán ma trận
C = A + B;       % Cộng element-wise
D = A * B;       % Matrix multiplication (nhân ma trận thực sự)
E = A .* B;      % Element-wise multiplication (NOT matrix mult)
F = A ^ 2;       % Ma trận bình phương (A*A)
G = A .^ 2;      % Element-wise square

% Transpose
A_T = A';         % Transpose

% Inverse & Determinant
inv_A = inv(A);   % Ma trận nghịch đảo
det_A = det(A);   % Định thức

% Eigen values
[V, D] = eig(A);  % V: eigenvectors, D: eigenvalues (diagonal)

% Giải hệ phương trình Ax = b
b = [1; 2];
x = A \ b;  % Hiệu quả hơn inv(A)*b

% Kích thước
[rows, cols] = size(A);
n = length(A);        % max(rows, cols)
total = numel(A);     % tổng số phần tử
```

**📋 Output thực tế:**
```
>> C = A + B
C =
   6   8
  10  12

>> D = A * B       % matrix mult: (1*5+2*7) (1*6+2*8) / (3*5+4*7) (3*6+4*8)
D =
  19  22
  43  50

>> E = A .* B      % element-wise: 1*5, 2*6, 3*7, 4*8
E =
    5   12
   21   32

>> G = A .^ 2      % bình phương từng phần tử
G =
    1    4
    9   16

>> det_A = det(A)  % 1*4 - 2*3 = -2
det_A = -2

>> x = A \ b       % giải: x1 + 2*x2 = 1; 3*x1 + 4*x2 = 2
x =
   0
   0.5000

>> [rows, cols] = size(A)
rows = 2
cols = 2

>> total = numel(A)
total = 4
```

> **🎯 Dùng khi nào?**
> - `.` trước operator = element-wise (từng phần tử)
> - Không có `.` = matrix operation
> - `A \ b` thay vì `inv(A)*b` → nhanh hơn và chính xác hơn

---

### 2.3 Indexing và Slicing
```matlab
A = [10, 20, 30; 40, 50, 60; 70, 80, 90];

% MATLAB index bắt đầu từ 1 (khác Python bắt đầu từ 0!)
A(1, 1)     % = 10 (hàng 1, cột 1)
A(2, 3)     % = 60
A(end, end) % = 90 (cuối cùng)

% Slicing
A(1, :)     % Hàng 1 toàn bộ: [10, 20, 30]
A(:, 2)     % Cột 2 toàn bộ: [20; 50; 80]
A(1:2, 2:3) % Sub-matrix: [20,30; 50,60]

% Linear indexing (column-major!)
A(1)  % = 10 (cột 1, hàng 1)
A(4)  % = 20 (cột 2, hàng 1) - KHÁC PYTHON!
% Python: row-major (C-style)
% MATLAB: column-major (Fortran-style)

% Logical indexing
v = [1, 5, 3, 8, 2];
v(v > 3)    % [5, 8] - phần tử > 3
v(logical([1,0,1,0,1]))  % [1, 3, 2]
```

**📋 Output thực tế:**
```
% Ma trận A được lưu trong bộ nhớ theo cột (column-major):
% Vị trí:  1   4   7
%           2   5   8
%           3   6   9
% Giá trị: 10  20  30
%          40  50  60
%          70  80  90

>> A(1,1)
ans = 10

>> A(2,3)
ans = 60

>> A(1, :)           % hàng 1
ans =  10  20  30

>> A(:, 2)           % cột 2
ans =
   20
   50
   80

>> A(1:2, 2:3)       % sub-matrix
ans =
   20  30
   50  60

>> A(4)              % linear index theo CỘT: cột 2, hàng 1 = 20
ans = 20
% ⚠️ Python: A.flatten()[3] = 40 (theo HÀNG) → KẾT QUẢ KHÁC NHAU!

>> v(v > 3)
ans =  5  8

>> v(logical([1,0,1,0,1]))
ans =  1  3  2
```

> **⚠️ QUAN TRỌNG khi tích hợp Python↔MATLAB:**
> - MATLAB index từ **1**, Python từ **0**
> - MATLAB **column-major**, Python/NumPy **row-major** (default)
> - Khi truyền data, cần chú ý reshape/transpose

---

### 2.4 Control Flow
```matlab
% if-else
score = 85;
if score >= 90
    grade = 'A';
elseif score >= 70
    grade = 'B';
else
    grade = 'C';
end

% for loop
total = 0;
for i = 1:10      % 1 đến 10 (inclusive cả hai đầu!)
    total = total + i;
end

% while loop
n = 1;
while n < 100
    n = n * 2;
end

% Vectorize thay vì loop (MATLAB best practice!)
% CHẬM:
for i = 1:1000
    result(i) = i^2;
end

% NHANH HƠN (vectorized):
result = (1:1000).^2;
```

**📋 Output thực tế:**
```
>> score = 85; if score>=90, grade='A'; elseif score>=70, grade='B'; else grade='C'; end
>> grade
grade = 'B'

>> total = 0; for i=1:10, total = total+i; end
>> total
total = 55      % = 1+2+3+...+10 = 10*(10+1)/2

>> n = 1; while n < 100, n = n*2; end
>> n
n = 128         % 1→2→4→8→16→32→64→128 (vượt 100 thì dừng)

>> result = (1:5).^2    % ví dụ 5 phần tử đầu
result =
    1    4    9   16   25
```

> **🎯 Vectorization là key trong MATLAB!**
> - Tránh for loops khi có thể
> - MATLAB tối ưu hóa vector/matrix ops
> - Tương tự như NumPy trong Python

---

### 2.5 Functions trong MATLAB
```matlab
% Function file: calculate_score.m
function [score, breakdown] = calculate_score(candidate_matrix, weights)
% Tính điểm phù hợp ứng viên với công việc
%
% Inputs:
%   candidate_matrix - Ma trận kỹ năng ứng viên (n_skills × 1)
%   weights          - Vector trọng số từng kỹ năng (n_skills × 1)
%
% Outputs:
%   score     - Tổng điểm (scalar)
%   breakdown - Chi tiết từng kỹ năng (vector)

% Validate inputs
if nargin < 2   % nargin = number of arguments in 
    weights = ones(size(candidate_matrix));  % Default: equal weights nếu trường hơp 
end

if length(candidate_matrix) ~= length(weights)
    error('Dimension mismatch: candidate_matrix and weights must have same length');
end

% Normalize weights
weights = weights / sum(weights);

% Calculate weighted score
breakdown = candidate_matrix .* weights;
score = sum(breakdown) * 100;

end  % end function


% Anonymous function (tương tự lambda Python)
square = @(x) x.^2;
result = square([1, 2, 3, 4]);  % [1, 4, 9, 16]

% Function handle (pass function như argument)
f = @sin;
result = arrayfun(f, 0:pi/4:pi);
```

**📋 Output thực tế khi gọi hàm:**
```
% Ví dụ 1: Gọi đủ 2 tham số
>> candidate = [0.8, 0.6, 0.9];   % Python=0.8, SQL=0.6, Docker=0.9
>> weights   = [0.5, 0.3, 0.2];   % Python quan trọng nhất
>> [score, breakdown] = calculate_score(candidate, weights)

% Bên trong hàm:
%   weights sau normalize = [0.5, 0.3, 0.2]  (tổng = 1.0, giữ nguyên)
%   breakdown = [0.8*0.5, 0.6*0.3, 0.9*0.2] = [0.40, 0.18, 0.18]
%   score = (0.40 + 0.18 + 0.18) * 100 = 76.0

breakdown =
   0.4000   0.1800   0.1800

score = 76

% Ví dụ 2: Chỉ 1 tham số → nargin=1 < 2 → weights tự động = [1,1,1]
>> [score2, bd2] = calculate_score([0.8, 0.6, 0.9])
%   weights normalize = [1/3, 1/3, 1/3] = [0.333, 0.333, 0.333]
%   breakdown = [0.267, 0.200, 0.300]
%   score = 0.767 * 100 = 76.67
score2 = 76.6667

% Ví dụ 3: Dimension mismatch → error
>> calculate_score([0.8, 0.6], [0.5, 0.3, 0.2])
Error using calculate_score
Dimension mismatch: candidate_matrix and weights must have same length

% Anonymous function
>> square = @(x) x.^2;
>> square([1, 2, 3, 4])
ans =
    1    4    9   16

% Function handle + arrayfun
>> f = @sin;
>> arrayfun(f, 0:pi/4:pi)
ans =
        0   0.7071   1.0000   0.7071   0.0000
%  sin(0)  sin(π/4)  sin(π/2) sin(3π/4) sin(π)
```

---

### 2.6 Data Analysis Functions
```matlab
data = [85, 90, 78, 92, 88, 75, 95];

% Thống kê cơ bản
avg = mean(data);          % Trung bình = 86.14
med = median(data);        % Trung vị = 88
sd = std(data);            % Độ lệch chuẩn
var = var(data);           % Phương sai
mn = min(data);            % Min = 75
mx = max(data);            % Max = 95
rng = range(data);         % Max - Min = 20

% Sorting
[sorted, idx] = sort(data, 'descend');
% sorted: [95, 92, 90, 88, 85, 78, 75]
% idx: vị trí gốc của phần tử

% Normalization
data_norm = (data - min(data)) / (max(data) - min(data));  % [0, 1]
data_z = zscore(data);  % Z-score normalization

% Correlation
A = rand(100, 5);  % 100 samples, 5 features
corr_matrix = corrcoef(A);  % 5×5 correlation matrix

% Linear regression
x = 1:10;
y = 2*x + randn(1,10);  % y = 2x + noise
p = polyfit(x, y, 1);   % p = [slope, intercept]
y_pred = polyval(p, x);
```

**📋 Output thực tế:**
```
>> data = [85, 90, 78, 92, 88, 75, 95];

>> mean(data)
ans = 86.1429

>> median(data)
ans = 88

>> std(data)
ans = 7.0397

>> [sorted, idx] = sort(data, 'descend')
sorted =
   95   92   90   88   85   78   75
idx =
    7    4    2    5    1    3    6
% idx cho biết: phần tử lớn nhất (95) ở vị trí 7 trong data gốc

>> data_norm = (data - min(data)) / (max(data) - min(data))
data_norm =
   0.5000   0.7500   0.1500   0.8500   0.6500        0   1.0000
% 75 → 0.0 (min), 95 → 1.0 (max), 85 → 0.5 (giữa)

>> x = 1:10; y = 2*x;  % lý tưởng không noise
>> p = polyfit(x, y, 1)
p =
   2.0000   0.0000    % [slope=2, intercept≈0] → y = 2x + 0
% Với noise thực tế: p ≈ [1.98, 0.15] (gần đúng y = 2x)
```

---

## 3. MATLAB COMPILER RUNTIME (MCR) INTEGRATION

### 3.1 Tổng quan MCR
```
MCR (MATLAB Compiler Runtime) cho phép chạy MATLAB code 
mà KHÔNG cần cài đặt MATLAB license.

Workflow:
1. Developer viết MATLAB code → Test trong MATLAB IDE
2. Compile code thành shared library (.so trên Linux, .dll trên Windows)
3. Deploy MCR Runtime + compiled library lên server
4. Python/Java/C++ gọi functions từ library qua wrapper
```

```
Trong dự án MBW của bạn:
- MATLAB: Thuật toán scoring proprietary
- Compile → libscoring.so (Linux shared library)
- Python: Gọi MATLAB function qua matlab.engine hoặc subprocess
- Server: Linux với MCR installed
```

---

### 3.2 Compile MATLAB code
```matlab
% Bước 1: Tạo function file (matlab_scorer.m)
function result = matlab_scorer(candidate_data, job_requirements)
    % candidate_data: n×m matrix (n candidates, m skills)
    % job_requirements: 1×m weight vector
    
    n_candidates = size(candidate_data, 1);
    result = zeros(n_candidates, 1);
    
    for i = 1:n_candidates
        result(i) = dot(candidate_data(i,:), job_requirements) / ...
                    (norm(candidate_data(i,:)) * norm(job_requirements) + 1e-8);
    end
end
```

```bash
# Bước 2: Compile thành Python package
# Chạy trong MATLAB hoặc command line
mcc -W python:MatlabScorer -T link:lib matlab_scorer.m

# Hoặc compile thành shared library
mcc -W lib:libscorer -T link:lib matlab_scorer.m
# Output: libscorer.so (Linux), libscorer.dll (Windows)

# Hoặc compile thành standalone executable
mcc -m matlab_scorer.m
# Output: matlab_scorer (executable)
```

---

### 3.3 Gọi MCR từ Python

#### Cách 1: matlab.engine (cần MATLAB installed)
```python
import matlab.engine
import numpy as np

# Khởi động MATLAB engine
eng = matlab.engine.start_matlab()

# Gọi function
candidate_data = np.array([[0.8, 0.9, 0.7], [0.6, 0.8, 0.9]])
job_req = np.array([0.9, 0.8, 0.7])

# Convert numpy → matlab array
matlab_candidate = matlab.double(candidate_data.tolist())
matlab_job = matlab.double(job_req.tolist())

# Gọi MATLAB function
result = eng.matlab_scorer(matlab_candidate, matlab_job)

# Convert về numpy
scores = np.array(result._data).reshape(result.size)
print(scores)  # [0.95, 0.88]

eng.quit()
```

#### Cách 2: Compiled Python package (MCR - production)
```python
# Sau khi compile với mcc -W python
import MatlabScorer  # compiled package
import matlab

# Khởi tạo runtime (chỉ làm 1 lần, tốn ~5-10s)
my_matlab = MatlabScorer.initialize()

# Convert data
candidate_data = matlab.double([[0.8, 0.9, 0.7], [0.6, 0.8, 0.9]])
job_req = matlab.double([0.9, 0.8, 0.7])

# Gọi function
scores = my_matlab.matlab_scorer(candidate_data, job_req)

my_matlab.terminate()
```

#### Cách 3: Subprocess (đơn giản nhất, production-safe)
```python
import subprocess
import json
import numpy as np
import tempfile
import os

def call_matlab_scorer(candidate_data: np.ndarray, job_req: np.ndarray) -> np.ndarray:
    """
    Gọi MATLAB scorer qua subprocess
    candidate_data: (n_candidates, n_skills) numpy array
    job_req: (n_skills,) numpy array
    Returns: (n_candidates,) scores array
    """
    # Tạo input file tạm
    input_data = {
        "candidates": candidate_data.tolist(),
        "requirements": job_req.tolist()
    }

    with tempfile.NamedTemporaryFile(suffix=".json", mode="w", delete=False) as f:
        json.dump(input_data, f)
        input_file = f.name

    output_file = input_file.replace(".json", "_output.json")

    try:
        # Gọi MATLAB compiled executable
        result = subprocess.run(
            ["/opt/matlab/scorer", input_file, output_file],
            capture_output=True,
            text=True,
            timeout=30,  # timeout 30 giây
            env={**os.environ, "LD_LIBRARY_PATH": "/usr/local/MATLAB/R2023b/runtime/glnxa64"}
        )

        if result.returncode != 0:
            raise RuntimeError(f"MATLAB Error: {result.stderr}")

        # Đọc output
        with open(output_file) as f:
            output = json.load(f)

        return np.array(output["scores"])

    finally:
        # Cleanup temp files
        os.unlink(input_file)
        if os.path.exists(output_file):
            os.unlink(output_file)
```

---

### 3.4 Production MATLAB trong Flask (như dự án MBW)
```python
# services/matlab_service.py
import matlab
import MatlabScorer
import numpy as np
from threading import Lock
import logging

logger = logging.getLogger(__name__)

class MatlabScoringService:
    """
    Singleton service quản lý MATLAB Runtime.
    MCR tốn nhiều memory, chỉ khởi tạo 1 lần.
    Thread-safe với Lock.
    """
    _instance = None
    _lock = Lock()
    _matlab_runtime = None

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Khởi tạo MCR - chỉ chạy 1 lần khi app start"""
        logger.info("Initializing MATLAB Compiler Runtime...")
        try:
            self._matlab_runtime = MatlabScorer.initialize()
            logger.info("MCR initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize MCR: {e}")
            raise

    def calculate_match_score(
        self,
        candidate_skills: list,
        job_requirements: list
    ) -> dict:
        """
        Tính điểm phù hợp candidate với job.

        Args:
            candidate_skills: List of skill scores [0-1] for each skill
            job_requirements: List of required skill weights [0-1]

        Returns:
            Dict with 'total_score', 'breakdown', 'recommendation'
        """
        if len(candidate_skills) != len(job_requirements):
            raise ValueError("Dimension mismatch between candidate skills and requirements")

        # Convert to MATLAB arrays
        matlab_candidate = matlab.double([candidate_skills])
        matlab_requirements = matlab.double([job_requirements])

        # Gọi MATLAB với lock để thread-safe
        with self._lock:
            try:
                result = self._matlab_runtime.score_candidate(
                    matlab_candidate,
                    matlab_requirements,
                    nargout=2  # Số lượng output values
                )
            except Exception as e:
                logger.error(f"MATLAB scoring failed: {e}")
                raise RuntimeError(f"Scoring calculation error: {e}")

        total_score = float(result[0])
        breakdown = list(result[1])

        return {
            "total_score": round(total_score * 100, 2),
            "breakdown": {f"skill_{i}": round(v, 3) for i, v in enumerate(breakdown)},
            "recommendation": "Strong Match" if total_score > 0.8 else
                            "Good Match" if total_score > 0.6 else "Weak Match"
        }

    def cleanup(self):
        """Cleanup khi app shutdown"""
        if self._matlab_runtime:
            self._matlab_runtime.terminate()
            logger.info("MCR terminated")


# Flask integration
# app/__init__.py
matlab_service = None

def create_app():
    app = Flask(__name__)
    # ...

    # Khởi tạo MATLAB service sau khi app created
    global matlab_service
    matlab_service = MatlabScoringService()

    @app.teardown_appcontext
    def cleanup(e=None):
        pass  # MCR cleanup on app shutdown only

    import atexit
    atexit.register(lambda: matlab_service.cleanup())

    return app


# API endpoint
@api_bp.route("/score-candidate", methods=["POST"])
@jwt_required()
def score_candidate():
    data = request.get_json()
    candidate = Candidate.query.get_or_404(data["candidate_id"])
    job = Job.query.get_or_404(data["job_id"])

    # Extract skill vectors
    candidate_skills = [candidate.skills.get(skill, 0) for skill in SKILL_LIST]
    job_requirements = [job.requirements.get(skill, 0) for skill in SKILL_LIST]

    try:
        result = matlab_service.calculate_match_score(candidate_skills, job_requirements)
        return jsonify(result)
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500
```

---

### 3.5 Linux Deployment với MCR
```bash
# Cài đặt MCR trên Linux (không cần MATLAB license)
# Download từ MathWorks website
chmod +x MCR_R2023b_glnxa64_installer.zip
unzip MCR_R2023b_glnxa64_installer.zip
./install -mode silent -agreeToLicense yes -destinationFolder /usr/local/MATLAB/R2023b

# Set environment variables
export LD_LIBRARY_PATH=/usr/local/MATLAB/R2023b/runtime/glnxa64:\
/usr/local/MATLAB/R2023b/bin/glnxa64:\
/usr/local/MATLAB/R2023b/sys/os/glnxa64:$LD_LIBRARY_PATH

export XAPPLRESDIR=/usr/local/MATLAB/R2023b/X11/app-defaults

# Docker deployment
```

```dockerfile
# Dockerfile với MCR
FROM python:3.11-slim

# Install MCR dependencies
RUN apt-get update && apt-get install -y \
    libxt6 libxmu6 libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copy MCR (đã install sẵn)
COPY --from=mcr-base /usr/local/MATLAB/R2023b /usr/local/MATLAB/R2023b

# Set MCR environment
ENV LD_LIBRARY_PATH=/usr/local/MATLAB/R2023b/runtime/glnxa64:\
/usr/local/MATLAB/R2023b/bin/glnxa64:$LD_LIBRARY_PATH
ENV MCR_ROOT=/usr/local/MATLAB/R2023b

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy compiled MATLAB package
COPY MatlabScorer/ /app/MatlabScorer/

COPY . /app/
WORKDIR /app

CMD ["gunicorn", "app:create_app()", "--bind", "0.0.0.0:5000"]
```

---

## 4. CÂU HỎI PHỎNG VẤN VỀ MATLAB/MCR

### Q1: Tại sao lại chọn MATLAB thay vì Python (scikit-learn, scipy)?
```
Trả lời mẫu:
"Thuật toán scoring trong dự án MBW là proprietary algorithm đã được phát triển 
và validate bởi domain experts trong MATLAB. Việc port sang Python có thể gây 
sai số trong floating-point calculations và mất đi trình độ tối ưu hóa 
của MATLAB BLAS/LAPACK.

MCR cho phép chúng tôi:
1. Giữ nguyên thuật toán gốc, không risk regression
2. Deploy không cần MATLAB license (tiết kiệm chi phí)
3. Tích hợp seamlessly với Python Flask backend
4. Scale independent component"
```

### Q2: Làm sao xử lý memory leak khi MATLAB Runtime?
```python
# Giải pháp: Singleton pattern + cleanup

# Vấn đề: MCR tốn ~500MB RAM mỗi instance
# Giải pháp: Chỉ 1 instance cho toàn bộ app (Singleton)

class MatlabScoringService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Cleanup on shutdown
import atexit
atexit.register(matlab_service.cleanup)
```

### Q3: Tại sao dùng subprocess thay vì matlab.engine trực tiếp?
```
"matlab.engine đòi hỏi MATLAB installed, không phải MCR.
Trong production với Docker:
1. MCR nhỏ hơn và free để distribute
2. Subprocess tách biệt memory space → crash không ảnh hưởng main app
3. Timeout control tốt hơn
4. Dễ debug và log output riêng biệt"
```

### Q4: Làm sao đảm bảo accuracy khi convert NumPy ↔ MATLAB?
```python
# Potential pitfall: Column-major vs Row-major
import numpy as np
import matlab

# NumPy: row-major (C order)
np_matrix = np.array([[1, 2, 3], [4, 5, 6]])

# MATLAB: column-major (Fortran order)
# Cần convert đúng cách
matlab_matrix = matlab.double(np_matrix.tolist())
# Hoặc: matlab.double(np_matrix.flatten(order='F').tolist(), size=(2,3))

# Verify
result = matlab_runtime.compute(matlab_matrix)
result_np = np.array(result._data).reshape(result.size, order='F')
```

---

## 5. MATLAB SIGNAL PROCESSING (ECG Project liên quan)
```matlab
% Lọc tín hiệu ECG
fs = 250;  % Sampling frequency 250 Hz
t = 0:1/fs:10;  % 10 seconds
ecg_signal = generate_ecg(t);  % Mock ECG

% Bandpass filter (0.5 - 40 Hz)
[b, a] = butter(4, [0.5, 40]/(fs/2), 'bandpass');
filtered = filtfilt(b, a, ecg_signal);  % Zero-phase filtering

% FFT analysis
N = length(filtered);
fft_result = fft(filtered);
frequencies = (0:N-1) * fs/N;
amplitude = abs(fft_result(1:N/2)) * 2/N;

% Find peaks (R peaks in QRS complex)
[peaks, locations] = findpeaks(filtered, 'MinPeakHeight', 0.5, 'MinPeakDistance', fs*0.6);
heart_rate = 60 / mean(diff(locations/fs));  % BPM
```

> **🎯 Liên hệ với dự án ECG của bạn:**
> - MATLAB xử lý tín hiệu cùng logic như code Python trong `dashboard.py`
> - Python dùng `scipy.signal` thay thế MATLAB Signal Processing Toolbox

---

## ✅ CHECKLIST MATLAB/MCR

- [ ] Giải thích tại sao dùng MATLAB thay vì Python cho thuật toán này
- [ ] Khác biệt index 0 vs 1, và row-major vs column-major
- [ ] MCR là gì và tại sao không cần license
- [ ] Singleton pattern cho MCR để tránh multiple instances
- [ ] Cách handle data type conversion NumPy ↔ MATLAB
- [ ] Thread-safety khi nhiều requests gọi MATLAB cùng lúc
- [ ] Monitoring memory usage của MCR trong production
