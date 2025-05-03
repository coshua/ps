class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        lenr = len(matrix)
        lenc = len(matrix[0])
        dp = [[0] * lenc for _ in range(lenr)]

        def getDP(r, c):
            if dp[r][c] == 0:
                curmax = 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < lenr
                        and 0 <= nc < lenc
                        and matrix[nr][nc] < matrix[r][c]
                    ):
                        curmax = max(curmax, getDP(nr, nc) + 1)
                dp[r][c] = curmax
            return dp[r][c]

        ans = 1
        for i in range(lenr):
            for j in range(lenc):
                ans = max(ans, getDP(i, j))

        return ans
