import tkinter as tk
import tkinter.font as tkFont
from graphics import *

root=tk.Tk()
c=tk.Canvas(root, bg="#123f56", height=600, width=1200)
c.pack(fill=tk.BOTH, expand=True)

draw_grid(c,260)

# Draw Circles
draw_nought(c, 0, 2,1)
draw_nought(c, 0, 3,2)
draw_nought(c, 0, 2,3)

# Draw Crosses
draw_cross(c, 0, 1,1)
draw_cross(c, 0, 2,2)
draw_cross(c, 0, 3,3)

# Draw Victory line
draw_victory_line(c, 0, 7)

# Name text
font = tkFont.Font(family='ModernDeco', size=65)
font2 = tkFont.Font(family='ModernDeco', size=30)
font3 = tkFont.Font(family='ModernDeco', size=35)
photo = tk.PhotoImage(file="N x C rainbow.gif")
c.create_image(600,105,image= photo)
c.create_text(600,170,text="by Nxxthing",font=font2, fill="white")
c.create_text(250,425,text="Be the first to align 3 symbols!",font=font3, fill="white",width=200)

#Button
def close_and_open():
    root.destroy()
    import NxCfig2

c.pack(fill=tk.BOTH, expand=True)
b = tk.Button(c, text="Click here to play",font=font3,fg= "#123f56",width=8, height=3, command=close_and_open, bg="white", wraplength=200)
b.place(x=900,y=325)

root.mainloop()
