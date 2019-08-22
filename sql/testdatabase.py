import mysql.connector
import sys

try:
    u='root';pw='1qwer$#@!';
    h='gungnir-249212:us-central1:iotsql';db='testdatabase'

    cnx = mysql.connector.connect(user=u,password=pw,host=h,database=db) 
    cursor = cnx.cursor()
    print("Successfully connected to database!")

    cnx.commit()
     
except:
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    
