class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        mydict = {}
        for i in range(len(nums)):
            mydict[nums[i]] = i
        for index,i in enumerate(nums):
            complement = target - i
            if complement in mydict and index != mydict[complement]:
                return [index,mydict[complement]]
        