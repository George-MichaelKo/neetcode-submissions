# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, float('-inf'), float('inf'))])
        while q:
            n = len(q)
            for _ in range(n):
                node, minimum, maximum = q.popleft()
                if node.val <= minimum or node.val >= maximum:
                    return False
                if node.left:
                    q.append((node.left,minimum, node.val))
                if node.right:
                    q.append((node.right,node.val, maximum))
        return True

