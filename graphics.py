def calc_box_coords(y, sx, sy):
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
    x1, y1, x2, y2 = calc_box_coords(y, sx, sy)
    c.create_oval(x1,y1,x2,y2,width=5.0, outline="#f26a5a")

def draw_cross(c, y, sx, sy):
    x1, y1, x2, y2 = calc_box_coords(y, sx, sy)
    c.create_line(x1,y1,x2,y2,width=5.0, fill="#1290af")
    c.create_line(x2,y1,x1,y2,width=5.0, fill="#1290af")


def draw_grid(c,y):
    # Draw grid
    c.create_line(550,y,550,y+300,width=5.0, fill="white")
    c.create_line(650,y,650,y+300,width=5.0, fill="white")
    c.create_line(450,y+100,750,y+100,width=5.0, fill="white")
    c.create_line(450,y+200,750,y+200,width=5.0, fill="white")

def draw_victory_line_h(c, sy):
    c.create_line(450,(sy+1)*100,750,(sy+1)*100,width=10.0, fill="#eb9d14")

def draw_victory_line_v(c, sx):
    c.create_line((sx+4)*100,150,(sx+4)*100,450,width=10.0, fill="#eb9d14")

def draw_victory_line_d1(c):
    c.create_line(450,150,750,450,width=10.0, fill="#eb9d14")

def draw_victory_line_d2(c):
    c.create_line(750,150,450,450,width=10.0, fill="#eb9d14")

def draw_victory_line_d(c,is_l):
    x1, x2 = (450, 750) if is_l else (750, 450)
    y1, y2 = 150, 450
    c.create_line(x1,y1,x2,y2,width=10.0, fill="#eb9d14")
