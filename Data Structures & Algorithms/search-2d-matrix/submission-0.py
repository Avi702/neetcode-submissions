class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_matrix = [item for sublist in matrix for item in sublist]
        print(new_matrix)
        L = 0; R = len(new_matrix) - 1
        while L <= R:
            M = (L+R)//2
            if new_matrix[M] > target:
                R = M - 1
            elif new_matrix[M] < target:
                L = M + 1
            else:
                return True
        return False