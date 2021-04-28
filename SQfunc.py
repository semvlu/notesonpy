import sqlite3
def newdata(id,name,sms):
    conn= sqlite3.connect("0421.db")
    c=conn.cursor()
    c.execute("insert into books values(?,?,?)",(id,name,sms))
    conn.commit()
    conn.close()
def newdata1(list):
    conn= sqlite3.connect("0421.db")
    c=conn.cursor()
    c.executemany("insert into books values(?,?,?)",(list)) #execute many
    conn.commit()
    conn.close()
def delete(id):
    conn= sqlite3.connect("0421.db")
    c=conn.cursor()
    c.executemany("delete from books where id=(?)",(id))
    conn.commit()
    conn.close()
def update(id):
    conn= sqlite3.connect("0421.db")
    c=conn.cursor()
    c.executemany("update books set name='Hello World' where id=(?)",(id))
    conn.commit()
    conn.close()
def read():
    conn= sqlite3.connect("0421.db")
    c=conn.cursor()
    c.execute("select * from books")
    all=c.fetchall()
    print(all)
    conn.commit()
    conn.close()
