class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        max_h = 0
        while L < R:
            h = min(heights[L],heights[R])
            area = h*(R-L)
            max_h = max(max_h,area)
            if heights[L] > heights[R]:
                R -= 1
            else:
                L +=1
        return max_h
