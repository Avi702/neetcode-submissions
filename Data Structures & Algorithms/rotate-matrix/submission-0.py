class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        ans = []
        for c in range(n):
            col = []
            for i in range(n):
                col.append(matrix[i][c])
            ans.append(col[::-1])
        print(ans)
        matrix[:] = ans

