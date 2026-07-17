class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        new_points = []
        for i in points:
            heapq.heappush(new_points,[(i[0]**2 + i[1]**2)**(1/2),i])
        count = 0
        ans = []
        while count < k:
            point = heapq.heappop(new_points)
            ans.append(point[1])
            count+=1
        return ans
       