import tkinter
import tkinter as tk
from tkinter import Label,Entry,Button,NORMAL,END,RIGHT,Text,Y,WORD
#from EXPENSESpack.Pay_Expenses.PayOperation import operation
from EXPENSESpack.Pay_Expenses.Model import FormValues
from tkinter import messagebox
from tkinter.ttk import *
class MyForm:
    No=""
    am=""
    de=""
    paid1=""
    pd=""
    root=""
    def ClearScreen(self):
        self.No.delete(0,tk.END)
        self.am.delete(0,tk.END)
        self.de.delete(0,tk.END)
        self.paid1.delete(0,tk.END)
        self.pd.delete(0,tk.END)
    def sub(self):
        no1 = self.No.get()
        am1 = self.am.get()
        de1 = self.de.get()
        paid1by = self.paid1.get()
        paid = self.pd.get()
        print(no1, am1, de1, paid1by, paid)
        # op=operation()
        # res=op.show(no1, am1, de1, paid1by, paid)
        messagebox.askyesno("Confirm", "")
        ob=FormValues()
        ob.values(no1, am1, de1, paid1by, paid)
        ss=self.ClearScreen()

        #self.root.destroy()
    def select(self):
        aa = FormValues()
        no1=self.No.get()
        ss = aa.search(no1)
        # ss=operation()
        #print(ss)
        self.txt.insert(tk.END,ss[0])
        self.txt.config(state="disabled")

    def NewForm(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x570")
        self.root.title("Smart_Society_Maintenance")
        self.root.iconbitmap(r'pp.ico')
        style = Style()
        style.configure('r.TLabel', font=('camel', 17, 'bold'), foreground='black')
        style.configure("wb.TLabel", font=('camel', 10), foreground="black")
        style.configure('g.TButton', font=('camel', 10 ), foreground='black')
        style.configure('f.TEntry', font=('camel', 11), foreground='black')

        pay = Label(self.root, text="Pay Expenses",style="r.TLabel")
        pay.place(x=170, y=20)

        no = Label(self.root, text="No",style="wb.TLabel")
        no.place(x=50, y=90)
        self.No = Entry(self.root,style="f.TEntry")
        self.No.place(x=150, y=90)
        self.No.insert(0, "Please Enter No")
        self.No.configure(state=NORMAL)

        search = Button(self.root, text="Search", command=self.select,style = 'g.TButton')
        search.place(x=330, y=90,height=30,width=80)
        #
        # self.txt = tkinter.Text(self.root, height=6, width=35)
        # self.txt.place(x=150, y=150)

        self.txtareaframe = Frame()
        self.txtareaframe.place(x=150, y=150)  # tkinter.Text(self.root, height=7, width=35)
        self.scroll = Scrollbar(self.txtareaframe)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.txt = Text(self.txtareaframe, wrap=WORD, yscrollcommand=self.scroll.set, height=6, width=35)
        self.txt.pack()
        self.scroll.config(command=self.txt.yview)

        #
        amt1 = Label(self.root, text="Amout",style="wb.TLabel")
        amt1.place(x=50, y=280)
        self.am = Entry(self.root,style="f.TEntry")
        self.am.place(x=150, y=280)

        des = Label(self.root, text="Description",style="wb.TLabel")
        des.place(x=50, y=330)
        self.de = Entry(self.root,style="f.TEntry")
        self.de.place(x=150, y=330,height=60,width=280)
        self.de.insert(0, "Enter Descripntion")
        self.de.configure(state=NORMAL)

        pb = Label(self.root, text="Paid by",style="wb.TLabel")
        pb.place(x=50, y=420)
        self.paid1 = Entry(self.root,style="f.TEntry")
        self.paid1.place(x=150, y=420)
        self.paid1.insert(0, "Enter name")
        self.paid1.configure(state=NORMAL)

        pdate = Label(self.root, text="Paid Date",style="wb.TLabel")
        pdate.place(x=50, y=470)
        self.pd = Entry(self.root,style="f.TEntry")
        self.pd.place(x=150, y=470)
        self.pd.insert(0, "YYYY-MM-DD")
        self.pd.configure(state=NORMAL)

        def on_click(event):
            self.No.configure(state=NORMAL)
            self.No.delete(0, END)

        def on_click1(event):
            self.am.configure(state=NORMAL)
            self.am.delete(0, END)

        def on_click2(event):
            self.de.configure(state=NORMAL)
            self.de.delete(0, END)

        def on_click3(event):
            self.paid1.configure(state=NORMAL)
            self.paid1.delete(0, END)

        def on_click4(event):
            self.de.configure(state=NORMAL)
            self.de.delete(0, END)

        self.on_click_id = self.No.bind('<Button-1>', on_click)
        self.on_click_id = self.am.bind('<Button-1>', on_click2)
        self.on_click_id = self.paid1.bind('<Button-1>', on_click3)
        self.on_click_id = self.de.bind('<Button-1>', on_click4)

        pay = Button(self.root, text="Pay", command=self.sub,style = 'g.TButton')
        pay.place(x=170, y=530)

        self.root.mainloop()


