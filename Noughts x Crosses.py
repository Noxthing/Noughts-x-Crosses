import tkinter as tk

c=tk.Canvas()
c.pack(fill=tk.BOTH, expand=True)

c.create_line(450,100,450,400,width=5.0)
c.create_line(550,100,550,400,width=5.0)
c.create_line(350,200,650,200,width=5.0)
c.create_line(350,300,650,300,width=5.0)