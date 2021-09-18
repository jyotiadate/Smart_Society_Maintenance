from MAINTENANCEpack.PayMaintenance.PayOperation import PayOpe
db=PayOpe
class OpeValues:
    def values(self,no, pdate):
        ope = PayOpe()
        res = ope.show(no, pdate)
        print(res)
        if res==True:
            print("insert successfully")
            # ope.selectQuery()
            # ope.selectWhere(no)
        else:
            print("Record not insert ")
    def sear(self,no):
        op=PayOpe()
        oo=op.selectWhere(no)
        return oo

    def upda(self,pdate,No1):
        bb=db.update(pdate,No1)
        return bb

