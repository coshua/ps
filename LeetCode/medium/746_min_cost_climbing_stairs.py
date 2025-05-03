class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost = [0] + cost
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
        
        return min(cost[-1], cost[-2])

if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostClimbingStairs([2, 3, 4, 4, 10, 5]))