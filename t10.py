import tkinter
from tkinter import ttk
frm=tkinter.Tk()
sw=frm.winfo_screenwidth()
sh=frm.winfo_screenheight()
w=(500)
h=(400)
x=(sw-w)//2
y=(sh-h)//2
frm.geometry('{}x{}+{}+{}'.format(w,h,x,y))
frm.title('welcom')

frm.mainloop()
