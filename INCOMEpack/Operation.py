import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="jyotiadate",
                                         database="Society_db")

class operator:

    def show(self,incomeno,incomedt,purpose,amount,givenby):
        sql = "insert into Income(Ino,date,purpose,amt,given_by) values(%s,%s,%s,%s,%s)"
        val = (incomeno,incomedt,purpose,amount,givenby)
        cursor = mydb.cursor()
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "Record inserted successfully into Income table")
        cursor.close()
        return True


    def selectQuery(self):
        cursor=mydb.cursor()
        cursor.execute("select * from Income")
        reult=cursor.fetchall()
        print(reult)

    # def selectWhere(self,no1):
    #     aa=no1
    #     cursor=mydb.cursor()
    #     cursor.execute("select * from Income where Incomno=%s,aa" )
    #     res=cursor.fetchall()
    #     print(res)

    def close(self):
        self.root.destroy()





