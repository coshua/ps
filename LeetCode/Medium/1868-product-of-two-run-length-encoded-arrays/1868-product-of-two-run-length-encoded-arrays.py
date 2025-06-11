class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        p1, p2 =  0, 0
        ans = []
        while p1 < len(encoded1):
            v1, v2 = encoded1[p1][0], encoded2[p2][0]
            pdt = v1 * v2
            cnt = min(encoded1[p1][1], encoded2[p2][1])
            if ans and ans[-1][0] == pdt:
                ans[-1][1] += cnt
            else:
                ans.append([pdt, cnt])
            encoded1[p1][1] -= cnt
            encoded2[p2][1] -= cnt
            if encoded1[p1][1] == 0:
                p1 += 1
            if encoded2[p2][1] == 0:
                p2 += 1
        #ans.append([val, cnt])
        return ans