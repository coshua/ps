from collections import deque
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        score = 0
        st = deque()
        s = set()
        ans = 0

        for i in range(len(nums)):
            if nums[i] in s:
                while st[0] != nums[i]:
                    removed = st.popleft()
                    score -= removed
                    s.remove(removed)
                st.popleft()
            else:
                score += nums[i]
                s.add(nums[i])
            st.append(nums[i])
            ans = max(ans, score)
        
        return ans

            
            