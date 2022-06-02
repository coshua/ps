# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        trackp, trackq = [], []
        
        def findWaytoNode(node, val, queue):
            queue.append(node)
            if node.val == val:
                return
            
            if node.left != None:
                findWaytoNode(node.left, val, queue)
                
                if queue[-1].val != val:
                    queue.pop()
            
            if node.right != None:
                findWaytoNode(node.right, val, queue)
                
                if queue[-1].val != val:
                    queue.pop()
                
            return
            
            
        findWaytoNode(root, p.val, trackp)
        findWaytoNode(root, q.val, trackq)
        
        pointer = 0
        for i in range(min(len(trackq), len(trackp))):
            if trackq[i].val != trackp[i].val:
                break
            pointer = i
        
        return trackq[pointer]