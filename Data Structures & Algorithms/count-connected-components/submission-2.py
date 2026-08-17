class Solution:
    from collections import defaultdict
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        visit = set()
        cycle = set()
        def dfs(node):
            if node in cycle:
                return
            cycle.add(node)
            for nei in graph[node]:
                if nei not in cycle:
                    dfs(nei)
            visit.add(node)
        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
                cycle = set()
                dfs(i)
        return count
            

