from MEMBERreg.Operation import operator
db=operator
class FormValues:
    def Values(self,no,dt1,name,email,dob,gender,mobno,ty,square):
        oo=operator()
        res=oo.show(no,dt1,name,email,dob,gender,mobno,ty,square)
        print(res)
        if res==True:
            print("inserted successfully")
            oo.selectQuery()
            oo.selectWhere(2)
        else:
            print("Record not inserted")
    def cn(self):
        oo=operator()
        j=oo.coun()
        return j