import mysql.connector

def DataUpdate(Name,pizza,mobile_no):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root@localhosy",
        passwd="root",
        database="mydatabase"
    )
    mycursor= mydb.cursor()
    # sql="CREATE TABLE CUSTOMERS(Name VARCHAR(255),pizza VARCHAR(255),mobile_no INT)"
    sql='INSERT INTO CUSTOMERS(Name,pizza,mobile_no) VALUES ("{0}","{1}","{2}");'.format(Name,pizza,mobile_no)

    mycursor.commit()
    
    print(mycursor.rowcount,"record inserted")


if if __name__ == "__main__":
    DataUpdate("Anish","Margharita","7858585858")
