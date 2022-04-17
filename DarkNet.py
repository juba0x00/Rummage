# Hawash, Bassel, Azab
# Darknet class is a child of internet class 

from internet import Internet 
import socks
import socket
import requests
from bs4 import BeautifulSoup
from os import system
from sys import platform
from time import sleep


"""
Attribues 
self.
    __ResponseHeaders (hold the cookies)
    __soup (hold the main page, EVENTVALIDATION, VIEWSTATE and VIEWSTATEGENERATOR)
    __ASP_SessionId
    __AntiXsrfToken
    __EVENTVALIDATION
    __VIEWSTATE
    __VIEWSTATEGENERATOR


"""
class DarkNet(Internet):
    def __init__(self):
        super().__init__('ewida777@gmail.com') 
        self.session = requests.session()
        self.session.proxies["http"] = "socks5h://localhost:9050"
        self.session.proxies["https"] = "socks5h://localhost:9050"
    #   socks.set_default_proxy(proxy_type, addr, port)
        socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
        socket.socket = socks.socksocket
        self.__CheckTorConnection()



    def StartSearch(self):
        self.__GetContent()
        self.__Get_EVENTVALIDATION()
        self.__Get_VIEWSTATE()
        self.__Get_VIEWSTATEGENERATOR()
        self.__GetCookies()
        self.__Scrape()
        
    # It is necessary for DNS resolution of Onion websites
    def GetAddrInfo(*args):
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

    socket.getaddrinfo = GetAddrInfo

    def __CheckTorConnection(self):
        URLs = [
            'http://freedomzw5x5tzeit4jgc3gvic3bmecje53hwcoc3nnwe2c3gsukdfid.onion/databases',
            'http://leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion/LeakedPass', 
            'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/', 
            'http://3bbad7fauom4d6sgppalyqddsqbf5u5p56b5k5uk2zxsy3d6ey2jobad.onion/'
            ]
        for URL in URLs:
            try:
                requests.get(URL)
                break
            except:
                #! Show Error window "Tor is not running"
                if platform == 'linux' or platform == 'Linux':
                    try:
                        system('systemctl start tor.service')
                        sleep(2)
                    except:
                        try:
                            system('apt install tor && systemctl start tor.service')
                            sleep(2)
                        except:
                            #! show error window "Install tor manually please before running the program (follow your distro documentation)"
                            pass
                else: 
                    #? Windows or Mac
                    #! Show Error window "please, start tor manually  before using the program"

                    pass
    
    
    def __GetContent(self):
        data = requests.get('http://leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion/LeakedPass')        
        self.__ResponseHeaders = data.headers
        self.__soup = BeautifulSoup(data.content, 'lxml')


    def __GetCookies(self):
        SetCookie = self.__ResponseHeaders['Set-Cookie']
        SetCookie = SetCookie.split()
        
        for cookie in SetCookie:
            if cookie.__contains__('ASP.NET_SessionId'):
                self.__ASP_SessionId = cookie.split('=')[1]
            elif  cookie.__contains__('AntiXsrfToken'):
                self.__AntiXsrfToken = cookie.split('=')[1]


    def __Get_EVENTVALIDATION(self):
        tag = self.__soup.find_all('input', {'type': 'hidden', 'id': '__EVENTVALIDATION'})[0]
        self.__EVENTVALIDATION = tag.get_attribute_list('value')[0]
        
        
    def __Get_VIEWSTATE(self):
        tag = self.__soup.find_all('input', {'type': 'hidden', 'id': '__VIEWSTATE'})[0]
        self.__VIEWSTATE = tag.get_attribute_list('value')[0]
        
        
    def __Get_VIEWSTATEGENERATOR(self):
        tag = self.__soup.find_all('input', {'type': 'hidden', 'id': '__VIEWSTATEGENERATOR'})[0]
        self.__VIEWSTATEGENERATOR = tag.get_attribute_list('value')[0]
        
        
    def __Scrape(self):
        LeaksHeaders = {
            
            'Host': 'leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion/LeakedPass',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion',
            'Connection': 'close',
            'Cookie': f'ASP.NET_SessionId={self.__ASP_SessionId} AntiXsrfToken={self.__AntiXsrfToken}',
            'Upgrade-Insecure-Requests':'1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1'
        }
        self.session.headers = LeaksHeaders
        InputData = {'__LASTFOCUS':	"", 
                    '__EVENTTARGET':"ctl00$ContentPlaceHolder1$BtnSearch",
                    '__EVENTARGUMENT':	"",
                    '__VIEWSTATE':	self.__VIEWSTATE,
                    '__VIEWSTATEGENERATOR':	self.__VIEWSTATEGENERATOR,
                    '__EVENTVALIDATION':	self.__EVENTVALIDATION,
                    'ctl00$ContentPlaceHolder1$TxtSearch':	self.GetSearchKey,
                    'ctl00$ContentPlaceHolder1$SearchType':	"Email"
                    }

        res = self.session.post('http://leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion/LeakedPass', data=InputData) 
        soup = BeautifulSoup(res.content, 'html.parser')
        self.__LeaksResult = soup.find_all('div', {'class': 'ResultPanel'})[0]
        if self.__LeaksResult:
            self.__HandleLeaks()
        else:
            self.AddResult('No Leaks Found')


    def __HandleLeaks(self):  
        for span in self.__LeaksResult.find_all('span', {'style':'display:inline-block;color:White;background-color:DarkRed;border-width:2px;border-style:Solid;'}):
            self.AddResult(span.contents[0])
        
        
finder = DarkNet()
