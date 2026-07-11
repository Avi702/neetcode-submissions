class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s.lower()
        b = a.split(" ")
        print(b)
        k = "".join(b)
        l = 0
        r = len(k) -1
        while l<r:
            while l < r and k[l] not in "abcdefghijklmnopqrstuvwxyz0123456789":
                l+=1
            while l < r and k[r] not in "abcdefghijklmnopqrstuvwxyz0123456789":
                r-=1
            if k[l]==k[r]:
                l+=1
                r-=1
            else:
                return False


        return True
