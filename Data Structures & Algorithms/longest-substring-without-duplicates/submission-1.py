class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        L = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in sset:
                sset.remove(s[L])
                L+=1
            sset.add(s[r])
            longest= max((r-L)+1,longest)

        return longest
            