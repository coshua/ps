class Solution:
    lst = [0] * 31
    lst[0] = 0
    lst[1] = 1
    def fib(self, n: int) -> int:

        if self.lst[n] == 0 and n not in [0, 1]:
            self.lst[n] = self.fib(n - 1) + self.fib(n - 2)
        
        return self.lst[n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.fib(5))
        