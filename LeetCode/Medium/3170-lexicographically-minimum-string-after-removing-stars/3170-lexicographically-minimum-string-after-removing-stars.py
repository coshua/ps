class Solution:
    def clearStars(self, s: str) -> str:
        prev = []
        ans = [True] * len(s)
        for i, ch in enumerate(s):
            if ch == '*':
                ans[i] = False
                if prev:
                    ch, idx = heapq.heappop(prev)
                    ans[-idx] = False
            else:
                heapq.heappush(prev, (ch, -i))
        ansstr = []
        for i in range(len(s)):
            if ans[i]:
                ansstr.append(s[i])
        return ''.join(ansstr)