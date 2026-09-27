class Solution:
    from collections import defaultdict
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        cycle = set()
        def dfs(node,parent):
            if node in cycle:
                return False
            cycle.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        if n == 0:
            return True
        if not dfs(0,-1):
            return False
        return len(cycle) == n