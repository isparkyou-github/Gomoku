from gamelogic import GameLogic

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