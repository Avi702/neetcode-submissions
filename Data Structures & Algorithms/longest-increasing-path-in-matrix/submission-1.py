class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        self.cache = {}
        def dfs(r,c,prev):
            if r >= m or c >= n or r < 0 or c < 0 or prev >= matrix[r][c]:
                return 0
            if (r,c,prev) in self.cache:
                return self.cache[(r,c,prev)]
            res = 1
            res = max(res, 1 + dfs(r+1,c,matrix[r][c]))
            res = max(res, 1+ dfs(r-1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r,c+1,matrix[r][c]))
            res = max(res, 1 + dfs(r,c-1,matrix[r][c]))
            self.cache[(r,c,prev)] = res
            return self.cache[(r,c,prev)]
        path = 0
        for row in range(m):
            for col in range(n):
                path = max(dfs(row,col,matrix[row][col]-1),path)
        return path


            