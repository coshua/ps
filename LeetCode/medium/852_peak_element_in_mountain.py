class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        lo, hi = 1, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] > arr[mid - 1] and arr[mid + 1] > arr[mid]:
                lo = mid + 1
            elif arr[mid] < arr[mid - 1] and arr[mid + 1] < arr[mid]:
                hi = mid - 1
            else:
                return mid
        return lo
