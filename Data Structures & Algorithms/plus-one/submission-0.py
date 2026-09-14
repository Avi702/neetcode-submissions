class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = [0] + digits
        carry = False
        i = len(ans) - 1
        while i >= 0:
            if carry:
                ans[i] += 1
                carry = False
            if i == len(ans) - 1:
                ans[i] += 1
            if ans[i] >= 10:
                remain = ans[i] % 10
                ans[i] = remain
                carry = True
            i -= 1
        if ans[0] == 0:
            return ans[1:]
        return ans

        