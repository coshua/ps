class Solution:
    def reverseParentheses(self, s: str) -> str:
        openBrk = []
        ln = len(s)
        ans = []
        for i in range(ln):
            ans.append(s[i])
            if s[i] == "(":
                openBrk.append(i)
            elif s[i] == ")":
                start = openBrk.pop()
                ans[start : i + 1] = reversed(ans[start : i + 1])
                ans[start] = "."
                ans[i] = "."
        output = ""
        for ch in ans:
            if ch != ".":
                output += ch
        return output


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseParentheses("(ed(et(oc))el)"))
