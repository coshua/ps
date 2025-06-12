class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ans = 0
        prev = 0 #idx
        nums.sort()
        st = deque()
        cost = 0 
        for i, n in enumerate(nums):
            if nums[i] != nums[prev]:
                ans = max(ans, len(st))
                cost += (nums[i]-nums[prev]) * len(st)
                while cost > k:
                    old = st.popleft()
                    cost -= (nums[i] - nums[old])
                prev = i
            st.append(i)
        ans = max(ans, len(st))
        return ans