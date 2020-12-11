class Solution:
    def __init__(self, board):
        self.board = board
        self.load = []
        self.solveSudoku()
        print(self.load)

    def solveSudoku(self):
        location = self.start()
        if location == False:
            return 0
        self.cycle(location)
        
    def cycle(self, location):
        #print(location)
        num = self.serch(location)
        #print(temp + ['location:'] + location)
        for i in range(len(num)):
            self.board[location[0]][location[1]] = num[i]
            #print(board)
            new_location = self.move(location)
            if len(new_location) != 0:
                self.cycle(new_location)
            else:
                self.end()
        self.board[location[0]][location[1]] = -1

    def end(self):
        for i in range(8,-1,-1):
            for j in range(8,-1,-1):
                if self.board[i][j] == -1:
                    return False
        #此处必须深拷贝才能load.append()
        board = [[self.board[i][j] for j in range(9)]for i in range(9)]
        self.load.append(board)
        return True
            
    def move(self, location):
        x = 0
        y = 0
        if location[1] == 8 and location[0] == 8:
            return []
        if location[1] == 8 and location[0] < 8:
            x = location[0] + 1
            y = 0
        else:
            x = location[0]
            y = location[1] + 1
        #print(location)
        for i in range(x,9):
            if i == x:
                for j in range(y,9):
                    if self.board[i][j] == -1:
                        return [i,j]
            else:
                for j in range(9):
                    if self.board[i][j] == -1:
                        return [i,j]
        return []
        
    def serch(self, location):
        #从 行，列，3x3中筛选
        temp = [0 for i in range(9)]
        val = []
        for i in range(9):
            if self.board[location[0]][i] is not -1:
                temp[self.board[location[0]][i] - 1] = 1

        for i in range(9):
            if self.board[i][location[1]] is not -1:
                temp[self.board[i][location[1]] - 1] = 1

        for i in range((location[0] // 3)*3,(location[0] // 3)*3 + 3):
            for j in range((location[1] // 3)*3,(location[1] // 3)*3 + 3):
                if self.board[i][j] is not -1:
                    temp[self.board[i][j] - 1] = 1

        for i in range(9):
            if temp[i] == 0:
                val.append(i+1)
        return val
    
    def start(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == -1:
                    return [i,j]
        return False#不考虑输入完全体

board = [[5,3,-1,-1,7,-1,-1,-1,-1],
         [6,-1,-1,1,9,5,-1,-1,-1],
	 [-1,9,8,-1,-1,-1,-1,6,-1],
	 [8,-1,-1,-1,6,-1,-1,-1,3],
	 [4,-1,-1,8,-1,3,-1,-1,1],
	 [7,-1,-1,-1,2,-1,-1,-1,6],
	 [-1,6,-1,-1,-1,-1,2,8,-1],
	 [-1,-1,-1,4,1,9,-1,-1,5],
	 [-1,-1,-1,-1,8,-1,-1,7,9]]
answer = [[5,3,4,6,7,8,9,1,2],
          [6,7,2,1,9,5,3,4,8],
	  [1,9,8,3,4,2,5,6,7],
	  [8,5,9,7,6,1,4,2,3],
	  [4,2,6,8,5,3,7,9,1],
	  [7,1,3,9,2,4,8,5,6],
	  [9,6,1,5,3,7,2,8,4],
	  [2,8,7,4,1,9,6,3,5],
	  [3,4,5,2,8,6,1,7,9]]
