# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        from collections import deque
        q = deque()
        q.append(root)
        ans = []
        while q:
            n = len(q)
            for i in range(n):
                v = q.popleft()
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            ans.append(v.val)
        return ans
                