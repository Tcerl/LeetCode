"""
Bài toán Valid Parentheses:
Đề bài: Kiểm tra chuỗi dấu ngoặc có hợp lệ không.

Phân tích:
-Dùng stack để lưu dấu ngoặc mở
- Khi gặp dấu ngoặc đóng, kiểm tra xem có khớp với dấu mở trên cùng stack không
- Stack phải rỗng sau khi duyệt xong
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
        
        return not stack