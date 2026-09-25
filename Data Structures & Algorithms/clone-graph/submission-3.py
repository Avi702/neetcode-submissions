"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.h = {}
        def dfs(node):
            if not node:
                return
            self.h[node] = Node(node.val,[])
            for nei in node.neighbors:
                if nei not in self.h:
                    newNode = dfs(nei)
                    self.h[node].neighbors.append(newNode)
                else:
                    self.h[node].neighbors.append(self.h[nei])
            return self.h[node]
        return dfs(node)