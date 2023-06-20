class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: list[int], profit: list[int]
    ) -> int:
        dp = [0] * (n + 1)
        unmet = [[0] * (n + 1) for _ in range(minProfit)]

        for i in range(len(group)):
            curppl, curprofit = group[i], profit[i]
            if curppl > n:
                pass
            q = []
            for nppl in range(1, n - curppl + 1):
                if dp[nppl]:
                    q.append(nppl)
            uq = []
            for nppl in range(1, n - curppl + 1):
                for nprofit in range(minProfit - curprofit, minProfit):
                    dp[nppl + curppl] += unmet[nprofit][nppl]
                for lessprofit in range(minProfit - curprofit):
                    if unmet[lessprofit][nppl]:
                        uq.append((lessprofit, nppl))
            for lp, nppl in uq:
                unmet[lp + curprofit][nppl + curppl] += unmet[lp][nppl]
            for np in q:
                dp[np + curppl] += 1
            if curprofit >= minProfit:
                dp[curppl] += 1
            else:
                unmet[curprofit][curppl] += 1
        print(dp)
        print(unmet)
        return sum(dp)


if __name__ == "__main__":
    sol = Solution()
    print(sol.profitableSchemes(5, 3, (2, 2), (2, 3)))
