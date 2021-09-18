import re
from datetime import datetime
#import datetime

class Validation:
    def readName(self,name):
        x=re.findall("[a-zA-Z _]",name)
        #print(x)
        if len(x)==len(name):
            print("Valid")
            #return True
        else:
            print("Invalid")
            #return False

    def readEmail(self,email):
        y='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (re.search(y,email)):
            print('email is valid')
        else:
            print('email is invalid')

    def num(self,no):
         n=re.findall("[0-9]",no)
         if len(n)==len(no):
             print('no is valid')
         else:
             print('no is invalid')

    def mobNo(self,mob):
        x = '^[7-9]\d{9}$'
        if (re.search(x,mob)):
            print("Valid Number")
            #return True
        else:
             print("Invalid Number")
            #return False

    def password(self,psswd):
        if re.match('[A-Za-z0-9@#$%^&+=]{8,}',psswd):
            print('match')
        else:
            print('no match')

    def date(self,dte):
        x='(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\\d\\d)'
        if (re.search(x,dte)):
        #if len(x)==len(dte):
            return True
            #print('valid date')
        else:
            return False
            #print('invalid date' )

val=Validation()
val.readName("jyoti adate")
val.readEmail('adatejyotijj123@gmail.com')
val.num('101')
val.mobNo('9098788689')
val.password('jyot@123')
val.date('01-01-2020')

