class Solution:
    from collections import defaultdict
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei)
        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)
        return count
            

