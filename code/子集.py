class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.lenth = len(self.nums)
        self.load = []
##        self.load.append([])
##        if len(self.nums) != 0:
##            self.subsets([],0,1)
        self.subsets1()
        print(self.load)

    def subsets(self, arr, m, k):#digui
        if k == 1:
            for i in range(self.lenth):
                self.load.append([self.nums[i]])
                self.subsets([self.nums[i]], i, k+1)
        else:
            for i in range(m+1,self.lenth):
                self.load.append(arr + [self.nums[i]])
                if i < self.lenth - 1:
                    self.subsets(arr+[self.nums[i]], i, k+1)
        
    def subsets1(self):#使用二进制位运算 00 01 10 11
        #bin(3) == '0b11' int('101',2)==5  '^'异或 '&' 'or' '<<'  '>>' '~'
        for i in range(2 ** self.lenth):
            temp = []
            num = bin(i)[2:]
            print(num)
            k = 0
            for j in range(len(num)-1,-1,-1):
                if num[j] == '1':
                    temp.append(self.nums[k])
                k += 1
            self.load.append(temp)
