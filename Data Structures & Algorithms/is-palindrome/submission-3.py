class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = s.lower().split(" ")
        p = "".join(strs)
        t = ""
        for i in p:
            if i not in "abcdefghijklmnopqrstuvwxyz0123456789":
                t += ""
            else:
                t += i
        print(t)
        if t == t[::-1]:
            return True
        else:
            return False
        