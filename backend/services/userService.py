from database.connect import connect
from datetime import datetime
from models.User import User
from psycopg2 import sql

def insert(username, password):
    try:
        conn = connect()
        cur = conn.cursor()
        
        insert_query = sql.SQL(
            "INSERT INTO users (username, password) VALUES (%s, %s)"
        )
        cur.execute(insert_query, (username, password))
        conn.commit()
        cur.close()
        conn.close()
        
        return User(username, password).to_dict()
    except Exception as e:
        print(f"An error occurred: {e}")

def get(username, password):
    try:
        conn = connect()
        cur = conn.cursor()
        
        select_query = sql.SQL(
            "SELECT * FROM users WHERE username = %s AND password = %s"
        )
        cur.execute(select_query, (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        
        if user:
            return User(username, password).to_dict()
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None