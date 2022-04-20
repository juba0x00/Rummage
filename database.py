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




