class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h = {}
        for i in t:
            if i not in h:
                h[i] = 1
            else:
                h[i]+=1
        g = {}
        L = 0
        most = float('inf')
        ans = ""
        def isValid(g:dict,h:dict):
            for key,val in h.items():
                if g.get(key,0) < val:
                    return False
            return True
        for R in range(len(s)):
            if s[R] not in g:
                    g[s[R]] = 1
            else:
                g[s[R]] += 1
            while isValid(g,h):
                if R-L+1 < most:
                    most = R-L+1
                    ans = s[L:R+1] 
                g[s[L]] -= 1
                if g[s[L]] == 0:
                    del g[s[L]]
                L +=1          
        return ans
