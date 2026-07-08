# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ps = []; qs = []
        def pdfs(node):
            if not node:
                ps.append(None)
                return
            ps.append(node.val)
            pdfs(node.left)
            pdfs(node.right)
        
        def qdfs(node):
            if not node:
                qs.append(None)
                return
            qs.append(node.val)
            qdfs(node.left)
            qdfs(node.right)
        pdfs(p)
        qdfs(q)
        return ps == qs
        
