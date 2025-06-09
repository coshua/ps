class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 0
        for n in arr:
            if n - prev > k:
                return prev + k
            k -= n - prev - 1
            prev = n
        
        return prev + k