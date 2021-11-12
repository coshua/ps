class Solution:
    def subsets(self, nums):
        comb = list()
        v = [0] * len(nums)
        def dfs(subnum, id):
            comb.append(subnum)
            for i in range(len(nums)):
                if v[i] == 0 and i > id:
                    temp = subnum[:]
                    temp.append(nums[i])
                    v[i] = 1
                    dfs(temp, i)
                    v[i] = 0
        dfs([], -1)
        return comb
if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
    