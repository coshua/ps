class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = defaultdict(set)
        maxsize = 0
        def backtrack(st, path, idx):
            if idx == len(s):
                nonlocal maxsize
                if not st and len(path) >= maxsize:
                    maxsize = max(maxsize, len(path))
                    ans[len(path)].add(''.join(path))
                return
                
            ch = s[idx]
            if ch.isalpha():
                backtrack(st, path + [ch], idx + 1)
            elif ch == '(':
                st1 = st[:]
                st2 = st1[:] + ['(']
                path1 = path[:]
                path2 = path[:] + ['(']
                backtrack(st1, path1, idx + 1)
                backtrack(st2, path2, idx + 1)
            else:
                if st:
                    st1 = st[:]
                    st1.pop()
                    backtrack(st1, path + [ch], idx + 1)
                st2 = st[:]
                backtrack(st2, path, idx + 1)
        backtrack([], [], 0)
        return list(ans[maxsize])