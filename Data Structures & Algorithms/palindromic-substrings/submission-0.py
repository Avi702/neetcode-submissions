class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i,j):
            l = i; r = j
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r+=1
            return count
        total = 0
        for i in range(len(s)):
            c1 = expand(i,i)
            c2 = expand(i,i+1)
            total += c1 + c2
        return total

            