import mysql.connector
connection=mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="root",
                                       database="")
class operator:

    def show(self,no,dt1,name,email,dob,gender,mobno,ty,square):

        sql="insert into member_register(no,date,name,email,date_of_birth,gender,mob_no,type,sq_ft) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(no,dt1,name,email,dob,gender,mobno,ty,square)
        cursor = connection.cursor()
        cursor.execute(sql,val)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into member_register table")
        cursor.close()
        return True

    def selectQuery(self):
        cursor=connection.cursor()
        cursor.execute("select * from member_register")
        reult=cursor.fetchall()
        print(reult)

    def selectWhere(self,No):
        cursor=connection.cursor()
        cursor.execute("select * from member_register where no=''")
        res=cursor.fetchall()
        print(res)

    def coun(self):
        cursor = connection.cursor()
        cursor.execute("select count(*) from member_register")
        res = cursor.fetchall()
        aa=res+1
        print(aa,"dgfghj")
        return aa