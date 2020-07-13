
import tkinter as tk
from tkinter import ttk
frm=tk.Tk()
frm.geometry('600x400')
frm.config(bg='white')
font1=('tahoma',25 )
#.......
lbls=ttk.Style()
lbls.configure('TLabel',background='#ffffff',foreground='red',font=font1)
btns=ttk.Style()
btns.configure('TButton',font=('',15))
#.......
lbl1=ttk.Label(frm,text='yoyo:')
lbl1.config(style='TLabel')
tname=ttk.Entry(frm,font=font1)
btn=ttk.Button(frm,text='nice',style='TButton')
#.......
lbl1.pack()
tname.pack()
btn.pack()
#.........
frm.mainloop()
