# Hawash
#class Methods:
#		Search
#		Connect
#		CheckConnection
#		DetectDataFormat
#		PlainTextSearch
#		PdfSearch
#class attributes:
#		Result
#		Status 	
from requests import get
from abc import ABCMeta 
class Internet(metaclass=ABCMeta):
    def __init__(self):
        self.__Result = ""
        self.__Status = ""
    
    def Search(self):
        
        
        # GET /unifiedsearch/#!Search_key HTTP/2
        # Host: haveibeenpwned.com
        # Cookie: __cf_bm=L.F0IkFDPKxcBK9fHkO_08ZoucV7pSKnVSh17768Gbw-1647687439-0-AYp9iOrFfEnkTOz8JW8zYQ37j7cfQvAx3tQ/XmLvCxs7u4ldDhTSz74ePa2OO6KkgWFhHUUZtEOoUj8iEa/FIZtJCYQ2xN/49hJNg6+Ue4UHGzwMLsofVkT5iPjFYhbtqHaDBRaAb8kqiBtonHG6U2YhkaJWhfcKoarqUAUwLTWn; ai_user=jp2OF|2022-03-19T10:57:19.117Z; ai_session=5VxYu|1647687439289|1647687439289; _ga=GA1.2.515572655.1647687439; _gid=GA1.2.1255740366.1647687439; _gat=1
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
    
    @property
    def CheckConnection(self):
        URLs = ['http://google.com']
        for URL in URLs: 
            if get(URL):
                return True
            
        return False
            
    @property
    def Connect(target):
        return get(target)
        pass
    
    def DetectDataFormat(self):
        pass
    
    def PlainTextSearch(self):
        pass
    
    def PdfSearch(self):
        pass
    
    @property 
    def GetResult(self):
        return self.__Result
    
    
    