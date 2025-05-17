class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        st = []
        pnt = 0
        sz = len(asteroids)
        while pnt < sz:
            cur = asteroids[pnt]
            if cur > 0:
                st.append(cur)
            else:
                while st and st[-1] < -cur:
                    st.pop()
                if st and st[-1] == -cur:
                    st.pop()
                elif not st:
                    ans.append(cur)
            pnt += 1
        ans += st
        return ans
                