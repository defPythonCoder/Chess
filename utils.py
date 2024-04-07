square_size = 50

def get_coords(x,y):
    return (x // square_size) * square_size, (y // square_size) * square_size

def get_pos(x,y):
    return int(x/square_size), int(y/square_size)