class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        array = [1] * n
        for i in range(n):
            if i > 0 and ratings[i-1] < ratings[i]:
                array[i] += array[i-1]
        for j in range(n-1,-1,-1):
            if j < n-1 and ratings[j] > ratings[j+1]:
                array[j] = max(array[j],array[j+1] + 1)
        return sum(array)
