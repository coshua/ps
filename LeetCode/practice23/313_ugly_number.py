class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        pointers = [0] * len(primes)
        ans = [1]
        for _ in range(n):
            last = float('inf')
            for i in range(len(primes)):
                last = min(last, ans[pointers[i]] * primes[i])

            for i in range(len(primes)):
                if last == ans[pointers[i]] * primes[i]:
                    pointers[i] += 1

            ans.append(last)

        return ans[-1]