class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        L = 0
        longest = 0
        for R in range(len(s)):
            if s[R] not in h:
                h[s[R]] = 1
            else:
                h[s[R]]+=1
            while (R-L+1)- max(h.values())> k:
                h[s[L]] -=1
                L+=1
            longest=max(longest,R-L+1)
        return longest


            

            


    