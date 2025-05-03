class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        profit_sum = 0

        task_p, worker_p = 0, 0
        cur_profit = 0
        while worker_p < len(worker):
            while task_p < len(jobs) and jobs[task_p][0] <= worker[worker_p]:
                cur_profit = max(cur_profit, jobs[task_p][1])
                task_p += 1

            profit_sum += cur_profit
            worker_p += 1
        
        return profit_sum