class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: list[int], informTime: list[int]
    ) -> int:
        maxtime = 0
        subordinates = [[] for _ in range(n)]

        for i in range(n):
            if i == headID:
                continue
            subordinates[manager[i]].append(i)

        def recursiveSpread(employee, time):
            maxtime = time
            for nxt in subordinates[employee]:
                maxtime = max(
                    maxtime, recursiveSpread(nxt, time + informTime[employee])
                )
            return maxtime

        return recursiveSpread(headID, 0)
