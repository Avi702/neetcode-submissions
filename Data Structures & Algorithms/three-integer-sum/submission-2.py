class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        num = sorted(nums)
        for index,i in enumerate(num):
            if index > 0 and num[index] == num[index-1]:
                continue
            L = index + 1; R = len(num) - 1
            target = -i
            while L < R:
                total = num[L] + num[R]
                if total > target:
                    R -=1
                elif total < target:
                    L +=1
                else:
                    ans.append([i,num[L],num[R]])
                    L += 1; R-=1
                    while L< R and num[L] == num[L-1]:
                        L +=1
                    while L < R and num[R] == num[R+1]:
                        R-=1
        return ans
            
            




            
