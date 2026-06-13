class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for index,i in enumerate(numbers):
            h[i] = index
            complement = target - i
            print(complement)
            if complement in h and index != h[complement]:
                if index+1>h[complement]+1:
                    return [h[complement]+1,index+1]
                else:
                    return [index+1,h[complement]+1]




