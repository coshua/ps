# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        leaves = []
        
        def helper(node, d, include, arr, leaves):
            if not node:
                return
            if d == -1:
                node.left, node.right = node.right, node.left
            # leaf
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            
            if node.left:
                if include:
                    arr.append(node.val)
                helper(node.left, d, include and True, arr, leaves)
                helper(node.right, d, False, arr, leaves)
                return
            if node.right:
                if include:
                    arr.append(node.val)
                helper(node.right, d, include and True, arr, leaves)
        left,right,left_leave,right_leave = [],[],[],[]
        helper(root.left, 0, True, left,left_leave)
        helper(root.right, -1, True, right,right_leave)
        return [root.val] + left + left_leave + right_leave[::-1] + right[::-1]
        print(left, left_leave, right_leave[::-1], right[::-1])
