# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.BST = True
        def search(root,high,low):
            if not root:
                return
            if low < root.val < high:
                l = search(root.left,root.val,low)
                r = search(root.right,high,root.val)
            else:
                self.BST = False
        search(root,high=float('inf'),low=float('-inf'))
        return self.BST
        

            
