class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # if connected remove everything except one
        rc = defaultdict(set)
        cr = defaultdict(set)
        v = set()

        for r, c in stones:
            rc[r].add(c)
            cr[c].add(r)
        
        ans = 0
        def dfs(r, c):
            local = 1
            for nxt in rc[r]:
                if (r, nxt) not in v:
                    v.add((r,nxt))
                    local += dfs(r, nxt)
            for nxt in cr[c]:
                if (nxt, c) not in v:
                    v.add((nxt,c))
                    local += dfs(nxt, c)
            return local
        
        for r, c in stones:
            if (r,c) not in v:
                v.add((r,c))
                ans += dfs(r ,c) - 1
        return ans