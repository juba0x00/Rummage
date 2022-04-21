# Omar Khaled 
import sqlite3 as sql 
class Database:        
        
    def search(self, DatabaseName, SearchKey):
        conn = sql.connect(DatabaseName)
        cursor = conn.cursor()
        table = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()[0][0]
        cursor.execute(f'select * from {table}')
        column = cursor.description[0][0]

        query = f"SELECT {column} FROM {table} WHERE {column}='{SearchKey}'"
        cursor.execute(query)
        conn.close()
        
        
        try:
            result = cursor.fetchall()[0][0]
            if SearchKey in str(result):
                return True
            
        except:
            return False


#Egypt
import sqlite3 as sql
conn = sql.connect('Leaks.db')
cursor = conn.cursor()


def create_table(table_name, attr):
    cursor.execute(f"Create table {table_name} ({attr}); ")


def insert_data(table_name, data1):
    cursor.execute(f"insert into {table_name} values('{data1}');")


def add_row(history, main, value):
    cursor.execute(f" insert into {history} select num from {main} where num='+2{value}';")


def exist(table_name, value):
    return cursor.execute(f"Select * from {table_name} where num = '+2{value}';").fetchone() is not None


def search(history, main, value):
    if exist(history, value):
        return 1
    if exist(main, value):
        add_row(history, main, value)
        return 1
    return 0


# def insert_data_file(filename, table_name):
#     with open(filename) as f:
#         file_data = f.readlines()
#         [insert_data(table_name, value[value.find('+'):value.find('"+')+15].strip('"')) for value in file_data]


# def show_result(table_name):
#     print(cursor.execute(f"Select * from {table_name} ;").fetchall())
