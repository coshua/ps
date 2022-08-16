# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = [[], []]
        idx = 0
        if root != None:
            q[idx].append(root)
        
        height = 0
        while len(q[idx]) > 0:
            for node in q[idx]:
                if node.left != None:
                    q[idx ^ 1].append(node.left)
                if node.right != None:
                    q[idx ^ 1].append(node.right)
            q[idx] = []
            idx ^= 1
            height += 1
        
        return height