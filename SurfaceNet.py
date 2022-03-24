# Mostafa, Omar Khaled
# surface net is a child of internet class

from ast import In
from mimetypes import suffix_map
from internet import Internet 
from requests import get, post
import urllib
from bs4 import BeautifulSoup
import urllib.parse
import json
class SurfaceNet(Internet):
    
    def __init__(self, InputSearchKey):
        super().__init__(InputSearchKey)
        pass
    
    
    def BreachDirectory(self):
        print("Breach dir start")
        self.AddStatus('[+] Searching in Breachdirectory.org')
        
        RapidApiKeys = ['bc090afa4fmsh1deb1aab994ffb5p12e048jsnc927c98c2a5d',
                        '34e1a45867msh16add060ce84999p1f9fe5jsnde128c337105',
                        '0e3df0fcd5msh7d1569b599bf58bp12b0c5jsn4b8605776364',
                        '74360fab20msh56421029cdeba39p13c40djsnc88f2280e4da', 
                        '8f9ef0f940msh1cfa8e4b10f8b48p19602ejsnd8bd044f6294', 
                        'da867eeff1msh706cd9fcce8ff49p1f2ce3jsnb0be9592a07d',
                        '4f45d3d561mshd055852cdf78cc6p172429jsncf3f35c5eee1', 
                        '02a582a085msh21bee297c7f6280p1323d6jsnf9271ae3dd4b', 
                        'c78778644dmsh3db1e6e39db4742p16fc25jsn3f32c58bea89', 
                        '9c660e018dmsh5f9fdd95ec19278p104342jsn7785c511f062', 
                        '49fc455904msh6d2927314900e50p18e9ffjsn7e584f6c6eda',
                        '14f5f8128cmsh0a984d7c98321a2p1a4d03jsn6c1205aa2b38', 
                        'c3ac1916aemsh1424cec2d08b121p19cc23jsnafc30b272fb8', 
                        ]
        try:
            querystring = {"func":"auto","term":f"{self.GetSearchKey}"}
            
            for key in RapidApiKeys:
                headers = {
                        "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com",
                        "X-RapidAPI-Key": key  #! Get your API key -> https://rapidapi.com/rohan-patra/api/breachdirectory
                          } 
                JsonData = json.loads(get("https://breachdirectory.p.rapidapi.com/", headers=headers, params=querystring).text)
                print(JsonData)
                if 'message' in JsonData:
                    print('expired')
                else:
                    break
            if not JsonData['success']: 
                self.AddResult('No Breaches found in BreachDirectory')
            else:
                print('Breaches Found')
             
        except:
            #! Show Get_API_Keys_Window @Omar_Ameer ذ        
            return False
        
    
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
        response = post('https://scatteredsecrets.com/', data={"identifier": SearchKey, "action": "search"}, headers=InputHeaders, allow_redirects=True)
        soup = BeautifulSoup(response.content, "lxml")
        print(soup.find_all('div', {"class": "alert alert-success alert-dismissible fade show"}))
  
  
    def BreachChecker(self):
        self.SearchKey = urllib.parse.quote(self.SearchKey)
        print(self.SearchKey)
        res = get(f'http://breachchecker.com/set-account/{self.SearchKey}/', allow_redirects=True)
        soup = BeautifulSoup(res.content, "lxml")
        _, self.__BreachedRecord, self.__LastBreach = soup.find_all('div', {'class': 'font-big'})
        self.__BreachedRecord, self.__LastBreach = self.__BreachedRecord.text, self.__LastBreach.text
        self.__RiskLevel = str(str(soup.find_all('div', {"class": "progress"})).split('width:')[1])[:3]
        print(f'breach rec = {self.__BreachedRecord} \n last breach = {self.__LastBreach} \n risk = {self.__RiskLevel}')    
        
        
    def EmailRep(self):
        JsonData = json.loads(get(f'https://emailrep.io/{self.SearchKey}').content)
        print(JsonData)

        
