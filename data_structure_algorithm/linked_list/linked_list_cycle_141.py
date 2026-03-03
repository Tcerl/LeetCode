"""
**Đề bài:** Kiểm tra linked list có cycle không.

**Phân tích:**

- Dùng Floyd's Cycle Detection (Tortoise and Hare)
- 2 pointers: slow (1 bước), fast (2 bước)
- Nếu có cycle, 2 pointers sẽ gặp nhau
**Giải thích từng bước:**

1. Khởi tạo `slow` và `fast` pointers
2. `slow` di chuyển 1 bước, `fast` di chuyển 2 bước
3. Nếu có cycle, `fast` sẽ "đuổi kịp" `slow`
4. Nếu `fast` đến None → không có cycle
"""

from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        try:
            if not head or not head.next:
                return False
            slow = head
            fast = head.next
            
            while fast and fast.next:
                if slow == fast:
                    return True
                slow = slow.next
                fast = fast.next.next
        except AttributeError:
            return False
