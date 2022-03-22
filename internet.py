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
        self.Result = ""
        self.Status = ""
        self.SearchKey = InputSearchKey
        self.RiskLevel = "" 
        self.LastBreach = "" 

    def Search(self):

        # GET /unifiedsearch/#!Search_key HTTP/2
        # Host: haveibeenpwned.com
        # User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0
        # Accept: */*
        # Accept-Language: en-US,en;q=0.5
        # Accept-Encoding: gzip, deflate
        # Referer: https://haveibeenpwned.com/
        # X-Requested-With: XMLHttpRequest
        # Request-Id: |xJMBl./ogp
        # Request-Context: appId=cid-v1:bcc569a3-d364-4306-8bbe-83e9fe4d020e
        # Sec-Fetch-Dest: empty
        # Sec-Fetch-Mode: cors
        # Sec-Fetch-Site: same-origin
        # Te: trailers
        pass


    def SetRiskLeve(self, NewValue):
        if self.__RiskLevel < NewValue:
            self.__RiskLevel = NewValue
        
    
    def SetLastBreach(self, NewValue):
        if self.__LastBreach < NewValue:
            self.__LastBreach = NewValue
    
    
    @property
    def CheckConnection(self):
        URLs = ['http://google.com', ]
        for URL in URLs:
            if get(URL):
                return True

        return False

    @property
    def GetSoup(self):
        return BeautifulSoup(get(self.__target).content, "lxml")

    def DetectDataFormat(self):
        pass

    def PlainTextSearch(self):
        pass

    def PdfSearch(self):
        pass

    @property
    def GetResult(self):
        return self.__Result
