class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [0] * len(s)
        for i in range(len(s)):
            cost[i] = abs(ord(s[i]) - ord(t[i]))
        ans = 0
        acc = 0
        st = 0
        for i in range(len(s)):
            if acc + cost[i] <= maxCost:
                acc += cost[i]
                ans = max(ans, i - st + 1)
            else:
                while acc + cost[i] > maxCost:
                    acc -= cost[st]
                    st += 1
                acc += cost[i]
        
        return ans