import bisect
class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        optidx = []
        for i in range(len(intervals)):
            optidx.append([intervals[i][0], i])
        
        optidx.sort()
        meta = [num[0] for num in optidx]
        ans = []
        for interval in intervals:
            id = bisect.bisect_left(meta, interval[1])
            if id == len(optidx):
                ans.append(-1)
            else:
                ans.append(optidx[id][1])
        
        return ans