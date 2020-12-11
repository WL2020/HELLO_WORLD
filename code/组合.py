class Solution:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.arr= [i for i in range(1,n+1)]
        self.combition(n, k)

    def combition(self, n, k):
        if k >1:
            temp = self.combition(n,k-1)
        else:
            temp = [[i] for i in range(1,n+1)]
            print(temp)
            return temp

        new_temp = []
        for i in range(len(temp),0,-1):
            if temp[i-1][k-2] == self.n:
                temp.pop(i-1)
                
        for i in range(len(temp)):
            for j in range(temp[i-1][k-2], self.n):
                new_temp.append(temp[i-1] + [self.arr[j]])

        print(new_temp)
        print(len(new_temp))
        return new_temp
