# Omar Khaled 
import sqlite3 as sql 
class Database:        
        
    def search(self, DatabaseName, SearchKey):
        conn = sql.connect(DatabaseName)
        cursor = conn.cursor()
        table = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()[0][0]
        cursor.execute(f'select * from {table}')
        column = cursor.description[0][0]

        query = f"SELECT {column} from {table} WHERE {column}='{SearchKey}'"
        cursor.execute(query)
        try:
            result = cursor.fetchall()[0][0]
        except:
            return False
        conn.close()
        if SearchKey in str(result):
            return True 
        else:
            return False



db = Database()
print(db.search('PayLeaks.sqlite', '41004-70360'))
