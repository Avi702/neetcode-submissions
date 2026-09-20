class Solution:
    from collections import Counter
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        targetCount = n / 3
        ans = []
        count = Counter(nums)
        for key,val in count.items():
            if float(val) > targetCount:
                ans.append(key)
        return ans
        