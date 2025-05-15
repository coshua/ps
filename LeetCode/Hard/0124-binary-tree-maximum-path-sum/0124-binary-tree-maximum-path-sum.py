# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')

        def rec(node):
            nonlocal ans
            if not node:
                return -float('inf')
            left_max = rec(node.left)
            right_max = rec(node.right)
            ans = max([ans, left_max, right_max, left_max + right_max + node.val, node.val, node.val + right_max, node.val + left_max])
            max_return = max([node.val, node.val + left_max, node.val+right_max])
            return max_return
        
        rec(root)

        return ans