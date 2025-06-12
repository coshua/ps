# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        q = [root]
        while q:
            nq = []
            ans.append(q[-1].val)
            for i in range(len(q)):
                cur = q[i]
                if cur.left:
                    nq.append(cur.left)
                if cur.right:
                    nq.append(cur.right)
            q = nq
        return ans