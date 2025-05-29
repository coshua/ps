class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valid = [True] * len(s)
        st = [] # track id

        for i in range(len(s)):
            c = s[i]
            if c == ')':
                if not st:
                    valid[i] = False
                else:
                    st.pop()
            elif c == '(':
                st.append(i)
        
        for idx in st:
            valid[idx] = False
        
        ans = ""
        for i in range(len(s)):
            if valid[i]:
                ans += s[i]
        return ans