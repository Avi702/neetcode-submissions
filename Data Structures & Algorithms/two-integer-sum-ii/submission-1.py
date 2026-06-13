class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for index,i in enumerate(numbers):
            h[i] = index
            complement = target - i
            print(complement)
            if complement in h and index != h[complement]:
                print(h)
                return sorted([index+1,h[complement]+1])




