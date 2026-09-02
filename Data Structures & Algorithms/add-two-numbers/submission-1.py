# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = l1
        carry = 0 
        while l1 or l2:

            if not l1:
                prev.next = l2
                l1 = l2
                l2 = None

            value1 = l1.val
            value2 = l2.val if l2 else 0
            total = value1 + value2 + carry
            digit = total % 10
            carry = total // 10

            l1.val = digit
            prev = l1
            l1 = l1.next
            
            if l2:
                l2 = l2.next 
        if carry:
            prev.next = ListNode(carry)
        return start
        