import tkinter as tk
from graphics import *
import tkinter.font as tkFont

def start():
    global root, c, font, photo, photo2, photo3, is_nought, stop, squares_clicked
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
    photo2 = tk.PhotoImage(file="Victory.png")
    photo3 = tk.PhotoImage(file="Game Over.png")
    c.create_image(150,150,image= photo)
    c.bind("<Button-1>", callback)

    is_nought = True
    stop = False
    squares_clicked = {}
    
#Replay button
def close_and_open():
    root.destroy()
    start()

def are_squares_same(s1, s2, s3):
    if s1 in squares_clicked and s2 in squares_clicked and s3 in squares_clicked and squares_clicked[s1] == squares_clicked[s2] == squares_clicked[s3]:
        return True
    else:
        return False

def is_game_finished():
    for i in range(3):
        if are_squares_same((i+1,1), (i+1,2), (i+1,3)):
            return True
        elif are_squares_same((1,i+1), (2,i+1), (3,i+1)):
            return True
    if are_squares_same((1,1),(2,2),(3,3)) or are_squares_same((1,3),(2,2),(3,1)):
        return True
    return False

def winner_is_nought():
    for i in range(3):
        if (i+1,1) in squares_clicked and (i+1,2) in squares_clicked and (i+1,3) in squares_clicked and squares_clicked[(i+1,1)] == squares_clicked[(i+1,2)] == squares_clicked[(i+1,3)] == True:
            return i+4
        if (1,i+1) in squares_clicked and (2,i+1) in squares_clicked and (3,i+1) in squares_clicked and squares_clicked[(1,i+1)] == squares_clicked[(2,i+1)] == squares_clicked[(3,i+1)] == True:
            return i+1
    if (1,1) in squares_clicked and (2,2) in squares_clicked and (3,3) in squares_clicked and squares_clicked[(1,1)] == squares_clicked[(2,2)] == squares_clicked[(3,3)] == True:
        return 7
    if (3,1) in squares_clicked and (2,2) in squares_clicked and (1,3) in squares_clicked and squares_clicked[(3,1)] == squares_clicked[(2,2)] == squares_clicked[(1,3)] == True:
        return 8
    
def winner_is_cross():
    for i in range(3):
        if (i+1,1) in squares_clicked and (i+1,2) in squares_clicked and (i+1,3) in squares_clicked and squares_clicked[(i+1,1)] == squares_clicked[(i+1,2)] == squares_clicked[(i+1,3)] == False:
            return i+4
        if (1,i+1) in squares_clicked and (2,i+1) in squares_clicked and (3,i+1) in squares_clicked and squares_clicked[(1,i+1)] == squares_clicked[(2,i+1)] == squares_clicked[(3,i+1)] == False:
            return i+1
    if (1,1) in squares_clicked and (2,2) in squares_clicked and (3,3) in squares_clicked and squares_clicked[(1,1)] == squares_clicked[(2,2)] == squares_clicked[(3,3)] == False:
        return 7
    if (3,1) in squares_clicked and (2,2) in squares_clicked and (1,3) in squares_clicked and squares_clicked[(3,1)] == squares_clicked[(2,2)] == squares_clicked[(1,3)] == False:
        return 8

def game_over():
    if len(squares_clicked) == 9 and winner_is_nought():
        return
    elif len(squares_clicked) == 9 and winner_is_cross():
        return
    elif len(squares_clicked) == 9:
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

    if game_over() or winner_is_nought() or winner_is_cross():
        c.create_rectangle(900,100,1200,200,fill="#123f56", outline="#123f56")
        c.create_rectangle(0,100,300,200,fill="#123f56", outline="#123f56")
        font3 = tkFont.Font(family='ModernDeco', size=35)
        b = tk.Button(c, text="Replay",font=font3,fg= "#123f56",width=8, height=3, command=close_and_open, bg="white", wraplength=200)
        b.place(x=900,y=265)
        
        stop = True
    if game_over():
        c.create_image(600,75,image= photo3)
    if winner_is_nought():
        c.create_image(150,150,image= photo2)
        draw_victory_line(c, -110, winner_is_nought())
    if winner_is_cross():
        c.create_image(1050,150,image= photo2)
        draw_victory_line(c, -110, winner_is_cross())
        
start()
