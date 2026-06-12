class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = {}
        box_seen = {}
        for row_idx,row in enumerate(board):
            h = set()
            for index,el in enumerate(row):
                box = (row_idx//3,index//3)
                if el != '.':
                    if box not in box_seen:
                        box_seen[box] = [el]
                    elif el in box_seen[box]:
                        return False
                    if el not in h:
                        h.add(el)
                    else:
                        return False
                    if el not in col:
                        col[el] = [index]
                    elif index in col[el]:
                        return False
                    else:
                        col[el].append(index)
        return True
