import tkinter
import tkinter as tk
from tkinter import Label,Entry,Button,NORMAL,END
#from EventMVC.Operation import operator
from EventMVC.Model import FormValues
from tkinter import messagebox
from tkinter.ttk import *
class MyForm:
        Eno1=""
        dat=""
        pur1=""
        cost1=""
        fd1=""
        td1=""
        root=""
        def ClearScreen(self):
            self.Eno1.delete(0,tk.END)
            self.dat.delete(0,tk.END)
            self.pur1.delete(0,tk.END)
            self.cost1.delete(0,tk.END)
            self.fd1.delete(0,tk.END)
            self.td1.delete(0,tk.END)

        def sub(self):
            Eno = self.Eno1.get()
            dt =self. dat.get()
            pur = self.pur1.get()
            cost =self. cost1.get()
            fdate =self. fd1.get()
            tdate = self.td1.get()
            print(Eno, " ", dt, " ", pur, " ", cost, " ", fdate, " ", tdate)
            # ope=operator()
            # res=ope.show(Eno,dt,pur,cost,fdate,tdate)
            # self.close()
            messagebox.askyesno("Inform", "Are you sure")
            ss=FormValues()
            ss.values(Eno,dt,pur,cost,fdate,tdate)
            aa=self.ClearScreen()

            #self.root.destroy()
        # def close(self):
        #     self.root.destroy()
        def cn(self):
            s=FormValues()
            ob=s.counter()
            Eno = self.Eno1.get()
            self.Eno1.insert(tk.END,ob)

        def NewForm(self):
            self.root = tkinter.Tk()
            self.root.geometry("500x570")
            self.root.title("Event")
            style = Style()
            style.configure('r.TLabel',font=('camel', 17, 'bold'),foreground='black')
            style.configure("wb.TLabel",font=('camel', 10), foreground="black")
            style.configure('b.TButton',font=('camel', 12),foreground='black')
            style.configure('f.TEntry', font=('camel', 11), foreground='black')

            Inc = Label(self.root, text="Event",style="r.TLabel")
            Inc.place(x=160, y=35)
            #style.configure("BW.TLabel", foreground="blue", background="white")

            no = Label(self.root, text="E.No",style="wb.TLabel")
            no.place(x=50, y=110)
            self.Eno1 = Entry(self.root,style="f.TEntry")
            self.Eno1.place(x=130, y=110)
            self.Eno1.insert(0, "Please Enter No")
            self.Eno1.configure(state=NORMAL)

            dt = Label(self.root, text="Date",style="wb.TLabel")
            dt.place(x=50, y=160)
            self.dat = Entry(self.root,style="f.TEntry")
            self.dat.place(x=130, y=160)
            self.dat.insert(0, "YYYY-MM-DD")
            self.dat.configure(state=NORMAL)

            pur = Label(self.root, text="Purpose",style="wb.TLabel")
            pur.place(x=50, y=200)
            self.pur1 = Entry(self.root,style="f.TEntry")
            self.pur1.place(x=130, y=200,height=57,width=310)

            amt = Label(self.root, text="Cost",style="wb.TLabel")
            amt.place(x=50, y=280)
            self.cost1 = Entry(self.root,style="f.TEntry")
            self.cost1.place(x=130, y=280)

            fd = Label(self.root, text="Date",style="wb.TLabel")
            fd.place(x=50, y=320)

            fd = Label(self.root, text="From", style="wb.TLabel")
            fd.place(x=160, y=320)
            self.fd1 = Entry(self.root)
            self.fd1.place(x=130, y=360)
            self.fd1.insert(0, "YYYY-MM-DD")
            self.fd1.configure(state=NORMAL)

            till = Label(self.root, text="Till",style="wb.TLabel")
            till.place(x=320, y=320)
            self.td1 = Entry(self.root,style="f.TEntry")
            self.td1.place(x=290, y=360)
            self.td1.insert(0, "YYYY-MM-DD")
            self.td1.configure(state=NORMAL)

            def on_click(event):
                self.Eno1.configure(state=NORMAL)
                self.Eno1.delete(0, END)

            def on_click1(event):
                self.dat.configure(state=NORMAL)
                self.dat.delete(0, END)

            def on_click2(event):
                self.fd1.configure(state=NORMAL)
                self.fd1.delete(0, END)

            def on_click3(event):
                self.td1.configure(state=NORMAL)
                self.td1.delete(0, END)

            self.on_click_id = self.Eno1.bind('<Button-1>', on_click)
            self.on_click_id = self.dat.bind('<Button-1>', on_click1)
            self.on_click_id = self.fd1.bind('<Button-1>', on_click2)
            self.on_click_id = self.td1.bind('<Button-1>', on_click3)

            add = Button(self.root, text="Submit",style = 'b.TButton',  command=self.sub)
            add.place(x=200, y=420)
            self.root.mainloop()


