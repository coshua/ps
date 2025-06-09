class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        idx = 0
        while idx < len(nums) and nums[idx] < 0:
            idx += 1
        
        # 0...idx-1 negative
        # idx... positive

        ans = []
        nidx = idx - 1
        while nidx >= 0 or idx < len(nums):
            if nidx == -1:
                ans.append(nums[idx]**2)
                idx += 1
            elif idx == len(nums):
                ans.append(nums[nidx]**2)
                nidx -= 1
            elif -nums[nidx] < nums[idx]:
                ans.append(nums[nidx]**2)
                nidx -= 1
            else:
                ans.append(nums[idx]**2)
                idx += 1
        return ans