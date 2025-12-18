import sqlite3



conn=sqlite3.connect("hospital.db")
cursor=conn.cursor()

cursor.execute("""
create table if not exists hospital_user(
    username text,
    password text
)
""")
conn.commit()
print("#################")
username = input("Enter your username: ")
password = input("enter your password: ")

cursor.execute("insert into hospital_user(username,password)values(?,?)",(username,password))
conn.commit()
print("data inserted successful")
conn.close()
