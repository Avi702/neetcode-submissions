class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cur = []
        def isValid(i,j,s):
            l = i; r = j
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1; r-=1
            return True
        def backtrack(i):
            if i >= len(s):
                ans.append(cur[:])
                return
            for j in range(i,len(s)):
                if isValid(i,j,s):
                    cur.append(s[i:j+1])
                    backtrack(j+1)
                    cur.pop()
        backtrack(0)
        return ans