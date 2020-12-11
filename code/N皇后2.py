class Solution(object):
    def __init__(self, n):
        self.n = n
        self.load = []
        self.solveNQuenns()
        
    def solveNQuenns(self):
        self.chest = self.creat_chest()
        self.cycle(0,0)
        print(len(self.load))
        
    def creat_chest(self):
        a = [[0 for i in range(self.n)]for i in range(self.n)]
        return a

    def serch_location(self, line, num):
        for i in range(num, self.n):
            if self.chest[line][i] == 0:
                return i
        return -1

    def cycle(self, line, num):
        #print(self.chest)
        location = self.serch_location(line, num)
        if location == -1:
            return -1
        else:
            self.add_location(line, location)

        if (line+1) == self.n:
            self.load.append(self.chest)
            self.delete_location(line, location)
            return -1
        else:
            self.cycle(line+1, 0)

        self.delete_location(line, location)
        flag = self.cycle(line, location + 1)
        if flag == -1:
            return -1

    def add_location(self, line, location):
        i = 0
        while(line+i < self.n):
            self.chest[line+i][location] += 1
            if i!=0 and (location - i)>=0:
                self.chest[line+i][location - i] += 1
            if i!=0 and (location + i)< self.n:
                self.chest[line+i][location + i] += 1
            i += 1
            
    def delete_location(self, line, location):
        i = 0
        while(line + i < self.n):
            self.chest[line+i][location] -= 1
            if i!=0 and (location - i)>=0:
                self.chest[line+i][location - i] -= 1
            if i!=0 and (location + i)< self.n:
                self.chest[line+i][location + i] -=1
            i+=1
