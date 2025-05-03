class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        depth = [0] * len(nums)
        ans = 0
        s = None
        for i in range(len(nums)):
            if depth[nums[i]] == 0:
                p = nums[i]
                s = set()
                while p not in s:
                    s.add(p)
                    p = nums[p]
                
                for el in s:
                    depth[el] = len(s)
                ans = max(ans, len(s))
        
        return ans
                
