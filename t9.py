def word():
	messagebox.showinfo('test succed',
	'its informaion,and welcom'+txt1.get())
	messagebox.showerror('hey','wrong')
	tkinter.messagebox.askokcancel('title','ok or ???')
import tkinter
from tkinter import ttk
from tkinter import messagebox
frm=tkinter.Tk()
frm.geometry('600x700+200+0')
frm.config(bg='white')
#.......
fnt=('tahoma',15)
#styles-------
lbls=ttk.Style()
lbls.configure('TLabel',font=fnt,background='white')
btns=ttk.Style()
btns.configure('TButton',font=('tahoma',15),padding=3,background='#ffff11',foreground='blue')
#stringvariables----
svname1=tkinter.StringVar()
#entry---------
txt1=ttk.Entry(frm,textvariable=svname1)
txt1.config(font=('tahoma',13))
svname1.set('write')
#button--------
btn=ttk.Button(frm,text='test again',command=word)
btn.config(style='TButton')
#label----------
lbl1=ttk.Label(frm,text='test')
lbl1.config(style='TLabel')
# .pack()--------
lbl1.pack()
txt1.pack()
btn.pack()
#mainloop--------
frm.mainloop() 
