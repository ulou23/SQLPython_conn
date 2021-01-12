import sqlite3                      #serverless DB  Python SQL modules
from sqlite3 import Error

import os

def create_conn(path):
    conn=None
    try:
        conn=sqlite3.connect(path)
        print("connection successful")
    except Error as e:
        print("the error %s" % e)

    return conn



def exec_query(conn,query):
    cur=conn.cursor()
    try:
        cur.execute(query)
        conn.commit()
    except Error as e:
        print("the error %s" % e)

def exec_read_query(conn,query):
    cur=conn.cursor()
    result=None
    try:
        cur.execute(query)
        result=cur.fetchall()
        return result
    except Error as e:
        print("the error %s" % e)



create_users_table=("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    location TEXT
    );
    """)

create_posts_table=("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    content TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """ )

create_users=("""
INSERT INTO users (name,age,gender,location)
VALUES
('Jamie',25,'M','US'),
('Liss',66,'F','US'),
('Tom',22,'M','FR'),
('Megan',18,'F','US'),
('Londy',54,'F','PL'),
""" )

create_posts=("""
INSERT INTO
posts (title,content,user_id)
VALUES
("abc","love is love",1),
("ab","lo love",2),
("abqqq","we lo love",2),
("abwww","lo awerlove",4),
("asdab","nopelo love",3),
""" )


if __name__ == "__main__":
    path_to_sqlite=os.path.join(os.path.dirname(__file__),'databasesql.sqlite3')
    connection=create_conn(path_to_sqlite)
    exec_query(connection,create_users_table)
    exec_query(connection,create_posts_table)
    exec_query(connection,create_users)
    exec_query(connection,create_posts)

    select_user="SELECT * from users"
    users=exec_read_query(connection,select_user)

    for user in users:
        print(user)