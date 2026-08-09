class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r,c,visit,prev):
            if (r,c) in visit or r >= m or c >= n or c < 0 or r < 0 or prev > heights[r][c]:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        
        for row in range(m):
            dfs(row,0,pacific,heights[row][0])
            dfs(row,n-1,atlantic,heights[row][n-1])
        for col in range(n):
            dfs(0,col,pacific,heights[0][col])
            dfs(m-1,col,atlantic,heights[m-1][col])
        ans = []
        for row in range(m):
            for col in range(n):
                if (row,col) in atlantic and (row,col) in pacific:
                    ans.append([row,col])
        return ans


            