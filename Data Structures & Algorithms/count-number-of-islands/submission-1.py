class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.visit = set()
        islands = 0
        def dfs(r,c):
            if (r,c) in self.visit or r >= m or c >= n or r < 0 or c < 0 or grid[r][c] == "0":
                return
            self.visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(m):
            for c in range(n):
                if (r,c) in self.visit or grid[r][c] == "0":
                    continue
                islands += 1
                dfs(r,c)
        return islands
