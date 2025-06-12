"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        tmp = Node(insertVal)
        if not head:
            tmp.next = tmp
            return tmp
        prev = head
        cur =  prev.next

        
        while True:
            print(prev.val, cur.val)
            if prev.val <= insertVal <= cur.val or (prev.val > cur.val and insertVal >= prev.val) or (prev.val > cur.val and insertVal <= cur.val):
                prev.next = tmp
                tmp.next = cur
                return head
            if cur == head:
                break
            prev = cur
            cur = cur.next
        prev.next = tmp
        tmp.next = cur
        return head