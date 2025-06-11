# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def helper(node, cum):
            nonlocal ans

            if not node.left and not node.right:
                ans += cum*10 + node.val
                return
            
            if node.left:
                helper(node.left, cum*10 + node.val)
            if node.right:
                helper(node.right, cum*10 + node.val)
        helper(root, 0)
        return ans