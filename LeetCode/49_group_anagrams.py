from collections import defaultdict
class Solution:
    def translate_into_key(self, s):
        lst = [0] * 26
        for c in s:
            lst[ord(c) - ord('a')] += 1
        return tuple(lst)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for s in strs:
            tup = self.translate_into_key(s)
            d[tup].append(s)
        ans = list()
        for key in d:
            ans.append(d[key])
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
