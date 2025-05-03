from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        m = defaultdict(int)
        parent = defaultdict(int)

        def find(x):
            if parent[x] == 0:
                return x
            y = find(parent[x])
            parent[x] = y
            return y
        
        mx = 1 if len(nums) > 0 else 0
        for num in nums:
            num += 10 ** 9 + 1
            if m[num] > 0:
                continue

            m[num] = 1
            pless = find(num - 1)
            pgreater = find(num + 1)
            
            # current num merges two sequence
            if m[pless] > 0 and m[pgreater] > 0 and pless != pgreater:
                if m[pless] >= m[pgreater]:
                    m[pless] += m[pgreater] + 1
                    parent[pgreater] = pless
                    parent[num] = pless
                else:
                    m[pgreater] += m[pless] + 1
                    parent[pless] = pgreater
                    parent[num] = pgreater
            
            elif m[pless] > 0 and m[pgreater] == 0:
                m[pless] += 1
                parent[num] = pless

            elif m[pless] == 0 and m[pgreater] > 0:
                m[pgreater] += 1
                parent[num] = pgreater

            mx = max(mx, max(m[pless], m[pgreater]))
        return mx


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))