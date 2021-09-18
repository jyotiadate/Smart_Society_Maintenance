import tkinter
import tkinter as tk
from tkinter import Label,Entry,Button,NORMAL,END
from MEETINGpack.Model import FormValues
from  tkinter import messagebox
from tkinter.ttk import *
class MyForm:
    dt1=""
    pur1=""
    des1=""
    root=""
    def clear(self):
        self.dt1.delete(0,tk.END)
        self.pur1.delete(0,tk.END)
        self.des1.delete(0,tk.END)
    def sub(self):

        mee = self.dt1.get()
        mpur = self.pur1.get()
        mdes = self.des1.get()
        print(mee, " ", mpur, " ", mdes)
        # ope=operator()
        # res=ope.show(mee,mpur,mdes)
        messagebox.askquestion("Confirm", "Are you attain the meeting")
        ob=FormValues()
        ob.values(mee, mpur, mdes)
        ss=self.clear()

        #self.root.destroy()
    def NewForm(self):
        self.root = tkinter.Tk()
        self.root.geometry("600x600")
        self.root.title("Smart_Society_Maintenance")
        self.root.iconbitmap(r'pp.ico')
        style = Style()
        style.configure('r.TLabel', font=('camel', 17 ,'bold'), foreground='black')
        style.configure("wb.TLabel", font=('camel', 10),foreground="black")
        style.configure('g.TButton', font=('camel', 12), foreground='black')
        style.configure('f.TEntry', font=('camel', 12), foreground='black')

        mee = Label(self.root, text="Meeting",style="r.TLabel")
        mee.place(x=190, y=50)

        dt = Label(self.root, text="Date",style="wb.TLabel")
        dt.place(x=80, y=150)
        self.dt1 = Entry(self.root,style="f.TEntry")
        self.dt1.place(x=180, y=150)
        self.dt1.insert(0, "YYYY-MM-DD")
        self.dt1.configure(state=NORMAL)

        pur = Label(self.root, text="Purpose",style="wb.TLabel")
        pur.place(x=80, y=210)
        self.pur1 = Entry(self.root,style="f.TEntry")
        self.pur1.place(x=180, y=210,width=300,height=30)

        des = Label(self.root, text="Discription",style="wb.TLabel")
        des.place(x=80, y=280)
        self.des1 = Entry(self.root,style="f.TEntry")
        self.des1.place(x=180, y=280, width=300,height=35)


        def on_click(event):
            self.dt1.configure(state=NORMAL)
            self.dt1.delete(0, END)

        self.on_click_id = self.dt1.bind('<Button-1>', on_click)

        btn = Button(self.root, text="Meeting", command=self.sub,style = 'g.TButton')
        btn.place(x=220, y=360)



        self.root.mainloop()



