# from internet import Internet
from modules.internet import Internet
from modules.leaksfinder import LeaksFinder 
from requests import get
from json import loads, dump 
# Breach Directory Attributes : 
#     self.
#         __JsonKeys 
#         __BreachDirHeaders
#         __AutoResponse


class BreachDir(Internet):

    def __init__(self):
        self.__JsonKeys = loads(str(open('APIkeys.json', 'r').read()))  # ? SurfaceNet.json.loads()
        self.__GetValidKey
        self.__BreachDirHeaders = {
            "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com",
            "X-RapidAPI-Key": self.__ValidKey  # ! Get your API key -> https://rapidapi.com/rohan-patra/api/breachdirectory
        }
        
        
    @property
    def __GetValidKey(self):    
        LeaksFinder.AddStatus('[-] Getting Valid API Key [-]')   
        count = 100 
        MinKey = ''
        
        for key in self.__JsonKeys:
            if self.__JsonKeys[key] < count:
                count = self.__JsonKeys[key]
                MinKey = key
                
                
        if self.__JsonKeys[MinKey] == 50:
            #! show Error Windows "all the keys are invalid "
            exit(0)
            pass 
        else:
            self.__ValidKey = MinKey
        


    def __UpdateKeyCounters(self):
        self.__JsonKeys[self.__ValidKey] += 1
        self.__UpdateKeysFile()
        
    
    
    def __UpdateKeysFile(self):
        file = open("APIkeys.json", 'w')
        dump(self.__JsonKeys, file) # ? SurfaceNet.json.dump()
        file.close()



    def Search(self):
        LeaksFinder.AddStatus("[*] Searching in Breachdirectory.org [*]")
        querystring = {"func": "auto", "term": LeaksFinder.GetSearchKey()}
        res = get("https://breachdirectory.p.rapidapi.com/", headers=self.__BreachDirHeaders, params=querystring)
        LeaksFinder.AddStatus('[-] Search Result received [-]')
        self.__AutoJsResponse = loads(res.text) # ? internet.json.loads
        self.__UpdateKeyCounters()
        
        if 'message' in str(self.__AutoJsResponse):
            self.__GetValidKey
            self.Search()
        else:
            if self.__AutoJsResponse["success"]:
                self.__AutoJsResponse = self.__AutoJsResponse["result"] 
                LeaksFinder.AddStatus('[+] Passwords Found in Breach Directory [+]')
                LeaksFinder.AddResult("Passwords Found in Breach Directory:\n ")
                for password in self.__GetPasswords:
                    LeaksFinder.AddResult(password)
                    LeaksFinder.IncreaseRiskLevel()
                
                for source in self.__GetSources:
                    LeaksFinder.AddSource(source)
                
            
            else:
                LeaksFinder.AddStatus('[+] No Breaches found in BreachDirectory [+]')
                LeaksFinder.AddResult("No Breaches found in BreachDirectory")
            
        
        
    @property
    def __GetSources(self):
        
        querystring = {"func": "sources", "term": LeaksFinder.GetSearchKey()}
        self.__UpdateKeyCounters()
        return loads(get("https://breachdirectory.p.rapidapi.com/", headers=self.__BreachDirHeaders, params=querystring).text.replace("'", '"'))['sources'] # ? internet.json.loads()
    
    
    @property
    def __GetPasswords(self):
        passwds = []
        for breach in self.__AutoJsResponse:
            if breach["has_password"]:
                passwds.append(breach["password"])
        return passwds 
    

