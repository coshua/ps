class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        lo, hi = min(weights), 5 * 10**4 + 1
        while lo <= hi:
            mid = (lo + hi) // 2
            spent = 0
            acc_weight = 0
            for i in range(len(weights)):
                if acc_weight + weights[i] > mid:
                    acc_weight = weights[i]
                    spent += 1
                else:
                    acc_weight += weights[i]
            
            if spent > days:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo