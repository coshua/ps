class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        d = {} # partial_sum -> list
        d[0] = []
        t = total // 2
        for n in nums:
            if t-n in d:
                d[t] = d[t-n] + [n]
                print(d[t])
                return True
            nxt = []
            for key in d:
                if key+n not in d:
                    nxt.append((key+n, d[key] + [n]))
            for key, elem in nxt:
                d[key] = elem
        return False