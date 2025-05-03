class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])

        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total += 1
                    rows[i] += 1
                    cols[j] += 1
        
        isolated = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    isolated += 1
        
        return total - isolated