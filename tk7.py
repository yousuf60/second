import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#--------
frm=tk.Tk()
frm.geometry('700x600+500+300')
frm.config(bg='#ffffff')
#------------
fnt=('tahoma',30)
#.........
'''lbls=ttk.Style()
lbls.configure('TLabel',bg='black',foregrond='blue')'''
btns=ttk.Style()
btns.configure('TButton',font=('tahoma',20))
#.......
lbl1=ttk.Label(frm,text='Enter any thing:')
lbl1.config(background='white',foreground='blue',font='tahoma')
#.........
txt=ttk.Entry(frm,font=('tahoma',20))
#==========
def m_m():
	print('okay')
	messagebox.showinfo('welcom','hello ' + txt.get())
#--------

btn=ttk.Button(frm,text='hello',padding=2,command=m_m)
btn.config(style='TButton')
#-----------------

lbl1.pack()
txt.pack()
btn.pack()
frm.mainloop()
