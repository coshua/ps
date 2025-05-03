class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rightpair, leftpair = [], []

        for i in range(len(s)):
            if s[i] == ')':
                if leftpair:
                    leftpair.pop()
                else:
                    rightpair.append(i)
            elif s[i] == '(':
                leftpair.append(i)
        
        p_r, p_l = 0, 0
        ans = ""
        for i in range(len(s)):
            if rightpair and p_r < len(rightpair) and rightpair[p_r] == i:
                p_r += 1
                continue
            elif leftpair and p_l < len(leftpair) and leftpair[p_l] == i:
                p_l += 1
                continue
            ans += s[i]
        
        return ans