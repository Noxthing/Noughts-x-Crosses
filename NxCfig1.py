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
#c.create_arc(480,290,520,330,start=45,extent=180,outline="#eb9d14",width=5.0,style=tk.ARC)
#c.create_arc(680,490,720,530,start=225,extent=180,outline="#eb9d14",width=5.0,style=tk.ARC)
#c.create_line(485,322.5,687.5,525,fill="#eb9d14",width=5.0)
#c.create_line(512.5,295,715,497.5,fill="#eb9d14",width=5.0)
c.create_line(450,260,750,560, fill="#eb9d14", width=10.0)

# Name text
font = tkFont.Font(family='ModernDeco', size=65)
font2 = tkFont.Font(family='ModernDeco', size=30)
font3 = tkFont.Font(family='ModernDeco', size=35)
photo = tk.PhotoImage(file="N x C rainbow.gif")
c.create_image(600,105,image= photo)
#c.create_text(600,105,text="NOUGHTS X CROSSES",font=font, fill="white")
c.create_text(600,170,text="by Nxxthing",font=font2, fill="white")
c.create_text(250,425,text="Be the first to align 3 symbols!",font=font3, fill="white",width=200)

#Button
def close_and_open():
    root.destroy()
    print ("Please wait for the game to start...")
    #exec (open ("Noughts x Crosses [fig 2].py").read())
    import NxCfig2

c.pack(fill=tk.BOTH, expand=True)
b = tk.Button(c, text="Click here to play",font=font3,fg= "#123f56",width=8, height=3, command=close_and_open, bg="white", wraplength=200)
b.place(x=900,y=325)
c.create_text(950,425,text="Click here to play",font=font3, fill="#123f56",width=200)

root.mainloop()
