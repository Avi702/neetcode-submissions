class Solution:
    from collections import defaultdict
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
        self.cycle = set()
        visit = set()
        path = []
        def dfs(node,prev):
            if node in visit:
                i = path.index(node)          
                self.cycle = set(path[i:])
                return True
            visit.add(node)
            path.append(node)
            for nei in graph[node]:
                if nei == prev:
                    continue
                if dfs(nei,node):
                    return True
            path.pop()
            return False
        dfs(1,1)

        for a, b in reversed(edges):
            if a in self.cycle and b in self.cycle:
                return [a, b]
        return []