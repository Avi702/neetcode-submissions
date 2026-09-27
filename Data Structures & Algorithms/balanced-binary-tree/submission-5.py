# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):
            if not root:
                return 0
            l = 1 + dfs(root.left)
            r = 1 + dfs(root.right)
            if abs(l - r) > 1:
                self.balanced = False
            return max(l,r)
        dfs(root)
        return self.balanced