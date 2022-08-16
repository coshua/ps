from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lst = []
        for i in nums:
            id = bisect_left(lst, i)
            if id > len(lst):
                lst.append(i)
            else:
                lst[id] = i
        return len(lst)