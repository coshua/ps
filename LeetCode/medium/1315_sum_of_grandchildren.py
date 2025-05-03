class Solution:
    ans = 0
    def sumEvenGrandparent(self, root) -> int:
        def sumGrandchildren(root):
            if root == None:
                return
            if root % 2 == 0:
                sumChildren(root.right)
                sumChildren(root.left)
            else:
                sumGrandchildren(root.right)
                sumGrandchildren(root.left)
        
        def sumChildren(root):
            if root == None:
                return 0
            self.ans += root.left.val if root.left else 0
            self.ans += root.right.val if root.right else 0
            if root % 2 == 0:
                sumChildren(root.right)
                sumChildren(root.left)
            else:
                sumGrandchildren(root.right)
                sumGrandchildren(root.left)
        
        sumGrandchildren(root)
        return self.ans
        