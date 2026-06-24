class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []; max_h = 0
        for index,i in enumerate(heights):
            start = index
            while s and i < s[-1][0]:
                h, w = s.pop()
                max_h = max(max_h,h*(index-w))
                start = w
            s.append((i,start))
        while s:
            h, w = s.pop()
            max_h = max(max_h,h*(len(heights)-w))
        return max_h
