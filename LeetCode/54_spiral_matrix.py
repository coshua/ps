class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        read = list()

        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        R = len(matrix)
        C = len(matrix[0])
        def dfs(i, j, d):
            read.append(matrix[i][j])
            matrix[i][j] = -101
            ni, nj = i + dirs[d][0], j + dirs[d][1]
            if 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] > -101:
                dfs(ni, nj, d)
            else:
                d = (d + 1) % 4
                ni, nj = i + dirs[d][0], j + dirs[d][1]
                if 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] > -101:
                    dfs(ni, nj, d)

        dfs(0, 0, 0)
        return read

if __name__ == "__main__":
    solution = Solution()
    print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))