# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            l = isSame(root1.left,root2.left)
            r = isSame(root1.right,root2.right)
            return l and r
        self.isSub = False
        def isSubTree(root,subtree):
            if not root:
                return
            if root.val == subtree.val and not self.isSub:
                self.isSub = isSame(root,subtree)
            isSubTree(root.left,subtree)
            isSubTree(root.right,subtree)
        isSubTree(root,subRoot)
        return self.isSub
            
                    
            