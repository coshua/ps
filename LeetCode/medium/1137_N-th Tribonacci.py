class Solution:
    lst = {}
    lst[0] = 0
    lst[1] = 1
    lst[2] = 1
    def tribonacci(self, n: int) -> int:

        if n not in self.lst:
            self.lst[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        
        return self.lst[n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.tribonacci(5))