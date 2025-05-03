class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if s.count('a') < k or s.count('b') < k or s.count('c') < k:
            return -1
        
        d = dict()
        d['a'] = d['b'] = d['c'] = 0
        
        crrcnt = 0
        pnt = len(s)
        while d['a'] < k or d['b'] < k or d['c'] < k:
            pnt -= 1
            d[s[pnt]] += 1
            crrcnt += 1

        mincnt = crrcnt

        for i in range(len(s)):
            d[s[i]] += 1
            crrcnt += 1

            while pnt < len(s) and d[s[pnt]] > k:
                d[s[pnt]] -= 1
                pnt += 1
                crrcnt -= 1
            
            mincnt = min(mincnt, crrcnt)

        return mincnt