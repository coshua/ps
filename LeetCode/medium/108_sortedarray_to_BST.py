# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        lo, hi = 0, len(nums) - 1
        def addNode(lo, hi):
            if lo > hi:
                return None
            
            mid = (lo + hi) // 2
            return TreeNode(nums[mid], addNode(lo, mid - 1), addNode(mid + 1, hi))
        
        return addNode(lo, hi)