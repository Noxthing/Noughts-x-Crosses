import tkinter as tk
root=tk.Tk()
c=tk.Canvas(root, bg="#123f56", height=600, width=1200)
c.pack(fill=tk.BOTH, expand=True)

def calc_coords(sx, sy):
    x1 = sx*100+370
    x2 = x1+60
    y1 = sy*100+180
    y2 = y1+60
    return x1, y1, x2, y2

def draw_nought(sx, sy):
    x1, y1, x2, y2 = calc_coords(sx, sy)
    c.create_oval(x1,y1,x2,y2,width=5.0, outline="#f26a5a")

def draw_cross(sx, sy):
    x1, y1, x2, y2 = calc_coords(sx, sy)
    c.create_line(x1,y1,x2,y2,width=5.0, fill="#1290af")
    c.create_line(x2,y1,x1,y2,width=5.0, fill="#1290af")

# Draw grid
c.create_line(550,260,550,560,width=5.0, fill="white")
c.create_line(650,260,650,560,width=5.0, fill="white")
c.create_line(450,360,750,360,width=5.0, fill="white")
c.create_line(450,460,750,460,width=5.0, fill="white")

# Draw Circles
draw_nought(2,1)
draw_nought(3,2)
draw_nought(2,3)

# Draw Crosses
draw_cross(1,1)
draw_cross(2,2)
draw_cross(3,3)

# Draw Victory line
c.create_arc(480,290,520,330,start=45,extent=180,outline="#eb9d14",width=5.0,style=tk.ARC)
c.create_arc(680,490,720,530,start=225,extent=180,outline="#eb9d14",width=5.0,style=tk.ARC)
c.create_line(485,322.5,687.5,525,fill="#eb9d14",width=5.0)
c.create_line(512.5,295,715,497.5,fill="#eb9d14",width=5.0)
