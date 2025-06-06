"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        ans = 0

        def helper(node):
            if not node:
                return
            max1 = max2 = 0
            for nxt in node.children:
                cand = helper(nxt)
                if cand > max1:
                    max1, max2 = cand, max1
                elif cand > max2:
                    max2 = cand
            nonlocal ans

            ans = max(ans, max1 + max2)
            return max1 + 1
        helper(root)
        return ans