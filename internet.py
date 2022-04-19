# Hawash
# class Methods:
# Search
# Connect
# CheckConnection
# DetectDataFormat
# PlainTextSearch
# PdfSearch
# class attributes:
# Result
# Status
from requests import get, session
from abc import ABCMeta
from bs4 import BeautifulSoup
from json import loads, dump

class Internet(metaclass=ABCMeta):
    
    def __init__(self, InputSearchKey, InputSearchType):
        Internet.__SetSearchKey(InputSearchKey)
        Internet.__SearchType = InputSearchType
        self.__Result = ""
        self.__Status = ""
        self.__RiskLevel = "" 
        self.__LastBreach = ""
        self.__Source = ""

    @staticmethod
    def __SetSearchKey(SearchKey):
        Internet.__SearchKey = SearchKey
        
    

    def SetRiskLevel(self, NewValue):
        if self.__RiskLevel < NewValue:
            self.__RiskLevel = NewValue
        
    @property
    def GetRiskLevel(self):
        return self.__RiskLevel
    
    
    def SetLastBreach(self, NewValue):
        if self._LastBreach < NewValue:
            self._LastBreach = NewValue
    
    @property
    def GetLastBreach(self):
        return self.__LastBreach
    
    def AddSource(self, NewSource):
        if not NewSource in self.__Source:
            self.__Source += NewSource + '\n' 
    
    @property 
    def GetSources(self):
        return self.__Source
    
    def AddResult(self, NewResult):
        if NewResult not in self.__Result:
            self.__Result += NewResult + '\n'
    
    
    @property    
    def GetResult(self):
        return self.__Result
        
    def AddStatus(self, NewStatus):
        self.__Status += NewStatus + '\n'
    
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
    
    @property 
    def GetCountry():
        return get('https://am.i.mullvad.net/country').text.replace('\n', '')
        
        
finder = Internet('ewida@mgila.com', 'tshlk')
