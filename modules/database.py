import sqlite3
from modules.leaksfinder import LeaksFinder

from datetime import timedelta,datetime

class Database():  
        
    def _init_(self):
        pass
        
    def __DBConnect(self, DatabaseName):
        self.__conn = sqlite3.connect(f'{DatabaseName}.db')
        self.__cursor = self.__conn.cursor()

    
    def Search(self, DatabaseName) :
        
        self.__DBConnect(DatabaseName) 

        table = self.__cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()[0][0]
        column = self.__cursor.execute(f"PRAGMA table_info({table})").fetchall()[0][1] #!0col1|INTEGER|1||1
        key = LeaksFinder.GetSearchKey()
        
        query = f"SELECT * FROM {table} WHERE {column}='{key}'"
        result = self.__cursor.execute(query).fetchall()
        
        if len(result) != 0:
            LeaksFinder.AddResult('Breaches found')
            return True
        else:
            LeaksFinder.AddResult('No Breaches found')
            return False
        
        
    
    def InsertRecord(self, Values): # ? Values is a list 
        self.__DBConnect('databases/History')
        self.__cursor.execute(f"INSERT INTO History VALUES('{Values[0]}', '{Values[1]}', '{Values[2]}', '{Values[3]}', '{Values[4]}')")
        self.__conn.commit()
        self.__conn.close()


    def HistorySearch(self):
        self.__DBConnect('{}History'.format(LeaksFinder.FileSystemStructure()))
        self.__cursor.execute("SELECT * FROM History WHERE SearchKey ='{}'".format(LeaksFinder.GetSearchKey()))
        
        
        try:
            result = self.__cursor.fetchall()[0]
        except:
            return False
        
        if len(result) != 0:
            LeaksFinder.AddResult(result[1])
            LeaksFinder.AddSource(result[2])
            LeaksFinder.SetLastSearch(result[3])
            LeaksFinder.SetRiskLevel(result[4])
            return True
        else:
            LeaksFinder.AddResult("Not Found")
            return False

    @staticmethod
    def TrustHistory():
        # d1 = datetime.strptime(str( LeaksFinder.GetLastSearch() ), "%Y-%m-%d")
        # d2 = datetime.strptime(str( datetime.today() ), "%Y-%m-%d")


        return  True #abs((d2 - d1).days) < 30


# |SearchKey|Result|Sources|LastSearch|RiskLevel
# 
# ! CREATE TABLE History(SearchKey VARCHAR(50) PRIMARY KEY, Result VARCHAR(10000), Sources VARCHAR(10000), LastSearch date, RiskLevel INT )
