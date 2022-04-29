from modules.leaksfinder import LeaksFinder
from modules.internet import Internet 
from modules.darknet import DarkNet
from modules.scatter import ScatterSecrets
from modules.database import Database
from modules.breachdir import BreachDir
from modules.validateinput import CheckinputType
from datetime import date 
from threading import Thread
import time

class Search():

            
            
    def __EmailSearch(self):
        self.BreachDirFinder = BreachDir()
        self.ScatterFinder = ScatterSecrets()
        self.DarkFinder = DarkNet()
        t1 = Thread(target=self.ScatterFinder.Search)
        t2 = Thread(target=self.BreachDirFinder.Search)  # ! handle 
        t3 = Thread(target=self.DarkFinder.Search)
        threads = [t1, t3] 
        for thread in threads:
            thread.start()
            
        threads.reverse()
        for thread in threads:
            thread.join()
        LeaksFinder.Done()
            
            
            
            
    
    def __UsernameSearch(self):

        self.BreachDirFinder = BreachDir()
        self.DarkFinder = DarkNet()
    

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
        start = time.time()
        
        SearchType = CheckinputType(SearchKey)

        if Internet.GetCountry != 'Israel':
            
            LeaksFinder.SetAtrrs(SearchKey, SearchType)

            self.DatabaseFinder = Database()
            
            if self.DatabaseFinder.HistorySearch():
                if not Database.TrustHistory():
                    start = time.time()
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
                                LeaksFinder.GetSearchKey(),
                                LeaksFinder.GetResult(),
                                LeaksFinder.GetSources(),
                                date.today(), 
                                LeaksFinder.GetRiskLevel()])
