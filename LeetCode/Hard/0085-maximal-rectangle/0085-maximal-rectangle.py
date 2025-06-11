class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # reference for number of consecutive 1 to the right
        rsz,csz= len(matrix),len(matrix[0])

        cnt = [[0]*csz for _ in range(rsz)]
        for i in range(rsz):
            for j in range(csz):
                if j == 0:
                    cnt[i][j] = 1 if matrix[i][j] == "1" else 0
                else:
                    cnt[i][j] = cnt[i][j-1] + 1 if matrix[i][j] == "1" else 0
        
        ans = 0
        def calc(r, c):
            w = float('inf')
            local = 0
            origin_r = r
            while r < rsz and cnt[r][c] > 0:
                w = min(w, cnt[r][c])
                local = max(local, w * (r-origin_r+1))
                r+=1
            return local

        for i in range(rsz):
            for j in range(csz):
                ans = max(ans, calc(i,j))
        return ans