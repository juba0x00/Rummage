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
from requests import get
from abc import ABCMeta
from bs4 import BeautifulSoup

class Internet(metaclass=ABCMeta):
    def __init__(self, InputSearchKey):
        self.__Result = ""
        self.__Status = ""
        self.__SearchKey = InputSearchKey
        self.__RiskLevel = "" 
        self.__LastBreach = ""
        self.__Source = ""

    def Search(self):
        pass

    def SetRiskLevel(self, NewValue):
        if self.__RiskLevel < NewValue:
            self.__RiskLevel = NewValue
        
    @property
    def GetRiskLevel(self):
        return self.__RiskLevel
    
    
    def SetLastBreach(self, NewValue):
        if self._LastBreach < NewValue:
            self._LastBreach = NewValue
    
    def AddSource(self, NewSource):
        if not NewSource in self.__Source:
            self.__Source += NewSource + '\n' 
        
    def AddResult(self, NewResult):
        if not NewResult in self.__Result:
            self.__Result += NewResult + '\n'
        
    def AddStatus(self, NewStatus):
        self.__Status += NewStatus + '\n'
    
    @property
    def GetSearchKey(self):
        return self.__SearchKey
    
    def SetLastBreach(self, NewBreach):
        self.__LastBreach = NewBreach
        
    @property
    def GetLastBreach(self):
        return self.LastBreach
    
    @property
    def CheckConnection(self):
        URLs = ['http://google.com', ]
        for URL in URLs:
            if get(URL):
                return True
        return False