class Solution:
    from collections import defaultdict
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        cycle = set()
        visit = set()
        order = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            cycle.remove(course)
            visit.add(course)
            order.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order
                    
            
                

