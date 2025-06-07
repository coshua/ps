class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(nums):
            if target - n in s:
                return [i, s[target - n]]
            s[n] = i
        
        return