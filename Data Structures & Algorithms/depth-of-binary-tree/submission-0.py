# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            count = 1
            if not root:
                return 0
            add = self.maxDepth(root.left)
            plus = self.maxDepth(root.right)
            count += max(add,plus)
            return count
        total = depth(root)
        return total