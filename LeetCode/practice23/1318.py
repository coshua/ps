class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        binary = 1
        cnt = 0
        limit = max(a, max(b, c))
        while binary <= limit:
            if binary & c:
                if not (binary & a or binary & b):
                    cnt += 1
            else:
                if binary & a:
                    cnt += 1
                if binary & b:
                    cnt += 1
            binary <<= 1
        return cnt
