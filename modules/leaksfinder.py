from bs4 import BeautifulSoup
from requests import get 
from sys import platform 
from os import getcwd, stat
from datetime import date
RED = '\033[93m'
YELLOW = '\033[33m'
UNDERLINE = '\033[4m'
CYAN = '\033[36m'
GREEN = '\033[32m'
RESET = '\033[0m'
BOLD = '\033[1m'
HEADER = '\033[95m'


class LeaksFinder():
    __SearchKey = ""
    __SearchType = ""
    __Status = ""
    __Result = ""
    __Source = " "
    __RiskLevel = 0
    __LastSearch = date.today()
    __CWD = getcwd()
    
    
    
    
    @staticmethod
    def SetAtrrs(InputSearchKey, InputSearchType):
        LeaksFinder.__SearchKey = InputSearchKey
        LeaksFinder.__SearchType = InputSearchType
        
        
    @staticmethod
    def IncreaseRiskLevel():
        LeaksFinder.__RiskLevel += 1
        
        
    @staticmethod
    def GetRiskLevel():
        return LeaksFinder.__RiskLevel
    
    
    @staticmethod
    def SetLastSearch(NewValue):
        LeaksFinder.__LastSearch = NewValue
    
    
    @staticmethod
    def SetRiskLevel(NewValue):
        LeaksFinder.__RiskLevel = NewValue
        
        
    @staticmethod
    def GetLastSearch():
        return LeaksFinder.__LastSearch
    
    
    @staticmethod
    def AddSource(NewSource):
        LeaksFinder.__Source += NewSource + '\n' 
    
    
    @staticmethod
    def GetSources():
        return LeaksFinder.__Source
    
    
    @staticmethod
    def AddResult(NewResult):
        if NewResult not in LeaksFinder.__Result:
            LeaksFinder.__Result += NewResult + '\n'
    
    
    def GetResult():
        return LeaksFinder.__Result
        
        
    @staticmethod
    def AddStatus(NewStatus):
        if str(NewStatus).startswith('[*]'):
            print(HEADER + '___________________________________________\n' + BOLD + GREEN + NewStatus + RESET)
        elif str(NewStatus).startswith('[+]'):
            print(YELLOW + UNDERLINE + NewStatus + RESET)
        else:
            print(CYAN + NewStatus  + RESET)
            
        LeaksFinder.__Status += NewStatus + '\n'
        
    
    @staticmethod
    def GetStatus():
        return LeaksFinder.__Status
    
    
    @staticmethod
    def GetSearchKey():
        return LeaksFinder.__SearchKey
    
    
    @staticmethod 
    def GetSearchType():
        return LeaksFinder.__SearchType
    
    
    @staticmethod
    def FileSystemStructure():
        if platform == 'Linux' or platform == 'linux' or platform == 'Darwin':
            return f'{LeaksFinder.__CWD}/databases/'
        elif platform == 'win32' or platform == 'windows':
            return f'{LeaksFinder.__CWD}\databases'   
        else:
            # ! show error winow 
            pass