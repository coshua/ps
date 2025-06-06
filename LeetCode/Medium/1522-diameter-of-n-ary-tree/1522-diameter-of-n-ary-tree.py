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
            cands = []
            for nxt in node.children:
                cands.append(helper(nxt))
            cands.sort(reverse=True)
            nonlocal ans
            while len(cands) < 2:
                cands.append(0)
            ans = max(ans, cands[0] + cands[1])
            return max(cands) + 1
        helper(root)
        return ans