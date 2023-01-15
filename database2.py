import pymysql as p
def getconnection():
    return p.connect(host="localhost",user="root",password="",database="hospital1")

def adddata(t):   
    con=getconnection()
    cur=con.cursor()
    query4="insert into appointment(name,email,dname,doa,toa,branch)values(%s,%s,%s,%s,%s,%s)"
    
    cur.execute(query4,t)
    con.commit()
    con.close()


def fetchdata():
    con=getconnection()
    cur=con.cursor()
    cur.execute("select * from appointment")
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist 


def specificdata(id):
    con=getconnection()
    cur=con.cursor()
    cur.execute("select * from appointment where id=%s",(id,))
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist[0]


def updatedata(t):
    con=getconnection()
    cur=con.cursor()
    query5="update appointment  set name=%s, email=%s,dname=%s,doa=%s where id=%s"
    cur.execute(query5,t)
    con.commit()
    con.close()


def deletedata(id):
    con=getconnection()
    cur=con.cursor()
    query6="delete from appointment where id=%s"
    cur.execute(query6,(id))
    con.commit()
    con.close()