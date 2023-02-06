class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        arr[0] = 1
        idx = 1
        while idx < len(arr):
            if arr[idx] - arr[idx - 1] > 1:
                idx += 1
        
        return arr[-1]
