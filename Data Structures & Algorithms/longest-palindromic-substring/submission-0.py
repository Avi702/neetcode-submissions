class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        ans = 0
        def expand(i,j):
            L = i
            R = j
            while L >= 0 and R < len(s):
                if s[L] != s[R]:
                    break
                L -= 1
                R += 1
            count = R - L - 1
            return count, L + 1
        for i in range(len(s)):
            count1, left1= expand(i,i)
            count2, left2 = expand(i,i+1)
            if count1 > maxlen:
                maxlen = count1
                ans = left1
            if count2 > maxlen:
                maxlen = count2
                ans = left2
        return s[ans:ans+maxlen]
                