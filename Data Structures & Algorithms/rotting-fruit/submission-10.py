class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        def check(r,c):
            if r >= m or c >= n or r < 0 or c < 0 or (r,c) in visit or grid[r][c] == 0:
                return
            visit.add((r,c))
            q.append((r,c))
        visit = set()
        total = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                    total += 1
                if grid[r][c] == 1:
                    total += 1
        if not total:
            return 0
        time = -1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                check(r+1,c)
                check(r-1,c)
                check(r,c+1)
                check(r,c-1)
            time += 1
        if len(visit) < total:
            return -1
        return time
        