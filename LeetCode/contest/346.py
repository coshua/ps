class Solution:
    def punishmentNumber(self, n: int) -> int:
        def recursivePartitionSum(digits, cur, i, target):
            ln = len(digits)
            if cur > target:
                return False

            if i == ln and cur == target:
                return True

            ans = False
            for nxt in range(i + 1, ln + 1):
                add = digits[i:nxt]
                ans |= recursivePartitionSum(digits, cur + int(add), nxt, target)

            return ans

        ans = 0
        for i in range(1, n + 1):
            if recursivePartitionSum(str(i * i), 0, 0, i):
                ans += i * i

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.punishmentNumber(37))
