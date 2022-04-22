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
from modules.leaksfinder import LeaksFinder
from requests import get

class Internet(LeaksFinder):
    
    @property
    def CheckConnection(self):
        URLs = ['http://google.com',
                'http://innergrandmajesticmorning.neverssl.com/online', 
                ]
        for URL in URLs:
            if get(URL):
                return True
        return False
    
    
    def GetCountry():
        return get('https://am.i.mullvad.net/country').text.replace('\n', '')
        
        
