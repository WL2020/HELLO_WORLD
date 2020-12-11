class Solution:
    def __init__(self, board, word):
        self.board = board
        self.lenth = len(self.board[0])
        self.high = len(self.board)
        self.word = word
        self.long = len(self.word)
        self.start = []

        a = self.exist()
        print(a)

    def exist(self):
        self.start = self.serchStart()
        if len(self.start) == 0:
            return False
        if self.long == 1:
            return True
        else:
            for i in range(len(self.start)):
                new_board = [[0 for i in range(self.lenth)] for j in range(self.high)]
                flag = self.serch(self.start[i], new_board, 0)
                if flag == 0:
                    print(flag)
                    return True
            return False

    def serch(self, location, new_board, k):
        temp = [[new_board[j][i] for i in range(self.lenth)] for j in range(self.high)]
        temp[location[0]][location[1]] += 1
        print(temp)
        #print(location)
        if k+2 == self.long:
            for i in range(4):
                flag = self.estimate(i, location, temp, k+1)
                if flag == 0:
                    return 0
            return -1
        else:
            for i in range(4):
                flag = self.estimate(i, location, temp, k+1)
                if flag == 0:
                    if i == 0:
                        new_location = [location[0]-1,location[1]]
                    elif i == 1:
                        new_location = [location[0]+1,location[1]]
                    elif i == 2:
                        new_location = [location[0],location[1]-1]
                    elif i == 3:
                        new_location = [location[0],location[1]+1]
                    
                    flag = self.serch(new_location, temp, k+1)
                    if flag == 0:
                        return 0
    
    def estimate(self, direction, location, new_board, k):
        if direction == 0:#上
            if location[0] - 1 >= 0:
                if new_board[location[0] - 1][location[1]] == 0 and self.board[location[0] - 1][location[1]] == self.word[k]:
                    return 0
                else:
                    return -1
            else:
                return -1
        elif direction == 1:#下
            if location[0] + 1 < self.high:
                if new_board[location[0] + 1][location[1]] == 0 and self.board[location[0] + 1][location[1]] == self.word[k]:
                    return 0
                else:
                    return -1
            else:
                return -1
        elif direction == 2:#左
            if location[1] - 1 >= 0:
                if new_board[location[0]][location[1] - 1] == 0 and self.board[location[0]][location[1] - 1] == self.word[k]:
                    return 0
                else:
                    return -1
            else:
                return -1
        elif direction == 3:#右
            if location[1] + 1 < self.lenth:
                if new_board[location[0]][location[1] + 1] == 0 and self.board[location[0]][location[1] + 1] == self.word[k]:
                    return 0
                else:
                    return -1
            else:
                return -1
    
    def serchStart(self):
        for i in range(self.high):
            for j in range(self.lenth):
                if self.board[i][j] == self.word[0]:
                    self.start.append([i,j])
        print(self.start)
        return self.start
