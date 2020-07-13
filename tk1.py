import tkinter as tk

class Applcation (tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()
        self.config(bg='gray')
    def create_widgets(self):
        self.welcom=tk.Button(self,text="welcoom",fg="green",bg='black')
        self.welcom.pack(side='right')
        self.hi_bro=tk.Button(self)
        self.hi_bro['text']= "welcome\n (you want some thing?)"
        self.hi_bro['fg']='blue'
        
        
        self.hi_bro["command"]=self.say_hi
        self.hi_bro.pack(side='top')
        self.quit=tk.Button(self,text="exite",fg="red",
                            command=self.master.destroy)
        self.quit.pack(side="bottom")
    def say_hi(self):
        print("hellooooooo")
root=tk.Tk()
app=Applcation(master=root)
app.master.title("this is for trying")
app.master.maxsize(0,0)
app.mainloop()
