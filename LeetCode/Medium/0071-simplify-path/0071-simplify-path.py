class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        for word in path.split('/'):
            if word == '..':
                if st:
                    st.pop()
            elif word == '.' or not word:
                continue
            else:
                st.append(word)
        return '/' + '/'.join(st)