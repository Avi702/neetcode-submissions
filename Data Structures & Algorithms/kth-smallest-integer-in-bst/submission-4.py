# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        self.kth = 0
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.kth += 1
            if self.kth == k:
                self.ans = root.val
                return
            dfs(root.right)
        dfs(root)
        return self.ans
            
            