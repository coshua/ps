class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        d = dict()
        minlen = float('inf')

        for i in range(len(cards)):
            if cards[i] in d:
                minlen = min(minlen, i - d[cards[i]] + 1)
            d[cards[i]] = i
        
        if minlen == float('inf'):
            minlen = -1
        return minlen