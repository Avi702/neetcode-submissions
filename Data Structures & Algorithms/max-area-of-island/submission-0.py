class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxans = 0
        def dfs(r,c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return
            if grid[r][c] == 0 or grid[r][c] == -1:
                return
            grid[r][c] = -1
            self.ans += 1
            up = dfs(r+1,c)
            down = dfs(r-1,c)
            right = dfs(r,c+1)
            left = dfs(r,c-1)
            return
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.ans = 0
                dfs(row,col)
                self.maxans = max(self.ans,self.maxans)
        return self.maxans
