def fff():
	frm2=tkinter.Tk()
	frm2.geometry('100x200+400+200')
	frm2.mainloop()
#importing-------
import tkinter
from tkinter import ttk

#---------
frm1=tkinter.Tk()
frm1.geometry('600x400+550+100')

#-----------
lbl1=ttk.Label(frm1,text='test again')
#button-----------
btn=ttk.Button(frm1,text='hello',command=fff)
#.pack()----------
lbl1.pack()
btn.pack()
#mainloops--------
frm1.mainloop()

