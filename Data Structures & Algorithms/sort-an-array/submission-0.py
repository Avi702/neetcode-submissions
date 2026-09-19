class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        half = n // 2
        l = self.sortArray(nums[:half])
        r = self.sortArray(nums[half:])
        i = 0
        j = 0
        res = []
        while i < len(l) and j < len(r):
            if l[i] >= r[j]:
                res.append(r[j])
                j+=1
            else:
                res.append(l[i])
                i+=1
        if i < len(l):
            res = res + l[i:]
        if j < len(r):
            res = res + r[j:]
        return res
