from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        numcnt = defaultdict(int)
        
        for num in nums:
            numcnt[num] += 1

        ansfornum = {}
        
        temp = 1
        
        for key in numcnt:
            if numcnt[key] > 1:
                temp *= key ** (numcnt[key] - 1)
        
        for key in numcnt:
            cur = temp
            for s_key in numcnt:
                if key != s_key:
                    cur *= s_key
            ansfornum[key] = cur
        
        ans = []
        for num in nums:
            ans.append(ansfornum[num])
            
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([5,9,2,-9,-9,-7,-8,7,-9,10]))

        