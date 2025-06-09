class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            c = nums[i]
            if c == elem:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    elem = c
                    cnt = 1
        return elem