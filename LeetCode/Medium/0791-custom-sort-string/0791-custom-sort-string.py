class Solution:
    def customSortString(self, order: str, s: str) -> str:
        g = [[] for _ in range(26)]
        for i in range(len(order) - 1):
            ch, nc = ord(order[i]) - ord('a'), ord(order[i + 1]) - ord('a')
            g[ch].append(nc)
        
        ans = []
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        
        for i in range(len(order)):
            ans += [order[i]] * d[order[i]]
            d[order[i]] = 0
        for key in d:
            ans += key * d[key]
        return ''.join(ans)