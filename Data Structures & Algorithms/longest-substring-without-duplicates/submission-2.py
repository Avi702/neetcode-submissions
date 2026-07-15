class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        l = 0
        k = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in sset:
                sset.remove(s[l])
                l += 1
            sset.add(s[r])
            longest= max((r-l)+1,longest)
        return longest
            