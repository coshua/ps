class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = 0
        for c in cnt:
            if c == k // 2 and k % 2 == 0:
                ans += cnt[c] // 2
            else:
                pair = k - c
                if c < pair:
                    ans += min(cnt[c], cnt[pair])
        return ans