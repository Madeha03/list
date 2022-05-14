import os
from datetime import datetime, timedelta
import pymysql
import json

DB_NAME='testdb'
DB_HOST='gamingdb.chlje3rkuefm.ap-south-1.rds.amazonaws.com'
DB_USER='admin'
DB_PASSWORD='z*V$H1JF%T'

def get_db():
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
    return conn



def time_now():
    """returns current timestamp"""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
"""
username="teja"
id=2

db= get_db()
try:
    with db.cursor() as cur:
        sql="SELECT * FROM users where id=%s"
        cur.execute(sql,(id))
        result= cur.fetchone()
        print(type(result))
        print(result)
finally:
    cur.close()
    db.close()
"""
def data(id):
    db= get_db()
    try:
        with db.cursor() as cur:
            sql="SELECT * FROM users where id=%s"
            cur.execute(sql,(id))
            result= cur.fetchone() #fetchall
            
    finally:
        cur.close()
        db.close()
    return result
t=data(4)
print(type(t))
print(t)
