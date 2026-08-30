# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subTree):
            if not root and not subTree:
                return True
            if not root or not subTree:
                return False
            if root.val != subTree.val:
                return False
            left_same = sameTree(root.left, subTree.left)
            right_same = sameTree(root.right, subTree.right)

            return left_same and right_same

        def dfs(root):
            if not root:
                return False
            #check tree beginning same
            if sameTree(root, subRoot):
                return True

            left = dfs(root.left)
            right = dfs(root.right)

            return left or right
        return dfs(root)

            

        