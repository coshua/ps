class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        v = set([1])
        # row = rsz - ((cur-1) // n) - 1
        # col = if even odd index row (cur % n)

        step = 0
        n = len(board)
        q = deque([1])
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.pop()
                if cur == n*n:
                    return step
                for nxt in range(cur + 1, min(cur + 6, n*n) + 1):
                    r = n - ((nxt-1) // n) - 1
                    c = (nxt-1) % n
                    # reverse column idx
                    if (n+r) % 2 == 0:
                        c = n - c - 1
                    tmp = nxt
                    if board[r][c] > -1:
                        tmp = board[r][c]
                    if tmp not in v:
                        v.add(tmp)
                        q.appendleft(tmp)
            print(q)
            step += 1
                        
        return -1