# from internet import Internet
from internet import Internet, get, loads, dump
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
        count = 100 
        MinKey = ''
        
        for key in self.__JsonKeys:
            if self.__JsonKeys[key] < count:
                count = self.__JsonKeys[key]
                MinKey = key
                
        if self.__JsonKeys[MinKey] == 50:
            #! show Error Windows "all the keys are invalid "
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
        self.AddStatus("[+] Searching in Breachdirectory.org")
        querystring = {"func": "auto", "term": f"{self.GetSearchKey}"}
        self.__AutoJsResponse = loads(get("https://breachdirectory.p.rapidapi.com/", headers=self.__BreachDirHeaders, params=querystring).text) # ? internet.json.loads
        self.__UpdateKeyCounters()
        print(self.GetStatus)
        print(self.__AutoJsResponse)
        print(self.__AutoJsResponse["success"])
        print(type(self.__AutoJsResponse["success"]))
        
        if 'message' in self.__AutoJsResponse:
            self.__GetValidKey
            self.Search()
        else:
            if self.__AutoJsResponse["success"]:
                self.__AutoJsResponse = self.__AutoJsResponse["result"] 
                self.AddResult(f"++ Passwords Found ++\n : \t\t{self.__GetPasswords}")
                self.AddResult("Source: {}".format(self.__GetSources))
            
            else:
                self.AddResult("No Breaches found in BreachDirectory")

            # print(self.GetResult)
        
        
    @property
    def __GetSources(self):
        querystring = {"func": "sources", "term": f"{self.GetSearchKey}"}
        self.__UpdateKeyCounters()
        return loads(get("https://breachdirectory.p.rapidapi.com/", headers=self.__BreachDirHeaders, params=querystring).text.replace("'", '"'))['sources'] # ? internet.json.loads()
    
    
    @property
    def __GetPasswords(self):
        passwds = []
        for breach in self.__AutoJsResponse:
            if breach["has_password"]:
                passwds.append(breach["password"])
        return passwds 
parent = Internet('mitnick@gmail.com', 'Email')
finder = BreachDir()
finder.Search()
print(finder.GetResult)