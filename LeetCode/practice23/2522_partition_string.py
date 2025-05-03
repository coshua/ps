class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        cnt = acc = 0

        for i in range(len(s)):
            if acc * 10 + int(s[i]) <= k:
                acc = acc * 10 + int(s[i])
            else:
                acc = int(s[i])
                if acc > k:
                    return -1
                cnt += 1
        
        return cnt + 1