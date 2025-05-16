class Node:
    def __init__(self):
        self.next = None
        self.prev = None
        self.elems = set()

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tail = head = Node()
        
        # num to node
        d = {}
        for n in nums:
            if n not in d:
                head.elems.add(n)
                d[n] = head
            else:
                cur = d[n]
                if not cur.next:
                    cur.next = Node()
                    tail = cur.next
                    cur.next.prev = cur
                cur.next.elems.add(n)
                cur.elems.remove(n)
                d[n] = cur.next
        ans = []
        while k > 0:
            for e in tail.elems:
                ans.append(e)
            k -= len(tail.elems)
            tail = tail.prev
        return ans