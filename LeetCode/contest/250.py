class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        R = len(points)
        C = len(points[0])

        dp = points[0][:]
        for i in range(1, len(points)):
            maxline = self.makeDP(dp)
            for j in range(C):
                dp[j] = maxline[j] + points[i][j]
        
        return max(dp)

    def makeDP(self, line):
        largest = [0] * len(line)
        for i in range(len(line)):
            c = line[i]
            forward = i
            backward = i - 1
            while c > 0 and forward < len(line):
                if largest[forward] >= c:
                    break
                largest[forward] = c
                c -= 1
                forward += 1
            c = line[i] - 1
            while c > 0 and backward >= 0:
                if largest[backward] >= c:
                    break
                largest[backward] = c
                c -= 1
                backward -= 1
        return largest
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxPoints([[5, 3], [3, 5], [3, 1]]))