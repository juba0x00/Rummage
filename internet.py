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
from abc import ABCMeta, abstractclassmethod
from bs4 import BeautifulSoup
from datetime import date
class Internet(metaclass=ABCMeta):
    
    @abstractclassmethod
    def __init__(self, InputSearchKey):
        self.__Result: str
        self.__Status: str
        self.__RiskLevel: str 
        self.__Source: str
        self.__LastBreach: date
        self.__SearchKey = InputSearchKey
        

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
    def GetSource(self):
        return self.__Source
        
    def AddResult(self, NewResult):
        if not NewResult in self.__Result:
            self.__Result += NewResult + '\n'
        
        
    @property 
    def GetResult(self):
        return self.__Result
    
    
    def AddStatus(self, NewStatus):
        self.__Status += NewStatus + '\n'
    
    @property 
    def GetStatus(self):
        return self.__Status
    
    def SetSearchKey(self, NewKey):
        self.__SearchKey = NewKey
        
    @property
    def GetSearchKey(self):
        return self.__SearchKey       

    
    @property
    def CheckConnection(self):
        URLs = ['http://google.com', 'http://youtube.com']
        for URL in URLs:
            if get(URL):
                return True
        
        return False
            
