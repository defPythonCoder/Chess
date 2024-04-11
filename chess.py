import pygame
pygame.init()

from vars import *

screen=pygame.display.set_mode((square_size*8,square_size*8))

from pieces import *

BLACK=(0,0,0)
WHITE = (255,255,255)

pieces = [pawn(0, 1*square_size, screen, True),
          pawn(1*square_size, 1*square_size, screen, True),
          pawn(2*square_size, 1*square_size, screen, True),
          pawn(3*square_size, 1*square_size, screen, True),
          pawn(4*square_size, 1*square_size, screen, True),
          pawn(5*square_size, 1*square_size, screen, True),
          pawn(6*square_size, 1*square_size, screen, True),
          pawn(7*square_size, 1*square_size, screen, True),
          pawn(0, 6*square_size, screen, False),
          pawn(1*square_size, 6*square_size, screen, False),
          pawn(2*square_size, 6*square_size, screen, False),
          pawn(3*square_size, 6*square_size, screen, False),
          pawn(4*square_size, 6*square_size, screen, False),
          pawn(5*square_size, 6*square_size, screen, False),
          pawn(6*square_size, 6*square_size, screen, False),
          pawn(7*square_size, 6*square_size, screen, False),
          rook(0, 7*square_size, screen, False),
          rook(7*square_size, 0, screen, True),
          rook(0, 0, screen, True),
          rook(7*square_size, 7*square_size, screen, False),
          knight(1*square_size, 0, screen, True),
          knight(6*square_size, 0, screen, True),
          knight(1*square_size, 7*square_size, screen, False),
          knight(6*square_size, 7*square_size, screen, False) ,
          bishop(2*square_size, 0, screen, True),
          bishop(5*square_size, 0, screen, True),
          bishop(2*square_size,7*square_size, screen, False),
          bishop(5*square_size, 7*square_size, screen, False),
          queen(4*square_size, 0, screen, True),
          queen(4*square_size, 7*square_size, screen, False),
          king(3*square_size, 0, screen, True),
          king(3*square_size, 7*square_size, screen, False)]

def drawBoard():
    screen.fill(WHITE)
    for i in range(8):
        if(i%2==1):
            for j in range(4):
                pygame.draw.rect(screen, BLACK, (j*2*square_size,i*square_size,square_size, square_size))
        else:
            for j in range(1,5):
                pygame.draw.rect(screen, BLACK, (j*2*square_size - square_size,i*square_size,square_size, square_size))

white_turn = True
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    for index in range(len(pieces)):
        if pieces[index] != None:
            try:
                piece_name = (str(pieces[index]).strip('<').split()[0].split('.')[1])
            except IndexError:
                piece_name = None
            if piece_name == 'pawn':
                if (pieces[index].rect.y == square_size*7) or (pieces[index].rect.y == 0):
                    temp = pieces[index]
                    pieces[index] = queen(temp.rect.x, temp.rect.y, screen, temp.white)
            if piece_name == 'king':
                if pieces[index].check(pieces):
                    pieces[index].attack = True

    drawBoard()
    for i in range(len(pieces)):
        if None != pieces[i]:
            pieces[i].highlight()
            pieces[i].click(pieces, white_turn)
            if pieces[i].turn:
                white_turn = not white_turn
                for x in range(len(pieces)):
                    if (i != x) and pieces[x] != None:
                        if (pieces[i].rect.y == pieces[x].rect.y) and (pieces[i].rect.x == pieces[x].rect.x):
                            pieces[x] = None
                            pieces[i].turn = False
            pieces[i].draw()

    for i in range(len(pieces)):
        try:
            if pieces[i] != None:
                pieces[i].turn = False
                piece_name = (str(pieces[i]).strip('<').split()[0].split('.')[1])
                if piece_name == 'king':
                    pieces[i].attack = False
            if pieces[i] == None:
                del pieces[i]
        except IndexError:
            continue


    pygame.display.update()
pygame.quit()