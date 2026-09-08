# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = dict()
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i
        preorderidx = 0

        def dfs (left, right):
            nonlocal preorderidx
            if left > right:
                return None

            rootVal = preorder[preorderidx]
            root = TreeNode(rootVal)
            mid = inorderMap[rootVal]
            preorderidx +=1

            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)

            return root
        return dfs(0, len(inorder)-1)

        