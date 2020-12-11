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
    def __init__(self, root):
        self.root = root
        self.nums = 0
        if self.root is not None:
            self.num = self.convertBST(self.root)

    def convertBST(self, node):
        if node.right is not None:
            self.convertBST(node.right)
        self.nums += node.val
        node.val = self.nums
        
        if node.left is not None:
            self.convertBST(node.left)

    def convertBST1(self, node, nums):#不定义全局变量
        if node.right is not None:
            val = self.convertBST1(node.right, nums)
            node.val += val
        else:
            node.val += nums

        if node.left is not None:
            val = self.convertBST1(node.left, node.val)
            return val
        else:
            return node.val
