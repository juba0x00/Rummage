from modules.internet import Internet, get, BeautifulSoup, post


#!status
"""
Scatter Attributes: 
    self.
        ScatterSoup
        __ScatterResHead 
        __ScatterSession
        __ScatterCSRF
        
"""  

class ScatterSecrets(Internet):
    
    def __init__(self):
        self.__GetContent()
        self.__GetCookie()
        self.__GetCSRF()


    def __GetContent(self):
        self.AddStatus("[-] Establishing connection with Scatter Secrets.")
        res = get('https://scatteredsecrets.com/')
        self.__ScatterSoup = BeautifulSoup(res.content, 'html.parser')
        self.__ScatterResHead = res.headers
        
    def __GetCookie(self):
        self.AddStatus("[-] Create a new ScatterSecrets session.")
        self.__Session = self.__ScatterResHead['set-cookie'].split(';')[0].split('=')[1]
        
    def __GetCSRF(self):
        # tag = self.__ScatterSoup.find('input', {'type': 'hidden', 'name': 'csrf_token'})
        # self.__ScatterCSRF = tag.attrs['value']
        self.__CSRFToken = self.__ScatterSoup.find('input', {'type': 'hidden', 'name': 'csrf_token'}).attrs['value']

        
    def Search(self):
        self.AddStatus('[-] Start searching in ScaterSecrets.')
        InputHeaders = {
            "Host": "scatteredsecrets.com",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
            "Cookie": f"session={self.__Session}",
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
        content = post('https://scatteredsecrets.com/', headers=InputHeaders, data=Parameters).content
        soup = BeautifulSoup(content, 'html.parser')
        self.__Result = soup.find('small', {'class': 'alerter'}).contents
        self.__Result = self.__Result.pop()
        if self.__CheckResult:
            self.AddStatus('[+] BREACHES Found in ScatterSecrets __[+]')
            self.AddResult(self.__Result)
        else:
            self.AddStatus("[+] You're SAFE :) [+]")



    def __CheckResult(self):
        if "Bad news" in self.__Result:
            return True 
        else:
            return False