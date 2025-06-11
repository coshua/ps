# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def helper(node):
            nonlocal ans
            if ans:
                return False, False
            if not node:
                return False, False
            lp, lq = helper(node.left)
            rp, rq = helper(node.right)
            cp, cq = node.val == p.val, node.val == q.val
            if (lp or rp or cp) and (lq or rq or cq) and not ans:
                ans = node
            return (lp or rp or cp), (lq or rq or cq)

        helper(root)
        return ans
