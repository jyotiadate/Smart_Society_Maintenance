import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="jyotiadate",
                                         database="Society_db")

class operator:

    def show(self,mee,mpur,mdes):
        sql = "insert into meeting(date,purpose,des) values(%s,%s,%s)"
        val = (mee,mpur,mdes)
        cursor = mydb.cursor()
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "Record inserted successfully into meeting table")
        cursor.close()
        return True


    def close(self):
        self.root.destroy()

    def selectQuery(self):
        cursor=mydb.cursor()
        cursor.execute("select * from meeting")
        reult=cursor.fetchall()
        print(reult)

    def selectWhere(self,No):
        cursor=mydb.cursor()
        cursor.execute("select * from meeting where ='%s' +(")
        res=cursor.fetchall()
        print(res)




