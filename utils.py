from vars import *

def get_coords(x,y):
    return (x // square_size) * square_size, (y // square_size) * square_size

def get_pos(x,y):
    return int(x/square_size), int(y/square_size)

def get_squares(kingx, kingy, attackx, attacky):
    attacks = []

    ydiff = 1 if kingy > attacky else -1
    xdiff = 1 if kingx > attackx else -1
    if attackx == kingx or attacky == kingy:
        if attackx == kingx:
            for i in range(0, abs(attacky - kingy), 50):
                attacks.append([attackx, attacky + ydiff*i])
        elif attacky == kingy:
            for i in range(0, abs(attackx - kingx), 50):
                attacks.append([attackx + xdiff*i, attacky])
    else:
        for i in range(0, (abs(attackx - kingx)), square_size):
            attacks.append([attackx + xdiff*i, attacky + ydiff*i])
    attacks.append([attackx, attacky])

    return attacks