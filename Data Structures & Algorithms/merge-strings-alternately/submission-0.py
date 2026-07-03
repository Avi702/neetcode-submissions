class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i in range(min(len(word1),len(word2))):
            ans += word1[i]
            ans += word2[i]
        remaining = abs(len(word1) - len(word2))
        if remaining and len(word1) > len(word2):
            ans += word1[len(word1) - remaining:]
        elif remaining:
            ans += word2[len(word2) - remaining:]
        return ans

