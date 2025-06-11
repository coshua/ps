# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d = defaultdict(list)
        def build(node):
            if not node: return
            if node.left:
                d[node.left.val].append(node.val)
                d[node.val].append(node.left.val)
            if node.right:
                d[node.right.val].append(node.val)
                d[node.val].append(node.right.val)
            build(node.left)
            build(node.right)
        
        build(root)
        q = [target.val]
        v = set([target.val])
        while q:
            sz = len(q)
            nq = []
            if k == 0:
                return q
            for _ in range(sz):
                cur = q.pop()
                for nxt in d[cur]:
                    if nxt not in v:
                        nq.append(nxt)
                        v.add(nxt)
            k -= 1
            q = nq
        return []