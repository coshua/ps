class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            mid = (lo + hi)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            if target < matrix[mid][0]:
                hi = mid-1
            else:
                lo = mid + 1
        lo, hi = 0, len(matrix[0]) - 1
        while lo <= hi:
            c = (lo+hi)//2
            if matrix[mid][c] == target:
                return True
            if target < matrix[mid][c]:
                hi = c - 1
            else:
                lo = c + 1
        return False