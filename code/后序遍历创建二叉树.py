class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class creatTree:#后序遍历创建二叉树
    def __init__(self, arr):
        self.arr = arr
        self.arr.reverse()
        self.root = None
        self.count = 0
        if self.arr != []:
            self.lenth = len(self.arr)
            self.creat(self.root)

    def creat(self, node):
        if self.count == 0:
            self.root = TreeNode(self.arr[self.count])
            self.count += 1
            self.creat(self.root)
        else:
            if self.arr[self.count] == None:
                self.count += 1
            else:
                node.right = TreeNode(self.arr[self.count])
                self.count += 1
                self.creat(node.right)
            if self.arr[self.count] == None:
                self.count += 1
            else:
                node.left = TreeNode(self.arr[self.count])
                self.count += 1
                self.creat(node.left)

a = [None,None,9,None,None,15,None,None,7,20,3]
