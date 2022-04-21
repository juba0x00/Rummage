from datetime import date 
from requests import get, session, post
from bs4 import BeautifulSoup
from json import loads, dump

class LeaksFinder():
    __SearchKey = ""
    __SearchType = ""
    __Status = ""
    __Result = ""
    __Source = ""
    __RiskLevel = ""
    __LastSearch = date.today()
    
    
    def __init__(self, InputSearchKey, InputSearchType):
        LeaksFinder.__SearchKey = InputSearchKey
        LeaksFinder.__SearchType = InputSearchType
        
    def SetRiskLevel(self, NewValue):
        if self.__RiskLevel < NewValue:
            self.__RiskLevel = NewValue
        
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
    
    @staticmethod
    def AddResult(NewResult):
        if NewResult not in LeaksFinder.__Result:
            LeaksFinder.__Result += NewResult + '\n'
    
    
    @property    
    def GetResult(self):
        return self.__Result
        
        
    @staticmethod
    def AddStatus(NewStatus):
        LeaksFinder.__Status += NewStatus + '\n'
    
    @property 
    def GetStatus(self):
        return self.__Status
    
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
        

