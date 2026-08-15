class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c = 0 , 0
        m, n = len(matrix)-1,len(matrix[0])-1
        ans = []
        while r <= m and c <= n:
            #traverse first row
            for i in range(c,n+1):
                ans.append(matrix[r][i])
            #traverse last col
            for i in range(r+1,m+1):
                ans.append(matrix[i][n])
            #traverse last row
            if r < m:
                for i in range(n-1,c-1,-1):
                    ans.append(matrix[m][i])
            #traverse first col
            if c < n:
                for i in range(m-1,r,-1):
                    ans.append(matrix[i][c])
            r += 1
            c += 1
            n -= 1
            m -= 1
        return ans

