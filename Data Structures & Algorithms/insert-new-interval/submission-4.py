class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res1 = []
        insert = False
        for s, e in intervals:
            if not insert and newInterval[0] <= s:
                res1.append(newInterval)
                insert = True
            res1.append([s,e])
        if not insert:
            res1.append(newInterval)
        #merge:
        ans = []
        for s, e in res1:
            if ans and s <= ans[-1][1]:
                s1, e1 = ans.pop()
                ans.append([min(s1,s),max(e1,e)])
            else:
                ans.append([s,e])
        return ans