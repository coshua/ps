from typing import Counter


class Solution:
    def powHelper(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        cut_half = n // 2
        temp = self.powHelper(x, cut_half)
        if n % 2 == 1:
            return temp * temp * x
        else:
            return temp * temp

    def myPow(self, x: float, n: int) -> float:
        reverse = n < 0

        ans = self.powHelper(x, abs(n))

        return 1/ans if reverse else ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(0.0001, 2147483472))