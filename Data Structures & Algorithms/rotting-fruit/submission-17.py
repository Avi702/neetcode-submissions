class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        total = 0
        rotten = 0
        visit = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                    rotten += 1
                    total+=1
                if grid[r][c] == 1:
                    total +=1
        if total == 0:
            return 0
        time = -1
        while q:
            time +=1
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for row, col in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if (r+row,c+col) not in visit and r+row < m and r+row >= 0 and c+col < n and c+col>=0 and grid[r+row][c+col] != 0:
                        q.append((r+row,c+col))
                        visit.add((r+row,c+col))
                        rotten+=1
        if rotten < total:
            return -1
        return time