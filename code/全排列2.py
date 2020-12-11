class Solution:
    def __init__(self, nums):
        self.nums = nums
        #self.nums.sort()
        self.load = []
        self.permuteUnique()
        print(self.load)

    def permuteUnique(self):
        #先求种类 求个数
        kind,count = self.category()
        self.cycle(kind,count,[])

    def cycle(self,kind,count,arr):
        if len(count) != 0:
            for i in range(len(kind)):
                if count[i] -1 != 0:
                    self.cycle(kind,count[:i]+[count[i]-1]+count[i+1:],arr+[kind[i]])
                else:
                    self.cycle(kind[:i]+kind[i+1:],count[:i]+count[i+1:],arr+[kind[i]])
        else:
            self.load.append(arr)
    
    def category(self):
        count = []
        kind = []
        for i in range(len(self.nums)):
            if self.nums[i] not in kind:
                kind.append(self.nums[i])
                count.append(1)
            else:
                count[kind.index(self.nums[i])] += 1
        return kind,count
