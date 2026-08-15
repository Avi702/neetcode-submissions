class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        def search(r,c,prev,visit):
            if r >= m or c >= n or r < 0 or c < 0 or (r,c) in visit or heights[r][c] < prev:
                return
            visit.add((r,c))
            search(r+1,c,heights[r][c],visit)
            search(r-1,c,heights[r][c],visit)
            search(r,c+1,heights[r][c],visit)
            search(r,c-1,heights[r][c],visit)
        for r in range(m):
            search(r,0,heights[r][0],pacific)
            search(r,n-1,heights[r][n-1],atlantic)
        for c in range(n):
            search(0,c,heights[0][c],pacific)
            search(m-1,c,heights[m-1][c],atlantic)
        ans = []
        for row in range(m):
            for col in range(n):
                if (row,col) in pacific and (row,col) in atlantic:
                    ans.append([row,col]) 
        return ans
