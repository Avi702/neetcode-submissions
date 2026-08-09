from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = set()
        q = deque()
        self.fresh = 0
        def search(r,c):
            if r >= m or c >= n or c < 0 or r < 0 or grid[r][c] == 0 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append((r,c))
            self.fresh -= 1
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    q.append((row,col))
                    visit.add((row,col))
                if grid[row][col] == 1:
                    self.fresh += 1
        if self.fresh == 0:
            return 0
        time = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                search(r+1,c)
                search(r-1,c)
                search(r,c+1)
                search(r,c-1)
            time += 1
        if self.fresh != 0:
            return -1
        return time

            

