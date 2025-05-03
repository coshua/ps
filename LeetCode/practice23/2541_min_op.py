class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int], k: int) -> int:
        offset = 0
        opcnt = 0
        if k == 0:
            return 0 if nums1 == nums2 else -1
        for i in range(len(nums1)):
            diff = nums1[i] - nums2[i]
            if diff % k != 0:
                return -1
            offset += diff // k
            if diff > 0:
                opcnt += diff // k
        
        if offset == 0:
            return opcnt
        else:
            return -1
        
        
