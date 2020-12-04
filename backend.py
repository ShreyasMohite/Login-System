import sqlite3

def Logins():
    conn=sqlite3.connect("Login")
    cur=conn.cursor()
    cur.execute("create table if not exists login_info(id integer primary key,email text,password text)")
    conn.commit()
    conn.close()
    
def add_login(email,password):
    conn=sqlite3.connect("Login")
    cur=conn.cursor()
    cur.execute("insert into login_info values(null,?,?)",(email,password))
    conn.commit()
    conn.close()
    
def view_login():
    conn=sqlite3.connect("Login")
    cur=conn.cursor()
    cur.execute("select * from login_info")
    row=cur.fetchall()
    conn.close()
    return row


def delete_login(id):
    conn=sqlite3.connect("Login")
    cur=conn.cursor()
    cur.execute("delete from login_info where id=?",(id,))
    conn.commit()
    conn.close()

def update_login(id,email=" ",password=" "):
    conn=sqlite3.connect("Contact")
    cur=conn.cursor()
    cur.execute("select * from contact_info where name=? or number=?",(email,password,id))
    conn.commit()
    conn.close()




Logins()

