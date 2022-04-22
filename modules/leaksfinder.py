from datetime import date 
from bs4 import BeautifulSoup
from requests import get 


class LeaksFinder():
    __SearchKey = ""
    __SearchType = ""
    __Status = ""
    __Result = ""
    __Source = ""
    __RiskLevel = 0
    __LastSearch = date.today()
    
    
    def __init__(self):
        pass
    
    
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
        if not NewSource in self.__Source:
            self.__Source += NewSource + '\n' 
    
    @property 
    def GetSources(self):
        return self.__Source
    
    

    def AddResult(self, NewResult):
        if NewResult not in LeaksFinder.__Result:
            LeaksFinder.__Result += NewResult + '\n'
    
    
    def GetResult():
        return LeaksFinder.__Result
        
        
    @staticmethod
    def AddStatus(NewStatus):
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
        

