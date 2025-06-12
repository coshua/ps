# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans = 0
        def helper(node):
            nonlocal k
            nonlocal ans
            if not node:
                return
            if k < 1:
                return
            lv = helper(node.left)
            if k==1:
                ans = node.val
                k-=1
                return
            k-=1
            rv = helper(node.right)
        
        helper(root)
        return ans