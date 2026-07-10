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
        ans = []
        q.append(root)
        while q:
            length = len(q)
            for i in range(length):
                v = q.popleft()
                if i == length - 1:
                    ans.append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
        return ans
