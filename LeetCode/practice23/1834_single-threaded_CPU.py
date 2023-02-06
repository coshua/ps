import heapq
class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        tasks_orders = [0] * len(tasks)
        for i in range(len(tasks)):
            tasks_orders[i] = (tasks[i][0], tasks[i][1], i)
        
        tasks_orders.sort()
        pq = [(tasks_orders[0][1], tasks_orders[0][2])]
        ans = []
        p = 1
        cur_time = tasks_orders[0][0]
        while p < len(tasks):
            if not pq:
                duration, idx = tasks_orders[p][1], tasks_orders[p][2]
                cur_time = tasks_orders[p][0] + duration
                p += 1
            else:
                duration, idx = heapq.heappop(pq)
                cur_time += duration
            ans.append(idx)
            
            while p < len(tasks) and tasks_orders[p][0] <= cur_time:
                heapq.heappush(pq, (tasks_orders[p][1], tasks_orders[p][2]))
                p += 1
        
        while pq:
            ans.append(heapq.heappop(pq)[1])
        return ans