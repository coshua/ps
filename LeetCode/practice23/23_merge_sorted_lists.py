import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        dummy = cur = ListNode()
        q = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
        
        while q:
            v, i = heapq.heappop(q)
            cur.next = ListNode(v)
            cur = cur.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
        
        return dummy.next