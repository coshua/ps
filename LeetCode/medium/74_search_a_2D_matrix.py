class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        found = False
        m, n = len(matrix), len(matrix[0])
        # find row
        s, e = 0, m

        while s < e:
            mid = (s + e) // 2
            if matrix[mid][n - 1] < target:
                s = mid + 1

            elif matrix[mid][0] > target:
                e = mid

            else:
                break
        
        # target is outside of every range of row
        if e == 0 or s == m:
            return False
        
        r = mid
        s, e = 0, n

        while s < e:
            mid = (s + e) // 2
            if matrix[r][mid] > target:
                e = mid
            
            elif matrix[r][mid] < target:
                s = mid + 1
            
            else:
                break
        
        return matrix[r][mid] == target


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],
7))
        