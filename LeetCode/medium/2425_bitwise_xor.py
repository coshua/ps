class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        num2xor = 0
        num1xor = 0
        for num in nums1:
            num1xor ^= num

        for num in nums2:
            num2xor ^= num

        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        elif len(nums1) % 2 == 1 and len(nums2) % 2 == 1:
            return num2xor ^ num1xor
        elif len(nums1) % 2 == 1:
            return num2xor
        else:
            return num1xor
