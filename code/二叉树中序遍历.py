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
a.root

import time
def test():
	time1 = int(round(time.time()*1000))
	for i in range(200):
		Solution(a.root)
	time2 = int(round(time.time()*1000))
	print(time2 - time1)

	
class Solution:
    def __init__(self, root):
        self.root = root
        self.load = []
        #self.inorderTraversal(self.root)#1741 1891 2094 2085
        self.stack = []
        self.iterationTraversal(self.root)#1875 1958 2054
        print(self.load)

    def inorderTraversal(self, node):#递归中序遍历
        if node.left is not None:
            self.inorderTraversal(node.left)
        self.load.append(node.val)
        if node.right is not None:
            self.inorderTraversal(node.right)
            
    def iterationTraversal(self, root):#迭代中序遍历 左链入栈
        while(root != None or len(self.stack) != 0):
            while(root is not None):
                self.stack.append(root)
                root = root.left
            temp = self.stack.pop()
            self.load.append(temp.val)
            root = temp.right


