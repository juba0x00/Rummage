from internet import get, BeautifulSoup
"""
Scatter Attributes: 
    self.
        __ScatterSoup
        __ScatterResHead 
        __ScatterSession
        __ScatterCSRF
        
"""    # """POST / HTTP/1.1
    # Host: scatteredsecrets.com
    # Cookie: session=ef1dd418-c60e-4e97-976b-867b88d475c9
    # User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0
    # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
    # Accept-Language: en-US,en;q=0.5
    # Accept-Encoding: gzip, deflate
    # Referer: https://scatteredsecrets.com/
    # Content-Type: application/x-www-form-urlencoded
    # Content-Length: 148
    # Origin: https://scatteredsecrets.com
    # Upgrade-Insecure-Requests: 1
    # Sec-Fetch-Dest: document
    # Sec-Fetch-Mode: navigate
    # Sec-Fetch-Site: same-origin
    # Sec-Fetch-User: ?1
    # Te: trailers
    # Connection: close
    # identifier=ewida777%40gmail.com&csrf_token=ImRmN2YwZTkxOGE2YWMyNzZhMGY2NDhmYTNiM2I4YWRkOGYyNmM2YTMi.Yl1baA.tNc00AHdlU_ZMcdtLbVDWOd76RQ&action=search"""

class ScatterSecrets():
    
    def __GetScatterContent(self):
        res = get('https://scatteredsecrets.com/')
        self.__ScatterSoup = BeautifulSoup(res.content, 'html.parser')
        self.__ScatterResHead = res.headers
        
    def __GetScatterCookie(self):
        self.__ScatterSession = self.__ScatterResHead['set-cookie'].split(';')[0].split('=')[1]

    def __GetScatterCSRF(self):
        tag = self.__ScatterSoup.find('input', {'type': 'hidden', 'name': 'csrf_token'})
        self.__ScatterCSRF = tag.attrs['value']
        
    
    def ScatterSecrets(self):
        
        InputHeaders = {
            "Host": "scatteredsecrets.com",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
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