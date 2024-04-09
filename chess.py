import pygame
pygame.init()

from vars import *

screen=pygame.display.set_mode((square_size*8,square_size*8))

from pieces import *

BLACK=(0,0,0)
WHITE = (255,255,255)

pieces = [pawn(0, square_size, screen, True), rook(0, 7*square_size, screen, False), rook(7*square_size, 0, screen, True), rook(0, 0, screen, True), rook(7*square_size, 7*square_size, screen, False), knight(1*square_size, 0, screen, True), knight(6*square_size, 0, screen, True), knight(1*square_size, 7*square_size, screen, False),knight(6*square_size, 7*square_size, screen, False) , bishop(2*square_size, 0, screen, True), bishop(5*square_size, 0, screen, True), bishop(2*square_size,7*square_size, screen, False), bishop(5*square_size, 7*square_size, screen, False), queen(4*square_size, 0, screen, True), queen(4*square_size, 7*square_size, screen, False), king(3*square_size, 0, screen, True), king(3*square_size, 7*square_size, screen, False)]

def drawBoard():
    screen.fill(WHITE)
    for i in range(8):
        if(i%2==1):
            for j in range(4):
                pygame.draw.rect(screen, BLACK, (j*2*square_size,i*square_size,square_size, square_size))
        else:
            for j in range(1,5):
                pygame.draw.rect(screen, BLACK, (j*2*square_size - square_size,i*square_size,square_size, square_size))

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    drawBoard()
    for i in range(len(pieces)):
        if None != pieces[i]:
            pieces[i].highlight()
            pieces[i].click(pieces)
            pieces[i].draw()
            if pieces[i].turn:
                for x in range(len(pieces)):
                    if (i != x) and pieces[x] != None:
                        if (pieces[i].rect.y == pieces[x].rect.y) and (pieces[i].rect.x == pieces[x].rect.x):
                            pieces[x] = None
                            pieces[i].turn = False

    for i in pieces:
        if i != None:
            i.turn = False

    pygame.display.update()
pygame.quit()