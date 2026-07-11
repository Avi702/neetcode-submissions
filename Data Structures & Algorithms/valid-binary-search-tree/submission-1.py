# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,min_v = float('-inf'),max_v = float('inf')):
            if not node:
                return True
            l = dfs(node.left, min_v , node.val)
            r = dfs(node.right, node.val, max_v)
            if l and r and node.val > min_v and node.val < max_v:
                return True
            return False
        return dfs(root)
