class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        d = defaultdict(int)

        middle = 0
        for w in words:
            d[w] += 1
        
        for w in words:
            if w[0] != w[1]:
                cnt = min(d[w], d[w[::-1]])
                ans += cnt * 4
                d[w] -= cnt
                d[w[::-1]] -= cnt
            else:
                cnt = d[w]
                if cnt >= 2:
                    ans += (cnt // 2) * 4
                    d[w] -= (cnt // 2) * 2
        for key in d:
            if key[0] == key[1] and d[key]:
                ans += 2
                break
        return ans