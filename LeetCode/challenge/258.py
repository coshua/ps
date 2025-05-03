class Solution:
    def addDigits(self, num: int) -> int:
        def digitsum(n):
            sum = 0
            while n > 0:
                sum += n % 10
                n /= 10

        while num >= 10:
            num = digitsum(num)

        return num
