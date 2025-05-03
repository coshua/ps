from collections import deque
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        q = deque()
        n = 0
        v = [0] * (amount)
        
        q.append(amount)

        while(q):
            ln = len(q)
            for _ in range(ln):
                c = q.popleft()
                if c == 0:
                    return n

                for coin in coins:
                    if c - coin >= 0 and v[c - coin] == 0:
                        v[c - coin] = 1
                        q.append(c - coin)
            
            n += 1