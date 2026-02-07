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