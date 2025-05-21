class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        oddtoptwo = [0, 0]
        oddtopidx = [-1,-1]
        oddtop = defaultdict(int)
        eventoptwo = [0, 0]
        eventopidx = [-1,-1]
        eventop = defaultdict(int)
        sz = len(nums)
        for i in range(sz):
            n = nums[i]
            if i % 2 == 0:
                eventop[n] += 1
            else:
                oddtop[n] += 1

        for elem, cnt in eventop.items():
            if cnt > eventoptwo[0]:
                eventoptwo = [cnt, eventoptwo[0]]
                eventopidx = [elem, eventopidx[0]]
            elif cnt > eventoptwo[1]:
                eventoptwo[1] = cnt
                eventopidx[1] = elem
        
        for elem, cnt in oddtop.items():
            if cnt > oddtoptwo[0]:
                oddtoptwo = [cnt, oddtoptwo[0]]
                oddtopidx = [elem, oddtopidx[0]]
            elif cnt > oddtoptwo[1]:
                oddtoptwo[1] = cnt
                oddtopidx[1] = elem
        
        oddsz = sz // 2
        evensz = math.ceil(sz/2)
        
        if eventopidx[0] != oddtopidx[0]:
            return sz - oddtoptwo[0] - eventoptwo[0]
        else:
            return sz - max(eventoptwo[0] + oddtoptwo[1], eventoptwo[1] + oddtoptwo[0])