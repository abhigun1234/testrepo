import sqlite3
connection=sqlite3.connect('data.db')
cursor=connection.cursor()
'''
create_table="CREATE TABLE  users(id int,username text,password text)"
cursor.execute(create_table)'''
user=(1,'abhishek','123456')
insert_query="insert into users values(?,?,?)"
cursor.execute(insert_query,user)
select_query='select * from users'
data=cursor.execute(select_query)
print(data)
for i in data :
    print(i[0])