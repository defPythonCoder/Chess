import pygame
pygame.init()

from utils import *
from vars import *

class base():
    def __init__(self, x, y, surface, white):
        self.win = surface
        if white:
            self.white = True
        else:
            self.white = False
        self.rect = pygame.Rect(x, y, square_size, square_size)
        self.dragx, self.dragy  = x, y
        self.selected = False
        self.move = False
        self.turn = False
        self.image()

    def image(self):
        pass
    def restrict(self, x, y, pieces_list):
        pass
    def rules(self,x,y, pieces_list):
        pass   
    def highlight(self):
        if self.selected:
            pygame.draw.rect(self.win, (0, 255, 0), (self.dragx, self.dragy, square_size, square_size))

    def draw(self):
        self.win.blit(self.img, self.rect)

    def click(self, pieces_list):
        if pygame.mouse.get_pressed()[0] and pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos()) and not self.selected and not self.move:
            self.selected = True
            self.dragx, self.dragy = self.rect.x, self.rect.y

        if self.selected and not self.move:
            if pygame.mouse.get_pressed()[0] and not (pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos())):
                mousex, mousey = get_coords(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                if self.rules(mousex, mousey, pieces_list) and self.restrict(mousex, mousey, pieces_list):
                    self.rect.x, self.rect.y = mousex, mousey
                    self.move = True
                    self.turn = True

        if self.move and self.selected:
            if not pygame.mouse.get_pressed()[0]:# and not pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos()):
                self.move = False
                self.selected = False

        if pygame.mouse.get_pressed()[0]:
            if self.selected and not self.move and not (pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos())):
                self.selected = False

class rook(base):
    def image(self):
        if self.white:
            self.img = pygame.transform.scale(pygame.image.load("images/w-rook.png"), (square_size, square_size))
        else:
            self.img = pygame.transform.scale(pygame.image.load("images/b-rook.png"), (square_size, square_size))
            self.white = False

    def restrict(self, x, y, pieces_list):
        for piece in pieces_list:
            if piece != None:
                if x == piece.rect.x:
                    if self.rect.y > piece.rect.y:
                        if y<piece.rect.y:
                            return False
                    elif self.rect.y < piece.rect.y:
                        if y>piece.rect.y:
                            return False
                elif y == piece.rect.y:
                    if self.rect.x > piece.rect.x:
                        if x<piece.rect.x:
                            return False
                    elif self.rect.x < piece.rect.x:
                        if x>piece.rect.x:
                            return False
        return True

    def rules(self,x,y, pieces_list):
        if (((x==self.rect.x) or (y==self.rect.y)) and not((x==self.rect.x) and (y==self.rect.y))):
            for i in pieces_list:
                if i != None:
                    if (i.rect.x == x) and (i.rect.y == y):
                        if i.white == self.white:
                            return False 
            return True
        return False

class bishop(base):
    def image(self):
        if self.white:
            self.img = pygame.transform.scale(pygame.image.load("images/w-bishop.png"), (square_size, square_size))
        else:
            self.img = pygame.transform.scale(pygame.image.load("images/b-bishop.png"), (square_size, square_size))
            self.white = False

    def restrict(self, x, y, pieces_list):
        ydiff = 1 if self.rect.y < y else -1
        xdiff = 1 if self.rect.x < x else -1
        for i in range(square_size, (abs(x - self.rect.x)), square_size):
            for piece in pieces_list:
                if piece != None:
                    if (piece.rect.y == (self.rect.y + (i*ydiff))) and (piece.rect.x == (self.rect.x + (i*xdiff))):
                        return False
        return True


    def rules(self,x,y, pieces_list):
        if abs(self.rect.x - x) == abs(self.rect.y - y):
            for i in pieces_list:
                if i != None:
                    if (i.rect.x == x) and (i.rect.y == y):
                        if i.white == self.white:
                            return False 
            return True
        return False
    
