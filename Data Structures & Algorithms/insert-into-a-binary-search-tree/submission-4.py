# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root
        prev = None
        while temp:
            prev = temp
            if val > temp.val:
                temp = temp.right
            else:
                temp = temp.left
        if prev and val > prev.val:
            prev.right = TreeNode(val)
        elif prev and val < prev.val:
            prev.left = TreeNode(val)
        else:
            root = TreeNode(val)
        return root