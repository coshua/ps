from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dec = deque()
        for i in range(k):
            while dec and dec[-1] < nums[i]:
                dec.pop()
            dec.append(nums[i])
        ans = [dec[0]]
        for i in range(k, len(nums)):
            if dec[0] == nums[i - k]:
                dec.popleft()
            while dec and dec[-1] < nums[i]:
                dec.pop()
            dec.append(nums[i])
            ans.append(dec[0])
