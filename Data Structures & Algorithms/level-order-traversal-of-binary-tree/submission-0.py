# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        q = deque()
        ans = []
        q.append(root)
        while q:
            cur = []
            for i in range(len(q)):
                v = q.popleft()
                cur.append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            ans.append(cur)
        return ans
            
            
            

