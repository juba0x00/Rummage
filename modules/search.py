from modules.leaksfinder import LeaksFinder
from modules.internet import Internet 
from modules.darknet import DarkNet
from modules.scatter import ScatterSecrets
from modules.database import Database
from modules.breachdir import BreachDir
from modules.validateinput import CheckinputType
from os import getcwd
from sys import platform 
import threading 

class Search():
        
    def __init__(self):
        self.__CWD = getcwd()

    @property
    def __FileSystemStructure(self):
        if platform == 'Linux' or platform == 'linux' or 'Darwin':
            return f'{self.__CWD}/databases/'
        elif platform == 'win32' or platform == 'windows':
            return f'{self.__CWD}\databases'    
            
            
    def __EmailSearch(self):
        self.BreachDirFinder = BreachDir()
        self.ScatterFinder = ScatterSecrets()
        self.DarkFinder = DarkNet()
        
        
        t1 = threading.Thread(target=self.ScatterFinder.Search)
        t2 = threading.Thread(target=self.BreachDirFinder.Search)
        t3 = threading.Thread(target=self.DarkFinder.Search)
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

        self.DatabaseFinder = Database()
        self.DatabaseFinder.Search(f'{self.__FileSystemStructure}History')  # ? History Search Default Database name
        
        if SearchType == 'Email':
            self.__EmailSearch()

        elif SearchType == 'Username':
            self.__UsernameSearch()
                
        elif SearchType == 'PhoneNumber':
            self.DatabaseFinder.Search(f'{self.__FileSystemStructure}{Internet.GetCountry}')
            
        elif SearchType == 'Visa':
            self.DatabaseFinder.Search(f'{self.__FileSystemStructure}Visa')
        else:
            # ! window error 
            pass
        
        