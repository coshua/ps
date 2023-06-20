from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def recursiveFinder(subs, k):
            d = defaultdict(int)
            for ch in subs:
                d[ch] += 1
            ans = len(subs)
            for i in range(len(subs)):
                if d[subs[i]] < k:
                    lo = recursiveFinder(subs[:i], k)
                    hi = recursiveFinder(subs[i + 1 :], k)
                    return max(lo, hi)

            return ans

        return recursiveFinder(s, k)


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubstring("aaaaaaaaaaaabcdefghijklmnopqrstuvwzyz", 3))
