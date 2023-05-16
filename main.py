import tictactoe as ttt 
import multiplayer
import singleplayer

mode = input('Multiplayer (M) or Singleplayer (S): ')


def gameMode(mode):    
    if mode.lower() == 'm':
        player = multiplayer.player
        turn = multiplayer.turn
        board = multiplayer.board
        
        multiplayer.ticTacToe()
        multiplayer.playAgain()

    elif mode.lower() == 's':        
        player = singleplayer.player
        turn = singleplayer.turn
        board = singleplayer.board
        
        singleplayer.playAgain()
        
        
    else:
        while mode.lower() not in ['m', 's']:
            mode = input('Multiplayer / Singleplayer (M / S): ')
        gameMode(mode)

gameMode(mode)
