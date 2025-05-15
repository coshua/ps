class Solution:
    def reorganizeString(self, s: str) -> str:
        occ = [0] * 26
        for ch in s:
            occ[ord(ch) - ord('a')] += 1
        
        q = []
        for i in range(26):
            if occ[i]:
                q.append((-occ[i], chr(i + ord('a'))))
        heapq.heapify(q)
        ans = ""
        while q:
            cur, ch = heapq.heappop(q)
            if not ans or ans[-1] != ch:
                ans += ch
                if cur < -1:
                    heapq.heappush(q, (cur + 1, ch))
            else:
                if not q:
                    return ""
                sndocc, sndch = heapq.heappop(q)
                ans += sndch
                heapq.heappush(q, (cur, ch))
                if sndocc < -1:
                    heapq.heappush(q, (sndocc + 1, sndch))
        
        return ans