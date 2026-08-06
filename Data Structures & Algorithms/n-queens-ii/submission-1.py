class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        diag1 = set()
        diag2 = set()
        self.ans = 0
        def placeQueen(r):
            if r == n:
                self.ans += 1
                return
            for c in range(n):
                if c in col or (c + r) in diag1 or (c-r) in diag2:
                    continue
                col.add(c)
                diag1.add(c+r)
                diag2.add(c-r)
                placeQueen(r+1)
                col.remove(c)
                diag1.remove(c+r)
                diag2.remove(c-r)
        placeQueen(0)
        return self.ans