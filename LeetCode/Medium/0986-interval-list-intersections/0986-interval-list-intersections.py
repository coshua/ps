class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        pnt1 = pnt2 = 0
        ans = []
        while pnt1 < len(firstList) and pnt2 < len(secondList):
            while pnt1 < len(firstList) and firstList[pnt1][1] < secondList[pnt2][0]:
                pnt1 += 1
            if pnt1 == len(firstList):
                return ans
            while pnt2 < len(secondList) and secondList[pnt2][1] < firstList[pnt1][0]:
                pnt2 += 1
            if pnt2 == len(secondList):
                return ans
            
            lo, hi = max(firstList[pnt1][0], secondList[pnt2][0]), min(firstList[pnt1][1], secondList[pnt2][1])
            if lo <= hi:
                ans.append([lo,hi])
            if firstList[pnt1][1] < secondList[pnt2][1]:
                pnt1 += 1
            else:
                pnt2 += 1
    
        return ans
        