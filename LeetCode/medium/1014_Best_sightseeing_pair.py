class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        maxFirst = values[0]
        maxScore = 0
        for i in range(1, len(values)):
            maxScore = max(maxScore, maxFirst - 1 + values[i])
            maxFirst = max(maxFirst - 1, values[i])
        
        return maxScore
        