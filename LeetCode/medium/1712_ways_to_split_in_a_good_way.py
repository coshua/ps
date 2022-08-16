class Solution:
    def waysToSplit(self, nums: list[int]) -> int:
        sum_0_i = [nums[0]] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            sum_0_i[i] = sum_0_i[i - 1] + nums[i]
    
        mod = 10**9 + 7
        ans = 0

        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            min_id = float('inf')
            while lo <= hi:
                mid = (lo + hi) // 2
                if sum_0_i[mid] - sum_0_i[i] >= sum_0_i[i] and sum_0_i[len(nums) - 1] - sum_0_i[mid] >= sum_0_i[mid] - sum_0_i[i]:
                    lo = mid + 1
                    mid_id = min(min_id, mid)
                else:
                    hi = mid - 1
            if mid_id < float('inf'):
                ans += hi - mid_id
            ans %= mod
        
        return ans
            


        