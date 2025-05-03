from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        m = defaultdict(lambda: defaultdict(float))

        for i in range(len(values)):
            a, b = equations[i]
            v = values[i]
            keys = list(m.keys())
            for prev in keys:
                if a in m[prev]:
                    m[prev][b] = m[prev][a] * v
                    m[b][prev] = 1 / (m[prev][b])
                if b in m[prev]:
                    m[prev][a] = m[prev][b] / v
                    m[a][prev] = v / m[prev][b]

            m[a][b] = v
            m[b][a] = 1 / v

        ans = []
        for a, b in queries:
            if a == b and m[a]:
                ans.append(1.0)
            elif m[a][b]:
                ans.append(m[a][b])
            else:
                ans.append(-1.0)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.calcEquation(
            [["a", "e"], ["b", "e"]],
            [4.0, 3.0],
            [["a", "b"], ["b", "a"]],
        )
    )
