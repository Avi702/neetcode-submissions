class Solution:
    from collections import defaultdict
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for s, e in prerequisites:
            graph[s].append(e)
        visit = set()
        self.order = []
        done = set()
        def dfs(course):
            if course in visit:
                return False
            if course in done:
                return True
            visit.add(course)
            for nei in graph[course]:
                res = dfs(nei)
                if res == False:
                    return False
            visit.remove(course)
            self.order.append(course)
            done.add(course)
            return True
        for course in range(numCourses):
            res = dfs(course)
            if not res:
                return []
        return self.order
                
            
            