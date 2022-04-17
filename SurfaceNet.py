# Mostafa, Omar Khaled
# surface net is a child of internet class

from internet import Internet
from requests import get, post
import urllib
from bs4 import BeautifulSoup
import urllib.parse
import json



class SurfaceNet(Internet):

    def __init__(self, InputSearchKey):
        super().__init__(InputSearchKey)
        self.__ApiKeysFile = open('APIkeys.json', 'r')
        self.__JsonKeys = json.loads(str(self.__ApiKeysFile.read()))
        self.__ValidKey = self.__GetValidKey(self.__JsonKeys)
        self.__BreachDirHeaders = {
            "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com",
            "X-RapidAPI-Key": self.__ValidKey  # ! Get your API key -> https://rapidapi.com/rohan-patra/api/breachdirectory
        }
        
        
    @staticmethod
    def __GetValidKey(keys):
        count = 100 
        MinKey = ''
        for key in keys:
            if keys[key] < count:
                count = keys[key]
                MinKey = key
        if keys[MinKey] == 50:
            #! show Error Windows "all the keys are invalid "
            pass 
        else:
            return MinKey
        

    def UpdateKeyCounters(self):
        print(self.__JsonKeys)
        self.__JsonKeys[self.__ValidKey] += 1
        print(self.__JsonKeys)
        self.__UpdateKeysFile()
        pass
    
    def __UpdateKeysFile(self):
        file = open("APIkeys.json", 'w')
        json.dump(self.__JsonKeys, file)

    def BreachDirectory(self):
        self.AddStatus("[+] Searching in Breachdirectory.org")
        querystring = {"func": "auto", "term": f"{self.GetSearchKey}"}
        res = get("https://breachdirectory.p.rapidapi.com/", headers=self.__BreachDirHeaders, params=querystring)

    
        JsonData = json.loads(res.text)
        JsonData = json.loads(res)
        if not JsonData["success"]:
            self.AddResult("No Breaches found in BreachDirectory")
        else:
            result = JsonData["result"]  # ? JsonData result value contains list with one index that holds a dictionary
            # passwd = self.__ReturnPasswd(result)
            # print(passwd)
            # self.AddResult(f"++ Breach Found ++\n Password: {passwd}")
            # self.AddResult(f"Source: {self.__()}")
    
                # {"success": True, "found": 1, "result": [{"has_password": True, "password": "1474**", "sha1": "bcb798b390b80ecefa34b6223e455dcb5b115538", "hash": "Ek2QLmXiRzh9faVY8PHgf6jAd9gwfw==", "sources": "Unverified"}]}
        # except:
        #     # ! Show Get_API_Keys_Window @Omar_Ameer
        #     return False

    def __RequestSrcs(self):
        querystring = {"func": "sources", "term": f"{self.GetSearchKey}"}
    
        res = get("https://breachdirectory.p.rapidapi.com/", headers=self.__BdirHeaders, params=querystring)
    
        JsonData = json.loads(res.text)
    
        if not JsonData["success"]:
            self.AddResult("No Source found in BreachDirectory")
        else:
            return JsonData["sources"]  # ? JsonData result value contains list with one index that holds a dictionary
    
    @staticmethod
    def __ReturnPasswd(data):
        passwds = []
        for breach in data:
            if breach["has_password"]:
                passwds.append(breach["password"])
            else:
                pass
    
    
    def __ReturnSource(self, data):
        if data["sources"] != "Unverified":
            return data["sources"]
        else:
            return self.__RequestSrcs()
        

    
    def ScaterSecrets(self):
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
        response = post("https://scatteredsecrets.com/", data={"identifier": SearchKey, "action": "search"},
                        headers=InputHeaders, allow_redirects=True)
        soup = BeautifulSoup(response.content, "lxml")
        print(soup.find_all("div", {"class": "alert alert-success alert-dismissible fade show"}))
    
    def BreachChecker(self):
        self.SearchKey = urllib.parse.quote(self.SearchKey)
        print(self.SearchKey)
        res = get(f"http://breachchecker.com/set-account/{self.SearchKey}/", allow_redirects=True)
        soup = BeautifulSoup(res.content, "lxml")
        _, self.__BreachedRecord, self.__LastBreach = soup.find_all("div", {"class": "font-big"})
        self.__BreachedRecord, self.__LastBreach = self.__BreachedRecord.text, self.__LastBreach.text
        self.__RiskLevel = str(str(soup.find_all("div", {"class": "progress"})).split("width:")[1])[:3]
        print(f"breach rec = {self.__BreachedRecord} \n last breach = {self.__LastBreach} \n risk = {self.__RiskLevel}")
    
    def EmailRep(self):
        JsonData = json.loads(get(f"https://emailrep.io/{self.SearchKey}").content)
        print(JsonData)
