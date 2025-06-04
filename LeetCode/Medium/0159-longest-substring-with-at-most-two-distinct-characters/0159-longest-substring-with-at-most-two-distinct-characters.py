class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        lo = hi = 0
        
        ans = 0
        track = {}

        while hi < len(s):
            if s[hi] not in track:
                track[s[hi]] = 0
            track[s[hi]] += 1

            while len(track) > 2:
                prev = s[lo]
                track[prev] -= 1
                if track[prev] == 0:
                    del track[prev]
                lo += 1
            ans = max(ans, hi - lo  + 1)
            hi += 1
        return ans