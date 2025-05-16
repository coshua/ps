# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = float('inf')

        def dfs(node, t):
            nonlocal ans
            if not node:
                return
            if abs(node.val - t) < abs(ans - t):
                ans = node.val
            elif abs(node.val - t) == abs(ans - t) and node.val < ans:
                ans = node.val
            dfs(node.left, t)
            dfs(node.right, t)
        dfs(root, target)
        return ans