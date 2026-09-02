# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        #for oddlength
        if fast:
            slow = slow.next
        curr = slow
        while curr:
            q = stack.pop()
            if curr.val != q:
                return False
            curr = curr.next
        return True 


    