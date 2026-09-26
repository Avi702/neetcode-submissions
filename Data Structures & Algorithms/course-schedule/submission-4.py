class Solution:
    from collections import defaultdict
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        cycle = set()
        visit = set()
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
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True