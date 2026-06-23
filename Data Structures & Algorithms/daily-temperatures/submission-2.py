class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ans = [0] * len(temperatures)
        for index,i in enumerate(temperatures):
            while s and s[-1][0] > i:
                s.append((i,index))
            while s and s[-1][0] < i:
                temp, day = s.pop()
                ans[day] = index - day
            s.append((i,index))
        return ans

            
            