class Solution:
    fst, lst = -1, -1
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def bnSearch(s, e):
            if s >= e:
                return
            mid = (s + e) // 2
            if nums[mid] == target:
                if self.fst == -1:
                    self.fst, self.lst = mid, mid
                else:
                    self.fst = min(self.fst, mid)
                    self.lst = max(self.lst, mid)
            bnSearch(mid + 1, e)
            bnSearch(s, mid)
        
        bnSearch(0, len(nums))

        return [self.fst, self.lst]
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([1,2,3,3,3,3,4,5,9], 3))
        