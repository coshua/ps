# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        head = ListNode()
        cur = head

        for i in range(len(lists)):
            c = lists[i]
            if c:
                heapq.heappush(q, (c.val, i, c))
        
        while q:
            v, i, c = heapq.heappop(q)
            cur.next = c
            if c.next:
                heapq.heappush(q, (c.next.val, i, c.next))
            cur = c
            cur.next = None
        return head.next
