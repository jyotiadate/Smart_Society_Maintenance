from EventMVC.Operation import operator
class FormValues:
    def values(self,Eno,dt,pur,cost,fdate,tdate):
        ope = operator()
        res = ope.show(Eno, dt, pur, cost, fdate, tdate)
        print(res)
        if res==True:
            print("Result successfully")
            ope.selectQuery()
            ope.selectWhere()
        else:
            print("Record not inserted")

    def counter(self):
        ob=operator()
        ss=ob.count()
        #return ss