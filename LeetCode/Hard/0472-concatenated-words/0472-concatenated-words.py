class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = {}
        ref = set(words)
        def helper(w):
            if w in ref:
                return True
            sz = len(w)
            if sz < 2:
                return False

            if w not in d:
                d[w] = False
                for i in range(sz):
                    bef = w[:i]
                    aft = w[i:]
                    if helper(bef) and helper(aft):
                        d[w] = True
                        break
            return d[w]
        ans = []
        for w in words:
            sz = len(w)
            for i in range(1, sz):
                bef = w[:i]
                aft = w[i:]
                if helper(bef) and helper(aft):
                    ans.append(w)
                    break
        
        return ans
