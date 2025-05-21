class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.prev = self.tail
        self.tail.next = self.head
        self.d = {}
        self.cap = capacity
        self.sz = 0
    
    def _remove(self, node):
        p, n = node.prev, node.next
        if p:
            p.next = n
        if n:
            n.prev = p
        return

    def _put(self, node):
        p = self.head.prev
        p.next = node
        node.next = self.head
        self.head.prev = node
        node.prev = p

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        v = self.d[key].val
        self._remove(self.d[key])
        node = Node(key, v)
        self.d[key] = node
        self._put(node)
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            cur = self.d[key]
            self._remove(cur)
        node = Node(key, value)
        self._put(node)
        self.d[key] = node
        if len(self.d) > self.cap:
            lru = self.tail.next
            self._remove(lru)
            del self.d[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)