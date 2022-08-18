class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        d = dict()
        ans = -1
        for num in nums:
            ori = num
            digitSum = 0
            while num > 0:
                digitSum += num % 10
                num = num // 10
            
            if digitSum in d:
                ans = max(ans, d[digitSum] + ori)
                d[digitSum] = max(d[digitSum], ori)
            else:
                d[digitSum] = ori
        
        return ans