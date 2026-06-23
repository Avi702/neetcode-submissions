class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        max_l = 0
        L = 0
        for R in range(len(s)):
            if s[R] not in h:
                h[s[R]] = 1
            else:
                h[s[R]] += 1
            while len(s[L:R+1]) - max(h.values()) > k:
                h[s[L]] -= 1
                L += 1
            max_l = max(max_l, R - L + 1)
        return max_l
            
      

            


    