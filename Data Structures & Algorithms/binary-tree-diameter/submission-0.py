# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def diameter(node):
            right = 0; left = 0
            if not node:
                return 0
            left = diameter(node.left)
            right = diameter(node.right)
            self.diameter = max(self.diameter, right+left)
            return 1 + max(right, left)
        diameter(root)
        return self.diameter



        