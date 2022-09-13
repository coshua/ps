class FindElements:
    eles = set()

    def __init__(self, root):
        def dfs(node, val):
            if node == None:
                return
            
            self.eles.add(val)
            dfs(node.left, val * 2 + 1)
            dfs(node.right, val * 2 + 2)
        
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.eles