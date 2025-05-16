class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        # row * 3 + col
        grid = [set() for _ in range(9)]
        cell = []
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != ".":
                    ci = int(c)
                    rows[i].add(ci)
                    cols[j].add(ci)
                    grid[(i//3) * 3+j//3].add(ci)
                else:
                    cell.append((i, j))
        def check(b, r, c, num, rows, cols, grid):
            if num in rows[r] or num in cols[c] or num in grid[(r//3) * 3+c//3]:
                return False
            return True
        def backtrack(idx):
            if idx == len(cell):
                return True
            
            i, j = cell[idx]
            for k in range(1, 10):
                if check(board, i, j, k, rows, cols, grid):
                    board[i][j] = str(k)
                    rows[i].add(k)
                    cols[j].add(k)
                    grid[(i//3) * 3+j//3].add(k)
                    if backtrack(idx + 1):
                        return True
                    rows[i].remove(k)
                    cols[j].remove(k)
                    grid[(i//3) * 3+j//3].remove(k)
            board[i][j] = "."
            return False
        backtrack(0)
