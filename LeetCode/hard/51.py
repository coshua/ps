class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        diagonal = ((-1, -1), (-1, 1), (1, -1), (1, 1))

        def validate(mp, r, c):
            for i in range(n):
                if mp[i][c] == "Q" or mp[r][i] == "Q":
                    return False
            for i in range(n):
                for dr, dc in diagonal:
                    if 0 <= dr * i + r < n and 0 <= dc * i + c < n:
                        if mp[dr * i + r][dc * i + c] == "Q":
                            return False
            return True

        def backtrack(mp, id):
            if id == n:
                ans.append(mp)
                return
            for i in range(n):
                if validate(mp, id, i):
                    nxtmp = [[] for _ in range(n)]
                    for st in range(n):
                        nxtmp[st] = mp[st]
                    nxtmp[id] = "." * i + "Q" + "." * (n - i - 1)
                    backtrack(nxtmp, id + 1)

        initmap = ["." * n for _ in range(n)]
        backtrack(initmap, 0)
        print(ans)
        return ans


if __name__ == "__main__":
    sol = Solution()
    sol.solveNQueens(4)
