from MEETINGpack.MeetingOpe import operator
class FormValues:
    def values(self,mee, mpur, mdes):
        ope = operator()
        res = ope.show(mee, mpur, mdes)
        print(res)
        if res == True:
            print("inserted successfully")
            ope.selectQuery()
            ope.selectWhere(2)

        else:
            print("Record not inserted")
