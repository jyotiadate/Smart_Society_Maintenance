import mysql.connector
connection = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="root",
                                     database="Society_db")

class operation:


    def show(self,no1, am1, de1, paid1by, paid):
        sql = "insert into Pay_Expenses(Eno,amt,description,paid_by,paid_date) values(%s,%s,%s,%s,%s)"
        val = (no1, am1, de1, paid1by, paid)
        cursor = connection.cursor()
        cursor.execute(sql, val)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Pay_Expenses table")
        cursor.close()
        return True

    # def selectQuery(self):
    #     cursor=connection.cursor()
    #     cursor.execute("select * from Pay_Expenses")
    #     reult=cursor.fetchall()
    #     print(reult)

    def selectWhere(self,no1):
        cursor=connection.cursor()
        a=(no1,)
        cursor.execute("select * from member_register where no=%s",(a))
        res=cursor.fetchall()
        print(res)
        return res



    # def close(self):
    #     self.root.destroy()

    # def select(self):
    #
    #     no1 = self.No.get()
    #     print(no1)
    #
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT * FROM member_register WHERE No='%s'" % (self.No.get()))
    #     result = cursor.fetchone()
    #     print(result)
    #     self.txt.insert(0.0, result)
    #     self.txt.configure(state='disabled')



'''    def select(self):
        cursor = mydb.cursor()
        #cursor.execute("SELECT * FROM MVC WHERE no='%s'" % (self.No1.get()))
        cursor.execute("SELECT * FROM MVC WHERE no=101")
        select = cursor.fetchone()
        print(select)'''

'''
def update():
    cursor = mydb.cursor()
    cursor.execute(" update mvc set address= where no=101")
    update = cursor.fetchone()
    print(update)'''


