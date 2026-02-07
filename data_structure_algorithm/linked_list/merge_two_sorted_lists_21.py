"""
**Đề bài:** Merge 2 linked list đã sắp xếp thành 1 list đã sắp xếp.

**Phân tích:**

- Dùng dummy node để đơn giản hóa code
- So sánh 2 node hiện tại, chọn node nhỏ hơn
- Di chuyển pointer tương ứng
"""

from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next
