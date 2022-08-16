class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def op(s):
            mani = []
            for ch in s:
                if ch == '#':
                    if len(mani) > 0:
                        mani.pop()
                else:
                    mani.append(ch)
            return ''.join(mani)
        print(op(s))
        print(op(t))
        return op(s) == op(t)

if __name__ == "__main__":
    sol = Solution()
    print(sol.backspaceCompare("y#fo##f",
"y#f#o##f"))