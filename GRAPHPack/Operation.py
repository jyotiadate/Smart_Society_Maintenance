import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="root",
                                         database="Smart_Society_db")
class Operator:
    def show(self):
        re = mydb.cursor()
        re.execute("select month(date),year(date) from Income  where year(date)")
        res = re.fetchall()
        print(res)
        re.execute("select count(*) from income")
        result = re.fetchall()
        print(result)
