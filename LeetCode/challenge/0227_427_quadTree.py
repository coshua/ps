
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        def recursiveValidateLeaf(sr, sc, er, ec):
            curnode = Node()
            isleaf = True
            for r in range(sr, er):
                for c in range(sc, ec):
                    if grid[r][c] != grid[sr][sc]:
                        isleaf = False
                        break
            curnode.val = grid[sr][sc]
            curnode.isLeaf = isleaf
            if not isleaf:
                curnode.topLeft = recursiveValidateLeaf(sr, sc, (sr + er) // 2, (sc + ec) // 2)
                curnode.topRight = recursiveValidateLeaf(sr, sc + (ec - sc) // 2, (sr + er) // 2, ec)
                curnode.bottomLeft = recursiveValidateLeaf((sr + er) // 2, sc, er, (sc + ec) // 2)
                curnode.bottomRight = recursiveValidateLeaf((sr + er) // 2, (sc + ec) // 2, er, ec)
            return curnode
        sr, sc, er, ec = 0, 0, len(grid), len(grid[0])
        head = recursiveValidateLeaf(sr, sc, er, ec)
        return head

        