class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        ans = [-1] * len(nums)
        cursum = 0
        for i in range(min(k, len(nums))):
            cursum += nums[i]
        for i in range(len(nums)):
            if i + k < len(nums):
                cursum += nums[i + k]
            if i - k - 1 >= 0:
                cursum -= nums[i - k - 1]
            if i - k >= 0 and i + k < len(nums):
                ans[i] = cursum // (2 * k + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.getAverages([8], 3))
