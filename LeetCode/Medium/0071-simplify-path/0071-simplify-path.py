class Solution:
    def simplifyPath(self, path: str) -> str:
        path = '/' + path + '/'
        s = re.sub(r'/+', '/', path)
        st = []
        dirs = []
        for ch in s:
            if ch == '/':
                prev = ''.join(dirs)
                if prev == '..':
                    if len(st) > 1:
                        st.pop()
                    if len(st) > 1:
                        st.pop()
                elif prev != '.':
                    if prev:
                        st.append(prev)
                    st.append('/')
                dirs.clear()
            else:
                dirs.append(ch)
        if len(st) > 1 and st[-1] == '/':
            st.pop()
        if not st:
            st.append('/')
        return ''.join(st)
