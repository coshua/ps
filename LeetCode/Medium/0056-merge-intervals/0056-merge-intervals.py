class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[1])

        st = []
        for iv in intervals:
            while st and iv[0] <= st[-1][1]:
                plo, phi = st.pop()
                iv = [min(plo,iv[0]), max(phi,iv[1])]
            st.append(iv)
        return st