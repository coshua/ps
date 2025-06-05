class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        def helper(w):
            ans = [0]
            for i in range(1, len(w)):
                ans.append((ord(w[i]) - ord(w[i-1])) % 26)
            return tuple(ans)
        for word in strings:
            d[helper(word)].append(word)
        
        ans = []
        for key in d:
            ans.append(d[key])
        
        return ans
