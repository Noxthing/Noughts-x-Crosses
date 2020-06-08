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
stop = False
squares_clicked = {}

def is_game_over():
    for i in range(3):
        if (i+1,1) in squares_clicked and (i+1,2) in squares_clicked and (i+1,3) in squares_clicked and squares_clicked[(i+1,1)] == squares_clicked[(i+1,2)] == squares_clicked[(i+1,3)]:
            return True
        if (1,i+1) in squares_clicked and (2,i+1) in squares_clicked and (3,i+1) in squares_clicked and squares_clicked[(1,i+1)] == squares_clicked[(2,i+1)] == squares_clicked[(3,i+1)]:
            return True
    if (1,1) in squares_clicked and (2,2) in squares_clicked and (3,3) in squares_clicked and squares_clicked[(1,1)] == squares_clicked[(2,2)] == squares_clicked[(3,3)]:
        return True
    if (3,1) in squares_clicked and (2,2) in squares_clicked and (1,3) in squares_clicked and squares_clicked[(3,1)] == squares_clicked[(2,2)] == squares_clicked[(1,3)]:
        return True
    if len(squares_clicked) == 9:
        return True

#Play
def callback(event):
    global is_nought
    global stop

    if stop:
        return

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
    if sx > 0 and sy > 0 and (sx, sy) not in squares_clicked:
        squares_clicked[(sx, sy)] = is_nought
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

    if is_game_over():
        print("Game OVER MAN!!!")
        stop = True

c.bind("<Button-1>", callback)
