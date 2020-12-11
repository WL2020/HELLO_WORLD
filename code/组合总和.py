class Solution:
    def __init__(self, candidates, target):
        self.candidates = candidates.sort()
        self.target = target
        self.load = []
        self.combitionSum([], 0)
        print(self.load)

    def combitionSum(self, arr, k):
        for i in range(k, len(self.candidates)):
            #print(arr)
            #print(i)
            temp = arr
            if (sum(temp) + self.candidates[i]) == self.target:
                self.load.append(temp + [self.candidates[i]])
                return 0
            elif (sum(temp) + self.candidates[i]) < self.target:
                self.combitionSum(temp + [self.candidates[i]], i)
            elif (sum(temp) + self.candidates[i]) > self.target:
                return -1
