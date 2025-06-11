class Solution:
    def isHappy(self, n: int) -> bool:
        v=set([n])
        while True:
            nxt = 0
            while n:
                nxt += (n%10)**2
                n//=10
            if nxt == 1:
                return True
            if nxt in v:
                return False
            v.add(nxt)
            n = nxt