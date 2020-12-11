class Solution:
    def __init__(self, root):
        self.root = root
        self.load = []
        if self.root:
            self.postTraversal(self.root)

    def postTraversal(self,node):#递归
        if node.left is not None:
            self.postTraversal(node.left)
        if node.right is not None:
            self.postTraversal(node.right)

        self.load.append(node.val)

    def postTraversal(self):#迭代
        stack = []
        node = self.root
        last = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.right is None or last == node.right:
                self.load.append(node.val)
                last = node
                node = None
            else:
                stack.append(node)
                node = node.right
                
