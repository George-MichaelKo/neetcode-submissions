"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Write your solution here
        
        # first pass be used creating copy node 
        # 2nd pass next and random pointer

        hashMap = dict()
        # first pass
        first = head
        if not head:
          return None
        first = head
        while first: 
          if first not in hashMap:
            hashMap[first] = Node(first.val)
            first = first.next
        
        second = head
        while second:
          if second.next:
            hashMap[second].next = hashMap[second.next]
          if second.random:
            hashMap[second].random = hashMap[second.random]
          second = second.next
        return hashMap[head]
        
      
        