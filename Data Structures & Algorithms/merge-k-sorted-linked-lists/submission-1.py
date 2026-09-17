# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i,lists[i] ))#lists[i] is the node
        #min heap has the initial vals

        dummy = ListNode()
        curr = dummy
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            node = node.next

            if node:
                heapq.heappush(min_heap, (node.val,i,node))

        return dummy.next 



        
        

        