from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        if root != None:
            q.append(root)
        nxtq = deque()
        prev = None
        while q:
            curNode = q.popleft()
            if prev != None:
                prev.next = curNode
            prev = curNode
            if curNode.left != None:
                nxtq.append(curNode.left)
            if curNode.right != None:
                nxtq.append(curNode.right)
            
            if not q:
                prev = None
                q = nxtq
                nxtq = deque()
        return root


        