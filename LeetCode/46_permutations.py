class Solution:
    def permute(self, nums):
        ln = len(nums)
        comb = list()
        v = [0] * 21
        def dfs(cur):
            if len(cur) == ln:
                comb.append(cur)
                return
            for i in nums:
                if v[i + 10] == 0:
                    v[i + 10] = 1
                    nxt = cur[:]
                    nxt.append(i)
                    dfs(nxt)
                    v[i + 10] = 0
        dfs(list())
        return comb

if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1,2,3]))