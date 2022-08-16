class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        sz = len(matrix)
        minrow = matrix[0]
        for i in range(1, sz):
            temp = minrow[:]
            minrow[0] = matrix[i][0] + min(temp[0], temp[1])
            minrow[sz - 1] = matrix[i][sz - 1] + min(temp[sz - 1], temp[sz - 2])
            for j in range(1, sz - 1):
                minrow[j] = matrix[i][j] + min(temp[j - 1], min(temp[j], temp[j + 1]))
        return min(minrow)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minFallingPathSum([[-19,57],[-40,-5]]))