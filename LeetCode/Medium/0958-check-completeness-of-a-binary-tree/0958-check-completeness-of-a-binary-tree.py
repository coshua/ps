# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [(root, 1)]
        
        prev = 0
        while q:
            sz = len(q)
            nq = []
            for i in range(sz):
                cur, v = q[i]
                if v - 1 != prev:
                    return False
                prev = v

                if cur.left:
                    nq.append((cur.left, v*2))
                if cur.right:
                    nq.append((cur.right, v*2+1))
            q = nq

        return True