class Solution:
    def nextGreaterElement(self, n: int) -> int:
        lst = []
        copy = n
        while copy > 0:
            lst.append(copy % 10)
            copy //= 10
        ln = len(lst)
        v = [False] * ln
        cnt = 0
        ans = float("inf")

        def backtrack(arr):
            if len(arr) == ln:
                nonlocal cnt
                cnt += 1
                if int("".join(list(map(str, arr)))) > n:
                    nonlocal ans
                    ans = min(ans, int("".join(list(map(str, arr)))))
                return

            for i in range(ln):
                if not v[i]:
                    v[i] = True
                    nxt = arr[:]
                    nxt.append(lst[i])
                    backtrack(nxt)
                    v[i] = False

            return

        backtrack([])
        print(cnt)
        return -1 if ans == float("inf") else ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElement(2147483486))
