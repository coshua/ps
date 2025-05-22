class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # "AACCGGTT"
        # "CAC..."
        # "GAC"
        # "AC"
        q = deque([startGene])

        cand = ['A', 'C', 'G', 'T']
        bankset = set(bank)
        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.pop()
                if cur == endGene:
                    return step
                for i in range(8):
                    for ch in cand:
                        nxt = cur[:i] + ch + cur[i + 1:]
                        if nxt != cur and nxt in bankset:
                            q.appendleft(nxt)
                            bankset.remove(nxt)
            step += 1

        return -1