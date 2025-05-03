class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [True] * n

        e = int(n ** 0.5)
        for i in range(2, e + 1):
            if sieve[i] == True:
                for j in range(i + i, n, i):
                    sieve[j] = False
        
        return sieve[2:].count(True)