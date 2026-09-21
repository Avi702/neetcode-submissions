class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        #end is True, we just ended extending subarray
        #end if False, we can extend or now end it
        self.cache = {}
        def dfs(i,end):
            if i == n:
                return float('-inf') if end else 0
            if (i,end) in self.cache:
                return self.cache[(i,end)]
            if not end:
                res = max(0,nums[i] + dfs(i+1,False))     
            else:
                res = max(dfs(i+1,True),nums[i] + dfs(i+1,False))  
            self.cache[(i,end)] = res
            return self.cache[(i,end)]   
        return dfs(0,True)             
                


            
            

        
        