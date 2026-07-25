class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        if not a:
            return 0
        i = min(a)
        total = 0
        most = 0
        while a:
            if i in a:
                a.remove(i)
                total+=1
            elif total > most:
                most = total
                total = 0
            else:
                total = 0
            i+=1
        if total > most:
            most = total
        return most

            

            
            
            

