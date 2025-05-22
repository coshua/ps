class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # sum1 = 5, sum2 = 3
        # zero1 = 1, zero2 = 1 working case
        # Case One
        # arr of smaller sum doesn't have zero
        # 2
        # min possible = sum + num_of_zeros
        # max possible = inf if contains 0 else sum

        
        sum1 = sum2 = 0
        zero1 = zero2 = 0

        for i in range(len(nums1)):
            v = nums1[i]
            if v == 0:
                zero1 += 1
            sum1 += v
        for i in range(len(nums2)):
            v = nums2[i]
            if v == 0:
                zero2 += 1
            sum2 += v
        min_one = sum1 + zero1
        min_two = sum2 + zero2
        max_one = float('inf') if zero1 else sum1
        max_two = float('inf') if zero2 else sum2

        if min_one > max_two or min_two > max_one:
            return -1
        
        return max(min_one, min_two)