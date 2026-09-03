# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        length = 0 
        l = head
        while l:
            length += 1
            l = l.next
        idx = length - n + 1
        curr = head
        prev = dummy
        for i in range(idx-1):
            prev = curr
            curr = curr.next
        prev.next = curr.next

        return dummy.next