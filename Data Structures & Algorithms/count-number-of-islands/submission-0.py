class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ans = 0
        def dfs(r,c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return
            if grid[r][c] == '0' or grid[r][c] == '#':
                return
            grid[r][c] = '#' 
            up = dfs(r+1,c)
            down = dfs(r-1,c)
            right = dfs(r,c+1)
            left = dfs(r,c-1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.ans += 1
                dfs(row,col)
        return self.ans
