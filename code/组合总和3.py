class Solution:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.arr = [i for i in range(1,10)]
        self.load = []
        self.combitionSum3([],0)
        print(self.load)

    def combitionSum3(self, arr1, location):
        if len(arr1) == self.k:
            return -1
        for i in range(location, 9):
            if sum(arr1) + self.arr[i] == self.n:
                if len(arr1) == self.k -1:
                    self.load.append(arr1 + [self.arr[i]])
                return 0
            elif sum(arr1) + self.arr[i] < self.n:
                self.combitionSum3(arr1 + [self.arr[i]], i+1)
            elif sum(arr1) + self.arr[i] > self.n:
                return -1
