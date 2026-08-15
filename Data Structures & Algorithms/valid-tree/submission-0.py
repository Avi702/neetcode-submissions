class Solution:
    from collections import defaultdict
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visit = set()
        def dfs(node,parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        if n == 0:
            return True
        if not dfs(0,0):
            return False
        return len(visit) == n

        