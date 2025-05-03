from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        s = defaultdict(int)
        for i in range(n):
            s[tuple(grid[i])] += 1

        ans = 0

        for j in range(n):
            ans += s[tuple([grid[i][j] for i in range(n)])]

        return ans
