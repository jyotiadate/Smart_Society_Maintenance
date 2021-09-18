import  mysql.connector

connection = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="root",
                                     database="Society_db")
class PayOpe:
    def show(self,no, pdate):
        sql = "insert into Pay_Maintenance(no,paid_date) values(%s,%s)"
        val = (no, pdate)
        cursor = connection.cursor()
        cursor.execute(sql, val)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Pay_Maintenance table")
        cursor.close()
        return True

    def selectQuery(self):
        cursor=connection.cursor()
        cursor.execute("select * from pay_maintenance")
        reult=cursor.fetchall()
        print(reult)

    def selectWhere(self,no):
        cursor=connection.cursor()
        a=(no,)
        cursor.execute("SELECT * FROM member_register WHERE no=%s",a)
        res=cursor.fetchall()
        print(res)
        return res
        # self.txt.insert(0.0, res)
        # self.txt.configure(state='disabled')
        #

    def update(self, pdate):
        # aa=amount
        # bb=No1
        cursor = connection.cursor()
        sql = "update set_maintenance set paid_date=%s where no=%s"
        val = (pdate)
        cursor.execute(sql, val)
        connection.commit()
        return







