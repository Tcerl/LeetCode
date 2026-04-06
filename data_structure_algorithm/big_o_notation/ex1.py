import time

# O(n²) - Tìm cặp có tổng = target (cách ngây thơ)
def two_sum_naive(nums, targets):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == targets:
                return [i, j]
    return []

# O(n) - Tìm cặp có tổng = target( dùng Hash Map)
def two_sum_optional(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


#Demo hiệu năng
import random

nums = [random.randint(1, 1000) for _ in range(10000)]
target = 999

start = time.time()
two_sum_naive(nums, target)
print(f"O(n2):{time.time() - start:.4f}s")

start = time.time()
two_sum_optional(nums, target)
print(f"O(n):{time.time() - start:.6f}s")



#Space Complexity(Độ phức tạp không gian)
#O(1) space - không dùng thêm bộ nhớ
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

#O(n) space - dùng thêm mảng mới
def reverse_new_place(arr):
    return arr[::-1]