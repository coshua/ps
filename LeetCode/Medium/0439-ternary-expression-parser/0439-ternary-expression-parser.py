class Solution:
    def parseTernary(self, expression: str) -> str:
        st = []
        for ex in expression[::-1]:
            if st and st[-1] == '?':
                st.pop()
                b = st.pop()
                st.pop()
                c = st.pop()
                a_truth = False if ex == 'F' else True

                ev = b if a_truth else c
                st.append(ev)
            else:
                st.append(ex)
        return st[-1]
