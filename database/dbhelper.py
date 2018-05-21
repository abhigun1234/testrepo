__author__ = 'AG00341558'
import psycopg2
conn = psycopg2.connect(database = "institutedb", user = "postgres", password = "123456", host = "127.0.0.1", port = "5432")
cur = conn.cursor()

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

allCourses()
print ("Operation done successfully");
