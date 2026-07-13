# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        M = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:M+1],inorder[:M])
        root.right = self.buildTree(preorder[M+1:],inorder[M+1:])
        return root