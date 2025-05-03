class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        v = [0] * 500002
        for i in nums:
            if i > 500001 or i <= 0:
                continue
            v[i] = 1
        for i in range(1, 500002):
            if v[i] == 0:
                return i

if __name__ == "__main__":
    solution = Solution()
    print(solution.firstMissingPositive([1,2,3,4,7,9,6,5]))