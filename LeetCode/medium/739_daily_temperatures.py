

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        daytowait = [0] * len(temperatures)
        q = []

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while len(q) > 0 and temp > temperatures[q[-1]]:
                daytowait[q[-1]] = i - q[-1]
                q.pop()
            q.append(i)
        return daytowait

if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
