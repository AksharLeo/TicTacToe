import tictactoe as ttt

def gameReset():
    global player
    global turn
    global board
    ttt.clear()
    player = '*'
    turn = 'X'
    board = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']


def currentPlayer():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player


def ticTacToe():
    global player
    global turn
    global board
    while ttt.gameRunning(board):
        ttt.printBoard(board)
        while True:
            try:
                box = int(input(f'{turn} select a box between 1-9: '))
                if ttt.boxIsValid(box) : break
            except(TypeError, ValueError):
                continue
            
        if board[box - 1] == '-':
            board[box - 1] = currentPlayer()
            turn = 'X' if turn == 'O' else 'O'
            ttt.clear()
        else:
            print(f'{box} is already Occupied, choose a different box\n')
            continue

    ttt.clear()
    ttt.printBoard(board)

    if ttt.gameTie(board):
        print('Its a tie')
    elif ttt.gameWon(board):
        print(f'{player}  Won')


def playAgain():
    play_again = input("do you want to play again? (y/N): ")
    if play_again.lower() == 'y':
        gameReset()
        ticTacToe()
        playAgain()


player = '*'
turn = 'X'
board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
if __name__ == "__main__": 
    ticTacToe()
    playAgain()

