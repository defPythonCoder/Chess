#Pygame
import pygame
pygame.init()

#imports
from newpices import *
import colors

#Constants
SQUARE_SIZE = 80
SQUARE_NUMBER = 8

#Colors
LIGHT_SQUARE = colors.WHITE
DARK_DARKSQUARE = colors.BLACK

#Variables

#Setup
window = pygame.display.set_mode((SQUARE_SIZE*SQUARE_NUMBER, SQUARE_SIZE*SQUARE_NUMBER))
pygame.display.set_caption("Chess - Python Coder")

#Functions
def drawBoard():
    window.fill(LIGHT_SQUARE)
    for x in range(SQUARE_NUMBER):
        for y in range(SQUARE_NUMBER):
            if (x%2 == 0) and (y%2 == 1):
                pygame.draw.rect(window, DARK_DARKSQUARE, (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            elif (x%2 == 1) and (y%2 == 0):
                pygame.draw.rect(window, DARK_DARKSQUARE, (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


#Main Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawBoard()
    pygame.display.update()
    
#Exit
pygame.quit()