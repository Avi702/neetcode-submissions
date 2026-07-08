# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(first,second):
            if not first and not second:
                return True
            if not first or not second:
                return False
            l = helper(first.left,second.left)
            r = helper(first.right,second.right)
            return l and r and first.val == second.val
        return helper(p,q)
            
        
