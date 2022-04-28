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
from sys import platform 
from threading import Thread
from time import sleep
from os import system
class Internet():
    
    @property
    def CheckConnection(self):
        URLs = ['http://google.com',
                'http://innergrandmajesticmorning.neverssl.com/online', 
                ]
        for URL in URLs:
            if get(URL):
                return True
        return False
    
    @staticmethod
    def GetCountry():
        return get('https://am.i.mullvad.net/country').text.replace('\n', '')
    
    @staticmethod
    def check_tor_circuit():
        if platform == 'linux' or platform == 'Linux' or platform == 'Darwin':
            Thread(target= lambda: system('tor > tor_status')).start()
            sleep(1)
            last = ''

        while True:
            content = open('tor_status', 'r').readlines()
            
            if last != content[-1]:
                print(content[-1].replace('\n', ''))

            
            last = content[-1]
            if 'Bootstrapped 100%' in content[-1]:
                break
            sleep(1)
        else:
            print(RED + BOLD + 'Please start TOR before running this program' + RESET)
        