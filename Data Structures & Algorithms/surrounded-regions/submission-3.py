class Solution:
    #True : is surrounded region
    #False: is not surrounded - fill x
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        def dfs(r,c):
            if r >= m or c >= n or c < 0 or r < 0 or board[r][c] != 'O':
                return 
            board[r][c] = 'S'
            u = dfs(r+1,c)
            d = dfs(r-1,c)
            left = dfs(r,c-1)
            right = dfs(r,c+1)
        for row in range(m):
            dfs(row,n-1)
            dfs(row,0)
        for col in range(n):
            dfs(m-1,col)
            dfs(0,col)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
        