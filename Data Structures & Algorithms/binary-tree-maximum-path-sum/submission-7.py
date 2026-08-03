# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        self.maxsum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.maxsum = max(l+node.val,r+node.val,self.maxsum,l+r+node.val,node.val)
            return max(max(l,r) + node.val,node.val)
        dfs(root)
        return self.maxsum
