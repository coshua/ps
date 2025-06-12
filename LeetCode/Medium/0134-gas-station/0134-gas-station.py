class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sz = len(gas)
        st = -1
        cur = 0
        for i in range(sz*2+1):
            ci = i % sz
            if ci == st:
                return ci
            cur += gas[ci] - cost[ci]
            if cur < 0:
                st = -1
                cur = 0
            else:
                if st == -1:
                    st = ci
        
        return -1