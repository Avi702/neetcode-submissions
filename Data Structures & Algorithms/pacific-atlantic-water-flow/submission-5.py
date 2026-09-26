class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        m = len(heights)
        n = len(heights[0])
        def dfs(r,c,visit,prev):
            if (r,c) in visit or r >= m or c >= n or r < 0 or c < 0 or heights[r][c] < prev:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        for r in range(m):
            dfs(r,0,pacific,-1)
            dfs(r,n-1,atlantic,-1)
        for c in range(n):
            dfs(0,c,pacific,-1)
            dfs(m-1,c,atlantic,-1)
        ans = []
        for r in range(m):
            for c in range(n):
                if (r,c) in pacific and (r,c) in atlantic:
                    ans.append([r,c])
        return ans
