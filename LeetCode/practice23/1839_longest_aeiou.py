class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        index_a = -1
        maxlen = 0
        chset = set()
        for i in range(len(word)):
                # holds valid string and it continues
            if i > 0 and word[i] >= word[i - 1]:
                chset.add(word[i])
                if len(chset) == 5:
                    maxlen = max(maxlen, i - index_a + 1)
                # held valid string but not anymore
            else:
                chset = set()
                chset.add(word[i])
                index_a = i

        return maxlen