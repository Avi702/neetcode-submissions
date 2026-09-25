class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        visited = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        while q:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                if row+1 < m and grid[row+1][col] != -1 and (row+1,col) not in visited:
                    grid[row+1][col] = min(grid[row+1][col],grid[row][col]+1)
                    q.append([row+1,col])
                    visited.add((row+1,col))
                if row-1 >= 0 and grid[row-1][col] != -1 and (row-1,col) not in visited:
                    grid[row-1][col] = min(grid[row-1][col],grid[row][col]+1)
                    q.append([row-1,col])
                    visited.add((row-1,col))
                if col+1 < n and grid[row][col+1] != -1 and (row,col+1) not in visited:
                    grid[row][col+1] = min(grid[row][col+1],grid[row][col]+1)
                    q.append([row,col+1])
                    visited.add((row,col+1))
                if col-1 >= 0 and grid[row][col-1] != -1 and (row,col-1) not in visited:
                    grid[row][col-1] = min(grid[row][col-1],grid[row][col]+1)
                    q.append([row,col-1])
                    visited.add((row,col-1))
            
