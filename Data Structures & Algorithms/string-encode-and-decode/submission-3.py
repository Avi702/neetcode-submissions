class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += str(len(i)) + "_" + i
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "_":
                j += 1
            length = int(s[i:j])
            ans.append(s[j+1:j+ length+1])
            i = j + length + 1
        return ans
