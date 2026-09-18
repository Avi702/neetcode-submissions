class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(l,r):
            while l >= 0 and r < n and s[l] == s[r]:
                l-=1
                r+=1
            return l + 1, r - 1
        maxlen = 0
        maxString = ""
        for i in range(n):
            oddl, oddr = expand(i,i)
            evenl, evenr = expand(i,i+1)
            if oddr - oddl + 1 > maxlen:
                maxlen = oddr - oddl + 1
                maxString = s[oddl:oddr+1]
            if evenr - evenl + 1 > maxlen:
                maxlen = evenr - evenl + 1 
                maxString = s[evenl:evenr+1]
        return maxString
            
