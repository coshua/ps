class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        lo, hi = 0, max(arr)
        dif = float('inf')
        ans = (lo + hi) // 2
        while lo <= hi:
            mid = (lo + hi) // 2
            arrsum = 0
            for i in range(len(arr)):
                arrsum += mid if arr[i] > mid else arr[i]
            if abs(arrsum - target) <= dif:
                if abs(arrsum - target) < dif:
                    ans = mid
                else:
                    ans = min(ans, mid)
                dif = abs(arrsum - target)
            print(lo, hi, arrsum, ans, dif)
            if arrsum > target:
                hi = mid - 1
            else:
                lo = mid + 1
                
        return ans
if __name__ == "__main__":
    solution = Solution()
    print(solution.findBestValue([2, 3, 5], 10))