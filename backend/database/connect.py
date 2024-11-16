import env.dev as dev
import psycopg2

def connect():
    conn = psycopg2.connect(
        dbname=dev.dbname,
        user=dev.user,
        password=dev.password,
        host=dev.host,
        port=dev.port
    )
    return conn