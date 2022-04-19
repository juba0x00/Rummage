# Omar Khaled 
import sqlite3
class Database:


# table -> PayLeaks_Sheet1
# PayLeaks 


# table -> Egypt 
# Username 


    def __init__(self, DatabaseName):
        self.DB_Connection = sqlite3.connect(DatabaseName)
        
        
    def search(self, SearchKey):
        cursor = self.DB_Connection.cursor()
        table = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        print(type(table))
        # query = f"SELECT {col} FROM {table} WHERE {col} = {SearchKey}"
        # cursor.execute(query)
        # result = cursor.fetchall()
        




db = Database('PayLeaks.sqlite', )
db.search('41003-91030')
