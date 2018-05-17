__author__ = 'AG00341558'
from  database import *

courselist=[]

def allCourses():
    cur.execute("SELECT * from COURSES")
    rows = cur.fetchall()
    for row in rows:
       print( "ID = ", row[0])
       print ("NAME = ", row[1])
       print( "Fees = ", row[2])
       print ("duration = ", row[3], "\n")
       course={"id":row[0],"name":row[1],"duration":row[2]}
       courselist.append(course)
       print(courselist)
    conn.close()
    return courselist


print ("Operation done successfully");
