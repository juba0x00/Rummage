from modules.leaksfinder import LeaksFinder
from modules.internet import Internet 
from modules.darknet import DarkNet
from modules.scatter import ScatterSecrets
from modules.database import Database
from modules.breachdir import BreachDir
from modules.validateinput import CheckinputType
from threading import Thread
from datetime import date 


class Search():

            
            
    def __EmailSearch(self):
        self.BreachDirFinder = BreachDir()
        self.ScatterFinder = ScatterSecrets()
        self.DarkFinder = DarkNet()
        
        
        t1 = Thread(target=self.ScatterFinder.Search)
        t2 = Thread(target=self.BreachDirFinder.Search)
        t3 = Thread(target=self.DarkFinder.Search)
        threads = [t1, t2, t3]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
            
            
    
    def __UsernameSearch(self):
        t1 = Thread(target=self.BreachDirFinder.Search)
        t2 = Thread(target=self.DarkFinder.Search)
        t2.start()
        t1.start()
        for i in [t1, t2]:
            i.join()
            
            
    def Search(self, SearchKey):
        if type(SearchKey) == str:
            self.__SingleSearch(SearchKey)
            
        elif type(SearchKey) == list:
            for key in SearchKey:
                self.__SingleSearch(key)
        

    def __SingleSearch(self, SearchKey):
        SearchType = CheckinputType(SearchKey)

        if LeaksFinder.GetCountry != 'Israel':
            
            LeaksFinder.SetAtrrs(SearchKey, SearchType)
            self.DatabaseFinder = Database()
            
            if self.DatabaseFinder.HistorySearch():
                if not LeaksFinder.TrustHistory():
                    self.__ExternalSearch(SearchType)
                    
            else:
                self.__ExternalSearch(SearchType)
        else:
            #ISRAEL
            pass
            
            
    def __ExternalSearch(self, SearchType):
        if SearchType == 'Email':
            self.__EmailSearch()
        elif SearchType == 'Username':
            self.__UsernameSearch()
            
        elif SearchType == 'PhoneNumber':
            self.DatabaseFinder.Search('{}{}'.format(LeaksFinder.FileSystemStructure(), Internet.GetCountry()))
            
        elif SearchType == 'Visa':
            self.DatabaseFinder.Search('{}Visa'.format(LeaksFinder.FileSystemStructure()))
        else:
            #! show error window 
            pass
        self.DatabaseFinder.InsertRecord([
                                self.DatabaseFinder.GetSearchKey,
                                LeaksFinder.GetResult(),
                                LeaksFinder.GetSources(),
                                date.today(), 
                                LeaksFinder.GetRiskLevel()])
        self.DatabaseFinder.HistorySearch()
        
