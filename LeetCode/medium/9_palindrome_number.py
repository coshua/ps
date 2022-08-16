import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        r = 0
        if x < 0:
            return False
        while x >= 10:
            r = r * 10 + int(x % 10)
            x = math.floor(x / 10)
        if x != 0:
            r = r * 10 + x
        return original == r
