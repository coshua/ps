# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        def build(idx):
            if idx >= len(s):
                return None
            val = []
            pnt = idx
            tmp = TreeNode()
            while idx < len(s) and s[idx] != ')':
                if s[idx] == '(':
                    if not tmp.left:
                        tmp.left, idx = build(idx+1)
                    else:
                        tmp.right, idx = build(idx+1)
                else:
                    val.append(s[idx])
                    idx += 1
            strval = ''.join(val)
            tmp.val = int(strval)
            return tmp, idx+1
        
        head, _ = build(0)
        return head
                    