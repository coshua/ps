# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def helper(node):
            if not node:
                return 0
            cur = node.val if node.val >= low and node.val <= high else 0
            left = right = 0
            if node.val < low:
                right = helper(node.right)
            if node.val > high:
                left = helper(node.left)
            if low <= node.val <= high:
                left, right = helper(node.left), helper(node.right)

            return cur + left + right
        return helper(root)