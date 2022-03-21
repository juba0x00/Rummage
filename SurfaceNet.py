# Mostafa, Omar Khaled
# surface net is a child of internet class

from internet import Internet 
import requests
import urllib
from bs4 import BeautifulSoup
class SurfaceNet(Internet):
    
    def __init(self):
        super().__init__()
        pass
    
    
    
    
    def __ScaterSecrets():
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

        SearchKey = urllib.parse.quote("user@gmail.com")
        response = requests.post('https://scatteredsecrets.com/', data={"identifier": SearchKey, "action": "search"}, headers=InputHeaders, allow_redirects=True)
        soup = BeautifulSoup(response.content, "lxml")
        print(soup.find_all('div', {"class": "alert alert-success alert-dismissible fade show"}))
  