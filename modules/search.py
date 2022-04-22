from modules.leaksfinder import LeaksFinder
from modules.internet import Internet 
from modules.darknet import DarkNet
from modules.scatter import ScatterSecrets
from modules.database import Database
from modules.breachdir import BreachDir
from modules.validateinput import CheckinputType

class Search():
    
    def __init__(self):
        self.ScatterFinder = ScatterSecrets()
        self.DbFinder = Database()
        self.BreachDirFinder = BreachDir()
        self.DarkFinder = DarkNet()
        
        pass
    
    
    def StartSearch(self, SearchKey):
        SearchType = CheckinputType(SearchKey)
        # Parent = LeaksFinder() 
        LeaksFinder.SetAtrrs(SearchKey, SearchType) 
        print(self.DarkFinder.GetSearchKey)
        
        
        self.DbFinder.Search('History')
        
        if SearchType == 'Email':
            # self.ScatterFinder.Search()
            self.BreachDirFinder.Search()
            self.DarkFinder.Search()
        elif SearchType == 'Username':
            self.BreachDirFinder.Search()
            self.DarkFinder.Search()
        elif SearchType == 'PhoneNumber':
            self.DbFinder.Search(Internet.GetCountry)
            self.BreachDirFinder.Search()
        elif SearchType == 'Visa':
            self.DbFinder.Search('Visa')
        else:
            #! window error 
            pass 
        
            