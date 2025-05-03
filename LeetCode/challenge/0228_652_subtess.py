from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:
        d = defaultdict(int)
        ans = []
        def serialize(node):
            if node == None:
                return 'x'
            
            s = str(node.val)
            s += serialize(node.left) + serialize(node.right)

            d[s] += 1
            if d[s] == 2:
                ans.append(node)

            return s
        
        serialize(root)
        return ans