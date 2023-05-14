import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def printBoard(board):
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')
    print('-----------------------')


def gameWonHorizontal(board):
    if board[0] == board[1] == board[2] and board[0] != '-':
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        return True
    if board[6] == board[7] == board[8] and board[6] != '-':
        return True


def gameWonVertical(board):
    if board[0] == board[3] == board[6] and board[0] != '-':
        return True
    if board[1] == board[4] == board[7] and board[1] != '-':
        return True
    if board[2] == board[5] == board[8] and board[2] != '-':
        return True


def gameWonDiagonal(board):
    if board[0] == board[4] == board[8] and board[0] != '-':
        return True
    if board[6] == board[4] == board[2] and board[6] != '-':
        return True


def gameWon(board):
    if gameWonDiagonal(board) or gameWonHorizontal(board) or gameWonVertical(board):
        return True
    else:
        return False


def gameTie(board):
    if not gameWon(board):
        if '-' not in board:
            return True
        else:
            return False

def gameRunning(board):
    if not (gameWon(board) or gameTie(board)):
        return True
    else:
        return False


def currentPlayer():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player


def gameReset():
    global player
    global turn
    global board
    clear()
    player = '*'
    turn = 'X'
    board = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']

def boxIsValid(box):
    if (box >= 1 and box <= 9):
        return True
    else:
        return False


def ticTacToe():
    global player
    global turn
    global board
    while gameRunning(board):
        printBoard(board)
        x = True
        while x:
            try:
                box = int(input(f'{turn} select a box between 1-9: '))
                if boxIsValid(box) : x = False; break
            except(TypeError, ValueError):
                continue
            
        if board[box - 1] == '-':
            board[box - 1] = currentPlayer()
            turn = 'X' if turn == 'O' else 'O'
            clear()
        else:
            print(f'{box} is already Occupied, choose a different box\n')
            continue

    clear()
    printBoard(board)

    if gameTie(board):
        print('Its a tie')
    elif gameWon(board):
        print(f'{player}  Won')


def playAgain():
    play_again = input("do you want to play again? (y/N): ")
    if play_again.lower() == 'y':
        gameReset()
        ticTacToe()
        playAgain()


player = 'P'
turn = 'X'
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

ticTacToe()
playAgain()
