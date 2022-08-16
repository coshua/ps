class Solution:
    found = False
    def exist(self, board, word):
        R = len(board)
        C = len(board[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def dfs(r, c, s):
            if len(s) == len(word):
                self.found = True
                return
            for dy, dx in dirs:
                if 0 <= r + dy < R and 0 <= c + dx < C and not v[r + dy][c + dx] and board[r + dy][c + dx] == word[len(s)]:
                    if len(s) + 1 == len(word):
                        self.found = True
                        return
                    else:
                        v[r + dy][c + dx] = True
                        dfs(r + dy, c + dx, s + word[len(s)])
                        v[r + dy][c + dx] = False

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    v = [[False for m in range(C)] for n in range(R)]
                    v[i][j] = True
                    dfs(i, j, word[0])
                    if self.found:
                        return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))