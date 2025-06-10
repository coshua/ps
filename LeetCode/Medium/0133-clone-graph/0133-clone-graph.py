"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}
        v = set()
        if not node:
            return None
        def helper(cur):
            if cur in d:
                return d[cur]
            tmp = Node(cur.val)
            d[cur] = tmp
            for nxt in cur.neighbors:
                tmp.neighbors.append(helper(nxt))
            
            return tmp
        
        return helper(node)