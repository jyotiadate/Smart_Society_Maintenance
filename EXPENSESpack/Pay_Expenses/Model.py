from EXPENSESpack.Pay_Expenses.PayOperation import operation
class FormValues:
    def values(self,no1, am1, de1, paid1by, paid):
        op = operation()
        res = op.show(no1, am1, de1, paid1by, paid)
        print(res)
        if res==True:
            print("insert successfully")
            #op.selectQuery()
            #op.selectWhere()

        else:
            print("insert unsuccessfully")

    def search(self,no1):
        op=operation()
        aa=op.selectWhere(no1)
        return  aa



