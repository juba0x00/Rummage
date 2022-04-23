from datetime import date 
from bs4 import BeautifulSoup
from requests import get 
from os import getcwd

RED = '\033[31m'
YELLOW = '\033[33m'
UNDERLINE = '\033[4m'
CYAN = '\033[36m'
GREEN = '\033[32m'
RESET = '\033[0m'


class LeaksFinder():
    __SearchKey = ""
    __SearchType = ""
    __Status = ""
    __Result = ""
    __Source = ""
    __RiskLevel = 0
    __LastSearch = date.today()
    
    
    def SetAtrrs(InputSearchKey, InputSearchType):
        LeaksFinder.__SearchKey = InputSearchKey
        LeaksFinder.__SearchType = InputSearchType
        
    def IncreaseRiskLevel(self, n=1):
        self.__RiskLevel += n
        
    @property
    def GetRiskLevel(self):
        return self.__RiskLevel
    
    
    def SetLastSearch(self, NewValue):
        if self._LastSearch < NewValue:
            self._LastSearch = NewValue
    
    @property
    def GetLastSearch(self):
        return self.__LastSearch
    
    def AddSource(self, NewSource):
        # if not NewSource in self.__Source:
        self.__Source += NewSource + '\n' 
    
    
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
            print(GREEN + NewStatus + RESET)
        elif str(NewStatus).startswith('[+]'):
            print(YELLOW + UNDERLINE + NewStatus + RESET)
        else:
            print(CYAN + NewStatus  + RESET)
            
        LeaksFinder.__Status += NewStatus + '\n'
        
    
    
    def GetStatus():
        return LeaksFinder.__Status
    
    @property
    def GetSearchKey(self):
        return self.__SearchKey
    
    @property 
    def GetSearchType(self):
        return self.__SearchType

    @property
    def CheckConnection(self):
        URLs = ['http://google.com', ]
        for URL in URLs:
            if get(URL):
                return True
        return False
    
    
    def GetCountry():
        return get('https://am.i.mullvad.net/country').text.replace('\n', '')
        

