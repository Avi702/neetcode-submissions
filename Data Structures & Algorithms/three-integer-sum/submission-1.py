class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        ans = []
        for i in range(len(num)-2):
            if i>0 and num[i] == num[i-1]:
                continue
            target = -num[i]
            L = i+1
            R = len(num)-1
            while L < R:
                total = num[L]+num[R]
                if total == target:
                    ans.append([num[i],num[L],num[R]])
                    R -=1
                    L +=1
                    while L < R and num[L] == num[L-1]:
                        L+=1
                    while L < R and num[R] == num[R+1]:
                        R-=1
                elif total > target:
                    R-=1
                else:
                    L+=1
        return ans
                
            
