class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        m = dict()
        mx = 0
        for num in nums:
            if num in m:
                continue
            else:
                temp = 0
                if num + 1 in m:
                    temp += m[num + 1]
                if num - 1 in m:
                    temp += m[num - 1]
                m[num] = temp + 1
                mx = max(mx, temp + 1)
        return mx


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))