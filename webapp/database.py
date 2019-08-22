import mysql.connector
import sys

try:
    f=open("person.txt","r")
    contents=f.readline().strip()


    u='assignmentuser';pw='dmitiot';
    h='localhost';db='assignmentdatabase'

    cnx = mysql.connector.connect(user=u,password=pw,host=h,database=db) 
    cursor = cnx.cursor()
    print("Successfully connected to database!")

    sql = "INSERT INTO person (number_of_people) VALUES (%(number)s);"
    cursor.execute(sql, {'number':contents})

    cnx.commit()
     
except:
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    
