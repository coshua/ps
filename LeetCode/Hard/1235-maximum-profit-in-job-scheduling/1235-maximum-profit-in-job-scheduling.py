class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        # base case
        dp_id = [-1]
        dp_val = [0]
        sz = len(startTime)
        for i in range(sz):
            jobs.append((endTime[i], startTime[i], profit[i]))
        jobs.sort()

        for e, s, p in jobs:
            pmax_id = bisect.bisect_right(dp_id, s)
            mp = max(dp_val[pmax_id - 1] + p, dp_val[-1])
            dp_id.append(e)
            dp_val.append(mp)
        
        return dp_val[-1]