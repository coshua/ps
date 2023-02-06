from collections import deque
class Solution:
    def minInsertions(self, s: str) -> int:
        st = deque()
        cnt = 0
        for ch in s:
            if ch == '(':
                if len(st) == 0 or st[-1] == '(':
                    st.append(ch)
                else:
                    cnt += 1
                    st.pop()
                    st.pop()
                    st.append(ch)
            else:
                if len(st) == 0:
                    st.append('(')
                    cnt += 1
                    st.append(ch)
                elif st[-1] == '(':
                    st.append(ch)
                else:
                    st.pop()
                    st.pop()
        
        if st and st[-1] == ')':
            cnt += 1
            st.pop()
            st.pop()
        
        cnt += len(st) * 2

        return cnt