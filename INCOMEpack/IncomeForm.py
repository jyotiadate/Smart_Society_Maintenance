import tkinter
import tkinter as tk
from tkinter import Label,Entry,Button,NORMAL,END
from INCOMEpack.Model import FromValues
from tkinter import messagebox
from tkinter.ttk import *
class MyForm:
    no1=""
    dt1=""
    pur1=""
    amt1=""
    given1=""
    root=""

    def ClearScreen(self):
        self.no1.delete(0,tk.END)
        self.dt1.delete(0,tk.END)
        self.pur1.delete(0,tk.END)
        self.amt1.delete(0,tk.END)
        self.given1.delete(0,tk.END)

    def sub(self):
        incomeno = self.no1.get()
        incomedt = self.dt1.get()
        purpose = self.pur1.get()
        amount = self.amt1.get()
        givenby = self.given1.get()
        print(incomeno, " ", incomedt, " ", purpose, " ", amount, " ", givenby)
    #     ope=operator()
    #     res=ope.show(incomeno,incomedt,purpose,amount,givenby)
        messagebox.askyesno("Confirm", "Can you submit income.....?")
        ob1=FromValues()
        ob1.Values(incomeno, incomedt, purpose, amount, givenby)
        ss=self.ClearScreen()
    # def close(self):
    #     self.root.destroy()

    def NewForm(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x570")
        self.root.title("Smart_Society_Maintenance")
        self.root.iconbitmap(r'pp.ico')
        style = Style()
        style.configure('r.TLabel', font=('camel', 17, 'bold'), foreground='black')
        style.configure("wb.TLabel", font=('camel', 10), foreground="black")
        style.configure('g.TButton', font=('camel', 12), foreground='black')
        style.configure('f.TEntry', font=('camel', 11), foreground='black')

        Inc = Label(self.root, text="Income",style="r.TLabel")
        Inc.place(x=170, y=40)

        no = Label(self.root, text="I.No",style="wb.TLabel")
        no.place(x=30, y=110)
        self.no1 = Entry(self.root,style="f.TEntry")
        self.no1.place(x=110, y=110)
        self.no1.insert(0, "Please Enter No")
        self.no1.configure(state=NORMAL)

        dt = Label(self.root, text="Date",style="wb.TLabel")
        dt.place(x=270, y=110)
        self.dt1 = Entry(self.root,style="f.TEntry")
        self.dt1.place(x=330, y=110)
        self.dt1.insert(0, "YYYY-MM-DD")
        self.dt1.configure(state=NORMAL)

        pur = Label(self.root, text="Purpose",style="wb.TLabel")
        pur.place(x=30, y=170)
        self.pur1 = Entry(self.root,style="f.TEntry")
        self.pur1.place(x=110, y=170,width=300,height=50)

        amt = Label(self.root, text="Amt",style="wb.TLabel")
        amt.place(x=30, y=250)
        self.amt1 = Entry(self.root,style="f.TEntry")
        self.amt1.place(x=110, y=250)

        given = Label(self.root, text="Given by",style="wb.TLabel")
        given.place(x=30, y=310)
        self.given1 = Entry(self.root,style="f.TEntry")
        self.given1.place(x=110, y=310)
        self.given1.insert(0, "Please Enter Full Name")
        self.given1.configure(state=NORMAL)

        def on_click(event):
            self.no1.configure(state=NORMAL)
            self.no1.delete(0, END)

        def on_click1(event):
            self.dt1.configure(state=NORMAL)
            self.dt1.delete(0, END)

        def on_click2(event):
            self.given1.configure(state=NORMAL)
            self.given1.delete(0, END)

        # def on_click3(event):
        #     self.till.configure(state=NORMAL)
        #     self.till.delete(0, END)
        #
        self.on_click_id = self.no1.bind('<Button-1>', on_click)
        self.on_click_id = self.dt1.bind('<Button-1>', on_click1)
        self.on_click_id = self.given1.bind('<Button-1>', on_click2)
        # self.on_click_id = self.till.bind('<Button-1>', on_click3)
        #
        add = Button(self.root, text="Add Income", command=self.sub,style = 'g.TButton')
        add.place(x=150, y=380)

        self.root.mainloop()





    