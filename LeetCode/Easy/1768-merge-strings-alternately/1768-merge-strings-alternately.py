class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        ans = []
        while p1 < len(word1) and p2 < len(word2):
            if p1 <= p2:
                ans.append(word1[p1])
                p1 += 1
            else:
                ans.append(word2[p2])
                p2 += 1
        ans += word1[p1:]
        ans += word2[p2:]

        return ''.join(ans)