class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dct = set(wordDict)
        sz = len(s)
        ans = [[] for _ in range(sz)]

        for i in range(sz):
            for j in range(i + 1):
                tmp = s[j:i + 1]
                if tmp in dct:
                    if j == 0:
                        ans[i].append(tmp)
                    else:
                        for prev in ans[j-1]:
                            ans[i].append(prev + " " + tmp)

        return ans[-1]