class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        cnt = 0
        self.visited = [False] * n
        def dfs(a):
            self.visited[a] = True
            for i in range(n):
                if isConnected[a][i] == 1 and not self.visited[i]:
                    dfs(i)


        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and not self.visited[j]:
                    cnt += 1
                    dfs(j)
        return cnt

if __name__ == "__main__":
    sol = Solution()
    print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))

                