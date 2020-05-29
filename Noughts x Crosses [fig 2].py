import tkinter as tk
from graphics import *
import tkinter.font as tkFont

root=tk.Tk()
c=tk.Canvas(root, bg="#123f56", height=600, width=1200)
c.pack(fill=tk.BOTH, expand=True)

# Draw grid for main game
draw_grid(c,150)

#Text
font = tkFont.Font(family='ModernDeco', size=35)
c.create_text(150,75,text="PLAYER 1",font=font, fill="white",width=200)
c.create_text(1050,75,text="PLAYER 2",font=font, fill="white",width=200)
#Turn
photo = tk.PhotoImage(file="Green Turn.png")
c.create_image(150,150,image= photo)

is_nought = True

#Play
def callback(event):
    global is_nought
    if  550 > event.x > 450:
        sx=1
    elif 650 > event.x > 550:
        sx=2
    elif 750 > event.x > 650:
        sx=3
    else:
        sx=0
        
    if  250 > event.y > 150:
        sy=1
    elif 350 > event.y > 250:
        sy=2
    elif 450 > event.y > 350:
        sy=3
    else:
        sy=0
    if sx > 0 and sy > 0:
        if is_nought:
            c.create_image(150,150,image= photo)
            c.create_rectangle(900,100,1200,200,fill="#123f56", outline="#123f56")
            draw_nought(c, -110, sx, sy)
            c.create_image(1050,150,image= photo)
            c.create_rectangle(0,100,300,200,fill="#123f56", outline="#123f56")
        else:
            c.create_image(1050,150,image= photo)
            c.create_rectangle(0,100,300,200,fill="#123f56", outline="#123f56")
            draw_cross(c, -110, sx, sy)
            c.create_image(150,150,image= photo)
            c.create_rectangle(900,100,1200,200,fill="#123f56", outline="#123f56")
            
        is_nought = not is_nought

c.bind("<Button-1>", callback)
