if __name__ == "__main__":
	import tkinter as tk
	from tkinter import ttk
	frm=tk.Tk()
	frm.title('hello!')
	frm.geometry('600x500')
	frm.maxsize(900,900)
	frm.minsize(100,200)
	frm.config(bg='white')
	lbl1=ttk.Label(frm,text='اهلا وسهلا ^_^')
	lbl2=ttk.Label(frm,text='great')
	lbl1.pack()
	lbl2.pack()
	frm.mainloop()
