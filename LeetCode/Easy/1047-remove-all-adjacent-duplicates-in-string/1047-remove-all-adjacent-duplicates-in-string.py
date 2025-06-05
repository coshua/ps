class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]

        for ch in s:
            if not st or ch != st[-1]:
                st.append(ch)
            elif ch==st[-1]:
                st.pop()
        
        return "".join(st)