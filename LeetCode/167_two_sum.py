class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, e = 0, len(numbers)
        while i < e:
            if numbers[i] + numbers[e] == target:
                return [i + 1, e + 1]
            elif numbers[i] + numbers[e] > target:
                i += 1
            else:
                e -= 1
        

        