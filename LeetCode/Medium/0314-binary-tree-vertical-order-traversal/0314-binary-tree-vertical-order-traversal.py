# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Link:
    def __init__(self):
        self.list = []
        self.prev = None
        self.next = None

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rt = Link()
        if not root:
            return []
        rt.list.append(root.val)
        q = deque([root])
        ntl = {}
        ntl[root] = rt
        head = rt
        while q:
            sz = len(q)
            for _ in range(sz):
                cur_node = q.pop()
                cur_link = ntl[cur_node]
                if cur_node.left:
                    if not cur_link.prev:
                        cur_link.prev = Link()
                        head = cur_link.prev
                    cur_link.prev.list.append(cur_node.left.val)
                    ntl[cur_node.left] = cur_link.prev
                    cur_link.prev.next = cur_link
                    q.appendleft(cur_node.left)
                if cur_node.right:
                    if not cur_link.next:
                        cur_link.next = Link()
                    cur_link.next.list.append(cur_node.right.val)
                    ntl[cur_node.right] = cur_link.next
                    cur_link.next.prev = cur_link
                    q.appendleft(cur_node.right)

        ans = []
        while head:
            tmp = head.list[:]
            ans.append(tmp)
            head = head.next
        
        return ans