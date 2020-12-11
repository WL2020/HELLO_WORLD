class Solution:
    def __init__(self, root):
        self.root = root
        if self.root:
            self.stack = [self.root]
            self.connect(self.stack)
        self.root
'''
    def connect1(self, arr):
        lenth = len(arr)
        for i in range(lenth):
            temp = arr.pop(0)
            if i != lenth-1:
                temp.next = arr[0]
            if temp.left is not None:
                arr.append(temp.left)
            if temp.right is not None:
                arr.append(temp.right)
        if len(arr):
            self.connect1(arr)
'''
'''
    def connect(self, node):#O(1)空间复杂度
        next_node = None
        temp = None
        while node:
            if node.left is not None:
                if temp:
                    temp.next = node.left
                    temp = node.left
                else:
                    temp = node.left
                    next_node = node.left
            if node.right is not None:
                if temp:
                    temp.next = node.right
                    temp = node.right
                else:
                    temp = node.right
                    next_node = node.right
            node = node.next
        if next_node:
            self.connect(next_node)
'''
    def connect(self, stack):#迭代
        while stack:
            node = self.stack.pop()
            next_node = None
            temp = None
            while node:
                if node.left is not None:
                    if temp:
                        temp.next = node.left
                        temp = node.left
                    else:
                        temp = node.left
                        next_node = node.left
                if node.right is not None:
                    if temp:
                        temp.next = node.right
                        temp = node.right
                    else:
                        temp = node.right
                        next_node = node.right
                node = node.next
            if next_node is not None:
                self.stack.append(next_node)
        
         
        
