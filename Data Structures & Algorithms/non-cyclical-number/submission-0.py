class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        nums = n
        while nums > 1:
            digits = []
            while nums > 0:
                digits.append((nums % 10))
                nums = nums // 10
            squared = 0
            for i in digits:
                squared += i**2
            if squared in seen:
                return False
            seen.add(squared)
            nums = squared
        return True

