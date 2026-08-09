class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        n = len(heights)
        for h in range(n):
            start = h
            while stack and stack[-1][0] > heights[h]:
                j, i = stack.pop()
                area = max(area,j*(h-i))
                start = i
            stack.append([heights[h],start])
        for height, idx in stack:
            area = max(height*(n-idx),area)
        return area
