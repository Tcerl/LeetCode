"""
#### Bài toán 1: Reverse Linked List (LeetCode 206)

**Đề bài:** Đảo ngược linked list.

**Phân tích:**

- Dùng 3 pointers: prev, current, next
- Lặp qua list, đảo ngược từng pointer
"""


class Solution:
    def reverse_list(head):
        prev = None
        current = head
        
        while current:
            next = current.next
            current.next = prev
            
            prev = current
            current = next
        return prev



"""
**Giải thích từng bước:**

1. Khởi tạo `prev = None`, `current = head`
2. Lưu `next_node = current.next` trước khi đảo
3. Đảo pointer: `current.next = prev`
4. Di chuyển: `prev = current`, `current = next_node`
5. Lặp cho đến khi `current = None`
"""