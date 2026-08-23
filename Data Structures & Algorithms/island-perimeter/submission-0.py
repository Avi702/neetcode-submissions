class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.count = 0
        visit = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                self.count += 1
                return
            if (r,c) in visit:
                return
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        foundIsland = False
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r,c)
                    foundIsland = True
                    break
            if foundIsland:
                break
        return self.count
            