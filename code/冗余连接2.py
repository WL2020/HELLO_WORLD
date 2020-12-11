class Solution:
    def __init__(self, edges):
        self.edges = edges
        self.ring = []
        self.load = []
        self.findRedundantDirectedConnection()
        print(self.load)
    def findRedundantDirectedConnection(self):
        # 找到 环
        self.findCircle([1], -1)
        #  找到两个父亲的node,还是单环
        gussroot = self.findTwoinput()
        if gussroot == []: #都只有一个输入，环中任意两个相邻点都是答案
            self.ring.append(self.ring[0])
            for i in range(len(self.ring)-1):
                self.load.append([self.ring[i],self.ring[i+1]])
        else:#有两个输入的节点， 判断有没有外输入点
            if gussroot[1][0] not in self.ring or gussroot[1][1] not in self.ring:
                if gussroot[1][0] not in self.ring:
                    self.load.append([gussroot[1][1], gussroot[0]])
                else:
                    self.load.append([gussroot[1][0], gussroot[0]])
            else:#没有外接入点 ，谁便断掉一个
                self.load.append([gussroot[1][0],gussroot[0]])
                self.load.append([gussroot[1][1],gussroot[0]])

    def findTwoinput(self):
        temp = [[] for i in range(len(self.ring))]
        for i in range(len(self.edges)):
            for j in range(len(self.ring)):
                if self.edges[i][1] == self.ring[j]:
                    temp[j].append(self.edges[i][0])
        for i in range(len(temp)):
            if len(temp[i]) == 2:
                return [self.ring[i]] + [temp[i]]
        return []
    
    def findCircle(self, arr, last):#调用的时候传入 ([1], -1)
        temp = []
        for i in range(len(self.edges)):
            if self.edges[i][0] == arr[len(arr)-1]:
                if self.edges[i][1] != last:
                    temp.append(self.edges[i][1])
            if self.edges[i][1] == arr[len(arr)-1]:
                if self.edges[i][0] != last:
                    temp.append(self.edges[i][0])
        if len(temp) == 0:
            return -1
        for i in range(len(temp)):
            a = self.judgeCircle( arr + [temp[i]])
            if a == []:
                flag = self.findCircle(arr + [temp[i]], arr[len(arr)-1])
                if flag == 0:
                    return 0
            else:
                arr.append(temp[i])
                self.ring = [arr[i] for i in range(a[0], a[1])]
                return 0

    def judgeCircle(self, arr):
        for i in range(len(arr)):
            if arr.count(arr[i]) > 1:
                a = arr.index(arr[i])
                b = arr[a+1:].index(arr[i])
                return [a, a+1+b]
        return []
