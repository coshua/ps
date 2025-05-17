class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        a, b = [], []
        for d in range(1, math.ceil(math.sqrt(n))):
            if n % d == 0:
                a.append(d)
                b.append(n//d)
        if int(math.sqrt(n)) * int(math.sqrt(n)) == n:
            a.append(int(math.sqrt(n)))
        arr = a + b[::-1]
        return arr[k-1] if k <= len(arr) else -1
