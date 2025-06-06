class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        sz = len(digits)
        for i in range(sz):
            if digits[i] == 0:
                continue
            d1 = digits[i]
            for j in range(sz):
                if i == j:
                    continue
                d2 = digits[j]
                for k in range(sz):
                    if i == k or j == k or digits[k] % 2 == 1:
                        continue
                    d3 = digits[k]
                    ans.add(d1 * 100 + d2 * 10 + d3)
        return sorted(list(ans))
