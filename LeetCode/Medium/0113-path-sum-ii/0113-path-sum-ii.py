# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return []
        def recursive(node, cum, path, target):
            newpath = path[:] + [node.val]
            cum += node.val
            if not node.left and not node.right:
                if cum == target:
                    ans.append(newpath)
                    return
                
            if node.left:
                nxt = path[:] + [node.val]
                recursive(node.left, cum, nxt, target)
            if node.right:
                nxt = path[:] + [node.val]
                recursive(node.right ,cum, nxt, target)

        recursive(root, 0, [], targetSum)
        return ans