class Solution:
    def sortColors(self, nums: list[int]) -> None:
        ln = len(nums)
        last_one_index = 0
        first_two_index = ln - 1
        i = 0
        while (i < ln):
            if nums[i] == 0:
                if i < last_one_index:
                    i += 1
                    continue
                id = i
                while id - 1 >= last_one_index:
                    nums[id] = nums[id - 1]
                    nums[id - 1] = 0
                    id -= 1
                last_one_index += 1
                i -= 1
            elif nums[i] == 2:
                if i > first_two_index:
                    i += 1
                    continue
                id = i
                while id + 1 <= first_two_index:
                    nums[id] = nums[id + 1]
                    nums[id + 1] = 2
                    id += 1
                first_two_index -= 1
                i -= 1
            i += 1
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2, 0, 1, 0]
    solution.sortColors(nums)
    print(nums)