# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #wherever the p and q slpit that is the lca

        def dfs(node):
            if not node:
                return node

            if p.val > node.val and q.val > node.val:
                return dfs(node.right)
            elif p.val < node.val and q.val < node.val:
                return dfs(node.left)
            else:
                return node

        return dfs(root)