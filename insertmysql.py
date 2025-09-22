from mysql.connector import MySQLConnection, Error
#from config import read_config
from mysql import mysql

def insert_book(title, isbn):
    config = {
    "host": "10.221.93.147",
    "user": "root",
    "password": "lsuy0",
    "database": "orion",
}
    query = "INSERT INTO test(title,isbn) VALUES(%s,%s)"
    args = (title, isbn)
    book_id = None
    try:
        #config = read_config()
        with MySQLConnection(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, args)
                book_id =  cursor.lastrowid
            conn.commit()
        return book_id
    except Error as error:
        print(error)

if __name__ == '__main__':
    insert_book('A Sudden Light', '9781439187036')
