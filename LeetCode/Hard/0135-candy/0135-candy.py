class Solution:
    def candy(self, ratings: List[int]) -> int:
        sz = len(ratings)
        dist = [-1] *  sz

        def getdp(n):
            if n < 0 or n >= sz:
                return 0
            if dist[n] == -1:
                left = ratings[n-1] if n > 0 else -1
                right = ratings[n+1] if n < sz-1 else -1
                cur = ratings[n]
                lval = rval = 0
                if cur > left:
                    lval = getdp(n-1)
                if cur > right:
                    rval = getdp(n+1)
                dist[n] = max(lval, rval) + 1
            return dist[n]

        for i in range(sz):
            dist[i] = getdp(i)
            

        return sum(dist)