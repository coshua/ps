class Solution:
    def trap(self, height: list[int]) -> int:
        st = list()
        amt = 0
        for i, h in enumerate(height):
            if h > 0:
                if len(st) == 0:
                    st.append((i, h))
                else:
                    while (len(st) > 0 and st[-1][1] <= h):
                        amt += st[-1][1] * (i - st[-1][0] - 1)