from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        acc = 0
        cnt = 0
        d = defaultdict(list)
        for i in range(len(nums)):
            acc += nums[i]
            print(k - acc, d[k - acc])
            if acc == k:
                cnt += 1
            if acc - k in d:
                print(len(d[acc - k]))
                cnt += len(d[acc - k])
            d[acc].append(i)
        print(d)
        return cnt


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.subarraySum(
            [
                1,
                1,
                1,
            ],
            2,
        )
    )
