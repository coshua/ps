class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # from backwards
        sz1, sz2 = len(nums1), len(nums2)
        p1, p2 = sz1-sz2-1, sz2-1
        pnt = sz1 - 1
        while pnt >= 0:
            if p1 < 0:
                nums1[pnt] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                nums1[pnt] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[pnt] = nums1[p1]
                p1 -= 1
            else:
                nums1[pnt] = nums2[p2]
                p2 -= 1
            pnt -= 1
        
