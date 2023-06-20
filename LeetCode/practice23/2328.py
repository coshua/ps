class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        ln_r, ln_c = len(grid), len(grid[0])
        cnt_routes = [[-1] * ln_c for _ in range(ln_r)]

        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        ans = 0

        def get_routes(
            r,
            c,
        ):
            if cnt_routes[r][c] == -1:
                cnt_routes[r][c] = 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ln_r and 0 <= nc < ln_c and grid[r][c] > grid[nr][nc]:
                        cnt_routes[r][c] += get_routes(nr, nc)
                cnt_routes[r][c] %= 10**9 + 7
            return cnt_routes[r][c]

        for i in range(ln_r):
            for j in range(ln_c):
                ans += get_routes(i, j)

        return ans % (10**9 + 7)
