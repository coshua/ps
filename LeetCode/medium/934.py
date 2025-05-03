class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        ln = len(grid)
        distgroup1 = [[-1] * ln for _ in range(ln)]
        distgroup2 = [[-1] * ln for _ in range(ln)]
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        fstgroup, sndgroup = [], []

        v = [[0] * ln for _ in range(ln)]

        def bfs(r, c, mp, v):
            ans = []
            q = [(r, c)]

            while q:
                sz = len(q)
                nq = []
                for _ in range(sz):
                    r, c = q.pop()
                    ans.append((r, c))
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < ln
                            and 0 <= nc < ln
                            and mp[nr][nc] == 1
                            and not v[nr][nc]
                        ):
                            nq.append((nr, nc))
                            v[nr][nc] ^= 1
                q = nq

            return ans

        for i in range(ln):
            for j in range(ln):
                if grid[i][j] == 1 and not v[i][j]:
                    if not fstgroup:
                        fstgroup = bfs(i, j, grid, v)
                    else:
                        sndgroup = bfs(i, j, grid, v)

        dist = 1
        while fstgroup:
            sz = len(fstgroup)
            nq = []
            for _ in range(sz):
                r, c = fstgroup.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ln
                        and 0 <= nc < ln
                        and grid[nr][nc] == 0
                        and distgroup1[nr][nc] == -1
                    ):
                        distgroup1[nr][nc] = dist
                        nq.append((nr, nc))
            fstgroup = nq
            dist += 1

        dist = 1
        while sndgroup:
            sz = len(sndgroup)
            nq = []
            for _ in range(sz):
                r, c = sndgroup.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ln
                        and 0 <= nc < ln
                        and grid[nr][nc] == 0
                        and distgroup2[nr][nc] == -1
                    ):
                        distgroup2[nr][nc] = dist
                        nq.append((nr, nc))
            sndgroup = nq
            dist += 1

        print(distgroup1)
        print(distgroup2)
        mindist = float("inf")
        for i in range(ln):
            for j in range(ln):
                if grid[i][j] == 0 and distgroup1[i][j] > -1 and distgroup2[i][j] > -1:
                    mindist = min(mindist, distgroup1[i][j] + distgroup2[i][j] - 1)
        return mindist


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.shortestBridge(
            [
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 1, 0, 1],
                [0, 0, 1, 1, 0],
            ]
        )
    )
