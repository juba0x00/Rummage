from modules.leaksfinder import LeaksFinder
from modules.internet import Internet 
from modules.darknet import DarkNet
from modules.scatter import ScatterSecrets
from modules.database import Database
from modules.breachdir import BreachDir
from modules.validateinput import CheckinputType
from os import getcwd
import threading 
from time import sleep

class Search():
        
    def __init__(self):
        self.__CWD = getcwd()
    def __EmailSearch(self):
        self.BreachDirFinder = BreachDir()
        self.ScatterFinder = ScatterSecrets()
        self.DarkFinder = DarkNet()
        
        t1 = threading.Thread(target=self.ScatterFinder.Search())
        t2 = threading.Thread(target=self.BreachDirFinder.Search())
        t3 = threading.Thread(target=self.DarkFinder.Search())
        threads = [t1, t2, t3]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
            
            
    
    def __UsernameSearch(self):
        t1 = threading.Thread(target=self.BreachDirFinder.Search())
        t2 = threading.Thread(target=self.DarkFinder.Search())
        t2.start()
        t1.start()
        for i in [t1, t2]:
            i.join()

    def Search(self, SearchKey):
        SearchType = CheckinputType(SearchKey)
        LeaksFinder.SetAtrrs(SearchKey, SearchType)
        
        # self.DatabaseFinder = Database()
        # self.DatabaseFinder.Search()  # ? History Search Default Database name
        
        if SearchType == 'Email':
            self.__EmailSearch()

        elif SearchType == 'Username':
            self.__UsernameSearch()
                
        # elif SearchType == 'PhoneNumber':
        #     self.DatabaseFinder.Search(Internet.GetCountry)
            
        # elif SearchType == 'Visa':
        #     self.DatabaseFinder.Search('Visa')
        else:
            # ! window error 
            pass 