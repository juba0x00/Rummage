from datetime import date 
from bs4 import BeautifulSoup
from requests import get 

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
    __Source = ""
    __RiskLevel = 0
    __LastSearch = date.today()
    
    
    @staticmethod
    def SetAtrrs(InputSearchKey, InputSearchType):
        LeaksFinder.__SearchKey = InputSearchKey
        LeaksFinder.__SearchType = InputSearchType
        
        
    @staticmethod
    def IncreaseRiskLevel():
        LeaksFinder.__RiskLevel += 1
        
    
    def GetRiskLevel():
        return LeaksFinder.__RiskLevel
    
    
    def SetLastSearch(self, NewValue):
        if self._LastSearch < NewValue:
            self._LastSearch = NewValue
    
    
    def GetLastSearch():
        return LeaksFinder.__LastSearch
    
    
    @staticmethod
    def AddSource(NewSource):
        LeaksFinder.__Source += NewSource + '\n' 
    
    
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
        

