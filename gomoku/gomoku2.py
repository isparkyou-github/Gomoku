import os

class Board:
    def __init__(self):
        self.board = [[0 for i in range(0, 9)] for j in range(0, 9)]

    def showBoard(self):
        os.system('cls')
        print('  1  2  3  4  5  6  7  8  9  ')
        for r in range(0, len(self.board)):
            data = str(r + 1)
            for c in range(0, len(self.board[r])):
                if self.board[r][c] == 0:
                    data += ' + '
                elif self.board[r][c] == 1:
                    data += ' @ '
                else:
                    data += ' $ '
            print(data)

    def isBlack(self, row, col):
        if self.board[row][col] == 0:
            return True
        return False

    def isWhite(self, row, col):
        if self.board[row][col] == 1:
            return True
        return False

    def isBlack(self, row, col):
        if self.board[row][col] == 2:
            return True
        return False

    def down(self, row, col, is_player):
        if is_player:
            self.board[row][col] = 2
        else:
            self.board[row][col] = 1

class GameLogic:
    def __init__(self):
        self.board = Board()
        self.player_row = 0
        self.player_col = 0
        self.cpu_row = 0
        self.cpu_col = 0

    def showBoard(self):
        self.board.showBoard()

    def isPlayerWin(self):
        count = 1
        for i in range(1, 5):
            if self.player_row + i < 9 and self.board.isBlack(self.player_row + i, self.player_col):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):
            if self.player_row + i > 0 and self.board.isBlack(self.player_row + i, self.player_col):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(1, 5):
            if self.player_col + i < 9 and self.board.isBlack(self.player_row, self.player_col + i):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):
            if self.player_col + i > 0 and self.board.isBlack(self.player_row, self.player_col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(-1, -5, -1):
            if self.player_row + i > 0 and self.player_col + i < 9 and self.board.isBlack(self.player_row + i, self.player_col + i):
                count += 1
            else:
                break
        for i in range(1, 5, ):
            if self.player_row + i < 9 and self.player_col + i > 0 and self.board.isBlack(self.player_row + i, self.player_col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(-1, -5, -1):
            if self.player_row + i > 0 and self.player_col + i > 0 and self.board.isBlack(self.player_row + i, self.player_col + i):
                count += 1
            else:
                break
        for i in range(1, 5, ):
            if self.player_row + i < 9 and self.player_col + i < 9 and self.board.isBlack(self.player_row + i, self.player_col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True
        return False

    def isCPUWin(self):
        count = 1
        for i in range(1, 5):
            if self.cpu_row + i < 9 and self.board.isBlack(self.cpu_row + i, self.cpu_col):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):
            if self.cpu_row + i > 0 and self.board.isBlack(self.cpu_row + i, self.cpu_col):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(1, 5):
            if self.cpu_col + i < 9 and self.board.isBlack(self.cpu_row, self.cpu_col + i):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):
            if self.cpu_col + i > 0 and self.board.isBlack(self.cpu_row, self.cpu_col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(-1, -5, -1):
            if self.cpu_row + i > 0 and self.cpu_col + i < 9 and self.board.isBlack(self.cpu_row + i, self.cpu_col + i):
                count += 1
            else:
                break
        for i in range(1, 5, ):
            if self.cpu_row + i < 9 and self.cpu_col + i > 0 and self.board.isBlack(self.cpu_row + i, self.cpu_col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(-1, -5, -1):
            if self.cpu_row + i > 0 and self.cpu_col + i > 0 and self.board.isBlack(self.cpu_row + i, self.cpu_col + i):
                count += 1
            else:
                break
        for i in range(1, 5, ):
            if self.cpu_row + i < 9 and self.cpu_col + i < 9 and self.board.isBlack(self.cpu_row + i, self.cpu_col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True
        return False

    def playerRound(self):
        self.player_input = input('你是黑子，请你输入行列来落子，例如：18 表示1行8列')
        self.player_row = int(self.player_input[0]) - 1
        self.player_col = int(self.player_input[1]) - 1
        self.board.down(self.player_row, self.player_col, True)

    def cpuRound(self):
        hengPos1 = -1
        hengPos2 = 1
        continueCount = 1
        maxContinueCount = 1
        finnalyRow = 0
        finnalyCol = 0
        while self.player_col + hengPos1 > 0 and self.board.isBlack(self.player_row, self.player_col + hengPos1):
            continueCount += 1
            hengPos1 -= 1
        while self.player_col + hengPos2 < 9 and self.board.isBlack(self.player_row, self.player_col + hengPos2):
            continueCount += 1
            hengPos2 += 1
        if continueCount >= maxContinueCount:
            if self.board.isBlank(self.player_row, self.player_col + hengPos1):
                maxContinueCount = continueCount
                finnalyRow = self.player_row
                finnalyCol = self.player_col + hengPos1
            elif self.board.isBlank(self.player_row, self.player_col + hengPos2):
                maxContinueCount = continueCount
                finnalyRow = self.player_row
                finnalyCol = self.player_col + hengPos2

        shuPos1 = -1
        shuPos2 = 1
        continueCount = 1
        while self.player_row + shuPos1 > 0 and self.board.isBlack(self.player_row + shuPos1, self.player_col):
            continueCount += 1
            shuPos1 -= 1
        while self.player_row + shuPos2 < 9 and self.board.isBlack(self.player_row + shuPos2, self.player_col):
            continueCount += 1
            shuPos2 += 1
        if continueCount >= maxContinueCount:
            if self.board.isBlank(self.player_row + shuPos1, self.player_col):
                maxContinueCount = continueCount
                finnalyRow = self.player_row + shuPos1
                finnalyCol = self.player_col
            elif self.board.isBlank(self.player_row + shuPos2, self.player_col):
                maxContinueCount = continueCount
                finnalyRow = self.player_row + shuPos2
                finnalyCol = self.player_col

        zuoShangRow = -1
        zuoShangCol = -1
        youXiaRow = 1
        youXiaCol = 1
        continueCount = 1
        while (self.player_row + zuoShangRow > 0 and self.player_col + zuoShangCol > 0
               and self.board.isBlack(self.player_row + zuoShangRow, self.player_col + zuoShangCol)):
            continueCount += 1
            zuoShangRow -= 1
            zuoShangCol -= 1
        while (self.player_row + youXiaRow < 9 and self.player_col + youXiaCol < 9
               and self.board.isBlack(self.player_row + youXiaRow, self.player_col + youXiaCol)):
            continueCount += 1
            youXiaRow += 1
            youXiaCol += 1
        if continueCount >= maxContinueCount:
            if self.board.isBlank(self.player_row + zuoShangRow, self.player_col + zuoShangCol):
                maxContinueCount = continueCount
                finnalyRow = self.player_row + zuoShangRow
                finnalyCol = self.player_col + zuoShangCol
            elif self.board.isBlank(self.player_row + youXiaRow, self.player_col + youXiaCol):
                maxContinueCount = continueCount
                finnalyRow = self.player_row + youXiaRow
                finnalyCol = self.player_col + youXiaCol

        zuoXiaRow = 1
        zuoXiaCol = -1
        youShangRow = -1
        youShangCol = 1
        continueCount = 1
        while (self.player_row + zuoXiaRow < 9 and self.player_col + zuoXiaCol > 0
               and self.board.isBlack(self.player_row + zuoXiaRow, self.player_col + zuoXiaCol)):
            continueCount += 1
            zuoXiaRow += 1
            zuoXiaCol -= 1
        while (self.player_row + youShangRow > 0 and self.player_col + youShangCol < 9
               and self.board.isBlack(self.player_row + youShangRow, self.player_col + youShangCol)):
            continueCount += 1
            youShangRow -= 1
            youShangCol += 1
        if continueCount >= maxContinueCount:
            if self.board.isBlank(self.player_row + zuoXiaRow, self.player_col + zuoXiaCol):
                maxContinueCount = continueCount
                finnalyRow = self.player_row + zuoXiaRow
                finnalyCol = self.player_col + zuoXiaCol
            elif self.board.isBlank(self.player_row + youShangRow, self.player_col + youShangCol):
                maxContinueCount = continueCount
                finnalyRow = self.player_row + youShangRow
                finnalyCol = self.player_col + youShangCol

        self.board.down(finnalyRow, finnalyCol, False)

game = GameLogic()
while True:
    game.showBoard()
    game.playerRound()
    if game.isPlayerWin():
        print('Player won!')
        break
    game.cpuRound()
    if game.isCPUWin():
        print('CPU won!')
        break