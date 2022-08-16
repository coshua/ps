class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]):
        def buildTree(nums, lo, hi):
            if lo == hi:
                return
            maxele, maxid = -1, -1
            for i in range(lo, hi):
                if nums[i] > maxele:
                    maxele = nums[i]
                    maxid = i
            
            return TreeNode(maxele, buildTree(nums, lo, maxid), buildTree(nums, maxid + 1, hi))
        return buildTree(nums, 0, len(nums))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right