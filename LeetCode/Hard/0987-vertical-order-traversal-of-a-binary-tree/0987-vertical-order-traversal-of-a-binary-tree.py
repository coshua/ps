# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
3
9 - 3
9 - 3 - 20
9 - 3, 15 - 20 - 7

d = 
d[0] = [(0, 1), (2, 5), (2, 6)]
'''
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)

        minid = maxid = 0

        def solve(node, idx, depth):
            nonlocal minid
            nonlocal maxid
            if not node:
                return
            minid = min(minid, idx)
            maxid = max(maxid, idx)
            d[idx].append((depth, node.val))
            solve(node.left, idx - 1, depth + 1)
            solve(node.right, idx + 1, depth + 1)
        
        solve(root, 0, 0)
        ans = []
        for i in range(minid, maxid + 1):
            local = [v for d, v in sorted(d[i])]
            ans.append(local)
        return ans