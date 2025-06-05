class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        st = []
        time = 0 # always starting point
        for log in logs:
            idx, op, t = log.split(":")
            idx = int(idx)
            t = int(t)
            if op == "start":
                if st:
                    c_idx = st[-1]
                    ans[c_idx] += t-time
                st.append(idx)
                time = t
            elif op == "end":
                c_idx = st.pop()
                ans[c_idx] += t + 1 - time
                time = t + 1
        return ans