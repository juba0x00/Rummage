# Hawash, Bassel, Azab
# Darknet class is a child of internet class 


# ! Search Type (Email or Username) don't support phone number or visa card 
from modules.internet import Internet
from requests import session, get
from bs4 import BeautifulSoup
from modules.leaksfinder import LeaksFinder 
import socks
import socket
from os import system
from sys import platform
from time import sleep
from threading import Thread 



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

# ? class name(file_name.class_name)
class DarkNet(Internet):
    def __init__(self): 
        LeaksFinder.AddStatus('[-] Setting TOR Proxy [-]')
        self.session = session() # ? internet.requests.session()
        self.session.proxies["http"] = "socks5h://localhost:9050"
        self.session.proxies["https"] = "socks5h://localhost:9050"
    #   socks.set_default_proxy(proxy_type, addr, port)
        socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
        socket.socket = socks.socksocket
        self.__CheckTorConnection()
        self.__GetContent()
        
        


    def __CreateThreads(self):
        self.__GetEventThread = Thread(target=self.__Get_EVENTVALIDATION)
        self.__GetViewStatThread = Thread(target=self.__Get_VIEWSTATE)
        self.__GetViewGenThread = Thread(target=self.__Get_VIEWSTATEGENERATOR)
        self.__GetCookieThread = Thread(target=self.__GetCookies)
        self.__Threads = [self.__GetEventThread, self.__GetViewStatThread, self.__GetViewGenThread, self.__GetCookieThread]
        
        
    def __StartThreads(self):
        for thread in self.__Threads:
            thread.start()
        
        
    def __JoinThreads(self):
        for thread in self.__Threads:
            thread.join()


    # It is necessary for DNS resolution of Onion websites
    def GetAddrInfo(*args):
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

    socket.getaddrinfo = GetAddrInfo

    def __CheckTorConnection(self):
        LeaksFinder.AddStatus('[-] Checking TOR Connection [-]')
        URLs = [
            'http://leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion/LeakedPass', 
            'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/', 
            'http://freedomzw5x5tzeit4jgc3gvic3bmecje53hwcoc3nnwe2c3gsukdfid.onion/databases',
            'http://3bbad7fauom4d6sgppalyqddsqbf5u5p56b5k5uk2zxsy3d6ey2jobad.onion/'
            ]
        for URL in URLs:
            try:
                LeaksFinder.AddStatus('[-] Requesting .onion site [-]')
                get(URL)
                break
            except:
                LeaksFinder.AddStatus('[-] Try to start TOR service [-]')

                #! Show Error window "Tor is not running"
                if platform == 'linux' or platform == 'Linux':
                    try:
                        print('starting tor will stop this program ')
                        system('tor 2>/dev/null 2>&1')
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
        LeaksFinder.AddStatus('[-] Establishing TOR Connection [-]')
        res = get('http://leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion/LeakedPass')  # ? internet.requests.get()
        LeaksFinder.AddStatus('[-] Onion Site Connected [-]')
        self.__ResponseHeaders = res.headers
        self.__soup = BeautifulSoup(res.content, 'lxml') 


    def __GetCookies(self):
        LeaksFinder.AddStatus('[-] Setting session Cookies [-]')        
        SetCookie = self.__ResponseHeaders['Set-Cookie']
        SetCookie = SetCookie.split()
        
        for cookie in SetCookie:
            if cookie.__contains__('ASP.NET_SessionId'):
                self.__ASP_SessionId = cookie.split('=')[1]
            elif  cookie.__contains__('AntiXsrfToken'):
                self.__AntiXsrfToken = cookie.split('=')[1]


    def __Get_EVENTVALIDATION(self):
        LeaksFinder.AddStatus('[-] Event Validation [-]')        
        # tag = self.__soup.find('input', {'type': 'hidden', 'id': '__EVENTVALIDATION'})
        # self.__EVENTVALIDATION = tag.attrs['value']
        self.__EVENTVALIDATION = self.__soup.find('input', {'type': 'hidden', 'id': '__EVENTVALIDATION'}).attrs['value']

        
    def __Get_VIEWSTATE(self):        
        # tag = self.__soup.find('input', {'type': 'hidden', 'id': '__VIEWSTATE'})
        # self.__VIEWSTATE = tag.attrs['value']
        self.__VIEWSTATE = self.__soup.find('input', {'type': 'hidden', 'id': '__VIEWSTATE'}).attrs['value']
        
        
    def __Get_VIEWSTATEGENERATOR(self):
        # tag = self.__soup.find('input', {'type': 'hidden', 'id': '__VIEWSTATEGENERATOR'})
        # self.__VIEWSTATEGENERATOR = tag.attrs['value']
        self.__VIEWSTATEGENERATOR = self.__soup.find('input', {'type': 'hidden', 'id': '__VIEWSTATEGENERATOR'}).attrs['value']
        
        
    def Search(self):
        self.__CreateThreads()
        self.__StartThreads()
        self.__JoinThreads()
        LeaksFinder.AddStatus('[*] Start Searching in the dark web [*]')
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
                    'ctl00$ContentPlaceHolder1$TxtSearch':	LeaksFinder.GetSearchKey(),
                    'ctl00$ContentPlaceHolder1$SearchType':	LeaksFinder.GetSearchType()
                    }

        # ? 1 res = self.session.post('http://leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion/LeakedPass', data=InputData) 
        # ? 2 soup = BeautifulSoup(res.content, 'html.parser')
        # ? 3 self.__LeaksResult = soup.find('div', {'class': 'ResultPanel'})
        # ? 1+2 soup = BeautifulSoup(self.session.post('http://leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion/LeakedPass', data=InputData) .content, 'html.parser')
        res = self.session.post('http://leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion/LeakedPass', data=InputData)
        LeaksFinder.AddStatus('[-] Search Result received [-]')
        soup = BeautifulSoup(res.content, 'html.parser')
        self.__LeaksResult = soup.find('div', {'class': 'ResultPanel'})        
        # ? 1+2+3 
        self.__LeaksResult = BeautifulSoup(self.session.post('http://leakfindrg5s2zcwwdmxlvz6oefz6hdwlkckh4eir4huqcpjsefxkead.onion/LeakedPass', data=InputData).content, 'html.parser').find('div', {'class': 'ResultPanel'})
        if self.__LeaksResult:
            self.__HandleLeaks()
            LeaksFinder.AddStatus('[+] Breaches Found in the Dark web [+]')
            
        else:
            LeaksFinder.AddResult('No Leaks Found In the dark web')


    def __HandleLeaks(self):  
        for span in self.__LeaksResult.find_all('span', {'style':'display:inline-block;color:White;background-color:DarkRed;border-width:2px;border-style:Solid;'}):
            LeaksFinder.AddResult(span.contents.pop())
            LeaksFinder.IncreaseRiskLevel()