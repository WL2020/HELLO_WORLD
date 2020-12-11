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
b = creatTree([3,2,1,None,None,None,4,None,None])

class Solution:
    def __init__(self,t1,t2):
        self.t1 = t1
        self.t2 = t2
        self.new = self.mergeTree(self.t1, self.t2)
        print(self.new.val)

    def mergeTree(self, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1        
        new = TreeNode(node1.val + node2.val)
        new.left = self.mergeTree(node1.left, node2.left)
        new.right = self.mergeTree(node1.right, node2.right)
        return new
