import psycopg2
from psycopg2 import OperationalError

def create_conn(db_name,db_user,db_pass,db_host,db_port):
    conn=None
    try:
        conn=psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
        )
        print("Connection to postgresql Successfull")
    except OperationalError as e:
        print(f"error '{e} occured")

    return conn

def create_query(conn,query):
    conn.autocommit=True
    cursor=conn.cursor()
    try:
        cursor.execute(query)
        print("query successfully")
    except OperationalError as e:
        print( f"error '{e} occured")

create_table="""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    location TEXT
    )
    """

users=[

    ('Jamie',25,'M','US'),
    ('Liss',66,'F','US'),
    ('Tom',22,'M','FR'),
    ('Megan',18,'F','US'),
    ('Londy',54,'F','PL'),
]

users_records=', '.join(["%s"]* len(users))

insert_query=( f"INSERT INTO users (name,age,gender,location) VALUES {users_records}")

if __name__ == "__main__":

    connection=create_conn("postgres","postgres","abc123","127.0.0.1","5432")
    create_base_query="CREATE DATABASE db_app"
   # create_query(connection,create_base_query)
    create_query(connection,create_table)

    create_query(connection,insert_query)
