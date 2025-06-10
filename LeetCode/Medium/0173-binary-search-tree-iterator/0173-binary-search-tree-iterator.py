# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = deque([root])

    def update(self):
        if not self.st:
            return
        if type(self.st[0]) is int:
            return
        cur = self.st.popleft()
        if cur.right:
            self.st.appendleft(cur.right)
        self.st.appendleft(cur.val)
        if cur.left:
            self.st.appendleft(cur.left)
        self.update()
    def next(self) -> int:
        self.update()
        cur = self.st.popleft()
        self.update()
        return cur

    def hasNext(self) -> bool:
        return len(self.st) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()