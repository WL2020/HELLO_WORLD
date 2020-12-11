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
'''
class Solution:#28ms 18.4MB
    def __init__(self, root, nums):
        self.root = root
        self.nums = nums
        self.load = []
        if self.root is not None:
            self.pathSum(self.root,[])

    def pathSum(self,node,arr):
        if node.left is None and node.right is None:
            if sum(arr)+node.val == self.nums:
                self.load.append(arr+[node.val])
            return
        if node.left is not None:
            self.pathSum(node.left, arr+[node.val])
        if node.right is not None:
            self.pathSum(node.right, arr+[node.val])
'''
class Solution:#28ms 14.6MB
    def __init__(self, root, nums):
        self.root = root
        self.nums = nums
        self.load = []
        if self.root is not None:
            stack = [[self.root,[self.root.val]]]
        while stack:
            temp = stack.pop()
            #print(temp)
            if temp[0].left is None and temp[0].right is None:
                if sum(temp[1]) == self.nums:
                    self.load.append(temp[1])
            if temp[0].left is not None:
                stack.append([temp[0].left, temp[1]+ [temp[0].left.val] ])
            if temp[0].right is not None:
                stack.append([temp[0].right, temp[1]+ [temp[0].right.val] ])
        print(self.load)
