# Omar Khaled 
import sqlite3  
from leaksfinder import LeaksFinder

class Database(LeaksFinder):        
        
    def __init__(self):
        
        
        
        pass
        
        
        
    def DBConnect(self, DatabaseName):
        self.__conn = sqlite3.connect(f'{DatabaseName}.db')
        self.__cursor = self.__conn.cursor()
        
    
    def Search(self):
        table = self.__cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()[0][0]
        self.__cursor.execute(f'SELECT * from {table}')
        column = self.__cursor.description[0][0]
        query = f"SELECT {column} FROM {table} WHERE {column}='{self.GetSearchKey}'"
        self.__cursor.execute(query)
        
        try:
            result = self.__cursor.fetchall()[0][0]
            if self.GetSearchKey in str(result):
                return True
            
        except:
            return False
        
    @property
    def Disconnect(self):
        self.__conn.close()










# |SearchKey|Result|Sources|LastSearch|RiskLevel

# def insert_data(table_name, data1):
#     cursor.execute(f"insert into {table_name} values('{data1}');")


# def add_row(history, main, value):
#     cursor.execute(f" insert into {history} select num from {main} where num='2{value}';")


# def exist(table_name, value):
#     return cursor.execute(f"Select * from {table_name} where num = '+2{value}';").fetchone() is not None


# def search(history, main, value):
#     if exist(history, value):
#         return 1
#     if exist(main, value):
#         add_row(history, main, value)
#         return 1
#     return 0


# def insert_data_file(filename, table_name):
#     with open(filename) as f:
#         file_data = f.readlines()
#         [insert_data(table_name, value[value.find('+'):value.find('"+')+15].strip('"')) for value in file_data]


# def show_result(table_name):
#     print(cursor.execute(f"Select * from {table_name} ;").fetchall())
