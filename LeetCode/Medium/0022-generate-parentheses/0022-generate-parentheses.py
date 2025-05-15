class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(prev, nopen):
            if len(prev) == 2 * n:
                if nopen == 0:
                    ans.append(prev)
                return
            if nopen:
                nxt= prev + ")"
                helper(nxt, nopen - 1)
            nxt = prev + "("
            helper(nxt, nopen + 1)
        
        helper("", 0)
        return ans