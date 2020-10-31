def calc_coords(y, sx, sy):
    x1 = sx*100+370
    x2 = x1+60
    y1 = sy*100+180+y
    y2 = y1+60
    return x1, y1, x2, y2

def draw_nought(c, y, sx, sy):
    """
Draws a nought
c: a Canvas object
sx: 
    """
    x1, y1, x2, y2 = calc_coords(y, sx, sy)
    c.create_oval(x1,y1,x2,y2,width=5.0, outline="#f26a5a")

def draw_cross(c, y, sx, sy):
    x1, y1, x2, y2 = calc_coords(y, sx, sy)
    c.create_line(x1,y1,x2,y2,width=5.0, fill="#1290af")
    c.create_line(x2,y1,x1,y2,width=5.0, fill="#1290af")


def draw_grid(c,y):
    # Draw grid
    c.create_line(550,y,550,y+300,width=5.0, fill="white")
    c.create_line(650,y,650,y+300,width=5.0, fill="white")
    c.create_line(450,y+100,750,y+100,width=5.0, fill="white")
    c.create_line(450,y+200,750,y+200,width=5.0, fill="white")

def draw_victory_line(c, y, code):
    if 1<=code<=3:
        x1, y1, _, y2 = calc_coords(y, 1, code)
        _, y1, x2, y2 = calc_coords(y, 3, code)
        sx, sy = x1, (y1+y2)/2
        fx, fy = x2, (y1+y2)/2
    elif 4<=code<=6:
        x1, y1, x2, _ = calc_coords(y, code-3, 1)
        x1, _, x2, y2 = calc_coords(y, code-3, 3)
        sx, sy = (x1+x2)/2, y1
        fx, fy = (x1+x2)/2, y2
    elif code == 7:
        x1, y1, _, _ = calc_coords(y, 1, 1)
        _, _, x2, y2 = calc_coords(y, 3, 3)
        sx, sy = x1, y1
        fx, fy = x2, y2
    elif code == 8:
        _, y1, x2, _ = calc_coords(y, 3, 1)
        x1, _, _, y2 = calc_coords(y, 1, 3)
        sx, sy = x2, y1
        fx, fy = x1, y2
    c.create_line(sx,sy,fx,fy, fill="#eb9d14", width=10.0)
