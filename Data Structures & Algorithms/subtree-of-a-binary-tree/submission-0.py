# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(first,second):
            if not first and not second:
                return True
            if not first or not second:
                return False
            l = isSame(first.left,second.left)
            r = isSame(first.right,second.right)
            return l and r and first.val == second.val
        def helper(node,subnode):
            if not subnode:
                return True
            if not node:
                return False
            if isSame(node,subnode):
                return True
            l = helper(node.left,subnode)
            r = helper(node.right,subnode)
            return l or r
            
        return helper(root,subRoot)

