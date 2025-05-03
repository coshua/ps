from collections import deque
class Solution:
    def reachNumber(self, target: int) -> int:
        d = set()
        q = deque()
        q.append(0)
        d.add(0)
        moves = 1

        while q:
            num = len(q)
            for i in range(num):
                pos = q.popleft()
                if pos == target:
                    return moves - 1
                if pos - moves not in d:
                    d.add(pos-moves)
                    q.append(pos-moves)
                if pos + moves not in d:
                    d.add(pos+moves)
                    q.append(pos+moves)
            
            moves += 1