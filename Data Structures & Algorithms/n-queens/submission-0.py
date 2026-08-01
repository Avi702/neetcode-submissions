class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [n*["."] for i in range(n)]
        col = set()
        diag1 = set()
        diag2 = set()
        ans = []
        def placeQueen(r):
            if r == n:
                new = ["".join(i) for i in board]
                ans.append(new)
                return
            for c in range(n):
                if c in col or (c + r) in diag1 or (c-r) in diag2:
                    continue
                col.add(c)
                diag1.add(c+r)
                diag2.add(c-r)
                board[r][c] = "Q"
                placeQueen(r+1)
                board[r][c] = "."
                col.remove(c)
                diag1.remove(c+r)
                diag2.remove(c-r)
        placeQueen(0)
        return ans
            

                
                