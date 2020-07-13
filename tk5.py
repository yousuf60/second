if __name__ == "__main__":
	import tkinter
	from tkinter import ttk
	frm = tkinter.Tk()
	frm.geometry('600x400')
	x='''frm.resizable(0,0)'''
	frm.config(background='white')
	#......
	lbl1=ttk.Label(frm,text="welcome")
	lbl2=ttk.Label(frm,background='#ffffff',text="your name")
	lbl1.config(background='black' ,foreground='#ff2233', font=('',30),padding=(1,1))
	text_=ttk.Entry(frm)
	text_.config(font=('',15))
	lbl1.pack()
	lbl2.pack()
	text_.pack()
	frm.mainloop()
