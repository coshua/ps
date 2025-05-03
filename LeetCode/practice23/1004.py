from collections import deque


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        q = deque()
        ans = 0
        lo = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if k:
                    if len(q) == k:
                        p = q.popleft()
                        lo = p + 1
                    q.append(i)
                else:
                    lo = i + 1
            ans = max(ans, i - lo + 1)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestOnes([0, 0, 1, 1, 0], 0))
