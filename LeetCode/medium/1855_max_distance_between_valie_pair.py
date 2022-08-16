class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        p1, p2 = 0, 0
        max_dist = 0
        while p2 < len(nums2):
            if nums2[p2] >= nums1[p1]:
                max_dist = max(max_dist, p2 - p1)
            if p1 == p2 or nums2[p2] >= nums1[p1]:
                p2 += 1
            else:
                p1 += 1
        
        return max_dist