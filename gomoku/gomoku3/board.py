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