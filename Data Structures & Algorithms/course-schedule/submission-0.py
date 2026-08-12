class Solution:
    from collections import defaultdict
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mydict = defaultdict(list)
        seen = set()
        for e, s in prerequisites:
            mydict[e].append(s)
        def dfs(course):
            if course in seen:
                return False
            if mydict[course] == []:
                return True
            seen.add(course)
            for nei in mydict[course]:
                res = dfs(nei)
                if not res:
                    return False
            seen.remove(course)
            mydict[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
        