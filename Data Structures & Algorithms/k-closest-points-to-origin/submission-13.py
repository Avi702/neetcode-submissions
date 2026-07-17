class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        new_points = []
        for point in points:
            distance = -(point[0]**2 + point[1]**2)
            if len(new_points) < k:
                heapq.heappush(new_points,[distance,point[0],point[1]])
            elif distance > new_points[0][0]:
                heapq.heapreplace(new_points,[distance,point[0],point[1]])
        return [[x,y] for d,x,y in new_points]
       