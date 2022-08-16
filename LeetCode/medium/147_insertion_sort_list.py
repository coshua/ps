# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from queue import PriorityQueue
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        q = PriorityQueue()
        while (head != None):
            q.put(head.val)
            head = head.next
        ans = None
        cur = ListNode()
        while (q.qsize() > 0):
            cur.val = q.get()
            if ans == None:
                ans = cur
            if q.qsize() == 0:
                break
            cur.next = ListNode()
            cur = cur.next
        return ans