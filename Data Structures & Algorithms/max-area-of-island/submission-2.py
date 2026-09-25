class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.visit = set()
        self.count = 0
        area = 0
        def dfs(r,c):
            if (r,c) in self.visit or r >= m or c >= n or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            self.visit.add((r,c))
            up = dfs(r+1,c)
            down = dfs(r-1,c)
            left = dfs(r,c-1)
            right = dfs(r,c+1)
            return 1 + up + down + left + right
        for r in range(m):
            for c in range(n):
                if (r,c) in self.visit or grid[r][c] == 0:
                    continue
                area = max(area,dfs(r,c))
        return area