class knight(base):
    def image(self):
        if self.white:
            self.img = pygame.transform.scale(pygame.image.load("images/w-knight.png"), (square_size, square_size))
        else:
            self.img = pygame.transform.scale(pygame.image.load("images/b-knight.png"), (square_size, square_size))
            self.white = False

    def restrict(self, x, y, pieces_list):
        return True
    
    def rules(self, x, y, pieces_list):
        if ((abs(self.rect.x-x)<=2*square_size and abs(self.rect.y-y)<=2*square_size and (abs(self.rect.x-x)+abs(self.rect.y-y))==3*square_size) and not((x==self.rect.x) and (y==self.rect.y))):
            for i in pieces_list:
                if i != None:
                    if (i.rect.x == x) and (i.rect.y == y):
                        if i.white == self.white:
                            return False 
            return True
        return False
    
class queen(base):
    def image(self):
        if self.white:
            self.img = pygame.transform.scale(pygame.image.load("images/w-queen.png"), (square_size, square_size))
        else:
            self.img = pygame.transform.scale(pygame.image.load("images/b-queen.png"), (square_size, square_size))
            self.white = False

    def restrict(self, x, y, pieces_list):
        rookrestrict, bishoprestrict = rook(self.rect.x, self.rect.y, self.win, self.white), bishop(self.rect.x, self.rect.y, self.win, self.white)
        return rookrestrict.restrict(x, y, pieces_list) and bishoprestrict.restrict(x, y, pieces_list)

    def rules(self,x,y, pieces_list):
        rookRules, bishoprules = rook(self.rect.x, self.rect.y, self.win, self.white), bishop(self.rect.x, self.rect.y, self.win, self.white)
        if rookRules.rules(x, y, pieces_list) or bishoprules.rules(x, y, pieces_list):
            for i in pieces_list:
                if i != None:
                    if (i.rect.x == x) and (i.rect.y == y):
                        if i.white == self.white:
                            return False 
            return True
        return False

class king(base):
    def image(self):
        if self.white:
            self.img = pygame.transform.scale(pygame.image.load("images/w-king.png"), (square_size, square_size))
        else:
            self.img = pygame.transform.scale(pygame.image.load("images/b-king.png"), (square_size, square_size))
            self.white = False

    def restrict(self, x, y, pieces_list):
        for index, piece in enumerate(pieces_list):
            try:
                piece_name = (str(piece).strip('<').split()[0].split('.')[1])
            except IndexError:
                piece_name = None
            if piece != None and piece_name != None:
                if piece.white != self.white:
                    if piece_name == 'king':
                        if piece.rules(x,y,pieces_list):
                            return False
                    if piece.rules(x,y,pieces_list) and piece.restrict(x,y,pieces_list):
                        print("False for ", piece)
                        return False
            if piece != None:
                if x == piece.rect.x and y == piece.rect.y:
                    withoutPiece = pieces_list[:index] + pieces_list[index+1:]
                    for other_piece in withoutPiece:
                        if other_piece is not None and other_piece.white != self.white:
                            if other_piece.rules(x, y, withoutPiece) and other_piece.restrict(x, y, withoutPiece):
                                print("False for", other_piece)
                                return False
        return True
    
    def rules(self, x, y, pieces_list):
        if abs(self.rect.x - x) <= square_size and abs(self.rect.y - y) <= square_size:
            for i in pieces_list:
                if i != None:
                    if (i.rect.x == x) and (i.rect.y == y):
                        if i.white == self.white:
                            return False 
            return True
        return False
    
class pawn(base):
    def image(self):
        if self.white:
            self.img = pygame.transform.scale(pygame.image.load("images/w-pawn.png"), (square_size, square_size))
        else:
            self.img = pygame.transform.scale(pygame.image.load("images/b-pawn.png"), (square_size, square_size))
            self.white = False
        if self.rect.y > 4*square_size:
            self.up = True
        else:
            self.up = False
        self.firstMove = True

    def restrict(self, x, y, pieces_list):
        return True

    def rules(self, x, y, pieces_list):
        if self.up:
            if self.rect.y > y:
                if self.firstMove:
                    if abs(self.rect.y - y) <= square_size*2:
                        self.firstMove = False
                        return True
                else:
                    if abs(self.rect.y - y) <= square_size:
                        self.firstMove = False
                        return True
        else:
            if self.rect.y < y:
                if self.firstMove:
                    if abs(self.rect.y - y) <= square_size*2:
                        self.firstMove = False
                        return True
                else:
                    if abs(self.rect.y - y) <= square_size:
                        self.firstMove = False
                        return True