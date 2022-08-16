class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        bit = [0 for i in range(len(nums) - 1)]
        for i in nums:
            if bit[i] == 1:
                return i
            else:
                bit[i] = 1
if __name__ == "__main__":
    solution = Solution()
    print(solution.findDuplicate([3,1,3,4,2]))