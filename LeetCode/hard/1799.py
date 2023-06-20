class Solution:
    def maxScore(self, nums: list[int]) -> int:
        ln = len(nums)
        nums.sort()
        graph = [[0] * ln for _ in range(ln)]

        # a < b
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        for i in range(ln):
            for j in range(i + 1, ln):
                c = gcd(nums[i], nums[j])
                graph[i][j] = c
                graph[j][i] = c

        ans = 1
        v = [False] * ln

        def backtrack(n, cur):
            if n * 2 > ln:
                nonlocal ans
                ans = max(ans, cur)
                return

            for i in range(ln):
                if not v[i]:
                    for j in range(i + 1, ln):
                        if not v[j]:
                            v[i], v[j] = True, True
                            backtrack(n + 1, cur + n * graph[i][j])
                            v[i], v[j] = False, False

        backtrack(1, 0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.maxScore(
            [
                984916,
                312350,
                779975,
                165893,
                436389,
                592384,
                264617,
                136726,
                8893,
                587955,
                921403,
                891842,
            ]
        )
    )
