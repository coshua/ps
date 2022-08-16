class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        pos = 0 # 
        result = 0
        length = 0
        neg_index = -1
        for i in range(len(nums)):
            # first column longest negative, second positive
            if nums[i] == 0:
                length = 0
                neg_index = -1
                pos = 0
            elif nums[i] > 0:
                if length == 0:
                    pos = 1
                length += 1
                if pos:
                    result = max(result, length)
                else:
                    result = max(result, i - neg_index)
            else:
                if neg_index < 0:
                    neg_index = i
                if length > 0:
                    pos ^= 1
                length += 1
                if pos:
                    result = max(result, length)
                else:
                    result = max(result, i - neg_index)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.getMaxLen([-10,-1, 0, -4,-3,10,-10]))
