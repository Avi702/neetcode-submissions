class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = i
            
        for j in range(len(nums)):
            if target - nums[j] in maps and maps[target - nums[j]] != j:
                return [j,maps[target-nums[j]]]
  
        
        
        
            