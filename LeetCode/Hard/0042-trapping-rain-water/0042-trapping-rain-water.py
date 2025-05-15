class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        q = []
        for i, h in enumerate(height):
            if not h:
                continue
            while q and q[-1][1] <= h:
                pi, ph, plv = q.pop()
                ans += (i - pi - 1) * (ph - plv)
            if q and q[-1][2] < h:
                ans += (i - q[-1][0] - 1) * (h - q[-1][2])
                q[-1][2] = h
            q.append([i, h, 0])
        return ans