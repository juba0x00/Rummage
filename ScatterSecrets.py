import SurfaceNet
"""
Scatter Attributes: 
    self.
        __ScatterSoup
        __ScatterResHead 
        __ScatterSession
        __ScatterCSRF
        
"""
class ScatterSecrets():
    
    def __GetScatterContent(self):
        res = SurfaceNet.internet.get('https://scatteredsecrets.com/')
        self.__ScatterSoup = SurfaceNet.internet.BeautifulSoup(res.content, 'html.parser')
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