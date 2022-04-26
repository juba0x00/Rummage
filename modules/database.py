import sqlite3  
from modules.leaksfinder import LeaksFinder

from datetime import timedelta,datetime

class Database():  
        
    def __init__(self):
        pass
        
    def __DBConnect(self, DatabaseName):
        self.__conn = sqlite3.connect(f'{DatabaseName}.db')
        self.__cursor = self.__conn.cursor()

    
    def Search(self, DatabaseName):
        print(DatabaseName)
        self.__DBConnect(DatabaseName) 
        try:
            table = self.__cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()[0][0]
            print(f'table -> {table}')
        except:
            return False
        
        column = self.__cursor.execute(f"PRAGMA table_info({table})").fetchall()[0][1]  # ! 0|col1|INTEGER|1||1
        
        print(f'col name {column}')
        test = LeaksFinder.GetSearchKey()
        print(f'tesst -> {test}')
        query = f"SELECT {column} FROM {table} WHERE {column}={test}"
        self.__cursor.execute('select * from Visa')
        self.__cursor.fetchall()
        
        
        # try:
        
        #     result = self.__cursor.fetchall()  # ! TODO search for solution 
        #     print(f'result -> {result}')
        
        #     if LeaksFinder.GetSearchKey in str(result):
        #         LeaksFinder.AddResult('found ksdfjlskjdfkls')
        #         return True
        # except :
        
        #     LeaksFinder.AddResult('not found')
        #     return False
        
        # finally:
        #     self.__cursor.close()
        
    
    
    def InsertRecord(self, Values): # ? Values is a list 
        self.__DBConnect('databases/History')
        self.__cursor.execute(f"INSERT INTO History VALUES('{Values[0]}', '{Values[1]}', '{Values[2]}', '{Values[3]}', '{Values[4]}')")
        self.__conn.commit()
        self.__conn.close()


    def HistorySearch(self):
        self.__DBConnect('{}History'.format(LeaksFinder.FileSystemStructure()))
        self.__cursor.execute("SELECT * FROM History WHERE SearchKey='{}'".format(LeaksFinder.GetSearchKey()))
        try:
            row = self.__cursor.fetchall()[0]
        except:
            return False
        
        if LeaksFinder.GetSearchKey() in row[0]:
            LeaksFinder.AddResult(row[1])
            LeaksFinder.AddSource(row[2])
            LeaksFinder.SetLastSearch(row[3])
            LeaksFinder.SetRiskLevel(row[4])
            self.__conn.close()
            return True
        else:
            return False
        
        
    @staticmethod
    def TrustHistory():
        today = str(datetime.today())
        d1 = datetime.strptime(str(LeaksFinder.GetLastSearch()), "%Y-%m-%d")
        d2 = datetime.strptime(str(today)), "%Y-%m-%d"
        return abs((d2 - d1).days) < 30


# |SearchKey|Result|Sources|LastSearch|RiskLevel
# 
# ! CREATE TABLE History(SearchKey VARCHAR(50) PRIMARY KEY, Result VARCHAR(10000), Sources VARCHAR(10000), LastSearch date, RiskLevel INT )