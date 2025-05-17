class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        v = set()
        def twosum(ex, t):
            lo, hi = ex + 1, len(nums) - 1
            while lo < hi:
                tmp = nums[lo] + nums[hi]
                if tmp == t:
                    ans.append([nums[ex], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi-1] == nums[hi]:
                        hi -= 1
                    lo += 1
                    
                elif tmp > t:
                    hi -= 1
                else:
                    lo += 1

            return
        for i in range(len(nums)):
            if nums[i] not in v:
                twosum(i, -nums[i])
                v.add(nums[i])
        
        return ans