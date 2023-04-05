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
from os import system, popen 
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
            

            for line in popen('tor'):
                if 'Could not bind' in line:
                    system('sudo pkill tor')
                    Internet.check_tor_circuit()
                elif 'Bootstrapped' in line:
                    percentage = line.split('%')[0].split('Bootstrapped ')[-1]
                    print(f'Establishing Tor Circuit: {percentage}', end="\r")
                    
                    if percentage == '100':
                        return True
        else:
            print(RED + BOLD + 'Please start TOR before running this program' + RESET)
        