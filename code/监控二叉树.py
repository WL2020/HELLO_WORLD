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

class Solution:#0：未监测 1：有相机 2：被监测
    def __init__(self, root):
        self.root = root
        self.count = 0
        if self.root is not None:
            root_a = self.minCameraCover(self.root)
            if root_a == 0:
                self.count += 1
        print(self.count)

    def minCameraCover(self, node):
        if node == None:
            return 2
        left = self.minCameraCover(node.left)
        right = self.minCameraCover(node.right)
        if left == 0 or right == 0:
            self.count += 1
            return 1
        if left == 1 or right == 1:
            return 2
        if left == 2 and right == 2:
            return 0


def dfs(root: TreeNode):#b 就是答案，计算3种状态：
    #1,有根节点相机的相机总数，2,最少相机总数，3,覆盖两颗子树相机总数
    if not root:
        return [float("inf"), 0, 0]#fooat('+ or - inf')表示无穷
    
    la, lb, lc = dfs(root.left)
    ra, rb, rc = dfs(root.right)
    a = lc + rc + 1
    b = min(a, la + rb, ra + lb)
    c = min(a, lb + rb)
    return [a, b, c]
