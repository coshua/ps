class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        ans = []
        while p1 < len(word1) or p2 < len(word2):
            if p1 == len(word1):
                ans.append(word2[p2])
                p2 += 1
            elif p2 == len(word2):
                ans.append(word1[p1])
                p1 += 1
            else:
                if word1[p1] == word2[p2]:
                    if word1[p1:] > word2[p2:]:
                        ans.append(word1[p1])
                        p1 += 1
                    else:
                        ans.append(word2[p2])
                        p2 += 1
                elif word1[p1] > word2[p2]:
                    ans.append(word1[p1])
                    p1 += 1
                else:
                    ans.append(word2[p2])
                    p2 += 1
        return "".join(ans)