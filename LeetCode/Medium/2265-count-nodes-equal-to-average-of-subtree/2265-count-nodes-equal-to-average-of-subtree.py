# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def calcSum(node):
            nonlocal ans
            if not node:
                return 0, 0
            
            lc, ls=calcSum(node.left)
            rc, rs = calcSum(node.right)
            cursum, curcnt = node.val + ls + rs, 1 + lc + rc
            if node.val == cursum // curcnt:
                ans += 1
            return curcnt, cursum

        calcSum(root)
        return ans