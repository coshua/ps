# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, d):
            nonlocal ans
            if not node:
                return 0
            
            left = dfs(node.left, d + 1)
            right = dfs(node.right, d + 1)
            ans = max(ans, left + right)
            return 1+ max(left, right)
        
        dfs(root, 0)
        return ans