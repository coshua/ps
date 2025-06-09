# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        q = deque([root])
        while q:
            if len(ans) % 2:
                ans.append([node.val for node in q])
            else:
                ans.append([node.val for node in reversed(q)])
            sz = len(q)
            for _ in range(sz):
                cur = q.pop()
                if cur.left:
                    q.appendleft(cur.left)
                if cur.right:
                    q.appendleft(cur.right)
        return ans