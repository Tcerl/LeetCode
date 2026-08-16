class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Adds two numbers represented by linked lists l1 and l2.
        Each node contains a single digit and the digits are stored in reverse.
        :param l1: ListNode - The head of the first linked list.
        :param l2: ListNode - The head of the second linked list.
        :return: ListNode - The head of the linked list representing the sum.
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        return dummy_head.next