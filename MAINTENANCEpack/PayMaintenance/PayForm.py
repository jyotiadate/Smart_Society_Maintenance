import  tkinter
import tkinter as tk
from tkinter import Label,Entry,Button,StringVar,END,NORMAL,WORD,RIGHT,Y,Text
#from MAINTENANCEpack.PayMaintenance.PayOperation import PayOpe
from MAINTENANCEpack.PayMaintenance.Model import OpeValues
from MAINTENANCEpack.PayMaintenance.PayOperation import PayOpe
from tkinter import messagebox
from tkinter.ttk import*

class MainForm:
    id=""
    payd=""
    #txt=""
    def clearScreen(self):
        self.Id.delete(0,tk.END)
        self.payd.delete(0,tk.END)


    def sub(self):
        no = self.Id.get()
        pdate = self.payd.get()
        print(no, " ", pdate)
        # ope=PayOpe()
        # res=ope.show(no, pdate)
        messagebox.askyesno("Confirm", "Can you Pay Money..?")
        ob=OpeValues()
        ob.values(no, pdate)
        ss = self.clearScreen()

        # self.root.destroy()
    def select(self):
        oo=OpeValues()
        no = self.Id.get()
        ss=oo.sear(no)
        print(ss)
        self.txt.insert(tk.END,ss[0])
        self.txt.config(state="disabled")

    def up(self):
        aa=OpeValues()
        no = self.Id.get()
        pdate = self.payd.get()
        bc=aa.upda(pdate,no)

    # def close(self):
    #     self.root.destroy()
    def NewForm(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x570")
        self.root.title("PayMaintenance")
        self.root.iconbitmap(r'pp.ico')
        style = Style()
        style.configure('r.TLabel', font=('camel', 17, 'bold'), foreground='black')
        style.configure("wb.TLabel", font=('camel', 10), foreground="black")
        style.configure('g.TButton', font=('camel', 12), foreground='black')
        style.configure('f.TEntry', font=('camel', 11), foreground='black')

        pay = Label(self.root, text="Pay Maintenance", style="r.TLabel")
        pay.place(x=170, y=40)

        no = Label(self.root, text="No",style='wb.TLabel')
        no.place(x=40, y=130)
        self.Id = Entry(self.root,style="f.TEntry")
        self.Id.place(x=130, y=130)
        self.Id.insert(0, "Please Enter R/C No")
        self.Id.configure(state=NORMAL)

    #def select(self):
        search = Button(self.root, text="Search", command=self.select,style = 'g.TButton')
        search.place(x=300, y=130)
        # if search==no:
        #     return no
        # else:
        #     messagebox.askokcancel("Confirm","plese insert number")
        #self.scroll=Scrollbar()
        self.txtareaframe=Frame()
        self.txtareaframe.place(x=130,y=220) # tkinter.Text(self.root, height=7, width=35)
        self.scroll=Scrollbar(self.txtareaframe)
        self.scroll.pack(side=RIGHT,fill=Y)
        self.txt=Text(self.txtareaframe,wrap=WORD,yscrollcommand=self.scroll.set,height=7,width=35)
        self.txt.pack()
        self.scroll.config(command=self.txt.yview)

        pdate = Label(self.root, text="Paid date", style="wb.TLabel")
        pdate.place(x=40, y=370)
        self.payd = Entry(self.root,style="f.TEntry")
        self.payd.place(x=130, y=370)
        self.payd.insert(0, "YYYY-MM-DD")
        self.payd.configure(state=NORMAL)

        def on_click(event):
            self.Id.configure(state=NORMAL)
            self.Id.delete(0, END)

        def on_click1(event):
            self.payd.configure(state=NORMAL)
            self.payd.delete(0, END)


        self.on_click_id = self.Id.bind('<Button-1>', on_click)
        self.on_click_id = self.payd.bind('<Button-1>', on_click1)

        pbtn = Button(self.root, text="Submit", command=self.sub, style = 'g.TButton')
        pbtn.place(x=150, y=450)
        self.root.mainloop()
























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































