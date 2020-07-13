import tkinter as tk
frm=tk.Tk()
w=500
h=400
sw=frm.winfo_screenwidth()
sh=frm.winfo_screenheight()
x=(sw-w)/2
y=(sh-h)/2
frm.update()
frm.geometry('%dx%d+%d+%d' %(w,h,x,y))
frm.title(str(w)+'x'+str(h))

frm.mainloop()
