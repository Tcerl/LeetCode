"""
Kiến thức:
- Stack là LIFO - Phần tử vào sau ra trước
- Operations: push(thêm), pop(xóa), peek(xem), is_empty(kiểm tra rỗng), size(kích thước)
- Applications: Expression evaluation, Undo/Endo, Function calls, Backtracking
- Time complexity: O(1) cho tất cả operations
Giải thích chi tiết:
1. Cách hoạt động:
Giống như chông đĩa: đĩa trên cùng được lấy ra trước
Push: thêm phần tử vào đỉnh stack
Pop: xóa phần tử ở đỉnh stack
Peek: xem phần tử ở đỉnh stack
Is_empty: kiểm tra stack có rỗng không
Size: lấy kích thước stack
2. Khi nào dùng Stack?????
- Kiểm ra dấu ngoặc đúng
- Tính toán biểu thức (infix, postfix, prefix)
- Undo/Redo operations
- Backtracking algorithms
- Function call stack
- DFS(Depth-First Search)
"""
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

"""
Expession Parser

"""
class Expression_Parser:
    def is_balanced(expression):
        stack = Stack()
        pairs = {')':'(', '}':'{', ']':'['}

        for char in expression:
            if char in pairs.values():
                stack.push(char)
            elif char in pairs:
                if stack.is_empty() or stack.pop() != pairs[char]:
                    return False

        return stack.is_empty()

    def evaluate_postfix(expression):
        stack = Stack()
        operators = {'+', '-', '*' , '/', '%'}

        for token in expression.split():
            if token not in operators:
                stack.push(float(token))
            else:
                b = stack.pop()
                a = stack.push()
                if token == '+':
                    stack.push(a + b)
                elif token == '-':
                    stack.push(a - b)
                elif token == '*':
                    stack.push(a * b)
                elif token == '/':
                    stack.push(a / b)
                elif token == '%':
                    stack.push(a % b)

        return stack.pop()