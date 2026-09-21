class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        R = 0
        count = 0
        longest = 0
        h = defaultdict(int)
        while R < len(s):
            h[s[R]] += 1
            while (R-L+1) - max(h.values()) > k:
                h[s[L]]-=1
                L+=1
            longest = max(longest,R-L+1)
            R+=1
        return longest

                



            


