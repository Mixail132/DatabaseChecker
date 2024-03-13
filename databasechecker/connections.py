import psycopg2

connect = psycopg2.connect(
    database="restored_itcoty",
    user="postgres",
    password="PostgresMixail132",
    host="localhost",
    port="5432"
)

cursor = connect.cursor()