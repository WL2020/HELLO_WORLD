class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
class Solution:#分割思想,传递数组，耗时128ms，内存85MB
    def __init__(self, inorder, postorder):
        self.inorder = inorder
        self.postorder = postorder
        self.root = None
        if self.inorder != []:
            self.buildTree(self.inorder, self.postorder, None)
        print(self.root)
        
    def buildTree(self, inarr, postarr, node):
        if node is None:
            self.root = TreeNode(postarr[len(postarr) - 1])
            self.buildTree(inarr, postarr, self.root)
        else:
            left = inarr.index(postarr[len(postarr) - 1])
            right = len(inarr) - left -1
            if left != 0:
                node.left = TreeNode(postarr[left -1])
                self.buildTree(inarr[:left],postarr[:left],node.left)
            if right != 0:
                node.right = TreeNode(postarr[left+right-1])
                self.buildTree(inarr[left+1:],postarr[left:left+right],node.right)
'''
a = [3,9,20,15,7]
b = [9, 3, 15,20,7]
c = [9, 15,7,20, 3]
class Solution:#传递下标，耗时56ms，内存17.7MB,传递的东西要尽量少
    def __init__(self, inorder, postorder):
        self.inorder = inorder
        self.postorder = postorder
        self.root = None
        if self.inorder != []:
            self.buildTree([0,len(self.inorder)-1], [0,len(self.inorder)-1], None)
        print(self.root)
        
    def buildTree(self, inarr, postarr, node):
        if node is None:
            self.root = TreeNode(self.postorder[postarr[1]])
            self.buildTree(inarr, postarr, self.root)
        else:
            temp = self.inorder.index(self.postorder[postarr[1]])
            postleft = [postarr[0], postarr[0] + temp - inarr[0] -1 ]
            postright = [postleft[1]+1, postarr[1]-1]
            inleft = [inarr[0],temp - 1]
            inright = [temp+1,inarr[1]]
            if inleft[0]-inleft[1] <= 0:
                node.left = TreeNode(self.postorder[postleft[1]])
                self.buildTree(inleft, postleft, node.left)
            if inright[0] - inright[1] <= 0:
                node.right = TreeNode(self.postorder[postright[1]])
                self.buildTree(inright, postright, node.right)
