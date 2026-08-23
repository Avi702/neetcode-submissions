class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rowZero = colZero = False
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        rowZero = True
                    if col > 0:
                        matrix[0][col] = 0
                    else:
                        colZero = True
        for row in range(1,m):
            if matrix[row][0] == 0:
                for col in range(n):
                    matrix[row][col] = 0
        for col in range(1,n):
            if matrix[0][col] == 0:
                for row in range(m):
                    matrix[row][col] = 0    
        if rowZero:
            for c in range(n):
                matrix[0][c] = 0
        if colZero:
            for r in range(m):
                matrix[r][0] = 0
            


        