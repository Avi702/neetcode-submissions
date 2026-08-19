"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        h = {}
        cur = head
        while cur:
            if cur not in h:
                h[cur] = Node(cur.val)
            if cur.random:
                if cur.random not in h:
                    h[cur.random] = Node(cur.random.val)
                h[cur].random = h[cur.random]
            
            if cur.next:
                if cur.next not in h:
                    h[cur.next] = Node(cur.next.val)
                h[cur].next = h[cur.next]
            cur = cur.next
        return h[head]
