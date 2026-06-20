class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        L = 0; R = m*n - 1
        while L <= R:
            M = (L+R)//2
            row, col = M//n, M%n #1 , 5%3 2
            val = matrix[row][col]
            if val > target:
                R = M - 1
            elif val < target:
                L = M + 1
            else:
                return True
        return False