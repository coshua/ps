class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        sz = len(triangle)
        dp = triangle[0]

        for i in range(1, sz):
            temp = [0] * (i + 1)
            temp[0] = triangle[i][0] + dp[0]
            temp[i] = triangle[i][i] + dp[i - 1]

            for j in range(1, i):
                temp[j] = triangle[i][j] + min(dp[j], dp[j - 1])
            
            dp = temp
        
        return min(dp)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))