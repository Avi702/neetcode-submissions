# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            cur = []
            for i in range(len(q)):
                val = q.popleft()
                cur.append(val.val)
                print(cur)
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
            ans.append(cur[-1])
        return ans