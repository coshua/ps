# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        prev = None
        dum = ListNode()
        dum.next = head
        fast = cur = dum
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            prev = cur
            cur = cur.next
        prev.next = cur.next
        return dum.next