from modules.leaksfinder import LeaksFinder
from modules.internet import Internet 
from modules.darknet import DarkNet
from modules.scatter import ScatterSecrets
from modules.database import Database
from modules.breachdir import BreachDir
from modules.validateinput import CheckinputType
from threading import Thread
from datetime import date 
import time


class Search():

            
            
    def __EmailSearch(self):
        self.BreachDirFinder = BreachDir()
        self.ScatterFinder = ScatterSecrets()
        self.DarkFinder = DarkNet()
    
        start = time.time()



        t1 = Thread(target=self.ScatterFinder.Search)
        t2 = Thread(target=self.BreachDirFinder.Search)
        t3 = Thread(target=self.DarkFinder.Search)
        threads = [t1, t2, t3]
        
        for thread in threads:
            start = time.time()
            thread.start()
            thread.join()
            print(f'Time: {time.time() - start}')
            
        # for thread in threads:
        #     
            
            
            
    
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
        start = time.time()
        
        SearchType = CheckinputType(SearchKey)

        if Internet.GetCountry != 'Israel':
            
            LeaksFinder.SetAtrrs(SearchKey, SearchType)
            start = time.time()

            self.DatabaseFinder = Database()
            print('create db object -> Time: {} - {}'.format(time.time(), start))
            start = time.time()
            
            if self.DatabaseFinder.HistorySearch():
                print(f'history db object -> Time: {time.time() - start}')
                
                if not LeaksFinder.TrustHistory():
                    start = time.time()
                    print('before external search')
                    self.__ExternalSearch(SearchType)
                    print(f'external object -> Time: {time.time() - start}')
                    
            else:
                print('here')
                self.__ExternalSearch(SearchType)
        else:
            #ISRAEL
            pass
        print(f'search -> Time: {time.time() - start}')
        
            
            
    def __ExternalSearch(self, SearchType):
        print(f'Search type -> {SearchType}')
        if SearchType == 'Email':
            self.__EmailSearch()
        elif SearchType == 'Username':
            self.__UsernameSearch()
            
        elif SearchType == 'PhoneNumber':
            self.DatabaseFinder.Search('{}{}'.format(LeaksFinder.FileSystemStructure(), Internet.GetCountry()))
            
        elif SearchType == 'Visa':
            print(LeaksFinder.FileSystemStructure())
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
        self.DatabaseFinder.HistorySearch()
        
