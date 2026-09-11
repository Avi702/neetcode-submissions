class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        n = len(s)
        for i in range(n):
            lastIndex[s[i]] = i
        L = 0
        ans = []
        R = 0
        last =0
        while R < n:
            last = max(last,lastIndex[s[R]])
            if last == R:
                ans.append(R-L+1)
                sset = set()
                L = R + 1
            R+=1
        return ans

            
