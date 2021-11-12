class Solution:
    def numSquares(self, n: int) -> int:
        ps = []
        i = 1
        while i * i <= n:
            ps.append(i * i)
            i += 1
        
        cnt = 0
        i = 1
        while n > 0:
            dv = n // ps[-i]
            n -= dv * ps[-i]
            cnt += dv
            i += 1
        return cnt
if __name__ == "__main__":
    solution = Solution()
    print(solution.numSquares(12))