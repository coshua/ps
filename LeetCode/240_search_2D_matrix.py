class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        lo_col, hi_col, lo_row, hi_row = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while (lo_col < hi_col or lo_row < hi_row) and lo_col < len(matrix[0]) and lo_row < len(matrix):
            mid_col = (lo_col + hi_col) // 2
            mid_row = (lo_row + hi_row) // 2

            if matrix[lo_row][lo_col] <= target <= matrix[mid_row][mid_col]:
                hi_row = mid_row
                hi_col = mid_col
            
            elif mid_col + 1 < len(matrix[0]) and  matrix[lo_row][mid_col + 1] <= target <= matrix[mid_row][hi_col]:
                lo_col = mid_col + 1
                hi_row = mid_row
            
            elif mid_row + 1 < len(matrix) and matrix[mid_row + 1][lo_col] <= target <= matrix[hi_row][mid_col]:
                lo_row = mid_row + 1
                hi_col = mid_col
            
            else:
                lo_row = mid_row + 1
                lo_col = mid_col + 1

        if 0 <= lo_row < len(matrix) and 0 <= lo_col < len(matrix[0]):
            return matrix[lo_row][lo_col] == target