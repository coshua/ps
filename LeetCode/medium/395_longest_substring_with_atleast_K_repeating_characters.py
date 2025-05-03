from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        
        maxsub = 0
        charset = [0] * 26
        for i in range(len(s)):
            if d[s[i]] >= k:
                charset[ord(s[i]) - ord('a')] += 1
            else:
                fulfill = True
                lt = 0
                for j in range(26):
                    if 0 < charset[j] < k:
                        fulfill = False
                        break
                    lt += charset[j]
                if fulfill:
                    maxsub = max(maxsub, lt)
                charset = [0] * 26
        fulfill = True
        lt = 0
        for j in range(26):
            if 0 < charset[j] < k:
                fulfill = False
                break
            lt += charset[j]
        if fulfill:
            maxsub = max(maxsub, lt)
        return maxsub

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubstring("bbaaacbd", 3))