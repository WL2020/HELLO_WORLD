class Solution:
    def __init__(self, candidates, target):
        self.candidates = candidates
        self.candidates.sort()
        self.lenth = len(self.candidates)
        self.target = target
        self.load = []
        self.combitionSum2([],0)
        print(self.load)

    def combitionSum2(self, arr, k):
        for i in range(k, self.lenth):
            temp = arr
            print(arr+ [self.candidates[i]])
            if (sum(temp) + self.candidates[i]) == self.target:
                if temp + [self.candidates[i]] not in self.load:
                    self.load.append(temp + [self.candidates[i]])
                    return -1
            elif (sum(temp) + self.candidates[i]) < self.target:
                flag = self.combitionSum2(temp + [self.candidates[i]], i+1)
            elif (sum(temp) + self.candidates[i]) > self.target:
                return -1
