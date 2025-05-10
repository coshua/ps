class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cmp = 1
        for _ in range(32):
            if cmp == n:
                return True
            cmp = cmp << 1
        return False