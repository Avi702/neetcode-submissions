# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.nodes = 0
        def dfs(root,prev):
            if not root:
                return
            if prev <= root.val:
                self.nodes += 1
            val = max(prev,root.val)
            dfs(root.left,val)
            dfs(root.right,val)
        dfs(root,float('-inf'))
        return self.nodes