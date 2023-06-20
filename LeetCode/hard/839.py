from collections import defaultdict


class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        def compareWords(f, s):
            ln = len(f)
            diff = 0
            for i in range(ln):
                if f[i] != s[i]:
                    diff += 1
                    if diff > 2:
                        break

            return diff <= 2

        d = defaultdict(int)
        for word in strs:
            d[word] += 1
        v = set()
        groupscnt = 0

        for word in strs:
            if word not in v:
                groupscnt += 1
                q = [word]
                while q:
                    cur = q.pop()
                    for nxtword in d:
                        if d[nxtword] > 0:
                            if compareWords(cur, nxtword):
                                # if two anagrams are neighbors of each other
                                d[nxtword] = 0
                                q.append(nxtword)
                                v.add(nxtword)
        return groupscnt
