import tkinter as tk
from tkinter import ttk
frm=tk.Tk()
w=600
h=400
sw =frm.winfo_screenwidth()
sh =frm.winfo_screenheight()
x=(sw-w)/2
y=(sh-h)/2

#.......
gw=frm.winfo_width()
gw=frm.winfo_height()
frm.title('hello user')
#frm.update()
frm.resizable(1,1)
#.........
lbl1=ttk.Label(frm,text='frist')
lbl1.config(foreground='blue',font='impact')
lbl1.pack()
#.......
frm.geometry('%dx%d+%d+%d'%(w,h,x,y))
frm.update()
frm.mainloop()
