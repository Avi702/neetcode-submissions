class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        self.Pacific = False
        self.Atlantic = False
        ans = []
        def waterFlow(r,c,val,visited):
            if r < 0 or c < 0:
                self.Pacific = True
                return
            if r >= m or c >= n:
                self.Atlantic = True
                return
            if (r,c) in visited:
                return
            if self.Atlantic and self.Pacific:
                return
            if val >= heights[r][c]:
                visited.add((r,c))
                waterFlow(r+1,c,heights[r][c],visited)
                waterFlow(r-1,c,heights[r][c],visited)
                waterFlow(r,c-1,heights[r][c],visited)
                waterFlow(r,c+1,heights[r][c],visited)
        
        for row in range(m):
            for col in range(n):
                self.Pacific = False
                self.Atlantic = False
                visited = set()
                waterFlow(row,col,heights[row][col],visited)
                if self.Pacific and self.Atlantic:
                    ans.append([row,col])
        return ans

            