class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            colset = set()
            rowset = set()
            for j in range(9):
                if board[i][j] in rowset:
                    return False
                if board[j][i] in colset:
                    return False
                if board[i][j] != '.':
                    rowset.add(board[i][j])
                if board[j][i] != '.':
                    colset.add(board[j][i])
        
        def squareCheck(r, c):
            s = set()
            for i in range(3):
                for j in range(3):
                    if board[r + i][c + j] in s:
                        return False
                    if board[r + i][c + j] != '.':
                        s.add(board[r + i][c + j])
            return True
        
        r = [0, 3, 6]
        for i in range(3):
            for j in range(3):
                if not squareCheck(r[i], r[j]):
                    return False
        return True