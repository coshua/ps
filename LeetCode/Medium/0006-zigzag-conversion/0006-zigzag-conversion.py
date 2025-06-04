class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        idx = 0
        dirs = 1
        if numRows == 1:
            return s
        for ch in s:
            ans[idx].append(ch)
            idx += dirs
            if idx == numRows:
                idx = numRows - 2
                dirs = -1
            elif idx == -1:
                idx = 1
                dirs = 1
        lst = []
        for i in range(numRows):
            lst.append("".join(ans[i]))

        return "".join(lst)