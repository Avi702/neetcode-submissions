class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0 
        for index, i in enumerate(heights):
            start = index
            while stack and i <= stack[-1][0]:
                h, j = stack.pop()
                w = index - j
                max_area = max(max_area,h*w)
                start = j
            stack.append((i,start))
        while stack:
            h, j = stack.pop()
            w = len(heights) - j
            max_area = max(max_area,h*w)
        return max_area

