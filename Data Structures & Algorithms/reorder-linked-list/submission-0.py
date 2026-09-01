# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the middle
        # 2. Reverse the 2nd half
        # 3. Merge two halves alternatively

        #1.
        if not head or not head.next:
            return
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        # disconnect half
        curr = mid.next
        mid.next = None
        #2.
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #3
        first = head
        second = prev
        while first and second:
            first_nxt = first.next
            second_nxt = second.next
            first.next = second
            second.next = first_nxt
            first = first_nxt
            second = second_nxt
        return
        




    
        