from collections import deque
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        v = [0] * len(nums)
        q = deque()
        v[0] = 1
        # q stores current position and jump length
        q.append((0, nums[0]))
        while(q):
            cur, jump = q.popleft()
            for i in range(1, jump + 1):
                nxt = cur + i
                if nxt >= len(nums) - 1:
                    return True
                
                if v[nxt] == 0:
                    v[nxt] = 1
                    q.append((nxt, nums[nxt]))
        
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump([3, 2, 1, 0, 4]))