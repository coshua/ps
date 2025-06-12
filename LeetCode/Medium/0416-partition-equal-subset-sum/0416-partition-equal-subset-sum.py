class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        dp = set([0])
        path = {0: -1}
        t = total // 2

        for n in nums:
            ns = set()
            for key in dp:
                if key+n not in dp:
                    ns.add(key+n)
                    path[key+n] = key
            dp = dp | ns
        
        if t in dp:
            cur = t
            prev = path[t]
            ans = []
            while prev > -1:
                ans.append(cur-prev)
                cur = prev
                prev = path[prev]
            return True
        return False