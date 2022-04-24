# Omar Khaled 
import sqlite3  
from modules.leaksfinder import LeaksFinder

class Database(LeaksFinder):        
        
        
    def __DBConnect(self, DatabaseName):
        self.__conn = sqlite3.connect(f'{DatabaseName}.db')
        self.__cursor = self.__conn.cursor()

    
    def Search(self, DatabaseName):
        self.__DBConnect(DatabaseName) 
        try:
            table = self.__cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()[0][0]
            
        
        except:
            return False

        column = self.__cursor.description
        print(column)
        # query = f"SELECT {column} FROM {table} WHERE {column}='{self.GetSearchKey}'"
        # self.__cursor.execute(query)
        # self.__conn.close()
        # try:
        #     result = self.__cursor.fetchall()[0][0]
        #     if self.GetSearchKey in str(result):
        #         return True
        # except:
        #     return False
    
    
    def InsertRecord(self, Values): # ? Values is a list 
        self.__DBConnect('databases/History')
        self.__cursor.execute(f"INSERT INTO History VALUES('{Values[0]}', '{Values[1]}', '{Values[2]}', '{Values[3]}', '{Values[4]}')")
        self.__conn.commit()
        self.__conn.close()


    def HistorySearch(self):
        self.__DBConnect('{}History'.format(LeaksFinder.FileSystemStructure()))
        self.__cursor.execute(f"SELECT * FROM History WHERE SearchKey='{self.GetSearchKey}'")
        try:
            row = self.__cursor.fetchall()[0]
        except:
            return False
        
        if self.GetSearchKey in row[0]:
            self.AddResult(row[1])
            self.AddSource(row[2])
            self.SetLastSearch(row[3])
            self.SetRiskLevel(row[4])
            self.__conn.close()
            return True
        else:
            return False
    





# |SearchKey|Result|Sources|LastSearch|RiskLevel
# 
# ! CREATE TABLE History(SearchKey VARCHAR(50) PRIMARY KEY, Result VARCHAR(10000), Sources VARCHAR(10000), LastSearch date, RiskLevel INT )