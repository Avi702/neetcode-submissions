class Solution:
    def climbStairs(self, n: int) -> int:
        one = 0
        two = 1
        for i in range(1,n+1):
            temp = two
            two = one + two
            one = temp
        return two