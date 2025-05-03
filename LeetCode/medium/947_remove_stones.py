from collections import defaultdict
class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        xSet, ySet = defaultdict(list), defaultdict(list)
        visited = set()
        connectedSet = 0
        for x, y in stones:
            xSet[x].append(y)
            ySet[y].append(x)
            
        def dfs(x, y):
            if (x, y) not in visited:
                visited.add((x, y))
                for nxtY in xSet(x):
                    dfs(x, nxtY)
                for nxtX in ySet(y):
                    dfs(nxtX, y)
        
        for x, y in stones:
            if (x, y) not in visited:
                dfs(x, y)
                connectedSet += 1
        
        return len(stones) - connectedSet