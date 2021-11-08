"""
       _                 
   ___| |__   ___  ___ ___            |\_
  / __| '_ \ / _ \/ __/ __|          /  .\_
 | (__| | | |  __/\__ \__ \         |   ___)
  \___|_| |_|\___||___/___/         |    \
                                    |  =  |
                                    /_____\
                                    [_______]
       8 /__////__////__////__////    
      7 ////__////__////__////__/                      
     6 /__////__////__////__////    
    5 ////__////__////__////__/    
   4 /__////__////__////__////   
  3 ////__////__////__////__/    
 2 /__////__////__////__////   
1 ////__////__////__////__/   
   a  b  c  d  e  f  g  h

Main driver / responsible for handling user input and dsiplaying current gamestate object
"""

import pygame as pygame
from ChessEngine import *
import ChessEngine

pygame.init()

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Global dictionary of images
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN','bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece  + ".png"), (SQ_SIZE, SQ_SIZE))



'''
Main driver
'''
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    game = GameState()
    print(game.board)
    validMoves = game.getValidMoves()
    moveMade = False # flag variable for when a move is made

    
    loadImages() # only do this once
    running = True
    squareSelected = () # keep track of last click of user (tuple: (row, col))
    playerClicks = [] # keep track of player clicks (two tuples : [(row 6, col 4), moves -> (row 4, col 4)])
    
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() # (x,y) location of mouse
                col = location [0] // SQ_SIZE
                row = location [1] // SQ_SIZE
                if squareSelected == (row, col): # the user clicked the same square twice
                    squareSelected = () # deselected
                    playerclicks = [] # clear player clicks
                else:
                    squareSelected = (row, col)
                    playerClicks.append(squareSelected) # append for both 1st and 2nd clicks
                if len(playerClicks) == 2: # after 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], game.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        game.makeMove(move)
                        moveMade = True
                    squareSelected = () # reset user clicks
                    playerClicks = []

        # key handler
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z: # undo when 'z' is pressed
                    game.undoMove()
                    moveMade = True


        if moveMade:
            validMoves = game.getValidMoves()
            moveMade = False
        drawGame(screen, game) 
        clock.tick(MAX_FPS)
        pygame.display.flip()

def drawGame(screen, game):
    drawBoard(screen) #draw squares on the board
    #add in pieces highlighting or move sugesstion (later)
    drawPieces(screen, game.board) #draw pieces on top of those squares


'''
Draw the squares on the board
'''

def drawBoard(screen):
    colors = [pygame.Color(238,238,210), pygame.Color(118,150,86)]
    for row in range(DIMENSION):
        for col in range(DIMENSION): 
            color = colors[ (row + col) % 2 ] 
            pygame.draw.rect(screen, color, pygame.Rect(col*SQ_SIZE,row*SQ_SIZE, SQ_SIZE, SQ_SIZE))



''' Draw pieces on the board using the current game \board'''

def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece  != "--": # not empty sqaure
                screen.blit(IMAGES[piece], pygame.Rect(col*SQ_SIZE,row*SQ_SIZE, SQ_SIZE,SQ_SIZE))


            


if __name__ == "__main__":
    main()



