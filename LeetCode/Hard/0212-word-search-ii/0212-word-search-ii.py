class Trie:
    def __init__(self):
        self.next = [None] * 26
        self.exist = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = set()
        rsz = len(board)
        csz = len(board[0])
        v = [[False] * csz for _ in range(rsz)]
        dirs = [[-1, 0], [1, 0], [0, 1], [0,-1]]
        head = Trie()
        for word in words:
            cur = head
            for i in range(len(word)):
                ch = ord(word[i]) - ord('a')
                if not cur.next[ch]:
                    cur.next[ch] = Trie()
                cur = cur.next[ch]
                if i == len(word) - 1:
                    cur.exist = True
        def stoi(ch):
            return ord(ch) - ord('a')
        def solve(trie, r, c, path):
            if trie.exist:
                ans.add(path[:])
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rsz and 0 <= nc < csz and not v[nr][nc] and trie.next[stoi(board[nr][nc])]:
                    v[nr][nc] = True
                    nxtpath = path + board[nr][nc]
                    solve(trie.next[stoi(board[nr][nc])], nr, nc, nxtpath)
                    v[nr][nc] = False

                    
        for i in range(rsz):
            for j in range(csz):
                if head.next[stoi(board[i][j])]:
                    v[i][j] = True
                    solve(head.next[stoi(board[i][j])], i, j, board[i][j])
                    v[i][j] = False
        
        return list(ans)