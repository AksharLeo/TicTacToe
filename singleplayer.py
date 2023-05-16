import random
import tictactoe as ttt

def easyBotTurn(board):
    global bot
    moves = botValidMoves(board)
    board[random.choice(moves)] = bot
    moves.clear()
    endMove()
    ttt.clear()
    
    
def gameEnd():
    if ttt.gameTie(board):
        ttt.printBoard(board)
        print('Its a tie')
    elif ttt.gameWon(board):
        endMove()
        ttt.printBoard(board)
        print(f'{turn}  Won')
    
    play_again = input('would you like to play again (y/N): ')
    if play_again == 'y':
        playAgain()


def easyMode(board):
    while ttt.gameRunning(board):       
        if turn == player:
            playerTurn(board)
        else:
            easyBotTurn(board)
    gameEnd()


def gameDifficulty():
    global difficulty
    
    while True:
        try:
            difficulty = input('difficulty - Easy / Medium / Hard (E / M / H): ')
            if difficulty.lower() in ['e', 'm', 'h']: break
        except:
            continue
    return difficulty.lower()


def playerPreferences():
    global player
    global bot
    global turn
    global difficulty
    difficulty = gameDifficulty()
    
    while player.capitalize() not in ['X', 'O']:
        player = input('would you like to play as X or O: ')
    bot = 'O' if player.capitalize() == 'X' else 'X'
    
    while True:
        try:
            player_turn = int(input('would you like to go first or second (1 / 2): '))
            if player_turn in [1,2] : break
        except(TypeError,ValueError):
            continue
    
    
    if player_turn == 1:
        turn = player
    else:
        turn = bot
    ttt.clear()

    if difficulty == 'e':
        easyMode(board)
    elif difficulty == 'm':
        mediumMode(board)
    elif difficulty == 'h':
        hardMode(board)


def endMove():
    global player
    global bot
    global turn
    
    if turn == player:
        turn = bot
    else:
        turn = player


def botValidMoves(board):
    moves = []
    for i in range(9):
        if board[i] == '-':
            moves.append(i)
    return moves


def playerTurn(board):
    global player
    ttt.printBoard(board)
    while True:
        try:
            box = int(input(f'{player} select a box between 1-9: '))
            if ttt.boxIsValid(box) : break
        except(TypeError, ValueError):
            continue
    
    if board[box-1] == '-':
        board[box-1] = player
        endMove()
    else:    
        print(f'{box} is already Occupied, choose a different box\n')
        playerTurn(board)
    ttt.clear()


def gameReset():
    global player
    global bot
    global turn
    global board
    player = '_'
    turn = '_'
    bot = '_'
    board = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']


def playAgain():
    gameReset()
    playerPreferences()


player = '_'
turn = '_'
bot = '_'
board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
difficulty = '_'

if __name__ =="__main__":    
    playAgain()
    
    