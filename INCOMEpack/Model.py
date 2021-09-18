from INCOMEpack.Operation import operator
class FromValues:
    def Values(self,incomeno, incomedt, purpose, amount, givenby):
        ob1 = operator()
        res = ob1.show(incomeno, incomedt, purpose, amount, givenby)
        print(res)
        if res==True:
            print("insert successfully")
            ob1.selectQuery()
           # ob1.selectWhere()
        else:
            print("insert unsuccessfully")

