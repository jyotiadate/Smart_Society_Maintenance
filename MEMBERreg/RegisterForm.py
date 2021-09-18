import tkinter
import tkinter as tk
from tkinter.ttk import *
from tkinter import Label,Entry,Radiobutton,StringVar,Button,re,IntVar,Tk,DISABLED,NORMAL,END
from MEMBERreg.Model import FormValues
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter.ttk import *
import re

class MyForm:
    no1=""
    dt=""
    fnm=""
    email1=""
    dob1=""
    v=""
    mobno1=""
    variable1=""
    Ft=""

    def clearScreen(self):
        self.no1.delete(0,tk.END)
        self.dt.delete(0,tk.END)
        self.fnm.delete(0,tk.END)
        self.email1.delete(0,tk.END)
        self.dob1.delete(0,tk.END)
        self.mobno1.delete(0,tk.END)
        self.Ft.delete(0,tk.END)

    def sub(self):
        no=self.no1.get()
        dt1=self.dt.get()
        name=self.fnm.get()
        email=self.email1.get()
        dob=self.dob1.get()
        gender=self.v.get()
        mobno=self.mobno1.get()
        ty=self.variable1.get()
        square=self.Ft.get()

        root=""
        print(no, " ", dt1, " ", name, " ", email, " ", dob, " ", gender, " ", mobno, " ", ty, " ", square)
        #self.close()
        #ope=operator()
        #res=ope.show(no,dt1,name,email,dob,gender,mobno, ty,square)


    # def close(self):
    #         self.root.destroy()
        MsgBox = tk.messagebox.askokcancel('Registration', 'Are you sure you want to submit form',
                                       icon='warning')

    # if MsgBox == 'yes':
    #     self.root.destroy()
    # else:
    #     tk.messagebox.showinfo('Return', 'You will now return to the application screen')
        #self.root.destroy()
        mm = FormValues()
        mm.Values(no, dt1, name, email, dob, gender, mobno, ty, square)
        s = self.clearScreen()

    def cooun(self):
        aa=FormValues()
        no = self.no1.get()
        bb=aa.cn()
        print(bb,"dfhghjk")
        self.no1.insert(tk.END,bb)


    def NewForm(self):
            self.root =Tk()
            self.root.geometry("600x600")
            self.root.title("Member Registration Form")
            style = Style()
            style.configure('r.TLabel', font=('camel', 17, 'bold'), foreground='black')
            style.configure("wb.TLabel", font=('camel', 10), foreground="black")
            style.configure('g.TButton', font=('camel', 13, 'bold'), foreground='black')
            style.configure('f.TEntry', font=('camel', 10, 'bold'), foreground='black')

            ll=Label(self.root,text="Member Registration",style="r.TLabel")
            ll.place(x=140,y=35)

            no = Label(self.root, text="No", style="wb.TLabel")
            no.place(x=50, y=110)
            ob = tkinter.StringVar()
            self.no1 = Entry(self.root, textvariable=ob,style="f.TEntry")
            self.no1.place(x=130, y=110)
            self.no1.insert(0, "enter R/C no")
            self.no1.configure(state=NORMAL)

            # ff = FormValues()
            # a=ff.cn()
            # #self.no1.insert(tk.END,a[0][0])
            dat = Label(self.root, text="Date",style="wb.TLabel" )
            dat.place(x=290, y=110)#
            self.dt = Entry(self.root,style="f.TEntry")
            self.dt.place(x=340, y=110)
            self.dt.insert(0, "YYYY-MM-DD")
            self.dt.configure(state=NORMAL)

            name = Label(self.root, text="Name",style="wb.TLabel")
            name.place(x=50, y=150)
            self.fnm = Entry(self.root,style="f.TEntry")
            self.fnm.place(x=130, y=150,width=300)
            self.fnm.insert(0,"Please Enter Full Name")
            self.fnm.configure(state=NORMAL)

            email = Label(self.root, text="Email",style="wb.TLabel")
            email.place(x=50, y=190)
            self.email1 = Entry(self.root,style="f.TEntry")
            self.email1.place(x=130, y=190,width=300)
            self.email1.insert(0, "email@gmail.com")
            self.email1.configure(state=NORMAL)
            #
            dob = Label(self.root, text="DOB", style="wb.TLabel")
            dob.place(x=50, y=230)
            self.dob1 =Entry(self.root)#,pattern="yyyy-mm-dd")
            self.dob1.place(x=130, y=230)

            mobno = Label(self.root, text="Mobno", width=20,style="wb.TLabel")
            mobno.place(x=50, y=270)
            self.mobno1 = Entry(self.root,style="f.TEntry")
            self.mobno1.place(x=130, y=270)

            Ty = Label(self.root, text="Type",style="wb.TLabel")
            Ty.place(x=50, y=310)

            OptionList = ["Select",
                          "Residential",
                          "Commercial"
                          ]
            self.variable1 = tkinter.StringVar(self.root)
            self.variable1.set(OptionList[0])
            opl = tkinter.OptionMenu(self.root, self.variable1, *OptionList)
            opl.config(width=8, font=('Helvetica', 12))
            opl.place(x=130, y=310)

            sq = Label(self.root, text="Sq/Ft", width=20, style="wb.TLabel")
            sq.place(x=50, y=370)
            self.Ft = Entry(self.root,style="f.TEntry")
            self.Ft.place(x=130, y=370)

            self.v = tkinter.StringVar()
            tk=Label(self.root, text="Gender",style="wb.TLabel")
            tk.place(x=50, y=420)
            tk=Radiobutton(self.root, text="male", variable=self.v, value="male")
            tk.place(x=130, y=420)
            tk=Radiobutton(self.root, text="female", variable=self.v, value="female")
            tk.place(x=200, y=420)

            CheckVar1 = IntVar()
            C1 = Checkbutton(self.root, text="Accept Terms and Conditions", variable=CheckVar1,onvalue=1, offvalue=0)
            C1.place(x=50,y=460)
            Button(self.root, text='Register', command=self.sub,style = 'g.TButton').place(x=180, y=510)

            def on_click(event):
                self.no1.configure(state=NORMAL)
                self.no1.delete(0,END)

            def on_click1(event):
                self.dt.configure(state=NORMAL)
                self.dt.delete(0, END)

            def on_click2(event):
                self.fnm.configure(state=NORMAL)
                self.fnm.delete(0,END)

            def on_click3(event):
                self.email1.configure(state=NORMAL)
                self.email1.delete(0, END)

                # make the callback only work once

           # self.no1.unbind('<Button-1>',self. on_click_id)

            self.on_click_id = self.no1.bind( '<Button-1>',on_click)
            self.on_click_id = self.dt.bind('<Button-1>', on_click1)
            self.on_click_id = self.fnm.bind('<Button-1>', on_click2)
            self.on_click_id = self.email1.bind('<Button-1>', on_click3)
            self.root.mainloop()
