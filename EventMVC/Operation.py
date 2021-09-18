import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="root",
                                         database="Smart_Society_db")

class operator:

    def show(self,Eno,dt,pur,cost,fdate,tdate):
        sql = "insert into event(no,date,purpose,cost,f_date,t_date) values(%s,%s,%s,%s,%s,%s)"
        val = (Eno,dt,pur,cost,fdate,tdate)
        cursor = mydb.cursor()
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "Record inserted successfully into event table")
        cursor.close()
        return True

    def selectQuery(self):
        cursor=mydb.cursor()
        cursor.execute("select * from Event")
        reult=cursor.fetchall()
        print(reult)

    def selectWhere(self,):
        cursor=mydb.cursor()
        cursor.execute("select * from Event where no=''")
        res=cursor.fetchall()
        print(res)

    def count(self):
        cursor = mydb.cursor()
        cursor.execute("select count(*) from event")
        res = cursor.fetchall()
        aa = (str(res + 1))
        print(aa, "dgfghj")


    def close(self):
        self.root.destroy()

