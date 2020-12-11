class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class creatTree:#先序遍历创建二叉树
    def __init__(self, arr):
        self.arr = arr
        self.root = None
        self.creatXian(0,None)
    def creatXian(self, k, Node):
        if k == 0:
            self.root = TreeNode(self.arr[k])
            self.creatXian(k+1,self.root)
        else:
            #Node.left
            if self.arr[k] is None:
                Node.left = None
                #Node.right
                if self.arr[k+1] is None:
                    Node.right = None
                    return k+1
                else:
                    Node.right = TreeNode(self.arr[k+1])
                    n = self.creatXian(k+2,Node.right)
                    return n
            else:
                Node.left = TreeNode(self.arr[k])
                n = self.creatXian(k+1,Node.left)

                #Node.right
                if self.arr[n+1] is None:
                    Node.right = None
                    return n+1
                else:
                    Node.right = TreeNode(self.arr[n+1])
                    n = self.creatXian(n+2,Node.right)
                    return n
        
a = creatTree([3,9,None,None,20,15,None,None,7,None,None])

class Solution:
    def __init__(self, root):
        self.root = root
        if self.root is not None:
            self.load = self.invertTree(self.root)
        else:
            self.load = None

    def invertTree(self, node):
        new_node = self.exchange(node)
        if new_node.left is not None:
            new_node.left = self.invertTree(new_node.left)
        if new_node.right is not None:
            new_node.right = self.invertTree(new_node.right)
        return new_node
        
    def exchange(self, node):
        temp = node.left
        node.left = node.right
        node.right = temp
        return node
