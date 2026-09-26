class Solution:
    from collections import defaultdict
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        cycle = set()
        visit = set()
        res = []
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res