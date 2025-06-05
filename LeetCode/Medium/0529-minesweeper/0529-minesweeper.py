class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rsz = len(board)
        csz = len(board[0])

        ecnt = 0
        for i in range(rsz):
            for j in range(csz):
                if board[i][j] == 'E':
                    ecnt += 1
        
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0,-1),(0,1),(1,-1),(1,0),(1,1)]
        def reveal(r, c):
            nonlocal ecnt
            mine=0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rsz and 0 <= nc < csz:
                    if board[nr][nc] == 'M':
                        mine += 1
            ecnt -= 1
            if not mine:
                board[r][c] = 'B'
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rsz and 0 <= nc < csz and board[nr][nc] == 'E':
                        reveal(nr, nc)
            else:
                board[r][c] = str(mine)
        
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'

        elif board[r][c] == 'E':
            reveal(r, c)

        return board
