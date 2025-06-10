class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s=set()
        if not k:
            return False
        for i in range(min(k, len(nums))):
            c = nums[i]
            if c in s:
                return True
            s.add(c)
        for i in range(k, len(nums)):
            c = nums[i]
            if c in s:
                return True
            s.remove(nums[i-k])
            s.add(c)
        return False