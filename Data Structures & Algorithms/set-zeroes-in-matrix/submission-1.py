class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRow = set()
        zeroCol = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeroRow.add(row)
                    zeroCol.add(col)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zeroRow:
                    matrix[row][col] = 0
                if col in zeroCol:
                    matrix[row][col] = 0


        