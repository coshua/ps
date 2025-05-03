class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        def calcSumfromArray(arr, cnt):
            ans = 0
            i = 0
            while cnt > 0:
                if arr[i] > 0:
                    if arr[i] <= cnt:
                        cnt -= arr[i]
                        ans += arr[i] * i
                    else:
                        ans += arr[i] * cnt
                        cnt -= cnt
                i += 1        
            return ans
        arr = [0] * (10**5)
        for i in range(len(nums)):
            acc = 0
            for j in range(i, len(nums)):
                acc += nums[j]
                arr[acc] += 1
        
        rightsum = calcSumfromArray(arr, right)
        leftsum = calcSumfromArray(arr, left - 1)
        return rightsum - leftsum