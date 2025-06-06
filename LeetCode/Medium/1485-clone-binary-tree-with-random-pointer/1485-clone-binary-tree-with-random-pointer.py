# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        d = {}
        if not root:
            return None
        def helper(node):
            if not node:
                return None
            cloned = d[node] if node in d else NodeCopy(node.val)
            d[node] = cloned
            if node.random and node.random not in d:
                ranNode = NodeCopy(node.random.val)
                d[node.random] = ranNode
            
            if node.random:
                ranNode = d[node.random]
                cloned.random = ranNode
            
            cloned.left = helper(node.left)
            cloned.right = helper(node.right)
            return cloned
        
        helper(root)
        return d[root]