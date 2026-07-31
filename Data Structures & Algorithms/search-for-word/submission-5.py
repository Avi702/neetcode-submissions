class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        m = len(board)
        n = len(board[0])
        def backtrack(row,col,w):
            if not w:
                return True
            if row < 0 or row == m or col < 0 or col == n:
                return False
            if board[row][col] == w[0]:
                new_w = w[1:]
                if not new_w:
                    return True
            else:
                return False
            temp = board[row][col]
            board[row][col] = '#'
            forward = up = down = backward = False
            if row < m - 1:
                down = backtrack(row+1,col,new_w)
            if row > 0:
                up = backtrack(row-1,col,new_w)
            if col < n - 1:
                forward = backtrack(row,col+1,new_w)
            if col > 0:
                backward = backtrack(row,col-1,new_w)
            board[row][col] = temp
            if forward or backward or down or up:
                return True
            return False
        for r in range(m):
            for c in range(n):
                if backtrack(r, c, word):
                    return True
        return False
        
            