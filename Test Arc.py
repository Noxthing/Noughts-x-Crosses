import tkinter as tk
root=tk.Tk()
c=tk.Canvas(root, bg="#123f56", height=600, width=1200)
c.pack(fill=tk.BOTH, expand=True)
c.create_arc(0,0,100,100,start=45,extent=180,style=tk.ARC)


