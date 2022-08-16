# need better solution, preferably O(n)
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        cnt = 0
        dp = [[0] * 3 for _ in range(1690)]

        pq = [1]
        while cnt < 1690:
            minnum = heapq.heappop(pq)
            dp[cnt] = [minnum * 2, minnum * 3, minnum * 5]
            if minnum * 2 not in pq:
                heapq.heappush(pq, minnum * 2)
            if minnum * 3 not in pq:
                heapq.heappush(pq, minnum * 3)
            if minnum * 5 not in pq:
                heapq.heappush(pq, minnum * 5)

            cnt += 1
        pointer = 1
        idx_2 = 0
        idx_3 = 0
        idx_5 = 0
        while n > 1:
            if dp[idx_2][0] <= dp[idx_3][1] and dp[idx_2][0] <= dp[idx_5][2]:
                if dp[idx_2][0] == pointer:
                    n += 1
                pointer = dp[idx_2][0]
                idx_2 += 1
            
            elif dp[idx_3][1] <= dp[idx_2][0] and dp[idx_3][1] <= dp[idx_5][2]:
                if dp[idx_3][1] == pointer:
                    n += 1
                pointer = dp[idx_3][1]
                idx_3 += 1
            
            else:
                if dp[idx_5][2] == pointer:
                    n += 1
                pointer = dp[idx_5][2]
                idx_5 += 1

            n -= 1
        
        return pointer

if __name__ == "__main__":
    sol = Solution()
    print(sol.nthUglyNumber(10))