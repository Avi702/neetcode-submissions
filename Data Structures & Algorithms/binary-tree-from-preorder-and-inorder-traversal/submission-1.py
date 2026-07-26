# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #[2,1,3,4]
        #[1,2,3,4]
        def traversal(inorder,preorder):
            if not preorder or not inorder:
                return None
            dummy = TreeNode(preorder[0])
            idx = inorder.index(preorder[0])
            dummy.left = traversal(inorder[:idx],preorder[1:idx + 1])
            dummy.right = traversal(inorder[idx+1:],preorder[idx+1:])
            return dummy
        return traversal(inorder,preorder)


