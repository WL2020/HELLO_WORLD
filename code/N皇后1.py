class Solution(object):
    def __init__(self, n):
        self.n = n
        self.solveNQuenns()
        
    def solveNQuenns(self):
        self.chest = self.creat_chest()
        load = []
        for i in range(self.n):
            self.chest[i][0] = 1
        #print(self.chest)
        while(1):
            flag0 = self.check(self.chest)
            if(flag0 == 1):
                load.append(self.chest)
                #print(self.chest)
            flag1 = self.move(self.chest, self.n-1)
            #print(self.chest)
            if flag1 == 1:
                break
        #print(load)
        print(len(load))
        
    def creat_chest(self):
        a = [[0 for i in range(self.n)]for i in range(self.n)]
        return a

    def move(self, chest, num):
        j = 0
        for i in range(self.n):
            if chest[num][i] == 1:
                j = i;
        self.chest[num][j] = 0
        self.chest[num][(j+1)%self.n] = 1
        if j == (self.n - 1):
            if num == 0:
                return 1
            else:
                flag = self.move(self.chest, num-1)
                if flag == 1:
                    return 1
                else:
                    return 0
        else:
            return 0

    def check(self, chest):
        load = []
        for i in range(self.n):
            for j in range(self.n):
                if chest[i][j] == 1:
                    load.append([i,j])
                    continue
        for i in range(self.n):
            for j in range(i+1,self.n):
                if load[i][1] == load[j][1]:
                    return 0
                if (load[i][0] - min(load[i])) == (load[j][0] - min(load[j])) and (load[i][1] - min(load[i])) == (load[j][1] - min(load[j])):
                    return 0
                if load[i][0] + load[i][1] == load[j][0] + load[j][1]:
                    return 0
        return 1

