import collections
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        list1 = [0] * 26
        list2 = [0] * 26

        for ch in word1:
            list1[ord(ch) - ord('a')] += 1
        for ch in word2:
            list2[ord(ch) - ord('a')] += 1

        return set(word1) == set(word2) and collections.Counter(list1) == collections.Counter(list2)
        