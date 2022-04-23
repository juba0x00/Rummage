from modules.internet import Internet
from requests import session
from bs4 import BeautifulSoup

#!status
"""
Scatter Attributes: 
    self.
        __ScatterSoup
        __ResponseHeaders 
        __SessionVal
        __ScatterCSRF
        
        
Scatter Method:
    self.
        __GetContent()
        __GetCookie()
        __GetCSRF()
        __CheckResult
        Search()
        
"""  

class ScatterSecrets(Internet):
    
    def __init__(self):
        self.__ResponseHeaders = ""
        self.__ScatterSoup = ""
        self.__CSRFToken = ""
        self.__SessionVal = ""
        

        self.Session = session() 
        self.__GetContent()
        self.__GetCookie()
        self.__GetCSRF()


    def __GetContent(self):
        self.AddStatus("[-] Establishing connection with Scatter Secrets.")
        res = self.Session.get('https://scatteredsecrets.com/')  
        open('scatter', 'w').write(str(res.text))      
        self.__ScatterSoup = BeautifulSoup(res.content, 'html.parser')
        self.__ResponseHeaders = res.headers
        
    def __GetCookie(self):
        self.AddStatus("[-] Create a new ScatterSecrets session. [-]")
        self.__SessionVal = self.__ResponseHeaders['set-cookie'].split(';')[0].split('=')[1]
        self.Session.cookies.set('session', self.__SessionVal)
        
    def __GetCSRF(self):
        # tag = self.__ScatterSoup.find('input', {'type': 'hidden', 'name': 'csrf_token'})
        # self.__ScatterCSRF = tag.attrs['value']
        self.__CSRFToken = self.__ScatterSoup.find('input', {'type': 'hidden', 'name': 'csrf_token'}).attrs['value']

        
    def Search(self):
        self.AddStatus('[*] Start searching in ScaterSecrets. [*]')
        InputHeaders = {
            "Host": "scatteredsecrets.com",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
            # "Cookie": f"session={self.__SessionVal}",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://scatteredsecrets.com/",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://scatteredsecrets.com",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Te": "trailers"
        }

        Parameters = {"identifier" : self.GetSearchKey,
                    "csrf_token" : self.__CSRFToken,
                    "action" : "search"
                    }
        content = self.Session.post('https://scatteredsecrets.com/', headers=InputHeaders, data=Parameters, allow_redirects=True).content
        soup = BeautifulSoup(content, 'html.parser')
        self.AddStatus('[-] ScatterSecrets reponded [-]')
        self.__Result = soup.find('small', {'class': 'alerter'}).contents
        self.__Result = self.__Result.pop()
        if self.__CheckResult():
            self.AddStatus('[+] BREACHES Found in ScatterSecrets [+]')
            self.AddResult(self.__Result)
        else:
            self.AddStatus("[+] You're SAFE :) [+]")
            self.AddResult('No Breaches found in ScatterSecrets')
            
        

    def __CheckResult(self):
        if f"Bad news. Leaked passwords found for {self.GetSearchKey}." == self.__Result:
            return True 
        else:
            return False