class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        visit = set()
        def dfs(r,c,visit):
            if (r,c) in visit or r >= m or c >= n or r < 0 or c < 0 or board[r][c] == "X":
                return
            visit.add((r,c))
            board[r][c] = "I"
            dfs(r+1,c,visit)
            dfs(r-1,c,visit)
            dfs(r,c+1,visit)
            dfs(r,c-1,visit)
        for r in range(m):
            if board[r][0] == "O":
                dfs(r,0,visit)
            if board[r][n-1] == "O":
                dfs(r,n-1,visit)
        for c in range(n):
            if board[0][c] == "O":
                dfs(0,c,visit)
            if board[m-1][c] == "O":
                dfs(m-1,c,visit)
        for r in range(m):
            for c in range(n):
                if board[r][c] == "I":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"

