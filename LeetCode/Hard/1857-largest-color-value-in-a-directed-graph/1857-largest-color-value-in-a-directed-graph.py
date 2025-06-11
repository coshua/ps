class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        sz = len(colors)
        g = [[] for _ in range(sz)]
        incoming = [0] * sz
        for a, b in edges:
            g[a].append(b)
            incoming[b] += 1
        # detect cycle
        v=set()
        def dfs(cur, v, path):
            for nxt in g[cur]:
                if nxt in path:
                    return True
                if nxt not in v:
                    v.add(nxt)
                    path.add(nxt)
                    if dfs(nxt, v, path):
                        return True
                    path.remove(nxt)
            return False
        startnode = []
        for i in range(sz):
            if i not in v:
                if incoming[i] == 0:
                    startnode.append(i)
                v.add(i)
                if dfs(i, v, set([i])):
                    return -1
        if not startnode:
            return -1
        
        ans = 0

        dp = [[] for _ in range(sz)]
        def getdp(n):
            if not dp[n]:
                dp[n] = [0] * 26
                
                for nxt in g[n]:
                    res = getdp(nxt)
                    for i in range(26):
                        dp[n][i] = max(dp[n][i], res[i])
                dp[n][ord(colors[n]) - ord('a')] += 1
            return dp[n]
        
        ans = 0
        for n in startnode:
            ans = max(ans, max(getdp(n)))
        return ans
