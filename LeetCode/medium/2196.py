# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]):
        d = dict()
        p = defaultdict(int)
        
        for parent, child, isLeft in descriptions:
            node = None
            if parent in d:
                node = d[parent]
            else:
                node = TreeNode(val=parent)
                d[parent] = node
            if isLeft:
                if child in d:
                    node.left = d[child]
                else:
                    node.left = TreeNode(val=child)
                    d[child] = node.left
            else:
                if child in d:
                    node.right = d[child]
                else:
                    node.right = TreeNode(val=child)
                    d[child] = node.right
            
            p[child] = parent
        
        root = descriptions[0][0]
        while p[root] != 0:
            root = p[root]
        return root

if __name__  == "__main__":
    sol = Solution()
    print(sol.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))