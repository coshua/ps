class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = [] # (ch, cnt)
        for ch in s:
            if not st or st[-1][0] != ch:
                st.append((ch, 1))
            else:
                _, cnt = st.pop()
                cnt += 1
                if cnt < k:
                    st.append((ch, cnt))
        
        ans = []
        for ch, n in st:
            ans += [ch] * n
        return ''.join(ans)