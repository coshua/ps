"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        first = None
        last = None
        if not root:
            return root

        def inorder(node):
            if not node:
                return
            nonlocal first, last
            inorder(node.left)
            if not first:
                first = node
            else:
                last.right = node
                node.left = last
            last = node
            inorder(node.right)
            return
        inorder(root)
        first.left = last
        last.right = first
        return first
